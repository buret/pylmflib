#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import ps_partOfSpeech, mdf_lmf, lmf_mdf, mdf_semanticRelation, pd_grammaticalNumber
from common.range import partOfSpeech_range
from utils.io import ENCODING

## To define languages and fonts
import config

items=lambda lexical_entry: lexical_entry.get_lexeme().replace('[','').replace(']','').replace('~','').replace('-','')

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps = [
      "sub",
      "ptc",
      "pf",
      "intj",
      "adv",
      "préd",
      "expr",
      "loc",
      "dx",
      "int",
      "pp",
      "n.dép",
      "excl",
      "adj",
      "conj",
      "prép",
      "adp",
      "asp",
      "sb",
      "nop",
      "dét",
      "mod",
      "pos",
      "sf",
      "voi",
      "intsf",
      "dir",
      "attr",
      "sop",
      "spp",
      "rel",
      "num",
      "art",
      "np",
      "expr.adj"
]
for item in ps:
    ps_partOfSpeech.update({item : item.decode(ENCODING)})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update(ps_partOfSpeech.values())

pdl = [
       "3sg",
       "3pl",
       "1s",
       "3s",
       "Pl.",
       "Sgl."
]

## Functions to process some MDF fields (input)
def remove_char(value):
    """Function to remove '^' character from MDF fields.
    """
    return value.replace('^','')

def replace_char(value):
    """Function to replace "|{~}" characters by an unbreakable space in MDF fields.
    """
    return value.replace("|{~}", u"\u00A0")

