:: -*- coding: utf-8 -*-

:: Launch this script using the following command:
:: ./examples/khaling/run_khaling.bat

:: Results are available under examples/khaling/result/ folder.

:: LaTeX file is generated with sound records and with cross references
:: python examples/khaling/run_khaling.py

:: LaTeX file is generated without sound records and with cross references
::python examples/khaling/run_khaling.py -a

:: LaTeX file is generated with sound records and without cross references
::python examples/khaling/run_khaling.py -c

:: LaTeX file is generated without sound records and without cross references
python examples/khaling/run_khaling.py -a -c

:: Generate PDF: add xelatex binary location to your PATH environment variable
xelatex.exe -output-directory=examples/khaling/result/ examples/khaling/result/dictionary.tex --halt-on-error=N
xelatex.exe -output-directory=examples/khaling/result/ examples/khaling/result/dictionary.tex --halt-on-error=N
