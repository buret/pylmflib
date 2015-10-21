========
pylmflib
========

Latest version: 1.0

Date: October 21, 2015

Author: Céline Buret

Maintainer: Séverine Guillaume

Documentation: http://himalco.huma-num.fr/documentation/index.htm

Home page: https://github.com/buret/pylmflib

License: gpl-3.0

Platform: Unix, Linux, Windows, MAC

Package index owner: Céline Buret

Introduction
=============

What is pylmflib?
___________________

The Python LMF library is a suite of open-source Python modules for dictionary format conversion. It performs automatic tasks for multi-languages dictionaries, such as conversion between different formats used for dictionaries.

The main idea of ``pylmflib`` is to provide a software package which integrates conversion functions from MDF format to several output formats: LaTeX (PDF), docx, HTML, etc.

``pylmflib`` implements the LMF standard. For more details, please see http://www.lexicalmarkupframework.org.

What can be done with pylmflib?
__________________________________

With the help of ``pylmflib``, users can:
 - convert a dictionary from a regular MDF format issued from Toolbox to a PDF printable document,
 - convert a dictionary from a regular MDF format issued from Toolbox to a docx editable document,
 - customise markers used in Toolbox to match the LMF internal format,
 - keep an archivable format of their dictionary in XML LMF,
 - display their dictionary online using an XSL conversion from XML LMF to HTML.

How can pylmflib be used?
_____________________________

``pylmflib`` is a library written in the Python programming language. It can be used directly in the Python interpreter or imported into Python scripts.
For more information about Python, see http://www.python.org.

How to cite pylmflib?
________________________

If you are using ``pylmflib`` for non-commercial, scientific projects, please cite the library in its current state along with the version that you used:

Buret, Céline (2015): pylmflib. Python Library for Automatic Tasks in Multi-Languages Dictionaries. Version 1.0 (Uploaded on 2015-10-21). URL: http://www.pylmflib.org.

Installation
=============

Basic setup
______________

Use pip to install ``pylmflib`` package from PyPI:
::

	$ pip install pylmflib

Usage
____________

In order to use the library, open Python2 in your terminal and import ``pylmflib`` as follows:
::

	>>> from pylmflib import *

Dependencies
___________________

Indispensable third party libraries
++++++++++++++++++++++++++++++++++++++

Here is the list of the libraries without which ``pylmflib`` won't work.

Regex: http://pypi.python.org/pypi/regex

Recommended third party libraries
++++++++++++++++++++++++++++++++++++++++

Here is a list of the libraries without which ``pylmflib`` core functions will work, but which are anyway used quite frequently in a lot of modules.

Docx: https://pypi.python.org/pypi/python-docx

ODF: https://pypi.python.org/pypi/odfpy

Setup for development version
__________________________________

Prerequisite
+++++++++++++++

Install git.

Setup with git
++++++++++++++++++

If you want to regularly work on ``pylmflib``, open a (git) terminal and type in the following:
::

	$ git clone https://github.com/buret/pylmflib

Instructions for a basic installation on Linux and Mac
_______________________________________________________

Prerequisites on Linux and Mac
+++++++++++++++++++++++++++++++++++++++

Before being able to run ``pylmflib``, you will need to follow these steps:

1. git
::

	$ sudo apt-get install git
	$ git clone https://github.com/buret/pylmflib pylmflib

2. setuptools
::

	$ wget https://bootstrap.pypa.io/ez_setup.py -O - | sudo python

3. python-docx

Download ``python-docx-0.8.5.tar.gz`` : https://pypi.python.org/pypi/python-docx
::

	$ tar xvzf python-docx-0.8.5.tar.gz
	$ cd python-docx-0.8.5/
	$ sudo python setup.py install

4. xsltproc
::

	$ sudo apt-get install xsltproc

5. xelatex
::

	$ sudo apt-get install texlive
	$ sudo apt-get install texlive-xetex

6. Charis SIL

Download : http://scripts.sil.org/cms/scripts/page.php?site_id=nrsi&id=charissil_download

Install : http://scripts.sil.org/cms/scripts/page.php?item_id=DecompressUtil

7. MingLiU

Download : http://www.fontpalace.com/font-download/MingLiU/

8. ArialUnicodeMS

Download : https://code.google.com/p/tuanphamvu/downloads/detail?name=Arial%20Unicode%20MS.rar&can=2&q=

9. Copy audio files if any.

pylmflib installation on Linux and Mac
+++++++++++++++++++++++++++++++++++++++++++++++++++++

We recommend to use the stable version of ``pylmflib`` (1.0). Make sure that ``regex`` is installed on you system prior to installing ``pylmflib``. In order to install this version, simply download it from https://github.com/buret/pylmflib or https://pypi.python.org/pypi/pylmflib/1.0, unpack the directory, then ``cd`` into it, and type in the prompt:
::

	$ python setup.py install

