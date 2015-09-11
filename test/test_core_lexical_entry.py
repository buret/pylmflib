#! /usr/bin/env python

from startup import *
from core.lexical_entry import LexicalEntry
from core.lexicon import Lexicon
from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from morphology.word_form import WordForm
from core.form_representation import FormRepresentation
from core.sense import Sense
from core.definition import Definition
from core.statement import Statement
from morphosyntax.paradigm import Paradigm
from mrd.subject_field import SubjectField

## Test LexicalEntry class

class TestLexicalEntryFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a LexicalEntry object
        self.lexical_entry = LexicalEntry()

    def tearDown(self):
        # Release instantiated objects
        del self.lexical_entry

    def test_init(self):
        self.assertIsNone(self.lexical_entry.homonymNumber)
        self.assertIsNone(self.lexical_entry.status)
        self.assertIsNone(self.lexical_entry.date)
        self.assertIsNone(self.lexical_entry.partOfSpeech)
        self.assertIsNone(self.lexical_entry.independentWord)
        self.assertIsNone(self.lexical_entry.bibliography)
        self.assertEqual(self.lexical_entry.id, '0')
        self.assertListEqual(self.lexical_entry.sense, [])
        self.assertIsNone(self.lexical_entry.lemma)
        self.assertListEqual(self.lexical_entry.related_form, [])
        self.assertListEqual(self.lexical_entry.word_form, [])
        self.assertListEqual(self.lexical_entry.stem, [])
        self.assertIsNone(self.lexical_entry.list_of_components)
        self.assertIsNone(self.lexical_entry.targets)
        self.assertIsNone(self.lexical_entry.get_speaker())

    def test_set_partOfSpeech(self):
        part_of_speech = "verb"
        self.lexical_entry.set_lexeme("action")
        self.assertEqual(self.lexical_entry.set_partOfSpeech(part_of_speech), self.lexical_entry)
        self.assertEqual(self.lexical_entry.partOfSpeech, part_of_speech)
        # Test error case
        self.lexical_entry.set_partOfSpeech("whatever")

    def test_get_partOfSpeech(self):
        self.assertIs(self.lexical_entry.get_partOfSpeech(), self.lexical_entry.partOfSpeech)

    def test_set_status(self):
        status = "draft"
        self.assertEqual(self.lexical_entry.set_status(status), self.lexical_entry)
        self.assertEqual(self.lexical_entry.status, status)

    def test_get_status(self):
        self.assertIs(self.lexical_entry.get_status(), self.lexical_entry.status)

    def test_set_date(self):
        date = "2014-06-15"
        self.assertEqual(self.lexical_entry.set_date(date), self.lexical_entry)
        self.assertEqual(self.lexical_entry.date, date)

    def test_get_date(self):
        self.assertIs(self.lexical_entry.get_date(), self.lexical_entry.date)

    def test_set_homonymNumber(self):
        nb = "3"
        self.assertEqual(self.lexical_entry.set_homonymNumber(nb), self.lexical_entry)
        self.assertEqual(self.lexical_entry.homonymNumber, nb)

    def test_get_homonymNumber(self):
        self.assertIs(self.lexical_entry.get_homonymNumber(), self.lexical_entry.homonymNumber)

    def test_set_bibliography(self):
        biblio = "212"
        self.assertEqual(self.lexical_entry.set_bibliography(biblio), self.lexical_entry)
        self.assertEqual(self.lexical_entry.bibliography, biblio)

    def test_get_bibliography(self):
        self.assertIs(self.lexical_entry.get_bibliography(), self.lexical_entry.bibliography)

    def test_set_independentWord(self):
        self.assertEqual(self.lexical_entry.set_independentWord(False), self.lexical_entry)
        self.assertFalse(self.lexical_entry.independentWord)
        # Test error case
        self.lexical_entry.set_independentWord("whatever")

    def test_get_independentWord(self):
        self.assertIs(self.lexical_entry.get_independentWord(), self.lexical_entry.independentWord)

    def test_get_id(self):
        self.assertEqual(self.lexical_entry.get_id(), self.lexical_entry.id + '1')

    def test_set_lexeme(self):
        lexeme = "hello"
        self.assertIs(self.lexical_entry.set_lexeme(lexeme), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.lexeme, lexeme)

    def test_get_lexeme(self):
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_lexeme())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        self.assertEqual(self.lexical_entry.get_lexeme(), self.lexical_entry.lemma.lexeme)
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_create_related_form(self):
        lexeme = "form"
        relation = "homonym"
        # Test create related form
        form = self.lexical_entry.create_related_form(lexeme, relation)
        self.assertEqual(form.targets, lexeme)
        self.assertEqual(form.semanticRelation, relation)
        # Release RelatedForm instance
        del form

    def test_add_related_form(self):
        # Create related forms
        form1 = RelatedForm("form1")
        form2 = RelatedForm("form2")
        # Test add related forms to the lexical entry
        self.assertIs(self.lexical_entry.add_related_form(form1), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1])
        self.assertEqual(self.lexical_entry.related_form[0].targets, "form1")
        self.assertIs(self.lexical_entry.add_related_form(form2), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.related_form, [form1, form2])
        self.assertEqual(self.lexical_entry.related_form[1].targets, "form2")
        # Release RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_create_and_add_related_form(self):
        # Test create and add related forms to the lexical entry
        lexeme = "form1"
        relation = "homonym"
        self.assertIs(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.related_form), 1)
        self.assertEqual(self.lexical_entry.related_form[0].targets, lexeme)
        lexeme = "form2"
        relation = "derived form"
        self.assertIs(self.lexical_entry.create_and_add_related_form(lexeme, relation), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.related_form), 2)
        self.assertEqual(self.lexical_entry.related_form[1].targets, lexeme)
        # Release RelatedForm instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]

    def test_find_related_forms(self):
        # Create several related forms with different semantic relations
        form1 = RelatedForm().set_semanticRelation("synonym")
        form2 = RelatedForm().set_semanticRelation("antonym")
        form3 = RelatedForm().set_semanticRelation("synonym")
        form4 = RelatedForm().set_semanticRelation("simple link")
        # Add related forms to the lexical entry
        self.lexical_entry.related_form = [form1, form2, form3, form4]
        # Test find related forms
        self.assertListEqual(self.lexical_entry.find_related_forms("antonym"), [form2.targets])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.lexical_entry.find_related_forms("synonym")), set([form1.targets, form3.targets]))
        # Release RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2, form3, form4

    def test_get_related_forms(self):
        # List of RelatedForm instances is empty
        self.assertEqual(self.lexical_entry.get_related_forms(), [])
        # Create RelatedForm instances and add them to the list
        form1 = RelatedForm()
        form2 = RelatedForm()
        self.lexical_entry.related_form = [form1, form2]
        # Test get related forms
        self.assertEqual(self.lexical_entry.get_related_forms(), [form1, form2])
        self.lexical_entry.related_form.append(form1)
        self.assertEqual(self.lexical_entry.get_related_forms(), [form1, form2, form1])
        # Delete RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_get_last_related_form(self):
        # List of RelatedForm instances is empty
        self.assertIsNone(self.lexical_entry.get_last_related_form())
        # Create RelatedForm instances and add them to the list
        form1 = RelatedForm()
        form2 = RelatedForm()
        self.lexical_entry.related_form = [form1, form2]
        # Test get last related form
        self.assertEqual(self.lexical_entry.get_last_related_form(), form2)
        self.lexical_entry.related_form.append(form1)
        self.assertEqual(self.lexical_entry.get_last_related_form(), form1)
        # Delete RelatedForm instances
        del self.lexical_entry.related_form[:]
        del form1, form2

    def test_get_form_representations(self):
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_form_representations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr2 = FormRepresentation()
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get form representations
        self.assertListEqual(self.lexical_entry.get_form_representations(), [repr1, repr2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_variant_form(self):
        form = "form"
        type = "archaic"
        self.assertIs(self.lexical_entry.set_variant_form(form, type), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].variantForm, form)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].type, type)

    def test_get_phonetic_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_variant_forms())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.variantForm = form1
        repr1.type = "1"
        repr2 = FormRepresentation()
        repr2.variantForm = form2
        repr2.type = "2"
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get variant forms
        self.assertListEqual(self.lexical_entry.get_variant_forms(type="1"), [form1])
        self.assertListEqual(self.lexical_entry.get_variant_forms(type="2"), [form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_variant_comment(self):
        comment = "comment"
        lang = "lang"
        self.assertIs(self.lexical_entry.set_variant_comment(comment, lang), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].comment, comment)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].language, lang)

    def test_set_tone(self):
        tone = "tone"
        self.assertIs(self.lexical_entry.set_tone(tone), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].tone, tone)

    def test_get_tones(self):
        tone1 = "My tone."
        tone2 = "Another tone."
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_tones())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.tone = tone1
        repr2 = FormRepresentation()
        repr2.tone = tone2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get tones
        self.assertListEqual(self.lexical_entry.get_tones(), [tone1, tone2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_geographical_variant(self):
        geo = "geo"
        self.assertIs(self.lexical_entry.set_geographical_variant(geo), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].geographicalVariant, geo)

    def test_set_phonetic_form (self):
        form = "form"
        self.assertIs(self.lexical_entry.set_phonetic_form(form), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].phoneticForm, form)

    def test_get_phonetic_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_phonetic_forms())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.phoneticForm = form1
        repr2 = FormRepresentation()
        repr2.phoneticForm = form2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get phonetic forms
        self.assertListEqual(self.lexical_entry.get_phonetic_forms(), [form1, form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_contextual_variation(self):
        ctx = "ctx"
        self.assertIs(self.lexical_entry.set_contextual_variation(ctx), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].contextualVariation, ctx)

    def test_get_contextual_variations(self):
        ctx1 = "ctx1"
        ctx2 = "ctx2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_contextual_variations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.contextualVariation = ctx1
        repr2 = FormRepresentation()
        repr2.contextualVariation = ctx2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get contextual variations
        self.assertListEqual(self.lexical_entry.get_contextual_variations(), [ctx1, ctx2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_spelling_variant(self):
        var = "var"
        self.assertIs(self.lexical_entry.set_spelling_variant(var), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].spellingVariant, var)

    def test_get_spelling_variants(self):
        var1 = "var1"
        var2 = "var2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_spelling_variants())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.spellingVariant = var1
        repr2 = FormRepresentation()
        repr2.spellingVariant = var2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get spelling variants
        self.assertListEqual(self.lexical_entry.get_spelling_variants(), [var1, var2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_citation_form(self):
        form = "form"
        self.assertIs(self.lexical_entry.set_citation_form(form), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].citationForm, form)

    def test_get_citation_forms(self):
        form1 = "form1"
        form2 = "form2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_citation_forms())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.citationForm = form1
        repr2 = FormRepresentation()
        repr2.citationForm = form2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get citations forms
        self.assertListEqual(self.lexical_entry.get_citation_forms(), [form1, form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_dialect(self):
        dial = "dial"
        self.assertIs(self.lexical_entry.set_dialect(dial), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].dialect, dial)

    def test_set_transliteration(self):
        trans = "trans"
        self.assertIs(self.lexical_entry.set_transliteration(trans), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].transliteration, trans)

    def test_get_transliterations(self):
        trans1 = "trans1"
        trans2 = "trans2"
        # There is no Lemma instance
        self.assertIsNone(self.lexical_entry.get_transliterations())
        # Create a Lemma instance
        self.lexical_entry.lemma = Lemma()
        # List of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.get_form_representations(), [])
        # Create FormRepresentation instances and add them to the list
        repr1 = FormRepresentation()
        repr1.transliteration = trans1
        repr2 = FormRepresentation()
        repr2.transliteration = trans2
        self.lexical_entry.lemma.form_representation = [repr1, repr2]
        # Test get transliterations
        self.assertListEqual(self.lexical_entry.get_transliterations(), [trans1, trans2])
        # Delete FormRepresentation instances
        del self.lexical_entry.lemma.form_representation[:]
        del repr1, repr2
        # Delete Lemma instance
        del self.lexical_entry.lemma
        self.lexical_entry.lemma = None

    def test_set_script_name(self):
        script = "script"
        self.assertIs(self.lexical_entry.set_script_name(script), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].scriptName, script)

    def test_create_and_add_sense(self):
        # Test create and add senses to the lexical entry
        nb1 = "1"
        self.assertIs(self.lexical_entry.create_and_add_sense(nb1), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(self.lexical_entry.sense[0].id, "01_1")
        # Test with an identifier
        self.lexical_entry.id = "form"
        nb2 = 22
        self.assertIs(self.lexical_entry.create_and_add_sense(nb2), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 2)
        self.assertEqual(self.lexical_entry.sense[1].id, "form1_22")
        # Release Sense instances
        del self.lexical_entry.sense[1], self.lexical_entry.sense[0]

    def test_get_senses(self):
        # List of Sense instances is empty
        self.assertListEqual(self.lexical_entry.get_senses(), [])
        # Create Sense instances and add them to the list
        sens1 = Sense()
        sens2 = Sense()
        self.lexical_entry.sense = [sens1, sens2]
        # Test get senses
        self.assertListEqual(self.lexical_entry.get_senses(), [sens1, sens2])
        # Delete Sense instances
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_create_sense(self):
        id = "ID"
        # Test create sense
        sense = self.lexical_entry.create_sense(id)
        self.assertEqual(sense.id, id)
        # Release Sense instance
        del sense

    def test_add_sense(self):
        # Create senses
        sens1 = Sense("id1")
        sens2 = Sense("id2")
        # Test add senses to the lexical entry
        self.assertIs(self.lexical_entry.add_sense(sens1), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.sense, [sens1])
        self.assertEqual(self.lexical_entry.sense[0].id, "id1")
        self.assertIs(self.lexical_entry.add_sense(sens2), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.sense, [sens1, sens2])
        self.assertEqual(self.lexical_entry.sense[1].id, "id2")
        # Release Sense instances
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_get_last_sense(self):
        # List of Sense instances is empty
        self.assertIsNone(self.lexical_entry.get_last_sense())
        # Create Sense instances and add them to the list
        sens1 = Sense()
        sens2 = Sense()
        self.lexical_entry.sense = [sens1, sens2]
        # Test get last sense
        self.assertIs(self.lexical_entry.get_last_sense(), sens2)
        self.lexical_entry.sense.pop()
        self.assertIs(self.lexical_entry.get_last_sense(), sens1)
        # Release Sense instances
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_set_definition(self):
        definition = "def"
        language = "lang"
        self.assertIs(self.lexical_entry.set_definition(definition, language), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].definition, definition)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].language, language)

    def test_set_gloss(self):
        gloss = "GLOSS"
        language = "lang"
        self.assertIs(self.lexical_entry.set_gloss(gloss, language), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].gloss, gloss)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].language, language)

    def test_set_note(self):
        note = "note"
        type = "comment"
        self.assertIs(self.lexical_entry.set_note(note, type), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].note, note)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].noteType, type)

    def test_find_notes(self):
        # Create several senses
        sens1 = Sense()
        sens2 = Sense()
        self.lexical_entry.sense = [sens1, sens2]
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        def3 = Definition()
        self.lexical_entry.sense[0].definition = [def1, def2]
        self.lexical_entry.sense[1].definition = [def3]
        # Create several statements with different notes and types
        state1 = Statement().set_note("note1", "comparison")
        state2 = Statement().set_note("note2", "general")
        state3 = Statement().set_note("note3", "comparison")
        state4 = Statement().set_note("note3", "history")
        self.lexical_entry.sense[0].definition[0].statement = [state1]
        self.lexical_entry.sense[0].definition[1].statement = [state2]
        self.lexical_entry.sense[1].definition[0].statement = [state3, state4]
        # Test find notes
        self.assertListEqual(self.lexical_entry.find_notes("general"), [state2.note])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.lexical_entry.find_notes("comparison")), set([state1.note, state3.note]))
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del self.lexical_entry.sense[0].definition[1].statement[:]
        del self.lexical_entry.sense[1].definition[0].statement[:]
        del state1, state2, state3, state4
        del self.lexical_entry.sense[0].definition[:]
        del self.lexical_entry.sense[1].definition[:]
        del def1, def2, def3
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_set_usage_note(self):
        note = "note"
        language = "bla"
        self.assertIs(self.lexical_entry.set_usage_note(note, language), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].usageNote, note)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].language, language)

    def test_set_encyclopedic_information(self):
        info = "info"
        language = "bla"
        self.assertIs(self.lexical_entry.set_encyclopedic_information(info, language), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].encyclopedicInformation, info)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].language, language)

    def test_set_restriction(self):
        only = "only"
        language = "bla"
        self.assertIs(self.lexical_entry.set_restriction(only, language), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].restriction, only)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].language, language)

    def test_set_borrowed_word(self):
        word = "borrowed"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_borrowed_word(word), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].borrowedWord, word)

    def test_get_borrowed_word(self):
        word = "borrowed"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set borrowed word
        self.lexical_entry.sense[0].definition[0].statement[0].borrowedWord = word
        # Test get borrowed word
        self.assertEqual(self.lexical_entry.get_borrowed_word(), word)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_writtenForm(self):
        form = "written"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_written_form(form), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].writtenForm, form)

    def test_get_writtenForm(self):
        form = "written"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set written form
        self.lexical_entry.sense[0].definition[0].statement[0].writtenForm = form
        # Test get written form
        self.assertEqual(self.lexical_entry.get_written_form(), form)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_etymology(self):
        etymology = "etymology"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_etymology(etymology), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].etymology, etymology)

    def test_get_etymology(self):
        etymology = "etymology"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set etymology
        self.lexical_entry.sense[0].definition[0].statement[0].etymology = etymology
        # Test get etymology
        self.assertEqual(self.lexical_entry.get_etymology(), etymology)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_etymology_comment(self):
        # Test etymology comment only
        comment = "etymology"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_etymology_comment(comment), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].etymologyComment, comment)
        # Test etymology comment and language
        commentaire = "etymologie"
        langage = "fra"
        self.assertIs(self.lexical_entry.set_etymology_comment(commentaire, term_source_language=langage), self.lexical_entry)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].etymologyComment, commentaire)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].termSourceLanguage, langage)

    def test_get_etymology_comment(self):
        comment = "etymology"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set etymology
        self.lexical_entry.sense[0].definition[0].statement[0].etymologyComment = comment
        # Test get etymology
        self.assertEqual(self.lexical_entry.get_etymology_comment(), comment)
        # Test with a language filter
        language = "eng"
        self.lexical_entry.sense[0].definition[0].statement[0].termSourceLanguage = language
        self.assertIsNone(self.lexical_entry.get_etymology_comment(term_source_language="fra"))
        self.assertEqual(self.lexical_entry.get_etymology_comment(term_source_language=language), comment)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_etymology_gloss(self):
        gloss = "GLOSS"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_etymology_gloss(gloss), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].etymologyGloss, gloss)

    def test_get_etymology_gloss(self):
        gloss = "GLOSS"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set etymology
        self.lexical_entry.sense[0].definition[0].statement[0].etymologyGloss = gloss
        # Test get etymology
        self.assertEqual(self.lexical_entry.get_etymology_gloss(), gloss)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_etymology_source(self):
        source = "etymology"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_etymology_source(source), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].etymologySource, source)

    def test_get_etymology_source(self):
        source = "etymology"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set etymology
        self.lexical_entry.sense[0].definition[0].statement[0].etymologySource = source
        # Test get etymology
        self.assertEqual(self.lexical_entry.get_etymology_source(), source)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_set_scientific_name(self):
        name = "Cretinus"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_scientific_name(name), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].definition[0].statement), 1)
        self.assertEqual(self.lexical_entry.sense[0].definition[0].statement[0].scientificName, name)

    def test_get_scientific_name(self):
        name = "Linus"
        # Create sense and definition and add them
        sense = Sense()
        self.lexical_entry.sense = [sense]
        definition = Definition()
        self.lexical_entry.sense[0].definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.lexical_entry.sense[0].definition[0].statement = [state]
        # Set scientific name
        self.lexical_entry.sense[0].definition[0].statement[0].scientificName = name
        # Test get scientific name
        self.assertEqual(self.lexical_entry.get_scientific_name(), name)
        # Release created instances
        del self.lexical_entry.sense[0].definition[0].statement[:]
        del state
        del self.lexical_entry.sense[0].definition[:]
        del definition
        del self.lexical_entry.sense[:]
        del sense

    def test_create_word_form(self):
        # Test create word form
        form = self.lexical_entry.create_word_form()
        self.assertIsInstance(form, WordForm)
        # Release WordForm instance
        del form

    def test_add_word_form(self):
        # Create word forms
        form1 = WordForm()
        form2 = WordForm()
        # Test add word forms to the lexical entry
        self.assertIs(self.lexical_entry.add_word_form(form1), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.word_form, [form1])
        self.assertIs(self.lexical_entry.add_word_form(form2), self.lexical_entry)
        self.assertListEqual(self.lexical_entry.word_form, [form1, form2])
        # Release WordForm instances
        del self.lexical_entry.word_form[:]
        del form1, form2

    def test_get_word_forms(self):
        # List of WordForm instances is empty
        self.assertEqual(self.lexical_entry.get_word_forms(), [])
        # Create WordForm instances and add them to the list
        form1 = WordForm()
        form2 = WordForm()
        self.lexical_entry.word_form = [form1, form2]
        # Test get word forms
        self.assertEqual(self.lexical_entry.get_word_forms(), [form1, form2])
        # Delete WordForm instances
        del self.lexical_entry.word_form[:]
        del form1, form2

    def test_set_paradigm(self):
        form = "written"
        self.assertIs(self.lexical_entry.set_paradigm(form), self.lexical_entry)
        self.assertEqual(self.lexical_entry.word_form[0].form_representation[0].writtenForm, form)
        # Test with optional arguments
        person = 2
        anymacy = "animate"
        number = "singular"
        clusivity = None
        self.assertIs(self.lexical_entry.set_paradigm(form, person=person, anymacy=anymacy, grammatical_number=number, clusivity=clusivity), self.lexical_entry)
        self.assertEqual(self.lexical_entry.word_form[1].form_representation[0].writtenForm, form)
        self.assertEqual(self.lexical_entry.word_form[1].person, "second person")
        self.assertEqual(self.lexical_entry.word_form[1].anymacy, anymacy)
        self.assertEqual(self.lexical_entry.word_form[1].grammaticalNumber, number)
        self.assertIsNone(self.lexical_entry.word_form[1].clusivity)
        # Test with same arguments and another variant form
        form = "another variant"
        self.assertIs(self.lexical_entry.set_paradigm(form, person="second person", anymacy=anymacy, grammatical_number=number, clusivity=clusivity), self.lexical_entry)
        self.assertEqual(self.lexical_entry.word_form[1].form_representation[1].writtenForm, form)
        self.assertEqual(self.lexical_entry.word_form[1].person, "second person")
        self.assertEqual(self.lexical_entry.word_form[1].anymacy, anymacy)
        self.assertEqual(self.lexical_entry.word_form[1].grammaticalNumber, number)
        self.assertIsNone(self.lexical_entry.word_form[1].clusivity)

    def test_find_paradigms(self):
        # There is no WordForm instance
        self.assertListEqual(self.lexical_entry.find_paradigms(), [])
        # Create WordForm instances
        word1 = WordForm()
        word2 = WordForm()
        self.lexical_entry.word_form = [word1, word2]
        # Lists of FormRepresentation instances is empty
        self.assertListEqual(self.lexical_entry.word_form[0].get_form_representations(), [])
        self.assertListEqual(self.lexical_entry.word_form[1].get_form_representations(), [])
        # Create FormRepresentation instances and add them to the lists
        repr1 = FormRepresentation()
        form1 = "written1"
        repr1.writtenForm = form1
        repr2 = FormRepresentation()
        form2 = "written2"
        repr2.writtenForm = form2
        word1.form_representation = [repr1, repr2]
        repr3 = FormRepresentation()
        form3 = "written3"
        repr3.writtenForm = form3
        word2.form_representation = [repr3]
        # Test find paradigms
        self.assertListEqual(self.lexical_entry.find_paradigms(), [form1, form2, form3])
        # Add a filter
        word1.anymacy = "animate"
        word2.anymacy = "inanimate"
        self.assertListEqual(self.lexical_entry.find_paradigms(anymacy="animate"), [form1, form2])
        # Delete FormRepresentation instances
        del self.lexical_entry.word_form[0].form_representation[:]
        del self.lexical_entry.word_form[1].form_representation[:]
        del repr1, repr2, repr3
        # Delete WordForm instances
        del self.lexical_entry.word_form[:]
        del word1, word2

    def test_set_paradigm_label(self):
        label = "lexicalized affix"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_paradigm_label(label), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].paradigm), 1)
        self.assertEqual(self.lexical_entry.sense[0].paradigm[0].paradigmLabel, label)

    def test_set_paradigm_form(self):
        # Test paradigm form only
        form = "paradigm"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_paradigm_form(form), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].paradigm), 1)
        self.assertEqual(self.lexical_entry.sense[0].paradigm[0].paradigm, form)
        # Test paradigm form and language
        forme = "paradigme"
        langage = "fra"
        self.assertIs(self.lexical_entry.set_paradigm_form(forme, langage), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense[0].paradigm), 2)
        self.assertEqual(self.lexical_entry.sense[0].paradigm[1].paradigm, forme)
        self.assertEqual(self.lexical_entry.sense[0].paradigm[1].language, langage)

    def test_set_morphology(self):
        morpho = "logy"
        # There is no Sense instance
        self.assertIs(self.lexical_entry.set_morphology(morpho), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].paradigm), 1)
        self.assertEqual(self.lexical_entry.sense[0].paradigm[0].morphology, morpho)

    def test_get_paradigms(self):
        # List of Paradigm instances is empty
        self.assertEqual(self.lexical_entry.get_paradigms(), [])
        # Create a Sense instance and add it to the list
        sense = Sense()
        self.lexical_entry.sense = [sense]
        # Create Paradigm instances and add them to the list
        para1 = Paradigm()
        para2 = Paradigm()
        self.lexical_entry.sense[0].paradigm = [para1, para2]
        # Test get paradigms
        self.assertEqual(self.lexical_entry.get_paradigms(), [para1, para2])
        # Delete Paradigm and Sense instances
        del self.lexical_entry.sense[0].paradigm[:]
        del para1, para2
        del self.lexical_entry.sense[:]
        del sense

    def test_get_morphologies(self):
        # List of Paradigm instances is empty
        self.assertEqual(self.lexical_entry.get_paradigms(), [])
        # Create a Sense instance and add it to the list
        sense = Sense()
        self.lexical_entry.sense = [sense]
        # Create Paradigm instances, set their morphology, and add them to the list
        morpho1 = "1"
        morpho2 = "2"
        para1 = Paradigm().set_morphology(morpho1)
        para2 = Paradigm().set_morphology(morpho2)
        self.lexical_entry.sense[0].paradigm = [para1, para2]
        # Test get morphologies
        self.assertEqual(self.lexical_entry.get_morphologies(), [morpho1, morpho2])
        # Delete Paradigm and Sense instances
        del self.lexical_entry.sense[0].paradigm[:]
        del para1, para2
        del self.lexical_entry.sense[:]
        del sense

    def test_create_example(self):
        ref = "toto"
        self.assertIs(self.lexical_entry.create_example(ref), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(self.lexical_entry.sense[0].context[0].targets, ref)
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 0)

    def test_create_and_add_example(self):
        form = "written"
        self.assertIs(self.lexical_entry.create_and_add_example(form), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[0].writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.lexical_entry.create_and_add_example(form, lang), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 2)
        self.assertEqual(self.lexical_entry.sense[0].context[1].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[1].text_representation), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[1].text_representation[0].writtenForm, form)
        self.assertEqual(self.lexical_entry.sense[0].context[1].text_representation[0].language, lang)

    def test_add_example(self):
        form = "written"
        self.assertIs(self.lexical_entry.add_example(form), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[0].writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.lexical_entry.add_example(form, lang), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 2)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[1].writtenForm, form)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[1].language, lang)

    def test_set_example_comment(self):
        comment = "example"
        self.assertIs(self.lexical_entry.set_example_comment(comment), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[0].comment, comment)
        # Test with a second comment
        comment = "another"
        self.assertIs(self.lexical_entry.set_example_comment(comment), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].context), 1)
        self.assertEqual(self.lexical_entry.sense[0].context[0].type, "example")
        self.assertEqual(len(self.lexical_entry.sense[0].context[0].text_representation), 2)
        self.assertEqual(self.lexical_entry.sense[0].context[0].text_representation[1].comment, comment)

    def test_set_semantic_domain(self):
        domain = "semantic"
        self.assertIs(self.lexical_entry.set_semantic_domain(domain), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].subject_field), 1)
        self.assertEqual(self.lexical_entry.sense[0].subject_field[0].semanticDomain, domain)
        # Test with language
        domain = "domain with lang"
        lang = "lang"
        self.assertIs(self.lexical_entry.set_semantic_domain(domain, lang), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].subject_field), 2)
        self.assertEqual(self.lexical_entry.sense[0].subject_field[1].semanticDomain, domain)
        self.assertEqual(self.lexical_entry.sense[0].subject_field[1].language, lang)

    def test_get_semantic_domains(self):
        domain1 = "semantic1"
        domain2 = "semantic2"
        self.assertListEqual(self.lexical_entry.get_semantic_domains(), [])
        # Create Sense and SubjectField instances and add them to corresponding lists
        sens1 = Sense()
        sens2 = Sense()
        self.lexical_entry.sense = [sens1, sens2]
        subject = SubjectField()
        field = SubjectField()
        sens1.subject_field = [subject]
        sens2.subject_field = [field]
        subject.semanticDomain = domain1
        self.assertEqual(self.lexical_entry.get_semantic_domains(), [domain1])
        field.semanticDomain = domain2
        self.assertEqual(self.lexical_entry.get_semantic_domains(), [domain1, domain2])
        # Test with a language filter
        language = "eng"
        subject.language = language
        self.assertEqual(self.lexical_entry.get_semantic_domains(), [domain1, domain2])
        self.assertListEqual(self.lexical_entry.get_semantic_domains("fra"), [])
        self.assertListEqual(self.lexical_entry.get_semantic_domains(language), [domain1])
        # Release created instances
        del self.lexical_entry.sense[0].subject_field[:]
        del subject, field
        del self.lexical_entry.sense[:]
        del sens1, sens2

    def test_set_translation(self):
        trans = "trans"
        self.assertIs(self.lexical_entry.set_translation(trans), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].equivalent), 1)
        self.assertEqual(self.lexical_entry.sense[0].equivalent[0].translation, trans)
        # Test with language
        trans = "trans with lang"
        lang = "lang"
        self.assertIs(self.lexical_entry.set_translation(trans, lang), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.sense), 1)
        self.assertEqual(len(self.lexical_entry.sense[0].equivalent), 2)
        self.assertEqual(self.lexical_entry.sense[0].equivalent[1].translation, trans)
        self.assertEqual(self.lexical_entry.sense[0].equivalent[1].language, lang)

    def test_set_audio(self):
        media_type = "audio"
        file_name = "name"
        author = "author"
        quality = "low"
        start_position = "T01:23:45"
        duration = "PT12H34M56S"
        external_reference = "ref"
        audio_file_format = "mp3"
        self.assertEqual(self.lexical_entry.set_audio(media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format), self.lexical_entry)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.mediaType, media_type)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.fileName, file_name)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.author, author)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.quality, quality)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.startPosition, start_position)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.durationOfEffectiveSpeech, duration)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.externalReference, external_reference)
        self.assertEqual(self.lexical_entry.lemma.form_representation[0].audio.audioFileFormat, audio_file_format)

    def test_is_subentry(self):
        # Add subentries to the lexical entry
        lexeme = "mn"
        lexeme1 = "first"
        lexeme2 = "second"
        self.lexical_entry.set_lexeme(lexeme)
        subentry1 = LexicalEntry().set_lexeme(lexeme1)
        subentry2 = LexicalEntry().set_lexeme(lexeme2)
        self.lexical_entry.create_and_add_related_form(lexeme1, "subentry")
        self.lexical_entry.create_and_add_related_form(lexeme2, "subentry")
        subentry1.create_and_add_related_form(lexeme, "main entry")
        subentry2.create_and_add_related_form(lexeme, "main entry")
        # Test "main entry" relation
        self.assertTrue(subentry1.is_subentry())
        self.assertTrue(subentry2.is_subentry())
        self.assertFalse(self.lexical_entry.is_subentry())
        # Release RelatedForm and LexicalEntry instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]
        del subentry1, subentry2

    def test_has_subentries(self):
        # Add subentries to the lexical entry
        lexeme = "mn"
        lexeme1 = "first"
        lexeme2 = "second"
        self.lexical_entry.set_lexeme(lexeme)
        subentry1 = LexicalEntry().set_lexeme(lexeme1)
        subentry2 = LexicalEntry().set_lexeme(lexeme2)
        self.lexical_entry.create_and_add_related_form(lexeme1, "subentry")
        self.lexical_entry.create_and_add_related_form(lexeme2, "subentry")
        subentry1.create_and_add_related_form(lexeme, "main entry")
        subentry2.create_and_add_related_form(lexeme, "main entry")
        # Test "subentry" relation
        self.assertFalse(subentry1.has_subentries())
        self.assertFalse(subentry2.has_subentries())
        self.assertTrue(self.lexical_entry.has_subentries())
        # Release RelatedForm and LexicalEntry instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]
        del subentry1, subentry2

    def test_get_subentries(self):
        # Add subentries to the lexical entry
        lexeme = "mn"
        lexeme1 = "first"
        lexeme2 = "second"
        subentry1 = LexicalEntry().set_lexeme(lexeme1)
        subentry2 = LexicalEntry().set_lexeme(lexeme2)
        self.lexical_entry.create_and_add_related_form(lexeme1, "subentry")
        self.lexical_entry.create_and_add_related_form(lexeme2, "subentry")
        subentry1.create_and_add_related_form(lexeme, "main entry")
        subentry2.create_and_add_related_form(lexeme, "main entry")
        # Add entries to a lexicon
        lexicon = Lexicon().add_lexical_entry(self.lexical_entry).add_lexical_entry(subentry1).add_lexical_entry(subentry2)
        lexicon.check_cross_references()
        # Test get subentries
        self.assertListEqual(subentry1.get_subentries(), [])
        self.assertListEqual(subentry2.get_subentries(), [])
        self.assertEqual(set(self.lexical_entry.get_subentries()), set([subentry1, subentry2]))
        # Release RelatedForm and LexicalEntry instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]
        del subentry1, subentry2

    def test_get_main_entry(self):
        # Add subentries to the lexical entry
        lexeme = "mn"
        lexeme1 = "first"
        lexeme2 = "second"
        self.lexical_entry.set_lexeme(lexeme)
        subentry1 = LexicalEntry().set_lexeme(lexeme1)
        subentry2 = LexicalEntry().set_lexeme(lexeme2)
        self.lexical_entry.create_and_add_related_form(lexeme1, "subentry")
        self.lexical_entry.create_and_add_related_form(lexeme2, "subentry")
        subentry1.create_and_add_related_form(lexeme, "main entry")
        subentry2.create_and_add_related_form(lexeme, "main entry")
        # Add entries to a lexicon
        lexicon = Lexicon().add_lexical_entry(self.lexical_entry).add_lexical_entry(subentry1).add_lexical_entry(subentry2)
        lexicon.check_cross_references()
        # Test get main entry
        self.assertIs(subentry1.get_main_entry(), self.lexical_entry)
        self.assertIs(subentry2.get_main_entry(), self.lexical_entry)
        self.assertIsNone(self.lexical_entry.get_main_entry())
        # Release RelatedForm and LexicalEntry instances
        del self.lexical_entry.related_form[1], self.lexical_entry.related_form[0]
        del subentry1, subentry2

    def test_create_and_add_component(self):
        # Test create and add components to the lexical entry
        lexeme = "lexeme1"
        position = 1
        self.assertIs(self.lexical_entry.create_and_add_component(position, lexeme), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.get_components()), 1)
        self.assertEqual(self.lexical_entry.list_of_components.component[0].targets, lexeme)
        lexeme = "lexeme2"
        position = 2
        self.assertIs(self.lexical_entry.create_and_add_component(position, lexeme), self.lexical_entry)
        self.assertEqual(len(self.lexical_entry.get_components()), 2)
        self.assertEqual(self.lexical_entry.list_of_components.component[1].targets, lexeme)
        # Release ListOfComponents and Component instances
        del self.lexical_entry.list_of_components.component[1], self.lexical_entry.list_of_components.component[0], self.lexical_entry.list_of_components

    def test_get_components(self):
        # Add components to the lexical entry
        lexeme1 = "first"
        position1 = 1
        lexeme2 = "second"
        position2 = 2
        self.lexical_entry.create_and_add_component(position1, lexeme1)
        self.lexical_entry.create_and_add_component(position2, lexeme2)
        # Test get components
        self.assertEqual(self.lexical_entry.get_components(), [self.lexical_entry.list_of_components.component[0], self.lexical_entry.list_of_components.component[1]])
        # Release ListOfComponents and Component instances
        del self.lexical_entry.list_of_components.component[1], self.lexical_entry.list_of_components.component[0], self.lexical_entry.list_of_components

    def test_is_component(self):
        # Add components to the lexical entry
        lexeme = "main"
        lexeme1 = "first"
        lexeme2 = "second"
        self.lexical_entry.set_lexeme(lexeme)
        component1 = LexicalEntry().set_lexeme(lexeme1)
        component2 = LexicalEntry().set_lexeme(lexeme2)
        component1.create_and_add_related_form(self.lexical_entry.get_lexeme(), "complex predicate")
        component2.create_and_add_related_form(self.lexical_entry.get_lexeme(), "complex predicate")
        # Test "complexe predicate" relation
        self.assertTrue(component1.is_component())
        self.assertTrue(component2.is_component())
        self.assertFalse(self.lexical_entry.is_component())
        # Release Component instances
        del component1, component2

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexicalEntryFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
