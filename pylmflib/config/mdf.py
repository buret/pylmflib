#! /usr/bin/env python

"""! @package config
"""

## To define languages
import config

## Functions to process some MDF fields (input)
def set_bw(bw, lexical_entry):
    # Retrieve if there is a written form following the borrowed word (e.g. "Portuguese fi:meirinho")
    borrowed_word = bw.split()[0]
    written_form = ""
    for item in bw.split()[1:]:
        written_form += item
    # Set borrowed word, and written form if any
    lexical_entry.set_borrowed_word(borrowed_word)
    if len(written_form) > 0:
        lexical_entry.set_written_form(written_form)

## Mapping between MDF markers and LMF representation (input)
mdf_lmf = dict({
    "lx" : lambda lx, lexical_entry: lexical_entry.set_lexeme(lx),
    "hm" : lambda hm, lexical_entry: lexical_entry.set_homonymNumber(hm),
    "lc" : lambda lc, lexical_entry: lexical_entry.set_citation_form(lc), # or lexical_entry.set_contextual_variation(lc)
    "ph" : lambda ph, lexical_entry: lexical_entry.set_phonetic_form(ph), # or lexical_entry.set_transliteration(ph)
    "se" : lambda se, lexical_entry: lexical_entry.create_and_add_related_form(se, mdf_semanticRelation["se"]),
    "ps" : lambda ps, lexical_entry: lexical_entry.set_partOfSpeech(ps),
    "pn" : lambda pn, lexical_entry: None,
    "sn" : lambda sn, lexical_entry: lexical_entry.create_and_add_sense(sn),
    "gv" : lambda gv, lexical_entry: lexical_entry.set_gloss(gv, language=config.xml.vernacular),
    "dv" : lambda dv, lexical_entry: lexical_entry.set_definition(dv, language=config.xml.vernacular),
    "ge" : lambda ge, lexical_entry: lexical_entry.set_gloss(ge, language=config.xml.English),
    "re" : lambda re, lexical_entry: lexical_entry.set_translation(re, language=config.xml.English),
    "we" : lambda we, lexical_entry: None,
    "de" : lambda de, lexical_entry: lexical_entry.set_definition(de, language=config.xml.English),
    "gn" : lambda gn, lexical_entry: lexical_entry.set_gloss(gn, language=config.xml.national),
    "rn" : lambda rn, lexical_entry: lexical_entry.set_translation(rn, language=config.xml.national),
    "wn" : lambda wn, lexical_entry: None,
    "dn" : lambda dn, lexical_entry: lexical_entry.set_definition(dn, language=config.xml.national),
    "gr" : lambda gr, lexical_entry: lexical_entry.set_gloss(gr, language=config.xml.regional),
    "rr" : lambda rr, lexical_entry: lexical_entry.set_translation(rr, language=config.xml.regional),
    "wr" : lambda wr, lexical_entry: None,
    "dr" : lambda dr, lexical_entry: lexical_entry.set_definition(dr, language=config.xml.regional),
    "lt" : lambda lt, lexical_entry: lexical_entry.set_literally(lt, language=config.xml.English),
    "sc" : lambda sc, lexical_entry: lexical_entry.set_scientific_name(sc),
    "rf" : lambda rf, lexical_entry: lexical_entry.create_example(rf),
    "xv" : lambda xv, lexical_entry: lexical_entry.create_and_add_example(xv, language=config.xml.vernacular),
    "xe" : lambda xe, lexical_entry: lexical_entry.add_example(xe, language=config.xml.English),
    "xn" : lambda xn, lexical_entry: lexical_entry.add_example(xn, language=config.xml.national),
    "xr" : lambda xr, lexical_entry: lexical_entry.add_example(xr, language=config.xml.regional),
    "xg" : lambda xg, lexical_entry: None,
    "uv" : lambda uv, lexical_entry: lexical_entry.set_usage_note(uv, language=config.xml.vernacular),
    "ue" : lambda ue, lexical_entry: lexical_entry.set_usage_note(ue, language=config.xml.English),
    "un" : lambda un, lexical_entry: lexical_entry.set_usage_note(un, language=config.xml.national),
    "ur" : lambda ur, lexical_entry: lexical_entry.set_usage_note(ur, language=config.xml.regional),
    "ev" : lambda ev, lexical_entry: lexical_entry.set_encyclopedic_information(ev, language=config.xml.vernacular),
    "ee" : lambda ee, lexical_entry: lexical_entry.set_encyclopedic_information(ee, language=config.xml.English),
    "en" : lambda en, lexical_entry: lexical_entry.set_encyclopedic_information(en, language=config.xml.national),
    "er" : lambda er, lexical_entry: lexical_entry.set_encyclopedic_information(er, language=config.xml.regional),
    "ov" : lambda ov, lexical_entry: lexical_entry.set_restriction(ov, language=config.xml.vernacular),
    "oe" : lambda oe, lexical_entry: lexical_entry.set_restriction(oe, language=config.xml.English),
    "on" : lambda on, lexical_entry: lexical_entry.set_restriction(on, language=config.xml.national),
    "or" : lambda OR, lexical_entry: lexical_entry.set_restriction(OR, language=config.xml.regional), # 'or' is a keyword in Python
    "lf" : lambda lf, lexical_entry: None,
    "lv" : lambda lv, lexical_entry: None,
    "le" : lambda le, lexical_entry: None,
    "ln" : lambda ln, lexical_entry: None,
    "lr" : lambda lr, lexical_entry: None,
    "sy" : lambda sy, lexical_entry: lexical_entry.create_and_add_related_form(sy, mdf_semanticRelation["sy"]),
    "an" : lambda an, lexical_entry: lexical_entry.create_and_add_related_form(an, mdf_semanticRelation["an"]),
    "mr" : lambda mr, lexical_entry: lexical_entry.set_morphology(mr),
    "cf" : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(cf, mdf_semanticRelation["cf"]),
    "ce" : lambda ce, lexical_entry: lexical_entry.set_last_related_form(ce, language=config.xml.English),
    "cn" : lambda cn, lexical_entry: lexical_entry.set_last_related_form(cn, language=config.xml.national),
    "cr" : lambda cr, lexical_entry: None,
    "mn" : lambda mn, lexical_entry: lexical_entry.create_and_add_related_form(mn, mdf_semanticRelation["mn"]),
    "va" : lambda va, lexical_entry: lexical_entry.set_variant_form(va, type="phonetics"), # or lexical_entry.set_geographical_variant(va)
    "ve" : lambda ve, lexical_entry: lexical_entry.set_variant_comment(ve, language=config.xml.English), # or lexical_entry.set_dialect(ve)
    "vn" : lambda vn, lexical_entry: lexical_entry.set_variant_comment(vn, language=config.xml.national),
    "vr" : lambda vr, lexical_entry: lexical_entry.set_variant_comment(vr, language=config.xml.regional),
    "bw" : lambda bw, lexical_entry: set_bw(bw, lexical_entry),
    "et" : lambda et, lexical_entry: lexical_entry.set_etymology(et),
    "eg" : lambda eg, lexical_entry: lexical_entry.set_etymology_gloss(eg),
    "es" : lambda es, lexical_entry: lexical_entry.set_etymology_source(es),
    "ec" : lambda ec, lexical_entry: lexical_entry.set_etymology_comment(ec),
    "pd" : lambda pd, lexical_entry: lexical_entry.set_paradigm(pd),
    "pdl": lambda pdl, lexical_entry: lexical_entry.set_paradigm_label(pdl),
    "pdv": lambda pdv, lexical_entry: lexical_entry.set_paradigm_form(pdv, language=config.xml.vernacular),
    "pde": lambda pde, lexical_entry: lexical_entry.set_paradigm_form(pde, language=config.xml.English),
    "pdn": lambda pdn, lexical_entry: lexical_entry.set_paradigm_form(pdn, language=config.xml.national),
    "pdr": lambda pdr, lexical_entry: lexical_entry.set_paradigm_form(pdr, language=config.xml.regional),
    "sg" : lambda sg, lexical_entry: lexical_entry.set_paradigm(sg, grammatical_number=pd_grammaticalNumber["sg"]),
    "pl" : lambda pl, lexical_entry: lexical_entry.set_paradigm(pl, grammatical_number=pd_grammaticalNumber["pl"]),
    "rd" : lambda rd, lexical_entry: None,
    "1s" : lambda a1s, lexical_entry: lexical_entry.set_paradigm(a1s, person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']),
    "2s" : lambda a2s, lexical_entry: lexical_entry.set_paradigm(a2s, person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']),
    "3s" : lambda a3s, lexical_entry: lexical_entry.set_paradigm(a3s, person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']),
    "4s" : lambda a4s, lexical_entry: lexical_entry.set_paradigm(a4s, anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']),
    "1d" : lambda a1d, lexical_entry: lexical_entry.set_paradigm(a1d, person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']),
    "2d" : lambda a2d, lexical_entry: lexical_entry.set_paradigm(a2d, person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']),
    "3d" : lambda a3d, lexical_entry: lexical_entry.set_paradigm(a3d, person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']),
    "4d" : lambda a4d, lexical_entry: lexical_entry.set_paradigm(a4d, anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']),
    "1p" : lambda a1p, lexical_entry: lexical_entry.set_paradigm(a1p, person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']),
    "1e" : lambda a1e, lexical_entry: lexical_entry.set_paradigm(a1e, person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']),
    "1i" : lambda a1i, lexical_entry: lexical_entry.set_paradigm(a1i, person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']),
    "2p" : lambda a2p, lexical_entry: lexical_entry.set_paradigm(a2p, person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']),
    "3p" : lambda a3p, lexical_entry: lexical_entry.set_paradigm(a3p, person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']),
    "4p" : lambda a4p, lexical_entry: lexical_entry.set_paradigm(a4p, anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']),
    "tb" : lambda tb, lexical_entry: None,
    "sd" : lambda sd, lexical_entry: lexical_entry.set_semantic_domain(sd),
    "is" : lambda IS, lexical_entry: lexical_entry.set_semantic_domain(IS), # 'is' is a keyword in Python
    "th" : lambda th, lexical_entry: lexical_entry.set_semantic_domain(th),
    "bb" : lambda bb, lexical_entry: lexical_entry.set_bibliography(bb),
    "pc" : lambda pc, lexical_entry: lexical_entry.set_picture(file_name=pc),
    "nt" : lambda nt, lexical_entry: lexical_entry.set_note(nt, type="general"),
    "np" : lambda np, lexical_entry: lexical_entry.set_note(np, type="phonology"),
    "ng" : lambda ng, lexical_entry: lexical_entry.set_note(ng, type="grammar"),
    "nd" : lambda nd, lexical_entry: lexical_entry.set_note(nd, type="discourse"),
    "na" : lambda na, lexical_entry: lexical_entry.set_note(na, type="anthropology"),
    "ns" : lambda ns, lexical_entry: lexical_entry.set_note(ns, type="sociolinguistics"),
    "nq" : lambda nq, lexical_entry: lexical_entry.set_note(nq, type="question"),
    "so" : lambda so, lexical_entry: None,
    "st" : lambda st, lexical_entry: lexical_entry.set_status(st),
    "dt" : lambda dt, lexical_entry: lexical_entry.set_date(dt)
})

## Order in which MDF markers must be written (output)
# This is the standard order defined in Appendix B of "Making Dictionaries. A guide to lexicography and the Multi-Dictionary Formatter",
# Software version 1.0, David F. Coward, Charles E. Grimes, SIL International, Waxhaw, North Carolina, 2000
mdf_order = [
    "lx", # lexeme
    "hm", # homonym number
    "lc", # lexical citation
    "ph", # phonetic
    "se", # subentry
    "ps", # part of speech
    "pn", # part of speech-national language
    [
        "sn", # sense number
        "gv", # gloss-vernacular
        "dv", # definition-vernacular
        "ge", # gloss-English
        "re", # reverse-English
        "we", # word level gloss-English
        "de", # definition-English
        "gn", # gloss-national language
        "rn", # reverse-national language
        "wn", # word level gloss-national language
        "dn", # definition-national language
        "gr", # gloss-regional lang. (with \gn)
        "rr", # reverse-regional lang. (with \rn)
        "wr", # word-level gloss-regional (with \wn)
        "dr", # definition-regional lang. (with \dn)
        "lt", # literal meaning
        "sc", # scientific name
        [
            "rf", # reference for example
            "xv", # example sentence-vernacular
            "xe", # example sentence-English
            "xn", # example sentence-national language
            "xr", # example sent.-regional (with \xn)
            "xg"  # example sentence-interlinear gloss
        ],
        "uv", # usage-vernacular
        "ue", # usage-English
        "un", # usage-national language
        "ur", # usage-regional (combines with \un)
        "ev", # encyclopedic-vernacular
        "ee", # encyclopedic-English
        "en", # encyclopedic-national language
        "er", # encyclopedic-regional language
        "ov", # only (restrictions)-vernacular
        "oe", # only (restrictions)-English
        "on", # only (restrictions)-national language
        "or"  # only (restrictions)-regional (with \on)
    ],
    "lf", # lexical function label-English
    "lv", # lexical function value-vernacular language
    "le", # lexical function value-English
    "ln", # lexical function value-national language
    "lr", # lexical function value-regional language
    "sy", # synonym
    "an", # antonym
    "mr", # morphemic representation
    "cf", # cross-reference
    "ce", # cross-reference-English gloss
    "cn", # cross-reference-national gloss
    "cr", # cross-reference-regional gloss
    "mn", # main entry form
    [
        "va", # variant form
        "ve", # variant comment-English
        "vn", # variant comment-national language
        "vr"  # variant comment-regional language
    ],
    "bw", # borrowed word
    "et", # etymology
    "eg", # etymology-gloss
    "es", # etymology-source
    "ec", # etymology-comment
    "pd", # paradigm
    [
        "pdl", # paradigm label-English
        "pdv", # paradigm form-vernacular language
        "pde", # paradigm form-English gloss
        "pdn", # paradigm form-national gloss
        "pdr"  # paradigm form-regional gloss
    ],
    "sg", # singular form
    "pl", # plural form
    "rd", # reduplication
    "1s", # 1st person singular
    "2s", # 2nd person singular
    "3s", # 3rd person singular
    "4s", # singular non-human/non-animate
    "1d", # 1st person dual
    "2d", # 2nd person dual
    "3d", # 3rd person dual
    "4d", # dual non-human/non-animate
    "1p", # 1st person plural-general
    "1e", # 1st person plural-exclusive
    "1i", # 1st person plural-inclusive
    "2p", # 2nd person plural
    "3p", # 3rd person plural
    "4p", # plural non-human/non-animate
    "tb", # table
    "sd", # semantic domain
    "is", # index of semantics
    "th", # thesaurus
    "bb", # bibliographic reference
    "pc", # picture
    "nt", # notes-general
    "np", # notes-phonology
    "ng", # notes-grammar
    "nd", # notes-discourse
    "na", # notes-anthropology
    "ns", # notes-sociolinguistics
    "nq", # notes-questions
    "so", # source
    "st", # status
    "dt"  # datestamp
]
# bundles of related fields: ge, re, de, xv, ue, oe, ee
# bundles related to other entries: lf, nt, pd, et, cf, va

## Functions to process some MDF fields (output)
def get_bw(lexical_entry):
    bw = lexical_entry.get_borrowed_word()
    if lexical_entry.get_written_form() is not None:
        bw += " " + lexical_entry.get_written_form()
    return bw

## Mapping between LMF representation and MDF markers (output)
lmf_mdf = dict({
    "lx" : lambda lexical_entry: lexical_entry.get_lexeme(),
    "hm" : lambda lexical_entry: lexical_entry.get_homonymNumber(),
    "lc" : lambda lexical_entry: lexical_entry.get_citation_forms(), # or lexical_entry.get_contextual_variations()
    "ph" : lambda lexical_entry: lexical_entry.get_phonetic_forms(), # or lexical_entry.get_transliterations()
    "se" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["se"]),
    "ps" : lambda lexical_entry: lexical_entry.get_partOfSpeech(),
    "pn" : lambda lexical_entry: None,
    "snGroup" : lambda lexical_entry: lexical_entry.get_senses(),
    "sn" : lambda sense: sense.get_senseNumber(),
    "gv" : lambda sense: sense.find_glosses(config.xml.vernacular),
    "dv" : lambda sense: sense.find_definitions(config.xml.vernacular),
    "ge" : lambda sense: sense.find_glosses(config.xml.English),
    "re" : lambda sense: sense.get_translations(config.xml.English),
    "we" : lambda sense: None,
    "de" : lambda sense: sense.find_definitions(config.xml.English),
    "gn" : lambda sense: sense.find_glosses(config.xml.national),
    "rn" : lambda sense: sense.get_translations(config.xml.national),
    "wn" : lambda sense: None,
    "dn" : lambda sense: sense.find_definitions(config.xml.national),
    "gr" : lambda sense: sense.find_glosses(config.xml.regional),
    "rr" : lambda sense: sense.get_translations(config.xml.regional),
    "wr" : lambda sense: None,
    "dr" : lambda sense: sense.find_definitions(config.xml.regional),
    "lt" : lambda sense: None,
    "sc" : lambda sense: sense.get_scientific_name(),
    "rfGroup" : lambda sense: sense.get_contexts(),
    "rf" : lambda context: None,
    "xv" : lambda context: context.find_written_forms(config.xml.vernacular),
    "xe" : lambda context: context.find_written_forms(config.xml.English),
    "xn" : lambda context: context.find_written_forms(config.xml.national),
    "xr" : lambda context: context.find_written_forms(config.xml.regional),
    "xg" : lambda sense: None,
    "uv" : lambda sense: sense.find_usage_notes(language=config.xml.vernacular),
    "ue" : lambda sense: sense.find_usage_notes(language=config.xml.English),
    "un" : lambda sense: sense.find_usage_notes(language=config.xml.national),
    "ur" : lambda sense: sense.find_usage_notes(language=config.xml.regional),
    "ev" : lambda sense: sense.find_encyclopedic_informations(language=config.xml.vernacular),
    "ee" : lambda sense: sense.find_encyclopedic_informations(language=config.xml.English),
    "en" : lambda sense: sense.find_encyclopedic_informations(language=config.xml.national),
    "er" : lambda sense: sense.find_encyclopedic_informations(language=config.xml.regional),
    "ov" : lambda sense: sense.find_restrictions(language=config.xml.vernacular),
    "oe" : lambda sense: sense.find_restrictions(language=config.xml.English),
    "on" : lambda sense: sense.find_restrictions(language=config.xml.national),
    "or" : lambda sense: sense.find_restrictions(language=config.xml.regional),
    "lf" : lambda lexical_entry: None,
    "lv" : lambda lexical_entry: None,
    "le" : lambda lexical_entry: None,
    "ln" : lambda lexical_entry: None,
    "lr" : lambda lexical_entry: None,
    "sy" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["sy"]),
    "an" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["an"]),
    "mr" : lambda lexical_entry: lexical_entry.get_morphologies(),
    "cf" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["cf"]),
    "ce" : lambda lexical_entry: None,
    "cn" : lambda lexical_entry: None,
    "cr" : lambda lexical_entry: None,
    "mn" : lambda lexical_entry: lexical_entry.find_related_forms(mdf_semanticRelation["mn"]),
    "vaGroup" : lambda lexical_entry: lexical_entry.get_form_representations(),
    "va" : lambda form_representation: form_representation.get_variantForm(), # or form_representation.get_geographicalVariant() or form_representation.get_spellingVariant()
    "ve" : lambda form_representation: form_representation.get_comment(config.xml.English), # or form_representation.get_dialect()
    "vn" : lambda form_representation: form_representation.get_comment(config.xml.national),
    "vr" : lambda form_representation: form_representation.get_comment(config.xml.regional),
    "bw" : lambda lexical_entry: get_bw(lexical_entry),
    "et" : lambda lexical_entry: lexical_entry.get_etymology(),
    "eg" : lambda lexical_entry: lexical_entry.get_etymology_gloss(),
    "es" : lambda lexical_entry: lexical_entry.get_etymology_source(),
    "ec" : lambda lexical_entry: lexical_entry.get_etymology_comment(),
    "pd" : lambda lexical_entry: lexical_entry.find_paradigms(),
    "pdlGroup": lambda lexical_entry: lexical_entry.get_paradigms(),
    "pdl": lambda paradigm: paradigm.get_paradigmLabel(),
    "pdv": lambda paradigm: paradigm.get_paradigm(language=config.xml.vernacular),
    "pde": lambda paradigm: paradigm.get_paradigm(language=config.xml.English),
    "pdn": lambda paradigm: paradigm.get_paradigm(language=config.xml.national),
    "pdr": lambda paradigm: paradigm.get_paradigm(language=config.xml.regional),
    "sg" : lambda lexical_entry: lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["sg"]),
    "pl" : lambda lexical_entry: lexical_entry.find_paradigms(grammatical_number=pd_grammaticalNumber["pl"]),
    "rd" : lambda lexical_entry: None,
    "1s" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['s']),
    "2s" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['s']),
    "3s" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['s']),
    "4s" : lambda lexical_entry: lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['s']),
    "1d" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['d']),
    "2d" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['d']),
    "3d" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['d']),
    "4d" : lambda lexical_entry: lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['d']),
    "1p" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p']),
    "1e" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['e']),
    "1i" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[1], grammatical_number=pd_grammaticalNumber['p'], clusivity=pd_clusivity['i']),
    "2p" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[2], grammatical_number=pd_grammaticalNumber['p']),
    "3p" : lambda lexical_entry: lexical_entry.find_paradigms(person=pd_person[3], grammatical_number=pd_grammaticalNumber['p']),
    "4p" : lambda lexical_entry: lexical_entry.find_paradigms(anymacy=pd_anymacy[4], grammatical_number=pd_grammaticalNumber['p']),
    "tb" : lambda lexical_entry: None,
    "sd" : lambda lexical_entry: lexical_entry.get_semantic_domains(),
    "is" : lambda lexical_entry: lexical_entry.get_semantic_domains(),
    "th" : lambda lexical_entry: lexical_entry.get_semantic_domains(),
    "bb" : lambda lexical_entry: lexical_entry.get_bibliography(),
    "pc" : lambda lexical_entry: None,
    "nt" : lambda lexical_entry: lexical_entry.find_notes(type="general"),
    "np" : lambda lexical_entry: lexical_entry.find_notes(type="phonology"),
    "ng" : lambda lexical_entry: lexical_entry.find_notes(type="grammar"),
    "nd" : lambda lexical_entry: lexical_entry.find_notes(type="discourse"),
    "na" : lambda lexical_entry: lexical_entry.find_notes(type="anthropology"),
    "ns" : lambda lexical_entry: lexical_entry.find_notes(type="sociolinguistics"),
    "nq" : lambda lexical_entry: lexical_entry.find_notes(type="question"),
    "so" : lambda lexical_entry: None,
    "st" : lambda lexical_entry: lexical_entry.get_status(),
    "dt" : lambda lexical_entry: lexical_entry.get_date()
})

