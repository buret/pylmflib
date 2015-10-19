#! /usr/bin/env python

import sys

# Find pylmflib/examples/test/ path location
ftest_path = sys.path[0] + '/'

# Add pylmflib/ folder to path
sys.path.append(ftest_path + '../..')

# Import LMF library
import pylmflib
