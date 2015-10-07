#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *
from output.odt import *
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from core.sense import Sense
from utils.io import EOL

## Test odt functions

class TestOdtFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_file_read(self):
        import sys, os
        # Create an introduction text file
        utest_path = sys.path[0] + '/'
        txt_filename = utest_path + "intro.txt"
        txt_file = open(txt_filename, "w+")
        intro = "Introduction" + EOL + "This is my introduction" + EOL
        txt_file.write(intro)
        txt_file.close()
        # Read intro file and test result
        self.assertEqual(file_read(txt_filename), intro)
        # Remove text file
        os.remove(txt_filename)

    def test_odt_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        lexicon = Lexicon()
        lexicon.add_lexical_entry(lexical_entry)
        lexical_resource = LexicalResource()
        lexical_resource.add_lexicon(lexicon)
        # Write document file and test result
        utest_path = sys.path[0] + '/'
        odt_filename = utest_path + "output.odt"
        odt_write(lexical_resource, odt_filename)
        odt_file = open(odt_filename, "r")
        odt_file.readlines()
        odt_file.close()
        # Customize mapping
        def lmf2odt(lexicon, document, items, sort_order, paradigms, reverse):
            return "test"
        # Write document file and test result
        odt_write(lexical_resource, odt_filename, None, lmf2odt)
        odt_file = open(odt_filename, "r")
        odt_file.readlines()
        odt_file.close()
        del lexical_entry.lemma
        lexical_entry.lemma = None
        del lexical_entry, lexicon
        lexicon = None
        del lexical_resource
        # Remove document file
        os.remove(odt_filename)

suite = unittest.TestLoader().loadTestsFromTestCase(TestOdtFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
