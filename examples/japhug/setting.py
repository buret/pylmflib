#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf, mdf_semanticRelation
from utils.io import EOL
import output.tex as tex
from common.defs import VERNACULAR, NATIONAL, ENGLISH, REGIONAL

## To define languages and fonts
import config
FRENCH = "French"

items=lambda lexical_entry: lexical_entry.get_lexeme().replace('{', '').replace('}', '')

## Functions to process some MDF fields (input)
def remove_char(value):
    """Function to remove '_', '^', '$', '&' character at the beginning of 'lx', 'se', 'a', 'xv', 'cf' MDF fields.
    """
    return value.lstrip('_^$&')

mdf_lmf.update({
    "lx"    : lambda lx, lexical_entry: lexical_entry.set_lexeme(remove_char(lx)),
    "a"     : lambda a, lexical_entry: lexical_entry.set_variant_form(remove_char(a), type="phonetics"),
    "se"    : lambda se, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(se), mdf_semanticRelation["se"]),
    "xv"    : lambda xv, lexical_entry: lexical_entry.create_and_add_example(remove_char(xv), language=config.xml.vernacular),
    "cf"    : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(cf), mdf_semanticRelation["cf"])
})

## Functions to process some MDF fields (output)
def process_audio(lexical_entry):
    sf = []
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_audio() is not None and form_representation.get_audio().get_fileName() is not None:
            sf.append(form_representation.get_audio().get_fileName())
    return sf

lmf_mdf.update({
    "sf" : lambda lexical_entry: process_audio(lexical_entry)
})

## Functions to process some LaTeX fields (output)

def format_lexeme(lexical_entry, font):
    result = ""
    if len(lexical_entry.get_components()) != 0:
        lexeme = ""
        for component in lexical_entry.get_components():
            lexeme += component.get_lexeme() + ","
        # Remove last punctuation
        lexeme = lexeme.rstrip(",")
        # Apply font
        lexeme = font[VERNACULAR](lexeme)
    else:
        lexeme = font[VERNACULAR](lexical_entry.get_lexeme())
    if lexical_entry.is_subentry():
        result += "\\subparagraph{\\dollar\\blacksquare\\dollar "
    else:
        result += "\\vspace{0.5cm} \\paragraph{\\hspace{-0.5cm} "
    if lexical_entry.get_homonymNumber() is not None:
        # Add homonym number to lexeme
        lexeme += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    if lexical_entry.get_contextual_variations() is not None and len(lexical_entry.get_contextual_variations()) != 0:
        # Format contextual variations
        for var in lexical_entry.get_contextual_variations():
            result += " " + font[VERNACULAR](var)
        result += " (de : " + lexeme + ")."
    else:
        # Format lexeme
        result += lexeme
    for form in lexical_entry.get_variant_forms(type = "phonetics"):
        result += " / " + font[VERNACULAR](form)
    result += "} \\hypertarget{" + tex.format_uid(lexical_entry, font) + "}{}" + EOL
    if not lexical_entry.is_subentry():
        result += "\markboth{" + lexeme + "}{}" + EOL
    if len(lexical_entry.get_components()) != 0:
        # Add components part of speech
        result += "pc("
        for component in lexical_entry.get_components():
            if component.get_lexical_entry() is not None:
                result += tex.format_part_of_speech(component.get_lexical_entry(), font)
                result = result.rstrip(". ") + ", "
        # Handle last punctuation
        result = result.rstrip(", ")
        result += ("). ")
    return result

def format_notes(lexical_entry, font):
    abbreviations = dict({
    })
    result = ""
    for note in lexical_entry.find_notes(type="grammar"):
        try:
            note = abbreviations[note]
        except KeyError:
            pass
        result += "\mytextsc{" + note + "} "
    return result

def format_definitions(sense, font, languages):
    result = ""
    for language in languages:
        if len(sense.find_definitions(language)) != 0:
            for definition in sense.find_definitions(language):
                if language == config.xml.vernacular:
                    result += font[VERNACULAR](definition) + ". "
                elif language == config.xml.national:
                    result += font[NATIONAL](tex.handle_font(definition)) + ". "
                elif language == config.xml.regional:
                    # Do not display Tibetan for now (dr)
                    pass #result += "\\textit{[Regnl: " + font[REGIONAL](definition) + "]}. "
                else:
                    result += definition + ". "
        elif len(sense.find_glosses(language)) != 0:
            for gloss in sense.find_glosses(language):
                if language == config.xml.vernacular:
                    result += font[VERNACULAR](gloss) + ". "
                elif language == config.xml.national:
                    result += font[NATIONAL](tex.handle_font(gloss)) + ". "
                elif language == config.xml.regional:
                    # Do not display Tibetan for now (gr)
                    pass #result += "\\textit{[Regnl: " + font[REGIONAL](gloss) + "]}. "
                else:
                    result += gloss + ". "
        if len(sense.get_translations(language)) != 0:
            for translation in sense.get_translations(language):
                if language == config.xml.national:
                    result += font[NATIONAL](translation) + ". "
                elif language == config.xml.regional:
                    result += "\\textbf{rr:}\\textit{[Regnl: " + translation + "]}. "
                else:
                    result += translation + ". "
    return result

