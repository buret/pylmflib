#! /usr/bin/env python

from startup import *
from resources.video import Video

## Test Video class

class TestVideoFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Video object
        self.video = Video()

    def tearDown(self):
        # Release instantiated objects
        del self.video

    def test_init(self):
        self.assertIsNone(self.video.mediaType)
        self.assertIsNone(self.video.fileName)
        self.assertIsNone(self.video.author)
        self.assertIsNone(self.video.description)

suite = unittest.TestLoader().loadTestsFromTestCase(TestVideoFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
