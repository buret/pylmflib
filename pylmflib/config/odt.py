#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package config
"""

## Function giving order in which information must be written in ODT and mapping between LMF representation and ODT (output)
def lmf_to_odt(lexicon, document, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, paradigms=False, reverse=False):
    """! @brief Function to convert LMF lexical entry information to be written into ODT commands.
    @param lexicon The Lexicon LMF instance to display.
    @param document The ODT document to fill in.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Python list. Default value is 'None', which means that the document output is alphabetically ordered.
    @param paradigms A boolean value to introduce paradigms in document or not.
    @param reverse A boolean value to set if a reverse dictionary is wanted.
    """
    pass
