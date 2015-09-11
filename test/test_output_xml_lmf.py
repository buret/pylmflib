#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *
from output.xml_lmf import xml_lmf_write, build_sub_elements, add_link, handle_reserved, handle_fv, handle_fn, handle_font, handle_pinyin, handle_caps, handle_tones
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from utils.xml_format import Element, SubElement, tostring
from utils.io import EOL, ENCODING

## Test XML LMF functions

class TestXmlLmfFunctions(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_xml_lmf_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        # Write XML LMF file and test result
        utest_path = sys.path[0] + '/'
        xml_lmf_filename = utest_path + "lmf_output.xml"
        xml_lmf_write(lexical_entry, xml_lmf_filename)
        xml_lmf_file = open(xml_lmf_filename, "r")
        expected_lines = ["""<?xml version="1.0" encoding="utf-8"?>""" + EOL,
            """<LexicalEntry id="0">""" + EOL,
            """    <feat att="status" val="draft"/>""" + EOL,
            """    <Lemma>""" + EOL,
            """        <feat att="lexeme" val="hello"/>""" + EOL,
            """    </Lemma>""" + EOL,
            """    <feat att="partOfSpeech" val="toto"/>""" + EOL,
            """</LexicalEntry>""" + EOL]
        self.assertListEqual(expected_lines, xml_lmf_file.readlines())
        xml_lmf_file.close()
        del lexical_entry.lemma
        lexical_entry.lemma = None
        del lexical_entry
        # Remove XML LMF file
        os.remove(xml_lmf_filename)

    def test_build_sub_elements(self):
        # Create LMF objects and an empty XML element
        instance = LexicalEntry()
        instance.lemma = Lemma()
        instance.partOfSpeech = "toto"
        instance.status = "draft"
        instance.lemma.lexeme = "hello"
        element = Element("LexicalEntry")
        # Build sub-elements and test result
        build_sub_elements(instance, element)
        lemma = element.find("Lemma")
        lexeme = lemma.find("feat")
        self.assertEqual(lexeme.attrib["att"], "lexeme")
        self.assertEqual(lexeme.attrib["val"], "hello")
        [status, partOfSpeech] = element.findall("feat")
        self.assertEqual(partOfSpeech.attrib["att"], "partOfSpeech")
        self.assertEqual(partOfSpeech.attrib["val"], "toto")
        self.assertEqual(status.attrib["att"], "status")
        self.assertEqual(status.attrib["val"], "draft")
        del instance.lemma
        instance.lemma = None
        del instance, element

    def test_add_link(self):
        from morphology.related_form import RelatedForm
        input = Element("RelatedForm", targets="lx")
        form = RelatedForm()
        form.set_lexical_entry(LexicalEntry(id="lx_id"))
        # Create output element and sub-elements
        output = Element("RelatedForm", targets="lx")
        sub = SubElement(output, "a")
        sub.attrib["href"] = "lx_id1"
        # Fill in text
        sub.text = "lx"
        result = add_link(form, input)
        self.assertEqual(result[0], form)
        self.assertEqual(tostring(result[1]), tostring(output))

    def test_handle_reserved(self):
        pass

    def test_handle_fv(self):
        value1 = "fv:something here and fv:there"
        value2 = "|fv{something here} and fv:there"
        for value in [value1, value2]:
            input = Element("name", val=unicode(value))
            # Create output element and sub-elements
            output = Element("name", val=unicode(value))
            sub1 = SubElement(output, "span")
            sub1.attrib["class"] = "vernacular"
            sub2 = SubElement(output, "span")
            sub2.attrib["class"] = "vernacular"
            # Fill in text
            output.text = ""
            if value == value1:
                sub1.text = "something"
                sub1.tail = " here and "
            elif value == value2:
                sub1.text = "something here"
                sub1.tail = " and "
            sub2.text = "there"
            sub2.tail = ""
            self.assertEqual(tostring(handle_fv(input)), tostring(output))

    def test_handle_fn(self):
        value1 = "textfn:this fn:but not this"
        value2 = "textfn:this |fn{and this}"
        for value in [value1, value2]:
            input = Element("name", val=unicode(value))
            # Create output element and sub-elements
            output = Element("name", val=unicode(value))
            sub1 = SubElement(output, "span")
            sub1.attrib["class"] = "national"
            sub2 = SubElement(output, "span")
            sub2.attrib["class"] = "national"
            # Fill in text
            output.text = "text"
            sub1.text = "this"
            sub1.tail = " "
            if value == value1:
                sub2.text = "but"
                sub2.tail = " not this"
            elif value == value2:
                sub2.text = "and this"
                sub2.tail = ""
            self.assertEqual(tostring(handle_fn(input)), tostring(output))

    def test_handle_font(self):
        value = "blaA{bla1} blaB {bla2}blaC {bla3}"
        input = Element("name", val=unicode(value))
        # Create output element and sub-elements
        output = Element("name", val=unicode(value))
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "ipa"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "ipa"
        sub3 = SubElement(output, "span")
        sub3.attrib["class"] = "ipa"
        # Fill in text
        output.text = "blaA"
        sub1.text = "bla1"
        sub1.tail = " blaB "
        sub2.text = "bla2"
        sub2.tail = "blaC "
        sub3.text = "bla3"
        sub3.tail = ""
        self.assertEqual(tostring(handle_font(input)), tostring(output))

    def test_handle_pinyin(self):
        value = "@at1 atA@at2 atB"
        input = Element("name", val=unicode(value))
        # Create output element and sub-elements
        output = Element("name", val=unicode(value))
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "pinyin"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "pinyin"
        # Fill in text
        output.text = ""
        sub1.text = "at1"
        sub1.tail = " atA"
        sub2.text = "at2"
        sub2.tail = " atB"
        self.assertEqual(tostring(handle_pinyin(input)), tostring(output))

    def test_handle_caps(self):
        value = u"°trucs et°astuces"
        input = Element("name", val=value)
        # Create output element and sub-elements
        output = Element("name", val=value)
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "sc"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "sc"
        # Fill in text
        output.text = ""
        sub1.text = "trucs"
        sub1.tail = " et"
        sub2.text = "astuces"
        sub2.tail = ""
        self.assertEqual(tostring(handle_caps(input)), tostring(output))

    def test_handle_tones(self):
        ## Test "tone"
        value = u"LaM1H"
        input = Element("name", att="tone", val=value)
        # Create output element and sub-elements
        output = Element("name", att="tone", val=value)
        sub1 = SubElement(output, "sub")
        sub2 = SubElement(output, "sub")
        # Fill in text
        output.text = "L"
        sub1.text = "a"
        sub1.tail = "M"
        sub2.text = "1"
        sub2.tail = "H"
        self.assertEqual(tostring(handle_tones(input)), tostring(output))
        ## Test "lexeme"
        value = "aa˩abb˧bcc˥c".decode(encoding=ENCODING)
        input = Element("name", att="lexeme", val=value)
        # Create output element and sub-elements
        output = Element("name", att="lexeme", val=value)
        sub = SubElement(output, "sub")
        # Fill in text
        output.text = "aa˩abb˧bcc˥".decode(encoding=ENCODING)
        sub.text = "c"
        self.assertEqual(tostring(handle_tones(input)), tostring(output))
        ## Test others
        input = Element("name", att="other", val=value)
        output = Element("name", att="other", val=value)
        self.assertEqual(tostring(handle_tones(input)), tostring(output))

suite = unittest.TestLoader().loadTestsFromTestCase(TestXmlLmfFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
