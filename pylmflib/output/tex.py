#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package output
"""

from config.tex import lmf_to_tex, partOfSpeech_tex
from config.mdf import mdf_semanticRelation, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from utils.io import open_read, open_write, EOL, ENCODING
from utils.error_handling import OutputError, Warning
from common.defs import VERNACULAR, ENGLISH, NATIONAL, REGIONAL

# To define languages and fonts
import config

def file_read(filename):
    """! @brief Read file contents.
    @param filename The name of the file with full path containing information to read, for instance the LaTeX header of the document: 'user/config/header.tex'.
    @return A Python string containing read information.
    """
    contents = ""
    if filename is not None:
        file = open_read(filename)
        contents = file.read()
        file.close()
    return contents

def insert_references(lexical_entry):
    """! @brief Insert references to paradigms.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @return A string representing the references in LaTeX format.
    """
    text = ""
    part_of_speech = lexical_entry.get_partOfSpeech()
    spelling_variant = None
    if len(lexical_entry.get_spelling_variants()) != 0:
        spelling_variant = lexical_entry.get_spelling_variants()[0]
    if spelling_variant is None:
        # If current entry is a subentry, then take the spelling variant of the main entry
        main_entry = lexical_entry.get_main_entry()
        if main_entry is not None:
            if len(main_entry.get_spelling_variants()) != 0:
                spelling_variant = main_entry.get_spelling_variants()[0]
    if spelling_variant is not None:
        if part_of_speech == "transitive verb":
            text += "\\hfill\\break See: \\ref{" + spelling_variant + ".vt}" + EOL
            text += "\\ref{" + spelling_variant + ".vt.eng}" + EOL
        elif part_of_speech == "intransitive verb":
            text += "\\hfill\\break See: \\ref{" + spelling_variant + ".vi}" + EOL
            text += "\\ref{" + spelling_variant + ".vi.eng}" + EOL
        elif part_of_speech == "reflexive verb":
            text += "\\hfill\\break See: \\ref{" + spelling_variant + ".vr}" + EOL
            text += "\\ref{" + spelling_variant + ".vr.eng}" + EOL
    return text

def tex_write(object, filename, preamble=None, introduction=None, lmf2tex=lmf_to_tex, font=None, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, paradigms=[], tables=[], title=None, tex_language=None):
    """! @brief Write a LaTeX file.
    Note that the lexicon must already be ordered at this point. Here, parameters 'items' and 'sort_order' are only used to define chapters.
    @param object The LMF instance to convert into LaTeX output format.
    @param filename The name of the LaTeX file to write with full path, for instance 'user/output.tex'.
    @param preamble The name of the LaTeX file with full path containing the LaTeX header of the document, for instance 'user/config/japhug.tex'. Default value is None.
    @param introduction The name of the LaTeX file with full path containing the LaTeX introduction of the document, for instance 'user/config/introduction.tex'. Default value is None.
    @param lmf2tex A function giving the mapping from LMF representation information that must be written to LaTeX commands, in a defined order. Default value is 'lmf_to_tex' function defined in 'pylmflib/config/tex.py'. Please refer to it as an example.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Default value is 'None', which means that the LaTeX output is alphabetically ordered.
    @param paradigms A Python list of LaTeX filenames with full path containing the paradigms in LaTeX format. Default value is an empty list.
    @param tables The name of the LaTeX file with full path containing some notes to add at the end of the LaTeX document, for instance 'user/config/conclusion.tex'. Default value is None.
    @param title A Python string containing the title of the LaTeX document. Default value is None.
    @param tex_language A Python string giving the default language to set in LaTeX.
    """
    import string, os
    # Define font
    if font is None:
        font = config.xml.font
    tex_file = open_write(filename)
    # Add file header if any
    tex_file.write(file_read(preamble))
    # Continue the header if needed
    if title is not None:
        tex_file.write("\\title{" + title + "}" + EOL)
    if tex_language is not None:
        tex_file.write("\setdefaultlanguage{" + tex_language + "}" + EOL)
    # Insert LaTeX commands to create a document
    tex_file.write(EOL + "\\begin{document}" + EOL)
    tex_file.write("\\maketitle" + EOL)
    tex_file.write("\\newpage" + EOL)
    # Add introduction if any
    if introduction is not None:
        tex_file.write("\\markboth{INTRODUCTION}{}" + EOL * 2)
    tex_file.write(file_read(introduction))
    # Add command for small caps
    tex_file.write(EOL + "\\def\\mytextsc{\\bgroup\\obeyspaces\\mytextscaux}" + EOL)
    tex_file.write("\\def\\mytextscaux#1{\\mytextscauxii #1\\relax\\relax\\egroup}" + EOL)
    tex_file.write("\\def\\mytextscauxii#1{%" + EOL)
    tex_file.write("\\ifx\\relax#1\\else \\ifcat#1\\@sptoken{} \\expandafter\\expandafter\\expandafter\\mytextscauxii\\else" + EOL)
    tex_file.write("\\ifnum`#1=\\uccode`#1 {\\normalsize #1}\\else {\\footnotesize \\uppercase{#1}}\\fi \\expandafter\\expandafter\\expandafter\\mytextscauxii\\expandafter\\fi\\fi}" + EOL * 2)
    # Configure space indent
    tex_file.write("\\setlength\\parindent{0cm}" + EOL)
    # Insert data path configuration
    # Unix-style paths
    audio_path = config.xml.audio_path
    graphic_path = os.path.abspath('.')
    if os.name != 'posix':
        # Windows-style paths
        audio_path = audio_path.replace("\\", "/")
        graphic_path = graphic_path.replace("\\", "/")
    tex_file.write(EOL + "\\addmediapath{" + audio_path.rstrip("/") + "}" + EOL)
    tex_file.write("\\addmediapath{" + audio_path + "mp3}" + EOL)
    tex_file.write("\\addmediapath{" + audio_path + "wav}" + EOL)
    tex_file.write("\\graphicspath{{" + graphic_path + "/pylmflib/output/img/}}" + EOL * 2)
    # Configure 2 columns
    tex_file.write("\\newpage" + EOL)
    tex_file.write("\\begin{multicols}{2}" + EOL * 2)
    if sort_order is None:
        # Lowercase and uppercase letters must have the same rank
        sort_order = dict([(c, ord(c)) for c in string.lowercase])
        up = dict([(c, ord(c) + 32) for c in string.uppercase])
        sort_order.update(up)
        sort_order.update({'':0, ' ':0})
    # For each element to write, get the corresponding LMF value
    if object.__class__.__name__ == "LexicalResource":
        for lexicon in object.get_lexicons():
            previous_character = ''
            current_character = ''
            # Lexicon is already ordered
            for lexical_entry in lexicon.get_lexical_entries():
                # Consider only main entries (subentries and components will be written as parts of the main entry)
                if lexical_entry.find_related_forms("main entry") == [] and lexical_entry.get_independentWord() is not False:
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
                            previous_character = current_character
                            tex_file.write("\\newpage" + EOL)
                            title = ''
                            if type(sort_order) is not type(dict()):
                                title += ' ' + font[NATIONAL](current_character)
                            else:
                                for key,value in sorted(sort_order.items(), key=lambda x: x[1]):
                                    if int(value) == int(sort_order[current_character]):
                                        title += ' ' + font[VERNACULAR](key)
                            tex_file.write("\\section*{\\centering-" + handle_reserved(title) + " -}" + EOL)
                            #tex_file.write("\\pdfbookmark[1]{" + title + " }{" + title + " }" + EOL)
                        tex_file.write(lmf2tex(lexical_entry, font))
                        if len(paradigms) != 0:
                            tex_file.write(insert_references(lexical_entry))
                        tex_file.write("\\lhead{\\firstmark}" + EOL)
                        tex_file.write("\\rhead{\\botmark}" + EOL)
                        # Separate lexical entries from each others with a blank line
                        tex_file.write(EOL)
                        # Handle subentries
                        for related_form in lexical_entry.get_related_forms("subentry"):
                            if related_form.get_lexical_entry() is not None:
                                tex_file.write(lmf2tex(related_form.get_lexical_entry(), font))
                                if len(paradigms) != 0:
                                    tex_file.write(insert_references(related_form.get_lexical_entry()))
                                # Separate sub-entries from each others with a blank line
                                tex_file.write(EOL)
                    except KeyError:
                        print Warning("Cannot sort item %s" % items(lexical_entry).encode(ENCODING))
                    except IndexError:
                        # Item is an empty string
                        pass
    else:
        raise OutputError(object, "Object to write must be a Lexical Resource.")
    # Insert LaTeX commands to finish the document properly
    tex_file.write("\end{multicols}" + EOL)
    # Insert paradigms if any
    for filename in paradigms:
        tex_file.write(EOL)
        tex_file.write("\\newpage" + EOL)
        tex_file.write("\markboth{paradigms}{}" + EOL)
        tex_file.write(file_read(filename))
        tex_file.write(EOL)
    # Insert other tables if any
    for filename in tables:
        tex_file.write(EOL)
        tex_file.write("\\newpage" + EOL)
        tex_file.write(file_read(filename))
        tex_file.write(EOL)
    tex_file.write("\end{document}" + EOL)
    tex_file.close()

## Functions to process LaTeX layout

def handle_font(text):
    """Replace '{xxx}' by '\ipa{xxx}' in 'un', 'xn', 'gn', 'dn', 'en'.
    """
    import re
    pattern = r"([^\\\|]*){([^}]*)}(.*)"
    while re.match(pattern, text):
        text = re.sub(pattern, r"\1" + r"\\ipa{" + r"\2" + "}" + r"\3", text)
    return text

def handle_reserved(text):
    """ Handle reserved characters $ & % # _ ^ except \ { }.
    """
    if text.find("$") != -1:
        text = text.replace('$', '\$')
    # In some LaTeX commands, '$' must not be replaced by '\$' => marked as '\\dollar' in this case
    if text.find("\\dollar") != -1:
        text = text.replace("\\dollar", '$')
    if text.find("& ") != -1:
        text = text.replace('& ', '\& ')
    if text.find("%") != -1:
        text = text.replace('%', '\%')
    if text.find("#") != -1:
        text = text.replace('#', '\#')
    if text.find("_") != -1:
        text = text.replace('_', "\string_")
    if text.find("^") != -1:
        text = text.replace('^', "U+005E")
    return text

def handle_fi(text):
    """Replace 'fi:xxx' and '|fi{xxx}' by \\textit{xxx}.
    """
    import re
    if text.find("fi:") != -1:
        pattern = r"(\w*)fi:([^\s\.,)]*)(\w*)"
        text = re.sub(pattern, r"\1" + r"\\textit{" + r"\2" + "}" + r"\3", text)
    if text.find("|fi{") != -1:
        pattern = r"(\w*)\|fi{([^}]*)}(\w*)"
        text = re.sub(pattern, r"\1" + r"\\textit{" + r"\2" + "}" + r"\3", text)
    return text

def handle_fv(text, font):
    """Replace 'fv:xxx' and '|fv{xxx}' by font[VERNACULAR](xxx).
    """
    import re
    if text.find("fv:") != -1:
        #pattern = r"(.*[ }])?fv:([^\s\.,)]*)(.*)"
        pattern = r"(\w*)fv:([^\s\.,)]*)(\w*)"
        text = re.sub(pattern, r"\1" + r"%s" % font[VERNACULAR](r"\2").replace('\\', r'\\').replace(r'\\2', r"\2") + r"\3", text)
    if text.find("|fv{") != -1:
        pattern = r"(\w*)\|fv{([^}]*)}(\w*)"
        text = re.sub(pattern, r"\1" + r"%s" % font[VERNACULAR](r"\2").replace('\\', r'\\').replace(r'\\2', r"\2") + r"\3", text)
    return text

def handle_fn(text, font):
    """Replace 'fn:xxx' and '|fn{xxx}' by font[NATIONAL](xxx).
    """
    import re
    if text.find("fn:") != -1:
        pattern = r"(\w*)fn:([^\s\.,)]*)(\w*)"
        text = re.sub(pattern, r"\1" + r"%s" % font[NATIONAL](r"\2").replace('\\', r'\\').replace(r'\\2', r"\2") + r"\3", text)
    if text.find("|fn{") != -1:
        pattern = r"(\w*)\|fn{([^}]*)}(\w*)"
        text = re.sub(pattern, r"\1" + r"%s" % font[NATIONAL](r"\2").replace('\\', r'\\').replace(r'\\2', r"\2") + r"\3", text)
    return text

def handle_pinyin(text):
    """Replace '@xxx' by '\\textcolor{gray}{xxx}' in 'lx', 'dv', 'xv' fields (already in API).
        """
    import re
    if text.find("@") != -1:
        text = re.sub(r"(\w*)@(\w*)", r"\1" + r"\\textcolor{gray}{" + r"\2" + "}", text)
    return text

def handle_caps(text):
    """Handle small caps.
    Replace '°xxx' by '\textsc{xxx}' in translated examples.
    """
    import re
    if text.encode("utf8").find("°") != -1:
        # LaTeX does not support '#' nor '_' characters inside '\mytextsc' command
        text = re.sub(r"(\w*)°([^\s\.,)+/:\#\_]*)(\w*)", r"\1" + r"\\textsc{" + r"\2" + "}" + r"\3", text.encode("utf8")).decode("utf8")
    return text

def handle_quotes(text):
    """Hanlde quotation marks.
    Replace each "xxx" by ``xxx".
    """
    import re
    pattern = r"""^([^\"]*)\"([^\"]*)\".*"""
    result = re.match(pattern, text)
    end = text
    text = ""
    while result:
        text += result.group(1) + r"``" + result.group(2) + "\""
        end = end.replace(result.group(1) + "\"" + result.group(2) + "\"", "")
        result = re.match(pattern, end)
    text += end
    return text

## Functions to process LaTeX fields (output)

def format_uid(lexical_entry, font):
    """! @brief Transform unique identifier of a lexical entry in ASCII format.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing the unique identifier in LaTeX format.
    """
    # LaTeX does not handle '\' (backslash), '{' (left brace) and '{' (right brace) characters in links
    text = lexical_entry.get_id()
    if text.find("\\") != -1:
        text = text.replace('\\', u"£")
    if text.find("{") != -1:
        text = text.replace('{', '\{')
    if text.find("}") != -1:
        text = text.replace('}', '\}')
    return text

def format_link(lexical_entry, font):
    """! @brief Display hyperlink to a lexical entry in LaTeX format.
    @param lexical_entry The targeted Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing the hyperlink in LaTeX format.
    """
    result = "\\hyperlink{" + format_uid(lexical_entry, font) + "}{" + font[VERNACULAR](lexical_entry.get_lexeme())
    if lexical_entry.get_homonymNumber() is not None:
        result += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    result += "}"
    return result

def format_lexeme(lexical_entry, font):
    """! @brief 'lx', 'hm' and 'lc' fields are flipped if 'lc' field has data.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing lexeme in LaTeX format.
    """
    result = ""
    lexeme = font[VERNACULAR](lexical_entry.get_lexeme())
    if lexical_entry.is_subentry():
        result += "\\subparagraph{\\dollar\\blacksquare\\dollar "
    else:
        result += "\\paragraph{\\hspace{-0.5cm} "
    if lexical_entry.get_homonymNumber() is not None:
        # Add homonym number to lexeme
        lexeme += " \\textsubscript{" + str(lexical_entry.get_homonymNumber()) + "}"
    if lexical_entry.get_contextual_variations() is not None and len(lexical_entry.get_contextual_variations()) != 0:
        # Format contextual variations
        for var in lexical_entry.get_contextual_variations():
            result += " " + font[VERNACULAR](var)
        result += " (from: " + lexeme + ")."
    else:
        # Format lexeme
        result += lexeme
    result += "} \\hypertarget{" + format_uid(lexical_entry, font) + "}{}" + EOL
    if not lexical_entry.is_subentry():
        result += "\markboth{" + lexeme + "}{}" + EOL
    return result

def format_audio(lexical_entry, font):
    """! @brief Embed sound file into PDF.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string embedding sound in LaTeX format.
    """
    import os
    from os.path import basename, isfile
    # To access options
    from pylmflib import options
    global options
    result = ""
    if not options.audio:
        return result
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_audio() is not None:
            # Embed local sound file
            # \includemedia[<options>]{<poster text>}{<main Flash (SWF) file or URL  |  3D (PRC, U3D) file>}
            # To include audio file in PDF, replace WAV extension by MP3 extension and search in audio, MP3 and WAV folders
            file_name = form_representation.get_audio().get_fileName().replace(".wav", ".mp3")
            file_path = []
            if os.name == 'posix':
                # Unix-style paths
                file_path.append(config.xml.audio_path + file_name)
                file_path.append(config.xml.audio_path + "mp3/" + file_name)
                file_path.append(config.xml.audio_path + "wav/" + file_name)
            else:
                # Windows-style paths
                audio_path = config.xml.audio_path.replace("/", "\\")
                file_path.append(audio_path + file_name)
                file_path.append(audio_path + "mp3\\" + file_name)
                file_path.append(audio_path + "wav\\" + file_name)
            exist = False
            for audio_file in file_path:
                if isfile(audio_file):
                    exist = True
                    break
            if not exist:
                print Warning("Sound file '%s' encountered for lexeme '%s' does not exist" % (file_name.encode(ENCODING), lexical_entry.get_lexeme().encode(ENCODING)))
                return result
            file_name = file_name.replace('-', '\string-')
            result += "\includemedia[" + EOL +\
                "\taddresource=" + file_name + "," + EOL +\
                "\tflashvars={" + EOL +\
                    "\t\tsource=" + file_name + EOL +\
                    "\t\t&autoPlay=true" + EOL +\
                    "\t\t&autoRewind=true" + EOL +\
                    "\t\t&loop=false" + EOL +\
                    "\t\t&hideBar=true" + EOL +\
                    "\t\t&volume=1.0" + EOL +\
                    "\t\t&balance=0.0" + EOL +\
                "}]{\includegraphics[scale=0.5]{sound.jpg}}{APlayer.swf}"
            # \mediabutton[<options>]{<normal button text or graphic>}
            result += " \\hspace{0.1cm}" + EOL
    return result

def format_part_of_speech(lexical_entry, font, mapping=partOfSpeech_tex, language=None):
    """! @brief Display part of speech in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @param mapping A Python dictionary giving the mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout.
    @param language Language to consider to display part of speech.
    @return A string representing part of speech in LaTeX format.
    """
    result = ""
    if lexical_entry.get_partOfSpeech() is not None:
        try:
            if language is None:
                result += "\\textit{" + mapping[lexical_entry.get_partOfSpeech()] + "}. "
            else:
                result += "\\textit{" + mapping[(language, lexical_entry.get_partOfSpeech())] + "}. "
        except KeyError:
            print Warning("Part of speech value '%s' encountered for lexeme '%s' is not defined in configuration" % (lexical_entry.get_partOfSpeech().encode(ENCODING), lexical_entry.get_lexeme().encode(ENCODING)))
    return result

def format_definitions(sense, font, languages=None):
    """! @brief Glosses are supplanted by definitions.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @param languages A list of languages to consider for definitions and glosses (all by default).
    @return A string representing glosses and definitions in LaTeX format.
    """
    result = ""
    if languages is None:
        languages = [config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional]
    for language in languages:
        if len(sense.find_definitions(language)) != 0:
            for definition in sense.find_definitions(language):
                if language == config.xml.vernacular:
                    result += font[VERNACULAR](definition) + ". "
                elif language == config.xml.national:
                    result += font[NATIONAL](handle_font(definition)) + ". "
                elif language == config.xml.regional:
                    result += "\\textit{[Regnl: " + font[REGIONAL](definition) + "]}. "
                else:
                    result += definition + ". "
        elif len(sense.find_glosses(language)) != 0:
            for gloss in sense.find_glosses(language):
                if language == config.xml.vernacular:
                    result += font[VERNACULAR](gloss) + ". "
                elif language == config.xml.national:
                    result += font[NATIONAL](handle_font(gloss)) + ". "
                elif language == config.xml.regional:
                    result += "\\textit{[Regnl: " + font[REGIONAL](gloss) + "]}. "
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

def format_lt(sense, font):
    """! @brief Display 'lt' in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'lt' in LaTeX format.
    """
    # return "\\textit{Lit:} " + u"\u2018" + sense.get_lt() + u"\u2019" + ". "
    return ""

def format_sc(sense, font):
    """! @brief Display 'sc' in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'sc' in LaTeX format.
    """
    # return "\\textit{\uline{" + sense.get_sc() + "}}. "
    return ""

def format_rf(sense, font):
    """! @brief Display 'rf' in LaTeX format.
    @param lexical_entry The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing 'rf' in LaTeX format.
    """
    # return "\\textit{Ref:} " + sense.get_rf() + " "
    return ""

def format_examples(sense, font, languages=None):
    """! @brief Display examples in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @param languages A list of languages to consider for examples (all by default).
    @return A string representing examples in LaTeX format.
    """
    result = ""
    if languages is None:
        languages = [config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional]
    for context in sense.get_contexts():
        tmp = ""
        for language in languages:
            for example in context.find_written_forms(language):
                if language == config.xml.vernacular:
                    tmp += "\\sn " + font[VERNACULAR](example) + EOL
                elif language == config.xml.national:
                    tmp += "\\trans \\textit{" + font[NATIONAL](handle_font(example)) + "}" + EOL
                elif language == config.xml.regional:
                    tmp += "\\trans \\textit{[" + font[REGIONAL](example) + "]}" + EOL
                else: # language == config.xml.English
                    tmp += "\\trans " + example + EOL
        # LaTeX does not support empty examples
        if len(tmp) != 0:
            result += "\\begin{exe}" + EOL + tmp + "\\end{exe}" + EOL
    return result

def format_usage_notes(sense, font):
    """! @brief Display usage notes in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing usage notes in LaTeX format.
    """
    result = ""
    for usage in sense.find_usage_notes(language=config.xml.vernacular):
        result += "\\textit{VerUsage:} " + font[VERNACULAR](usage) + " "
    for usage in sense.find_usage_notes(language=config.xml.English):
        result += "\\textit{Usage:} " + usage + " "
    for usage in sense.find_usage_notes(language=config.xml.national):
        result += "\\textit{" + font[NATIONAL](handle_font(usage)) + "} "
    for usage in sense.find_usage_notes(language=config.xml.regional):
        result += "\\textit{[" + font[REGIONAL](usage) + "]} "
    return result

def format_encyclopedic_informations(sense, font):
    """! @brief Display encyclopedic informations in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing encyclopedic informations in LaTeX format.
    """
    result = ""
    for information in sense.find_encyclopedic_informations(language=config.xml.vernacular):
        result += font[VERNACULAR](information) + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.English):
        result += information + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.national):
        result += font[NATIONAL](handle_font(information)) + " "
    for information in sense.find_encyclopedic_informations(language=config.xml.regional):
        result += "\\textit{[" + font[REGIONAL](information) + "]} "
    return result

