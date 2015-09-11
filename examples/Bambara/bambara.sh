#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Go under pylmflib/ and launch this script using the following command:
# ./examples/Bambara/bambara.sh

# Results are available under pylmflib/examples/Bambara/result/ folder.

# LaTeX file is generated with sound records and with cross references
#python examples/Bambara/bambara.py

# LaTeX file is generated without sound records and with cross references
python examples/Bambara/bambara.py -a

# LaTeX file is generated with sound records and without cross references
#python examples/Bambara/bambara.py -c

# LaTeX file is generated without sound records and without cross references
#python examples/Bambara/bambara.py -a -c

# Generate PDF
xelatex -output-directory=examples/Bambara/result/ examples/Bambara/result/Bambara.tex --halt-on-error=N >> /dev/null
