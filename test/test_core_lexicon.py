#! /usr/bin/env python

from startup import *
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry

## Test Lexicon class

class TestLexiconFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a Lexicon object
        self.lexicon = Lexicon()

    def tearDown(self):
        # Release instantiated objects
        del self.lexicon

    def test_init(self):
        self.assertIsNone(self.lexicon.language)
        self.assertIsNone(self.lexicon.languageScript)
        self.assertIsNone(self.lexicon.id)
        self.assertIsNone(self.lexicon.label)
        self.assertIsNone(self.lexicon.lexiconType)
        self.assertIsNone(self.lexicon.entrySource)
        self.assertIsNone(self.lexicon.vowelHarmony)
        self.assertListEqual(self.lexicon.lexical_entry, [])
        self.assertIsNone(self.lexicon.localPath)

    def test_set_id(self):
        id = "English lexicon"
        self.assertEqual(self.lexicon.set_id(id), self.lexicon)
        self.assertEqual(self.lexicon.id, id)

    def test_get_id(self):
        self.assertIs(self.lexicon.get_id(), self.lexicon.id)

    def test_set_language(self):
        language = "eng"
        self.assertEqual(self.lexicon.set_language(language), self.lexicon)
        self.assertEqual(self.lexicon.language, language)

    def test_get_language(self):
        self.assertIs(self.lexicon.get_language(), self.lexicon.language)

    def test_set_languageScript(self):
        script = "latn"
        self.assertEqual(self.lexicon.set_languageScript(script), self.lexicon)
        self.assertEqual(self.lexicon.languageScript, script)

    def test_get_languageScript(self):
        self.assertIs(self.lexicon.get_languageScript(), self.lexicon.languageScript)

    def test_set_label(self):
        label = "online dictionary"
        self.assertEqual(self.lexicon.set_label(label), self.lexicon)
        self.assertEqual(self.lexicon.label, label)

    def test_get_label(self):
        self.assertIs(self.lexicon.get_label(), self.lexicon.label)

    def test_set_lexiconType(self):
        type = "bilingual dictionary"
        self.assertEqual(self.lexicon.set_lexiconType(type), self.lexicon)
        self.assertEqual(self.lexicon.lexiconType, type)

    def test_get_lexiconType(self):
        self.assertIs(self.lexicon.get_lexiconType(), self.lexicon.lexiconType)

    def test_set_entrySource(self):
        source = "test.txt"
        self.assertEqual(self.lexicon.set_entrySource(source), self.lexicon)
        self.assertEqual(self.lexicon.entrySource, source)

    def test_get_entrySource(self):
        self.assertIs(self.lexicon.get_entrySource(), self.lexicon.entrySource)

    def test_set_vowelHarmony(self):
        test = False
        try:
            self.lexicon.set_vowelHarmony(None)
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_get_vowelHarmony(self):
        test = False
        try:
            self.lexicon.get_vowelHarmony()
        except NotImplementedError:
            test = True
        self.assertTrue(test)

    def test_set_localPath(self):
        path = "/full/local/path/to/audio/files/"
        self.assertEqual(self.lexicon.set_localPath(path), self.lexicon)
        self.assertEqual(self.lexicon.localPath, path)

    def test_get_localPath(self):
        self.assertIs(self.lexicon.get_localPath(), self.lexicon.localPath)

    def test_get_lexical_entries(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2]
        # Test get lexical entries
        self.assertListEqual(self.lexicon.get_lexical_entries(), [entry1, entry2])
        self.lexicon.lexical_entry.append(entry1)
        self.assertListEqual(self.lexicon.get_lexical_entries(), [entry1, entry2, entry1])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_add_lexical_entry(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Test add entries to the lexicon
        self.assertEqual(self.lexicon.add_lexical_entry(entry1), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry1])
        self.assertEqual(self.lexicon.add_lexical_entry(entry2), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry1, entry2])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_remove_lexical_entry(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2]
        # Test remove lexical entries
        self.assertEqual(self.lexicon.remove_lexical_entry(entry1), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [entry2])
        self.assertEqual(self.lexicon.remove_lexical_entry(entry2), self.lexicon)
        self.assertListEqual(self.lexicon.lexical_entry, [])
        # Release LexicalEntry instances
        del entry1, entry2

    def test_count_lexical_entries(self):
        # Create lexical entries
        entry1 = LexicalEntry()
        entry2 = LexicalEntry()
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1]
        # Test count lexical entries
        self.assertEqual(self.lexicon.count_lexical_entries(), 1)
        self.lexicon.lexical_entry.append(entry2)
        self.assertEqual(self.lexicon.count_lexical_entries(), 2)
        self.lexicon.lexical_entry.append(entry1)
        self.assertEqual(self.lexicon.count_lexical_entries(), 3)
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2

    def test_sort_homonym_numbers(self):
        # Create several lexical entries
        entry1 = LexicalEntry().set_lexeme("aa").set_homonymNumber("2")
        entry2 = LexicalEntry().set_lexeme("aa").set_homonymNumber("1")
        entry3 = LexicalEntry().set_lexeme("ab")
        entry4 = LexicalEntry().set_lexeme("ba")
        entry5 = LexicalEntry().set_lexeme("bb").set_homonymNumber("6")
        entry6 = LexicalEntry().set_lexeme("bb").set_homonymNumber("5")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2, entry3, entry4, entry5, entry6]
        # Test sort homonym numbers
        self.assertListEqual(self.lexicon.sort_homonym_numbers(), [entry2, entry1, entry3, entry4, entry6, entry5])
        self.assertListEqual(self.lexicon.lexical_entry, [entry2, entry1, entry3, entry4, entry6, entry5])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4, entry5, entry6

    def test_sort_lexical_entries(self):
        # Create several lexical entries with different lexemes
        entry1 = LexicalEntry().set_lexeme("aa")
        entry2 = LexicalEntry().set_lexeme("ab")
        entry3 = LexicalEntry().set_lexeme("ba")
        entry4 = LexicalEntry().set_lexeme("bb")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry4, entry1, entry2, entry3]
        # Test sort lexical entries
        self.assertListEqual(self.lexicon.sort_lexical_entries(), [entry1, entry2, entry3, entry4])
        self.assertListEqual(self.lexicon.lexical_entry, [entry1, entry2, entry3, entry4])
        # Provide a sort order
        my_order = dict({'A':1.1, 'a':1.2, 'B':2.1, 'b':2.2})
        my_unicode_order = ({})
        for key in my_order.keys():
            my_unicode_order.update({key.decode(encoding='utf8'):my_order[key]})
        entry5 = LexicalEntry().set_lexeme("Aa")
        entry6 = LexicalEntry().set_lexeme("bB")
        self.lexicon.lexical_entry.append(entry5)
        self.lexicon.lexical_entry.append(entry6)
        self.assertListEqual(self.lexicon.sort_lexical_entries(sort_order=my_order), [entry5, entry1, entry2, entry3, entry6, entry4])
        self.assertListEqual(self.lexicon.lexical_entry, [entry5, entry1, entry2, entry3, entry6, entry4])
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4, entry5, entry6

    def test_find_lexical_entries(self):
        # Create several lexical entries with different lexemes
        entry1 = LexicalEntry().set_lexeme("Hello")
        entry2 = LexicalEntry().set_lexeme("world!")
        entry3 = LexicalEntry().set_lexeme("hello")
        entry4 = LexicalEntry().set_lexeme("world")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2, entry3, entry4]
        # Test find lexical entries
        self.assertListEqual(self.lexicon.find_lexical_entries(lambda entry: entry.get_lexeme() == "Hello"), [entry1])
        def test_filter(entry):
            return entry.get_lexeme().lower() == "hello"
        # List is randomly ordered => create a set to avoid random results
        self.assertEqual(set(self.lexicon.find_lexical_entries(test_filter)), set([entry1, entry3]))
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4

    def test_check_cross_references(self):
        # Create lexical entries with lexemes and related lexemes
        entry1 = LexicalEntry().set_lexeme("Hello").create_and_add_related_form("world!", "main entry")
        entry2 = LexicalEntry().set_lexeme("world!").create_and_add_related_form("Hello", "subentry")
        # Add entries to the lexicon
        self.lexicon.lexical_entry = [entry1, entry2]
        # Test check cross references
        self.assertIs(self.lexicon.check_cross_references(), self.lexicon)
        self.assertIs(entry1.related_form[0].get_lexical_entry(), entry2)
        self.assertIs(entry2.related_form[0].get_lexical_entry(), entry1)
        # Test warning case: entry not found
        entry3 = LexicalEntry().set_lexeme("hello").create_and_add_related_form("world", "main entry")
        self.lexicon.lexical_entry.append(entry3)
        self.lexicon.reset_check()
        self.lexicon.check_cross_references()
        # Retrieve nominal case
        entry4 = LexicalEntry().set_lexeme("world")
        self.lexicon.lexical_entry.append(entry4)
        self.lexicon.reset_check()
        self.assertIs(self.lexicon.check_cross_references(), self.lexicon)
        self.assertIs(entry3.related_form[0].get_lexical_entry(), entry4)
        # Test warning case: several entries found
        entry5 = LexicalEntry().set_lexeme("world")
        self.lexicon.lexical_entry.append(entry5)
        self.lexicon.reset_check()
        self.lexicon.check_cross_references()
        # Test check cross references with homonym number
        entry3.related_form[0].set_lexical_entry(None)
        entry3.related_form[0].targets = "world2"
        entry4.homonymNumber = "1"
        entry5.homonymNumber = "2"
        self.lexicon.reset_check()
        self.assertIs(self.lexicon.check_cross_references(), self.lexicon)
        self.assertIs(entry3.related_form[0].get_lexical_entry(), entry5)
        # Release LexicalEntry instances
        del self.lexicon.lexical_entry[:]
        del entry1, entry2, entry3, entry4, entry5

    def test_convert_to_latex(self):
        pass

suite = unittest.TestLoader().loadTestsFromTestCase(TestLexiconFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
