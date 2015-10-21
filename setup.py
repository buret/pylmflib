#! /usr/bin/env python
# -*- coding: utf-8 -*-

from distutils.core import setup
import pylmflib

setup(name='pylmflib',
    version=pylmflib.wrapper.__version__,
    description='Python LMF library',
    long_description=open('README.rst').read(),
    author='Céline Buret',
    author_email='buret.celine@gmail.com',
    #install_requires=["docx", "odf"],
    classifiers=['Development Status :: 5 - Production/Stable',
                 'Environment :: Console',
                 'Intended Audience :: Developers',
                 'Intended Audience :: End Users/Desktop',
                 'Intended Audience :: Science/Research',
                 'License :: OSI Approved :: GNU General Public License (GPL)',
                 'Natural Language :: English',
                 'Operating System :: OS Independent',
                 'Programming Language :: Python :: 2.7',
                 'Topic :: Scientific/Engineering'],
    url='https://github.com/buret/pylmflib',
    py_modules=['pylmflib.wrapper'],
    package_dir={'' : '.'},
    packages=['pylmflib', 'pylmflib.common', 'pylmflib.config', 'pylmflib.core', 'pylmflib.input', 'pylmflib.morphology', 'pylmflib.morphosyntax', 'pylmflib.mrd', 'pylmflib.output', 'pylmflib.resources', 'pylmflib.utils', 'pylmflib.utils.eol', 'pylmflib.utils.ipa2sampa', 'pylmflib.utils.tables', 'pylmflib.utils.uid'],
    package_data={'pylmflib.utils.ipa2sampa' : ['sampa.csv', 'token.test']},
    data_files=[('bitmaps', ['pylmflib/output/img/sound.jpg'])],
    scripts=['pylmflib/utils/ipa2devanagari/ipa2devanagari.pl', 'pylmflib/utils/ipa2devanagari/ipa2devanagari.pl', 'pylmflib/utils/paradigms/paradigms_eng.pl', 'pylmflib/utils/paradigms/paradigms.pl', 'pylmflib/utils/paradigms/reflexive_paradigms_eng.pl', 'pylmflib/utils/paradigms/reflexive_paradigms.pl', 'pylmflib/utils/lmf2htm/htm.xsl', 'pylmflib/utils/lmf2tei/lmf2tei.xsl']
)
