#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package output
"""

from config.odt import lmf_to_odt
from utils.error_handling import OutputError
from utils.io import open_read

from odf.opendocument import OpenDocumentText
from odf.style import Style, TextProperties
from odf.text import H, P, Span

def file_read(filename):
    """! @brief Read file contents.
    @param filename The name of the file with full path containing information to read, for instance the text introduction of the document: 'user/config/introduction.txt'.
    @return A Python string containing read information.
    """
    contents = ""
    if filename is not None:
        file = open_read(filename)
        contents = file.read()
        file.close()
    return contents

def odt_write(object, filename, introduction=None, lmf2odt=lmf_to_odt, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, paradigms=False, reverse=False):
    """! @brief Write a document file.
    @param object The LMF instance to convert into document output format.
    @param filename The name of the document file to write with full path, for instance 'user/output.odt'.
    @param introduction The name of the text file with full path containing the introduction of the document, for instance 'user/config/introduction.txt'. Default value is None.
    @param lmf2odt A function giving the mapping from LMF representation information that must be written to ODT commands, in a defined order. Default value is 'lmf_to_odt' function defined in 'pylmflib/config/odt.py'. Please refer to it as an example.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Python list. Default value is 'None', which means that the document output is alphabetically ordered.
    @param paradigms A boolean value to introduce paradigms in document or not.
    @param reverse A boolean value to set if a reverse dictionary is wanted.
    """
    import string
    if sort_order is None:
        # Lowercase and uppercase letters must have the same rank
        sort_order = dict([(c, ord(c)) for c in string.lowercase])
        up = dict([(c, ord(c) + 32) for c in string.uppercase])
        sort_order.update(up)
        sort_order.update({'':0, ' ':0})
    textdoc = OpenDocumentText()
    # Styles
    s = textdoc.styles
    h1style = Style(name="Heading 1", family="paragraph")
    h1style.addElement(TextProperties(attributes={'fontsize':"24pt", 'fontweight':"bold" }))
    s.addElement(h1style)
    # An automatic style
    boldstyle = Style(name="Bold", family="text")
    boldprop = TextProperties(fontweight="bold", fontname="Arial", fontsize="8pt")
    boldstyle.addElement(boldprop)
    textdoc.automaticstyles.addElement(boldstyle)
    # Parse LMF values
    if object.__class__.__name__ == "LexicalResource":
        for lexicon in object.get_lexicons():
            # Document title
            h = H(outlinelevel=1, stylename=h1style, text=lexicon.get_id())
            textdoc.text.addElement(h)
            # Plain paragraph
            p = P(text=lexicon.get_label())
            # Text
            boldpart = Span(stylename=boldstyle, text="Test. ")
            p.addElement(boldpart)
            # Introduction
            if introduction is not None:
                p.addText(file_read(introduction))
                textdoc.text.addElement(p)
            # Page break
            #
            # Text body
            lmf2odt(lexicon, textdoc, items, sort_order, paradigms, reverse)
    else:
        raise OutputError(object, "Object to write must be a Lexical Resource.")
    textdoc.save(filename)
