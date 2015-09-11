#! /usr/bin/env python

from startup import *
from morphosyntax.paradigm import Paradigm

## Test Paradigm class

class TestParadigmFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Paradigm object
        self.paradigm = Paradigm()

    def tearDown(self):
        # Release instantiated objects
        del self.paradigm

    def test_init(self):
        self.assertIsNone(self.paradigm.paradigmLabel)
        self.assertIsNone(self.paradigm.paradigm)
        self.assertIsNone(self.paradigm.language)
        self.assertIsNone(self.paradigm.morphology)
        self.assertIsNone(self.paradigm.targets)
        self.assertIsNone(self.paradigm.get_lexical_entry())

    def test_set_paradigmLabel(self):
        label = "comitative"
        self.assertIs(self.paradigm.set_paradigmLabel(label), self.paradigm)
        self.assertEqual(self.paradigm.paradigmLabel, label)
        # Test error case
        self.paradigm.set_paradigmLabel(label)

    def test_get_paradigmLabel(self):
        label = "label"
        self.paradigm.paradigmLabel = label
        self.assertEqual(self.paradigm.get_paradigmLabel(), label)

    def test_set_paradigm(self):
        paradigm = "paradigm"
        self.assertIs(self.paradigm.set_paradigm(paradigm), self.paradigm)
        self.assertEqual(self.paradigm.paradigm, paradigm)

    def test_get_paradigm(self):
        self.assertIsNone(self.paradigm.get_paradigm())
        paradigm = "paradigm"
        self.paradigm.paradigm = paradigm
        self.assertEqual(self.paradigm.get_paradigm(), paradigm)
        # Test with a language filter
        language = "eng"
        self.paradigm.language = language
        self.assertEqual(self.paradigm.get_paradigm(), paradigm)
        self.assertIsNone(self.paradigm.get_paradigm("fra"))
        self.assertEqual(self.paradigm.get_paradigm("eng"), paradigm)

    def test_set_language(self):
        language = "English"
        self.assertIs(self.paradigm.set_language(language), self.paradigm)
        self.assertEqual(self.paradigm.language, language)

    def test_get_language(self):
        language = "language"
        self.paradigm.language = language
        self.assertEqual(self.paradigm.get_language(), language)

    def test_set_morphology(self):
        morphology = "morphology"
        self.assertIs(self.paradigm.set_morphology(morphology), self.paradigm)
        self.assertEqual(self.paradigm.morphology, morphology)

    def test_get_morphology(self):
        morphology = "morphology"
        self.paradigm.morphology = morphology
        self.assertEqual(self.paradigm.get_morphology(), morphology)

suite = unittest.TestLoader().loadTestsFromTestCase(TestParadigmFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