def format_restrictions(sense, font):
    """! @brief Display restrictions in LaTeX format.
    @param sense The current Sense LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing restrictions in LaTeX format.
    """
    result = ""
    for restriction in sense.find_restrictions(language=config.xml.vernacular):
        result += "\\textit{VerRestrict:} " + font[VERNACULAR](restriction) + " "
    for restriction in sense.find_restrictions(language=config.xml.English):
        result += "\\textit{Restrict:} " + restriction + " "
    for restriction in sense.find_restrictions(language=config.xml.national):
        result += "\\textit{" + font[NATIONAL](restriction) + "} "
    for restriction in sense.find_restrictions(language=config.xml.regional):
        result += "\\textit{[" + font[REGIONAL](restriction) + "]} "
    return result

def format_lexical_functions(lexical_entry, font):
    """! @brief Display lexical functions in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing lexical functions in LaTeX format.
    """
    result = ""
    # result += "\\textit{" + lexical_entry.get_lf() + ": }"
    # result += lexical_entry.get_le() + " "
    # result += lexical_entry.get_ln() + " "
    # result += lexical_entry.get_lr() + " "
    return result

def format_related_forms(lexical_entry, font, language=None):
    """! @brief Display related forms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @param language Language to consider to display related forms.
    @return A string representing related forms in LaTeX format.
    """
    result = ""
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["sy"]):
        result += "\\textit{Syn:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["an"]):
        result += "\\textit{Ant:} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += ". "
    for morphology in lexical_entry.get_morphologies():
        result += "\\textit{Morph:} " + font[VERNACULAR](morphology) + ". "
    for related_form in lexical_entry.get_related_forms(mdf_semanticRelation["cf"]):
        if language == config.xml.English:
            result += "\\textit{See:} "
        else:
            result += "\\textit{Voir :} "
        if related_form.get_lexical_entry() is not None:
            result += format_link(related_form.get_lexical_entry(), font)
        else:
            result += font[VERNACULAR](related_form.get_lexeme())
        result += " "
    # ce
    # cn
    # cr
    # result += "\\textit{See main entry:} " + font[VERNACULAR](lexical_entry.get_mn()) + ". "
    return result