You may need sudo-rights to carry out these command.

At this stage, you can run the unit tests:
::

	$ test/test_all.py

And you could run all provided examples:
::

	$ examples/Bambara/bambara.py
	$ examples/japhug/dict_japhug.py
	$ examples/khaling/dict_khaling.py
	$ examples/na/dict_na.py
	$ examples/test/scenario.py
	$ examples/yuanga/dict_yuanga.py

Installation instructions on Windows
________________________________________

Prerequisites on Windows
++++++++++++++++++++++++++++++++++

Before being able to install ``pylmflib-1.0``, you will need to install:

1. ``pip-7.1.2``
2. ``VCForPython27.msi``
3. ``python-docx-0.8.5``
4. ``lxml-2.0.3``

In some cases, you may need to install:

 * ``setuptools-18.4``
 * ``ez_setup.py``
 * ``get-pip.py``

pylmflib installation on Windows
++++++++++++++++++++++++++++++++++++++++++

The current version of ``pylmflib`` for Python2 should basically also run on Windows. In order to install ``pylmflib`` on a Windows machine, I recommend to use the Cygwin terminal and install ``pylmflib`` in the same way in which one would otherwise install it on Linux or Mac machines.

Workarounds
___________________

To use the library without installing it, i.e. without running the setup-command, a simple way to use ``pylmflib`` is to include it in your sys-path just before you call the library:
::

	>>> import sys
	>>> sys.path.append("path_to_pylmflib)

Code
======

Source code is available at: https://github.com/buret/pylmflib

``pylmflib`` has been developed in Python 2.7.5.

It is under GPL licence.

Basic modules
_____________________

The library in its current state consists of the following modules:
 * common
 * config
 * core
 * input
 * morphology
 * morphosyntax
 * mrd
 * output
 * resources
 * utils

Basic formats
____________________

In the following, we list some of the formats that are frequently used by ``pylmflib``, be it that they are taken as input formats, or that they are produced as output from the classes and methods provided by ``pylmflib``:

* MDF
* XML LMF
* LaTeX
* docx

Here is a list of formats that can be used, but need to be further developed, i.e. integration has been done but implementation has to be completed:

* XML TEI
* HTML
* ODT

Formats that have to be added to the library in the future:

* xls / csv
* Elan
* XML ITE
* XML LIFT
* XML LexiquePro
* XML OLIF
* XML Toolbox

Coding conventions
_________________________

Please respect the coding rules used in the library.

Test
======

For tests, I use the ``unittest``Python library. To run the tests, just enter the main directory and call ``test/test_all.py`` on the command line. Please do not commit any changes without all tests running without failure or error.

All tests are in a directory ``test/`` within the main directory. For each Python source file in the source directory, there is a test file with a prefix ``test_``. For example, the tests of the ``core`` module, which has its source in ``pylmflib/core/``, are located in ``test/test_core_xxx.py``. Within the test files, there is a class defined for each class in the original source files, with a prefix ``Test``. For example, there is a class ``TestLexicalEntry`` defined in ``test_core_lexical_entry.py`` as there is a class ``LexicalEntry`` in ``lexical_entry.py``. For each method of a class, the test class has a method with the prefix ``test_``. For example, the method ``create_related_form()`` of the ``LexicalEntry`` class is tested with the method ``test_create_related_form()`` of the test class.

Documentation
=============

If you contribute to ``pylmflib``, you should document your code.
The first step for documentation is the documentation within the code.

Currently, documentation is created using the following steps:

- Whenever code is added to ``pylmflib``, the contributors add documentation inline in their code, following the style used in the project.
- Then, they run ``Doxygen`` using the ``Doxyfile`` provided under ``doc/Doxygen``.
- The general website structure is added around the code. You can find its content by browsing the ``doc/Doxygen/html/`` directory.

Examples
==========

Workflow example
_______________________

This is an example workflow that illustrates some of the functionalities of ``pylmflib``. We start with a small dataset from the Bambara language.

Getting started
+++++++++++++++++++++++++++++

First, make sure to have the Python LMF library downloaded, extracted and installed properly. The dataset that will be used is located under ``examples/Bambara``.

This folder includes a Python script that runs the whole code from the beginning to the end. In order to start the conversion, go under the main directory and run this script:
::

	$ python examples/Bambara/bambara.py

As a result, the following files will appear in the result directory:

* ``Bambara.docx``, that shows an example of a Microsoft Word document that you can obtain ;
* ``Bambara.tex``, that you must compile using XeLaTeX to get a PDF printable dictionary ;
* ``Bambara.txt``, which is similar to the input database ``BambaraDemo.db`` in MDF format ;
* ``Bambara.xml``, which is the XML LMF representation of the dictionary.

You can also directly run the conversion and XeLaTeX command by running ``bambara.sh`` or ``bambara.bat`` depending on your operating system.

Python scripts
++++++++++++++++++++++++++++++

* ``bambara.py``

It is the main script, the one which calls ``pylmflib`` functions:

1. ``read_config``
2. ``read_mdf``
3. ``read_sort_order``
4. ``write_xml_lmf``
5. ``write_tex``
6. ``write_mdf``
7. ``write_doc``

So the basic steps are:

1. to read the configuration defined in ``config.xml`` (see the tutorial chapter below for details) ;
2. to read the MDF file, so in this case the ``BambaraDemo.db`` Toolbox dictionary ;
3. to read the alphabetical order defined in ``sort_order.xml`` (see the tutorial chapter below for details) ;
4. to convert the MDF text format into a structured XML format, based on LMF standard ;
5. to generate an output LaTeX file ;
6. to generate an MDF file, similar to the input one ;
7. to generate an output document file.

In this script, user also has access to all ``pylmflib`` objects methods, which are fully documented at:
http://himalco.huma-num.fr/documentation/index.htm

* ``setting.py``

To be able to customise some Python variables, it is possible to write a ``setting.py file``, in which user can:

 - define the items to sort: in this case, we choose to sort the ``lx`` MDF marker contents, but it could be any other field ;
 - customise input MDF markers used by modifying the ``mdf_lmf`` Pyhton variable ;
 - customise output MDF markers by modifying the ``lmf_mdf`` Python variable.

It is also possible to customise Python functions. See the other examples below for more advanced use.

* ``startup.py``

This file is needed to define working path and path to the library. Normally, you should not have to modify it.

Basic example
__________________

A simple example is presented under ``examples/test``. All available output formats are generated:

 * XML LMF
 * LaTeX
 * MDF
 * docx
 * ODT
 * HTML
 * XML TEI

Note that conversion scripts from XML LMF to HTML, ODT and XML TEI are here as examples to show what is possible to do. They have to be reworked to generate user-friendly outputs.

PDF examples
___________________

It is possible to fully customise the desired output. There are three examples to generate customised PDF printable dictionaries, located under ``examples/japhug``, ``examples/khaling`` and ``examples/na``.

In all cases, the file ``setting.py`` has been deeply modified. The most important function is ``lmf2tex()``, which role is to organise data information in the LaTeX output file. If user do not provide this Python function, there is a default function for basic presentation. Again, coding details about this function is available at:
http://himalco.huma-num.fr/documentation/index.htm

Docx example
____________________

It is also possible to customise a document output. There is an example to generate a customised docx editable dictionary, located under ``examples/yuanga``.

Moreover, in this case, entries are not classified by alphabetical order, but by semantic domain.

Chapter titles of the output docx document are defined in ``setting.py``, with ``order`` then ``sd_order`` variables.

Moreover, part of speech authorised values have been deeply extended by modifying the ``ps_partOfSpeech`` Python variable.

Tutorial
==========

Configuration files
_______________________

This part is an overview of the configuration files you may have to customise.

* ``config.xml``

The root element is named ``Config``. It contains following elements that user has to set.

	``Language``: define the vernacular, national, regional and other languages that you have to use in your multi-languages dictionary, by setting the ISO-639-3 code value (usually composed of three letters).

	``Font``: define fonts to use for LaTeX output format if needed ; for each defined language, a font has to be defined using LaTeX commands.

	``LMF``: define ``GlobalInformation`` and ``Lexicon`` attributes of ``LexicalResource`` (author, version, dictionary description and title, identifier, etc.) ; among these settings, two are very important to define: ``entrySource`` must point to the dictionary MDF input file, and ``localPath`` must point to the folder where your audio files are located if you have any.

	``MDF``: here you can define your own part of speech values if you do not use standard ones defined in MDF.

	``LaTeX``: not implemented.

* ``introduction.tex``

If user wants to insert an introduction in his dictionary, here is the file to write it. It has to use LaTeX commands.

* ``preamble.tex``

This file is used to define all LaTeX packages that will be needed to compile your LaTeX output file. You have to update it if you customise the ``lmf2tex()`` function by using non-basic LaTeX commands.

* ``sort_order.xml``

If you want your dictionary classified by a specific alphabetical order or if you use IPA or special characters, you have to write your own ``sort_order.xml`` file. Format is simple: for each character, you have to define a rank value.

For any of the settings defined above, please refer to examples for the exact syntax to respect.

Library options
______________________

The library provides several options. There are all described in the help menu, that you can display by running for instance:
::

	$ python examples/Bambara/bambara.py -h

Code warnings
____________________

While running your Python script, you may notice that lots of warning messages are generated by the library. Indeed, all values that are not defined in your configuration files or allowed by the MDF or LMF standards are reported, as part of speech and paradigm label values. Note that it does not block the script execution. The library also reports unresolved cross references and sound files that are not found.

Execution errors
______________________

Any error will raise a Python exception, giving some details about the cause.
