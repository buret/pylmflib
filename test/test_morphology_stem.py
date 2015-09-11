#! /usr/bin/env python

from startup import *
from morphology.stem import Stem

## Test Stem class

class TestStemFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Stem object
        self.stem = Stem()

    def tearDown(self):
        # Release instantiated objects
        del self.stem

    def test_init(self):
        self.assertListEqual(self.stem.form_representation, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestStemFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
