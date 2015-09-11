#! /usr/bin/env python

"""! @package core
"""

from core.definition import Definition
from morphosyntax.paradigm import Paradigm
from mrd.context import Context
from mrd.subject_field import SubjectField
from mrd.equivalent import Equivalent

class Sense():
    """! "Sense is a class representing one meaning of a lexical entry. The Sense class allows for hierarchical senses in that a sense may be more specific than another sense of the same lexical entry." (LMF)
    """
    def __init__(self, id=0):
        """! @brief Constructor.
        Sense instances are owned by LexicalEntry.
        @param id IDentifier. If not provided, default value is 0.
        @return A Sense instance.
        """
        self.senseNumber = None
        # ID is managed at the LexicalEntry level
        self.id = id
        ## Definition instances are owned by Sense
        # There is zero to many Definition instances per Sense
        self.definition = []
        ## Sense instances are owned by Sense
        # There is zero to many Sense instances per Sense
        self.sense = []
        ## Equivalent instances are owned by Sense
        # There is zero to many Equivalent instances per Sense
        self.equivalent = []
        ## Context instances are owned by Sense
        # There is zero to many Context instances per Sense
        self.context = []
        ## SubjectField instances are owned by Sense
        # There is zero to many SubjectField instances per Sense
        self.subject_field = []
        ## Paradigm instances are owned by Sense
        # There is zero to many Paradigm instances per Sense
        self.paradigm = []

    def __del__(self):
        """! @brief Destructor.
        Release Definition, Sense, Equivalent, Context, SubjectField, Paradigm instances.
        """
        for definition in self.definition:
            del definition
        del self.definition[:]
        for sense in self.sense:
            del sense
        del self.sense[:]
        for equivalent in self.equivalent:
            del equivalent
        del self.equivalent[:]
        for context in self.context:
            del context
        del self.context[:]
        for subject_field in self.subject_field:
            del subject_field
        del self.subject_field[:]
        for paradigm in self.paradigm:
            del paradigm
        del self.paradigm[:]

    def get_id(self):
        """! @brief IDentifier.
        @return Sense attribute 'id'.
        """
        return self.id

    def set_senseNumber(self, sense_number):
        """! @brief Set sense number.
        @param sense_number The sense number to set.
        @return Sense instance.
        """
        self.senseNumber = sense_number
        return self

    def get_senseNumber(self, integer=False):
        """! @brief Get sense number.
        @integer If True, return a numerical value.
        @return Sense attribute 'senseNumber'.
        """
        if not integer:
            return self.senseNumber
        if self.senseNumber is None:
            return 0
        return int(self.senseNumber)

    def create_definition(self):
        """! @brief Create a definition.
        @return Definition instance.
        """
        return Definition()

    def add_definition(self, definition):
        """! @brief Add a definition to the sense.
        @param definition The Definition instance to add to the sense.
        @return Sense instance.
        """
        self.definition.append(definition)
        return self

    def get_definitions(self):
        """! @brief Get all definitions maintained by the sense.
        @return A Python list of definitions.
        """
        return self.definition

    def get_last_definition(self):
        """! @brief Get the previously registered Definition instance.
        @return The last element of Sense attribute 'definition'.
        """
        if len(self.get_definitions()) >= 1:
            return self.get_definitions()[-1]

    def find_definitions(self, language):
        """! @brief Find definitions.
        This attribute is owned by Definition.
        @param language The language to consider to retrieve the definition.
        @return A Python list of found Definition attributes 'definition'.
        """
        found_definitions = []
        for definition in self.get_definitions():
            if definition.get_language() == language and definition.get_definition() is not None:
                found_definitions.append(definition.get_definition())
        return found_definitions

    def set_definition(self, definition, language=None):
        """! @brief Set definition and language.
        These attributes are owned by Definition.
        @param definition Definition.
        @param language Language of definition.
        @return Sense instance.
        """
        instance = None
        # Find if there is a Definition instance with this language without definition
        for inst in self.get_definitions():
            if inst.get_language() == language and inst.get_definition() is None:
                # Found the Definition instance to set
                instance = inst
                break
        if instance is None:
            # Set first Definition instance that has no definition nor language
            for inst in self.get_definitions():
                if inst.get_language() is None and inst.get_definition() is None:
                    # Found the Definition instance to set
                    instance = inst
                    break
        if instance is None:
            # Create a Definition instance
            instance = self.create_definition()
            self.add_definition(instance)
        instance.set_definition(definition, language)
        return self

    def find_glosses(self, language):
        """! @brief Find glosses.
        This attribute is owned by Definition.
        @param language The language to consider to retrieve the gloss.
        @return A Python list of found Definition attributes 'gloss'.
        """
        found_glosses = []
        for definition in self.get_definitions():
            if definition.get_language() == language and definition.get_gloss() is not None:
                found_glosses.append(definition.get_gloss())
        return found_glosses

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss and language.
        These attributes are owned by Definition.
        @param gloss Gloss.
        @param language Language of gloss.
        @return Sense instance.
        """
        instance = None
        # Find if there is a Definition instance with this language without gloss
        for inst in self.get_definitions():
            if inst.get_language() == language and inst.get_gloss() is None:
                # Found the Definition instance to set
                instance = inst
                break
        if instance is None:
            # Set first Definition instance that has no gloss nor language
            for inst in self.get_definitions():
                if inst.get_language() is None and inst.get_gloss() is None:
                    # Found the Definition instance to set
                    instance = inst
                    break
        if instance is None:
            # Create a Definition instance
            instance = self.create_definition()
            self.add_definition(instance)
        instance.set_gloss(gloss, language)
        return self

    def set_note(self, note, type=None, language=None):
        """! @brief Set note, note type and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param note Note to set.
        @param type Type of the note.
        @param language Language used for the note.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_note(note, type, language)
        return self

    def find_notes(self, type, language=None):
        """! @brief Find notes.
        This attribute is owned by Statement, which owned by Definition.
        @param type Type of the note to consider to retrieve the note.
        @param language If this argument is given, find note only if written in this language.
        @return A Python list of found Statement attributes 'notes'.
        """
        found_notes = []
        for definition in self.get_definitions():
            found_notes += definition.find_notes(type, language)
        return found_notes

    def set_usage_note(self, usage_note, language=None):
        """! @brief Set usage note and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param usage_note Usage note to set.
        @param language Language used for the usage note.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_usage_note(usage_note, language)
        return self

    def find_usage_notes(self, language):
        """! @brief Find usage notes.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the usage note.
        @return A Python list of found Statement attributes 'usageNote'.
        """
        found_notes = []
        for definition in self.get_definitions():
            found_notes += definition.find_usage_notes(language)
        return found_notes

    def set_encyclopedic_information(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language used for the encyclopedic information.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_encyclopedic_information(encyclopedic_information, language)
        return self

    def find_encyclopedic_informations(self, language):
        """! @brief Find encyclopedic informations.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the encyclopedic informations.
        @return A Python list of found Statement attributes 'encyclopedicInformation'.
        """
        found_informations = []
        for definition in self.get_definitions():
            found_informations += definition.find_encyclopedic_informations(language)
        return found_informations

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction and language.
        These attributes are owned by Statement, which is owned by Definition.
        @param restriction Restriction to set.
        @param language Language used for the restriction.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instances, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_restriction(restriction, language)
        return self

    def find_restrictions(self, language):
        """! @brief Find restrictions.
        This attribute is owned by Statement, which owned by Definition.
        @param language Language to consider to retrieve the restriction.
        @return A Python list of found Statement attributes 'restriction'.
        """
        found_restrictions = []
        for definition in self.get_definitions():
            found_restrictions += definition.find_restrictions(language)
        return found_restrictions

    def set_borrowed_word(self, borrowed_word):
        """! @brief Set source language (in English).
        Attribute 'borrowedWord' is owned by Statement, which is owned by Definition.
        @param borrowed_word Source language.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_borrowed_word(borrowed_word)
        return self

    def get_borrowed_word(self):
        """! @brief Get source language (in English).
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'borrowedWord'.
        """
        for definition in self.get_definitions():
            if definition.get_borrowed_word() is not None:
                # Get borrowed word if any
                return definition.get_borrowed_word()

    def set_written_form(self, written_form):
        """! @brief Set loan word.
        Attribute 'writtenForm' is owned by Statement, which is owned by Definition.
        @param written_form Loan word.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_written_form(written_form)
        return self

    def get_written_form(self):
        """! @brief Get loan word.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'writtenForm'.
        """
        for definition in self.get_definitions():
            if definition.get_written_form() is not None:
                # Get loan word if any
                return definition.get_written_form()

    def set_etymology(self, etymology):
        """! @brief Set etymology.
        Attribute 'etymology' is owned by Statement, which is owned by Definition.
        @param etymology Etymology.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology(etymology)
        return self

    def get_etymology(self):
        """! @brief Get etymology.
        This attribute is owned by Statement, which is owned by Definition.
        @return The first found Statement attribute 'etymology'.
        """
        for definition in self.get_definitions():
            if definition.get_etymology() is not None:
                return definition.get_etymology()

    def set_etymology_comment(self, etymology_comment, term_source_language=None):
        """! @brief Set etymology comment and language.
        Attributes 'etymologyComment' and 'termSourceLanguage' are owned by Statement, which is owned by Definition.
        @param etymology_comment Etymology comment.
        @param term_source_language Language of the comment.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_comment(etymology_comment, term_source_language)
        return self

    def get_etymology_comment(self, term_source_language=None):
        """! @brief Get etymology comment.
        This attribute is owned by Statement, which is owned by Definition.
        @param term_source_language The language of the etymology comment to retrieve.
        @return The first found Statement attribute 'etymologyComment'.
        """
        for definition in self.get_definitions():
            if definition.get_etymology_comment(term_source_language) is not None:
                return definition.get_etymology_comment(term_source_language)

    def get_term_source_language(self):
        """! @brief Get language used for the etymology comment.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'termSourceLanguage'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology comment language
        if definition is not None:
            return definition.get_term_source_language()

    def set_etymology_gloss(self, etymology_gloss):
        """! @brief Set etymology gloss.
        Attribute 'etymologyGloss' is owned by Statement, which is owned by Definition.
        @param etymology_gloss Etymology gloss.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_gloss(etymology_gloss)
        return self

    def get_etymology_gloss(self):
        """! @brief Get etymology gloss.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'etymologyGloss'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology gloss
        if definition is not None:
            return definition.get_etymology_gloss()

    def set_etymology_source(self, etymology_source):
        """! @brief Set etymology source.
        Attribute 'etymologySource' is owned by Statement, which is owned by Definition.
        @param etymology_source Etymology source.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_etymology_source(etymology_source)
        return self

    def get_etymology_source(self):
        """! @brief Get etymology source.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'etymologySource'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get etymology source
        if definition is not None:
            return definition.get_etymology_source()

    def set_scientific_name(self, scientific_name):
        """! @brief Set scientific name.
        Attribute 'scientificName' is owned by Statement, which is owned by Definition.
        @param scientific_name Scientific name.
        @return Sense instance.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is no Definition instance, create and add one
        if definition is None:
            definition = self.create_definition()
            self.add_definition(definition)
        definition.set_scientific_name(scientific_name)
        return self

    def get_scientific_name(self):
        """! @brief Get scientific name.
        This attribute is owned by Statement, which is owned by Definition.
        @return Statement attribute 'scientificName'.
        """
        # Get the last Definition instance if any
        definition = self.get_last_definition()
        # If there is a Definition instance, get scientific name
        if definition is not None:
            return definition.get_scientific_name()

    def create_paradigm(self):
        """! @brief Create a paradigm.
        @return Paradigm instance.
        """
        return Paradigm()

    def add_paradigm(self, paradigm):
        """! @brief Add a paradigm to the sense.
        @param paradigm The Paradigm instance to add to the sense.
        @return Sense instance.
        """
        self.paradigm.append(paradigm)
        return self

    def get_paradigms(self):
        """! @brief Get all paradigms maintained by the sense.
        @return A Python list of paradigms.
        """
        return self.paradigm

    def get_last_paradigm(self):
        """! @brief Get the previously registered Paradigm instance.
        @return The last element of Sense attribute 'paradigm'.
        """
        if len(self.get_paradigms()) >= 1:
            return self.get_paradigms()[-1]

    def set_paradigm_label(self, paradigm_label):
        """! @brief Set paradigm label.
        Attribute 'paradigmLabel' is owned by Paradigm.
        @param paradigm_label Paradigm label.
        @return Sense instance.
        """
        # Create a paradigm instance, set it, and add it to the list
        self.add_paradigm(self.create_paradigm().set_paradigmLabel(paradigm_label))
        return self

    def set_paradigm_form(self, paradigm_form, language=None):
        """! @brief Set paradigm form and language.
        Attributes 'paradigm' and 'language' are owned by Paradigm.
        @param paradigm_form Paradigm form.
        @param language Language used for the paradigm form.
        @return Sense instance.
        """
        paradigm_label = None
        # Get the last Paradigm instance if any
        paradigm = self.get_last_paradigm()
        # If there is a Paradigm instance, check if the paradigm form or language are already set
        if paradigm is not None:
            # Save the paradigm label
            paradigm_label = paradigm.get_paradigmLabel()
            if paradigm.get_paradigm() is not None or (paradigm.get_language() is not None and paradigm.get_language() != language):
                # A new paradigm instance has to be created
                paradigm = None
        if paradigm is None:
            # Create a paradigm instance and add it to the list
            paradigm = self.create_paradigm()
            self.add_paradigm(paradigm)
        paradigm.set_paradigm(paradigm_form)
        if language is not None:
            paradigm.set_language(language)
        # Report previous paradigm label if needed
        if paradigm_label is not None and paradigm.get_paradigmLabel() is None:
            paradigm.set_paradigmLabel(paradigm_label)
        return self

    def set_morphology(self, morphology):
        """! @brief Set morphology.
        Attribute 'morphology' is owned by Paradigm.
        @param morphology Morphology.
        @return Sense instance.
        """
        paradigm = None
        # Get the first Paradigm instance that has no morphology
        for item in self.get_paradigms():
            if item.get_morphology() is None:
                paradigm = item
                break
        if paradigm is None:
            # Create a paradigm instance and add it to the list
            paradigm = self.create_paradigm()
            self.add_paradigm(paradigm)
        paradigm.set_morphology(morphology)
        return self

    def create_and_add_context(self, reference=None):
        """! @brief Create a context and add it to the list.
        @param reference The context reference to set. If not provided, default value is None.
        @return Context instance.
        """
        context = Context(reference)
        self.context.append(context)
        return context

    def get_contexts(self):
        """! @brief Get all contexts maintained by the sense.
        @return A Python list of contexts.
        """
        return self.context

    def get_last_context(self):
        """! @brief Get the previously registered Context instance.
        @return The last element of Sense attribute 'context'.
        """
        if len(self.get_contexts()) >= 1:
            return self.get_contexts()[-1]

    def create_example(self, reference=None):
        """! @brief Create a Context instance and set its reference.
        Attribute 'targets' is owned by Context.
        @param reference The example reference to set. If not provided, default value is None.
        @return Sense instance.
        """
        self.create_and_add_context(reference).set_type("example")
        return self

    def create_and_add_example(self, written_form, language=None, script_name=None):
        """! @brief Set written form, language and script of a new Context instance.
        Attributes 'writtenForm', 'language' and 'scriptName' are owned by TextRepresentation, which is owned by Context.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @param script_name The name of the script used to write the example, e.g. devanagari.
        @return Sense instance.
        """
        # Get the last Context instance if any
        context = self.get_last_context()
        # If there is no Context instance, create and add one
        if context is None or len(context.get_text_representations()) != 0:
            context = self.create_and_add_context().set_type("example")
        context.set_written_form(written_form, language, script_name)
        return self

    def add_example(self, written_form, language=None, script_name=None):
        """! @brief Set written form, language and script of an existing Context instance.
        Attributes 'writtenForm', 'language' and 'scriptName' are owned by TextRepresentation, which is owned by Context.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @param script_name The name of the script used to write the example, e.g. devanagari.
        @return Sense instance.
        """
        # Get the last Context instance if any
        context = self.get_last_context()
        # If there is no Context instance, create and add one
        if context is None:
            context = self.create_and_add_context().set_type("example")
        context.set_written_form(written_form, language, script_name)
        return self

    def set_example_comment(self, comment):
        """! @brief Set comment of an existing Context instance.
        Attribute 'comment' is owned by TextRepresentation, which is owned by Context.
        @param comment The comment to set.
        @return Sense instance.
        """
        # Get the last Context instance if any
        context = self.get_last_context()
        # If there is no Context instance, create and add one
        if context is None:
            context = self.create_and_add_context().set_type("example")
        context.set_comment(comment)
        return self

    def create_and_add_subject_field(self):
        """! @brief Create a subject field and add it to the list.
        @return SubjectField instance.
        """
        subject_field = SubjectField()
        self.subject_field.append(subject_field)
        return subject_field

    def get_subject_fields(self):
        """! @brief Get all subject fields maintained by the sense.
        @return A Python list of subject fields.
        """
        return self.subject_field

    def set_semantic_domain(self, semantic_domain, language=None):
        """! @brief Create a SubjectField instance and set its semantic domain and language.
        Attributes 'semanticDomain' and 'language' are owned by SubjectField.
        @param semantic_domain The semantic domain to set.
        @param language Language used to describe the semantic domain.
        @return Sense instance.
        """
        self.create_and_add_subject_field().set_semanticDomain(semantic_domain, language)
        return self

    def create_and_add_equivalent(self):
        """! @brief Create an equivalent and add it to the list.
        @return Equivalent instance.
        """
        equivalent = Equivalent()
        self.equivalent.append(equivalent)
        return equivalent

    def get_equivalents(self):
        """! @brief Get all equivalents maintained by the sense.
        @return A Python list of equivalents.
        """
        return self.equivalent

    def set_translation(self, translation, language=None):
        """! @brief Create an Equivalent instance and set its translation and language.
        Attributes 'translation' and 'language' are owned by Equivalent.
        @param translation The translation to set.
        @param language Language used for the translation.
        @return Sense instance.
        """
        self.create_and_add_equivalent().set_translation(translation, language)
        return self

    def get_translations(self, language=None):
        """! @brief Get all translations.
        This attribute is owned by Equivalent.
        @param language If this argument is given, get only translations that are described using this language.
        @return A Python list of filtered Equivalent attributes 'translation'.
        """
        translations = []
        for equivalent in self.get_equivalents():
            if equivalent.get_translation(language) is not None:
                translations.append(equivalent.get_translation(language))
        return translations
