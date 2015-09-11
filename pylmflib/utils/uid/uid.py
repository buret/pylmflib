#/usr/bin/python
# -*- coding: utf-8 -*-

"""! @package utils.uid
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

import sys
sys.path.append('./pylmflib/utils/ipa2sampa')
from ipa2sampa import uni2sampa

# To generate UID, we need to keep values of 'lx' and 'hm'
import re
pattern = r"^\\(\w{2,3}) ?(.*)$"
lx = ""
mkr = "lx"
sf = []
hm = ""
for line in in_file.readlines():
    result = re.search(pattern, line)
    if result:
        if result.group(1) == "lx" or result.group(1) == "se":
            lx = result.group(2)
            if result.group(1) == "se":
                mkr = "se"
        elif result.group(1) == "sf":
            sf.append(result.group(2))
        elif result.group(1) == "hm":
            hm = result.group(2)
            if lx != "":
                # Generate UID and remove spaces around separation character
                uid = uni2sampa(lx).replace(" | ", "|")
                # Concatenate homonym number if any, otherwise add '1'
                uid += str(hm)
                if hm == "":
                    uid += str("1")
                out_file.write("\\" + mkr + " <id=\"" + uid.encode('utf-8') + "\"> " + lx + EOL)
                out_file.write("\\sf " + uid.replace('|', u"€").replace('?', 'Q').replace('*', 'F').encode('utf-8') + ".wav" + EOL)
                for i in range (0, len(sf)):
                    out_file.write("\\sf " + sf[i] + EOL)
                out_file.write("\\hm " + hm + EOL)
                # Reset loop variables
                lx = ""
                mkr = "lx"
                sf = []
                hm = ""
            else:
                out_file.write(line)
        else:
            out_file.write(line)
    else:
        out_file.write(line)

# Do not forget to close files
in_file.close()
out_file.close()
