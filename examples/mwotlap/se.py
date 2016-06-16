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

# Loop variables
lx = ""
hm = ""
se = ""
tmp_buffer = ""
lx_buffer = ""
se_buffer = ""
is_se = False

for line in in_file.readlines():
    result = re.search(pattern, line)

    if result:

        if result.group(1) == "lx":
            if is_se is None:
                # We know now that it was a subentry
                se_buffer += "\\se " + se + EOL
                se_buffer += tmp_buffer
            # Copy entry fields then subentries if any
            out_file.write(lx_buffer)
            out_file.write(se_buffer)
            # Reset loop variables
            hm = ""
            se = ""
            tmp_buffer = ""
            se_buffer = ""
            is_se = False
            # Start a new main entry
            lx = result.group(2)
            lx_buffer = EOL + line

        elif result.group(1) == "hm":
            hm = result.group(2)
            lx_buffer += line
    
        elif result.group(1) == "se":
            if is_se is None:
                # We know now that it was a subentry
                se_buffer += "\\se " + se + EOL
                se_buffer += tmp_buffer
                tmp_buffer = ""
            if result.group(2) == "":
                # Copy entry fields then subentries if any
                out_file.write(lx_buffer)
                out_file.write(se_buffer)
                # Create a new main entry
                lx_buffer = EOL + "\\lx " + lx + EOL
                if hm != "" :
                    lx_buffer += "\\hm " + hm + EOL
                # Reset loop variables
                se = ""
                tmp_buffer = ""
                se_buffer = ""
                is_se = False
            else:
                # We do not know yet if it is a subentry or another main entry
                se = result.group(2)
                is_se = None

        elif result.group(1) == "wr":
            if is_se is None:
                # We knwow now that it is a main entry
                # Copy entry fields then subentries if any
                out_file.write(lx_buffer)
                out_file.write(se_buffer)
                # \lx <lx>
                # \lc <se>
                lx_buffer = EOL + "\\lx " + lx + EOL
                lx_buffer += "\\lc " + se + EOL
                if hm != "":
                    lx_buffer += "\\hm " + hm + EOL
                lx_buffer += tmp_buffer
                lx_buffer += line
                # Reset loop variables
                se = ""
                tmp_buffer = ""
                se_buffer = ""
                is_se = False
            elif is_se is True:
                # This case should not happen
                raise IOError
            elif is_se is False:
                # We already knew that it is a main entry
                lx_buffer += line

        elif result.group(1) == "sn" or result.group(1) == "el":
            if is_se is None:
                # We know now that it was a subentry
                se_buffer += "\\se " + se + EOL
                se_buffer += tmp_buffer
                tmp_buffer = ""
                is_se = False
            lx_buffer += line

        else:
            # Copy until next 'lx' / 'se' / 'sn' / 'el'
            if is_se is True:
                se_buffer += line
            elif is_se is None:
                tmp_buffer += line
            elif is_se is False:
                lx_buffer += line

    elif line != EOL:
        # Copy until next 'lx' / 'se' / 'sn' / 'el'
        if is_se is True:
            se_buffer += line
        elif is_se is None:
                tmp_buffer += line
        elif is_se is False:
            lx_buffer += line

# Do not forget to close files
in_file.close()
out_file.close()
