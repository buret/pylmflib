#! /usr/bin/env python

from startup import *
from mrd.equivalent import Equivalent

## Test Equivalent class

class TestEquivalentFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Equivalent object
        self.equivalent = Equivalent()

    def tearDown(self):
        # Release instantiated objects
        del self.equivalent

    def test_init(self):
        self.assertIsNone(self.equivalent.language)
        self.assertIsNone(self.equivalent.translation)
        self.assertListEqual(self.equivalent.text_representation, [])

    def test_set_translation(self):
        trans = "trans"
        self.assertIs(self.equivalent.set_translation(trans), self.equivalent)
        self.assertEqual(self.equivalent.translation, trans)
        # Test with language
        trans = "trans with lang"
        lang = "lang"
        self.assertIs(self.equivalent.set_translation(trans, lang), self.equivalent)
        self.assertEqual(self.equivalent.translation, trans)
        self.assertEqual(self.equivalent.language, lang)

    def test_get_translation(self):
        self.assertIsNone(self.equivalent.get_translation())
        trans = "trans"
        self.equivalent.translation = trans
        self.assertEqual(self.equivalent.get_translation(), trans)
        # Test with a language filter
        language = "eng"
        self.equivalent.language = language
        self.assertEqual(self.equivalent.get_translation(), trans)
        self.assertIsNone(self.equivalent.get_translation("fra"))
        self.assertEqual(self.equivalent.get_translation("eng"), trans)

    def test_set_language(self):
        language = "English"
        self.assertIs(self.equivalent.set_language(language), self.equivalent)
        self.assertEqual(self.equivalent.language, language)

    def test_get_language(self):
        language = "language"
        self.equivalent.language = language
        self.assertEqual(self.equivalent.get_language(), language)

suite = unittest.TestLoader().loadTestsFromTestCase(TestEquivalentFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
