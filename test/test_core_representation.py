#! /usr/bin/env python

from startup import *
from core.representation import Representation

## Test Representation class

class TestRepresentationFunctions(unittest.TestCase, Representation):

    def setUp(self):
        # Try to instantiate a Representation object
        test = False
        try:
            Representation()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def tearDown(self):
        # Try to release a Representation object
        test = False
        try:
            self.__del__()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_init(self):
        Representation.__new__(self)
        self.assertIsNone(self.comment)
        self.assertIsNone(self.writtenForm)
        self.assertIsNone(self.language)

suite = unittest.TestLoader().loadTestsFromTestCase(TestRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
