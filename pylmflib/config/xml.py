#! /usr/bin/env python

"""! @package config
"""

from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from utils.xml_format import parse_xml
from utils.error_handling import InputError
from config.mdf import mdf_lmf, lmf_mdf, mdf_order, ps_partOfSpeech, pdl_paradigmLabel, pd_grammaticalNumber, pd_person, pd_anymacy, pd_clusivity
from config.tex import partOfSpeech_tex, paradigmLabel_tex
from common.range import partOfSpeech_range, paradigmLabel_range

# If an LMF module needs to access languages or fonts, copy following lines:
# import config
# print config.xml.vernacular, config.xml.English, config.xml.national, config.xml.regional, config.xml.French
# print config.xml.font

def sort_order_read(filename):
    """! @brief Read an XML file giving sort order.
    @param filename The name of the XML file to read with full path, for instance 'pylmflib/pylmflib/config/default/sort_order.xml'.
    @return A Python dictionary of ordered characters.
    """
    order = dict()
    type = dict()
    root = parse_xml(filename)
    # Parse XML elements
    for rules in root:
        # XML elements "rules" have 1 XML attribute: "level"
        if rules.tag != "rules":
            raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
        for rule in rules:
            # XML elements "rule" have 2 or 3 XML attributes: one for the character ("str"), a second for the rank value ("rank"), and an optional one for the type ("type")
            if rule.tag != "rule":
                raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
            order.update({rule.attrib["str"] : float(rule.attrib["rank"])})
            try:
                type.update({rule.attrib["str"] : rule.attrib["type"]})
            except KeyError:
                pass
    if len(type) != 0:
        return order, type
    return order

