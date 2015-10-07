#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of pylmflib/examples/Bambara/ folder
from startup import *
import os

# Add Bambara configuration folder to path
sys.path.append(user_path)

# Create result folder
if not os.path.exists(user_path + "result"):
    os.mkdir(user_path + "result")

# Import user customized configuration
from setting import items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = pylmflib.read_mdf(id="Bambara")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = pylmflib.read_sort_order(user_path + "sort_order.xml")
lexical_resource.get_lexicon("Bambara").sort_lexical_entries(items=items, sort_order=xml_order)

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "result/Bambara.xml")

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "result/Bambara.tex", preamble=user_path + "preamble.tex", introduction=user_path + "introduction.tex", items=items, sort_order=xml_order)

# Write MDF file
pylmflib.write_mdf(lexical_resource, user_path + "result/Bambara.txt")

# Write document file
pylmflib.write_doc(lexical_resource, user_path + "result/Bambara.docx", items=items, sort_order=xml_order)

# Release created objects
del lexical_resource
