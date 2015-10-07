#! /usr/bin/env python

"""! @pmodule wrapper Contains one main function, wrapper_rw(), which runs another function which should be a user function. If the library raises an exception, wrapper_rw() will restore the terminal to a sane state so you can read the resulting traceback.
"""

__version__ = '1.0'

# Add pylmflib/pylmflib/ folder to path
import sys
sys.path.append('./pylmflib')

## Functions to read from a file: MDF, XML LMF, sort order, XML config
from input.mdf import mdf_read
from input.xml_lmf import xml_lmf_read as lmf_read
from config.xml import sort_order_read as order_read
from config.xml import config_read

## Functions to write into a file: MDF, XML LMF, LaTeX, doc
from output.mdf import mdf_write
from output.xml_lmf import xml_lmf_write as lmf_write
from output.tex import tex_write

from utils.error_handling import Error
from utils.log import log

## Module variable
lexical_resource = None

def wrapper_rw(func, *args, **kwds):
    """! @brief Wrapper function that calls another function, restoring normal behavior on error.
    @param func Callable object.
    @param args Arguments passed to 'func' as its first argument.
    @param kwds Other arguments passed to 'func'.
    """
    import wrapper
    ## As this is a user function, it is executed under 'try' statement to catch and handle exceptions
    try:
        object = func(*args, **kwds)
        if object.__class__.__name__ == "LexicalResource":
            wrapper.lexical_resource = object
            return object
        elif object.__class__.__name__ == "Lexicon":
            from core.lexical_resource import LexicalResource
            if wrapper.lexical_resource is None:
                # Create a Lexical Resource only once
                wrapper.lexical_resource = LexicalResource()
            # Attach lexicon to the lexical resource if not yet done
            if wrapper.lexical_resource.get_lexicon(object.get_id()) is None:
                wrapper.lexical_resource.add_lexicon(object)
            return wrapper.lexical_resource
        elif type(object) == type(dict()) or type(object) == type(tuple()):
            return object
    except Error as exception:
        ## A library error has occured
        exception.handle()
    except SystemExit:
        ## The library decided to stop execution
        raise
    except:
        ## A system error has occured
        import sys
        sys.stderr.write("Unexpected error: " + str(sys.exc_info()[0]) + "\n")
        raise
    else:
        ## Nominal case
        pass
    finally:
        ## Set everything back to normal and release created objects if any
        pass

def read_mdf(*args, **kwds):
    import wrapper
    # To access options
    from pylmflib import options
    global options
    # Find lexicon configuration if any
    try:
        id = kwds['id']
    except KeyError:
        id = None
    if id is not None and wrapper.lexical_resource is not None:
        lexicon = wrapper.lexical_resource.get_lexicon(id)
        # Add lexicon argument
        kwds.update({'lexicon': lexicon})
    # An MDF file contains one lexicon only, but wrapper_rw() function encapsulates it into a lexical resource
    lexical_resource = wrapper_rw(mdf_read, *args, **kwds)
    for lexicon in lexical_resource.lexicon:
        if options.cross_references:
            # Verify lexicon coherence
            lexicon.check_cross_references()
        log("Successfully created %s LMF entries from MDF file '%s'." % (lexicon.count_lexical_entries(), lexicon.get_entrySource()))
    return lexical_resource

def read_xml_lmf(*args, **kwds):
    # To access options
    from pylmflib import options
    global options
    # An XML LMF file contains one lexical resource, itself containing lexicon(s)
    lexical_resource = wrapper_rw(lmf_read, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in lexical_resource.get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
        if options.cross_references:
            # Verify lexicon coherence
            lexicon.check_cross_references()
    log("Successfully created %s LMF entries from XML LMF file '%s'." % (entries_nb, args[0]))
    return lexical_resource

def read_sort_order(*args, **kwds):
    sort_order = wrapper_rw(order_read, *args, **kwds)
    log("Successfully read sort order: " + str(sort_order))
    return sort_order

def read_config(*args, **kwds):
    lexical_resource = wrapper_rw(config_read, *args, **kwds)
    log("Successfully read config")
    return lexical_resource

def write_mdf(*args, **kwds):
    # As an MDF file can only contain one lexicon, create as many MDF files as lexicons in the lexical resource (TODO: rename files)
    for lexicon in args[0].get_lexicons():
        wrapper_rw(mdf_write, lexicon, *args[1:], **kwds)
        log("Successfully wrote %s LMF entries into MDF file '%s'." % (lexicon.count_lexical_entries(), args[1]))

def write_xml_lmf(*args, **kwds):
    # An XML LMF file contains one lexical resource, itself containing lexicon(s)
    wrapper_rw(lmf_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into XML LMF file '%s'." % (entries_nb, args[1]))

def write_tex(*args, **kwds):
    # A LaTeX file contains one or several lexicons and informations about the lexical resource
    wrapper_rw(tex_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into LaTeX file '%s'." % (entries_nb, args[1]))

def write_doc(*args, **kwds):
    # Import only when needed because it requires installation of Python package 'docx'
    from output.doc import doc_write
    # A document file contains one or several lexicons and informations about the lexical resource
    wrapper_rw(doc_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into document file '%s'." % (entries_nb, args[1]))

def write_odt(*args, **kwds):
    # Import only when needed because it requires installation of Python package 'odf'
    from output.odt import odt_write
    # A document file contains one or several lexicons and informations about the lexical resource
    wrapper_rw(odt_write, *args, **kwds)
    # Count total number of entries to report to user
    entries_nb = 0
    for lexicon in args[0].get_lexicons():
        entries_nb += lexicon.count_lexical_entries()
    log("Successfully wrote %s LMF entries into document file '%s'." % (entries_nb, args[1]))
