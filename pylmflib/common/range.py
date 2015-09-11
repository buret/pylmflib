#! /usr/bin/env python

"""! @package common
"""

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range = set([
    "adjective", # http://www.isocat.org/datcat/DC-1230
    "adposition", # http://www.isocat.org/datcat/DC-1231
    "adverb", # http://www.isocat.org/datcat/DC-1232
    "affirmative particle", # http://www.isocat.org/datcat/DC-1918
    "affix", # http://www.isocat.org/datcat/DC-1234
    "article", # http://www.isocat.org/datcat/DC-1892
    "auxiliary", #  http://www.isocat.org/datcat/DC-1244
    "bitransitive verb", # http://www.isocat.org/datcat/DC-1275
    "classifier", # http://www.isocat.org/datcat/DC-2345
    "comparative particle", # http://www.isocat.org/datcat/DC-1922
    "conditional particle", # http://www.isocat.org/datcat/DC-2230
    "conjunction", # http://www.isocat.org/datcat/DC-1260
    "coordinating conjunction", # http://www.isocat.org/datcat/DC-1262
    "declarative punctuation", # http://www.isocat.org/datcat/DC-2086
    "demonstrative determiner", # http://www.isocat.org/datcat/DC-1269
    "determiner", # http://www.isocat.org/datcat/DC-1272
    "existential pronoun", # http://www.isocat.org/datcat/DC-3012
    "ideophone", # http://www.isocat.org/datcat/DC-4192
    "impersonal verb", # http://www.isocat.org/datcat/DC-1306
    "indefinite determiner", # http://www.isocat.org/datcat/DC-1307
    "interjection", # http://www.isocat.org/datcat/DC-1318
    "interrogative determiner", # http://www.isocat.org/datcat/DC-1320
    "interrogative particle", # http://www.isocat.org/datcat/DC-1921
    "intransitive verb", # http://www.isocat.org/datcat/DC-1322
    "modal", # http://www.isocat.org/datcat/DC-1329
    "negation", # http://www.isocat.org/datcat/DC-2313
    "negative particle", # http://www.isocat.org/datcat/DC-1894
    "noun", # http://www.isocat.org/datcat/DC-1333
    "numeral", # http://www.isocat.org/datcat/DC-1334
    "particle", # http://www.isocat.org/datcat/DC-3372 or http://www.isocat.org/datcat/DC-1342
    "participle adjective", # http://www.isocat.org/datcat/DC-1598
    "possessive pronoun", # http://www.isocat.org/datcat/DC-1359
    "possessive relative pronoun", # http://www.isocat.org/datcat/DC-3005
    "postposition", # http://www.isocat.org/datcat/DC-1360
    "preposition", # http://www.isocat.org/datcat/DC-1366
    "presentative pronoun", # http://www.isocat.org/datcat/DC-3015
    "pronoun", # http://www.isocat.org/datcat/DC-1370
    "proper noun", # http://www.isocat.org/datcat/DC-1371
    "reciprocal pronoun", # http://www.isocat.org/datcat/DC-1924
    "reflexive determiner", # http://www.isocat.org/datcat/DC-1377
    "reflexive verb", # http://www.isocat.org/datcat/DC-5592
    "relative determiner", # http://www.isocat.org/datcat/DC-1379
    "time noun", # http://www.isocat.org/datcat/DC-3855
    "transitive verb", # http://www.isocat.org/datcat/DC-1405
    "verb" # http://www.isocat.org/datcat/DC-1424
])

## Possible values allowed for LMF variant type FormRepresentation attribute
type_variant_range = set([
    "unspecified",
    "orthography",
    "phonetics",
    "archaic"
])

## Possible values allowed for LMF note type Statement attribute
noteType_range = set([
    "comparison",
    "history",
    "semantics",
    "tone",
    "derivation",
    "case",
    "subord",
    "usage",
    "comment",
    "legend",
    "restriction",
    "encyclopedic",
    "anthropology",
    "discourse",
    "grammar",
    "phonology",
    "question",
    "sociolinguistics",
    "general"
])

## Possible values allowed for LMF grammatical number WordForm attribute
grammaticalNumber_range = set([
    "collective",
    "dual",
    "paucal",
    "plural",
    "quadrial",
    "singular",
    "trial"
])

## Possible values allowed for LMF grammatical gender WordForm attribute
grammaticalGender_range = set([
    "common gender",
    "feminine",
    "masculine",
    "neuter"
])

## Possible values allowed for LMF grammatical person WordForm attribute
person_range = set([
    "first person",
    "second person",
    "third person"
])

## Possible values allowed for LMF anymacy WordForm attribute
anymacy_range = set([
    "animate",
    "inanimate",
    "other anymacy"
])

## Possible values allowed for LMF clusivity WordForm attribute
clusivity_range = set([
    "inclusive",
    "exclusive"
])

## Possible values allowed for LMF grammatical tense WordForm attribute
tense_range = set([
    "future",
    "imperfect",
    "past",
    "present"
])

## Possible values allowed for LMF voice WordForm attribute
voice_range = set([
    "active voice",
    "middle voice",
    "passive voice"
])

## Possible values allowed for LMF verb form mood WordForm attribute
verbFormMood_range = set([
    "gerundive",
    "imperative",
    "indicative",
    "infinitive",
    "participle",
    "subjunctive",
    "conditional",
    "relative mood",
    "prohibitive mood",
    "debitive mood"
])

## Possible values allowed for LMF degree WordForm attribute
degree_range = set([
    "comparative degree",
    "positive degree",
    "superlative degree"
])

## Possible values allowed for semantic relation RelatedForm attribute
semanticRelation_range = set([
    "synonym",
    "antonym",
    "homonym",
    "etymology",
    "subentry",
    "main entry",
    "simple link",
    "complex predicate",
    "derived form",
    "root",
    "stem",
    "collocation"
])

## Possible values allowed for paradigm label Paradigm attribute
paradigmLabel_range = set([
    "lexicalized affix",
    "conjugation class",
    "past stem",
    "comitative", "COM",
    "construction",
    "directional",
    "irregularity",
    "classifier"
])

## Possible values allowed for example type Context attribute
type_example_range = set([
    "proverb",
    "locution",
    "example",
    "combination"
])

## Possible values allowed for media type Material attribute
mediaType_range = set([
    "unspecified",
    "unknown",
    "audio",
    "video",
    "document",
    "text",
    "image",
    "drawing"
])

## Possible values allowed for quality Audio attribute
quality_range = set([
    "very low",
    "low",
    "normal",
    "good",
    "very good" # high
])
