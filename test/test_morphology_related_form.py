#! /usr/bin/env python

from startup import *
from morphology.related_form import RelatedForm
from core.lexical_entry import LexicalEntry
from core.form_representation import FormRepresentation

## Test RelatedForm class

class TestRelatedFormFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a RelatedForm object
        self.related_form = RelatedForm()

    def tearDown(self):
        # Release instantiated objects
        del self.related_form

    def test_init(self):
        self.assertListEqual(self.related_form.form_representation, [])
        self.assertIsNone(self.related_form.semanticRelation)
        self.assertIsNone(self.related_form.targets)
        self.assertIsNone(self.related_form.get_lexical_entry())

    def test_set_semanticRelation(self):
        # Test error case
        self.related_form.set_semanticRelation("whatever")
        # Test nominal case
        relation = "homonym"
        self.assertIs(self.related_form.set_semanticRelation(relation), self.related_form)
        self.assertEqual(self.related_form.semanticRelation, relation)

    def test_get_semanticRelation(self):
        # Set semantic relation
        relation = "whatever"
        self.related_form.semanticRelation = relation
        # Test get semantic relation
        self.assertEqual(self.related_form.get_semanticRelation(), relation)

    def test_get_lexeme(self):
        # Set lexeme
        lexeme = "hello"
        self.related_form.targets = lexeme
        # Test get lexeme
        self.assertEqual(self.related_form.get_lexeme(), lexeme)

    def test_set_get_lexical_entry(self):
        # Create a lexical entry
        entry = LexicalEntry()
        # Test set lexical entry
        self.assertEqual(self.related_form.set_lexical_entry(entry), self.related_form)
        # Test get lexical entry
        self.assertEqual(self.related_form.get_lexical_entry(), entry)
        # Test lexical entry modifications
        entry.lexeme = "toto"
        self.assertEqual(self.related_form.get_lexical_entry().lexeme, "toto")
        # Release lexical entry
        del entry

    def test_create_and_add_form_representations(self):
        # Test create and add form representations to the related form
        form = "form1"
        language = "lang1"
        self.assertIs(self.related_form.create_and_add_form_representation(form, language), self.related_form)
        self.assertEqual(len(self.related_form.form_representation), 1)
        self.assertEqual(self.related_form.form_representation[0].writtenForm, form)
        self.assertEqual(self.related_form.form_representation[0].language, language)
        form = "form2"
        language = "lang2"
        self.assertIs(self.related_form.create_and_add_form_representation(form, language), self.related_form)
        self.assertEqual(len(self.related_form.form_representation), 2)
        self.assertEqual(self.related_form.form_representation[1].writtenForm, form)
        self.assertEqual(self.related_form.form_representation[1].language, language)
        # Release FormRepresentation instances
        del self.related_form.form_representation[1], self.related_form.form_representation[0]

    def test_find_written_forms(self):
        # Create several form representations with different languages
        form1 = FormRepresentation().set_language("langA")
        form2 = FormRepresentation().set_language("langB")
        form3 = FormRepresentation().set_language("langA")
        form4 = FormRepresentation().set_language("langC")
        # Add form representations to the related form
        self.related_form.form_representation = [form1, form2, form3, form4]
        # Test find form representations
        self.assertListEqual(self.related_form.find_written_forms("langB"), [form2.writtenForm])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.related_form.find_written_forms("langA")), set([form1.writtenForm, form3.writtenForm]))
        # Release FormRepresentation instances
        del self.related_form.form_representation[:]
        del form1, form2, form3, form4

suite = unittest.TestLoader().loadTestsFromTestCase(TestRelatedFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
