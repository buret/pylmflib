#! /usr/bin/env python

from startup import *
from resources.speaker import Speaker

## Test Speaker class

class TestSpeakerFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Speaker object
        self.speaker = Speaker()

    def tearDown(self):
        # Release instantiated objects
        del self.speaker

    def test_init(self):
        self.assertIsNone(self.speaker.name)
        self.assertIsNone(self.speaker.anonymizationFlag)
        self.assertIsNone(self.speaker.reference)
        self.assertIsNone(self.speaker.source)
        self.assertIsNone(self.speaker.speakerID)

suite = unittest.TestLoader().loadTestsFromTestCase(TestSpeakerFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
