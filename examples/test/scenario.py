#! /usr/bin/env python
# -*- coding: utf-8 -*-

## Needed to import LMF library properly
# Also automatically define 'ftest_path' as location of pylmflib/examples/test/ folder
from startup import *
import os

# Create result folder
if not os.path.exists(ftest_path + "obj"):
    os.mkdir(ftest_path + "obj")

# Read default configuration
lexical_resource = pylmflib.read_config(ftest_path + "../../pylmflib/config/default/config.xml")

# Read MDF file and set lexicon identifier
input_lexical_resource = pylmflib.read_mdf(ftest_path + "input.txt", id="short example")

# Set global information
input_lexical_resource.set_creation_date("2015-09-30")
input_lexical_resource.set_last_update("2015-09-30")
input_lexical_resource.set_author(u"Céline Buret")
input_lexical_resource.set_description("This is a testing lexicon.")
print input_lexical_resource.get_bibliographic_citation()

# Get created lexicon
my_lexicon = input_lexical_resource.get_lexicon("short example")

# Set lexicon attributes
my_lexicon.set_label("test online dictionary").set_language("eng").set_languageScript("latn").set_lexiconType("bilingual dictionary")

# Alphabetize lexemes
my_lexicon.sort_lexical_entries()

# Write XML LMF file
pylmflib.write_xml_lmf(input_lexical_resource, ftest_path + "obj/output.xml")

# Read XML LMF file
output_lexical_resource = pylmflib.read_xml_lmf(ftest_path + "obj/output.xml")

# Write LaTeX file
pylmflib.write_tex(output_lexical_resource, ftest_path + "obj/output.tex", preamble=ftest_path + "header.tex")

# Write MDF file
pylmflib.write_mdf(output_lexical_resource, ftest_path + "obj/output.txt")

# Write Microsoft Word document file
pylmflib.write_doc(output_lexical_resource, ftest_path + "obj/output.docx")

# Write Open Office document file
pylmflib.write_odt(output_lexical_resource, ftest_path + "obj/output.odt")

# Write HTML file
os.system("xsltproc -o " + ftest_path + "obj/output.html " + ftest_path + "../../pylmflib/utils/lmf2htm/htm.xsl " + ftest_path + "obj/output.xml")

# Write XML TEI file
os.system("xsltproc -o " + ftest_path + "obj/tei.xml " + ftest_path + "../../pylmflib/utils/lmf2tei/lmf2tei.xsl " + ftest_path + "obj/output.xml")

# Release created objects
del input_lexical_resource, output_lexical_resource
