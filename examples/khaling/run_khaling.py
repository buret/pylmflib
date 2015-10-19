#! /usr/bin/env python

# Launch this script using the following command:
# ./examples/khaling/run_khaling.py

import sys, os

# Define 'user_path' as path location of pylmflib/examples/ folder
user_path = sys.path[0] + '/../'

# Add khaling configuration folder to path
sys.path.append(user_path + 'khaling')

# Add pylmflib/ folder to path
sys.path.append(user_path + '..')

# Create result folder
if not os.path.exists(user_path + "khaling/result"):
    os.mkdir(user_path + "khaling/result")

# Import LMF library
import pylmflib

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "khaling/config.xml")

# Run Perl script
os.system("perl " + user_path + "../pylmflib/utils/ipa2devanagari/ipa2devanagari.pl " + user_path + "khaling/Dictionary.txt " + user_path + "khaling/result/dictionary-dev.txt")

# Read MDF file and set lexicon identifier
lexical_resource = pylmflib.read_mdf(id="khaling")

# Classify lexicon
sort_order = lambda character: ord(character.encode('utf-8').decode('utf-8'))
lexical_resource.get_lexicon("khaling").sort_lexical_entries(items=items, sort_order=sort_order)

# Generate paradigms
os.system("perl " + user_path + "../pylmflib/utils/paradigms/paradigms.pl " + user_path + "khaling/verbs.txt " + user_path + "khaling/result/paradigms.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/paradigms_eng.pl " + user_path + "khaling/verbs_eng.txt " + user_path + "khaling/result/paradigms_eng.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/reflexive_paradigms.pl " + user_path + "khaling/reflexive_verbs.txt " + user_path + "khaling/result/reflexive_paradigms.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/reflexive_paradigms_eng.pl " + user_path + "khaling/reflexive_verbs.txt " + user_path + "khaling/result/reflexive_paradigms_eng.tex")

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "khaling/result/dictionary.tex", preamble=user_path + "khaling/preamble.tex", introduction=user_path + "khaling/introduction.tex", lmf2tex=lmf2tex, items=items, sort_order=sort_order, paradigms=[user_path + "khaling/result/paradigms.tex", user_path + "khaling/result/paradigms_eng.tex", user_path + "khaling/result/reflexive_paradigms.tex", user_path + "khaling/result/reflexive_paradigms_eng.tex"])

# Release created objects
del lexical_resource
