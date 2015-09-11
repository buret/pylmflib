#! /usr/bin/env python

from startup import *
from resources.audio import Audio

## Test Audio class

class TestAudioFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate an Audio object
        self.audio = Audio()

    def tearDown(self):
        # Release instantiated objects
        del self.audio

    def test_init(self):
        self.assertIsNone(self.audio.mediaType)
        self.assertIsNone(self.audio.fileName)
        self.assertIsNone(self.audio.author)
        self.assertIsNone(self.audio.quality)
        self.assertIsNone(self.audio.sound)
        self.assertIsNone(self.audio.startPosition)
        self.assertIsNone(self.audio.durationOfEffectiveSpeech)
        self.assertIsNone(self.audio.externalReference)
        self.assertIsNone(self.audio.audioFileFormat)
        self.assertIsNone(self.audio.transcription)

    def test_set_mediaType(self):
        # Test error case
        self.audio.set_mediaType("whatever")
        # Test nominal case
        media_type = "audio"
        self.assertIs(self.audio.set_mediaType(media_type), self.audio)
        self.assertEqual(self.audio.mediaType, media_type)

    def test_get_mediaType(self):
        # Set media type
        media_type = "whatever"
        self.audio.mediaType = media_type
        # Test get media type
        self.assertEqual(self.audio.get_mediaType(), media_type)

    def test_set_fileName(self):
        name = "file"
        self.assertIs(self.audio.set_fileName(name), self.audio)
        self.assertEqual(self.audio.fileName, name)

    def test_get_fileName(self):
        name = "name"
        self.audio.fileName = name
        self.assertEqual(self.audio.get_fileName(), name)

    def test_set_author(self):
        name = "My Name"
        self.assertIs(self.audio.set_author(name), self.audio)
        self.assertEqual(self.audio.author, name)

    def test_get_author(self):
        name = "Your Name"
        self.audio.author = name
        self.assertEqual(self.audio.get_author(), name)

    def test_set_quality(self):
        # Test error case
        self.audio.set_quality("whatever")
        # Test nominal case
        quality = "good"
        self.assertIs(self.audio.set_quality(quality), self.audio)
        self.assertEqual(self.audio.quality, quality)

    def test_get_quality(self):
        quality = "whatever"
        self.audio.quality = quality
        self.assertEqual(self.audio.get_quality(), quality)

    def test_set_sound(self):
        sound = "sound"
        self.assertIs(self.audio.set_sound(sound), self.audio)
        self.assertEqual(self.audio.sound, sound)

    def test_get_sound(self):
        sound = "something"
        self.audio.sound = sound
        self.assertEqual(self.audio.get_sound(), sound)

    def test_set_transcription(self):
        transcription = "transcription"
        self.assertIs(self.audio.set_transcription(transcription), self.audio)
        self.assertEqual(self.audio.transcription, transcription)
    
    def test_get_transcription(self):
        trans = "trans"
        self.audio.transcription = trans
        self.assertEqual(self.audio.get_transcription(), trans)

    def test_set_startPosition(self):
        # Test error case
        self.audio.set_startPosition("0h00")
        # Test nominal case
        start = "00:00:00"
        self.assertIs(self.audio.set_startPosition(start), self.audio)
        self.assertEqual(self.audio.startPosition, 'T' + start)

    def test_get_startPosition(self):
        pos = "whatever"
        self.audio.startPosition = pos
        self.assertEqual(self.audio.get_startPosition(), pos)

    def test_set_durationOfEffectiveSpeech(self):
        # Test error case
        self.audio.set_durationOfEffectiveSpeech("0h00")
        # Test nominal case
        duration = "00H00M00S"
        self.assertIs(self.audio.set_durationOfEffectiveSpeech(duration), self.audio)
        self.assertEqual(self.audio.durationOfEffectiveSpeech,'P' + 'T' + duration)

    def test_get_durationOfEffectiveSpeech(self):
        duration = "whatever"
        self.audio.durationOfEffectiveSpeech = duration
        self.assertEqual(self.audio.get_durationOfEffectiveSpeech(), duration)

    def test_set_externalReference(self):
        ref = "ref"
        self.assertIs(self.audio.set_externalReference(ref), self.audio)
        self.assertEqual(self.audio.externalReference, ref)

    def test_get_externalReference(self):
        ref = "something"
        self.audio.externalReference = ref
        self.assertEqual(self.audio.get_externalReference(), ref)

    def test_set_audioFileFormat(self):
        format = "audio file"
        self.assertIs(self.audio.set_audioFileFormat(format), self.audio)
        self.assertEqual(self.audio.audioFileFormat, format)

    def test_get_audioFileFormat(self):
        format = "something"
        self.audio.audioFileFormat = format
        self.assertEqual(self.audio.get_audioFileFormat(), format)

suite = unittest.TestLoader().loadTestsFromTestCase(TestAudioFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
