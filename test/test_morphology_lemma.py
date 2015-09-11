#! /usr/bin/env python

from startup import *
from morphology.lemma import Lemma
from core.form_representation import FormRepresentation

from core.form import Form

## Test Lemma class

class TestLemmaFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Lemma object
        self.lemma = Lemma()

    def tearDown(self):
        # Release instantiated objects
        del self.lemma

    def test_init(self):
        self.assertListEqual(self.lemma.form_representation, [])
        self.assertIsNone(self.lemma.hyphenation)
        self.assertIsNone(self.lemma.lexeme)

    def test_set_lexeme(self):
        lexeme = "This is a lexeme."
        self.assertIs(self.lemma.set_lexeme(lexeme), self.lemma)
        self.assertEqual(self.lemma.lexeme, lexeme)

    def test_get_lexeme(self):
        lexeme = "My lexeme."
        self.lemma.lexeme = lexeme
        self.assertEqual(self.lemma.get_lexeme(), lexeme)

    def test_create_form_representation(self):
        # Test create form representation
        repr = self.lemma.create_form_representation()
        self.assertIsInstance(repr, FormRepresentation)
        # Release FormRepresentation instance
        del repr

    def test_add_form_representation(self):
        # Create form representations
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        # Test add form representations to the lemma
        self.assertIs(self.lemma.add_form_representation(repr1), self.lemma)
        self.assertListEqual(self.lemma.form_representation, [repr1])
        self.assertIs(self.lemma.add_form_representation(repr2), self.lemma)
        self.assertListEqual(self.lemma.form_representation, [repr1, repr2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_find_form_representations(self):
        # Create several form representations with different types
        repr1 = FormRepresentation().set_variantForm("form1").set_type("phonetics")
        repr2 = FormRepresentation().set_variantForm("form2").set_type("orthography")
        repr3 = FormRepresentation().set_variantForm("form3").set_type("phonetics")
        repr4 = FormRepresentation().set_variantForm("form4").set_type("archaic")
        # Add form representations to the lemma
        self.lemma.form_representation = [repr1, repr2, repr3, repr4]
        # Test find form representations
        self.assertListEqual(self.lemma.find_form_representations("orthography"), [repr2.variantForm])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.lemma.find_form_representations("phonetics")), set([repr1.variantForm, repr3.variantForm]))
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2, repr3, repr4

    def test_get_form_representations(self):
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lemma.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        self.lemma.form_representation = [repr1, repr2]
        # Test get form representations
        self.assertListEqual(self.lemma.get_form_representations(), [repr1, repr2])
        # Delete FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_get_form_representation(self):
        # List of FormRepresentation instances is empty
        test = False
        try:
            self.lemma.get_form_representation(0)
        except IndexError:
            test = True
        self.assertTrue(test)
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        self.lemma.form_representation = [repr1, repr2]
        # Test get form representation
        self.assertIs(self.lemma.get_form_representation(0), repr1)
        self.assertEqual(self.lemma.get_form_representation(1), repr2)
        # Delete FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_variant_form(self):
        form = "alternative"
        # There is no FormRepresentation
        self.assertIs(self.lemma.set_variant_form(form), self.lemma)
        self.assertEqual(len(self.lemma.form_representation), 1)
        self.assertEqual(self.lemma.form_representation[0].variantForm, form)
        self.assertEqual(self.lemma.form_representation[0].type, "unspecified")
        # Test set a second variant form
        type = "archaic"
        self.assertIs(self.lemma.set_variant_form(form, type), self.lemma)
        self.assertEqual(len(self.lemma.form_representation), 2)
        self.assertEqual(self.lemma.form_representation[1].variantForm, form)
        self.assertEqual(self.lemma.form_representation[1].type, type)

    def test_get_variant_forms(self):
        form1 = "form1"
        form2 = "form2"
        form3 = "form3"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_variant_forms(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.variantForm = form1
        repr1.type = "A"
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_variant_forms(type="A"), [form1])
        self.assertEqual(self.lemma.get_variant_forms(type="B"), [])
        repr2 = FormRepresentation()
        repr2.variantForm = form2
        repr2.type = "B"
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_variant_forms(type="A"), [form1])
        self.assertEqual(self.lemma.get_variant_forms(type="B"), [form2])
        repr3 = FormRepresentation()
        repr3.variantForm = form3
        repr3.type = "A"
        self.lemma.form_representation.append(repr3)
        self.assertEqual(self.lemma.get_variant_forms(type="A"), [form1, form3])
        self.assertEqual(self.lemma.get_variant_forms(type="B"), [form2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2, repr3

    def test_set_variant_comment(self):
        comment = "useful comment"
        # There is no FormRepresentation
        self.assertIs(self.lemma.set_variant_comment(comment), self.lemma)
        self.assertEqual(len(self.lemma.form_representation), 1)
        self.assertEqual(self.lemma.form_representation[0].comment, comment)
        self.assertIsNone(self.lemma.form_representation[0].language)
        # Test set a second comment
        lang = "English"
        self.assertIs(self.lemma.set_variant_comment(comment, lang), self.lemma)
        self.assertEqual(len(self.lemma.form_representation), 2)
        self.assertEqual(self.lemma.form_representation[1].comment, comment)
        self.assertEqual(self.lemma.form_representation[1].language, lang)

    def test_set_tone(self):
        tone = "This is a tone."
        self.assertIs(self.lemma.set_tone(tone), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].tone, tone)

    def test_get_tones(self):
        tone1 = "My tone."
        tone2 = "Another tone."
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_tones(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.tone = tone1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_tones(), [tone1])
        repr2 = FormRepresentation()
        repr2.tone = tone2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_tones(), [tone1, tone2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_geographical_variant(self):
        geo = "geo"
        self.assertIs(self.lemma.set_geographical_variant(geo), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].geographicalVariant, geo)

    def test_set_phonetic_form (self):
        form = "form"
        self.assertIs(self.lemma.set_phonetic_form(form), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].phoneticForm, form)

    def test_get_phonetic_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_phonetic_forms(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.phoneticForm = form1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_phonetic_forms(), [form1])
        repr2 = FormRepresentation()
        repr2.phoneticForm = form2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_phonetic_forms(), [form1, form2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_contextual_variation(self):
        ctx = "ctx"
        self.assertIs(self.lemma.set_contextual_variation(ctx), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].contextualVariation, ctx)

    def test_get_contextual_variations(self):
        var1 = "var1"
        var2 = "var2"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_contextual_variations(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.contextualVariation = var1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_contextual_variations(), [var1])
        repr2 = FormRepresentation()
        repr2.contextualVariation = var2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_contextual_variations(), [var1, var2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_spelling_variant(self):
        var = "var"
        self.assertIs(self.lemma.set_spelling_variant(var), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].spellingVariant, var)

    def test_get_spelling_variants(self):
        var1 = "var1"
        var2 = "var2"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_spelling_variants(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.spellingVariant = var1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_spelling_variants(), [var1])
        repr2 = FormRepresentation()
        repr2.spellingVariant = var2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_spelling_variants(), [var1, var2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_citation_form(self):
        form = "form"
        self.assertIs(self.lemma.set_citation_form(form), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].citationForm, form)

    def test_get_citation_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_citation_forms(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.citationForm = form1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_citation_forms(), [form1])
        repr2 = FormRepresentation()
        repr2.citationForm = form2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_citation_forms(), [form1, form2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_dialect(self):
        dial = "dial"
        self.assertIs(self.lemma.set_dialect(dial), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].dialect, dial)

    def test_set_transliteration(self):
        trans = "trans"
        self.assertIs(self.lemma.set_transliteration(trans), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].transliteration, trans)

    def test_get_transliterations(self):
        trans1 = "trans1"
        trans2 = "trans2"
        # There is no FormRepresentation
        self.assertListEqual(self.lemma.get_transliterations(), [])
        # Create a FormRepresentation instance
        repr1 = FormRepresentation()
        repr1.transliteration = trans1
        self.lemma.form_representation.append(repr1)
        self.assertEqual(self.lemma.get_transliterations(), [trans1])
        repr2 = FormRepresentation()
        repr2.transliteration = trans2
        self.lemma.form_representation.append(repr2)
        self.assertEqual(self.lemma.get_transliterations(), [trans1, trans2])
        # Release FormRepresentation instances
        del self.lemma.form_representation[:]
        del repr1, repr2

    def test_set_script_name(self):
        script = "script"
        self.assertIs(self.lemma.set_script_name(script), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].scriptName, script)

    def test_set_audio(self):
        media_type = "audio"
        file_name = "name"
        author = "author"
        quality = "low"
        start_position = "T01:23:45"
        duration = "PT12H34M56S"
        external_reference = "ref"
        audio_file_format = "mp3"
        self.assertEqual(self.lemma.set_audio(media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format), self.lemma)
        self.assertEqual(self.lemma.form_representation[0].audio.mediaType, media_type)
        self.assertEqual(self.lemma.form_representation[0].audio.fileName, file_name)
        self.assertEqual(self.lemma.form_representation[0].audio.author, author)
        self.assertEqual(self.lemma.form_representation[0].audio.quality, quality)
        self.assertEqual(self.lemma.form_representation[0].audio.startPosition, start_position)
        self.assertEqual(self.lemma.form_representation[0].audio.durationOfEffectiveSpeech, duration)
        self.assertEqual(self.lemma.form_representation[0].audio.externalReference, external_reference)
        self.assertEqual(self.lemma.form_representation[0].audio.audioFileFormat, audio_file_format)

suite = unittest.TestLoader().loadTestsFromTestCase(TestLemmaFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
