#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Launch this script using the following command:
# ./examples/khaling/run_khaling.sh

# Results are available under examples/khaling/result/ folder

# LaTeX file is generated with sound records and with cross references
python examples/khaling/run_khaling.py

# LaTeX file is generated without sound records and with cross references
#python examples/khaling/run_khaling.py -a

# LaTeX file is generated with sound records and without cross references
#python examples/khaling/run_khaling.py -c

# LaTeX file is generated without sound records and without cross references
#python examples/khaling/run_khaling.py -a -c

# Generate PDF
xelatex -output-directory=examples/khaling/result/ examples/khaling/result/dictionary.tex --halt-on-error=N >> /dev/null
xelatex -output-directory=examples/khaling/result/ examples/khaling/result/dictionary.tex --halt-on-error=N >> /dev/null
