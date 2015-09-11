#! /usr/bin/env python

from startup import *
from resources.material import Material

## Test Material class

class TestMaterialFunctions(unittest.TestCase, Material):

    def setUp(self):
        # Try to instantiate a Material object
        test = False
        try:
            Material()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def tearDown(self):
        # Try to release a Material object
        test = False
        try:
            Material.__del__(self)
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_init(self):
        Material.__new__(self)
        self.assertIsNone(self.mediaType)
        self.assertIsNone(self.fileName)
        self.assertIsNone(self.author)

suite = unittest.TestLoader().loadTestsFromTestCase(TestMaterialFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
