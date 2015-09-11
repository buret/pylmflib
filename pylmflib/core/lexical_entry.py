#! /usr/bin/env python

"""! @package core
"""

from morphology.lemma import Lemma
from morphology.related_form import RelatedForm
from morphology.word_form import WordForm
from common.range import partOfSpeech_range
from config.mdf import ps_partOfSpeech
from utils.attr import check_attr_type, check_attr_range
from core.sense import Sense
from morphology.list_of_components import ListOfComponents

class LexicalEntry():
    """! "Lexical Entry is a class representing a lexeme in a given language and is a container for managing the Form and Sense classes. A Lexical Entry instance can contain one to many different forms and can have from zero to many different senses." (LMF)
    """
    def __init__(self, id='0'):
        """! @brief Constructor.
        LexicalEntry instances are owned by Lexicon.
        @param id Unique IDentifier. If not provided, default value is 0.
        @return A LexicalEntry instance.
        """
        self.homonymNumber = None
        self.status = None
        self.date = None
        self.partOfSpeech = None
        self.independentWord = None
        self.bibliography = None
        ## UID is managed at the Lexicon level
        self.id = id
        ## Sense instances are owned by LexicalEntry
        # There is zero to many Sense instances per LexicalEntry
        self.sense = []
        ## Lemma instance is owned by LexicalEntry
        # There is one Lemma instance by LexicalEntry instance
        self.lemma = None # lemmatized form
        ## RelatedForm instances are owned by LexicalEntry
        # There is zero to many RelatedForm instances per LexicalEntry
        self.related_form = []
        ## WordForm instances are owned by LexicalEntry
        # There is zero to many WordForm instances per LexicalEntry
        self.word_form = []
        ## Stem instances are owned by LexicalEntry
        # There is zero to many Stem instances per LexicalEntry
        self.stem = [] # ordered list
        ## ListOfComponents instance is owned by LexicalEntry
        # There is zero or one ListOfComponents instance per LexicalEntry
        self.list_of_components = None
        # Speaker id
        self.targets = None
        ## Pointer to an existing Speaker
        # There is one Speaker pointer per LexicalEntry instance
        self.__speaker = None

    def __del__(self):
        """! @brief Destructor.
        Release Sense, Lemma, RelatedForm, WordForm, Stem, ListOfComponents instances.
        """
        for sense in self.sense:
            del sense
        del self.sense[:]
        for related_form in self.related_form:
            del related_form
        del self.related_form[:]
        for word_form in self.word_form:
            del word_form
        del self.word_form[:]
        for stem in self.stem:
            del stem
        del self.stem[:]
        if self.lemma is not None:
            del self.lemma
        if self.list_of_components is not None:
            del self.list_of_components
        # Decrement the reference count on pointed objects
        self.__speaker = None

    def set_partOfSpeech(self, part_of_speech, range=partOfSpeech_range, mapping=ps_partOfSpeech):
        """! @brief Set grammatical category.
        @param part_of_speech The grammatical category to set.
        @param range A Python set giving all possible values of part of speech LMF attribute.
        @param mapping A Python dictionary giving the mapping between MDF and LMF values.
        @return LexicalEntry instance.
        """
        error_msg = "Part of speech value '%s' encountered for lexeme '%s' is not allowed" % (part_of_speech.encode('utf8'), self.get_lexeme().encode('utf8'))
        # Check part of speech type
        check_attr_type(part_of_speech, [str, unicode], error_msg)
        # Check range of part of speech value (also try with converted value from MDF to LMF)
        value = check_attr_range(part_of_speech.encode('utf8'), range, error_msg, mapping)
        self.partOfSpeech = value
        return self

    def get_partOfSpeech(self):
        """! @brief Get grammatical category.
        @return LexicalEntry attribute 'partOfSpeech'.
        """
        return self.partOfSpeech

    def set_status(self, status):
        """! @brief Set lexical entry status.
        @param status The status to set.
        @return LexicalEntry instance.
        """
        self.status = status
        return self

    def get_status(self):
        """! @brief Get lexical entry status.
        @return LexicalEntry attribute 'status'.
        """
        return self.status

    def set_date(self, date):
        """! @brief Set lexical entry date.
        @param status The date to set.
        @return LexicalEntry instance.
        """
        self.date = date
        return self

    def get_date(self):
        """! @brief Get lexical entry date.
        @return LexicalEntry attribute 'date'.
        """
        return self.date

    def set_homonymNumber(self, homonym_number):
        """! @brief Set lexical entry homonym number.
        @param homonym_number The homonym number to set.
        @return LexicalEntry instance.
        """
        self.homonymNumber = homonym_number
        return self

    def get_homonymNumber(self):
        """! @brief Get lexical entry homonym number.
        @return LexicalEntry attribute 'homonymNumber'.
        """
        return self.homonymNumber

    def set_bibliography(self, bibliography):
        """! @brief Set lexical entry bibliography.
        @param bibliography The bibliography to set.
        @return LexicalEntry instance.
        """
        self.bibliography = bibliography
        return self

    def get_bibliography(self):
        """! @brief Get lexical entry bibliography.
        @return LexicalEntry attribute 'bibliography'.
        """
        return self.bibliography

    def set_independentWord(self, independent_word):
        """! @brief Set lexical entry independent word indication.
        @param independent_word The independent word indication to set.
        @return LexicalEntry instance.
        """
        error_msg = "Independent word '%s' encountered for lexeme '%s' is not allowed" % (str(independent_word), self.get_lexeme())
        check_attr_type(independent_word, bool, error_msg)
        self.independentWord = independent_word
        return self

    def get_independentWord(self):
        """! @brief Get lexical entry independent word indication.
        @return LexicalEntry attribute 'independentWord'.
        """
        return self.independentWord

    def get_id(self):
        """! @brief Get Unique IDentifier.
        @return LexicalEntry attribute 'id' followed by the homonym number.
        """
        homonymNumber = self.get_homonymNumber()
        if homonymNumber is None:
            homonymNumber = 1
        return self.id + str(homonymNumber)

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @param lexeme The lexeme to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_lexeme(lexeme)
        return self

    def get_lexeme(self):
        """! @brief Get lexeme.
        Attribute 'lexeme' is owned by Lemma.
        @return Lemma attribute 'lexeme' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_lexeme()

    def create_related_form(self, lexeme, semantic_relation):
        """! @brief Create a related form.
        @param lexeme Related lexeme.
        @param semantic_relation The semantic relation existing between this lexical entry and the related lexeme to create.
        @return RelatedForm instance.
        """
        return RelatedForm(lexeme).set_semanticRelation(semantic_relation)

    def add_related_form(self, related_form):
        """! @brief Add a related form to the lexical entry.
        @param related_form The RelatedForm instance to add to the lexical entry.
        @return LexicalEntry instance.
        """
        self.related_form.append(related_form)
        return self

    def create_and_add_related_form(self, lexeme, semantic_relation):
        """! @brief Create and add a related form to the lexical entry.
        @param lexeme Related lexeme.
        @param semantic_relation The semantic relation existing between this lexical entry and the related lexeme to create.
        @return LexicalEntry instance.
        """
        # Check if this related form already exists
        for related_form in self.get_related_forms():
            if related_form.get_lexeme() == lexeme:
                return self
        self.related_form.append(RelatedForm(lexeme).set_semanticRelation(semantic_relation))
        return self

    def find_related_forms(self, semantic_relation):
        """! @brief Find related lexemes.
        This attribute is owned by RelatedForm.
        @param semantic_relation The semantic relation to consider to retrieve the related form.
        @return A Python list of found RelatedForm attributes 'targets'.
        """
        found_lexemes = []
        for related_form in self.get_related_forms():
            if related_form.get_semanticRelation() == semantic_relation:
                found_lexemes.append(related_form.get_lexeme())
        return found_lexemes

    def get_related_forms(self, semantic_relation=None):
        """! @brief Get all related forms maintained by the lexical entry.
        @param semantic_relation The semantic relation to consider to retrieve the related forms.
        @return A Python set of related forms.
        """
        if semantic_relation is None:
            return self.related_form
        found_forms = []
        for related_form in self.related_form:
            if related_form.get_semanticRelation() == semantic_relation:
                found_forms.append(related_form)
        return found_forms

    def get_last_related_form(self, semantic_relation=None):
        """! @brief Get the previously registered related form.
        @param semantic_relation The semantic relation to consider to retrieve the last related form.
        @return The last element of LexicalEntry attribute 'related_form' that matches with semantic relation if provided.
        """
        if len(self.get_related_forms(semantic_relation)) >= 1:
            return self.get_related_forms()[-1]

    def get_form_representations(self):
        """! @brief Get all form representations maintained by the lemma.
        Attribute 'form_representation' is owned by Lemma.
        @return Lemma attribute 'form_representation' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_form_representations()

    def set_variant_form(self, variant_form, type="unspecified"):
        """! @brief Set variant form and type.
        Attributes 'variantForm' and 'type' are owned by FormRepresentation, which is owned by Lemma.
        @param variant_form Variant form.
        @param type Type of variant, in range 'type_variant_range' defined in 'common/range.py'.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_variant_form(variant_form, type)
        return self

    def get_variant_forms(self, type="unspecified"):
        """! @brief Get all variant forms of specified type.
        Attribute 'variantForm' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'variantForm' if type matches.
        """
        if self.lemma is not None:
            return self.lemma.get_variant_forms(type)

    def set_variant_comment(self, comment, language=None):
        """! @brief Set variant comment and language.
        Attributes 'comment' and 'language' are owned by FormRepresentation, which is owned by Lemma.
        @param comment Variant comment.
        @param language Language of comment.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_variant_comment(comment, language)
        return self

    def set_tone(self, tone):
        """! @brief Set tone.
        Attribute 'tone' is owned by FormRepresentation, which is owned by Lemma.
        @param tone The tone to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_tone(tone)
        return self

    def get_tones(self):
        """! @brief Get all tones.
        Attribute 'tone' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'tone' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_tones()

    def set_geographical_variant(self, geographical_variant):
        """! @brief Set geographical variant.
        Attribute 'geographicalVariant' is owned by FormRepresentation, which is owned by Lemma.
        @param geographical_variant The geographical variant to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_geographical_variant(geographical_variant)
        return self

    def set_phonetic_form(self, phonetic_form, script_name=None):
        """! @brief Set phonetic form.
        Attribute 'phoneticForm' is owned by FormRepresentation, which is owned by Lemma.
        @param phonetic_form The phonetic form to set.
        @param script_name The name of the script used to write the phonetic form, e.g. pinyin.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_phonetic_form(phonetic_form, script_name)
        return self

    def get_phonetic_forms(self, script_name=None):
        """! @brief Get all phonetic forms.
        Attribute 'phoneticForm' is owned by FormRepresentation, which is owned by Lemma.
        @param script_name If provided, get only phonetic forms that are written using this script.
        @return A Python list of FormRepresentation attributes 'phoneticForm' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_phonetic_forms(script_name)

    def set_contextual_variation(self, contextual_variation):
        """! @brief Set contextual variation.
        Attribute 'contextualVariation' is owned by FormRepresentation, which is owned by Lemma.
        @param contextual_variation The contextual variation to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_contextual_variation(contextual_variation)
        return self

    def get_contextual_variations(self):
        """! @brief Get all contextual variations.
        Attribute 'contextualVariation' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'contextualVariation' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_contextual_variations()

    def set_spelling_variant(self, spelling_variant):
        """! @brief Set spelling variant.
        Attribute 'spellingVariant' is owned by FormRepresentation, which is owned by Lemma.
        @param spelling_variant The spelling variant to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_spelling_variant(spelling_variant)
        return self

    def get_spelling_variants(self):
        """! @brief Get all spelling variants.
        Attribute 'spellingVariant' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'spellingVariant' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_spelling_variants()

    def set_citation_form(self, citation_form, script_name=None):
        """! @brief Set citation form.
        Attribute 'citationForm' is owned by FormRepresentation, which is owned by Lemma.
        @param citation_form The citation form to set.
        @param script_name The name of the script used to write the citation form, e.g. devanagari.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_citation_form(citation_form, script_name)
        return self

    def get_citation_forms(self, script_name=None):
        """! @brief Get all citation forms.
        Attribute 'citationForm' is owned by FormRepresentation, which is owned by Lemma.
        @param script_name If provided, get only citation forms that are written using this script.
        @return A Python list of FormRepresentation attributes 'citationForm' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_citation_forms(script_name)

    def set_dialect(self, dialect):
        """! @brief Set dialect.
        Attribute 'dialect' is owned by FormRepresentation, which is owned by Lemma.
        @param dialect The dialect to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_dialect(dialect)
        return self

    def set_transliteration(self, transliteration):
        """! @brief Set transliteration.
        Attribute 'transliteration' is owned by FormRepresentation, which is owned by Lemma.
        @param transliteration The transliteration to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_transliteration(transliteration)
        return self

    def get_transliterations(self):
        """! @brief Get all transliterations.
        Attribute 'transliteration' is owned by FormRepresentation, which is owned by Lemma.
        @return A Python list of FormRepresentation attributes 'transliteration' if any.
        """
        if self.lemma is not None:
            return self.lemma.get_transliterations()

    def set_script_name(self, script_name):
        """! @brief Set script name.
        Attribute 'scriptName' is owned by FormRepresentation, which is owned by Lemma.
        @param script_name The script name to set.
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_script_name(script_name)
        return self

    def create_sense(self, id=0):
        """! @brief Create a sense.
        @param id Identifier.
        @return Sense instance.
        """
        return Sense(id)

    def add_sense(self, sense):
        """! @brief Add a sense to the lexical entry.
        @param sense The Sense instance to add to the lexical entry.
        @return LexicalEntry instance.
        """
        self.sense.append(sense)
        return self

    def create_and_add_sense(self, sense_number):
        """! @brief Create and add a sense to the lexical entry.
        @param sense_number Number of the sense to add.
        @return LexicalEntry instance.
        """
        id = self.get_id() + "_" + str(sense_number)
        self.add_sense(self.create_sense(id).set_senseNumber(sense_number))
        return self

    def get_senses(self):
        """! @brief Get all senses maintained by the lexical entry.
        @return LexicalEntry attribute 'sense'.
        """
        return self.sense

    def get_last_sense(self):
        """! @brief Get the previously registered sense.
        @return The last element of LexicalEntry attribute 'sense'.
        """
        if len(self.get_senses()) >= 1:
            return self.get_senses()[-1]

    def set_definition(self, definition, language=None):
        """! @brief Set definition and language.
        Attributes 'definition' and 'language' are owned by Definition, which is owned by Sense.
        @param definition Definition.
        @param language Language of definition.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_definition(definition, language)
        return self

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss and language.
        Attributes 'gloss' and 'language' are owned by Definition, which is owned by Sense.
        @param gloss Gloss.
        @param language Language of gloss.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_gloss(gloss, language)
        return self

    def set_note(self, note, type=None, language=None):
        """! @brief Set note, type and language.
        Attributes 'note', 'noteType' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param note Note to set.
        @param type Type of the note.
        @param language Language of the note.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_note(note, type, language)
        return self

    def find_notes(self, type, language=None):
        """! @brief Find notes.
        This attribute is owned by Statement, which owned by Definition, itself owned by Sense.
        @param type Type of the note to consider to retrieve the note.
        @param language If this argument is given, find note only if written in this language.
        @return A Python list of found Statement attributes 'notes'.
        """
        found_notes = []
        for sense in self.get_senses():
            found_notes += sense.find_notes(type, language)
        return found_notes

    def set_usage_note(self, usage_note, language=None):
        """! @brief Set usage note and language.
        Attributes 'usageNote' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param usage_note Usage note to set.
        @param language Language of the usage note.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_usage_note(usage_note, language)
        return self

    def set_encyclopedic_information(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information and language.
        Attributes 'encyclopedicInformation' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language of the encyclopedic information.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_encyclopedic_information(encyclopedic_information, language)
        return self

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction and language.
        Attributes 'restriction' and 'language' are owned by Statement, which owned by Definition, itself owned by Sense.
        @param restriction Restriction to set.
        @param language Language of the restriction.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instances, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_restriction(restriction, language)
        return self

    def set_borrowed_word(self, borrowed_word):
        """! @brief Set source language (in English).
        Attribute 'borrowedWord' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param borrowed_word Source language.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_borrowed_word(borrowed_word)
        return self

    def get_borrowed_word(self):
        """! @brief Get source language (in English).
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'borrowedWord'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get source language
        if sense is not None:
            return sense.get_borrowed_word()

    def set_written_form(self, written_form):
        """! @brief Set loan word.
        Attribute 'writtenForm' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param written_form Loan word.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_written_form(written_form)
        return self

    def get_written_form(self):
        """! @brief Get loan word.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'writtenForm'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get loan word
        if sense is not None:
            return sense.get_written_form()

    def set_etymology(self, etymology):
        """! @brief Set etymology.
        Attribute 'etymology' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology Etymology.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology(etymology)
        return self

    def get_etymology(self):
        """! @brief Get etymology.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return The first found Statement attribute 'etymology'.
        """
        for sense in self.get_senses():
            if sense.get_etymology() is not None:
                return sense.get_etymology()

    def set_etymology_comment(self, etymology_comment, term_source_language=None):
        """! @brief Set etymology comment and language.
        Attributes 'etymologyComment' and 'termSourceLanguage' are owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_comment Etymology comment.
        @param term_source_language Language of the comment.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_comment(etymology_comment, term_source_language)
        return self

    def get_etymology_comment(self, term_source_language=None):
        """! @brief Get etymology comment.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param term_source_language The language of the etymology comment to retrieve.
        @return The first found Statement attribute 'etymologyComment'.
        """
        for sense in self.get_senses():
            if sense.get_etymology_comment(term_source_language) is not None:
                return sense.get_etymology_comment(term_source_language)

    def get_term_source_language(self):
        """! @brief Get language used for the etymology comment.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'termSourceLanguage'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology comment language
        if sense is not None:
            return sense.get_term_source_language()

    def set_etymology_gloss(self, etymology_gloss):
        """! @brief Set etymology gloss.
        Attribute 'etymologyGloss' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_gloss Etymology gloss.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_gloss(etymology_gloss)
        return self

    def get_etymology_gloss(self):
        """! @brief Get etymology gloss.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'etymologyGloss'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology gloss
        if sense is not None:
            return sense.get_etymology_gloss()

    def set_etymology_source(self, etymology_source):
        """! @brief Set etymology source.
        Attribute 'etymologySource' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param etymology_source Etymology source.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_etymology_source(etymology_source)
        return self

    def get_etymology_source(self):
        """! @brief Get etymology source.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'etymologySource'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get etymology source
        if sense is not None:
            return sense.get_etymology_source()

    def set_scientific_name(self, scientific_name):
        """! @brief Set scientific_name.
        Attribute 'scientificName' is owned by Statement, which is owned by Definition, itself owned by Sense.
        @param scientific_name Scientific name.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_scientific_name(scientific_name)
        return self

    def get_scientific_name(self):
        """! @brief Get scientific name.
        This attribute is owned by Statement, which is owned by Definition, itself owned by Sense.
        @return Statement attribute 'scientificName'.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is a Sense instance, get scientific name
        if sense is not None:
            return sense.get_scientific_name()

    def create_word_form(self):
        """! @brief Create a word form.
        @return WordForm instance.
        """
        return WordForm()

    def add_word_form(self, word_form):
        """! @brief Add a word form to the lexical entry.
        @param word_form The WordForm instance to add to the lexical entry.
        @return LexicalEntry instance.
        """
        self.word_form.append(word_form)
        return self

    def get_word_forms(self):
        """! @brief Get all word forms maintained by the lexical entry.
        @return A Python list of word forms.
        """
        return self.word_form

    def set_paradigm(self, written_form, script_name=None, person=None, anymacy=None, grammatical_number=None, clusivity=None):
        """! @brief Set paradigm.
        Attributes 'writtenForm' and 'scriptName' are owned by FormRepresentation, wich is owned by WordForm.
        Attributes 'person', 'anymacy', 'grammaticalNumber' and 'clusivity' are owned by WordForm.
        @param written_form The paradigm to set.
        @param script_name Script used for the written form.
        @param person Person, e.g. first person.
        @param anymacy Anymacy, e.g. animate or inanimate.
        @param grammatical_number Grammatical number, e.g. singular or plural.
        @param clusivity Clusivity, e.g. inclusive or exclusive.
        @return LexicalEntry instance.
        """
        word_form = None
        # Find corresponding word form
        for form in self.get_word_forms():
            if form.get_person() == person and form.get_anymacy() == anymacy and form.get_grammaticalNumber() == grammatical_number and form.get_clusivity() == clusivity:
                # Add a paradigm as a written form to an existing word form
                word_form = form
                break
        if word_form is None:
            # Create a WordForm instance
            word_form = self.create_word_form()
            self.add_word_form(word_form)
            if person is not None:
                word_form.set_person(person)
            if anymacy is not None:
                word_form.set_anymacy(anymacy)
            if grammatical_number is not None:
                word_form.set_grammaticalNumber(grammatical_number)
            if clusivity is not None:
                word_form.set_clusivity(clusivity)
        word_form.set_written_form(written_form, script_name)
        return self

    def find_paradigms(self, script_name=None, person=None, anymacy=None, grammatical_number=None, clusivity=None):
        """! @brief Find paradigms.
        Attribute 'scriptName' is owned by FormRepresentation, wich is owned by WordForm.
        Attributes 'person', 'anymacy', 'grammaticalNumber' and 'clusivity' are owned by WordForm.
        Attribute 'writtenForm' to retrieve is owned by FormRepresentation, wich is owned by WordForm.
        @param script_name If this argument is given, get paradigm written form only if written using this script.
        @param person Person, e.g. first person.
        @param anymacy Anymacy, e.g. animate or inanimate.
        @param grammatical_number Grammatical number, e.g. singular or plural.
        @param clusivity Clusivity, e.g. inclusive or exclusive.
        @return A Python list of FormRepresentation attributes 'writtenForm'.
        """
        written_forms = []
        # Find corresponding word form
        for form in self.get_word_forms():
            if form.get_person() == person and form.get_anymacy() == anymacy and form.get_grammaticalNumber() == grammatical_number and form.get_clusivity() == clusivity:
                written_forms += form.get_written_forms(script_name)
        return written_forms

    def set_paradigm_label(self, paradigm_label):
        """! @brief Set paradigm label.
        Attribute 'paradigmLabel' is owned by Paradigm, which is owned by Sense.
        @param paradigm_label Paradigm label.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_paradigm_label(paradigm_label)
        return self

    def set_paradigm_form(self, paradigm, language=None):
        """! @brief Set paradigm form.
        Attribute 'paradigm' is owned by Paradigm, which is owned by Sense.
        @param paradigm Paradigm form.
        @param language Language of the paradigm form.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_paradigm_form(paradigm, language)
        return self

    def set_morphology(self, morphology):
        """! @brief Set morphology.
        Attribute 'morphology' is owned by Paradigm, which is owned by Sense.
        @param morphology Morphology.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_morphology(morphology)
        return self

    def get_paradigms(self):
        """! @brief Get all paradigms.
        This attribute is owned by Sense.
        @return Sense attribute 'paradigm'.
        """
        paradigms = []
        for sense in self.get_senses():
            paradigms += sense.get_paradigms()
        return paradigms

    def get_morphologies(self):
        """! @brief Get all morphologies.
        This attribute is owned by Paradigm, which is owned by Sense.
        @return A Python list of Paradigm attributes 'morphology'.
        """
        morphologies = []
        for sense in self.get_senses():
            for paradigm in sense.get_paradigms():
                if paradigm.get_morphology() is not None:
                    morphologies.append(paradigm.get_morphology())
        return morphologies

    def create_example(self, reference=None):
        """! @brief Create a context.
        Attribute 'targets' is owned by Context, itself owend by Sense.
        @param reference The example reference to set. If not provided, default value is None.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.create_example(reference)
        return self

    def create_and_add_example(self, written_form, language=None, script_name=None):
        """! @brief Add an example to a new context and set its written form, language and script.
        Attributes 'writtenForm', 'language' and 'scriptName' are owned by TextRepresentation, which is owned by Context, itself owend by Sense.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @param script_name The name of the script used to write the example, e.g. devanagari.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.create_and_add_example(written_form, language, script_name)
        return self

    def add_example(self, written_form, language=None, script_name=None):
        """! @brief Add an example to an existing context and set its written form, language and script.
        Attributes 'writtenForm', 'language' and 'scriptName' are owned by TextRepresentation, which is owned by Context, itself owend by Sense.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @param script_name The name of the script used to write the example, e.g. devanagari.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.add_example(written_form, language, script_name)
        return self

    def set_example_comment(self, comment):
        """! @brief Set comment of an existing example.
        Attribute 'comment' is owned by TextRepresentation, which is owned by Context, itself owend by Sense.
        @param comment The comment to set.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_example_comment(comment)
        return self

    def set_semantic_domain(self, semantic_domain, language=None):
        """! @brief Set semantic domain and language.
        Attributes 'semanticDomain' and 'language' are owned by SubjectField, which is owned by Sense.
        @param semantic_domain The semantic domain to set.
        @param language Language used to describe the semantic domain.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_semantic_domain(semantic_domain, language)
        return self

    def get_semantic_domains(self, language=None):
        """! @brief Get all semantic domains.
        This attribute is owned by SubjectField, which is owned by Sense.
        @param language If this argument is given, get only semantic domains that are described using this language.
        @return A Python list of filtered SubjectField attributes 'semanticDomain'.
        """
        semantic_domains = []
        for sense in self.get_senses():
            for subject_field in sense.get_subject_fields():
                if subject_field.get_semanticDomain(language) is not None:
                    semantic_domains.append(subject_field.get_semanticDomain(language))
                semantic_domains += subject_field.get_sub_domains(language)
        return semantic_domains

    def set_translation(self, translation, language=None):
        """! @brief Set translation and language.
        Attributes 'translation' and 'language' are owned by Equivalent, which is owned by Sense.
        @param translation The translation to set.
        @param language Language used for the translation.
        @return LexicalEntry instance.
        """
        # Get the last Sense instance if any
        sense = self.get_last_sense()
        # If there is no Sense instance, create and add one
        if sense is None:
            sense = self.create_sense()
            self.add_sense(sense)
        sense.set_translation(translation, language)
        return self

    def set_audio(self, media_type="audio", file_name=None, author=None, quality=None, start_position="T00:00:00", duration=None, external_reference=None, audio_file_format=None):
        """! @brief Set audio resource.
        Attributes 'mediaType', 'fileName', 'author', 'quality', 'startPosition', 'durationOfEffectiveSpeech', 'externalReference', 'audioFileFormat' are owned by Material/Audio, which is owned by FormRepresentation, itself owend by Lemma.
        @param media_type The media type to set.
        @param file_name Name of the audio file.
        @param author Author of the recording.
        @param quality Quality of the recording, in range 'quality_range' defined in 'common/range.py'.
        @param start_position Start position of the form in the recording, in format 'Thh:mm:ss,msms', e.g. "T00:05:00".
        @param duration Duration of the effcetive speech, in format 'PThhHmmMssS', e.g. "PT00:05:00".
        @param external_reference Reference of the audio file, if not directly provided.
        @param audio_file_format Format of the audio file, e.g. "wav".
        @return LexicalEntry instance.
        """
        # Create a Lemma instance if not yet created
        if self.lemma is None:
            self.lemma = Lemma()
        self.lemma.set_audio(media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format)
        return self

    def is_subentry(self):
        """! @brief Check if this lexical entry is a subentry.
        @return 'True' if it is a subentry, 'False' otherwise.
        """
        for related_form in self.get_related_forms():
            # If one of the related form is a main entry, it means that the current lexical entry is a subentry
            if related_form.get_semanticRelation() == "main entry":
                return True
        return False

    def has_subentries(self):
        """! @brief Check if this lexical entry has subentries.
        @return 'True' if it has subentries, 'False' otherwise.
        """
        for related_form in self.get_related_forms():
            # If one of the related form is a subentry, it means that the current lexical entry is a main entry
            if related_form.get_semanticRelation() == "subentry":
                return True
        return False

    def get_subentries(self):
        """! @brief Get subentries of this lexical entry.
        @return A Python list of LexicalEntry.
        """
        subentries = []
        for related_form in self.get_related_forms():
            if related_form.get_semanticRelation() == "subentry":
                subentries.append(related_form.get_lexical_entry())
        return subentries

    def get_main_entry(self):
        """! @brief If this lexical entry is a subentry, get its main entry.
        @return A LexicalEntry if it exists, 'None' otherwise.
        """
        for related_form in self.get_related_forms():
            if related_form.get_semanticRelation() == "main entry":
                return related_form.get_lexical_entry()

    def create_and_add_component(self, position, lexeme):
        """! @brief Create and add a component to the lexical entry.
        @param position The position of the component in the multiword expression.
        @param lexeme Related lexeme.
        @return LexicalEntry instance.
        """
        if self.list_of_components is None:
            self.list_of_components = ListOfComponents()
        self.list_of_components.create_and_add_component(position, lexeme)
        return self

    def get_components(self):
        """! @brief If this lexical entry is a multiword expression, get its components.
        @return A list of components if any, an empty list otherwise.
        """
        if self.list_of_components is None:
            return []
        return self.list_of_components.get_components()

    def is_component(self):
        """! @brief Check if this lexical entry is a component.
        @return 'True' if it is a component, 'False' otherwise.
        """
        for related_form in self.get_related_forms():
            # If one of the related form is a complex predicate, it means that the current lexical entry is a component
            if related_form.get_semanticRelation() == "complex predicate":
                return True
        return False

    def get_speaker(self):
        """! @brief Get speaker.
        @return LexicalEntry private attribute '__speaker'.
        """
        return self.__speaker
