#! /usr/bin/env python

from startup import *
from input.xml_lmf import compute_name, factory, xml_lmf_read, get_sub_elements
from core.lexical_entry import LexicalEntry
from utils.xml_format import Element, SubElement

## Test XML LMF functions

class TestXmlLmfFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_compute_name(self):
        self.assertEqual(compute_name("Lexicon"), "lexicon")
        self.assertEqual(compute_name("LexicalEntry"), "lexical_entry")

    def test_factory(self):
        sys.path[0] = sys.path[0] + "/../examples/test"
        entry = factory('LexicalEntry', {'partOfSpeech': 'n'})
        self.assertEqual(entry.__class__.__name__, 'LexicalEntry')
        self.assertEqual(entry.partOfSpeech, 'n')

    def test_xml_lmf_read(self):
        import sys, os
        # Create an input XML LMF file
        utest_path = sys.path[0] + '/'
        xml_lmf_filename = utest_path + "lmf_input.xml"
        xml_lmf_file = open(xml_lmf_filename, "w+")
        xml_lmf_file.write("""<LexicalEntry><Lemma><feat att="lexeme" val="hello"/></Lemma><feat att="partOfSpeech" val="toto"/><feat att="status" val="draft"/></LexicalEntry>""")
        xml_lmf_file.close()
        # Read XML LMF file and test result
        entry = xml_lmf_read(xml_lmf_filename)
        self.assertEqual(entry.get_lexeme(), "hello")
        self.assertEqual(entry.get_partOfSpeech(), "toto")
        self.assertEqual(entry.get_status(), "draft")
        del entry
        # Remove XML LMF file
        os.remove(xml_lmf_filename)

    def test_get_sub_elements(self):
        # Declare instance and prepare XML element with its sub-elements
        instance = LexicalEntry()
        element = Element("LexicalEntry")
        lemma = SubElement(element, "Lemma")
        SubElement(lemma, "feat", att="lexeme", val="hello")
        SubElement(element, "feat", att="partOfSpeech", val="toto")
        SubElement(element, "feat", att="status", val="draft")
        # Test results
        get_sub_elements(instance, element)
        self.assertEqual(instance.get_lexeme(), "hello")
        self.assertEqual(instance.get_partOfSpeech(), "toto")
        self.assertEqual(instance.get_status(), "draft")
        del instance, element, lemma

suite = unittest.TestLoader().loadTestsFromTestCase(TestXmlLmfFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