def format_variant_forms(lexical_entry, font):
    """! @brief Display variant forms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing variant forms in LaTeX format.
    """
    result = ""
    for form_representation in lexical_entry.get_form_representations():
        if form_representation.get_variantForm() is not None:
            result += "\\textit{Variant:} " + font[VERNACULAR](form_representation.get_variantForm()) + " "
        if form_representation.get_comment(config.xml.English) is not None:
            result +=  "(" + form_representation.get_comment(config.xml.English) + ") "
        if form_representation.get_comment(config.xml.national) is not None:
            result +=  "(" + font[NATIONAL](form_representation.get_comment(config.xml.national)) + ") "
        if form_representation.get_comment(config.xml.regional) is not None:
            result +=  "(" + font[REGIONAL](form_representation.get_comment(config.xml.regional)) + ") "
    return result

def format_borrowed_word(lexical_entry, font):
    """! @brief Display borrowed word in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing borrowed word in LaTeX format.
    """
    result = ""
    if lexical_entry.get_borrowed_word() is not None:
        result += "\\textit{From:} " + lexical_entry.get_borrowed_word()
        if lexical_entry.get_written_form() is not None:
            result += " " + lexical_entry.get_written_form()
        result += ". "
    return result

def format_etymology(lexical_entry, font):
    """! @brief Display etymology in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing etymology in LaTeX format.
    """
    result = ""
    if lexical_entry.get_etymology() is not None:
        result += "\\textit{Etym:} \\textbf{" + lexical_entry.get_etymology() + "} "
    if lexical_entry.get_etymology_gloss() is not None:
        result += u"\u2018" + lexical_entry.get_etymology_gloss() + u"\u2019" + ". "
    return result

