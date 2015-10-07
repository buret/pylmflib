#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import ps_partOfSpeech, mdf_lmf, set_bw
from common.range import partOfSpeech_range
from config.tex import partOfSpeech_tex
from utils.io import EOL, ENCODING
from common.defs import VERNACULAR, NATIONAL, ENGLISH, REGIONAL
from utils.error_handling import Warning

## To define languages and fonts
import config
FRENCH = "French"

## Semantic domains
order = [
    ("TITLE 1", "1. Le corps : humains et animaux"),
    [
        ("TITLE 2", "1.1. Anatomie"),
        [
            ("corps", "1.1.1. Corps humain"),
            [
                ("corps_doigt", "1.1.1.1. Parties du corps humain : doigts, orteil")
            ],
            ("corps_animaux", "1.1.2. Corps animal")
        ],
        ("TITLE 2", "1.2. Fonctions naturelles"),
        [
            ("fonct.nat", "1.2.1. Fonctions naturelles humaines"),
            ("fonct.nat.animaux", "1.2.2. Fonctions naturelles des animaux")
        ],
        ("TITLE 2", "1.3. Santé, maladie, médecine"),
        [
            ("santé", "1.3.1. Santé, maladie"),
            ("médecine", "1.3.2. Remèdes, médecine")
        ],
        ("TITLE 2", "1.4. Vêtements, parure, soins du corps"),
        [
            ("habillement", "1.4.1. Vêtements, parure"),
            ("soin", "1.4.2. Soins du corps")
        ],
        ("TITLE 2", "1.5. Positions, déplacements, mouvements, actions"),
        [
            ("position", "1.5.1. Préfixes et verbes de position"),
            ("TITLE 3", "1.5.2. Verbes de déplacement et de mouvement"),
            [
                ("déplacement", "1.5.2.1. Verbes de déplacement et moyens de déplacement"),
                ("mouvement", "1.5.2.2. Verbes de mouvement"),
                ("déplacement_moyen", "1.5.2.3. Moyens de locomotion et chemins")
            ],
            ("action", "1.5.3. Verbes d'action (en général)"),
            ("portage", "1.5.4. Portage"),
            ("action_corps", "1.5.5. Mouvements ou actions faits avec le corps, les bras, les mains, les pieds"),
            ("action.tête", "1.5.6. Mouvements ou actions avec la tête, les yeux, la bouche"),
            ("action_corps_animaux", "1.5.7. Verbes d'action faite par des animaux"),
            ("interaction_animaux", "1.5.8. Interaction avec les animaux"),
            ("action eau, liquide, fumée", "1.5.9. Actions liées aux éléments (liquide, fumée)"),
            ("action.plantes","1.5.10. Actions liées aux plantes"),
            ("grammaire_manière", "1.5.11. Manière de faire l’action : verbes et adverbes de manière"),
            ("action.outils", "1.5.12. Actions avec un instrument, un outil")
        ]
    ],
    ("TITLE 1", "2. Caractéristiques et propriétés"),
    [
        ("son", "2.1. Sons, bruits"),
        ("couleur", "2.2. Couleurs"),
        ("caract.personne", "2.3. Caractéristiques et propriétés des personnes"),
        ("caract.animal", "2.4. Caractéristiques et propriétés des animaux"),
        ("TITLE 2", "2.5. Caractéristiques et propriétés des objets"),
        [
            ("caract.objet", "2.5.1. Description des objets, formes, consistance, taille"),
            ("configuration", "2.5.2. Configuration des objets")
        ],
    ],
    ("TITLE 1", "3. Techniques"),
    [
        ("TITLE 2", "3.1. Habitat"),
        [
            ("habitat", "3.1.1. Habitat"),
            ("maison", "3.1.2. Types de maison, architecture de la maison"),
            ("maison.objet", "3.1.3. Objets et meubles de la maison"),
        ],
        ("TITLE 2", "3.2. Cultures, plantations, récoltes, végétation"),
        [
            ("cultures", "3.2.1. Cultures, techniques, boutures"),
            ("cultures_outil", "3.2.2. Objets, outils"),
            ("cultures_champ", "3.2.3. Types de champs"),
            ("végétation", "3.2.4. Végétation")
        ],
        ("TITLE 2", "3.3. Chasse guerre"),
        [
            ("armes", "3.3.1. Armes"),
            ("chasse", "3.3.2. Chasse"),
            ("guerre", "3.3.3. Guerre")
        ],
        ("pêche", "3.4. Pêche"),
        ("navigation", "3.5. Navigation"),
        ("feu", "3.6. Feu : objets et actions liés au feu"),
        ("TITLE 2", "3.7. Cuisine, alimentation"),
        [
            ("ustensile", "3.7.1. Ustensiles"),
            ("prép.aliments", "3.7.2. Préparation des aliments; modes de préparation et de cuisson"),
            ("nourriture", "3.7.3. Aliments, alimentation"),
            ("nourriture_goût", "3.7.4. Goût des aliments"),
            ("nourriture_tabac", "3.7.5. Tabac, actions liées au tabac")
        ],
        ("TITLE 2", "3.8. Tressage (nattes, paniers), cordes, noeuds, paquets"),
        [
            ("tressage", "3.8.1. Tressage"),
            ("noeud", "3.8.2. Noeuds"),
            ("natte", "3.8.3. Nattes"),
            ("paniers", "3.8.4. Paniers"),
            ("cordes", "3.8.5. Cordes, cordages"),
            ("couture", "3.8.6. Couture")
        ],
        ("TITLE 2", "3.9. Bois et travail du bois, outils"),
        [
            ("bois", "3.9.1. Bois"),
            ("bois_travail", "3.9.2. Travail bois")
        ],
        ("TITLE 2", "3.10. Outils, instruments, matériaux, pont"),
        [
            ("outils", "3.10.1. Outils"),
            ("TITLE 3", "3.10.2. Instruments et ponts"),
            [
                ("instrument", "3.10.2.1. Instruments"),
                ("instrument_pont", "3.10.2.2. Ponts")
            ]
        ]
    ],
    ("TITLE 1", "4. Individu - société"),
    [
        ("étapes.vie", "4.1. Cours de la vie"),
        ("TITLE 2", "4.2. Fonctions intellectuelles, sentiments"),
        [
            ("fonct.intell.", "4.2.1. Fonctions intellectuelles"),
            ("sentiments", "4.2.2. Sentiments")
        ],
        ("TITLE 2", "4.3. Parenté"),
        [
            ("parenté", "4.3.1. Parenté"),
            ("parenté_appellation", "4.3.2. Appellation parenté"),
            ("parenté_alliance", "4.3.3. Alliance"),
            ("parenté_couple", "4.3.4. Couples de parenté")
        ],
        ("TITLE 2", "4.4. Organisation sociale, richesses, dons, échanges"),
        [
            ("TITLE 3", "4.4.1. Société et organisation sociale"),
            [
                ("société", "4.4.1.1. Société"),
                ("société_organisation", "4.4.1.2. Organisation sociale")
            ],
            ("interaction", "4.4.2. Relations et interaction sociales"),
            ("richesses", "4.4.3. Richesses, monnaies traditionnelles"),
            ("échanges", "4.4.4. Dons, échanges, achat et vente, vol"),
            ("coutumes_objet", "4.4.5. Objets coutumiers"),
            ("coutumes", "4.4.6. Coutumes, dons coutumiers")
        ],
        ("religion", "4.5. Religion, représentations religieuses"),
        ("TITLE 2", "4.6. Fêtes, danse, chant, jeux"),
        [
            ("danse", "4.6.1. Danses"),
            ("musique", "4.6.2. Musique, instruments de musique"),
            ("jeu", "4.6.3. Jeux divers")
        ],
        ("TITLE 2", "4.7. Traditions orales, relations inter-individuelles"),
        [
            ("discours_tradition_orale", "4.7.1. Tradition orale"),
            ("discours", "4.7.2. Discours, échanges verbaux")
        ],
        ("TITLE 2", "4.8. Découpage du temps, jours, saisons"),
        [
            ("temps", "4.8.1. Temps"),
            ("temps_deixis", "4.8.2. Adverbes déictiques de temps"),
            ("temps_découpage", "4.8.3. Découpage du temps"),
            ("temps_jours", "4.8.4. Jours"),
            ("temps_saison", "4.8.5. Saisons")
        ],
        ("TITLE 2", "4.9. Orientation, direction, localisation"),
        [
            ("grammaire_direction", "4.9.1. Directions"),
            ("grammaire_directionnel", "4.9.2. Directionnels"),
            ("grammaire_locatif", "4.9.3. Localisation"),
            [
                ("nom_locatif", "4.9.3.1. Noms locatifs"),
                ("verbe_locatif", "4.9.3.2. Verbes locatifs")
            ]
        ]
    ],
    ("TITLE 1", "5. Nature"),
    [
        ("TITLE 2", "5.1. Ciel"),
        [
            ("astre", "5.1.1. Astres"),
            ("vent", "5.1.2. Vents"),
            ("temps_atmosphérique", "5.1.3. Phénomènes atmosphériques et naturels"),
            ("température", "5.1.4. Température")
        ],
        ("TITLE 2", "5.2. Terre; les terrains et leur constitution"),
        [
            ("terrain_pierre", "5.2.1. Pierre, roche"),
            ("terrain_terre", "5.2.2. Terre"),
            ("topographie", "5.2.3. Topographie")
        ],
        ("TITLE 2", "5.3. Eau (eau douce, mer)"),
        [
            ("eau", "5.3.1. Eau"),
            ("eau_marée", "5.3.2. Marées"),
            ("eau_mer", "5.3.3. Mer"),
            ("eau_mer_plante", "5.3.4. Coraux"),
            ("eau_topographie", "5.3.5. Mer : topographie")
        ],
        ("matière", "5.4. Matière, matériaux"),
        ("lumière", "5.5. Lumière et obscurité")
    ],
    ("TITLE 1", "6. Zoologie"),
    [
        ("oiseau", "6.1. Oiseaux"),
        ("TITLE 2", "6.2. Mammifères"),
        [
            ("mammifères", "6.2.1. Mammifères"),
            ("mammifères marins", "6.2.2. Mammifères marins")
        ],
        ("TITLE 2", "6.3. Reptiles"),
        [
            ("reptile", "6.3.1. Reptiles"),
            ("reptile_marin", "6.3.2. Reptiles marins")
        ],
        ("crustacés", "6.4. Crustacés, crabes"),
        ("TITLE 2", "6.5. Echinodermes, céphalopodes"),
        [
            ("échinoderme", "6.5.1. Echinodermes"),
            ("céphalopode", "6.5.2. Céphalopodes")
        ],
        ("mollusque", "6.6. Mollusques"),
        ("poisson", "6.7. Poissons"),
        ("anguille", "6.8. Anguilles"),
        ("insecte", "6.9. Insectes")
    ],
    ("TITLE 1", "7. Botanique"),
    [
        ("arbre", "7.1. Arbre"),
        ("TITLE 2", "7.2. Description des végétaux"),
        [
            ("plantes", "7.2.1. Noms des plantes"),
            ("plantes_partie", "7.2.2. Parties de plantes"),
            ("plantes_processus", "7.2.3. Processus liés aux plantes")
        ],
        ("arbre_cocotier", "7.3. Cocotiers"),
        ("igname", "7.4. Ignames"),
        ("taro", "7.5. Taros"),
        ("bananier", "7.6. Bananiers et bananes"),
        ("cucurbitacée", "7.7. Cucurbitacées"),
        ("plantes.fruit", "7.8. Fruits")
    ],
    ("TITLE 1", "8. Classificateurs"),
    [
        ("classificateur sémantique", "8.1. Préfixes classificateurs sémantiques"),
        ("classificateur possessif", "8.2. Préfixes classificateurs possessifs"),
        ("classificateur nourriture", "8.3. Préfixes classificateurs de la nourriture"),
        ("classificateur numérique", "8.4. Préfixes classificateurs numériques")
    ],
    ("TITLE 1", "9. Numération"),
    [
        ("grammaire_numéral", "9.1. Numéraux cardinaux"),
        ("grammaire_ordinal", "9.2. Numéraux ordinaux")
    ],
    ("TITLE 1", "10. Quantificateurs et marques de degré"),
    [
        ("grammaire_quantificateur", "10.1. Quantificateurs"),
        ("grammaire_quantificateur_degré", "10.2. Marques de degré"),
        ("grammaire_distributif", "10.3. Distributifs")
    ],
    ("TITLE 1", "11. Eléments grammaticaux"),
    [
        ("grammaire_adverbe", "11.1. Adverbe"),
        ("grammaire_agent", "11.2. Agent"),
        ("grammaire_article", "11.3. Articles"),
        ("grammaire_article_indéfini", "11.4. Article indéfini"),
        ("grammaire_aspect", "11.5. Aspect"),
        ("grammaire_temps", "11.6. Temps"),
        ("grammaire_modalité", "11.7. Modalité, verbes modaux"),
        ("grammaire_assertif", "11.8. Marques assertives"),
        ("grammaire_causatif", "11.9. Causatif"),
        ("grammaire_comparaison", "11.10. Comparaison"),
        ("grammaire_conjonction", "11.11. Conjonction"),
        ("grammaire_contraste", "11.12. Contraste"),
        ("grammaire_démonstratif", "11.13. Démonstratifs"),
        ("grammaire_dérivation", "11.14. Dérivation"),
        ("grammaire_existentiel", "11.15. Prédicats existentiels"),
        ("grammaire_injonction", "11.16. Injonction"),
        ("TITLE 2", "11.17. Interjection et interpellation"),
        [
            ("discours_interjection", "11.17.1. Interjection"),
            ("grammaire_interpellation", "11.17.2. Interpellation")
        ],
        ("grammaire_interrogatif", "11.18. Interrogatifs"),
        ("grammaire_négation", "11.19. Négation"),
        ("grammaire_négation_existentiel", "11.20. Négation existentielle"),
        ("grammaire_nombre", "11.21. Marque de nombre"),
        ("grammaire_relateur_possessif", "11.22. Relateurs et relateurs possessifs"),
        ("grammaire_préfixe", "11.23. Préfixes dérivationnels"),
        ("TITLE 2", "11.24. Préfixes compositionnels sémantiques"),
        [
            ("grammaire_préfixe_sémantique", "11.24.1. Préfixes sémantiques divers"),
            ("grammaire_préfixe_sémantique_position", "11.24.2. Préfixes sémantiques de position"),
            ("grammaire_préfixe_sémantique_action", "11.24.3. Préfixes sémantiques d’action"),
            ("grammaire_préfixe_sémantique_déplacement", "11.24.4. Préfixes sémantiques de déplacement")
        ],
        ("grammaire_préposition", "11.25. Prépositions"),
        ("grammaire_présentatif", "11.26. Présentatifs"),
        ("grammaire_pronom", "11.27. Pronoms"),
        ("grammaire_pronom_négatif", "11.28. Pronom négatif"),
        ("grammaire_réciproque", "11.29. Réciproque"),
        ("TITLE 2", "11.30. Réfléchi, intensificateur"),
        [
            ("grammaire_réfléchi", "11.30.1. Réfléchi"),
            ("grammaire_réfléchi_intensificateur", "11.30.2. Intensificateur")
        ],
        ("grammaire_restrictif", "11.31. Marques restrictives"),
        ("grammaire_suff.transitif", "11.32. Suffixes transitifs"),
        ("grammaire_IS", "11.33. Structure informationnelle"),
        ("grammaire_vocatif", "11.34. Vocatifs")
    ]
]

