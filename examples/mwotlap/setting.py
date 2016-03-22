#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import ps_partOfSpeech, mdf_lmf, lmf_mdf
from common.range import partOfSpeech_range
from utils.io import ENCODING

## To define languages and fonts
import config

items=lambda lexical_entry: lexical_entry.get_lexeme()

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
mdf_lmf.update({
    "wr"    : lambda wr, lexical_entry: None,
    "we"    : lambda we, lexical_entry: lexical_entry.set_note(he, type="restriction", language=config.xml.French),
    "wn"    : lambda wn, lexical_entry: lexical_entry.set_note(he, type="restriction", language=config.xml.English),
    # Fonction sémantique (Fr)
    "he"    : lambda he, lexical_entry: lexical_entry.set_note(he, type="semantics", language=config.xml.French),
    # Fonction linguistique (Ang)
    "hn"    : lambda hn, lexical_entry: lexical_entry.set_note(hn, type="semantics", language=config.xml.English),
    "ur"    : lambda ur, lexical_entry: lexical_entry.set_note(ur, type="usage", language=config.xml.French),
    "uv"    : lambda uv, lexical_entry: lexical_entry.set_note(uv, type="usage", language=config.xml.English),
    "lt"    : lambda lt, lexical_entry: None,#set(config.xml.French), # TODO in pylmflib
    "ll"    : lambda ll, lexical_entry: None,#set(config.xml.English),
    "oe"    : lambda oe, lexical_entry: None,
    "on"    : lambda on, lexical_entry: None,
    "ur"    : lambda ur, lexical_entry: None,
#    "se"    : lambda se, lexical_entry: None,
    # Etymological language
    "el"    : lambda ol, lexical_entry: None,
    "dc"    : lambda dc, lexical_entry: None,
    "la"    : lambda la, lexical_entry: lexical_entry.set_citation_form(la),
    # Legend
    "lg"    : lambda lg, lexical_entry: None,
    "ce"    : lambda ce, lexical_entry: None,
    "u"     : lambda u, lexical_entry: None,
    "xm"    : lambda xm, lexical_entry: None,
    "rm"    : lambda rm, lexical_entry: None,
    "xa"    : lambda xa, lexical_entry: None,
    "xf"    : lambda xf, lexical_entry: None,
    "mr"    : lambda mr, lexical_entry: None,
    "ue"    : lambda ue, lexical_entry: None,
    "un"    : lambda un, lexical_entry: None,
    "tb"    : lambda tb, lexical_entry: None,
    # Table Anglais (n)
    "ta"    : lambda ta, lexical_entry: None,
    # Table large
    "tl"    : lambda tl, lexical_entry: None,
    # Table large anglais (n)
    "tn"    : lambda tn, lexical_entry: None,
    "br"    : lambda br, lexical_entry: None,
    "url"   : lambda url, lexical_entry: None,
    # Mwesen
    "ms"    : lambda ms, lexical_entry: None,
    # Mota
    "mt"    : lambda mt, lexical_entry: None,
    # morphèmes
    "m"     : lambda m, lexical_entry: None,
    "p"     : lambda p, lexical_entry: None,
    "g"     : lambda g, lexical_entry: None,
    "wav"   : lambda wav, lexical_entry: None,
    "a"     : lambda a, lexical_entry: lexical_entry.set_variant_form(a, type="phonetics"),
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(de, language=config.xml.French),
    "dn"    : lambda dn, lexical_entry: lexical_entry.set_definition(dn, language=config.xml.English),
    "ge"    : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=config.xml.French),
    "xe"    : lambda xe, lexical_entry: lexical_entry.add_example(xe, language=config.xml.French),
    "xn"    : lambda xn, lexical_entry: lexical_entry.add_example(xn, language=config.xml.English),
    "xb"    : lambda xb, lexical_entry: None
})

## Functions to process some MDF fields (output)
lmf_mdf.update({})

## Functions to process some LaTeX fields (output)

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