## Possible values allowed for 'ps' MDF marker
ps_range = set([
    "ADJ",      # Adjective
    "ADJR",     # Adjectivizer
    "MDL",      # Modal
    "ADV",      # Adverb
    "ADVR",     # Adverbializer
    "NEG",      # Negative
    "AFFM",     # Affirmative
    "NEGimp",   # Negative imperative
    "AL",       # Alienable
    "NOM",      # Nominative
    "AN",       # Animate
    "NOMR",     # Nominalizer
    "APPL",     # Applicative
    "n",        # Noun
    "ART",      # Article
    "NUM",      # Number
    "ASP",      # Aspect
    "AUX",      # Auxiliary
    "PTCL",     # Particle
    "PART",     # Participle
    "CLASS",    # Classifier
    "PAUS",     # Pause word
    "CMPAR",    # Comparative
    "PL",       # Plural
    "CMPLR",    # Complementizer
    "POSS",     # Possessive
    "CNJ",      # Conjunction
    "POSSR",    # Possessor
    "COND",     # Conditional
    "POST",     # Postposition
    "CONF",     # Confirmative
    "PREP",     # Preposition
    "CONN",     # Connective
    "PRO",      # Pronoun/pronominal
    "COP",      # Copula
    "PropN",    # Proper noun
    "DECL",     # Declarative
    "Q",        # Query/Question/Interrogative
    "DEIC",     # Deictic (spatial & temp.)
    "QNT",      # Quantifier
    "DEM",      # Demonstrative
    "DIR",      # Directional
    "REC",      # Reciprocal
    "REL",      # Relative(izer)
    "EVID",     # Evidential
    "RFLX",     # Reflexive
    "EXASP",    # Exasperative
    "RLR",      # Relater
    "EXIST",    # Existential
    "TAM",      # Tense-Aspect-Mood
    "FOC",      # Focus marker
    "TIME",     # Time expression
    "TNS",      # Tense
    "HORT",     # Hortative
    "TR",       # Transitive(izer)
    "ID",       # Idiom
    "v",        # Verb/verba
    "IMP",      # Imperative
    "vi",       # Intransitive verb
    "INTJ",     # Interjection
    "vm",       # Middle verb
    "INT",      # Interrogative (non-agentive passive)
    "ITR",      # Intransitive(izer)
    "vn",       # Non-active verb
    "vp",       # Passive verb (agentive)
    "vr",       # Reflexive/quasi-reflexive/intradirective
    "LIG",      # Ligature
    "vt",       # Transitive verb
    "LOC",      # Locative
    "vt/i"      # Ambitransitive verb
])

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
# Source: http://www.isocat.org/rest/dcs/119
ps_partOfSpeech = dict({
    "ADJ"       : "adjective", # http://www.isocat.org/datcat/DC-1230
    "ADJR"      : "adjective", # http://www.isocat.org/datcat/DC-1230
    "MDL"       : "modal", # http://www.isocat.org/datcat/DC-1329
    "ADV"       : "adverb", # http://www.isocat.org/datcat/DC-1232
    "ADVR"      : "adverb", # http://www.isocat.org/datcat/DC-1232
    "NEG"       : "negative particle", # http://www.isocat.org/datcat/DC-1894
    "AFFM"      : "affirmative particle", # http://www.isocat.org/datcat/DC-1918
    "NEGimp"    : None,
    "AL"        : None,
    "NOM"       : None,
    "AN"        : None,
    "NOMR"      : None,
    "APPL"      : None,
    "n"         : "noun", # http://www.isocat.org/datcat/DC-1333
    "ART"       : "article", # http://www.isocat.org/datcat/DC-1892
    "NUM"       : "numeral", # http://www.isocat.org/datcat/DC-1334
    "ASP"       : None,
    "AUX"       : "auxiliary", #  http://www.isocat.org/datcat/DC-1244
    "PTCL"      : "particle", # http://www.isocat.org/datcat/DC-1342
    "PART"      : "participle adjective", # http://www.isocat.org/datcat/DC-1598
    "CLASS"     : "classifier", # http://www.isocat.org/datcat/DC-2345
    "PAUS"      : None,
    "CMPAR"     : None,
    "PL"        : None,
    "CMPLR"     : "comparative particle", # http://www.isocat.org/datcat/DC-1922
    "POSS"      : "possessive pronoun", # http://www.isocat.org/datcat/DC-1359
    "CNJ"       : "conjunction", # http://www.isocat.org/datcat/DC-1260
    "POSSR"     : "possessive relative pronoun", # http://www.isocat.org/datcat/DC-3005
    "COND"      : "conditional particle", # http://www.isocat.org/datcat/DC-2230
    "POST"      : "postposition", # http://www.isocat.org/datcat/DC-1360
    "CONF"      : None,
    "PREP"      : "preposition", # http://www.isocat.org/datcat/DC-1366
    "CONN"      : None,
    "PRO"       : "pronoun", # http://www.isocat.org/datcat/DC-1370
    "COP"       : None,
    "PropN"     : "proper noun", # http://www.isocat.org/datcat/DC-1371
    "DECL"      : "declarative punctuation", # http://www.isocat.org/datcat/DC-2086
    "Q"         : "interrogative particle", # http://www.isocat.org/datcat/DC-1921
    "DEIC"      : None,
    "QNT"       : None,
    "DEM"       : "demonstrative determiner", # http://www.isocat.org/datcat/DC-1269
    "DIR"       : None,
    "REC"       : "reciprocal pronoun", # http://www.isocat.org/datcat/DC-1924
    "REL"       : "relative determiner", # http://www.isocat.org/datcat/DC-1379
    "EVID"      : None,
    "RFLX"      : "reflexive determiner", # http://www.isocat.org/datcat/DC-1377
    "EXASP"     : None,
    "RLR"       : None,
    "EXIST"     : "existential pronoun", # http://www.isocat.org/datcat/DC-3012
    "TAM"       : None,
    "FOC"       : None,
    "TIME"      : "time noun", # http://www.isocat.org/datcat/DC-3855
    "TNS"       : None,
    "HORT"      : None,
    "TR"        : None,
    "ID"        : None,
    "v"         : "verb", # http://www.isocat.org/datcat/DC-1424
    "IMP"       : None,
    "vi"        : "intransitive verb", # http://www.isocat.org/datcat/DC-1322
    "INTJ"      : "interjection", # http://www.isocat.org/datcat/DC-1318
    "vm"        : None,
    "INT"       : "interrogative determiner", # http://www.isocat.org/datcat/DC-1320
    "ITR"       : None,
    "vn"        : None,
    "vp"        : None,
    "vr"        : "reflexive verb", # http://www.isocat.org/datcat/DC-5592
    "LIG"       : None,
    "vt"        : "transitive verb", # http://www.isocat.org/datcat/DC-1405
    "LOC"       : "presentative pronoun", # http://www.isocat.org/datcat/DC-3015
    "vt/i"      : "bitransitive verb" # http://www.isocat.org/datcat/DC-1275
})

