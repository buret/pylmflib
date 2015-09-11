#! /usr/bin/env python

"""! @package core
"""

from utils.attr import check_attr_type, check_attr_range
from common.range import noteType_range

class Statement():
    """! "Statement is a class representating a narrative description that refines or complements Definition." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Statement instances are owned by Definition.
        @return A Statement instance.
        """
        self.noteType = None
        self.note = None
        self.language = None
        self.encyclopedicInformation = None
        self.usageNote = None
        self.restriction = None
        self.derivation = None
        self.borrowedWord = None
        self.writtenForm = None
        self.sense = None
        self.etymology = None
        self.etymologyComment = None
        self.etymologyGloss = None
        self.etymologySource = None
        self.termSourceLanguage = None
        self.targetLexicalEntry = None
        self.scientificName = None
        ## TextRepresentation instances are owned by Statement
        # There is zero to many TextRepresentation instances per Statement
        self.text_representation = []

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]

    def set_note(self, note, type=None, language=None):
        """! @brief Set note.
        @param note Note to set.
        @param type Type of the note.
        @param language Language used for the note.
        @return Statement instance.
        """
        self.note = note
        if type is not None:
            self.set_noteType(type)
        if language is not None:
            self.set_language(language)
        return self

    def get_note(self, type=None, language=None):
        """! @brief Get note.
        @param type If this argument is given, get note only if its type corresponds.
        @param language If this argument is given, get note only if written in this language.
        @return The filtered Statement attribute 'note'.
        """
        if type is None:
            if language is None or self.get_language() == language:
                return self.note
        elif self.get_noteType() == type:
            if language is None or self.get_language() == language:
                return self.note

    def set_language(self, language):
        """! @brief Set language used for the note.
        @param language Language used for the note.
        @return Statement instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for the note.
        @return Statement attribute 'language'.
        """
        return self.language

    def set_noteType(self, note_type):
        """! @brief Set type of the note.
        @param note_type Type of the note.
        @return Statement instance.
        """
        error_msg = "Note type value '%s' is not allowed" % note_type
        check_attr_type(note_type, [str, unicode], error_msg)
        check_attr_range(note_type, noteType_range, error_msg)
        self.noteType = note_type
        return self

    def get_noteType(self):
        """! @brief Get type of the note.
        @return Statement attribute 'noteType'.
        """
        return self.noteType

    def set_usageNote(self, usage_note, language=None):
        """! @brief Set usage note.
        @param usage_note Usage note to set.
        @param language Language used for the usage note.
        @return Statement instance.
        """
        self.usageNote = usage_note
        if language is not None:
            self.set_language(language)
        return self

    def get_usageNote(self, language=None):
        """! @brief Get usage note.
        @param language If this argument is given, get usage note only if written in this language.
        @return The filtered Statement attribute 'usageNote'.
        """
        if language is None:
            return self.usageNote
        if self.get_language() == language:
            return self.usageNote

    def set_encyclopedicInformation(self, encyclopedic_information, language=None):
        """! @brief Set encyclopedic information.
        @param encyclopedic_information Encyclopedic information to set.
        @param language Language used for the encyclopedic information.
        @return Statement instance.
        """
        self.encyclopedicInformation = encyclopedic_information
        if language is not None:
            self.set_language(language)
        return self

    def get_encyclopedicInformation(self, language=None):
        """! @brief Get encyclopedic information.
        @param language If this argument is given, get encyclopedic information only if written in this language.
        @return The filtered Statement attribute 'encyclopedicInformation'.
        """
        if language is None:
            return self.encyclopedicInformation
        if self.get_language() == language:
            return self.encyclopedicInformation

    def set_restriction(self, restriction, language=None):
        """! @brief Set restriction.
        @param restriction Restriction to set.
        @param language Language used for the restriction.
        @return Statement instance.
        """
        self.restriction = restriction
        if language is not None:
            self.set_language(language)
        return self

    def get_restriction(self, language=None):
        """! @brief Get restriction.
        @param language If this argument is given, get restriction only if written in this language.
        @return The filtered Statement attribute 'restriction'.
        """
        if language is None:
            return self.restriction
        if self.get_language() == language:
            return self.restriction

    def set_borrowedWord(self, borrowed_word):
        """Set source language (in English), e.g. "Chinese".
        @param borrowed_word The source language to set.
        @return Statement instance.
        """
        error_msg = "Borrowed word value '%s' is not allowed" % borrowed_word
        check_attr_type(borrowed_word, [str, unicode], error_msg)
        self.borrowedWord = borrowed_word
        return self

    def get_borrowedWord(self):
        """Get source language (in English).
        @return Statement attribute 'borrowedWord'.
        """
        return self.borrowedWord

    def set_writtenForm(self, written_form):
        """Set loan word.
        @param written_form The loan word to set.
        @return Statement instance.
        """
        error_msg = "Written form value '%s' is not allowed" % written_form
        check_attr_type(written_form, [str, unicode], error_msg)
        self.writtenForm = written_form
        return self

    def get_writtenForm(self):
        """Get loan word.
        @return Statement attribute 'writtenForm'.
        """
        return self.writtenForm

    def set_etymology(self, etymology):
        """Set etymology.
        @param etymolgy The etymology to set.
        @return Statement instance.
        """
        error_msg = "Etymology value '%s' is not allowed" % etymology
        check_attr_type(etymology, [str, unicode], error_msg)
        self.etymology = etymology
        return self

    def get_etymology(self):
        """Get etymology.
        @return Statement attribute 'etymology'.
        """
        return self.etymology

    def set_etymologyComment(self, etymology_comment, term_source_language=None):
        """Set etymology comment (in English).
        @param etymolgy_comment The etymology comment to set.
        @param term_source_language The language used for the comment.
        @return Statement instance.
        """
        error_msg = "Etymology comment value '%s' is not allowed" % etymology_comment
        check_attr_type(etymology_comment, [str, unicode], error_msg)
        self.etymologyComment = etymology_comment
        if term_source_language is not None:
            self.set_termSourceLanguage(term_source_language)
        return self

    def get_etymologyComment(self, term_source_language=None):
        """Get etymology comment (in English).
        @param term_source_language The language of the etymology comment to retrieve.
        @return Statement attribute 'etymologyComment'.
        """
        if term_source_language is None or self.get_termSourceLanguage() == term_source_language:
            return self.etymologyComment

    def set_termSourceLanguage(self, term_source_language):
        """Set language used for the etymology comment.
        @param term_source_language The etymology comment language to set.
        @return Statement instance.
        """
        error_msg = "Term source language value '%s' is not allowed" % term_source_language
        check_attr_type(term_source_language, [str, unicode], error_msg)
        self.termSourceLanguage = term_source_language
        return self

    def get_termSourceLanguage(self):
        """Get language used for the etymology comment.
        @return Statement attribute 'termSourceLanguage'.
        """
        return self.termSourceLanguage

    def set_etymologyGloss(self, etymology_gloss):
        """Set etymology gloss.
        @param etymolgy_gloss The etymology gloss to set.
        @return Statement instance.
        """
        error_msg = "Etymology gloss value '%s' is not allowed" % etymology_gloss
        check_attr_type(etymology_gloss, [str, unicode], error_msg)
        self.etymologyGloss = etymology_gloss
        return self

    def get_etymologyGloss(self):
        """Get etymology gloss.
        @return Statement attribute 'etymologyGloss'.
        """
        return self.etymologyGloss

    def set_etymologySource(self, etymology_source):
        """Set etymology source.
        @param etymolgy_source The etymology source to set.
        @return Statement instance.
        """
        error_msg = "Etymology source value '%s' is not allowed" % etymology_source
        check_attr_type(etymology_source, [str, unicode], error_msg)
        self.etymologySource = etymology_source
        return self

    def get_etymologySource(self):
        """Get etymology source.
        @return Statement attribute 'etymologySource'.
        """
        return self.etymologySource

    def set_scientificName(self, scientific_name):
        """Set scientific name.
        @param scientific_name The scientific name to set.
        @return Statement instance.
        """
        error_msg = "Scientific name value '%s' is not allowed" % scientific_name
        check_attr_type(scientific_name, [str, unicode], error_msg)
        self.scientificName = scientific_name
        return self

    def get_scientificName(self):
        """Get scientific name.
        @return Statement attribute 'scientificName'.
        """
        return self.scientificName
