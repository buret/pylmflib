#! /usr/bin/env python

from startup import *
from core.sense import Sense
from core.definition import Definition
from core.statement import Statement
from morphosyntax.paradigm import Paradigm
from mrd.context import Context
from mrd.subject_field import SubjectField
from mrd.equivalent import Equivalent

## Test Sense class

class TestSenseFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Sense object
        self.sense = Sense()

    def tearDown(self):
        # Release instantiated objects
        del self.sense

    def test_init(self):
        self.assertIsNone(self.sense.senseNumber)
        self.assertEqual(self.sense.id, 0)
        self.assertListEqual(self.sense.definition, [])
        self.assertListEqual(self.sense.sense, [])
        self.assertListEqual(self.sense.equivalent, [])
        self.assertListEqual(self.sense.context, [])
        self.assertListEqual(self.sense.subject_field, [])
        self.assertListEqual(self.sense.paradigm, [])

    def test_get_id(self):
        self.assertIs(self.sense.get_id(), self.sense.id)

    def test_set_senseNumber(self):
        nb = 123
        self.assertIs(self.sense.set_senseNumber(nb), self.sense)
        self.assertEqual(self.sense.senseNumber, nb)

    def test_get_senseNumner(self):
        nb = 456
        self.sense.senseNumber = nb
        self.assertEqual(self.sense.get_senseNumber(), nb)

    def test_create_definition(self):
        # Test create definition
        definition = self.sense.create_definition()
        self.assertIsInstance(definition, Definition)
        # Release Definition instance
        del definition

    def test_add_definition(self):
        # Create definitions
        def1 = Definition()
        def2 = Definition()
        # Test add definitions to the sense
        self.assertIs(self.sense.add_definition(def1), self.sense)
        self.assertListEqual(self.sense.definition, [def1])
        self.assertIs(self.sense.add_definition(def2), self.sense)
        self.assertListEqual(self.sense.definition, [def1, def2])
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_get_definitions(self):
        # List of Definition instances is empty
        self.assertListEqual(self.sense.get_definitions(), [])
        # Create Definition instances and add them to the list
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Test get definitions
        self.assertListEqual(self.sense.get_definitions(), [def1, def2])
        # Delete Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_get_last_definition(self):
        # List of Definition instances is empty
        self.assertIsNone(self.sense.get_last_definition())
        # Create Definition instances and add them to the list
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Test get last definition
        self.assertIs(self.sense.get_last_definition(), def2)
        self.sense.definition.pop()
        self.assertIs(self.sense.get_last_definition(), def1)
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2

    def test_find_definitions(self):
        # Create several definitions with different languages
        def1 = Definition().set_definition("def1").set_language("fra")
        def2 = Definition().set_definition("def2").set_language("eng")
        def3 = Definition().set_definition("def3").set_language("fra")
        def4 = Definition().set_definition("def4").set_language("srp")
        # Add definitions to the sense
        self.sense.definition = [def1, def2, def3, def4]
        # Test find definitions
        self.assertListEqual(self.sense.find_definitions("eng"), [def2.definition])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_definitions("fra")), set([def1.definition, def3.definition]))
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2, def3, def4

    def test_set_definition(self):
        definition = "#define"
        # There is no Definition instance
        self.assertIs(self.sense.set_definition(definition), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(self.sense.definition[0].definition, definition)
        # Test set a second definition
        language = "C++"
        self.assertIs(self.sense.set_definition(definition, language), self.sense)
        self.assertEqual(len(self.sense.definition), 2)
        self.assertEqual(self.sense.definition[1].definition, definition)
        self.assertEqual(self.sense.definition[1].language, language)

    def test_find_glosses(self):
        # Create several definitions with different glosses and languages
        def1 = Definition().set_gloss("DEF1").set_language("fra")
        def2 = Definition().set_gloss("DEF2").set_language("eng")
        def3 = Definition().set_gloss("DEF3").set_language("fra")
        def4 = Definition().set_gloss("DEF4").set_language("srp")
        # Add definitions to the sense
        self.sense.definition = [def1, def2, def3, def4]
        # Test find glosses
        self.assertListEqual(self.sense.find_glosses("eng"), [def2.gloss])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_glosses("fra")), set([def1.gloss, def3.gloss]))
        # Release Definition instances
        del self.sense.definition[:]
        del def1, def2, def3, def4

    def test_set_gloss(self):
        gloss = "GLOSS"
        # There is no Definition instance
        self.assertIs(self.sense.set_gloss(gloss), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(self.sense.definition[0].gloss, gloss)
        # Test set a second gloss
        language = "C++"
        self.assertIs(self.sense.set_gloss(gloss, language), self.sense)
        self.assertEqual(len(self.sense.definition), 2)
        self.assertEqual(self.sense.definition[1].gloss, gloss)
        self.assertEqual(self.sense.definition[1].language, language)

    def test_set_note(self):
        note = "note"
        # There is no Definition instance
        self.assertIs(self.sense.set_note(note), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].note, note)
        # Test set a second note
        language = "C++"
        self.assertIs(self.sense.set_note(note, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].note, note)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_notes(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different notes and types
        state1 = Statement().set_note("note1", "comparison")
        state2 = Statement().set_note("note2", "general")
        state3 = Statement().set_note("note3", "comparison")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find notes
        self.assertListEqual(self.sense.find_notes("general"), [state2.note])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_notes("comparison")), set([state1.note, state3.note]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_usage_note(self):
        note = "note"
        # There is no Definition instance
        self.assertIs(self.sense.set_usage_note(note), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].usageNote, note)
        # Test set a second usage note
        language = "C++"
        self.assertIs(self.sense.set_usage_note(note, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].usageNote, note)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_usage_notes(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different usage notes and languages
        state1 = Statement().set_usageNote("note1", "eng")
        state2 = Statement().set_usageNote("note2", "fra")
        state3 = Statement().set_usageNote("note3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find usage notes
        self.assertListEqual(self.sense.find_usage_notes("fra"), [state2.usageNote])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_usage_notes("eng")), set([state1.usageNote, state3.usageNote]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_encyclopedic_information(self):
        info = "encyclopedic"
        # There is no Definition instance
        self.assertIs(self.sense.set_encyclopedic_information(info), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].encyclopedicInformation, info)
        # Test set a second encyclopedic information
        language = "C++"
        self.assertIs(self.sense.set_encyclopedic_information(info, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].encyclopedicInformation, info)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_encyclopedic_informations(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different encyclopedic informations and languages
        state1 = Statement().set_encyclopedicInformation("info1", "eng")
        state2 = Statement().set_encyclopedicInformation("info2", "fra")
        state3 = Statement().set_encyclopedicInformation("info3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find encyclopedic informations
        self.assertListEqual(self.sense.find_encyclopedic_informations("fra"), [state2.encyclopedicInformation])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_encyclopedic_informations("eng")), set([state1.encyclopedicInformation, state3.encyclopedicInformation]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_restriction(self):
        only = "restriction"
        # There is no Definition instance
        self.assertIs(self.sense.set_restriction(only), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].restriction, only)
        # Test set a second restriction
        language = "C++"
        self.assertIs(self.sense.set_restriction(only, language=language), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 2)
        self.assertEqual(self.sense.definition[0].statement[1].restriction, only)
        self.assertEqual(self.sense.definition[0].statement[1].language, language)

    def test_find_restrictions(self):
        # Create several definitions
        def1 = Definition()
        def2 = Definition()
        self.sense.definition = [def1, def2]
        # Create several statements with different restrictions and languages
        state1 = Statement().set_restriction("only1", "eng")
        state2 = Statement().set_restriction("only2", "fra")
        state3 = Statement().set_restriction("only3", "eng")
        self.sense.definition[0].statement = [state1, state2]
        self.sense.definition[1].statement = [state3]
        # Test find restrictions
        self.assertListEqual(self.sense.find_restrictions("fra"), [state2.restriction])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.sense.find_restrictions("eng")), set([state1.restriction, state3.restriction]))
        # Release created instances
        del self.sense.definition[0].statement[:]
        del self.sense.definition[1].statement[:]
        del state1, state2, state3
        del self.sense.definition[:]
        del def1, def2

    def test_set_borrowed_word(self):
        word = "borrowed"
        # There is no Definition instance
        self.assertIs(self.sense.set_borrowed_word(word), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].borrowedWord, word)

    def test_get_borrowed_word(self):
        word = "borrowed"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set borrowed word
        self.sense.definition[0].statement[0].borrowedWord = word
        # Test get borrowed word
        self.assertEqual(self.sense.get_borrowed_word(), word)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_writtenForm(self):
        form = "written"
        # There is no Definition instance
        self.assertIs(self.sense.set_written_form(form), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].writtenForm, form)

    def test_get_writtenForm(self):
        form = "written"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set written form
        self.sense.definition[0].statement[0].writtenForm = form
        # Test get written form
        self.assertEqual(self.sense.get_written_form(), form)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology(self):
        etymology = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology(etymology), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymology, etymology)

    def test_get_etymology(self):
        etymology = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymology = etymology
        # Test get etymology
        self.assertEqual(self.sense.get_etymology(), etymology)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_comment(self):
        # Test etymology comment only
        comment = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_comment(comment), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyComment, comment)
        # Test etymology comment and language
        commentaire = "etymologie"
        langage = "fra"
        self.assertIs(self.sense.set_etymology_comment(commentaire, term_source_language=langage), self.sense)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyComment, commentaire)
        self.assertEqual(self.sense.definition[0].statement[0].termSourceLanguage, langage)

    def test_get_etymology_comment(self):
        comment = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologyComment = comment
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_comment(), comment)
        # Test with a language filter
        language = "eng"
        self.sense.definition[0].statement[0].termSourceLanguage = language
        self.assertIsNone(self.sense.get_etymology_comment(term_source_language="fra"))
        self.assertEqual(self.sense.get_etymology_comment(term_source_language=language), comment)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_gloss(self):
        gloss = "GLOSS"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_gloss(gloss), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologyGloss, gloss)

    def test_get_etymology_gloss(self):
        gloss = "GLOSS"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologyGloss = gloss
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_gloss(), gloss)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_etymology_source(self):
        source = "etymology"
        # There is no Definition instance
        self.assertIs(self.sense.set_etymology_source(source), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].etymologySource, source)

    def test_get_etymology_source(self):
        source = "etymology"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set etymology
        self.sense.definition[0].statement[0].etymologySource = source
        # Test get etymology
        self.assertEqual(self.sense.get_etymology_source(), source)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_set_scientific_name(self):
        name = "Scientificus"
        # There is no Definition instance
        self.assertIs(self.sense.set_scientific_name(name), self.sense)
        self.assertEqual(len(self.sense.definition), 1)
        self.assertEqual(len(self.sense.definition[0].statement), 1)
        self.assertEqual(self.sense.definition[0].statement[0].scientificName, name)

    def test_get_scientific_name(self):
        name = "Nameus"
        # Create definition and add it to the sense
        definition = Definition()
        self.sense.definition = [definition]
        # Create a statement and add it to the definition
        state = Statement()
        self.sense.definition[0].statement = [state]
        # Set scientific name
        self.sense.definition[0].statement[0].scientificName = name
        # Test get scientific name
        self.assertEqual(self.sense.get_scientific_name(), name)
        # Release created instances
        del self.sense.definition[0].statement[:]
        del state
        del self.sense.definition[:]
        del definition

    def test_create_paradigm(self):
        # Test create paradigm
        paradigm = self.sense.create_paradigm()
        self.assertIsInstance(paradigm, Paradigm)
        # Release Paradigm instance
        del paradigm

    def test_add_paradigm(self):
        # Create paradigms
        para1 = Paradigm()
        para2 = Paradigm()
        # Test add paradigms to the sense
        self.assertIs(self.sense.add_paradigm(para1), self.sense)
        self.assertListEqual(self.sense.paradigm, [para1])
        self.assertIs(self.sense.add_paradigm(para2), self.sense)
        self.assertListEqual(self.sense.paradigm, [para1, para2])
        # Release Paradigm instances
        del self.sense.paradigm[:]
        del para1, para2

    def test_get_paradigms(self):
        # List of Paradigm instances is empty
        self.assertListEqual(self.sense.get_paradigms(), [])
        # Create Paradigm instances and add them to the list
        para1 = Paradigm()
        para2 = Paradigm()
        self.sense.paradigm = [para1, para2]
        # Test get paradigms
        self.assertListEqual(self.sense.get_paradigms(), [para1, para2])
        # Delete Paradigm instances
        del self.sense.paradigm[:]
        del para1, para2

    def test_get_last_paradigm(self):
        # List of Paradigm instances is empty
        self.assertIsNone(self.sense.get_last_paradigm())
        # Create Paradigm instances and add them to the list
        para1 = Paradigm()
        para2 = Paradigm()
        self.sense.paradigm = [para1, para2]
        # Test get last paradigm
        self.assertIs(self.sense.get_last_paradigm(), para2)
        self.sense.paradigm.pop()
        self.assertIs(self.sense.get_last_paradigm(), para1)
        # Release Paradigm instances
        del self.sense.paradigm[:]
        del para1, para2

    def test_set_paradigm_label(self):
        label = "construction"
        # There is no Paradigm instance
        self.assertIs(self.sense.set_paradigm_label(label), self.sense)
        self.assertEqual(len(self.sense.paradigm), 1)
        self.assertEqual(self.sense.paradigm[0].paradigmLabel, label)
        # Test error case
        label = "whatever"
        self.sense.set_paradigm_label(label)

    def test_set_paradigm_form(self):
        # Test paradigm form only
        form = "paradigm"
        # There is no Paradigm instance
        self.assertIs(self.sense.set_paradigm_form(form), self.sense)
        self.assertEqual(len(self.sense.paradigm), 1)
        self.assertEqual(self.sense.paradigm[0].paradigm, form)
        # Test paradigm form and language
        form = "paradigme"
        langage = "fra"
        self.assertIs(self.sense.set_paradigm_form(form, langage), self.sense)
        self.assertEqual(len(self.sense.paradigm), 2)
        self.assertEqual(self.sense.paradigm[1].paradigm, form)
        self.assertEqual(self.sense.paradigm[1].language, langage)

    def test_set_morphology(self):
        morpho = "morpho"
        # There is no Paradigm instance
        self.assertIs(self.sense.set_morphology(morpho), self.sense)
        self.assertEqual(len(self.sense.paradigm), 1)
        self.assertEqual(self.sense.paradigm[0].morphology, morpho)

    def test_create_and_add_context(self):
        # Test create context
        context1 = self.sense.create_and_add_context()
        self.assertIsInstance(context1, Context)
        # Create another context
        context2 = self.sense.create_and_add_context()
        self.assertIsInstance(context2, Context)
        # Test add context
        self.assertListEqual(self.sense.context, [context1, context2])
        # Release Context instances
        del self.sense.context[:]
        del context1, context2

    def test_get_contexts(self):
        # List of Context instances is empty
        self.assertListEqual(self.sense.get_contexts(), [])
        # Create Context instances and add them to the list
        ctx1 = Context()
        ctx2 = Context()
        self.sense.context = [ctx1, ctx2]
        # Test get contexts
        self.assertListEqual(self.sense.get_contexts(), [ctx1, ctx2])
        # Delete Context instances
        del self.sense.context[:]
        del ctx1, ctx2

    def test_get_last_context(self):
        # List of Context instances is empty
        self.assertIsNone(self.sense.get_last_context())
        # Create Context instances and add them to the list
        ctx1 = Context()
        ctx2 = Context()
        self.sense.context = [ctx1, ctx2]
        # Test get last context
        self.assertIs(self.sense.get_last_context(), ctx2)
        self.sense.context.pop()
        self.assertIs(self.sense.get_last_context(), ctx1)
        # Release Context instances
        del self.sense.context[:]
        del ctx1, ctx2

    def test_create_example(self):
        ref = "toto"
        self.assertIs(self.sense.create_example(ref), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(self.sense.context[0].targets, ref)
        self.assertEqual(len(self.sense.context[0].text_representation), 0)

    def test_create_and_add_example(self):
        form = "written"
        self.assertIs(self.sense.create_and_add_example(form), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(len(self.sense.context[0].text_representation), 1)
        self.assertEqual(self.sense.context[0].text_representation[0].writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.sense.create_and_add_example(form, lang), self.sense)
        self.assertEqual(len(self.sense.context), 2)
        self.assertEqual(self.sense.context[1].type, "example")
        self.assertEqual(len(self.sense.context[1].text_representation), 1)
        self.assertEqual(self.sense.context[1].text_representation[0].writtenForm, form)
        self.assertEqual(self.sense.context[1].text_representation[0].language, lang)

    def test_add_example(self):
        form = "written"
        self.assertIs(self.sense.add_example(form), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(len(self.sense.context[0].text_representation), 1)
        self.assertEqual(self.sense.context[0].text_representation[0].writtenForm, form)
        # Test with language
        form = "form with lang"
        lang = "lang"
        self.assertIs(self.sense.add_example(form, lang), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(len(self.sense.context[0].text_representation), 2)
        self.assertEqual(self.sense.context[0].text_representation[1].writtenForm, form)
        self.assertEqual(self.sense.context[0].text_representation[1].language, lang)

    def test_set_example_comment(self):
        comment = "example"
        self.assertIs(self.sense.set_example_comment(comment), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(len(self.sense.context[0].text_representation), 1)
        self.assertEqual(self.sense.context[0].text_representation[0].comment, comment)
        # Test with a second comment
        comment = "another"
        self.assertIs(self.sense.set_example_comment(comment), self.sense)
        self.assertEqual(len(self.sense.context), 1)
        self.assertEqual(self.sense.context[0].type, "example")
        self.assertEqual(len(self.sense.context[0].text_representation), 2)
        self.assertEqual(self.sense.context[0].text_representation[1].comment, comment)

    def test_create_and_add_subject_field(self):
        # Test create subject field
        subject = self.sense.create_and_add_subject_field()
        self.assertIsInstance(subject, SubjectField)
        # Create another subject field
        field = self.sense.create_and_add_subject_field()
        self.assertIsInstance(field, SubjectField)
        # Test add subject fields
        self.assertListEqual(self.sense.subject_field, [subject, field])
        # Release SubjectField instances
        del self.sense.subject_field[:]
        del subject, field

    def test_get_subject_fields(self):
        # List of SubjectField instances is empty
        self.assertListEqual(self.sense.get_subject_fields(), [])
        # Create SubjectField instances and add them to the list
        subject = SubjectField()
        field = SubjectField()
        self.sense.subject_field = [subject, field]
        # Test get subject fields
        self.assertListEqual(self.sense.get_subject_fields(), [subject, field])
        # Delete SubjectField instances
        del self.sense.subject_field[:]
        del subject, field

    def test_set_semantic_domain(self):
        domain = "semantic"
        self.assertIs(self.sense.set_semantic_domain(domain), self.sense)
        self.assertEqual(len(self.sense.subject_field), 1)
        self.assertEqual(self.sense.subject_field[0].semanticDomain, domain)
        # Test with language
        domain = "domain with lang"
        lang = "lang"
        self.assertIs(self.sense.set_semantic_domain(domain, lang), self.sense)
        self.assertEqual(len(self.sense.subject_field), 2)
        self.assertEqual(self.sense.subject_field[1].semanticDomain, domain)
        self.assertEqual(self.sense.subject_field[1].language, lang)

    def test_create_and_add_equivalent(self):
        # Test create equivalent
        equivalent1 = self.sense.create_and_add_equivalent()
        self.assertIsInstance(equivalent1, Equivalent)
        # Create another equivalent
        equivalent2 = self.sense.create_and_add_equivalent()
        self.assertIsInstance(equivalent2, Equivalent)
        # Test add equivalents
        self.assertListEqual(self.sense.equivalent, [equivalent1, equivalent2])
        # Release Equivalent instances
        del self.sense.equivalent[:]
        del equivalent1, equivalent2

    def test_get_equivalents(self):
        # List of Equivalent instances is empty
        self.assertListEqual(self.sense.get_equivalents(), [])
        # Create Equivalent instances and add them to the list
        equivalent1 = Equivalent()
        equivalent2 = Equivalent()
        self.sense.equivalent = [equivalent1, equivalent2]
        # Test get equivalents
        self.assertListEqual(self.sense.get_equivalents(), [equivalent1, equivalent2])
        # Delete Equivalent instances
        del self.sense.equivalent[:]
        del equivalent1, equivalent2

    def test_set_translation(self):
        trans = "trans"
        self.assertIs(self.sense.set_translation(trans), self.sense)
        self.assertEqual(len(self.sense.equivalent), 1)
        self.assertEqual(self.sense.equivalent[0].translation, trans)
        # Test with language
        trans = "trans with lang"
        lang = "lang"
        self.assertIs(self.sense.set_translation(trans, lang), self.sense)
        self.assertEqual(len(self.sense.equivalent), 2)
        self.assertEqual(self.sense.equivalent[1].translation, trans)
        self.assertEqual(self.sense.equivalent[1].language, lang)

    def test_get_translations(self):
        # List of Equivalent instances is empty
        self.assertListEqual(self.sense.get_translations(), [])
        # Create Equivalent instances and add them to the list
        equivalent1 = Equivalent()
        equivalent2 = Equivalent()
        self.sense.equivalent = [equivalent1, equivalent2]
        # Set their translations
        trans1 = "trans1"
        trans2 = "trans2"
        equivalent1.translation = trans1
        # Test get translations
        self.assertListEqual(self.sense.get_translations(), [trans1])
        equivalent2.translation = trans2
        self.assertListEqual(self.sense.get_translations(), [trans1, trans2])
        # Test with a language filter
        lang = "lang"
        equivalent2.language = lang
        self.assertListEqual(self.sense.get_translations(), [trans1, trans2])
        self.assertListEqual(self.sense.get_translations("eng"), [])
        self.assertListEqual(self.sense.get_translations(lang), [trans2])
        # Delete Equivalent instances
        del self.sense.equivalent[:]
        del equivalent1, equivalent2

suite = unittest.TestLoader().loadTestsFromTestCase(TestSenseFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
