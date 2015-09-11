#! /usr/bin/env python
# -*- coding: utf-8 -*-

from startup import *
from output.tex import *
from core.lexical_resource import LexicalResource
from core.lexicon import Lexicon
from core.lexical_entry import LexicalEntry
from morphology.lemma import Lemma
from core.sense import Sense
from utils.io import EOL

## Test LaTeX functions

## Fonts to use in LaTeX format (output)
font = dict({
    VERNACULAR  : lambda text: "\\textbf{\ipa{" + text + "}}",
    ENGLISH     : lambda text: text,
    NATIONAL    : lambda text: "\\textit{\zh{" + text + "}}",
    REGIONAL    : lambda text: "\ipa{" + text + "}"
})

# To define languages and fonts
import config
class Xml():
    def __init__(self):
        self.font = font
        self.vernacular = "ver"
        self.English = "eng"
        self.national = "nat"
        self.regional = "reg"
        self.audio_path = "./"

class TestTexFunctions(unittest.TestCase):

    def setUp(self):
        config.xml = Xml()

    def tearDown(self):
        pass

    def test_file_read(self):
        import sys, os
        # Create a header LaTeX file
        utest_path = sys.path[0] + '/'
        tex_filename = utest_path + "header.tex"
        tex_file = open(tex_filename, "w+")
        header = "\documentclass{article}" + EOL + "\\title{test}" + EOL + "\\author{C\'eline Buret}" + EOL
        tex_file.write(header)
        tex_file.close()
        # Read header file and test result
        self.assertEqual(file_read(tex_filename), header)
        # Remove LaTeX file
        os.remove(tex_filename)

    def test_insert_references(self):
        lexical_entry = LexicalEntry()
        lexical_entry.set_spelling_variant("tata")
        # Test transitive verb
        lexical_entry.partOfSpeech = "transitive verb"
        expected_lines = "\\hfill\\break See: \\ref{tata.vt}" + EOL
        expected_lines += "\\ref{tata.vt.eng}" + EOL
        self.assertEqual(expected_lines, insert_references(lexical_entry))
        # Test intransitive verb
        lexical_entry.partOfSpeech = "intransitive verb"
        expected_lines = "\\hfill\\break See: \\ref{tata.vi}" + EOL
        expected_lines += "\\ref{tata.vi.eng}" + EOL
        self.assertEqual(expected_lines, insert_references(lexical_entry))
        # Test reflexive verb
        lexical_entry.partOfSpeech = "reflexive verb"
        expected_lines = "\\hfill\\break See: \\ref{tata.vr}" + EOL
        expected_lines += "\\ref{tata.vr.eng}" + EOL
        self.assertEqual(expected_lines, insert_references(lexical_entry))

    def test_tex_write(self):
        import sys, os
        # Create LMF objects
        lexical_entry = LexicalEntry()
        lexical_entry.lemma = Lemma()
        lexical_entry.partOfSpeech = "toto"
        lexical_entry.status = "draft"
        lexical_entry.lemma.lexeme = "hello"
        lexicon = Lexicon()
        lexicon.add_lexical_entry(lexical_entry)
        lexical_resource = LexicalResource()
        lexical_resource.add_lexicon(lexicon)
        # Write LaTeX file and test result
        utest_path = sys.path[0] + '/'
        tex_filename = utest_path + "output.tex"
        tex_write(lexical_resource, tex_filename)
        tex_file = open(tex_filename, "r")
        begin_lines = [EOL,
            "\\begin{document}" + EOL,
            "\\maketitle" + EOL,
            "\\newpage" + EOL,
            EOL,
            "\\def\\mytextsc{\\bgroup\\obeyspaces\\mytextscaux}" + EOL,
            "\\def\\mytextscaux#1{\\mytextscauxii #1\\relax\\relax\\egroup}" + EOL,
            "\\def\\mytextscauxii#1{%" + EOL,
            "\\ifx\\relax#1\\else \\ifcat#1\\@sptoken{} \\expandafter\\expandafter\\expandafter\\mytextscauxii\\else" + EOL,
            "\\ifnum`#1=\\uccode`#1 {\\normalsize #1}\\else {\\footnotesize \\uppercase{#1}}\\fi \\expandafter\\expandafter\\expandafter\\mytextscauxii\\expandafter\\fi\\fi}" + EOL,
            EOL,
            "\\setlength\\parindent{0cm}" + EOL,
            EOL,
            "\\addmediapath{.}" + EOL,
            "\\addmediapath{./mp3}" + EOL,
            "\\addmediapath{./wav}" + EOL,
            "\\graphicspath{{" + os.path.abspath('.') + "/pylmflib/output/img/}}" + EOL,
            EOL,
            "\\newpage" + EOL,
            "\\begin{multicols}{2}" + EOL,
            EOL
        ]
        end_lines = [
            "\end{multicols}" + EOL,
            "\end{document}" + EOL
        ]
        expected_lines = [
            "\\newpage" + EOL,
            "\\section*{\\centering- \\textbf{\ipa{H}} \\textbf{\ipa{h}} -}" + EOL,
            #"\\pdfbookmark[1]{\ipa{ H h }}{ H h }" + EOL,
            "\\paragraph{\\hspace{-0.5cm} \\textbf{\ipa{hello}}} \\hypertarget{01}{}" + EOL,
            "\markboth{\\textbf{\\ipa{hello}}}{}" + EOL,
            "\\textit{Status:} draft" + EOL,
            "\lhead{\\firstmark}" + EOL,
            "\\rhead{\\botmark}" + EOL,
            EOL
        ]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        # Customize mapping
        my_lmf_tex = dict({
            "Lemma.lexeme" : lambda lexical_entry: "is " + lexical_entry.get_lexeme() + "." + EOL,
            "LexicalEntry.id" : lambda lexical_entry: "The lexical entry " + str(lexical_entry.get_id()) + " ",
            "LexicalEntry.partOfSpeech" : lambda lexical_entry: "Its grammatical category is " + lexical_entry.get_partOfSpeech() + "." + EOL,
            "LexicalEntry.status" : lambda lexical_entry: "Warning: " + lexical_entry.get_status() + " version!" + EOL
        })
        my_order = ["LexicalEntry.id", "Lemma.lexeme", "LexicalEntry.partOfSpeech", "LexicalEntry.status"]
        def lmf2tex(entry, font):
            result = ""
            for attribute in my_order:
                result += my_lmf_tex[attribute](entry)
            return result
        # Write LaTeX file and test result
        tex_write(lexical_resource, tex_filename, None, None, lmf2tex, font)
        tex_file = open(tex_filename, "r")
        expected_lines = [
            "\\newpage" + EOL,
            "\\section*{\\centering- \\textbf{\ipa{H}} \\textbf{\ipa{h}} -}" + EOL,
            #"\\pdfbookmark[1]{\ipa{ H h }}{ H h }" + EOL,
            "The lexical entry 01 is hello." + EOL,
            "Its grammatical category is toto." + EOL,
            "Warning: draft version!" + EOL,
            "\lhead{\\firstmark}" + EOL,
            "\\rhead{\\botmark}" + EOL,
            EOL
            ]
        self.assertListEqual(begin_lines + expected_lines + end_lines, tex_file.readlines())
        tex_file.close()
        del lexical_entry.lemma
        lexical_entry.lemma = None
        del lexical_entry, lexicon
        lexicon = None
        del lexical_resource
        # Remove LaTeX file
        os.remove(tex_filename)

    def test_handle_font(self):
        input = "bla{bla} bla {bla}bla |ipa{bla}"
        output = "bla\ipa{bla} bla \ipa{bla}bla |ipa{bla}"
        self.assertEqual(handle_font(input), output)

    def test_handle_fi(self):
        input = "textfi:this fi:but not this"
        output = "text\\textit{this} \\textit{but} not this"
        self.assertEqual(handle_fi(input), output)
        input = "textfi:this |fi{and this}"
        output = "text\\textit{this} \\textit{and this}"
        self.assertEqual(handle_fi(input), output)

    def test_handle_fn(self):
        input = "textfn:this fn:but not this"
        output = "text\\textit{\zh{this}} \\textit{\zh{but}} not this"
        self.assertEqual(handle_fn(input, font), output)
        input = "textfn:this |fn{and this}"
        output = "text\\textit{\zh{this}} \\textit{\zh{and this}}"
        self.assertEqual(handle_fn(input, font), output)

    def test_handle_fv(self):
        input = "fv:something here and fv:there"
        output = "\\textbf{\ipa{something}} here and \\textbf{\ipa{there}}"
        self.assertEqual(handle_fv(input, font), output)
        input = "|fv{something here} and fv:there"
        output = "\\textbf{\ipa{something here}} and \\textbf{\ipa{there}}"
        self.assertEqual(handle_fv(input, font), output)

    def test_handle_pinyin(self):
        input = "@at at@at at"
        output = "\\textcolor{gray}{at} at\\textcolor{gray}{at} at"
        self.assertEqual(handle_pinyin(input), output)

    def test_handle_caps(self):
        input = u"°trucs et°astuces"
        output = "\\textsc{trucs} et\\textsc{astuces}"
        self.assertEqual(handle_caps(input), output)

    def test_handle_quotes(self):
        input = u"He said: \"hello\" \"hello!\" and that's it."
        output = u"He said: ``hello\" ``hello!\" and that's it."
        self.assertEqual(handle_quotes(input), output)

    def test_format_uid(self):
        entry = LexicalEntry("link_0")
        entry.set_lexeme("link")
        expected = "\\hyperlink{link_01}{\\textbf{\ipa{link}}}"
        self.assertEqual(format_link(entry, font), expected)
        del entry

    def test_format_link(self):
        entry = LexicalEntry("link_0")
        entry.set_lexeme("link")
        expected = "\\hyperlink{link_01}{\\textbf{\ipa{link}}}"
        self.assertEqual(format_link(entry, font), expected)
        entry.set_homonymNumber(2)
        expected = "\\hyperlink{link_02}{\\textbf{\ipa{link}} \\textsubscript{2}}"
        self.assertEqual(format_link(entry, font), expected)
        del entry

    def test_format_lexeme(self):
        entry = LexicalEntry()
        entry.set_lexeme("hello")
        expected = "\\paragraph{\\hspace{-0.5cm} \\textbf{\ipa{hello}}} \\hypertarget{01}{}\n\markboth{\\textbf{\ipa{hello}}}{}\n"
        self.assertEqual(format_lexeme(entry, font), expected)
        del entry

    def test_format_audio(self):
        entry = LexicalEntry()
        entry.set_audio(file_name="./test/input.wav")
        expected = "\includemedia[\n" \
            "\taddresource=./test/input.mp3,\n" \
            "\tflashvars={\n" \
            "\t\tsource=./test/input.mp3\n" \
            "\t\t&autoPlay=true\n" \
            "\t\t&autoRewind=true\n" \
            "\t\t&loop=false\n" \
            "\t\t&hideBar=true\n" \
            "\t\t&volume=1.0\n" \
            "\t\t&balance=0.0\n" \
            "}]{\includegraphics[scale=0.5]{sound.jpg}}{APlayer.swf} \\hspace{0.1cm}\n"
        self.assertEqual(format_audio(entry, font), expected)
        del entry

    def test_format_part_of_speech(self):
        entry = LexicalEntry()
        entry.set_lexeme("action")
        entry.set_partOfSpeech("verb")
        expected = "\\textit{v}. "
        self.assertEqual(format_part_of_speech(entry, font), expected)
        del entry

    def test_format_definitions(self):
        entry = LexicalEntry()
        entry.set_definition("def_ver", language="ver")
        entry.set_definition("def_nat", language="nat")
        entry.set_definition("def_eng", language="eng")
        entry.set_gloss("gloss_ver", language="ver")
        entry.set_gloss("gloss_nat", language="nat")
        entry.set_gloss("gloss_eng", language="eng")
        entry.set_gloss("gloss_reg", language="reg")
        entry.set_translation("trans_ver", language="ver")
        entry.set_translation("trans_nat", language="nat")
        entry.set_translation("trans_eng", language="eng")
        entry.set_translation("trans_reg", language="reg")
        # vernacular
        expected = "\\textbf{\ipa{def_ver}}. trans_ver. "
        # English
        expected += "def_eng. trans_eng. "
        # national
        expected += "\\textit{\zh{def_nat}}. \\textit{\zh{trans_nat}}. "
        # regional
        expected += "\\textit{[Regnl: \ipa{gloss_reg}]}. \\textbf{rr:}\\textit{[Regnl: trans_reg]}. "
        self.assertEqual(format_definitions(entry.get_senses()[0], font), expected)
        del entry

    def test_format_lt(self):
        sense = Sense()
        expected = ""
        self.assertEqual(format_lt(sense, font), expected)
        del sense

    def test_format_sc(self):
        sense = Sense()
        expected = ""
        self.assertEqual(format_sc(sense, font), expected)
        del sense

    def test_format_rf(self):
        sense = Sense()
        expected = ""
        self.assertEqual(format_rf(sense, font), expected)
        del sense

    def test_format_examples(self):
        entry = LexicalEntry()
        entry.add_example("ex_ver", language="ver")
        entry.add_example("ex_eng", language="eng")
        entry.add_example("ex_nat", language="nat")
        entry.add_example("ex_reg", language="reg")
        expected = "\\begin{exe}\n\\sn \\textbf{\ipa{ex_ver}}\n\\trans ex_eng\n\\trans \\textit{\\textit{\zh{ex_nat}}}\n\\trans \\textit{[\ipa{ex_reg}]}\n\\end{exe}\n"
        self.assertEqual(format_examples(entry.get_senses()[0], font), expected)
        del entry

    def test_format_usage_notes(self):
        entry = LexicalEntry()
        entry.set_usage_note("use_ver", language="ver")
        entry.set_usage_note("use_eng", language="eng")
        entry.set_usage_note("use_nat", language="nat")
        entry.set_usage_note("use_reg", language="reg")
        expected = "\\textit{VerUsage:} \\textbf{\ipa{use_ver}} \\textit{Usage:} use_eng \\textit{\\textit{\zh{use_nat}}} \\textit{[\ipa{use_reg}]} "
        self.assertEqual(format_usage_notes(entry.get_senses()[0], font), expected)
        del entry

    def test_format_encyclopedic_informations(self):
        entry = LexicalEntry()
        entry.set_encyclopedic_information("info_ver", language="ver")
        entry.set_encyclopedic_information("info_eng", language="eng")
        entry.set_encyclopedic_information("info_nat", language="nat")
        entry.set_encyclopedic_information("info_reg", language="reg")
        expected = "\\textbf{\ipa{info_ver}} info_eng \\textit{\zh{info_nat}} \\textit{[\ipa{info_reg}]} "
        self.assertEqual(format_encyclopedic_informations(entry.get_senses()[0], font), expected)
        del entry

    def test_format_restrictions(self):
        entry = LexicalEntry()
        entry.set_restriction("strict_ver", language="ver")
        entry.set_restriction("strict_eng", language="eng")
        entry.set_restriction("strict_nat", language="nat")
        entry.set_restriction("strict_reg", language="reg")
        expected = "\\textit{VerRestrict:} \\textbf{\ipa{strict_ver}} \\textit{Restrict:} strict_eng \\textit{\\textit{\zh{strict_nat}}} \\textit{[\ipa{strict_reg}]} "
        self.assertEqual(format_restrictions(entry.get_senses()[0], font), expected)
        del entry

    def test_format_lexical_functions(self):
        entry = LexicalEntry()
        expected = ""
        self.assertEqual(format_lexical_functions(entry, font), expected)
        del entry

    def test_format_related_forms(self):
        entry = LexicalEntry()
        entry.create_and_add_related_form("syn", mdf_semanticRelation["sy"])
        entry.create_and_add_related_form("ant", mdf_semanticRelation["an"])
        entry.set_morphology("morph")
        entry.create_and_add_related_form("see", mdf_semanticRelation["cf"])
        expected = "\\textit{Syn:} \\textbf{\ipa{syn}}. \\textit{Ant:} \\textbf{\ipa{ant}}. \\textit{Morph:} \\textbf{\ipa{morph}}. \\textit{See:} \\textbf{\ipa{see}} "
        self.assertEqual(format_related_forms(entry, font), expected)
        del entry

    def test_format_variant_forms(self):
        entry = LexicalEntry()
        entry.set_variant_form("var_ver")
        entry.set_variant_comment("com_ver", language="ver")
        entry.set_variant_comment("com_eng", language="eng")
        entry.set_variant_comment("com_nat", language="nat")
        entry.set_variant_comment("com_reg", language="reg")
        expected = "\\textit{Variant:} \\textbf{\ipa{var_ver}} (com_eng) (\\textit{\zh{com_nat}}) (\ipa{com_reg}) "
        self.assertEqual(format_variant_forms(entry, font), expected)
        del entry

    def test_format_borrowed_word(self):
        entry = LexicalEntry()
        entry.set_borrowed_word("English")
        entry.set_written_form("wave")
        expected = "\\textit{From:} English wave. "
        self.assertEqual(format_borrowed_word(entry, font), expected)
        del entry

    def test_format_etymology(self):
        entry = LexicalEntry()
        entry.set_etymology("etym")
        entry.set_etymology_gloss("ETYM")
        expected = u"\\textit{Etym:} \\textbf{etym} \u2018ETYM\u2019. "
        self.assertEqual(format_etymology(entry, font), expected)
        del entry

    def test_format_paradigms(self):
        entry = LexicalEntry()
        entry.set_paradigm("pd")
        entry.set_paradigm("sg", grammatical_number=pd_grammaticalNumber["sg"])
        entry.set_paradigm("pl", grammatical_number=pd_grammaticalNumber["pl"])
        entry.set_paradigm("a1s", person=pd_person[1], grammatical_number=pd_grammaticalNumber['s'])
        entry.set_paradigm("a2s", person=pd_person[2], grammatical_number=pd_grammaticalNumber['s'])
        entry.set_paradigm("a3s", person=pd_person[3], grammatical_number=pd_grammaticalNumber['s'])
        entry.set_paradigm("a4s", anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s'])
        entry.set_paradigm("a1d", person=pd_person[1], grammatical_number=pd_grammaticalNumber['d'])
        entry.set_paradigm("a2d", person=pd_person[2], grammatical_number=pd_grammaticalNumber['d'])
        entry.set_paradigm("a3d", person=pd_person[3], grammatical_number=pd_grammaticalNumber['d'])
        entry.set_paradigm("a4d", anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d'])
        entry.set_paradigm("a1p", person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'])
        entry.set_paradigm("a1e", person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e'])
        entry.set_paradigm("a1i", person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i'])
        entry.set_paradigm("a2p", person=pd_person[2], grammatical_number=pd_grammaticalNumber['p'])
        entry.set_paradigm("a3p", person=pd_person[3], grammatical_number=pd_grammaticalNumber['p'])
        entry.set_paradigm("a4p", anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p'])
        expected = "\\textit{Prdm:} \\textbf{pd}. "
        expected += "\\textit{Sg:} \\textbf{sg} "
        expected += "\\textit{Pl:} \\textbf{pl} "
        expected += "\\textit{1s:} \\textbf{a1s} "
        expected += "\\textit{2s:} \\textbf{a2s} "
        expected += "\\textit{3s:} \\textbf{a3s} "
        expected += "\\textit{3sn:} \\textbf{a4s} "
        expected += "\\textit{1d:} \\textbf{a1d} "
        expected += "\\textit{2d:} \\textbf{a2d} "
        expected += "\\textit{3d:} \\textbf{a3d} "
        expected += "\\textit{3dn:} \\textbf{a4d} "
        expected += "\\textit{1p:} \\textbf{a1p} "
        expected += "\\textit{1px:} \\textbf{a1e} "
        expected += "\\textit{1pi:} \\textbf{a1i} "
        expected += "\\textit{2p:} \\textbf{a2p} "
        expected += "\\textit{3p:} \\textbf{a3p} "
        expected += "\\textit{3pn:} \\textbf{a4p} "
        self.assertEqual(format_paradigms(entry, font), expected)
        del entry

    def test_format_table(self):
        entry = LexicalEntry()
        expected = ""
        self.assertEqual(format_table(entry, font), expected)
        del entry

    def test_format_semantic_domains(self):
        entry = LexicalEntry()
        entry.set_semantic_domain("semantic")
        entry.set_semantic_domain("domain")
        expected = "\\textit{SD:} semantic. "
        expected += "\\textit{SD:} domain. "
        self.assertEqual(format_semantic_domains(entry, font), expected)
        del entry

    def test_format_bibliography(self):
        entry = LexicalEntry()
        entry.set_bibliography("biblio")
        expected = "\\textit{Read:} biblio. "
        self.assertEqual(format_bibliography(entry, font), expected)
        del entry

    def test_format_picture(self):
        entry = LexicalEntry()
        expected = ""
        self.assertEqual(format_picture(entry, font), expected)
        del entry

    def test_format_notes(self):
        entry = LexicalEntry()
        entry.set_note("general1", type="general")
        entry.set_note("general2", type="general")
        entry.set_note("phonology", type="phonology")
        entry.set_note("grammar", type="grammar")
        entry.set_note("discourse", type="discourse")
        entry.set_note("anthropology", type="anthropology")
        entry.set_note("sociolinguistics", type="sociolinguistics")
        entry.set_note("question", type="question")
        expected = "\\textit{[Note: general1]} "
        expected += "\\textit{[Note: general2]} "
        expected += "\\textit{[Phon: phonology]} "
        expected += "\\textit{[Gram: grammar]} "
        expected += "\\textit{[Disc: discourse]} "
        expected += "\\textit{[Ant: anthropology]} "
        expected += "\\textit{[Socio: sociolinguistics]} "
        expected += "\\textit{[Ques: question]} "
        self.assertEqual(format_notes(entry, font), expected)
        del entry

    def test_format_source(self):
        entry = LexicalEntry()
        expected = ""
        self.assertEqual(format_source(entry, font), expected)
        del entry

    def test_format_status(self):
        entry = LexicalEntry()
        entry.set_status("status")
        expected = "\\textit{Status:} status"
        self.assertEqual(format_status(entry, font), expected)
        del entry

    def test_format_date(self):
        entry = LexicalEntry()
        expected = ""
        self.assertEqual(format_date(entry, font), expected)
        del entry

suite = unittest.TestLoader().loadTestsFromTestCase(TestTexFunctions)

## Run test suite

testResult = unittest.TextTestRunner(verbosity=2).run(suite)
