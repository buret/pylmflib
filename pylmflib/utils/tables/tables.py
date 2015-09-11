#/usr/bin/python
# -*- coding: utf-8 -*-

"""! @package utils.tables
"""

# Get command line arguments
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--input", dest="input", action="store", help="input MDF file")
parser.add_option("-e", "--output-eng", dest="output_eng", action="store", help="output LaTeX file in English")
parser.add_option("-f", "--output-fra", dest="output_fra", action="store", help="output LaTeX file in French")
options = parser.parse_args()[0]

# Open input and output files
try:
    in_file = open(options.input, "r", encoding='utf-8')
    out_eng = open(options.output_eng, "w", encoding='utf-8')
    out_fra = open(options.output_fra, "w", encoding='utf-8')
except TypeError:
    in_file = open(options.input, "r")
    out_eng = open(options.output_eng, "w")
    out_fra = open(options.output_fra, "w")

# Define EOL depending on operating system
import os
if os.name == 'posix':
    # Unix-style end of line
    EOL = '\n'
else:
    # Windows-style end of line
    EOL = '\r\n'

title_eng = """Words for which no close equivalent could be found"""
introduction_eng = """The list that follows groups words for which no close equivalents could be found. These negative pieces of information contain hints about the consultants' Na vocabulary and its 'soft shoulders'."""
title_fra = """Mots dont aucun équivalent n'a été trouvé"""
introduction_fra = """Cette liste regroupe les mots dont aucun équivalent n'a été trouvé. Même s'il ne s'agit que d'informations négatives, elles éclairent les limites du vocabulaire na des consultants."""

# Add section
out_eng.write("\\section*{\\centering " + title_eng + "}" + EOL)
out_fra.write("\\section*{\\centering " + title_fra + "}" + EOL)
# Insert explanation
out_eng.write(introduction_eng + EOL)
out_fra.write(introduction_fra + EOL)
# Begin table
out_eng.write("\\begin{center}" + EOL)
out_fra.write("\\begin{center}" + EOL)
out_eng.write("\\begin{longtable}{r|l}" + EOL)
out_fra.write("\\begin{longtable}{r|l}" + EOL)

# Generate table
import re
pattern = r"^\\(\w{2,3}) ?(.*)$"
lx = ""
ge = ""
gn = ""
gf = ""
for line in in_file.readlines():
    result = re.search(pattern, line)
    if result:
        if result.group(1) == "lx" and result.group(2) == "*":
            lx = result.group(2)
        elif result.group(1) == "ge":
            if lx == "*":
                ge = result.group(2).replace('_', "\string_")
        elif result.group(1) == "gn":
            if lx == "*":
                gn = result.group(2).replace('_', "\string_")
        elif result.group(1) == "gf":
            if lx == "*":
                gf = result.group(2).replace('_', "\string_")
                out_eng.write(ge)
                out_fra.write(gf)
                out_eng.write(" & ")
                out_fra.write(" & ")
                out_eng.write("\\textcolor{brown}{\zh{" + gn + "}}")
                out_fra.write("\\textcolor{brown}{\zh{" + gn + "}}")
                out_eng.write(" \\\\" + EOL)
                out_fra.write(" \\\\" + EOL)
                # Reset loop variables
                lx = ""
                ge = ""
                gn = ""
                gf = ""

# Do not forget to end tabular and close files
out_eng.write("\\end{longtable}")
out_fra.write("\\end{longtable}")
out_eng.write("\\end{center}")
out_fra.write("\\end{center}")
in_file.close()
out_eng.close()
out_fra.close()
