#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of pylmflib/examples/ folder
from startup import *
import os

# Add na configuration folder to path
sys.path.append(user_path + 'na')

# Create result folder
if not os.path.exists(user_path + "na/result"):
    os.mkdir(user_path + "na/result")

# Import user customized configuration
from setting import tex_eng, tex_fra, items, classify_lexicon

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "na/config.xml")

# Read MDF file, generate UID and set lexicon identifier
os.system("python " + user_path + "../pylmflib/utils/eol/eol.py -i " + user_path + "na/Dictionary.txt -o " + user_path + "na/result/dictionary-eol.txt")
os.system("python " + user_path + "../pylmflib/utils/uid/uid.py -i " + user_path + "na/result/dictionary-eol.txt -o " + user_path + "na/result/dictionary-uid.txt")
lexical_resource = pylmflib.read_mdf(id="na")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
(xml_order, xml_type) = pylmflib.read_sort_order(user_path + "na/sort_order.xml")
classify_lexicon(lexical_resource.get_lexicon("na"), xml_order, xml_type)

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "na/result/dictionary.xml")

# Generate tables
os.system("python " + user_path + "../pylmflib/utils/tables/tables.py -i " + user_path + "na/Dictionary.txt -e " + user_path + "na/result/table_eng.tex -f " + user_path + "na/result/table_fra.tex")

# Write LaTeX files
pylmflib.write_tex(lexical_resource, user_path + "na/result/dictionary_eng.tex", preamble=user_path + "na/preamble.tex", introduction=user_path + "na/introduction_eng.tex", lmf2tex=tex_eng, items=items, sort_order=xml_order, tables=[user_path + "na/result/table_eng.tex"], title="Online Na-English-Chinese Dictionary (version 1.0)")
pylmflib.write_tex(lexical_resource, user_path + "na/result/dictionary_fra.tex", preamble=user_path + "na/preamble.tex", introduction=user_path + "na/introduction_fra.tex", lmf2tex=tex_fra, items=items, sort_order=xml_order, tables=[user_path + "na/result/table_fra.tex"], title=u"Dictionnaire na-chinois-français en ligne (version 1.0)", tex_language="french")

# Write MDF file
pylmflib.write_mdf(lexical_resource, user_path + "na/result/dictionary.txt")

# Write document file
pylmflib.write_doc(lexical_resource, user_path + "na/result/dictionary.docx", items=items, sort_order=xml_order)

# Release created objects
del lexical_resource
