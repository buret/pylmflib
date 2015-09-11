#! /usr/bin/env python

"""! @package mrd
"""

from utils.attr import check_attr_type

class Equivalent():
    """! "Equivalent is a class representing the translation equivalent of the word form managed by the Lemma class." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Equivalent instances are owned by Sense.
        @return An Equivalent instance.
        """
        self.language = None
        self.translation = None
        ## TextRepresentation instances are owned by Equivalent
        # There is zero to many TextRepresentation instances per Equivalent
        self.text_representation = []

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]

    def set_translation(self, translation, language=None):
        """! @brief Set translation and language.
        @param translation The translation to set.
        @param language Language used for the translation.
        @return Equivalent instance.
        """
        error_msg = "Translation value '%s' is not allowed" % translation
        check_attr_type(translation, [str, unicode], error_msg)
        self.translation = translation
        if language is not None:
            self.set_language(language)
        return self

    def get_translation(self, language=None):
        """! @brief Get translation.
        @param language If this argument is given, get translation only if written in this language.
        @return The filtered Equivalent attribute 'translation'.
        """
        if language is None or language == self.get_language():
            return self.translation

    def set_language(self, language):
        """! @brief Set language used for translation.
        @param language Language used for the translation.
        @return Equivalent instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for translation.
        @return Equivalent attribute 'language'.
        """
        return self.language
