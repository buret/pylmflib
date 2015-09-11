#! /usr/bin/env python

from startup import *
from mrd.subject_field import SubjectField

## Test SubjectField class

class TestSubjectFieldFunctions(unittest.TestCase):

    def setUp(self):
        # Instantiate a SubjectField object
        self.subject_field = SubjectField()

    def tearDown(self):
        # Release instantiated objects
        del self.subject_field

    def test_init(self):
        self.assertIsNone(self.subject_field.language)
        self.assertIsNone(self.subject_field.semanticDomain)
        self.assertListEqual(self.subject_field.subject_field, [])

    def test_set_semanticDomain(self):
        domain = "semantic"
        self.assertIs(self.subject_field.set_semanticDomain(domain), self.subject_field)
        self.assertEqual(self.subject_field.semanticDomain, domain)
        # Test with language
        domain = "semantic with lang"
        lang = "lang"
        self.assertIs(self.subject_field.set_semanticDomain(domain, lang), self.subject_field)
        self.assertEqual(self.subject_field.semanticDomain, domain)
        self.assertEqual(self.subject_field.language, lang)

    def test_get_semanticDomain(self):
        self.assertIsNone(self.subject_field.get_semanticDomain())
        domain = "semantic"
        self.subject_field.semanticDomain = domain
        self.assertEqual(self.subject_field.get_semanticDomain(), domain)
        # Test with a language filter
        language = "eng"
        self.subject_field.language = language
        self.assertEqual(self.subject_field.get_semanticDomain(), domain)
        self.assertIsNone(self.subject_field.get_semanticDomain("fra"))
        self.assertEqual(self.subject_field.get_semanticDomain("eng"), domain)

    def test_set_language(self):
        language = "English"
        self.assertIs(self.subject_field.set_language(language), self.subject_field)
        self.assertEqual(self.subject_field.language, language)

    def test_get_language(self):
        language = "language"
        self.subject_field.language = language
        self.assertEqual(self.subject_field.get_language(), language)

    def test_create_and_add_subject_field(self):
        # Test create subject field
        subject = self.subject_field.create_and_add_subject_field()
        self.assertIsInstance(subject, SubjectField)
        # Create another subject field
        field = self.subject_field.create_and_add_subject_field()
        self.assertIsInstance(field, SubjectField)
        # Test add subject fields
        self.assertListEqual(self.subject_field.subject_field, [subject, field])
        # Release SubjectField instances
        del self.subject_field.subject_field[:]
        del subject, field

    def test_get_subject_fields(self):
        # List of SubjectField instances is empty
        self.assertListEqual(self.subject_field.get_subject_fields(), [])
        # Create SubjectField instances and add them to the list
        subject = SubjectField()
        field = SubjectField()
        self.subject_field.subject_field = [subject, field]
        # Test get subject fields
        self.assertListEqual(self.subject_field.get_subject_fields(), [subject, field])
        # Delete SubjectField instances
        del self.subject_field.subject_field[:]
        del subject, field

    def test_set_sub_domain(self):
        domain = "semantic"
        self.assertIs(self.subject_field.set_sub_domain(domain), self.subject_field)
        self.assertEqual(len(self.subject_field.subject_field), 1)
        self.assertEqual(self.subject_field.subject_field[0].semanticDomain, domain)
        # Test with language
        domain = "semantic with lang"
        lang = "lang"
        self.assertIs(self.subject_field.set_sub_domain(domain, lang), self.subject_field)
        self.assertEqual(len(self.subject_field.subject_field), 2)
        self.assertEqual(self.subject_field.subject_field[1].semanticDomain, domain)
        self.assertEqual(self.subject_field.subject_field[1].language, lang)

    def test_get_sub_domains(self):
        self.assertListEqual(self.subject_field.get_sub_domains(), [])
        # Create SubjectField instances and add them to the list
        subject = SubjectField()
        field = SubjectField()
        self.subject_field.subject_field = [subject, field]
        domain1 = "semantic"
        self.subject_field.subject_field[0].semanticDomain = domain1
        self.assertEqual(self.subject_field.get_sub_domains(), [domain1])
        # Test with a language filter
        domain2 = "domain"
        language = "eng"
        self.subject_field.subject_field[1].semanticDomain = domain2
        self.subject_field.subject_field[1].language = language
        self.assertEqual(self.subject_field.get_sub_domains(), [domain1, domain2])
        self.assertListEqual(self.subject_field.get_sub_domains("fra"), [])
        self.assertEqual(self.subject_field.get_sub_domains("eng"), [domain2])

suite = unittest.TestLoader().loadTestsFromTestCase(TestSubjectFieldFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
