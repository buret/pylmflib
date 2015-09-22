:: -*- coding: utf-8 -*-

:: Launch this script using the following command:
:: ./examples/japhug/run_japhug.bat

:: Results are available under examples/japhug/result/ folder.

:: LaTeX file is generated with sound records and with cross references
python examples/japhug/run_japhug.py

:: LaTeX file is generated without sound records and with cross references
::python examples/japhug/run_japhug.py -a

:: LaTeX file is generated with sound records and without cross references
::python examples/japhug/run_japhug.py -c

:: LaTeX file is generated without sound records and without cross references
::python examples/japhug/run_japhug.py -a -c

:: Generate PDF: add xelatex binary location to your PATH environment variable
xelatex.exe -output-directory=examples/japhug/result/ examples/japhug/result/dictionary.tex --halt-on-error=N
xelatex.exe -output-directory=examples/japhug/result/ examples/japhug/result/dictionary.tex --halt-on-error=N
