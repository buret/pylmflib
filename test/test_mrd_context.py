#! /usr/bin/env python

from startup import *
from mrd.context import Context
from core.text_representation import TextRepresentation

## Test Context class

class TestContextFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Context object
        self.context = Context()

    def tearDown(self):
        # Release instantiated objects
        del self.context

    def test_init(self):
        self.assertIsNone(self.context.language)
        self.assertIsNone(self.context.type)
        self.assertListEqual(self.context.text_representation, [])
        self.assertIsNone(self.context.targets)
        self.assertIsNone(self.context.get_speaker())

    def test_set_type(self):
        typ = "proverb"
        self.assertIs(self.context.set_type(typ), self.context)
        self.assertEqual(self.context.type, typ)
        # Test error case
        typ = "whatever"
        self.context.set_type(typ)

    def test_get_type(self):
        typ = "type"
        self.context.type = typ
        self.assertEqual(self.context.get_type(), typ)

    def test_text_representation(self):
        # Test create text representation
        repr = self.context.create_text_representation()
        self.assertIsInstance(repr, TextRepresentation)
        # Release TextRepresentation instance
        del repr

    def test_add_text_representation(self):
        # Create text representations
        text = TextRepresentation()
        repr = TextRepresentation()
        # Test add text representations to the context
        self.assertIs(self.context.add_text_representation(text), self.context)
        self.assertListEqual(self.context.text_representation, [text])
        self.assertIs(self.context.add_text_representation(repr), self.context)
        self.assertListEqual(self.context.text_representation, [text, repr])
        # Release TextRepresentation instances
        del self.context.text_representation[:]
        del text, repr

    def test_get_text_representations(self):
        # List of TextRepresentation instances is empty
        self.assertListEqual(self.context.get_text_representations(), [])
        # Create TextRepresentation instances and add them to the list
        text = TextRepresentation()
        repr = TextRepresentation()
        self.context.text_representation = [text, repr]
        # Test get text representations
        self.assertListEqual(self.context.get_text_representations(), [text, repr])
        # Delete TextRepresentation instances
        del self.context.text_representation[:]
        del text, repr

    def test_get_last_text_representation(self):
        # List of TextRepresentation instances is empty
        self.assertIsNone(self.context.get_last_text_representation())
        # Create TextRepresentation instances and add them to the list
        text = TextRepresentation()
        repr = TextRepresentation()
        self.context.text_representation = [text, repr]
        # Test get last text representation
        self.assertIs(self.context.get_last_text_representation(), repr)
        self.context.text_representation.pop()
        self.assertIs(self.context.get_last_text_representation(), text)
        # Release TextRepresentation instances
        del self.context.text_representation[:]
        del text, repr

    def test_find_written_forms(self):
        # List of TextRepresentation instances is empty
        self.assertListEqual(self.context.find_written_forms(), [])
        # Create TextRepresentation instances and add them to the list
        text = TextRepresentation()
        repr = TextRepresentation()
        self.context.text_representation = [text, repr]
        # Set their written form and language
        form1 = "form1"
        form2 = "form2"
        lang = "lang"
        text.writtenForm = form1
        text.language = lang
        # Test find written forms
        self.assertListEqual(self.context.find_written_forms(), [form1])
        repr.writtenForm = form2
        self.assertListEqual(self.context.find_written_forms(), [form1, form2])
        # Test with a language filter
        self.assertListEqual(self.context.find_written_forms("eng"), [])
        self.assertListEqual(self.context.find_written_forms(lang), [form1])
        # Release TextRepresentation instances
        del self.context.text_representation[:]
        del text, repr

    def test_get_comments(self):
        # List of TextRepresentation instances is empty
        self.assertListEqual(self.context.get_comments(), [])
        # Create TextRepresentation instances and add them to the list
        text = TextRepresentation()
        repr = TextRepresentation()
        self.context.text_representation = [text, repr]
        # Set their comment
        comment1 = "comment1"
        comment2 = "comment2"
        text.comment = comment1
        # Test get comments
        self.assertListEqual(self.context.get_comments(), [comment1])
        repr.comment = comment2
        self.assertListEqual(self.context.get_comments(), [comment1, comment2])
        # Release TextRepresentation instances
        del self.context.text_representation[:]
        del text, repr

    def test_set_written_form(self):
        form = "written"
        self.assertIs(self.context.set_written_form(form), self.context)
        self.assertEqual(len(self.context.text_representation), 1)
        self.assertEqual(self.context.text_representation[0].writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.context.set_written_form(form, lang), self.context)
        self.assertEqual(len(self.context.text_representation), 2)
        self.assertEqual(self.context.text_representation[1].writtenForm, form)
        self.assertEqual(self.context.text_representation[1].language, lang)

    def test_set_comment(self):
        comment = "comment1"
        # Test with an existing text representation
        repr = TextRepresentation()
        self.context.text_representation = [repr]
        self.assertIs(self.context.set_comment(comment), self.context)
        self.assertEqual(len(self.context.text_representation), 1)
        self.assertEqual(self.context.text_representation[0].comment, comment)
        # Test with a new text representation to create
        comment = "comment2"
        self.assertIs(self.context.set_comment(comment), self.context)
        self.assertEqual(len(self.context.text_representation), 2)
        self.assertEqual(self.context.text_representation[1].comment, comment)
        # Release TextRepresentation instance
        del repr

    def test_get_speakerID(self):
        id = "toto"
        self.context.targets = id
        self.assertEqual(self.context.get_speakerID(), id)

suite = unittest.TestLoader().loadTestsFromTestCase(TestContextFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
