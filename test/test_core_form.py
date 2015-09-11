#! /usr/bin/env python

from startup import *
from core.form import Form

## Test Form class

class TestFormFunctions(unittest.TestCase, Form):

    def setUp(self):
        # Try to instantiate a Form object
        test = False
        try:
            Form()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def tearDown(self):
        # Try to release a Form object
        test = False
        try:
            self.__del__()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_init(self):
        Form.__new__(self)
        self.assertListEqual(self.form_representation, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestFormFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
