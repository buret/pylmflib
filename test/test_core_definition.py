#! /usr/bin/env python

from startup import *
from core.definition import Definition
from core.statement import Statement

## Test Definition class

class TestDefinitionFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Definition object
        self.definition = Definition()

    def tearDown(self):
        # Release instantiated objects
        del self.definition

    def test_init(self):
        self.assertIsNone(self.definition.language)
        self.assertIsNone(self.definition.definition)
        self.assertIsNone(self.definition.gloss)
        self.assertIsNone(self.definition.literally)
        self.assertListEqual(self.definition.text_representation, [])
        self.assertListEqual(self.definition.statement, [])

    def test_set_language(self):
        lang = "Python"
        self.assertIs(self.definition.set_language(lang), self.definition)
        self.assertEqual(self.definition.language, lang)

    def test_get_language(self):
        # Set language
        lang = "python"
        self.definition.language = lang
        # Test get language
        self.assertEqual(self.definition.get_language(), lang)

    def test_set_definition(self):
        # Test definition only
        definition = "blablabla"
        self.assertIs(self.definition.set_definition(definition), self.definition)
        self.assertEqual(self.definition.definition, definition)
        # Test definition and language
        definition = "This is a definition."
        language = "eng"
        self.assertIs(self.definition.set_definition(definition, language), self.definition)
        self.assertEqual(self.definition.definition, definition)
        self.assertEqual(self.definition.language, language)

    def test_get_definition(self):
        # Set definition
        definition = "whatever"
        self.definition.definition = definition
        # Test get definition
        self.assertEqual(self.definition.get_definition(), definition)
        # Test with a language filter
        language = "eng"
        self.definition.language = language
        self.assertEqual(self.definition.get_definition(), definition)
        self.assertIsNone(self.definition.get_definition("fra"))
        self.assertEqual(self.definition.get_definition(language), definition)

    def test_set_gloss(self):
        # Test gloss only
        gloss = "BLA"
        self.assertIs(self.definition.set_gloss(gloss), self.definition)
        self.assertEqual(self.definition.gloss, gloss)
        # Test gloss and language
        gloss = "This is a gloss."
        language = "eng"
        self.assertIs(self.definition.set_gloss(gloss, language), self.definition)
        self.assertEqual(self.definition.gloss, gloss)
        self.assertEqual(self.definition.language, language)

    def test_get_gloss(self):
        # Set gloss
        gloss = "WHATEVER"
        self.definition.gloss = gloss
        # Test get gloss
        self.assertEqual(self.definition.get_gloss(), gloss)
        # Test with a language filter
        language = "eng"
        self.definition.language = language
        self.assertEqual(self.definition.get_gloss(), gloss)
        self.assertIsNone(self.definition.get_gloss("fra"))
        self.assertEqual(self.definition.get_gloss(language), gloss)

    def test_create_statement(self):
        # Test create statement
        statement = self.definition.create_statement()
        self.assertIsInstance(statement, Statement)
        # Release Statement instance
        del statement

    def test_add_statement(self):
        # Create statements
        state1 = Statement()
        state2 = Statement()
        # Test add statements to the definition
        self.assertIs(self.definition.add_statement(state1), self.definition)
        self.assertListEqual(self.definition.statement, [state1])
        self.assertIs(self.definition.add_statement(state2), self.definition)
        self.assertListEqual(self.definition.statement, [state1, state2])
        # Release Statement instances
        del self.definition.statement[:]
        del state1, state2

    def test_get_statements(self):
        # List of Statement instances is empty
        self.assertListEqual(self.definition.get_statements(), [])
        # Create Statement instances and add them to the list
        state1 = Statement()
        state2 = Statement()
        self.definition.statement = [state1, state2]
        # Test get statements
        self.assertListEqual(self.definition.get_statements(), [state1, state2])
        # Delete Statement instances
        del self.definition.statement[:]
        del state1, state2

    def test_set_note(self):
        note = "note"
        # There is no Statement instance
        self.assertIs(self.definition.set_note(note), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].note, note)
        # Test set a second note
        language = "Python"
        self.assertIs(self.definition.set_note(note, language=language), self.definition)
        self.assertEqual(len(self.definition.statement), 2)
        self.assertEqual(self.definition.statement[1].note, note)
        self.assertEqual(self.definition.statement[1].language, language)

    def test_find_notes(self):
        # Create several statements with different notes, types and languages
        state1 = Statement().set_note("note1", "comparison", "eng")
        state2 = Statement().set_note("note2", "general", "fra")
        state3 = Statement().set_note("note3", "comparison")
        state4 = Statement().set_note("note4", "history")
        # Add statements to the definition
        self.definition.statement = [state1, state2, state3, state4]
        # Test find notes
        self.assertListEqual(self.definition.find_notes("general"), [state2.note])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.definition.find_notes("comparison")), set([state1.note, state3.note]))
        # Release Statement instances
        del self.definition.statement[:]
        del state1, state2, state3, state4

    def test_set_usage_note(self):
        note = "note"
        # There is no Statement instance
        self.assertIs(self.definition.set_usage_note(note), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].usageNote, note)
        # Test set a second usage note
        language = "Python"
        self.assertIs(self.definition.set_usage_note(note, language=language), self.definition)
        self.assertEqual(len(self.definition.statement), 2)
        self.assertEqual(self.definition.statement[1].usageNote, note)
        self.assertEqual(self.definition.statement[1].language, language)

    def test_find_usage_notes(self):
        # Create several statements with different usage notes and languages
        state1 = Statement().set_usageNote("note1", "eng")
        state2 = Statement().set_usageNote("note2", "fra")
        state3 = Statement().set_usageNote("note3", "eng")
        state4 = Statement().set_usageNote("note4")
        # Add statements to the definition
        self.definition.statement = [state1, state2, state3, state4]
        # Test find usage notes
        self.assertListEqual(self.definition.find_usage_notes("fra"), [state2.usageNote])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.definition.find_usage_notes("eng")), set([state1.usageNote, state3.usageNote]))
        # Release Statement instances
        del self.definition.statement[:]
        del state1, state2, state3, state4

    def test_set_encyclopedic_information(self):
        info = "note"
        # There is no Statement instance
        self.assertIs(self.definition.set_encyclopedic_information(info), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].encyclopedicInformation, info)
        # Test set a second encyclopedic information
        language = "Python"
        self.assertIs(self.definition.set_encyclopedic_information(info, language=language), self.definition)
        self.assertEqual(len(self.definition.statement), 2)
        self.assertEqual(self.definition.statement[1].encyclopedicInformation, info)
        self.assertEqual(self.definition.statement[1].language, language)

    def test_find_encyclopedic_informations(self):
        # Create several statements with different encyclopedic informations and languages
        state1 = Statement().set_encyclopedicInformation("info1", "eng")
        state2 = Statement().set_encyclopedicInformation("info2", "fra")
        state3 = Statement().set_encyclopedicInformation("info3", "eng")
        state4 = Statement().set_encyclopedicInformation("info4")
        # Add statements to the definition
        self.definition.statement = [state1, state2, state3, state4]
        # Test find usage notes
        self.assertListEqual(self.definition.find_encyclopedic_informations("fra"), [state2.encyclopedicInformation])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.definition.find_encyclopedic_informations("eng")), set([state1.encyclopedicInformation, state3.encyclopedicInformation]))
        # Release Statement instances
        del self.definition.statement[:]
        del state1, state2, state3, state4

    def test_set_restriction(self):
        only = "note"
        # There is no Statement instance
        self.assertIs(self.definition.set_restriction(only), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].restriction, only)
        # Test set a second restriction
        language = "Python"
        self.assertIs(self.definition.set_restriction(only, language=language), self.definition)
        self.assertEqual(len(self.definition.statement), 2)
        self.assertEqual(self.definition.statement[1].restriction, only)
        self.assertEqual(self.definition.statement[1].language, language)

    def test_find_restrictions(self):
        # Create several statements with different restrictions and languages
        state1 = Statement().set_restriction("only1", "eng")
        state2 = Statement().set_restriction("only2", "fra")
        state3 = Statement().set_restriction("only3", "eng")
        state4 = Statement().set_restriction("only4")
        # Add statements to the definition
        self.definition.statement = [state1, state2, state3, state4]
        # Test find usage notes
        self.assertListEqual(self.definition.find_restrictions("fra"), [state2.restriction])
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.definition.find_restrictions("eng")), set([state1.restriction, state3.restriction]))
        # Release Statement instances
        del self.definition.statement[:]
        del state1, state2, state3, state4

    def test_set_borrowed_word(self):
        word = "borrowed"
        # There is no Statement instance
        self.assertIs(self.definition.set_borrowed_word(word), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].borrowedWord, word)

    def test_get_borrowed_word(self):
        word = "borrowed"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set borrowed word
        self.definition.statement[0].borrowedWord = word
        # Test get borrowed word
        self.assertEqual(self.definition.get_borrowed_word(), word)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_writtenForm(self):
        form = "written"
        # There is no Statement instance
        self.assertIs(self.definition.set_written_form(form), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].writtenForm, form)

    def test_get_writtenForm(self):
        form = "written"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set written form
        self.definition.statement[0].writtenForm = form
        # Test get written form
        self.assertEqual(self.definition.get_written_form(), form)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_etymology(self):
        etymology = "etymology"
        # There is no Statement instance
        self.assertIs(self.definition.set_etymology(etymology), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].etymology, etymology)

    def test_get_etymology(self):
        etymology = "etymology"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set etymology
        self.definition.statement[0].etymology = etymology
        # Test get etymology
        self.assertEqual(self.definition.get_etymology(), etymology)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_etymology_comment(self):
        # Test etymology comment only
        comment = "etymology"
        # There is no Statement instance
        self.assertIs(self.definition.set_etymology_comment(comment), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].etymologyComment, comment)
        # Test etymology comment and language
        commentaire = "etymologie"
        langage = "fra"
        self.assertIs(self.definition.set_etymology_comment(commentaire, term_source_language=langage), self.definition)
        self.assertEqual(self.definition.statement[0].etymologyComment, commentaire)
        self.assertEqual(self.definition.statement[0].termSourceLanguage, langage)

    def test_get_etymology_comment(self):
        comment = "etymology"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set etymology comment
        self.definition.statement[0].etymologyComment = comment
        # Test get etymology comment
        self.assertEqual(self.definition.get_etymology_comment(), comment)
        # Test with a language filter
        language = "eng"
        self.definition.statement[0].termSourceLanguage = language
        self.assertIsNone(self.definition.get_etymology_comment(term_source_language="fra"))
        self.assertEqual(self.definition.get_etymology_comment(term_source_language=language), comment)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_etymology_gloss(self):
        gloss = "GLOSS"
        # There is no Statement instance
        self.assertIs(self.definition.set_etymology_gloss(gloss), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].etymologyGloss, gloss)

    def test_get_etymology_gloss(self):
        gloss = "GLOSS"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set etymology gloss
        self.definition.statement[0].etymologyGloss = gloss
        # Test get etymology gloss
        self.assertEqual(self.definition.get_etymology_gloss(), gloss)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_etymology_source(self):
        source = "etymology"
        # There is no Statement instance
        self.assertIs(self.definition.set_etymology_source(source), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].etymologySource, source)

    def test_get_etymology_source(self):
        source = "etymology"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set etymology source
        self.definition.statement[0].etymologySource = source
        # Test get etymology source
        self.assertEqual(self.definition.get_etymology_source(), source)
        # Release Statement instance
        del self.definition.statement[:]
        del state

    def test_set_scientific_name(self):
        name = "Brutus"
        # There is no Statement instance
        self.assertIs(self.definition.set_scientific_name(name), self.definition)
        self.assertEqual(len(self.definition.statement), 1)
        self.assertEqual(self.definition.statement[0].scientificName, name)

    def test_get_scientific_name(self):
        name = "Maximus"
        # Create a statement
        state = Statement()
        # Add statement to the definition
        self.definition.statement = [state]
        # Set scientific name
        self.definition.statement[0].scientificName = name
        # Test get scientific name
        self.assertEqual(self.definition.get_scientific_name(), name)
        # Release Statement instance
        del self.definition.statement[:]
        del state

suite = unittest.TestLoader().loadTestsFromTestCase(TestDefinitionFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
