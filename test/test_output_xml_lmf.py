#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *
from output.xml_lmf import xml_lmf_write, build_sub_elements, add_link, handle_reserved, handle_styles, handle_font, handle_pinyin, handle_caps, handle_tones
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
        sub.attrib["href"] = "lx_id"
        # Fill in text
        sub.text = "lx"
        result = add_link(form, input)
        self.assertEqual(result[0], form)
        self.assertEqual(tostring(result[1]), tostring(output))

    def test_handle_reserved(self):
        pass

    def test_handle_styles(self):
        # fv
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
            self.assertEqual(tostring(handle_styles(input)), tostring(output))
        # fn
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
            self.assertEqual(tostring(handle_styles(input)), tostring(output))
        # all
        value = "bla fs:regional bla ax:i bla fr:regional bla fi:i bla fl:i bla fn:national bla fv:vernacular bla"
        input = Element("name", val=unicode(value))
        # Create output element and sub-elements
        output = Element("name", val=unicode(value))
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "char_fs"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "char_ax"
        sub3 = SubElement(output, "span")
        sub3.attrib["class"] = "char_fr"
        sub4 = SubElement(output, "span")
        sub4.attrib["class"] = "char_fi"
        sub5 = SubElement(output, "span")
        sub5.attrib["class"] = "char_fl"
        sub6 = SubElement(output, "span")
        sub6.attrib["class"] = "national"
        sub7 = SubElement(output, "span")
        sub7.attrib["class"] = "vernacular"
        # Fill in text
        output.text = "bla "
        sub1.text = "regional"
        sub1.tail = " bla "
        sub2.text = "i"
        sub2.tail = " bla "
        sub3.text = "regional"
        sub3.tail = " bla "
        sub4.text = "i"
        sub4.tail = " bla "
        sub5.text = "i"
        sub5.tail = " bla "
        sub6.text = "national"
        sub6.tail = " bla "
        sub7.text = "vernacular"
        sub7.tail = " bla"
        self.assertEqual(tostring(handle_styles(input)), tostring(output))
        # Mwotlap example
        value = u"Les fées (fv:na-tbunbun), les ogres (fv:Wotamat, fv:Wetmat), les serpents-de-mer (fv:ne-m̄e), de nombreuses catégories de démons (fv:na-taqat, fv:nō-kōs, fv:na-mgēl, fv:yebek, fv:na-psisgon, etc.), appartiennent à l'ensemble des fv:na-tmat. On les évoque pour effrayer les enfants turbulents, en les menaçant d'être dévorés (fv:kuy), et les enfants eux-mêmes s'en servent comme d'une insulte entre eux."
        input = Element("name", val=value)
        # Create output element and sub-elements
        output = Element("name", val=value)
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "vernacular"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "vernacular"
        sub3 = SubElement(output, "span")
        sub3.attrib["class"] = "vernacular"
        sub4 = SubElement(output, "span")
        sub4.attrib["class"] = "vernacular"
        sub5 = SubElement(output, "span")
        sub5.attrib["class"] = "vernacular"
        sub6 = SubElement(output, "span")
        sub6.attrib["class"] = "vernacular"
        sub7 = SubElement(output, "span")
        sub7.attrib["class"] = "vernacular"
        sub8 = SubElement(output, "span")
        sub8.attrib["class"] = "vernacular"
        sub9 = SubElement(output, "span")
        sub9.attrib["class"] = "vernacular"
        sub10 = SubElement(output, "span")
        sub10.attrib["class"] = "vernacular"
        sub11 = SubElement(output, "span")
        sub11.attrib["class"] = "vernacular"
        # Fill in text
        output.text = u"Les fées ("
        sub1.text = u"na-tbunbun"
        sub1.tail = u"), les ogres ("
        sub2.text = u"Wotamat"
        sub2.tail = u", "
        sub3.text = u"Wetmat"
        sub3.tail = u"), les serpents-de-mer ("
        sub4.text = u"ne-m̄e"
        sub4.tail = u"), de nombreuses catégories de démons ("
        sub5.text = u"na-taqat"
        sub5.tail = u", "
        sub6.text = u"nō-kōs"
        sub6.tail = u", "
        sub7.text = u"na-mgēl"
        sub7.tail = u", "
        sub8.text = u"yebek"
        sub8.tail = u", "
        sub9.text = u"na-psisgon"
        sub9.tail = u", etc.), appartiennent à l'ensemble des "
        sub10.text = u"na-tmat"
        sub10.tail = u". On les évoque pour effrayer les enfants turbulents, en les menaçant d'être dévorés ("
        sub11.text = u"kuy"
        sub11.tail = u"), et les enfants eux-mêmes s'en servent comme d'une insulte entre eux."
        self.assertEqual(tostring(handle_styles(input)), tostring(output))
        # Another Mwotlap example
        value = u"peindre ‹qqch› de façon minutieuse et appliquée (fl:opp. fv:suw), dessiner des motifs, fl:partic. dans l'art des masques sacrés (fv:na-tmat)"
        input = Element("name", val=value)
        # Create output element and sub-elements
        output = Element("name", val=value)
        sub1 = SubElement(output, "span")
        sub1.attrib["class"] = "char_fl"
        sub2 = SubElement(output, "span")
        sub2.attrib["class"] = "vernacular"
        sub3 = SubElement(output, "span")
        sub3.attrib["class"] = "char_fl"
        sub4 = SubElement(output, "span")
        sub4.attrib["class"] = "vernacular"
        # Fill in text
        output.text = u"peindre ‹qqch› de façon minutieuse et appliquée ("
        sub1.text = u"opp"
        sub1.tail = u". "
        sub2.text = u"suw"
        sub2.tail = u"), dessiner des motifs, "
        sub3.text = u"partic"
        sub3.tail = u". dans l'art des masques sacrés ("
        sub4.text = u"na-tmat"
        sub4.tail = u")"
        self.assertEqual(tostring(handle_styles(input)), tostring(output))

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
