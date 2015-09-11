#! /usr/bin/env python

from startup import *
from morphology.word_form import WordForm
from core.form_representation import FormRepresentation

## Test WordForm class

class TestWordFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a WordForm object
        self.word_form = WordForm()

    def tearDown(self):
        # Release instantiated objects
        del self.word_form

    def test_init(self):
        self.assertListEqual(self.word_form.form_representation, [])
        self.assertIsNone(self.word_form.grammaticalNumber)
        self.assertIsNone(self.word_form.grammaticalGender)
        self.assertIsNone(self.word_form.person)
        self.assertIsNone(self.word_form.anymacy)
        self.assertIsNone(self.word_form.clusivity)
        self.assertIsNone(self.word_form.tense)
        self.assertIsNone(self.word_form.case)
        self.assertIsNone(self.word_form.degree)
        self.assertIsNone(self.word_form.voice)
        self.assertIsNone(self.word_form.verbFormMood)

    def test_create_form_representation(self):
        # Test create form representation
        repr = self.word_form.create_form_representation()
        self.assertIsInstance(repr, FormRepresentation)
        # Release FormRepresentation instance
        del repr

    def test_add_form_representation(self):
        # Create form representations
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        # Test add form representations to the word form
        self.assertIs(self.word_form.add_form_representation(repr1), self.word_form)
        self.assertListEqual(self.word_form.form_representation, [repr1])
        self.assertIs(self.word_form.add_form_representation(repr2), self.word_form)
        self.assertListEqual(self.word_form.form_representation, [repr1, repr2])
        # Release FormRepresentation instances
        del self.word_form.form_representation[:]
        del repr1, repr2

    def test_get_form_representations(self):
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.word_form.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        self.word_form.form_representation = [repr1, repr2]
        # Test get form representations
        self.assertListEqual(self.word_form.get_form_representations(), [repr1, repr2])
        # Delete FormRepresentation instances
        del self.word_form.form_representation[:]
        del repr1, repr2

    def test_set_written_form(self):
        form = "written"
        self.assertIs(self.word_form.set_written_form(form), self.word_form)
        self.assertEqual(self.word_form.form_representation[0].writtenForm, form)
        script = "name"
        self.assertIs(self.word_form.set_written_form(form, script), self.word_form)
        self.assertEqual(self.word_form.form_representation[1].writtenForm, form)
        self.assertEqual(self.word_form.form_representation[1].scriptName, script)

    def test_get_written_forms(self):
        form1 = "written1"
        form2 = "written2"
        script1 = "name1"
        script2 = "name2"
        # There is no FormRepresentation
        self.assertListEqual(self.word_form.get_written_forms(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.writtenForm = form1
        repr1.scriptName = script1
        self.word_form.form_representation.append(repr1)
        self.assertEqual(self.word_form.get_written_forms(), [form1])
        self.assertEqual(self.word_form.get_written_forms(script1), [form1])
        repr2 = FormRepresentation()
        repr2.writtenForm = form2
        repr2.scriptName = script2
        self.word_form.form_representation.append(repr2)
        self.assertEqual(self.word_form.get_written_forms(), [form1, form2])
        self.assertEqual(self.word_form.get_written_forms(script2), [form2])
        # Release FormRepresentation instances
        del self.word_form.form_representation[:]
        del repr1, repr2

    def test_set_variant_form(self):
        form = "variant"
        self.assertIs(self.word_form.set_variant_form(form), self.word_form)
        self.assertEqual(self.word_form.form_representation[0].variantForm, form)

    def test_get_variant_forms(self):
        form1 = "variant1"
        form2 = "variant2"
        # There is no FormRepresentation
        self.assertListEqual(self.word_form.get_variant_forms(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.variantForm = form1
        self.word_form.form_representation.append(repr1)
        self.assertEqual(self.word_form.get_variant_forms(), [form1])
        repr2 = FormRepresentation()
        repr2.variantForm = form2
        self.word_form.form_representation.append(repr2)
        self.assertEqual(self.word_form.get_variant_forms(), [form1, form2])
        # Release FormRepresentation instances
        del self.word_form.form_representation[:]
        del repr1, repr2

    def test_set_person(self):
        person = 1
        self.assertEqual(self.word_form.set_person(person), self.word_form)
        self.assertEqual(self.word_form.person, "first person")
        # Test error case
        self.word_form.set_person("whatever")

    def test_get_person(self):
        self.assertIs(self.word_form.get_person(), self.word_form.person)

    def test_set_anymacy(self):
        anymacy = 4
        self.assertEqual(self.word_form.set_anymacy(anymacy), self.word_form)
        self.assertEqual(self.word_form.anymacy, "inanimate")
        # Test error case
        self.word_form.set_anymacy("whatever")

    def test_get_anymacy(self):
        self.assertIs(self.word_form.get_anymacy(), self.word_form.anymacy)

    def test_set_grammaticalNumber(self):
        nb = 'p'
        self.assertEqual(self.word_form.set_grammaticalNumber(nb), self.word_form)
        self.assertEqual(self.word_form.grammaticalNumber, "plural")
        # Test error case
        self.word_form.set_grammaticalNumber("whatever")

    def test_get_grammaticalNumber(self):
        self.assertIs(self.word_form.get_grammaticalNumber(), self.word_form.grammaticalNumber)

    def test_set_clusivity(self):
        clusivity = 'i'
        self.assertEqual(self.word_form.set_clusivity(clusivity), self.word_form)
        self.assertEqual(self.word_form.clusivity, "inclusive")
        # Test error case
        self.word_form.set_clusivity("whatever")

    def test_get_clusivity(self):
        self.assertIs(self.word_form.get_clusivity(), self.word_form.clusivity)

suite = unittest.TestLoader().loadTestsFromTestCase(TestWordFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
