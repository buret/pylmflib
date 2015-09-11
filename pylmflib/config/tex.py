#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package config
"""

from utils.io import EOL
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL

## Mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout (output)
partOfSpeech_tex = dict({
    "adjective"                     : "adj", # Leipzig, MDF
    "adposition"                    : "adp",
    "adverb"                        : "adv", # Leipzip, MDF
    "affirmative particle"          : "affm", # MDF
    "affix"                         : "aff",
    "article"                       : "art", # MDF
    "auxiliary"                     : "aux", # MDF
    "classifier"                    : "clf", # Leipzip, MDF -> CLASS
    "comparative particle"          : "cmpar", # MDF
    "conditional particle"          : "cond", # MDF
    "conjunction"                   : "cnj", # MDF
    "coordinating conjunction"      : "lnk", # MDF
    "declarative punctuation"       : "decl", # MDF
    "demonstrative determiner"      : "dem", # MDF
    "determiner"                    : "det",
    "existential pronoun"           : "exist", # MDF
    "ideophone"                     : "ideo",
    "impersonal verb"               : "vimp",
    "interjection"                  : "intj", # MDF
    "interrogative determiner"      : "int", # MDF
    "interrogative particle"        : "q", # MDF
    "intransitive verb"             : "vi", # MDF
    "modal"                         : "mdl", # MDF
    "negation"                      : "neg", # Leipzip, MDF
    "negative particle"             : "neg", # Leipzip, MDF
    "noun"                          : "n", # MDF
    "numeral"                       : "num", # MDF
    "particle"                      : "ptcl", # MDF
    "participle adjective"          : "part", # MDF
    "possessive pronoun"            : "poss", # Leipzig, MDF
    "possessive relative pronoun"   : "possr", # MDF
    "postposition"                  : "post", # MDG
    "preposition"                   : "prep", # MDF
    "presentative pronoun"          : "loc", # MDF
    "pronoun"                       : "pro", # MDF
    "proper noun"                   : "propn", # MDF
    "reciprocal pronoun"            : "rec", # MDF
    "reflexive determiner"          : "rflx", # MDF
    "reflexive verb"                : "vr", # MDF
    "relative determiner"           : "rel", # MDF
    "time noun"                     : "time", # MDF
    "transitive verb"               : "vt", # MDF
    "verb"                          : "v" # MDF
})

## Mapping between LMF paradigmLabel Paradigm attribute value and LaTeX layout (output)
paradigmLabel_tex = dict({
})

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf_to_tex(lexical_entry, font=None, partOfSpeech_mapping=partOfSpeech_tex, languages=[VERNACULAR, ENGLISH, NATIONAL, REGIONAL]):
    """! @brief Function to convert LMF lexical entry information to be written into LaTeX commands.
    @param lexical_entry The Lexical Entry LMF instance to display.
    @param font A Python dictionary describing fonts to use for different languages.
    @param partOfSpeech_mapping A Python dictionary giving abbreviations for LMF part of speech values.
    @param languages A list of languages to consider for LaTeX layout (all by default).
    @return A string representing the lexical entry in LaTeX format.
    """
    import output.tex as tex
    # Define font
    if font is None:
        font = config.xml.font
    tex_entry = ""
    # lexeme and id
    tex_entry += tex.format_lexeme(lexical_entry, font)
    # sound
    tex_entry += tex.format_audio(lexical_entry, font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, font, mapping=partOfSpeech_mapping)
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            tex_entry += sense.get_senseNumber() + ") "
        # definition/gloss and translation
        tex_entry += tex.format_definitions(sense, font, languages)
        # TODO
        tex_entry += tex.format_lt(sense, font)
        tex_entry += tex.format_sc(sense, font)
        tex_entry += tex.format_rf(sense, font)
        # example
        tex_entry += tex.format_examples(sense, font)
        # usage note
        tex_entry += tex.format_usage_notes(sense, font)
        # encyclopedic information
        tex_entry += tex.format_encyclopedic_informations(sense, font)
        # restriction
        tex_entry += tex.format_restrictions(sense, font)
    # TODO
    tex_entry += tex.format_lexical_functions(lexical_entry, font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, font)
    # variant form
    tex_entry += tex.format_variant_forms(lexical_entry, font)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, font)
    # TODO
    tex_entry += tex.format_table(lexical_entry, font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, font)
    # bibliography
    tex_entry += tex.format_bibliography(lexical_entry, font)
    # TODO
    tex_entry += tex.format_picture(lexical_entry, font)
    # notes
    tex_entry += tex.format_notes(lexical_entry, font)
    # source
    tex_entry += tex.format_source(lexical_entry, font)
    # status
    tex_entry += tex.format_status(lexical_entry, font)
    # date
    tex_entry += tex.format_date(lexical_entry, font)
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    return tex_entry + EOL
