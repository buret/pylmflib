#! /usr/bin/env python

from startup import *
from core.global_information import GlobalInformation

## Test GlobalInformation class

class TestGlobalInformationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a GlobalInformation object
        self.global_information = GlobalInformation()

    def tearDown(self):
        # Release instantiated objects
        del self.global_information

    def test_init(self):
        self.assertIsNone(self.global_information.languageCode)
        self.assertIsNone(self.global_information.author)
        self.assertIsNone(self.global_information.version)
        self.assertIsNone(self.global_information.lastUpdate)
        self.assertIsNone(self.global_information.license)
        self.assertIsNone(self.global_information.characterEncoding)
        self.assertIsNone(self.global_information.dateCoding)
        self.assertIsNone(self.global_information.creationDate)
        self.assertIsNone(self.global_information.projectName)
        self.assertIsNone(self.global_information.description)
        self.assertIsNone(self.global_information.bibliographicCitation)

    def test_set_languageCode(self):
        code = "iso"
        self.assertEqual(self.global_information.set_languageCode(code), self.global_information)
        self.assertEqual(self.global_information.languageCode, code)

    def test_get_languageCode(self):
        self.assertIs(self.global_information.get_languageCode(), self.global_information.languageCode)

    def test_set_version(self):
        version = "0"
        self.assertEqual(self.global_information.set_version(version), self.global_information)
        self.assertEqual(self.global_information.version, version)

    def test_get_version(self):
        self.assertIs(self.global_information.get_version(), self.global_information.version)

    def test_set_license(self):
        license = "free"
        self.assertEqual(self.global_information.set_license(license), self.global_information)
        self.assertEqual(self.global_information.license, license)

    def test_get_license(self):
        self.assertIs(self.global_information.get_license(), self.global_information.license)

    def test_set_characterEncoding(self):
        coding = "iso"
        self.assertEqual(self.global_information.set_characterEncoding(coding), self.global_information)
        self.assertEqual(self.global_information.characterEncoding, coding)

    def test_get_characterEncoding(self):
        self.assertIs(self.global_information.get_characterEncoding(), self.global_information.characterEncoding)

    def test_set_dateCoding(self):
        coding = "iso"
        self.assertEqual(self.global_information.set_dateCoding(coding), self.global_information)
        self.assertEqual(self.global_information.dateCoding, coding)

    def test_get_dateCoding(self):
        self.assertIs(self.global_information.get_dateCoding(), self.global_information.dateCoding)

    def test_set_projectName(self):
        name = "project"
        self.assertEqual(self.global_information.set_projectName(name), self.global_information)
        self.assertEqual(self.global_information.projectName, name)

    def test_get_projectName(self):
        self.assertIs(self.global_information.get_projectName(), self.global_information.projectName)

    def test_set_creationDate(self):
        date = "2014-10-08"
        self.assertEqual(self.global_information.set_creationDate(date), self.global_information)
        self.assertEqual(self.global_information.creationDate, date)
        
    def test_get_creationDate(self):
        self.assertIs(self.global_information.get_creationDate(), self.global_information.creationDate)

    def test_set_lastUpdate(self):
        date = "2014-10-08"
        self.assertEqual(self.global_information.set_lastUpdate(date), self.global_information)
        self.assertEqual(self.global_information.lastUpdate, date)

    def test_get_lastUpdate(self):
        self.assertIs(self.global_information.get_lastUpdate(), self.global_information.lastUpdate)

    def test_set_author(self):
        author = "My Name"
        self.assertEqual(self.global_information.set_author(author), self.global_information)
        self.assertEqual(self.global_information.author, author)

    def test_get_author(self):
        self.assertIs(self.global_information.get_author(), self.global_information.author)

    def test_set_description(self):
        descr = "This is a short description of the lexical resource."
        self.assertEqual(self.global_information.set_description(descr), self.global_information)
        self.assertEqual(self.global_information.description, descr)

    def test_get_description(self):
        self.assertIs(self.global_information.get_description(), self.global_information.description)

    def test_compute_bibliographicCitation(self):
        self.global_information.author = "CNRS"
        self.global_information.lastUpdate = "2014"
        # Test compute bibliographic citation
        self.global_information.compute_bibliographicCitation()
        self.assertEqual(self.global_information.bibliographicCitation, "Online dictionaries, CNRS, 2014")

    def test_get_bibliographicCitation(self):
        self.assertIs(self.global_information.get_bibliographicCitation(), self.global_information.bibliographicCitation)

suite = unittest.TestLoader().loadTestsFromTestCase(TestGlobalInformationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