## Mapping between MDF markers and LMF semantic relation RelatedForm attribute value (input)
mdf_semanticRelation = dict({
    "sy" : "synonym",
    "an" : "antonym",
    "hm" : "homonym",
    "et" : "etymology",
    "se" : "subentry",
    "mn" : "main entry",
    "cf" : "simple link",
    "cp" : "complex predicate",
    "lf" : None,
    "ev" : None,
    "ee" : None,
    "en" : None,
    "er" : None
    # "derived form",
    # "root",
    # "stem",
    # "collocation"
})

## Mapping between 'pd' MDF markers and LMF person WordForm attribute value (input)
pd_person = dict({
    1 : "first person",
    2 : "second person",
    3 : "third person"
})

## Mapping between 'pd' MDF markers and LMF anymacy WordForm attribute value (input)
pd_anymacy = dict({
    4 : "inanimate"
})

## Mapping between 'pd' MDF markers and LMF grammatical number WordForm attribute value (input)
pd_grammaticalNumber = dict({
    'd'     : "dual",
    'p'     : "plural",
    "pl"    : "plural",
    's'     : "singular",
    "sg"    : "singular"
})

## Mapping between 'pd' MDF markers and LMF clusivity WordForm attribute value (input)
pd_clusivity = dict({
    'i'     : "inclusive",
    'e'     : "exclusive"
})

