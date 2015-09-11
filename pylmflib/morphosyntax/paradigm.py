#! /usr/bin/env python

"""! @package morphosyntax
"""

from utils.attr import check_attr_type, check_attr_range
from common.range import paradigmLabel_range
from config.mdf import pdl_paradigmLabel

class Paradigm():
    """! Paradigm is a class representing a morphological paradigm.
    """
    def __init__(self):
        """! @brief Constructor.
        Paradigm instances are owned by Sense.
        @return A Paradigm instance.
        """
        self.paradigmLabel = None
        self.paradigm = None
        self.language = None
        self.morphology = None
        # LexicalEntry lexeme
        self.targets = None
        ## Pointer to an existing LexicalEntry
        # There is zero or one LexicalEntry pointer per Paradigm instance
        self.__lexical_entry = None

    def __del__(self):
        """! @brief Destructor.
        """
        # Decrement the reference count on pointed objects
        self.__lexical_entry = None

    def set_paradigmLabel(self, paradigm_label):
        """! @brief Set paradigm label.
        @param paradigm_label The paradigm label to set.
        @return Paradigm instance.
        """
        error_msg = "Paradigm label value '%s' is not defined" % str(paradigm_label)
        # Check paradigm label type
        check_attr_type(paradigm_label, [str, unicode], error_msg)
        # Check range of paradigm label value (also try with converted value from MDF to LMF)
        value = check_attr_range(str(paradigm_label), paradigmLabel_range, error_msg, mapping=pdl_paradigmLabel)
        # Do not restrict range of paradigm label value
        if value is None:
            value = paradigm_label
        self.paradigmLabel = value
        return self

    def get_paradigmLabel(self):
        """! @brief Get paradigm label.
        @return Paradigm attribute 'paradigmLabel'.
        """
        return self.paradigmLabel

    def set_paradigm(self, paradigm):
        """! @brief Set paradigm.
        @param paradigm The paradigm to set.
        @return Paradigm instance.
        """
        self.paradigm = paradigm
        return self

    def get_paradigm(self, language=None):
        """! @brief Get paradigm.
        @param language Language filter.
        @return Paradigm attribute 'paradigm'.
        """
        if language is None:
            return self.paradigm
        if language == self.get_language():
            return self.paradigm

    def set_language(self, language):
        """! @brief Set language of the paradigm.
        @param language The paradigm language to set.
        @return Paradigm instance.
        """
        self.language = language
        return self

    def get_language(self):
        """! @brief Get paradigm language.
        @return Paradigm attribute 'language'.
        """
        return self.language

    def set_morphology(self, morphology):
        """! @brief Set morphology.
        @param morphology The morphology to set.
        @return Paradigm instance.
        """
        self.morphology = morphology
        return self

    def get_morphology(self):
        """! @brief Get morphology.
        @return Paradigm attribute 'morphology'.
        """
        return self.morphology

    def get_lexical_entry(self):
        """! @brief Get pointed lexical entry.
        @return Paradigm private attribute '__lexical_entry'.
        """
        return self.__lexical_entry