def read_order(order, sd_order, rank, sd_list):
    for element in order:
        if type(element) is not list:
            sd = element[0]
            if not sd.startswith("TITLE"):
                rank += 1
                sd_order.update({sd.decode(ENCODING) : rank})
            sd_list.append(element)
        else:
            (sd_order, rank, sd_list) = read_order(element, sd_order, rank, sd_list)
    return (sd_order, rank, sd_list)

sd_order = dict()
rank = 0
sd_list = list()
(sd_order, rank, sd_list) = read_order(order, sd_order, rank, sd_list)
sd_order.update({"-" : rank + 1})

def compare_sd(x, y):
    """Compare 2 semantic domains between each other.
    """
    try:
        # Both equal => do nothing
        if sd_order[x] == sd_order[y]:
            return 0
        # If the 1st one is lower than the 2nd one, its rank is decremented
        if sd_order[x] < sd_order[y]:
            return -1
        # If the 1st one is greater than the 2nd one, its rank is incremented
        elif sd_order[x] > sd_order[y]:
            return 1
    except KeyError:
        print Warning("Cannot compare " + x.encode(ENCODING) + " and " + y.encode(ENCODING))
        return -1

sd_errors = set()
def get_is(lexical_entry):
    for sd in lexical_entry.get_semantic_domains():
        # Consider only the first semantic domain
        if sd in sd_order.keys():
            return sd
        sd_errors.add(sd)
    return "-"
