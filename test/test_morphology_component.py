#! /usr/bin/env python

from startup import *
from morphology.component import Component
from core.lexical_entry import LexicalEntry

## Test Component class

class TestComponentFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Component object
        self.component = Component()

    def tearDown(self):
        # Release instantiated objects
        del self.component

    def test_init(self):
        self.assertIsNone(self.component.position)
        self.assertIsNone(self.component.targets)
        self.assertIsNone(self.component.get_lexical_entry())

    def test_set_get_lexical_entry(self):
        # Create a lexical entry
        entry = LexicalEntry()
        # Test set lexical entry
        self.assertEqual(self.component.set_lexical_entry(entry), self.component)
        # Test get lexical entry
        self.assertEqual(self.component.get_lexical_entry(), entry)
        # Test lexical entry modifications
        entry.lexeme = "toto"
        self.assertEqual(self.component.get_lexical_entry().lexeme, "toto")
        # Release lexical entry
        del entry

    def test_get_lexeme(self):
        # Set lexeme
        lexeme = "hello"
        self.component.targets = lexeme
        # Test get lexeme
        self.assertEqual(self.component.get_lexeme(), lexeme)

suite = unittest.TestLoader().loadTestsFromTestCase(TestComponentFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
