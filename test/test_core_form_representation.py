#! /usr/bin/env python

from startup import *
from core.form_representation import FormRepresentation
from resources.audio import Audio

## Test FormRepresentation class

class TestFormRepresentationFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a FormRepresentation object
        self.form_representation = FormRepresentation()

    def tearDown(self):
        # Release instantiated objects
        del self.form_representation

    def test_init(self):
        self.assertIsNone(self.form_representation.comment)
        self.assertIsNone(self.form_representation.writtenForm)
        self.assertIsNone(self.form_representation.language)
        self.assertIsNone(self.form_representation.variantForm)
        self.assertIsNone(self.form_representation.type)
        self.assertIsNone(self.form_representation.transliteration)
        self.assertIsNone(self.form_representation.tone)
        self.assertIsNone(self.form_representation.geographicalVariant)
        self.assertIsNone(self.form_representation.phoneticForm)
        self.assertIsNone(self.form_representation.contextualVariation)
        self.assertIsNone(self.form_representation.spellingVariant)
        self.assertIsNone(self.form_representation.citationForm)
        self.assertIsNone(self.form_representation.dialect)
        self.assertIsNone(self.form_representation.language)
        self.assertIsNone(self.form_representation.scriptName)
        self.assertIsNone(self.form_representation.audio)
        self.assertIsNone(self.form_representation.targets)
        self.assertListEqual(self.form_representation.get_speakers(), [])

    def test_set_writtenForm(self):
        form = "written"
        self.assertIs(self.form_representation.set_writtenForm(form), self.form_representation)
        self.assertEqual(self.form_representation.writtenForm, form)
        script = "name"
        self.assertIs(self.form_representation.set_writtenForm(form, script), self.form_representation)
        self.assertEqual(self.form_representation.writtenForm, form)
        self.assertEqual(self.form_representation.scriptName, script)

    def test_get_writtenForm(self):
        # Set written form
        form = "hello"
        script = "bye"
        self.form_representation.writtenForm = form
        self.form_representation.scriptName = script
        # Test get written form
        self.assertEqual(self.form_representation.get_writtenForm(), form)
        self.assertIsNone(self.form_representation.get_writtenForm("byebye"))
        self.assertEqual(self.form_representation.get_writtenForm(script), form)

    def test_set_variantForm(self):
        form = "alternative"
        self.assertIs(self.form_representation.set_variantForm(form), self.form_representation)
        self.assertEqual(self.form_representation.variantForm, form)

    def test_get_variantForm(self):
        # Set variant form
        form = "hello"
        self.form_representation.variantForm = form
        # Test get variant form
        self.assertEqual(self.form_representation.get_variantForm(), form)

    def test_set_type(self):
        # Test error case
        self.form_representation.set_type("whatever")
        # Test nominal case
        variant_type = "phonetics"
        self.assertIs(self.form_representation.set_type(variant_type), self.form_representation)
        self.assertEqual(self.form_representation.type, variant_type)

    def test_get_type(self):
        # Set variant type
        variant_type = "whatever"
        self.form_representation.type = variant_type
        # Test get type
        self.assertEqual(self.form_representation.get_type(), variant_type)

    def test_set_comment(self):
        # Test error case
        self.form_representation.set_comment(0)
        # Test comment only
        comment = "blablabla"
        self.assertIs(self.form_representation.set_comment(comment), self.form_representation)
        self.assertEqual(self.form_representation.comment, comment)
        # Test comment and language
        comment = "This is a comment."
        language = "eng"
        self.assertIs(self.form_representation.set_comment(comment, language), self.form_representation)
        self.assertEqual(self.form_representation.comment, comment)
        self.assertEqual(self.form_representation.language, language)

    def test_get_comment(self):
        # Set comment
        comment = "whatever"
        self.form_representation.comment = comment
        # Test get comment
        self.assertEqual(self.form_representation.get_comment(), comment)
        # Test with a language filter
        language = "eng"
        self.form_representation.language = language
        self.assertEqual(self.form_representation.get_comment(), comment)
        self.assertIsNone(self.form_representation.get_comment("fra"))
        self.assertEqual(self.form_representation.get_comment(language), comment)

    def test_set_language(self):
        lang = "Python"
        self.assertIs(self.form_representation.set_language(lang), self.form_representation)
        self.assertEqual(self.form_representation.language, lang)
    
    def test_get_language(self):
        # Set language
        lang = "python"
        self.form_representation.language = lang
        # Test get language
        self.assertEqual(self.form_representation.get_language(), lang)

    def test_set_tone(self):
        tone = "TONE"
        self.assertIs(self.form_representation.set_tone(tone), self.form_representation)
        self.assertEqual(self.form_representation.tone, tone)

    def test_get_tone(self):
        # Set tone
        tone = "whatever"
        self.form_representation.tone = tone
        # Test get tone
        self.assertEqual(self.form_representation.get_tone(), tone)

    def test_set_geographicalVariant(self):
        geo = "GEO"
        self.assertIs(self.form_representation.set_geographicalVariant(geo), self.form_representation)
        self.assertEqual(self.form_representation.geographicalVariant, geo)

    def test_get_geographicalVariant(self):
        # Set geographical variant
        geo = "whatever"
        self.form_representation.geographicalVariant = geo
        # Test get geographical variant
        self.assertEqual(self.form_representation.get_geographicalVariant(), geo)

    def test_set_phoneticForm(self):
        phono = "PHONO"
        self.assertIs(self.form_representation.set_phoneticForm(phono), self.form_representation)
        self.assertEqual(self.form_representation.phoneticForm, phono)

    def test_get_phoneticForm(self):
        # Set phonetic form
        phono = "whatever"
        self.form_representation.phoneticForm = phono
        # Test get tone
        self.assertEqual(self.form_representation.get_phoneticForm(), phono)

    def test_set_contextualVariation(self):
        ctx = "CTX"
        self.assertIs(self.form_representation.set_contextualVariation(ctx), self.form_representation)
        self.assertEqual(self.form_representation.contextualVariation, ctx)

    def test_get_contextualVariation(self):
        # Set contextual variation
        ctx = "whatever"
        self.form_representation.contextualVariation = ctx
        # Test get contextual variation
        self.assertEqual(self.form_representation.get_contextualVariation(), ctx)

    def test_set_spellingVariant(self):
        spell = "SPELL"
        self.assertIs(self.form_representation.set_spellingVariant(spell), self.form_representation)
        self.assertEqual(self.form_representation.spellingVariant, spell)

    def test_get_spellingVariant(self):
        # Set spelling variant
        spell = "whatever"
        self.form_representation.spellingVariant = spell
        # Test get spelling variant
        self.assertEqual(self.form_representation.get_spellingVariant(), spell)

    def test_set_citationForm(self):
        cit = "CIT"
        self.assertIs(self.form_representation.set_citationForm(cit), self.form_representation)
        self.assertEqual(self.form_representation.citationForm, cit)

    def test_get_citationForm(self):
        # Set citation form
        cit = "whatever"
        self.form_representation.citationForm = cit
        # Test get citation form
        self.assertEqual(self.form_representation.get_citationForm(), cit)

    def test_set_dialect(self):
        dial = "DIAL"
        self.assertIs(self.form_representation.set_dialect(dial), self.form_representation)
        self.assertEqual(self.form_representation.dialect, dial)

    def test_get_dialect(self):
        # Set dialect
        dial = "whatever"
        self.form_representation.dialect = dial
        # Test get dialect
        self.assertEqual(self.form_representation.get_dialect(), dial)

    def test_set_transliteration(self):
        trans = "TRANS"
        self.assertIs(self.form_representation.set_transliteration(trans), self.form_representation)
        self.assertEqual(self.form_representation.transliteration, trans)

    def test_get_transliteration(self):
        # Set transliteration
        trans = "whatever"
        self.form_representation.transliteration = trans
        # Test get transliteration
        self.assertEqual(self.form_representation.get_transliteration(), trans)

    def test_set_scriptName(self):
        script = "SCRIPT"
        self.assertIs(self.form_representation.set_scriptName(script), self.form_representation)
        self.assertEqual(self.form_representation.scriptName, script)

    def test_get_scriptName(self):
        # Set script name
        script = "whatever"
        self.form_representation.scriptName = script
        # Test get script name
        self.assertEqual(self.form_representation.get_scriptName(), script)

    def test_create_audio(self):
        # Test create audio
        audio = self.form_representation.create_audio()
        self.assertIsInstance(audio, Audio)
        # Release Audio instance
        del audio

    def test_get_audio(self):
        # Create Audio instance
        audio = Audio()
        self.form_representation.audio = audio
        # Test get audio
        self.assertEqual(self.form_representation.get_audio(), audio)
        # Delete Audio instance
        del audio

    def test_set_audio(self):
        media_type = "audio"
        file_name = "name"
        author = "author"
        quality = "low"
        start_position = "T01:23:45"
        duration = "PT12H34M56S"
        external_reference = "ref"
        audio_file_format = "mp3"
        self.assertEqual(self.form_representation.set_audio(media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format), self.form_representation)
        self.assertEqual(self.form_representation.audio.mediaType, media_type)
        self.assertEqual(self.form_representation.audio.fileName, file_name)
        self.assertEqual(self.form_representation.audio.author, author)
        self.assertEqual(self.form_representation.audio.quality, quality)
        self.assertEqual(self.form_representation.audio.startPosition, start_position)
        self.assertEqual(self.form_representation.audio.durationOfEffectiveSpeech, duration)
        self.assertEqual(self.form_representation.audio.externalReference, external_reference)
        self.assertEqual(self.form_representation.audio.audioFileFormat, audio_file_format)

suite = unittest.TestLoader().loadTestsFromTestCase(TestFormRepresentationFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