def format_examples(sense, font):
    result = ""
    for context in sense.get_contexts():
        result += u"\u00B6 "
        for example in context.find_written_forms(config.xml.vernacular):
            result += font[VERNACULAR](example) + EOL
        for example in context.find_written_forms(config.xml.English):
            result += example + EOL
        for example in context.find_written_forms(config.xml.national):
            result += "\\textit{" + font[NATIONAL](tex.handle_font(example)) + "}" + EOL
        for example in context.find_written_forms(config.xml.regional):
            # Do not display Tibetan for now (xr)
            pass #result += "\\textit{[" + font[REGIONAL](example) + "]}" + EOL
    return result

def format_usage_notes(sense, font):
    result = ""
    for usage in sense.find_usage_notes(language=config.xml.vernacular):
        result += "\\textit{UsageVer:} " + font[VERNACULAR](usage) + " "
    for usage in sense.find_usage_notes(language=config.xml.English):
        result += "\\textit{Usage:} " + usage + " "
    for usage in sense.find_usage_notes(language=config.xml.national):
        result += "\\textit{UsageNat:} " + font[NATIONAL](tex.handle_font(usage)) + " "
    for usage in sense.find_usage_notes(language=config.xml.regional):
        result += "\\textit{[" + font[REGIONAL](usage) + "]} "
    return result

def format_encyclopedic_informations(sense, font):
    result = ""
    for information in sense.find_encyclopedic_informations(language=config.xml.vernacular):
        result += font[VERNACULAR](information) + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.English):
        result += information + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.national):
        result += font[NATIONAL](tex.handle_font(information)) + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.regional):
        # Do not display Tibetan for now (er)
        pass #result += "\\textit{[" + font[REGIONAL](information) + "]} "
    return result

def format_paradigms(sense, font):
    from config.tex import paradigmLabel_tex
    result = ""
    current_label = None
    for paradigm in sense.get_paradigms():
        if paradigm.get_paradigmLabel() is not None and paradigm.get_paradigm(language=config.xml.vernacular) is not None:
            if paradigm.get_paradigmLabel() != current_label:
                current_label = paradigm.get_paradigmLabel()
                try:
                    label = paradigmLabel_tex[current_label]
                except KeyError:
                    label = current_label
                # Display label
                result += "\\textit{" + label + ":} "
            else:
                # Just add semi-colomn
                result += "; "
            result += font[VERNACULAR](paradigm.get_paradigm(language=config.xml.vernacular)) + " "
    return result

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf2tex(lexical_entry, font):
    tex_entry = ""
    if lmf2tex.is_first_entry:
        tex_entry += "\\setlength{\\parskip}{-0.5cm}" + EOL
        lmf2tex.is_first_entry = False
    # lexeme, id and phonetic variants
    tex_entry += format_lexeme(lexical_entry, font)
    # sound
    tex_entry += tex.format_audio(lexical_entry, font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, font)
    # grammatical notes
    tex_entry += format_notes(lexical_entry, font)
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            # In LaTeX, "\ding{202}" represents '➊' character, "\ding{203}" '➋' character, etc.
            code = 201 + int(sense.get_senseNumber())
            tex_entry += "\ding{" + str(code) + "} "
        # paradigms
        tex_entry += format_paradigms(sense, font)
        # definition/gloss and translation
        tex_entry += format_definitions(sense, font, languages=[config.xml.vernacular, config.xml.French, config.xml.national])
        # example
        tex_entry += format_examples(sense, font)
        # usage note
        tex_entry += format_usage_notes(sense, font)
        # encyclopedic information
        tex_entry += format_encyclopedic_informations(sense, font)
        # restriction
        tex_entry += tex.format_restrictions(sense, font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, font, language=config.xml.French)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, font)
    # source
    tex_entry += tex.format_source(lexical_entry, font)
    # status
    tex_entry += tex.format_status(lexical_entry, font)
    # date
    tex_entry += tex.format_date(lexical_entry, font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    # Handle reserved characters and fonts
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    return tex_entry + EOL
lmf2tex.is_first_entry = True
