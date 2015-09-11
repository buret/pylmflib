#! /usr/bin/env python

"""! @package core
"""

from utils.attr import check_attr_type
from core.statement import Statement

class Definition():
    """! "Definition is a class representing a narrative description of a sense. It is provided to help human users understand the meaning of a lexical entry. A Sense instance can have zero to many definitions. Each Definition instance may be associated with zero to many Text Representation instances in order to manage the text defintion in more than one language or script. In addition, the narrative description can be expressed in a different language or script than the one in the Lexical Entry instance." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Definition instances are owned by Sense.
        @return A Definition instance.
        """
        self.language = None
        self.definition = None
        self.gloss = None
        self.literally = None
        ## TextRepresentation instances are owned by Definition
        # There is zero to many TextRepresentation instances per Definition
        self.text_representation = []
        ## Statement instances are owned by Definition
        # There is zero to many Statement instances per Definition
        self.statement = []

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation and Statement instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]
        for statement in self.statement:
            del statement
        del self.statement[:]

    def set_language(self, language):
        """! @brief Set language used for definition and gloss.
        @param language Language used for definition and gloss.
        @return Definition instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        # Check value
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for definition and gloss.
        @return Definition attribute 'language'.
        """
        return self.language

    def set_definition(self, definition, language=None):
        """! @brief Set definition.
        @param definition Definition.
        @param language Language used for the definition.
        @return Definition instance.
        """
        self.definition = definition
        if language is not None:
            self.set_language(language)
        return self

    def get_definition(self, language=None):
        """! @brief Get definition.
        @param language If this argument is given, get definition only if written in this language.
        @return The filtered Definition attribute 'definition'.
        """
        if language is None:
            return self.definition
        if self.language == language:
            return self.definition

    def set_gloss(self, gloss, language=None):
        """! @brief Set gloss.
        @param gloss Gloss.
        @param language Language used for the gloss.
        @return Definition instance.
        """
        self.gloss = gloss
        if language is not None:
            self.set_language(language)
        return self

    def get_gloss(self, language=None):
        """! @brief Get gloss.
        @param language If this argument is given, get gloss only if written in this language.
        @return The filtered Definition attribute 'gloss'.
        """
        if language is None:
            return self.gloss
        if self.language == language:
            return self.gloss

    def create_statement(self):
        """! @brief Create a Statement instance.
        @return Statement instance.
        """
        return Statement()

    def add_statement(self, statement):
        """! @brief Add a Statement instance to this Definition instance.
        @param statemement The Statement instance to add to the Definition instance.
        @return Definition instance.
        """
        self.statement.append(statement)
        return self

    def get_statements(self):
        """! @brief Get all Statement instances maintained by this Definition instance.
        @return A Python list of Statement instances.
        """
        return self.statement

    def get_first_statement(self):
        """! @brief Get the previously registered statement.
        @return The last element of Definition attribute 'statement'.
        """
        if len(self.get_statements()) >= 1:
            return self.get_statements()[0]

    def set_note(self, note, type=None, language=None):
        """! @brief Set note, note type and language.
        These attributes are owned by Statement.
        @param note Note to set.
        @param type Type of the note.
        @param language Language used for the note.
        @return Definition instance.
        """
        instance = None
        if language is None:
            # Find if there is a Statement instance without note
            for statement in self.get_statements():
                if statement.get_note() is None:
                    instance = statement
                    break
        else:
            # Find if there is a Statement instance with this language without note
            for statement in self.get_statements():
                if statement.get_language() == language and statement.get_note() is None:
                    # Found the Statement instance to set
                    instance = statement
                    break
            if instance is None:
                # Set first Statement instance that has no note nor language
                for statement in self.get_statements():
                    if statement.get_language() is None and statement.get_note() is None:
                        # Found the Statement instance to set
                        instance = statement
                        break
        if instance is None:
            # Create a Statement instance
            instance = self.create_statement()
            self.add_statement(instance)
        instance.set_note(note, type, language)
        return self

    def find_notes(self, type, language=None):
        """! @brief Find notes.
        This attribute is owned by Statement.
        @param type The type to consider to retrieve the note.
        @param language If this argument is given, find note only if written in this language.
        @return A Python list of found Statement attributes 'note'.
        """
        found_notes = []
        for statement in self.get_statements():
            if statement.get_note(type, language) is not None:
                found_notes.append(statement.get_note(type, language))
        return found_notes

    def set_usage_note(self, usage_note, language=None):
        """! @brief Set usage note and language.
        These attributes are owned by Statement.
        @param usage_note Usage note to set.
        @param language Language used for the usage note.
        @return Definition instance.
        """
        instance = None
        # Find if there is a Statement instance with this language without usage note
        for statement in self.get_statements():
            if statement.get_language() == language and statement.get_usageNote() is None:
                # Found the Statement instance to set
                instance = statement
                break
        if instance is None:
            # Set first Statement instance that has no usage note nor language
            for statement in self.get_statements():
                if statement.get_language() is None and statement.get_usageNote() is None:
                    # Found the Statement instance to set
                    instance = statement
                    break
        if instance is None:
            # Create a Statement instance
            instance = self.create_statement()
            self.add_statement(instance)
        instance.set_usageNote(usage_note, language)
        return self

    def find_usage_notes(self, language):
        """! @brief Find usage notes.
        This attribute is owned by Statement.
        @param language The language to consider to retrieve the usage note.
        @return A Python list of found Statement attributes 'usageNote'.
        """
        found_notes = []
        for statement in self.get_statements():
            if statement.get_usageNote(language) is not None:
                found_notes.append(statement.get_usageNote(language))
        return found_notes

    def set_encyclopedic_information(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information and language.
        These attributes are owned by Statement.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language used for the encyclopedic information.
        @return Definition instance.
        """
        instance = None
        # Find if there is a Statement instance with this language without encyclopedic information
        for statement in self.get_statements():
            if statement.get_language() == language and statement.get_encyclopedicInformation() is None:
                # Found the Statement instance to set
                instance = statement
                break
        if instance is None:
            # Set first Statement instance that has no encyclopedic information nor language
            for statement in self.get_statements():
                if statement.get_language() is None and statement.get_encyclopedicInformation() is None:
                    # Found the Statement instance to set
                    instance = statement
                    break
        if instance is None:
            # Create a Statement instance
            instance = self.create_statement()
            self.add_statement(instance)
        instance.set_encyclopedicInformation(encyclopedic_information, language)
        return self

    def find_encyclopedic_informations(self, language):
        """! @brief Find encyclopedic informations.
        This attribute is owned by Statement.
        @param language The language to consider to retrieve the encyclopedic information.
        @return A Python list of found Statement attributes 'encyclopedicInformation'.
        """
        found_informations = []
        for statement in self.get_statements():
            if statement.get_encyclopedicInformation(language) is not None:
                found_informations.append(statement.get_encyclopedicInformation(language))
        return found_informations

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction and language.
        These attributes are owned by Statement.
        @param restriction Restriction to set.
        @param language Language used for the restriction.
        @return Definition instance.
        """
        instance = None
        # Find if there is a Statement instance with this language without restriction
        for statement in self.get_statements():
            if statement.get_language() == language and statement.get_restriction() is None:
                # Found the Statement instance to set
                instance = statement
                break
        if instance is None:
            # Set first Statement instance that has no restriction nor language
            for statement in self.get_statements():
                if statement.get_language() is None and statement.get_restriction() is None:
                    # Found the Statement instance to set
                    instance = statement
                    break
        if instance is None:
            # Create a Statement instance
            instance = self.create_statement()
            self.add_statement(instance)
        instance.set_restriction(restriction, language)
        return self

    def find_restrictions(self, language):
        """! @brief Find restrictions.
        This attribute is owned by Statement.
        @param language The language to consider to retrieve the restriction.
        @return A Python list of found Statement attributes 'restriction'.
        """
        found_restrictions = []
        for statement in self.get_statements():
            if statement.get_restriction(language) is not None:
                found_restrictions.append(statement.get_restriction(language))
        return found_restrictions

    def set_borrowed_word(self, borrowed_word):
        """! @brief Set source language (in English).
        Attribute 'borrowedWord' is owned by the first Statement.
        @param borrowed_word Source language.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_borrowedWord(borrowed_word)
        return self

    def get_borrowed_word(self):
        """! @brief Get source language (in English).
        This attribute is owned by the first Statement.
        @return Statement attribute 'borrowedWord'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get borrowed word
        if statement is not None:
            return statement.get_borrowedWord()

    def set_written_form(self, written_form):
        """! @brief Set loan word.
        Attribute 'writtenForm' is owned by the first Statement.
        @param written_form Loan word.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_writtenForm(written_form)
        return self

    def get_written_form(self):
        """! @brief Get loan word.
        This attribute is owned by the first Statement.
        @return Statement attribute 'writtenForm'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get loan word
        if statement is not None:
            return statement.get_writtenForm()

    def set_etymology(self, etymology):
        """! @brief Set etymology.
        Attribute 'etymology' is owned by the first Statement.
        @param etymology Etymology.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_etymology(etymology)
        return self

    def get_etymology(self):
        """! @brief Get etymology.
        This attribute is owned by the first Statement.
        @return Statement attribute 'etymology'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get etymology
        if statement is not None:
            return statement.get_etymology()

    def set_etymology_comment(self, etymology_comment, term_source_language=None):
        """! @brief Set etymology comment and language.
        Attributes 'etymologyComment' and 'termSourceLanguage' are owned by the first Statement.
        @param etymology_comment Etymology comment.
        @param term_source_language Language of the comment.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_etymologyComment(etymology_comment, term_source_language)
        return self

    def get_etymology_comment(self, term_source_language=None):
        """! @brief Get etymology comment.
        This attribute is owned by the first Statement.
        @param term_source_language The language of the etymology comment to retrieve.
        @return Statement attribute 'etymologyComment'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get etymology comment
        if statement is not None:
            return statement.get_etymologyComment(term_source_language)

    def get_term_source_language(self):
        """! @brief Get language used for the etymology comment.
        This attribute is owned by the first Statement.
        @return Statement attribute 'termSourceLanguage'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get etymology comment language
        if statement is not None:
            return statement.get_termSourceLanguage()

    def set_etymology_gloss(self, etymology_gloss):
        """! @brief Set etymology gloss.
        Attribute 'etymologyGloss' is owned by the first Statement.
        @param etymology_gloss Etymology gloss.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_etymologyGloss(etymology_gloss)
        return self

    def get_etymology_gloss(self):
        """! @brief Get etymology gloss.
        This attribute is owned by the first Statement.
        @return Statement attribute 'etymologyGloss'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get etymology gloss
        if statement is not None:
            return statement.get_etymologyGloss()

    def set_etymology_source(self, etymology_source):
        """! @brief Set etymology source.
        Attribute 'etymologySource' is owned by the first Statement.
        @param etymology_source Etymology source.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_etymologySource(etymology_source)
        return self

    def get_etymology_source(self):
        """! @brief Get etymology source.
        This attribute is owned by the first Statement.
        @return Statement attribute 'etymologySource'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get etymology source
        if statement is not None:
            return statement.get_etymologySource()

    def set_scientific_name(self, scientific_name):
        """! @brief Set scientific name.
        Attribute 'scientficName' is owned by the first Statement.
        @param scientific_name Scientific name.
        @return Definition instance.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is no Statement instance, create and add one
        if statement is None:
            statement = self.create_statement()
            self.add_statement(statement)
        statement.set_scientificName(scientific_name)
        return self

    def get_scientific_name(self):
        """! @brief Get scientific name.
        This attribute is owned by the first Statement.
        @return Statement attribute 'scientificName'.
        """
        # Get the first Statement instance if any
        statement = self.get_first_statement()
        # If there is a Statement instance, get scientific name
        if statement is not None:
            return statement.get_scientificName()
