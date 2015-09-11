#! /usr/bin/env python

## Importing the modules executes the tests
# Config Package
import test_config_xml
# Core Package
import test_core_definition, test_core_form_representation, test_core_form, test_core_global_information, test_core_lexical_entry, test_core_lexical_resource, test_core_lexicon, test_core_representation, test_core_sense, test_core_statement, test_core_text_representation
# Input
import test_input_mdf, test_input_xml_lmf
# Morphology
import test_morphology_component, test_morphology_lemma, test_morphology_list_of_components, test_morphology_related_form, test_morphology_stem, test_morphology_word_form
# Morphosyntax
import test_morphosyntax_paradigm
# MRD
import test_mrd_context, test_mrd_equivalent, test_mrd_subject_field
# Output
import test_output_mdf, test_output_tex, test_output_xml_lmf
# Resources
import test_resources_audio, test_resources_human_resource, test_resources_material, test_resources_picture, test_resources_resource, test_resources_speaker, test_resources_video
# Utils
import test_utils_attr, test_utils_error_handling, test_utils_io, test_utils_log, test_utils_xml_format
