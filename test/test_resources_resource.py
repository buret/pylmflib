#! /usr/bin/env python

from startup import *
from resources.resource import Resource

## Test Resource class

class TestResourceFunctions(unittest.TestCase, Resource):

    def setUp(self):
        # Try to instantiate a Resource object
        test = False
        try:
            Resource()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def tearDown(self):
        # Try to release a Resource object
        test = False
        try:
            self.__del__()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_init(self):
        Resource.__call__(self)

suite = unittest.TestLoader().loadTestsFromTestCase(TestResourceFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
