#! /usr/bin/env python

from startup import *
from resources.picture import Picture

## Test Picture class

class TestPictureFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Picture object
        self.picture = Picture()

    def tearDown(self):
        # Release instantiated objects
        del self.picture

    def test_init(self):
        self.assertIsNone(self.picture.mediaType)
        self.assertIsNone(self.picture.fileName)
        self.assertIsNone(self.picture.author)
        self.assertIsNone(self.picture.filename)
        self.assertIsNone(self.picture.reference)
        self.assertIsNone(self.picture.width)
        self.assertIsNone(self.picture.height)
        self.assertIsNone(self.picture.format)
        self.assertListEqual(self.picture.statement, [])

suite = unittest.TestLoader().loadTestsFromTestCase(TestPictureFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
