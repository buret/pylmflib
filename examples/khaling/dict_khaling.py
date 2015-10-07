#! /usr/bin/env python

## Needed to import LMF library properly
# Also automatically define 'user_path' as location of pylmflib/examples/ folder
from startup import *
import os

# Add khaling configuration folder to path
sys.path.append(user_path + 'khaling')

# Create result folder
if not os.path.exists(user_path + "khaling/result"):
    os.mkdir(user_path + "khaling/result")

# Import user customized configuration
from setting import lmf2tex, items

# Read user configuration
lexical_resource = pylmflib.read_config(user_path + "khaling/config.xml")

# Run Perl script
os.system("perl " + user_path + "../pylmflib/utils/ipa2devanagari/ipa2devanagari.pl " + user_path + "khaling/Dictionary.txt " + user_path + "khaling/result/dictionary-dev.txt")

# Read MDF file and set lexicon identifier
lexical_resource = pylmflib.read_mdf(id="khaling")

# Display global information
print lexical_resource.get_bibliographic_citation()

# Classify lexicon
xml_order = pylmflib.read_sort_order(user_path + "khaling/sort_order.xml")
dev_order = lambda character: ord(character.encode('utf-8').decode('utf-8'))
lexical_resource.get_lexicon("khaling").sort_lexical_entries(items=items, sort_order=dev_order)

# Write XML LMF file
pylmflib.write_xml_lmf(lexical_resource, user_path + "khaling/result/dictionary.xml")

# Generate paradigms
os.system("perl " + user_path + "../pylmflib/utils/paradigms/paradigms.pl " + user_path + "khaling/verbs.txt " + user_path + "khaling/result/paradigms.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/paradigms_eng.pl " + user_path + "khaling/verbs_eng.txt " + user_path + "khaling/result/paradigms_eng.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/reflexive_paradigms.pl " + user_path + "khaling/reflexive_verbs.txt " + user_path + "khaling/result/reflexive_paradigms.tex")
os.system("perl " + user_path + "../pylmflib/utils/paradigms/reflexive_paradigms_eng.pl " + user_path + "khaling/reflexive_verbs.txt " + user_path + "khaling/result/reflexive_paradigms_eng.tex")

# Write LaTeX file
pylmflib.write_tex(lexical_resource, user_path + "khaling/result/dictionary.tex", preamble=user_path + "khaling/preamble.tex", introduction=user_path + "khaling/introduction.tex", lmf2tex=lmf2tex, items=items, sort_order=dev_order, paradigms=[user_path + "khaling/result/paradigms.tex", user_path + "khaling/result/paradigms_eng.tex", user_path + "khaling/result/reflexive_paradigms.tex", user_path + "khaling/result/reflexive_paradigms_eng.tex"])

# Write MDF file
pylmflib.write_mdf(lexical_resource, user_path + "khaling/result/dictionary.txt")

# Write document file
pylmflib.write_doc(lexical_resource, user_path + "khaling/result/dictionary.docx", items=items, sort_order=dev_order, paradigms=True)

# Release created objects
del lexical_resource
