#! /usr/bin/env python

from startup import *
from resources.human_resource import HumanResource

## Test HumanResource class

class TestHumanResourceFunctions(unittest.TestCase, HumanResource):

    def setUp(self):
        # Try to instantiate a HumanResource object
        test = False
        try:
            HumanResource()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def tearDown(self):
        # Try to release a HumanResource object
        test = False
        try:
            self.__del__()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_init(self):
        HumanResource.__new__(self)
        self.assertIsNone(self.name)
        self.assertIsNone(self.anonymizationFlag)
        self.assertIsNone(self.reference)
        self.assertIsNone(self.source)

suite = unittest.TestLoader().loadTestsFromTestCase(TestHumanResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