items=lambda lexical_entry: get_is(lexical_entry)

def get_gf(lexical_entry):
    for sense in lexical_entry.get_senses():
        for gloss in sense.find_glosses(language=config.xml.French):
            return gloss[0].lower() + gloss[1:]
    return "-"
reverse_items=lambda lexical_entry: get_gf(lexical_entry)

## Functions to process some MDF fields (input)
def set_ce(ce, lexical_entry):
    related_form = lexical_entry.get_last_related_form()
    if related_form is not None:
        related_form.create_and_add_form_representation(written_form=ce, language=config.xml.French)

def retrieve_dialect_name(text):
    text = text.replace("BO", u"Bondé")
    text = text.replace("PA", "Paimboa")
    text = text.replace("GO(s)", "Gomen Sud")
    text = text.replace("GO(n)", "Gomen Nord")
    text = text.replace("GO", "Gomen")
    text = text.replace("WEM", "WEM")
    text = text.replace("WE", "WE")
    return text

def force_caps(text):
    """Force first letter to be in upper case.
    """
    return text[0].upper() + text[1:]

mdf_lmf.update({
    # dialx : dialecte BO / PA / GO / GO(s) / GO(n) + WEM / WE => OK
    "dialx" : lambda dialx, lexical_entry: lexical_entry.set_usage_note(dialx.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), language="nua"),
    # empr : emprunt => OK
    "empr"  : lambda empr, lexical_entry: set_bw(empr, lexical_entry),
    # sc : nom scientifique => OK
    "sc"    : lambda sc, lexical_entry: lexical_entry.set_scientific_name(force_caps(sc)),
    # ge : French gloss
    "ge"    : lambda ge, lexical_entry: lexical_entry.set_gloss(force_caps(ge.replace('_', ' ').replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE")), language=config.xml.French),
    # xn : French example
    "xn"    : lambda xn, lexical_entry: lexical_entry.add_example(force_caps(xn), language=config.xml.French),
    # xe : English example
    "xe"    : lambda xe, lexical_entry: lexical_entry.add_example(force_caps(xe), language=config.xml.English),
    # sge : French gloss of the subentry
    "sge"   : lambda sge, lexical_entry: lexical_entry.set_gloss(force_caps(sge), language=config.xml.French),
    # de : French definition
    "de"    : lambda de, lexical_entry: lexical_entry.set_definition(force_caps(de), language=config.xml.French),
    # gr : note grammaticale => [Note grammaticale : ] à la suite de [Note : ]
    "gr"    : lambda gr, lexical_entry: lexical_entry.set_note(gr, type="grammar", language=config.xml.regional),
    # gt: traduction de gr en français => [Note grammaticale : 'gr' (en gras) 'gt' (non gras)]
    "gt"    : lambda gt, lexical_entry: lexical_entry.set_note(force_caps(gt), type="grammar", language=config.xml.French),
    # ce : French translation of cf => cf : 'cf' (en gras) 'ce' (non gras)
    "ce"    : lambda ce, lexical_entry: set_ce(force_caps(ce), lexical_entry),
    # nt : note => OK
    "nt"    : lambda nt, lexical_entry: lexical_entry.set_note(nt, type="general"),
    # ng : note grammaticale => OK
    "ng"    : lambda ng, lexical_entry: lexical_entry.set_note(ng, type="grammar", language=config.xml.vernacular),
    # np : note phonologique => OK
    "np"    : lambda np, lexical_entry: lexical_entry.set_note(np, type="phonology"),
    # na : note anthropologique => OK
    "na"    : lambda na, lexical_entry: lexical_entry.set_note(na, type="anthropology"),
    # ve : dialect(s) of variant BO / PA / GO / GO(s) / GO(n) + WEM / WE / vx / BO [BM] / BO (Corne) / BO (Corne, BM)
    "ve"    : lambda ve, lexical_entry: lexical_entry.set_dialect(ve.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE")),
    # xv : vernacular example => OK
    "xv"    : lambda xv, lexical_entry: lexical_entry.create_and_add_example(xv.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), language=config.xml.vernacular),
    # cf : confer => OK
    "cf"    : lambda cf, lexical_entry: lexical_entry.create_and_add_related_form(cf.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"), "simple link")
})

## Mapping between 'ps' MDF marker value and LMF part of speech LexicalEntry attribute value (input)
ps = [
    "ACC",

    "adresse honorifique",

    "AGT",
    "AGT ???",

    "ADJ",

    "ADV",
    "ADV.LOC (spatio-temporel) ANAPH ???",
    "ADV LOC DX2",
    "ADV.LOC",
    "ADV ; QNT",
    "ADV ; MODIF",
    "ADV ATTEN (ordre) (forme de politesse) ; ponctuel",
    "ADV.TEMPS",
    "ADV.SEQ (continuatif)",
    "ADV ???",
    "ADV.LOC.DEIC.2",
    "ADV ; LOC",

    "ANAPH",
    "ANAPH (discours ou passé ???)",
    "ANAPH (discours)",

    "ART",
    "ART.PL",

    "ASSOC",

    "ASP",
    "ASP duratif",
    "ASP ou RESTR",
    "ASP persistif",
    "ASP (itératif)",
    "ASP (révolu)",
    "ASP.HAB",
    "ASP.ACC",
    "ASP.INACC",
    "ASP (post-verbal)",
    "ASP transition, répétition, réversif",

    "atténuatif ???",

    "BENEF",

    "c",

    "CLF",
    "CLF.NUM (morceaux)",
    "CLF.NUM (morceaux) PA [pas à Gomen]",
    "CLF.NUM (multiples)",
    "CLF (armes)",
    "CLF.NUM (objets ronds)",
    "CLF.NUM (maisons)",
    "CLF.NUM (animés)",
    "CLF.NUM",
    "CLF.NUM (morceaux de bois)",
    "CLF.NUM (feuilles)",
    "CLF.NUM (tissus et étoffes végétales)",
    "CLF.NUM (lots : fête de la nouvelle igname, contexte cérémoniel)",
    "CLF.NUM (lots cérémoniels)",
    "CLF.NUM (pour compter des paquets d'ignames constitués de trois ignames)",
    "CLF.NUM (générique et des objets ronds)",
    "CLF.NUM (objets longs)",
    "CLF.NUM (bois, arbres, certaines racines comestibles, cordes, objets longs, sagaies, doigts)",
    "CLF.NUM (mains de banane)",
    "CLF.POSS",
    "CLF.POSS (armes)",

    "CNJ",
    "CNJ ; THEM",
    "CNJ TIME",
    "CNJ (complémentation)",
    "CNJ.HYP",
    "CNJ (but)",
    "CNJ.REL",
    "CNJ (passé)",
    "CNJ ; COMP",

    "COI",

    "COLL",
    "COLL + PRO",
    "COLL ; QNT",

    "COMPAR",

    "CONN",

    "contraste",
    "contraste ; état",

    "COORD",

    "couple PAR",

    "DEIC",
    "DEIC.DIR",
    "DEIC.3",
    "DEIC.PL.1 ou ANAPH",
    "DEIC.PL",
    "DEIC.1 duel ou ANAPH",
    "DEIC.3 duel (latéralement)",
    "DEIC.3 (visible)",
    "DEIC.1; ANAPH",
    "DEIC.1",
    "DEIC.2 ; ANAPH ; ASS",

    "DEM",
    "DEM duel",
    "DEM duel ou PL",
    "DEM triel (post-nom)",
    "DEM DX",
    "DEM.ANAPH",
    "DEM DX2",
    "DEM DX1",
    "DEM DX3",
    "DEM SG",
    "DEM (médial ou proche)",
    "DEM PL",
    "DEM PL (post-nom)",
    "DEM duel (post-nom)",
    "DEM.DIR",
    "DEM.DEIC.2 duel et ANAPH",
    "DEM.DEIC.2 ; ANAPH ; assertif",
    "DEM.DEIC.3 PL",
    "DEM DX3 ou ANAPH",
    "DEM.DEIC.3 duel",
    "DEM.DEIC.3 ou ANAPH",
    "DEM.DEIC.3 (distal)",
    "DEM DX4",
    "DEM.DEIC",
    "DEM.DEIC.1",
    "DEM.DEIC.2",
    "DEM.DEIC.3",
    "DEM.DEIC.4",

    "déterminant ; DEM duel",
    "DET duel",
    "DET; PRO.DEIC.1",

    "DIR",
    "DIR (transverse)",
    "DIR (centripète)",
    "DIR (centrifuge)",

    "dire du mal de qqn",

    "dispersif ; DISTR",

    "DISTR",

    "doute",

    "duel",

    "DUR",

    "DX1",
    "DX1 ; ANAPH",
    "DX2 ; ANAPH ; ASS",

    "FOC",
    "FOC ; RESTR (antéposé au GN) (za ... nye ...)",

    "forme déterminée de mwa ; PREF (désignant un contenant)",

    "FREQ",

    "FUT",

    "GEN (déterminant non-spécifique, générique ???)",

    "INCH",
    "INCH, en cours",

    "INDEF",

    "indétermination",

    "INJ",
    "INJ (en composition)",

    "INT",
    "INT.LOC (dynamique)",
    "INT.LOC (statique)",
    "INT (statique : humains, PRO, n)",
    "INT (statique)",
    "INT (indéfini)",
    "INT.COMPAR",

    "INTENS",
    "INTENS ; assertif (devant le prédicat)",
    "INTENS ; QNT",

    "interlocative",

    "interpellation",
    "interpellation ou DEM",

    "INTJ",
    "INTJ (pitié, affection)",
    "INTJ ; v",
    "INTJ ; appel respectueux à une pers.",

    "ITER",

    "LOC",
    "LOC.DIR",
    "LOC DX2",
    "LOC DX3",
    "LOC.ANAPH",
    "LOC DEIC DX3",
    "LOC ; n",
    "LOC (spatio-temporel)",
    "LOC CMPAR",
    "pré-LOC + LOC",
    "LOC.DEIC.2",
    "LOC.3",

    "LOCUT",
    "LOCUT ADV",
    "LOCUT INT",

    "MODAL",
    "MODAL n",
    "MODAL INTJ",

    "MODIF",

    "morphème de THEM (nrowö ... ca)",

    "n-fois",

    "n",
    "n (inaliénable)",
    "n ; CLF POSS",
    "n ; PAR REC",
    "n (composition)",
    "n LOC",
    "n.BENEF",
    "n ORD",
    "n ; v",
    "n ; v.stat.",
    "n ; LOC",
    "n (référence)",
    "n SG",
    "n ; CLF.NUM",
    "n.QNT",
    "n.CNJ",
    "n ; PRO",
    "n.LOC (forme POSS de pwamwa)",
    "n.LOC ; v",
    "n CMPAR",
    "n (terme d'appellation ou référence)",
    "n.INTJ",
    "n ; v ; COLL",
    "n.LOC",
    "n ; couple PAR",
    "n ; CLF.POSS",

    "NEG",
    "NEG (en réponse à une question)",

    "nombre",

    "NMLZ",

    "NUM",
    "NUM (animés)",
    "NUM.ORD",
    "NUM (pour certains types de dons coutumiers)",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux)",
    "NUM (pour certains types de dons coutumiers qui se comptent par deux) Bretteville",
    "NUM.COMPAR",

    "OBJ.INDIR",
    "objet",

    "OPT",

    "ORD",

    "PAR REC ???",
    "PAR REC",

    "passé",

    "POSS (certains lexèmes)",
    "POSS.INDIR",
    "POSS 1° pers. duel incl.",
    "POSS 1° pers. incl.",

    "PRED.NEG",
    "PRED.NEG (humain)",

    "PREF",
    "PREF (n agent)",
    "PREF (référant à une surface extérieure)",
    "PREF.NMLZ (instrumental)",
    "PREF ORD",
    "PREF CLF NUM (mains de banane)",
    "PREF (couple PAR)",
    "PREF (relations duelles)",
    "PREF (indiquant une position couchée)",
    "PREF.NMLZ",
    "PREF (lieu)",
    "PREF.CAUS",
    "PREF REC ; COLL",
    "PREF (position assise)",
    "PREF.NMLZ (n. d'agent)",
    "PREF (action avec le pied)",
    "PREF (indiquant la position debout)",
    "PREF.REC",
    "PREF.LOC",

    "PREP",
    "PREP (objet indirect)",
    "PREP ; ADV ; CNJ",
    "PREP.LOC",
    "PREP (ablatif)",
    "PREP (spatio-temporelle)",
    "PREP.BENEF",
    "PREP (instrumental) ; AGT ???",
    "PREP (régime indirect)",
    "PREP ; CNJ",
    "PREP (instrument)",
    "PREP.LOC (spatio-temporel)",

    "PRO",
    "PRO (sujet)",
    "PRO 1° pers. incl. (OBJ ou POSS)",
    "PRO 1° pers. excl. PL (sujet)",
    "PRO 1° pers. excl. PL (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 1° pers. triel incl.",
    "PRO 1° pers. SG (sujet ou OBJ)",
    "PRO (OBJ) ou POSS 1° pers. SG",
    "PRO 1° pers. incl. PL (sujet)",
    "PRO 1° pers. triel incl. (sujet)",
    "PRO 1° pers. duel incl. (sujet)",
    "PRO 1° pers. triel excl. (sujet, OBJ ou POSS)",
    "PRO 1° pers. duel excl. (sujet, OBJ ou POSS)",
    "PRO 1° pers. duel excl. (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 1° pers. duel incl.",
    "PRO 1° pers. incl. PL",
    "PRO 1° pers. incl. PL (OBJ ou POSS)",
    "PRO 1° pers. duel incl. (OBJ ou POSS)",
    "PRO 1° pers. SG (OBJ ou POSS)",
    "PRO 1° pers. triel incl. (OBJ ou POSS)",
    "PRO 2° pers. duel (sujet)",
    "PRO 2° pers. SG (sujet ou OBJ)",
    "PRO 2° pers. PL (sujet)",
    "PRO 2° pers. PL",
    "PRO (OBJ) ou POSS 2° pers. duel",
    "PRO 2° pers. SG (sujet, OBJ ou POSS)",
    "PRO (OBJ) ; POSS 2° pers. PL",
    "PRO 2° pers. PL (sujet, OBJ ou POSS)",
    "PRO 2° pers. duel (OBJ ou POSS)",
    "PRO 2° pers. PL (OBJ ou POSS)",
    "PRO 3° pers. SG (sujet)",
    "PRO 3° pers. SG (OBJ)",
    "PRO 3° pers. masc. PL",
    "PRO 3° pers. masc. duel (DX ou ANAPH)",
    "PRO 3° pers. PL (sujet)",
    "PRO 3° pers. PL (obj. ou poss.)",
    "PRO (OBJ) ou POSS 3° pers. duel",
    "PRO 3° pers. duel (sujet)",
    "PRO 3° pers. triel (sujet, OBJ ou POSS)",
    "PRO 3° pers. duel (OBJ ou POSS)",
    "PRO 3° pers. triel (OBJ ou POSS)",
    "PRO 3° pers. SG (OBJ ou POSS)",
    "PRO (OBJ) ou POSS 3° pers. triel",
    "PRO (OBJ) ou POSS 3° pers. SG",
    "PRO (sujet) (aspiré)",
    "PRO DEIC DX2 (latéral)",
    "PRO.DEIC ou ANAPH DX3",
    "PRO.DEIC.2 (latéral)",
    "PRO.DEIC PL",
    "PRO.DEIC 3° pers. fém. PL",
    "PRO.DEIC.2 (3° pers. masc. SG)",
    "PRO.DEIC.2 (3° pers. masc. PL)",
    "PRO.DEIC.2 (3° pers. PL)",
    "PRO.DEIC.3 (3° pers. masc. PL)",
    "PRO.DEIC.3 (3° pers.)",
    "PRO.DEIC.3 (3° pers. fém. PL)",
    "PRO DEM PL",
    "PRO DX2 3° pers. masc. SG",
    "PRO DX2 3° pers. masc. PL",
    "PRO DX3 3° pers. masc. PL",
    "PRO DX2 3° pers. fém. PL",
    "PRO DX2 3° pers. PL",
    "PRO DX3 3° pers. fém. PL",
    "PRO DX3 3° pers.",
    "PRO.INDEP 1° pers. duel excl.",
    "PRO.INDEP 1° pers. triel excl.",
    "PRO.INDEP 1° pers.",
    "PRO.INDEP 1° pers. triel incl.",
    "PRO.INDEP 1° pers. excl. PL",
    "PRO.INDEP 2° pers. PL",
    "PRO.INDEP 2° pers. triel",
    "PRO.INDEP 2° pers. SG",
    "PRO.INDEP 2° pers. duel",
    "PRO.INDEP 3° pers. duel",
    "PRO.INDEP 3° pers.",
    "PRO.INDEP 3° pers. PL",
    "PRO.INDEP 3° pers. triel ou paucal",
    "PRO.INT",
    "PRO.NEG",

    "PROH",

    "PTCL.MODAL (adversatif, hypothétique)",
    "PTCL ASP (post-verbal)",
    "PTCL (assertive)",
    "PTCL ASP",

    "QNT",
    "QNT (réduplication de pe- ???)",
    "QNT.DISTR",
    "QNT ; DISTR",
    "QNT ; atténuatif",
    "QNT ???",
    "QNT ; atténuatif (ordre) (forme de politesse) ; ponctuel",

    "REC",

    "REL",
    "REL ou DEM ???",

    "RESTR",
    "RESTR ; ASP",
    "RESTR + NUM",
    "RESTR ???",

    "relateur",

    "REV ; ITER GO(s)",
    "REV (u ... mwã)",

    "RFLX",

    "saturateur transitif ???",

    "SEQ",

    "sujet ; AGT",

    "SUFF",
    "SUFF.DIR",
    "SUFF.POSS 1° pers.",
    "SUFF.POSS 2° pers.",
    "SUFF.POSS 3° pers. SG",
    "SUFF.POSS.INT",
    "SUFF (transitif)",
    "SUFF.NMLZ",

    "THEM",
    "THEM (nrowö ... ca)",

    "transition, répétition, réversif",

    "triel",

    "v",
    "v.t.",
    "v.i.",
    "v ; MODIF ; INTENS ; RFLX",
    "v.LOC ; progressif",
    "v.stat. ; n",
    "v.LOC",
    "v ; ASP",
    "v ; PREP",
    "v ; QNT",
    "v ; n",
    "v.DIR",
    "v.stat.",
    "v.MODAL",
    "v ; ADV",
    "v.stat. ; ADV",
    "v.INT",
    "v.IMPERS",
    "v.stat. ???",
    "v (non-humains)",
    "v (en composition)",
    "v ; n ; CLF.POSS",
    "v.COMPAR",
    "v ; INTJ",
    "v.REC",
    "v ; INTJ ; n",
    "v.stat. ; QNT",
    "v.stat. ; MODIF",
    "v ASP",
    "v ; ADV",
    "v.i. ; n",
    "v.t. (+ PRO pers.)",
    "vt (+ PRO)",
    "v ; n ; CLF.NUM",
    "v.stat. ; v",
    "v ; n STAT",
    "v.COLL",
    "v ; MODIF",

    "vocatif",

    "voyelle euphonique",

    "???"
]
for item in ps:
    ps_partOfSpeech.update({item : item.decode(ENCODING)})

## Possible values allowed for LMF part of speech LexicalEntry attribute
partOfSpeech_range.update(ps_partOfSpeech.values())

## Functions to process some MDF fields (input)

## Functions to process some MDF fields (output)

## Mapping between LMF part of speech LexicalEntry attribute value and LaTeX layout (output)
partOfSpeech_tex.update({
    "XXX" : "unknown"
})

## Function giving order in which information must be written in docx and mapping between LMF representation and docx (output)
def lmf2doc(lexicon, document, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, paradigms=False, reverse=False):
    """! @brief Function to convert LMF lexical entry information to be written into docx commands.
    @param lexicon The Lexicon LMF instance to display.
    @param document The docx document to fill in.
    @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
    @param sort_order Python list. Default value is 'None', which means that the document output is alphabetically ordered.
    @param paradigms A boolean value to introduce paradigms in document or not.
    @param reverse A boolean value to set if a reverse dictionary is wanted.
    """
    # Pictures in a table
    table = document.add_table(rows=1, cols=4)
    table.cell(0, 0).paragraphs[0].add_run().add_picture('examples/yuanga/img1.png')
    table.cell(0, 1).paragraphs[0].add_run().add_picture('examples/yuanga/img2.png')
    table.cell(0, 2).paragraphs[0].add_run().add_picture('examples/yuanga/img3.png')
    table.cell(0, 3).paragraphs[0].add_run().add_picture('examples/yuanga/img4.png')
    # Page break
    document.add_page_break()
    # Lexicon is already ordered
    n = -1
    level = 0
    current_item = ("", "")
    for lexical_entry in lexicon.get_lexical_entries():
        # Consider only main entries (subentries will be written as parts of the main entry)
        if lexical_entry.find_related_forms("main entry") != []:
            continue
        if type(sort_order) is type(list()):
            # Check if item of current element is different from previous one
            while items(lexical_entry) != current_item[0].decode(ENCODING):
                try:
                    n += 1
                    current_item = sort_order[n]
                    while current_item[0].startswith("TITLE"):
                        level = int(current_item[0][-1])
                        # Heading
                        document.add_heading(current_item[1].decode(ENCODING), level=level)
                        n += 1
                        current_item = sort_order[n]
                    # Heading
                    document.add_heading(current_item[1].decode(ENCODING), level=level+1)
                    # Paragraph
                    p = document.add_paragraph()
                except IndexError:
                    # Reached end of list
                    break
        else:
            raise OutputError(object, "Sort order must be a list.")
        if not reverse:
            # Lexeme
            lexeme = lexical_entry.get_lexeme()
            if lexical_entry.get_homonymNumber() is not None:
                # Add homonym number to lexeme
                lexeme += " (" + str(lexical_entry.get_homonymNumber()) + ")"
            # Add morphology if any
            morph = ""
            for morphology in lexical_entry.get_morphologies():
                morph += " " + morphology
            # Add dialect if any
            dialect = ""
            for sense in lexical_entry.get_senses():
                for usage_note in sense.find_usage_notes(language=config.xml.vernacular):
                    dialect += " [" + usage_note + "]"
            p = document.add_paragraph()
            p.add_run(lexeme).bold = True
            if morph != "":
                p.add_run(" Morph. :").italic = True
            p.add_run(morph)
            p.add_run(dialect)
            # Dialectal variants
            write_title = True
            for repr in lexical_entry.get_form_representations():
                if repr.get_geographicalVariant() is not None:
                    if write_title:
                        p.add_run(" Var. : ")
                        write_title = False
                    else:
                        p.add_run(" ; ")
                    p.add_run(repr.get_geographicalVariant()).bold = True
                    if repr.get_dialect() is not None:
                        p.add_run(" [" + repr.get_dialect() + "]")
            # Part of speech in italic
            if lexical_entry.get_partOfSpeech() is not None:
                p.add_run(". ")
                p.add_run(lexical_entry.get_partOfSpeech()).italic = True
            p.add_run(".")
            # Note grammaticale
            if len(lexical_entry.find_notes(type="grammar")) != 0:
                p = document.add_paragraph()
                p.add_run("  ")
                p.add_run("[Note grammaticale :")
                for note in lexical_entry.find_notes(type="grammar", language=config.xml.regional):
                    p.add_run(" ")
                    p.add_run(note).bold = True
                try:
                    for note in lexical_entry.find_notes(type="grammar", language=config.xml.French):
                        p.add_run(" ")
                        p.add_run(note)
                except AttributeError:
                    for note in lexical_entry.find_notes(type="grammar", language=config.xml.English):
                        p.add_run(" ")
                        p.add_run(note)
                for note in lexical_entry.find_notes(type="grammar", language=config.xml.vernacular):
                    p.add_run(" ")
                    p.add_run(note)
                p.add_run("].")
            for sense in lexical_entry.get_senses():
                # Glosses
                glosses = ""
                if sense.get_senseNumber() is not None:
                    p = document.add_paragraph()
                    p.add_run("  " + sense.get_senseNumber() + ")")
                for gloss in sense.find_glosses(language=config.xml.vernacular):
                    glosses += " " + gloss + "."
                if glosses == "":
                    glosses = glosses.rstrip(".")
                try:
                    for gloss in sense.find_glosses(language=config.xml.French):
                        glosses += " " + gloss + "."
                except AttributeError:
                    for gloss in sense.find_glosses(language=config.xml.English):
                        glosses += " " + gloss + "."
                glosses = glosses.rstrip(".")
                if glosses != "" and glosses[-1] != '.' and glosses[-1] != '!' and glosses[-1] != '?':
                    glosses += "."
                p.add_run(glosses)
                # Scientific name
                if lexical_entry.get_scientific_name() is not None:
                    p.add_run(" ")
                    p.add_run(lexical_entry.get_scientific_name()).italic = True
                    p.add_run(".")
                # Examples
                for context in sense.get_contexts():
                    p = document.add_paragraph()
                    examples = ""
                    vernacular_forms = context.find_written_forms(language=config.xml.vernacular)
                    for example in vernacular_forms:
                        p.add_run("  ")
                        p.add_run(example.split('[')[0]).bold = True
                        for element in example.split('[')[1:]:
                            p.add_run('[' + element)
                    try:
                        fra_forms = context.find_written_forms(language=config.xml.French)
                        if len(vernacular_forms) != 0 and len(fra_forms) != 0:
                            p.add_run(" ")
                        for example in fra_forms:
                            p.add_run(example)
                        if len(fra_forms) != 0 and fra_forms[0][-1] != '!' and fra_forms[0][-1] != '?':
                            p.add_run(".")
                    except AttributeError:
                        pass
                # Links
                if len(lexical_entry.get_related_forms("simple link")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  Voir :").italic = True
                    for related_form in lexical_entry.get_related_forms("simple link"):
                        if related_form.get_lexical_entry() is not None:
                            # TODO : hyperlink
                            pass
                        p.add_run(" ")
                        p.add_run(related_form.get_lexeme().split('[')[0]).bold = True
                        for element in related_form.get_lexeme().split('[')[1:]:
                            p.add_run('[' + element)
                        try:
                            for written_form in related_form.find_written_forms(language=config.xml.French):
                                p.add_run(" " + written_form)
                        except AttributeError:
                            for written_form in related_form.find_written_forms(language=config.xml.English):
                                p.add_run(" " + written_form)
                    p.add_run(".")
                # Notes
                if len(lexical_entry.find_notes(type="general")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note :")
                    for note in lexical_entry.find_notes(type="general"):
                        p.add_run(" ")
                        p.add_run(note)
                    p.add_run("].")
                # Note phonologique
                if len(lexical_entry.find_notes(type="phonology")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note phonologique :")
                    for note in lexical_entry.find_notes(type="phonology"):
                        p.add_run(" ")
                        p.add_run(note)
                    p.add_run("].")
                # Note anthropologique
                if len(lexical_entry.find_notes(type="anthropology")) != 0:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run("[Note anthropologique :")
                    for note in lexical_entry.find_notes(type="anthropology"):
                        p.add_run(" ")
                        p.add_run(note)
                        p.add_run("].")
            # Handle subentries
            for related_form in lexical_entry.get_related_forms("subentry"):
                if related_form.get_lexical_entry() is not None:
                    p = document.add_paragraph()
                    p.add_run("  ")
                    p.add_run(related_form.get_lexeme().split('[')[0]).bold = True
                    for element in related_form.get_lexeme().split('[')[1:]:
                        p.add_run('[' + element.replace("GO(s)", "GOs").replace("GO(n)", "GOn").replace("WEM", "WE"))
                    for sense in related_form.get_lexical_entry().get_senses():
                        glosses = ""
                        for gloss in sense.find_glosses(language=config.xml.vernacular):
                            glosses += " " + gloss + "."
                        if glosses == "":
                            glosses = glosses.rstrip(".")
                        try:
                            for gloss in sense.find_glosses(language=config.xml.French):
                                glosses += " " + gloss + "."
                        except AttributeError:
                            for gloss in sense.find_glosses(language=config.xml.English):
                                glosses += " " + gloss + "."
                        if glosses == "":
                            glosses = glosses.rstrip(".")
                        p.add_run(glosses)
            p.add_run(EOL)
        else: # reverse
            # French gloss
            is_gloss = False
            for sense in lexical_entry.get_senses():
                for gloss in sense.find_glosses(language=config.xml.French):
                    if not is_gloss:
                        # Paragraph
                        p = document.add_paragraph()
                        # Write gloss in bold, except characters that are between brackets or square brackets
                        brackets = 0
                        bold = True
                        for c in gloss:
                            if c == '(' or c == '[':
                                # Write following characters in non-bold
                                brackets += 1
                                if brackets > 0:
                                    bold = False
                                else:
                                    bold = True
                                p.add_run(c).bold = bold
                            elif c == ')' or c == ']':
                                # Write following characters in bold
                                p.add_run(c).bold = bold
                                brackets -= 1
                                if brackets > 0:
                                    bold = False
                                else:
                                    bold = True
                            else:
                                p.add_run(c).bold = bold
                        if gloss[-1] != '?' and gloss[-1] != '!' and gloss[-1] != '.':
                            p.add_run(".")
                        p.add_run(" ")
                        is_gloss = True
            if is_gloss:
                # Scientific name
                if lexical_entry.get_scientific_name() is not None:
                    p.add_run(lexical_entry.get_scientific_name()).italic = True
                    p.add_run(". ")
                # Lexeme
                p.add_run(lexical_entry.get_lexeme())
                if lexical_entry.get_lexeme()[-1] != '?' and lexical_entry.get_lexeme()[-1] != '!' and lexical_entry.get_lexeme()[-1] != '.':
                    p.add_run(".")

## Functions to process some LaTeX fields (output)

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
def lmf2tex(lexical_entry, font):
    import output.tex as tex
    tex_entry = ""
    # lexeme, id and phonetic variants
    tex_entry += tex.format_lexeme(lexical_entry, font)
    # sound
    tex_entry += tex.format_audio(lexical_entry, font)
    # part of speech
    tex_entry += tex.format_part_of_speech(lexical_entry, font)
    # grammatical notes
    tex_entry += tex.format_notes(lexical_entry, font)
    # Order by sense number
    senses = lexical_entry.get_senses()
    senses.sort(key=lambda sense: sense.get_senseNumber(integer=True))
    for sense in senses:
        if sense.get_senseNumber() is not None:
            tex_entry += sense.get_senseNumber() + ") "
        # definition/gloss and translation
        tex_entry += tex.format_definitions(sense, font, languages=[config.xml.vernacular, config.xml.French, config.xml.national])
        # example
        tex_entry += tex.format_examples(sense, font)
        # usage note
        tex_entry += tex.format_usage_notes(sense, font)
        # encyclopedic information
        tex_entry += tex.format_encyclopedic_informations(sense, font)
        # restriction
        tex_entry += tex.format_restrictions(sense, font)
    # synonym, antonym, morphology, related form
    tex_entry += tex.format_related_forms(lexical_entry, font)
    # borrowed word
    tex_entry += tex.format_borrowed_word(lexical_entry, font)
    # etymology
    tex_entry += tex.format_etymology(lexical_entry, font)
    # paradigms
    tex_entry += tex.format_paradigms(lexical_entry, font)
    tex_entry += tex.format_paradigms(lexical_entry, font)
    # semantic domain
    tex_entry += tex.format_semantic_domains(lexical_entry, font)
    # source
    tex_entry += tex.format_source(lexical_entry, font)
    # status
    tex_entry += tex.format_status(lexical_entry, font)
    # date
    tex_entry += tex.format_date(lexical_entry, font)
    # Handle reserved characters and fonts
    tex_entry = tex.handle_reserved(tex_entry)
    tex_entry = tex.handle_quotes(tex_entry)
    tex_entry = tex.handle_fv(tex_entry, font)
    tex_entry = tex.handle_fn(tex_entry, font)
    # Special formatting
    tex_entry = tex.handle_pinyin(tex_entry)
    tex_entry = tex.handle_caps(tex_entry)
    return tex_entry + EOL