def format_paradigms(lexical_entry, font):
    """! @brief Display all paradigms in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing all paradigms in LaTeX format.
    """
    result = ""
    for paradigm in lexical_entry.find_paradigms():
        result += "\\textit{Prdm:} \\textbf{" + paradigm + "}. "
    for paradigm in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["sg"]):
        result += "\\textit{Sg:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["pl"]):
        result += "\\textit{Pl:} \\textbf{" + paradigm + "} "
    # result += "\\textit{Redup:} \\textbf{" + lexical_entry.get_rd() + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{1s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{2s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{3s:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']):
        result += "\\textit{3sn:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{1d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{2d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{3d:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']):
        result += "\\textit{3dn:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{1p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']):
        result += "\\textit{1px:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']):
        result += "\\textit{1pi:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{2p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{3p:} \\textbf{" + paradigm + "} "
    for paradigm in lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']):
        result += "\\textit{3pn:} \\textbf{" + paradigm + "} "
    return result

def format_table(lexical_entry, font):
    """! @brief Display a table in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing a table in LaTeX format.
    """
    return ""

def format_semantic_domains(lexical_entry, font):
    """! @brief Display semantic domains in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing semantic domains in LaTeX format.
    """
    result = ""
    for semantic_domain in lexical_entry.get_semantic_domains():
        result += "\\textit{SD:} " + semantic_domain + ". "
    # is
    # result += "\\textit{Semantics:} " + lexical_entry.get_is() + ". "
    # th
    # result += "\\textit{Thes:} " + lexical_entry.get_th() + ". "
    return result

