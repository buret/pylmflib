#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of pylmflib/examples/ folder
from startup import *
import os

# Add japhug configuration folder to path
sys.path.append(user_path + 'japhug')

# Create result folder
if not os.path.exists(user_path + "japhug/result"):
    os.mkdir(user_path + "japhug/result")

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "japhug/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = pylmflib.read_mdf(id="japhug")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = pylmflib.read_sort_order(user_path + "japhug/sort_order.xml")
lexical_resource.get_lexicon("japhug").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "japhug/result/dictionary.xml")

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "japhug/result/dictionary.tex", preamble=user_path + "japhug/preamble.tex", introduction=user_path + "japhug/introduction.tex", lmf2tex=lmf2tex, items=items, sort_order=xml_order)

# Write MDF file
pylmflib.write_mdf(lexical_resource, user_path + "japhug/result/dictionary.txt")

# Write document file
pylmflib.write_doc(lexical_resource, user_path + "japhug/result/dictionary.docx", items=items, sort_order=xml_order, paradigms=True)

# Release created objects
del lexical_resource
