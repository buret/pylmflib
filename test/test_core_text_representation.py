#! /usr/bin/env python

from startup import *
from core.text_representation import TextRepresentation

## Test TextRepresentation class

class TestTextRepresentationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a TextRepresentation object
        self.text_representation = TextRepresentation()

    def tearDown(self):
        # Release instantiated objects
        del self.text_representation

    def test_init(self):
        self.assertIsNone(self.text_representation.comment)
        self.assertIsNone(self.text_representation.writtenForm)
        self.assertIsNone(self.text_representation.language)
        self.assertIsNone(self.text_representation.font)

    def test_set_comment(self):
        comment = "comment"
        self.assertIs(self.text_representation.set_comment(comment), self.text_representation)
        self.assertEqual(self.text_representation.comment, comment)

    def test_get_comment(self):
        comment = "comment"
        self.text_representation.comment = comment
        self.assertEqual(self.text_representation.get_comment(), comment)

    def test_set_writtenForm(self):
        form = "written"
        self.assertIs(self.text_representation.set_writtenForm(form), self.text_representation)
        self.assertEqual(self.text_representation.writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.text_representation.set_writtenForm(form, lang), self.text_representation)
        self.assertEqual(self.text_representation.writtenForm, form)
        self.assertEqual(self.text_representation.language, lang)

    def test_get_writtenForm(self):
        self.assertIsNone(self.text_representation.get_writtenForm())
        form = "written"
        self.text_representation.writtenForm = form
        self.assertEqual(self.text_representation.get_writtenForm(), form)
        # Test with a language filter
        language = "eng"
        self.text_representation.language = language
        self.assertEqual(self.text_representation.get_writtenForm(), form)
        self.assertIsNone(self.text_representation.get_writtenForm("fra"))
        self.assertEqual(self.text_representation.get_writtenForm("eng"), form)

    def test_set_language(self):
        language = "English"
        self.assertIs(self.text_representation.set_language(language), self.text_representation)
        self.assertEqual(self.text_representation.language, language)

    def test_get_language(self):
        language = "language"
        self.text_representation.language = language
        self.assertEqual(self.text_representation.get_language(), language)

suite = unittest.TestLoader().loadTestsFromTestCase(TestTextRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
