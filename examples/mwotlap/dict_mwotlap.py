#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of pylmflib/examples/mwotlap/ folder
from startup import *
import os

# Add mwotlap configuration folder to path
sys.path.append(user_path)

# Create result folder
if not os.path.exists(user_path + "result"):
    os.mkdir(user_path + "result")

# Import user customized configuration
from setting import items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "config.xml")

# Read MDF file and set lexicon identifier
os.system("python " + user_path + "../../pylmflib/utils/eol/eol.py -i " + user_path + "Mwotlap.lex -o " + user_path + "result/Mwotlap-eol.lex -e windows")
os.system("python " + user_path + "../../examples/mwotlap/se.py -i " + user_path + "result/Mwotlap-eol.lex -o " + user_path + "result/Mwotlap-eol-se.lex")
lexical_resource = pylmflib.read_mdf(id="mwotlap")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = pylmflib.read_sort_order(user_path + "sort_order.xml")
lexical_resource.get_lexicon("mwotlap").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "result/dictionary.xml")

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "result/mwotlap.tex", preamble=user_path + "preamble.tex", introduction=user_path + "introduction.tex", items=items, sort_order=xml_order)

# Write MDF file
pylmflib.write_mdf(lexical_resource, user_path + "result/mwotlap.txt")

# Write document file
pylmflib.write_doc(lexical_resource, user_path + "result/mwotlap.docx", items=items, sort_order=xml_order)

# Release created objects
del lexical_resource