def config_read(filename):
    """! @brief Read an XML file giving the user configuration.
    @param filename The name of the XML file to read with full path, for instance 'pylmflib/pylmflib/config/default/config.xml'.
    @return A Lexical Resource.
    """
    import os
    import config.xml
    configuration = parse_xml(filename)
    # Parse XML elements
    for format in configuration:
        if format.tag == "Language":
            # XML element "Language" have several XML subelements "lang"
            for lang in format:
                # XML elements "lang" have 2 XML attributes: one for the nature of the language ("att"), a second for the language code ("val")
                exec("config.xml." + lang.attrib["att"] + " = '" + lang.attrib["val"] + "'")
        elif format.tag == "Font":
            config.xml.font = dict()
            # XML element "Font" have several XML subelements "font"
            for font in format:
                # XML elements "font" have 2 XML attributes: one for the nature of the language ("att"), a second for the variable name ("var")
                exec("l = lambda " + font.attrib['var'] + ": " + font.text)
                config.xml.font.update({font.attrib['att']: l})
        elif format.tag == "LMF":
            # Create lexical resource and set DTD version
            lexical_resource = LexicalResource(format[0].attrib["dtdVersion"])
            for object in format[0]:
                if object.tag == "GlobalInformation":
                    # Set global information
                    for feat in object:
                        if feat.attrib["att"] == "languageCode":
                            lexical_resource.set_language_code(feat.attrib["val"])
                        elif feat.attrib["att"] == "author":
                            lexical_resource.set_author(feat.attrib["val"])
                        elif feat.attrib["att"] == "version":
                            lexical_resource.set_version(feat.attrib["val"])
                        elif feat.attrib["att"] == "lastUpdate":
                            lexical_resource.set_last_update(feat.attrib["val"])
                        elif feat.attrib["att"] == "license":
                            lexical_resource.set_license(feat.attrib["val"])
                        elif feat.attrib["att"] == "characterEncoding":
                            lexical_resource.set_character_encoding(feat.attrib["val"])
                        elif feat.attrib["att"] == "dateCoding":
                            lexical_resource.set_date_coding(feat.attrib["val"])
                        elif feat.attrib["att"] == "creationDate":
                            lexical_resource.set_creation_date(feat.attrib["val"])
                        elif feat.attrib["att"] == "projectName":
                            lexical_resource.set_project_name(feat.attrib["val"])
                        elif feat.attrib["att"] == "description":
                            lexical_resource.set_description(feat.attrib["val"])
                elif object.tag == "Lexicon":
                    # Create lexicon and set identifier
                    lexicon = Lexicon(object.attrib["id"])
                    # Set lexicon attributes
                    for feat in object:
                        if feat.attrib["att"] == "language":
                            lexicon.set_language(feat.attrib["val"])
                        elif feat.attrib["att"] == "languageScript":
                            lexicon.set_languageScript(feat.attrib["val"])
                        elif feat.attrib["att"] == "label":
                            lexicon.set_label(feat.attrib["val"])
                        elif feat.attrib["att"] == "lexiconType":
                            lexicon.set_lexiconType(feat.attrib["val"])
                        elif feat.attrib["att"] == "entrySource":
                            lexicon.set_entrySource(feat.attrib["val"])
                        elif feat.attrib["att"] == "localPath":
                            lexicon.set_localPath(feat.attrib["val"])
                            # Set absolute path to audio files
                            config.xml.audio_path = os.path.abspath(os.path.abspath('.') + "/" + feat.attrib["val"]) + "/"
                    # Attach lexicon to the lexical resource
                    lexical_resource.add_lexicon(lexicon)
        elif format.tag == "MDF":
            for mdf in format:
                if mdf.tag == "mdf_lmf":
                    # XML elements "mdf_lmf" have 2 XML attributes: one for the name of the marker ("marker"), a second for the variable name ("var")
                    exec("l = lambda " + mdf.attrib['var'] + ": " + mdf.text)
                    mdf_lmf.update({mdf.attrib['marker']: l})
                elif mdf.tag == "ps_partOfSpeech":
                    # XML elements "ps_partOfSpeech" have 2 XML attributes: one for the MDF value ("ps"), a second for the LMF value ("partOfSpeech")
                    ps_partOfSpeech.update({mdf.attrib['ps']: mdf.attrib['partOfSpeech']})
                    # Also automatically update range of possible values allowed for LMF part of speech LexicalEntry attribute -->
                    partOfSpeech_range.add(mdf.attrib['partOfSpeech'])
                    # And automatically update the reverse operation
                    partOfSpeech_tex.update({mdf.attrib['partOfSpeech']: mdf.attrib['ps']})
                elif mdf.tag == "pdl_paradigmLabel":
                    # XML elements "pdl_paradigmLabel" have 2 XML attributes: one for the MDF value ("pdl"), a second for the LMF value ("paradigmLabel")
                    pdl_paradigmLabel.update({mdf.attrib['pdl']: mdf.attrib['paradigmLabel']})
                    # Also automatically update range of possible values allowed for LMF paradigm label Paradigm attribute -->
                    paradigmLabel_range.add(mdf.attrib['paradigmLabel'])
                    # And automatically update the reverse operation
                    paradigmLabel_tex.update({mdf.attrib['paradigmLabel']: mdf.attrib['pdl']})
                elif mdf.tag == "lmf_mdf":
                    # XML elements "lmf_mdf" have 2 XML attributes: one for the name of the marker ("marker"), a second for the variable name ("var")
                    exec("l = lambda " + mdf.attrib['var'] + ": " + mdf.text)
                    lmf_mdf.update({mdf.attrib['marker']: l})
                elif mdf.tag == "mdf_order":
                    mdf_order = []
                    for element in mdf:
                        mdf_order.append(element.tag)
                        list1 = []
                        for level1 in element:
                            list1.append(level1.tag)
                            list2 = []
                            for level2 in level1:
                                list2.append(level2.tag)
                            if len(list2) != 0:
                                list1.append(list2)
                        if len(list1) != 0:
                            mdf_order.append(list1)
        elif format.tag == "LaTeX":
            for param in format:
                if param.tag == "partOfSpeech_tex":
                    # XML elements "partOfSpeech_tex" have 2 or 3 XML attributes: one for the LMF value ("partOfSpeech"), a second for the LaTeX value ("tex"), and an optional one to define language
                    try:
                        partOfSpeech_tex.update({(param.attrib['lang'], param.attrib['partOfSpeech']): param.attrib['tex']})
                    except KeyError:
                        partOfSpeech_tex.update({param.attrib['partOfSpeech']: param.attrib['tex']})
                    # Also automatically update range of possible values allowed for LMF part of speech LexicalEntry attribute -->
                    partOfSpeech_range.add(param.attrib['partOfSpeech'])
                elif param.tag == "paradigmLabel_tex":
                    # XML elements "paradigmLabel_tex" have 2 XML attributes: one for the LMF value ("paradigmLabel"), a second for the LaTeX value ("tex")
                    paradigmLabel_tex.update({param.attrib['paradigmLabel']: param.attrib['tex']})
                    # Also automatically update range of possible values allowed for LMF paradigm label Paradigm attribute -->
                    paradigmLabel_range.add(param.attrib['paradigmLabel'])
        else:
            raise InputError(module_name + ".py", "XML file '%s' is not well-formatted." % filename)
    return lexical_resource