def format_bibliography(lexical_entry, font):
    """! @brief Display bibliography in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing bibliography in LaTeX format.
    """
    result = ""
    if lexical_entry.get_bibliography() is not None:
        result += "\\textit{Read:} " + lexical_entry.get_bibliography() + ". "
    return result

def format_picture(lexical_entry, font):
    """! @brief Display a picture in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing a picture in LaTeX format.
    """
    # return "(" + lexical_entry.get_pc() + ") "
    return ""

def format_notes(lexical_entry, font):
    """! @brief Display all notes in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing all notes in LaTeX format.
    """
    result = ""
    for note in lexical_entry.find_notes(type="general"):
        result += "\\textit{[Note: " + note + "]} "
    for note in lexical_entry.find_notes(type="phonology"):
        result += "\\textit{[Phon: " + note + "]} "
    for note in lexical_entry.find_notes(type="grammar"):
        result += "\\textit{[Gram: " + note + "]} "
    for note in lexical_entry.find_notes(type="discourse"):
        result += "\\textit{[Disc: " + note + "]} "
    for note in lexical_entry.find_notes(type="anthropology"):
        result += "\\textit{[Ant: " + note + "]} "
    for note in lexical_entry.find_notes(type="sociolinguistics"):
        result += "\\textit{[Socio: " + note + "]} "
    for note in lexical_entry.find_notes(type="question"):
        result += "\\textit{[Ques: " + note + "]} "
    return result

def format_source(lexical_entry, font):
    """! @brief Display source in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing source in LaTeX format.
    """
    # return "\\textit{Source:} " + lexical_entry.get_so() + ". "
    return ""

def format_status(lexical_entry, font):
    """! @brief Display status in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return A string representing status in LaTeX format.
    """
    result = ""
    if lexical_entry.get_status() is not None:
        result += "\\textit{Status:} " + lexical_entry.get_status()
    return result

def format_date(lexical_entry, font):
    """! @brief Do not display date in LaTeX format.
    @param lexical_entry The current Lexical Entry LMF instance.
    @param font A Python dictionary giving the vernacular, national, regional fonts to apply to a text in LaTeX format.
    @return An empty string.
    """
    return ""