## Mapping between 'pdl' MDF marker value and LMF paradigm label Paradigm attribute value (input)
pdl_paradigmLabel = dict({
    "la"        : "lexicalized affix",
    "cc"        : "conjugation class",
    "past"      : "past stem",
    "comit"     : "comitative",
    "constr"    : "construction",
    "dir"       : "directional",
    "ir"        : "irregularity",
    "cl"        : "classifier"
})

## Possible values allowed for 'sd' MDF marker
sd_range = set([
    "Nagri", "nAgri", "Agriculture", # agriculture
    "Nanim", # animal
    "Nboat", # boat related
    "Nbody", "nBody", "Body", # body part
    "Ncult", # material culture
    "Nfish", # fish related
    "Nfood", # food related
    "Ngovt", # government
    "Nhouse", # house related
    "Ninsect", # insect
    "Ninstr", # instrument
    "Nkin", # kinship
    "Nloc", # locative noun
    "Nnature", # nature/meteorological
    "Npart", # part of a larger whole
    "Nplant", # plant
    "Nresult", # noun of result
    "Nrit", # ritual
    "Nsick", # sickness/medicine
    "Nsocial", # social relations (non-kin)
    "Ntime", # time
    "Vaffect", # affect (hit, kick, knock, hammer)
    "Vagri", # agriculture
    "Vbody", # bodily function
    "Vcarry", "vCarry", "Carry", # carry verb
    "Vcog", # verb of cognition
    "Vcolor", # color verb
    "Vcut", "vCut", "Cut", # cutting verb
    "Veffect", # verb of effect
    "Vemot", # verb expressing emotion
    "Vevent", # verb naming or characterizing a whole event
    "Vexchange", # verb of exchange (give, receive, take, get)
    "Vhit", # hitting verb
    "Vhold", # holding verb
    "Vhunt", # hunting related
    "Vmotion", # verb of locomotion
    "Vposture", # verb of posture or rest
    "Vrit", # verb describing ritual
    "Vsee", # verb of perception
    "Vsize", # verb of dimension
    "Vsocial", # verb expressing social relationship
    "Vspeak", # speech-act verb
    "Vspeed", # verb of speed
    "Vtouch", # touching verb
    "Vvalue", # verb expressing value
    "Vweath", # weather verbs (rain, fog)
    "Vweight", # verb expressing weight
    "ADJage", # age
    "ADJbodily", # bodily function
    "ADJcol", # color adjective
    "ADJemot", # emotion/human propensity
    "ADJphys", # physical property (hard, clean, hot)
    "ADJsize", "adjSize", "Size", # size/dimension
    "ADJspeed", "adjSpeed", "Speed", # speed
    "ADJtext", # texture
    "ADJval" # value (good, bad, nice)
])

