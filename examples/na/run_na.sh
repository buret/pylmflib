#! /usr/bin/env bash
# -*- coding: utf-8 -*-

# Launch this script using the following command:
# ./examples/na/run_na.sh

# Results are available under examples/na/result/ folder.

# LaTeX file is generated with sound records and with cross references
python examples/na/run_na.py

# LaTeX file is generated without sound records and with cross references
#python examples/na/run_na.py -a

# LaTeX file is generated with sound records and without cross references
#python examples/na/run_na.py -c

# LaTeX file is generated without sound records and without cross references
#python examples/na/run_na.py -a -c

# Generate PDF
xelatex -output-directory=examples/na/result/ examples/na/result/dictionary_eng.tex --halt-on-error=N >> /dev/null
xelatex -output-directory=examples/na/result/ examples/na/result/dictionary_eng.tex --halt-on-error=N >> /dev/null
xelatex -output-directory=examples/na/result/ examples/na/result/dictionary_fra.tex --halt-on-error=N >> /dev/null
xelatex -output-directory=examples/na/result/ examples/na/result/dictionary_fra.tex --halt-on-error=N >> /dev/null