mdf_lmf.update({
    # To ignore
    "wr"    : lambda wr, lexical_entry: lexical_entry.set_homonymNumber(wr),

    "we"    : lambda we, lexical_entry: lexical_entry.set_note(replace_char(remove_char(we)), type="restriction", language=config.xml.French),
    "wn"    : lambda wn, lexical_entry: lexical_entry.set_note(wn, type="restriction", language=config.xml.English),

    # Fonction sémantique (Fr)
    "he"    : lambda he, lexical_entry: lexical_entry.set_note(he, type="semantics", language=config.xml.French),
    # Fonction linguistique (Ang)
    "hn"    : lambda hn, lexical_entry: lexical_entry.set_note(hn, type="semantics", language=config.xml.English),

    "ur"    : lambda ur, lexical_entry: lexical_entry.set_note(ur, type="usage", language=config.xml.French),
    "uv"    : lambda uv, lexical_entry: lexical_entry.set_note(uv, type="usage", language=config.xml.English),

    "nt"    : lambda nt, lexical_entry: lexical_entry.set_note(replace_char(remove_char(nt)), type="general"),

    "lt"    : lambda lt, lexical_entry: lexical_entry.set_literally(remove_char(lt), language=config.xml.French),
    "ll"    : lambda ll, lexical_entry: lexical_entry.set_literally(ll, language=config.xml.English),

    "oe"    : lambda oe, lexical_entry: lexical_entry.set_example_comment(remove_char(oe), language=config.xml.French),
    "on"    : lambda on, lexical_entry: lexical_entry.set_example_comment(on, language=config.xml.English),

    # Etymological language
    "el"    : lambda el, lexical_entry: lexical_entry.set_term_source_language(replace_char(el)),
    "eg"    : lambda eg, lexical_entry: lexical_entry.set_etymology_gloss(replace_char(eg)),
    "et"    : lambda et, lexical_entry: lexical_entry.set_etymology(replace_char(et)),

    # To ignore
    "dc"    : lambda dc, lexical_entry: None,

    "la"    : lambda la, lexical_entry: lexical_entry.set_citation_form(remove_char(la)),

    # Legend (TODO)
    "lg"    : lambda lg, lexical_entry: None,

    "ce"    : lambda ce, lexical_entry: lexical_entry.set_last_related_form(remove_char(ce), language=config.xml.French),
    "cn"    : lambda cn, lexical_entry: lexical_entry.set_last_related_form(cn, language=config.xml.English),
    "cf"    : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(cf), mdf_semanticRelation["cf"]),

    "sy"    : lambda sy, lexical_entry: lexical_entry.create_and_add_related_form(remove_char(sy), mdf_semanticRelation["sy"]),

    # Hidden (TODO later)
    "u"     : lambda u, lexical_entry: None,

    # Hidden example (TODO later)
    "xm"    : lambda xm, lexical_entry: None,
    "rm"    : lambda rm, lexical_entry: None,
    "xa"    : lambda xa, lexical_entry: None,
    "xf"    : lambda xf, lexical_entry: None,

    # (TODO later: add hyperlinks)
    #"mr"    : lambda mr, lexical_entry: None,

    "ue"    : lambda ue, lexical_entry: lexical_entry.set_usage_note(ue, language=config.xml.French),
    "un"    : lambda un, lexical_entry: lexical_entry.set_usage_note(un, language=config.xml.English),

    "ee"    : lambda ee, lexical_entry: lexical_entry.set_encyclopedic_information(replace_char(remove_char(ee)), language=config.xml.French),
    "en"    : lambda en, lexical_entry: lexical_entry.set_encyclopedic_information(remove_char(en), language=config.xml.English),

    "sc"    : lambda sc, lexical_entry: lexical_entry.set_scientific_name(remove_char(sc)),

    "pc"    : lambda pc, lexical_entry: lexical_entry.set_picture(file_name=pc, format="jpg"),

    # TODO
    "tb"    : lambda tb, lexical_entry: None,
    # Table Anglais (n)
    "ta"    : lambda ta, lexical_entry: None,
    # Table large (replace_char)
    "tl"    : lambda tl, lexical_entry: None,
    # Table large anglais (n)
    "tn"    : lambda tn, lexical_entry: None,

    # To ignore
    "br"    : lambda br, lexical_entry: None,

    # Mwesen
    "ms"    : lambda ms, lexical_entry: None,
    # Mota
    "mt"    : lambda mt, lexical_entry: None,

    # morphèmes
    "m"     : lambda m, lexical_entry: None,

    "pl"    : lambda pl, lexical_entry: lexical_entry.set_paradigm(remove_char(pl), grammatical_number=pd_grammaticalNumber["pl"]),

    "a"     : lambda a, lexical_entry: lexical_entry.set_variant_form(remove_char(a), type="phonetics"),
    "va"    : lambda va, lexical_entry: lexical_entry.set_variant_form(remove_char(va), type="phonetics"),
    "ph"    : lambda ph, lexical_entry: lexical_entry.set_phonetic_form(remove_char(ph)),

    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(remove_char(de), language=config.xml.French),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(remove_char(dn), language=config.xml.English),

    "ge"    : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=config.xml.French),
    "gn"    : lambda gn, lexical_entry: lexical_entry.set_gloss(gn, language=config.xml.English),

    "re"    : lambda re, lexical_entry: lexical_entry.set_translation(remove_char(re), language=config.xml.French),
    "rn"    : lambda rn, lexical_entry: lexical_entry.set_translation(rn, language=config.xml.English),

    "xe"    : lambda xe, lexical_entry: lexical_entry.add_example(replace_char(remove_char(xe)), language=config.xml.French),
    "xn"    : lambda xn, lexical_entry: lexical_entry.add_example(replace_char(remove_char(xn)), language=config.xml.English),
    "xv"    : lambda xv, lexical_entry: lexical_entry.create_and_add_example(remove_char(xv), language=config.xml.vernacular),

    "ve"    : lambda ve, lexical_entry: lexical_entry.set_variant_comment(ve, language=config.xml.French),
    "vn"    : lambda vn, lexical_entry: lexical_entry.set_variant_comment(vn, language=config.xml.English),

    # TBD
    "url"   : lambda url, lexical_entry: None,
    "p"     : lambda p, lexical_entry: None,
    "g"     : lambda g, lexical_entry: None,
    "wav"   : lambda wav, lexical_entry: None,
    "xb"    : lambda xb, lexical_entry: None
})

## Functions to process some MDF fields (output)
lmf_mdf.update({})

## Functions to process some LaTeX fields (output)

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
