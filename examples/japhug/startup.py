#! /usr/bin/env python

import sys

# Find pylmflib/examples/ path location
user_path = sys.path[0] + '/../'

# Add pylmflib/ folder to path
sys.path.append(user_path + '..')

# Import LMF library
import pylmflib
