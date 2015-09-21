#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *
from config.xml import sort_order_read, config_read
import config

## Test sort order functions

class TestSortOrderFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_sort_order_read(self):
        import sys
        utest_path = sys.path[0] + '/'
        sort_order_filename = utest_path + "../pylmflib/config/default/sort_order.xml"
        # Read XML sort order file and test result
        order = sort_order_read(sort_order_filename)
        expected_order = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26}
        self.assertEqual(order, expected_order)

    def test_config_read(self):
        import sys
        utest_path = sys.path[0] + '/'
        config_filename = utest_path + "../pylmflib/config/default/config.xml"
        # Read XML config file and test result
        lexical_resource = config_read(config_filename)
        self.assertEqual(config.xml.vernacular, "ver")
        self.assertEqual(config.xml.English, "eng")
        self.assertEqual(config.xml.national, "nat")
        self.assertEqual(config.xml.regional, "reg")
        self.assertEqual(config.xml.French, "fra")
        self.assertEqual(config.xml.font["vernacular"]("test"), "\\textbf{\ipa{test}}")
        self.assertEqual(config.xml.font["English"]("test"), "test")
        self.assertEqual(config.xml.font["national"]("test"), "\\textit{\zh{test}}")
        self.assertEqual(config.xml.font["regional"]("test"), "\ipa{test}")
        self.assertEqual(config.xml.font["French"]("test"), "test")
        self.assertEqual(lexical_resource.get_dtdVersion(), "16")
        self.assertEqual(lexical_resource.get_language_code(), "ISO-639-3")
        self.assertEqual(lexical_resource.get_author(), u"Céline Buret")
        self.assertEqual(lexical_resource.get_version(), "0.1")
        self.assertEqual(lexical_resource.get_license(), "GPL")
        self.assertEqual(lexical_resource.get_character_encoding(), "UTF-8")
        self.assertEqual(lexical_resource.get_date_coding(), "ISO-8601")
        self.assertEqual(lexical_resource.get_creation_date(), "2015-09-30")
        self.assertEqual(lexical_resource.get_project_name(), "ANR HimalCo")
        self.assertEqual(lexical_resource.get_description(), "This is a lexicon of the HimalCo project.")

suite = unittest.TestLoader().loadTestsFromTestCase(TestSortOrderFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
