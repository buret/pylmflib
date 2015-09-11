#! /usr/bin/env python

"""! @package input
"""

from config.mdf import mdf_lmf
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from utils.io import open_read, EOL, ENCODING
from utils.error_handling import Warning, Error
from utils.ipa2sampa import uni2sampa

def mdf_read(filename=None, mdf2lmf=mdf_lmf, lexicon=None, id=None, encoding=ENCODING):
    """! @brief Read an MDF file.
    @param filename The name of the MDF file to read with full path, for instance 'user/input.txt'.
    @param mdf2lmf A Python dictionary describing the mapping between MDF markers and LMF representation. Default value is 'mdf_lmf' dictionary defined in 'pylmflib/config/mdf.py'. Please refer to it as an example.
    @param lexicon An existing Lexicon to fill with lexical entries to read.
    @param id A Python string identifying the lexicon to create.
    @param encoding Use 'utf-8' encoding by default. Otherwise, user has to precise the native encoding of its document.
    @return A Lexicon instance containing all lexical entries.
    """
    import re
    # If not provided, create a Lexicon instance to contain all lexical entries
    if lexicon is None:
        lexicon = Lexicon(id)
    # Read in unicode
    if filename is None:
        filename = lexicon.get_entrySource()
    else:
        # Set lexicon attribute
        lexicon.set_entrySource(filename)
    # Read in unicode
    mdf_file = open_read(filename, encoding=encoding)
    # MDF syntax is the following: '\marker value'
    mdf_pattern = """^\\\(\w*) (<(.*)>)? ?(.*)$"""
    # Add each lexical entry to the lexicon
    current_entry = None
    sub_entry = None
    component = None
    main_entry = None
    for line in mdf_file.readlines():
        # Do not parse empty lines
        if line != EOL:
            result = re.match(mdf_pattern, line)
            if result is None:
                # Line is empty => continue parsing next line
                continue
            marker = result.group(1)
            attrs = result.group(3)
            value = result.group(4)
            # Do not consider markers starting with an underscore character (e.g. '_sh' and '_DateStampHasFourDigitYear')
            if marker[0] == '_':
                continue
            # Remove trailing spaces and end-of-line characters
            value = value.rstrip(' \r\n')
            # Do not consider empty fields
            if value == "":
                continue
            # Check if the current entry is a multiword expression
            is_mwe = False
            if marker == "lf":
                lf = value.split(" = ")
                if lf[0].startswith("Component"):
                    component_nb = lf[0].lstrip("Component")
                    value = lf[1]
                    is_mwe = True
            # 'lx' and 'se' markers indicate a new entry
            if marker == "lx" or marker == "se" or is_mwe:
                # Compute a unique identifier
                uid = uni2sampa(value)
                if marker == "se":
                    # Create a subentry
                    sub_entry = LexicalEntry(uid)
                    # An MDF subentry corresponds to an LMF lexical entry
                    mdf2lmf["lx"](value, sub_entry)
                    # Add it to the lexicon
                    lexicon.add_lexical_entry(sub_entry)
                    # Manage main entry
                    if main_entry is None:
                        main_entry = current_entry
                    else:
                        current_entry = main_entry
                    # Set main entry
                    homonym_nb = current_entry.get_homonymNumber()
                    if homonym_nb is None:
                        homonym_nb = ""
                    sub_entry.create_and_add_related_form(current_entry.get_lexeme() + homonym_nb, "main entry")
                elif is_mwe:
                    # Create a subentry
                    component = LexicalEntry(uid)
                    # An MDF subentry corresponds to an LMF lexical entry
                    mdf2lmf["lx"](value, component)
                    # Add it to the lexicon
                    lexicon.add_lexical_entry(component)
                    # Manage current entry
                    if sub_entry is not None:
                        current_entry = sub_entry
                    # Set component
                    homonym_nb = current_entry.get_homonymNumber()
                    if homonym_nb is None:
                        homonym_nb = ""
                    current_entry.create_and_add_component(component_nb, value)
                    component.create_and_add_related_form(current_entry.get_lexeme() + homonym_nb, "complex predicate")
                    component.set_independentWord(False)
                else:
                    # Create a new entry
                    current_entry = LexicalEntry(uid)
                    # Add it to the lexicon
                    lexicon.add_lexical_entry(current_entry)
                    # Reset main entry
                    main_entry = None
            # Map MDF marker and value to LMF representation
            try:
                if attrs is not None:
                    # There are attributes
                    attributes = {}
                    # Remove quotation marks from attributes if any
                    attrs = attrs.replace('"', '')
                    for attr in attrs.split(' '):
                        attributes.update({attr.split('=')[0] : attr.split('=')[1]})
                    # A customized marker starts with '__' characters
                    mdf2lmf["__" + marker](attributes, value, current_entry)
                else:
                    mdf2lmf[marker](value, current_entry)
                if sub_entry is not None:
                    current_entry = sub_entry
                    sub_entry = None
                if component is not None:
                    sub_entry = current_entry
                    current_entry = component
                    component = None
            except KeyError:
                # When printing, we need to convert 'unicode' into 'str' using 'utf-8' encoding:
                print Warning("MDF marker '%s' encountered for lexeme '%s' is not defined in configuration" % (marker.encode(ENCODING), current_entry.get_lexeme().encode(ENCODING)))
            except Error as exception:
                exception.handle()
    mdf_file.close()
    return lexicon
