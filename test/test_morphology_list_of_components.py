#! /usr/bin/env python

from startup import *
from morphology.list_of_components import ListOfComponents

## Test ListOfComponents class

class TestListOfComponentsFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a ListOfComponents object
        self.list_of_components = ListOfComponents()

    def tearDown(self):
        # Release instantiated objects
        del self.list_of_components

    def test_init(self):
        self.assertListEqual(self.list_of_components.component, [])

    def test_create_and_add_component(self):
        # Test create and add components to the list
        lexeme = "lexeme1"
        position = 1
        self.assertIs(self.list_of_components.create_and_add_component(position, lexeme), self.list_of_components)
        self.assertEqual(len(self.list_of_components.get_components()), 1)
        self.assertEqual(self.list_of_components.component[0].targets, lexeme)
        lexeme = "lexeme2"
        position = 2
        self.assertIs(self.list_of_components.create_and_add_component(position, lexeme), self.list_of_components)
        self.assertEqual(len(self.list_of_components.get_components()), 2)
        self.assertEqual(self.list_of_components.component[1].targets, lexeme)
        # Release Component instances
        del self.list_of_components.component[1], self.list_of_components.component[0]

    def test_get_components(self):
        # Add components to the list
        lexeme1 = "first"
        position1 = 1
        lexeme2 = "second"
        position2 = 2
        self.list_of_components.create_and_add_component(position1, lexeme1)
        self.list_of_components.create_and_add_component(position2, lexeme2)
        # Test get components
        self.assertEqual(self.list_of_components.get_components(), [self.list_of_components.component[0], self.list_of_components.component[1]])
        # Release Component instances
        del self.list_of_components.component[1], self.list_of_components.component[0]

suite = unittest.TestLoader().loadTestsFromTestCase(TestListOfComponentsFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