## Possible values allowed for 'lf' MDF marker
lf_range = set([
    "Ant", # Antonym
    "Caus", # Causal
    "Compound", # Lexicalized compound using headword not easily handled by other lexical functions
    "Cpart", # Counterpart (complement, conversive)
    "Degrad", # Degraded degree or state
    "Feel", # Feeling or sensation associated with headword
    "Gen", # Generic
    "Group", # Collective/group
    "Head", # Head or leader of group
    "Idiom", # Idiom
    "Mat", # Material used to make headword
    "Max", # Superlative degree of headword
    "Min", # Diminished degree of headword
    "Nact", # Actor noun
    "Nben", # Benefactee noun
    "Ndev", # Deverbal noun
    "Ninst", # Instrumental noun
    "Ngoal", # Goal of action
    "Nloc", # Locative noun
    "Nug", # Undergoer noun
    "ParS", # Parallelism representing Same as headword
    "ParD", # Parallelism representing Different end of scale
    "Part", # Part of headword
    "Phase", # Phase of headword
    "Prep", # Preparatory activity
    "Res", # Consequence or resulting state
    "Serial", # Conventionalized serial verb combination not clearly handled by other lexical functions
    "Sim", # Similar type at same level of hierarchy
    "Sit", # Situation or activity typically associated with headword
    "Sound", # Sound associated with headword
    "Spec", # Specific (kind of, type of, species)
    "Start", # Beginning phase of headword (inceptive)
    "Stop", # Final phase of headword (cessative)
    "Syn", # Synonym (same range of meaning)
    "SynD", # Synonym in another dialect of the same language
    "SynL", # Loan synonym fully assimilated into language
    "SynR", # Synonym in another register of same language
    "SynT", # Taboo synonym
    "Unit", # Single occurrence of headword
    "Vwhole", # Verb of the whole
    "Whole" # Whole of which the headword is a part
])
