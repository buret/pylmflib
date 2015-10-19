#! /usr/bin/env python

# Launch this script using the following command:
# ./examples/japhug/run_japhug.py

import sys, os

# Define 'user_path' as path location of pylmflib/examples/ folder
user_path = sys.path[0] + '/../'

# Add japhug configuration folder to path
sys.path.append(user_path + 'japhug')

# Add pylmflib/ folder to path
sys.path.append(user_path + '..')

# Create result folder
if not os.path.exists(user_path + "japhug/result"):
    os.mkdir(user_path + "japhug/result")

# Import LMF library
import pylmflib

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "japhug/config.xml")

# Read MDF file and set lexicon identifier
lexical_resource = pylmflib.read_mdf(id="japhug")

# Classify lexicon
xml_order = pylmflib.read_sort_order(user_path + "japhug/sort_order.xml")
lexical_resource.get_lexicon("japhug").sort_lexical_entries(items=items, sort_order=xml_order)

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "japhug/result/dictionary.tex", preamble=user_path + "japhug/preamble.tex", introduction=user_path + "japhug/introduction.tex", lmf2tex=lmf2tex, items=items, sort_order=xml_order)

# Release created objects
del lexical_resource
