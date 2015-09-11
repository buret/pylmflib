#! /usr/bin/env python
# -*- coding: utf-8 -*-

from config.mdf import mdf_lmf, lmf_mdf

## To define languages and fonts
import config

items=lambda lexical_entry: lexical_entry.get_lexeme()

## Functions to process some MDF fields (input)
mdf_lmf.update({})

## Functions to process some MDF fields (output)
lmf_mdf.update({})

## Functions to process some LaTeX fields (output)

## Function giving order in which information must be written in LaTeX and mapping between LMF representation and LaTeX (output)
