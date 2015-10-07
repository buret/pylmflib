#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package config
"""

from config.mdf import pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from utils.error_handling import OutputError
from utils.io import ENCODING, EOL

## To define languages and fonts
import config

## Function giving order in which information must be written in docx and mapping between LMF representation and docx (output)
def lmf_to_doc(lexicon, document, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, paradigms=False, reverse=False):
    """! @brief Function to convert LMF lexical entry information to be written into docx commands.
    @param lexicon The Lexicon LMF instance to display.
    @param document The docx document to fill in.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Python list. Default value is 'None', which means that the document output is alphabetically ordered.
    @param paradigms A boolean value to introduce paradigms in document or not.
    @param reverse A boolean value to set if a reverse dictionary is wanted.
    """
    # Lexicon is already ordered
    level = 0
    previous_character = ''
    current_character = ''
    for lexical_entry in lexicon.get_lexical_entries():
        if type(sort_order) is type(dict()) or type(sort_order) is type(lambda l:l):
            # Check if current element is a lexeme starting with a different character than previous lexeme
            try:
                current_character = items(lexical_entry)[0]
                if sort_order[items(lexical_entry)[0:1]]:
                    current_character = items(lexical_entry)[0:1]
                if sort_order[items(lexical_entry)[0:2]]:
                    current_character = items(lexical_entry)[0:2]
            except IndexError:
                pass
            except KeyError:
                pass
            except TypeError:
                pass
            try:
                if ( (type(sort_order) is not type(dict())) and ((previous_character == '') or (sort_order(current_character) != sort_order(previous_character))) ) \
                    or ( (type(sort_order) is type(dict())) and (int(sort_order[current_character]) != int(sort_order[previous_character])) ):
                    # Do not consider special characters
                    if previous_character != '':
                        document.add_page_break()
                    previous_character = current_character
                    title = ''
                    if type(sort_order) is not type(dict()):
                        title += ' ' + current_character
                    else:
                        for key,value in sorted(sort_order.items(), key=lambda x: x[1]):
                            if int(value) == int(sort_order[current_character]):
                                title += ' ' + key
                    document.add_heading("-" + title + " -".decode(ENCODING), level=level+1)
            except KeyError:
                print Warning("Cannot sort item %s" % items(lexical_entry).encode(ENCODING))
            except IndexError:
                # Item is an empty string
                pass
        else:
            raise OutputError(object, "Sort order must be a dictionary.")
        if not reverse:
            # Lexeme
            lexeme = lexical_entry.get_lexeme()
            if lexical_entry.get_homonymNumber() is not None:
                # Add homonym number to lexeme
                lexeme += " (" + str(lexical_entry.get_homonymNumber()) + ")"
            # Add morphology if any
            morph = ""
            for morphology in lexical_entry.get_morphologies():
                morph += " " + morphology
            # Add dialect if any
            dialect = ""
            for sense in lexical_entry.get_senses():
                for usage_note in sense.find_usage_notes(language=config.xml.vernacular):
                    dialect += " [" + usage_note + "]"
            p = document.add_paragraph()
            p.add_run(lexeme).bold = True
            if morph != "":
                p.add_run(" Morph. :").italic = True
            p.add_run(morph)
            p.add_run(dialect)
            # Dialectal variants
            write_title = True
            for repr in lexical_entry.get_form_representations():
                if repr.get_geographicalVariant() is not None:
                    if write_title:
                        p.add_run(" Var. : ")
                        write_title = False
                    else:
                        p.add_run(" ; ")
                    p.add_run(repr.get_geographicalVariant()).bold = True
                    if repr.get_dialect() is not None:
                        p.add_run(" [" + repr.get_dialect() + "]")
            # Part of speech in italic
            if lexical_entry.get_partOfSpeech() is not None:
                p.add_run(". ")
                p.add_run(lexical_entry.get_partOfSpeech()).italic = True
            p.add_run(".")
            # Note grammaticale
            if len(lexical_entry.find_notes(type="grammar")) != 0:
                p = document.add_paragraph()
                p.add_run("  ")
                p.add_run("[Note grammaticale :")
                for note in lexical_entry.find_notes(type="grammar", language=config.xml.regional):
                    p.add_run(" ")
                    p.add_run(note).bold = True
                try:
                    for note in lexical_entry.find_notes(type="grammar", language=config.xml.French):
                        p.add_run(" ")
                        p.add_run(note)
                except AttributeError:
                    for note in lexical_entry.find_notes(type="grammar", language=config.xml.English):
                        p.add_run(" ")
                        p.add_run(note)
                for note in lexical_entry.find_notes(type="grammar", language=config.xml.vernacular):
                    p.add_run(" ")
                    p.add_run(note)
                for note in lexical_entry.find_notes(type="grammar", language=config.xml.national):
                    p.add_run(" ")
                    p.add_run(note)
                # Italic
                for note in lexical_entry.find_notes(type="grammar"):
                    p.add_run(" ")
                    p.add_run(note).italic = True
                p.add_run("].")
            for sense in lexical_entry.get_senses():
                # Glosses
                glosses = ""
                if sense.get_senseNumber() is not None:
                    p = document.add_paragraph()
                    p.add_run("  " + sense.get_senseNumber() + ")")
                for gloss in sense.find_glosses(language=config.xml.vernacular):
                    glosses += " " + gloss + "."
                if glosses == "":
                    glosses = glosses.rstrip(".")
                try:
                    for gloss in sense.find_glosses(language=config.xml.French):
                        glosses += " " + gloss + "."
                except AttributeError:
                    for gloss in sense.find_glosses(language=config.xml.English):
                        glosses += " " + gloss + "."
                glosses = glosses.rstrip(".")
                if glosses != "" and glosses[-1] != '.' and glosses[-1] != '!' and glosses[-1] != '?':
                    glosses += "."
                p.add_run(glosses)
                # Scientific name
                if lexical_entry.get_scientific_name() is not None:
                    p.add_run(" ")
                    p.add_run(lexical_entry.get_scientific_name()).italic = True
                    p.add_run(".")
                # Examples
                for context in sense.get_contexts():
                    p = document.add_paragraph()
                    examples = ""
                    vernacular_forms = context.find_written_forms(language=config.xml.vernacular)
                    for example in vernacular_forms:
                        p.add_run("  ")
                        p.add_run(example.split('[')[0]).bold = True
                        for element in example.split('[')[1:]:
                            p.add_run('[' + element)
                    try:
                        fra_forms = context.find_written_forms(language=config.xml.French)
                        if len(vernacular_forms) != 0 and len(fra_forms) != 0:
                            p.add_run(" ")
                        for example in fra_forms:
                            p.add_run(example)
                        if len(fra_forms) != 0 and fra_forms[0][-1] != '!' and fra_forms[0][-1] != '?':
                            p.add_run(".")
                    except AttributeError:
                        pass
                # Links
                if len(lexical_entry.get_related_forms("simple link")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  Voir :").italic = True
                    for related_form in lexical_entry.get_related_forms("simple link"):
                        if related_form.get_lexical_entry() is not None:
                            # TODO : hyperlink
                            pass
                        p.add_run(" ")
                        p.add_run(related_form.get_lexeme().split('[')[0]).bold = True
                        for element in related_form.get_lexeme().split('[')[1:]:
                            p.add_run('[' + element)
                        try:
                            for written_form in related_form.find_written_forms(language=config.xml.French):
                                p.add_run(" " + written_form)
                        except AttributeError:
                            for written_form in related_form.find_written_forms(language=config.xml.English):
                                p.add_run(" " + written_form)
                    p.add_run(".")
                # Notes
                if len(lexical_entry.find_notes(type="general")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note :")
                    for note in lexical_entry.find_notes(type="general"):
                        p.add_run(" ")
                        p.add_run(note)
                    p.add_run("].")
                # Note phonologique
                if len(lexical_entry.find_notes(type="phonology")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note phonologique :")
                    for note in lexical_entry.find_notes(type="phonology"):
                        p.add_run(" ")
                        p.add_run(note)
                    p.add_run("].")
                # Note anthropologique
                if len(lexical_entry.find_notes(type="anthropology")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note anthropologique :")
                    for note in lexical_entry.find_notes(type="anthropology"):
                        p.add_run(" ")
                        p.add_run(note)
                        p.add_run("].")
            if paradigms:
                if len(lexical_entry.get_word_forms()) != 0:
                    # Intense quote
                    document.add_paragraph('Paradigms', style='IntenseQuote')
                    # Table
                    table = document.add_table(rows=1, cols=2)
                    hdr_cells = table.rows[0].cells
                    hdr_cells[0].text = 'Paradigm'
                    hdr_cells[1].text = 'Form'
                for item in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["sg"]):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "sg"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["pl"]):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "pl"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4s"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4d"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1e"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "1i"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "2p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "3p"
                    row_cells[1].text = item
                for item in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']):
                    row_cells = table.add_row().cells
                    row_cells[0].text = "4p"
                    row_cells[1].text = item
                if len(lexical_entry.get_word_forms()) != 0:
                    p = document.add_paragraph()
            # Handle subentries
            for related_form in lexical_entry.get_related_forms("subentry"):
                if related_form.get_lexical_entry() is not None:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run(related_form.get_lexeme().split('[')[0]).bold = True
                    for element in related_form.get_lexeme().split('[')[1:]:
                        p.add_run('[' + element.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"))
                    for sense in related_form.get_lexical_entry().get_senses():
                        glosses = ""
                        for gloss in sense.find_glosses(language=config.xml.vernacular):
                            glosses += " " + gloss + "."
                        if glosses == "":
                            glosses = glosses.rstrip(".")
                        try:
                            for gloss in sense.find_glosses(language=config.xml.French):
                                glosses += " " + gloss + "."
                        except AttributeError:
                            for gloss in sense.find_glosses(language=config.xml.English):
                                glosses += " " + gloss + "."
                        if glosses == "":
                            glosses = glosses.rstrip(".")
                        p.add_run(glosses)
            p.add_run(EOL)
        else: # reverse
            # English gloss
            is_gloss = False
            for sense in lexical_entry.get_senses():
                for gloss in sense.find_glosses(language=config.xml.English):
                    if not is_gloss:
                        # Paragraph
                        p = document.add_paragraph()
                        # Write gloss in bold, except characters that are between brackets or square brackets
                        brackets = 0
                        bold = True
                        for c in gloss:
                            if c == '(' or c == '[':
                                # Write following characters in non-bold
                                brackets += 1
                                if brackets > 0:
                                    bold = False
                                else:
                                    bold = True
                                p.add_run(c).bold = bold
                            elif c == ')' or c == ']':
                                # Write following characters in bold
                                p.add_run(c).bold = bold
                                brackets -= 1
                                if brackets > 0:
                                    bold = False
                                else:
                                    bold = True
                            else:
                                p.add_run(c).bold = bold
                        if gloss[-1] != '?' and gloss[-1] != '!' and gloss[-1] != '.':
                            p.add_run(".")
                        p.add_run(" ")
                        is_gloss = True
            if is_gloss:
                # Scientific name
                if lexical_entry.get_scientific_name() is not None:
                    p.add_run(lexical_entry.get_scientific_name()).italic = True
                    p.add_run(". ")
                # Lexeme
                p.add_run(lexical_entry.get_lexeme())
                if lexical_entry.get_lexeme()[-1] != '?' and lexical_entry.get_lexeme()[-1] != '!' and lexical_entry.get_lexeme()[-1] != '.':
                    p.add_run(".")
