#/usr/bin/python
# -*- coding: utf-8 -*-

"""! @package utils.se
"""

# Get command line arguments
from optparse import OptionParser
parser = OptionParser()
parser.add_option("-i", "--input", dest="input", action="store", help="input MDF file")
parser.add_option("-o", "--output", dest="output", action="store", help="output MDF file")
options = parser.parse_args()[0]

# Open input and output files
try:
    in_file = open(options.input, "r", encoding='utf-8')
    out_file = open(options.output, "w", encoding='utf-8')
except TypeError:
    in_file = open(options.input, "r")
    out_file = open(options.output, "w")

# Define EOL depending on operating system
import os
if os.name == 'posix':
    # Unix-style end of line
    EOL = '\n'
else:
    # Windows-style end of line
    EOL = '\r\n'

import re
pattern = r"^\\(\w{2,3}) ?(.*)$"
lx = ""
for line in in_file.readlines():
    result = re.search(pattern, line)
    if result:
        if result.group(1) == "lx":
            lx = result.group(2)
            out_file.write(line)
        elif result.group(1) == "se":
            if result.group(2) == "":
                # Create a lexeme
                out_file.write("\\lx " + lx + EOL)
            else:
                out_file.write(line)
        else:
            out_file.write(line)
    else:
        out_file.write(line)

# Do not forget to close files
in_file.close()
out_file.close()
