#! /usr/bin/env python

"""! @package pylmflib The main package for LMF library support for Python. Normally used by importing the package, and perhaps a particular module inside it.
    
    Usage:
    >>> import pylmflib
    >>> from pylmflib import config
    >>> pylmflib.read_config(...)
"""

# Add pylmflib/ folder to path
import sys
sys.path.append(sys.path[-1] + '/pylmflib')

# Initialize API
from wrapper import *

## Functions used to initialize LMF library
def parse_options():
    """! @brief Get command line arguments.
    @return Parsed command line arguments.
    """
    # Options management
    from optparse import OptionParser
    parser = OptionParser()
    parser.add_option("-a", "--audio", dest="audio", action="store_false", default=True, help="include sound files [default=True]")
    parser.add_option("-c", "--cross-references", dest="cross_references", action="store_false", default=True, help="check cross references [default=True]")
    parser.add_option("-l", "--log-filename", dest="log_filename", action="store", default=None, help="log filename [default=None]")
    parser.add_option("-u", "--unit-test", dest="unit_test", action="store_true", default=False, help="unit test mode [default=False]")
    parser.add_option("-v", "--verbose", dest="verbose", action="store_true", default=False, help="print more details to stdout [default=False]")
    parser.add_option("-i", "--uid", dest="uid", action="store_true", default=False, help="include UID in output format [default=False]")
    return parser.parse_args()[0]

## Initialize LMF library global variables
# If an LMF module needs to access options, copy following lines:
# from pylmflib import options
# global options
options = parse_options()
# Initialize helper functions and log options
log("Command line options: " + str(options), options)
