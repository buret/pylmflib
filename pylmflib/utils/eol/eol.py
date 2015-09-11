#/usr/bin/python

"""! @package utils.eol
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

# Merge lines by deleting unwanted EOL
lines = []
for line in in_file.readlines():
    # Do not parse empty lines
    if line != EOL and not line.startswith('\\'):
        previous_line = lines.pop()
        line = previous_line.replace(EOL, " ") + line
    lines.append(line)
for line in lines:
    out_file.write(line)

# Do not forget to close files
in_file.close()
out_file.close()
