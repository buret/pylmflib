#! /usr/bin/env python

"""! @package mrd
"""

from utils.attr import check_attr_type

class SubjectField():
    """! "Subject Field is a class representing a text string that provides domain or status information." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        SubjectField instances are owned by Sense.
        @return A SubjectField instance.
        """
        self.language = None
        self.semanticDomain = None
        ## SubjectField instances are owned by SubjectField
        # There is zero to many SubjectField instances per SubjectField
        self.subject_field = []

    def __del__(self):
        """! @brief Destructor.
        Release SubjectField instances.
        """
        for subject_field in self.subject_field:
            del subject_field
        del self.subject_field[:]

    def set_semanticDomain(self, semantic_domain, language=None):
        """! @brief Set semantic domain and language.
        @param semantic_domain The semantic domain to set.
        @param language Language used to describe the semantic domain.
        @return SubjectField instance.
        """
        error_msg = "Semantic domain value '%s' is not allowed" % semantic_domain
        check_attr_type(semantic_domain, [str, unicode], error_msg)
        self.semanticDomain = semantic_domain
        if language is not None:
            self.set_language(language)
        return self

    def get_semanticDomain(self, language=None):
        """! @brief Get semantic domain.
        @param language If this argument is given, get semantic domain only if written in this language.
        @return The filtered SubjectField attribute 'semanticDomain'.
        """
        if language is None or language == self.get_language():
            return self.semanticDomain

    def set_language(self, language):
        """! @brief Set language used for semantic domain.
        @param language Language used to describe the semantic domain.
        @return SubjectField instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for semantic domain.
        @return SubjectField attribute 'language'.
        """
        return self.language

    def create_and_add_subject_field(self):
        """! @brief Create and add a subject field.
        @return The created SubjectField instance.
        """
        subject_field = SubjectField()
        self.subject_field.append(subject_field)
        return subject_field

    def get_subject_fields(self):
        """! @brief Get all subject fields maintained by this subject field.
        @return A Python list of subject fields.
        """
        return self.subject_field

    def set_sub_domain(self, semantic_domain, language=None):
        """! @brief Set a sub-domain and language.
        @param semantic_domain The sub-domain to set.
        @param language Language used to describe the sub-domain.
        @return SubjectField instance.
        """
        self.create_and_add_subject_field().set_semanticDomain(semantic_domain, language)
        return self

    def get_sub_domains(self, language=None):
        """! @brief Get all sub-domains.
        Attribute 'semanticDomain' is owned by SubjectField, which is owned by SubjectField, etc.
        @param language If this argument is given, get only semantic domains that are described using this language.
        @return A Python list of all SubjectField attributes 'semanticDomain'.
        """
        semantic_domains = []
        for subject_field in self.get_subject_fields():
            if subject_field.get_semanticDomain(language) is not None:
                semantic_domains.append(subject_field.get_semanticDomain(language))
            semantic_domains += subject_field.get_sub_domains(language)
        return semantic_domains
