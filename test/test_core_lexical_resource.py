#! /usr/bin/env python

from startup import *
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from core.global_information import GlobalInformation

## Test LexicalResource class

class TestLexicalResourceFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalResource object
        self.lexical_resource = LexicalResource()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_resource

    def test_init(self):
        self.assertEqual(self.lexical_resource.dtdVersion, 16)
        self.assertIsInstance(self.lexical_resource.global_information, GlobalInformation)
        self.assertListEqual(self.lexical_resource.lexicon, [])
        self.assertListEqual(self.lexical_resource.speaker, [])

    def test_get_lexicons(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Add lexicons to the lexical resource
        self.lexical_resource.lexicon = [lexicon1, lexicon2]
        # Test get lexicons
        self.assertListEqual(self.lexical_resource.get_lexicons(), [lexicon1, lexicon2])
        # Release Lexicon instances
        del self.lexical_resource.lexicon[:]
        del lexicon1, lexicon2

    def test_add_lexicon(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Test add lexicons to the lexical resource
        self.assertEqual(self.lexical_resource.add_lexicon(lexicon1), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon1])
        self.assertEqual(self.lexical_resource.add_lexicon(lexicon2), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon1, lexicon2])
        # Release Lexicon instances
        del self.lexical_resource.lexicon[:]
        del lexicon1, lexicon2

    def test_remove_lexicon(self):
        # Create lexicons
        lexicon1 = Lexicon()
        lexicon2 = Lexicon()
        # Add lexicons to the lexical resource
        self.lexical_resource.lexicon = [lexicon1, lexicon2]
        # Test remove lexicons
        self.assertEqual(self.lexical_resource.remove_lexicon(lexicon1), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [lexicon2])
        self.assertEqual(self.lexical_resource.remove_lexicon(lexicon2), self.lexical_resource)
        self.assertListEqual(self.lexical_resource.lexicon, [])
        # Release Lexicon instances
        del lexicon1, lexicon2

    def test_get_lexicon(self):
        # Create lexicons
        lexicon1 = Lexicon("lexicon1")
        lexicon2 = Lexicon("lexicon2")
        # Add lexicons to the lexical resource
        self.lexical_resource.lexicon = [lexicon1, lexicon2]
        # Test get lexicon
        self.assertIsNone(self.lexical_resource.get_lexicon("unknown identifier"))
        self.assertEqual(self.lexical_resource.get_lexicon("lexicon2"), lexicon2)
        # Release Lexicon instances
        del lexicon1, lexicon2

    def test_set_dtdVersion(self):
        version = "0"
        self.assertEqual(self.lexical_resource.set_dtdVersion(version), self.lexical_resource)
        self.assertEqual(self.lexical_resource.dtdVersion, version)

    def test_get_dtdVersion(self):
        self.assertIs(self.lexical_resource.get_dtdVersion(), self.lexical_resource.dtdVersion)

    def test_set_language_code(self):
        code = "iso"
        self.assertEqual(self.lexical_resource.set_language_code(code), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.languageCode, code)

    def test_get_language_code(self):
        self.assertIs(self.lexical_resource.get_language_code(), self.lexical_resource.global_information.languageCode)

    def test_set_version(self):
        version = "0"
        self.assertEqual(self.lexical_resource.set_version(version), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.version, version)

    def test_get_version(self):
        self.assertIs(self.lexical_resource.get_version(), self.lexical_resource.global_information.version)

    def test_set_license(self):
        license = "free"
        self.assertEqual(self.lexical_resource.set_license(license), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.license, license)

    def test_get_license(self):
        self.assertIs(self.lexical_resource.get_license(), self.lexical_resource.global_information.license)

    def test_set_character_encoding(self):
        coding = "iso"
        self.assertEqual(self.lexical_resource.set_character_encoding(coding), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.characterEncoding, coding)

    def test_get_character_encoding(self):
        self.assertIs(self.lexical_resource.get_character_encoding(), self.lexical_resource.global_information.characterEncoding)

    def test_set_date_coding(self):
        coding = "iso"
        self.assertEqual(self.lexical_resource.set_date_coding(coding), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.dateCoding, coding)

    def test_get_date_coding(self):
        self.assertIs(self.lexical_resource.get_date_coding(), self.lexical_resource.global_information.dateCoding)

    def test_set_project_name(self):
        name = "project"
        self.assertEqual(self.lexical_resource.set_project_name(name), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.projectName, name)
    
    def test_get_project_name(self):
        self.assertIs(self.lexical_resource.get_project_name(), self.lexical_resource.global_information.projectName)

    def test_set_creation_date(self):
        date = "2014-10-08"
        self.assertEqual(self.lexical_resource.set_creation_date(date), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.creationDate, date)

    def test_get_creation_date(self):
        self.assertIs(self.lexical_resource.get_creation_date(), self.lexical_resource.global_information.creationDate)

    def test_set_last_update(self):
        date = "2014-10-10"
        self.assertEqual(self.lexical_resource.set_last_update(date), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.lastUpdate, date)

    def test_get_last_update(self):
        self.assertIs(self.lexical_resource.get_last_update(), self.lexical_resource.global_information.lastUpdate)

    def test_set_author(self):
        author = "My Name"
        self.assertEqual(self.lexical_resource.set_author(author), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.author, author)

    def test_get_author(self):
        self.assertIs(self.lexical_resource.get_author(), self.lexical_resource.global_information.author)

    def test_set_description(self):
        descr = "This is a short description of this lexical resource."
        self.assertEqual(self.lexical_resource.set_description(descr), self.lexical_resource)
        self.assertEqual(self.lexical_resource.global_information.description, descr)

    def test_get_description(self):
        self.assertIs(self.lexical_resource.get_description(), self.lexical_resource.global_information.description)

    def test_get_bibliographic_citation(self):
        self.assertIs(self.lexical_resource.get_bibliographic_citation(), self.lexical_resource.global_information.bibliographicCitation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
