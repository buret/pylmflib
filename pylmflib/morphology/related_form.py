#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form
from core.form_representation import FormRepresentation
from common.range import semanticRelation_range
from utils.attr import check_attr_type, check_attr_range

class RelatedForm(Form):
    """! "Related Form is a Form subclass representing a word form or a morph that can be related to the Lexical Entry. There is no asumption that the Related Form is associated with the Sense class in the Lexical Entry." (LMF)
    """
    def __init__(self, lexeme=None):
        """! @brief Constructor.
        RelatedForm instances are owned by LexicalEntry.
        @param lexeme Related lexeme. If not provided, default value is None.
        @return A RelatedForm instance.
        """
        # Initialize Form attribute 'form_representation'
        self.__new__()
        self.semanticRelation = None
        # Related LexicalEntry lexeme
        self.targets = lexeme
        ## Pointer to an existing LexicalEntry
        # There is one LexicalEntry pointer per RelatedForm instance
        self.__lexical_entry = None

    def __del__(self):
        """! @brief Destructor.
        """
        # Decrement the reference count on pointed objects
        self.__lexical_entry = None

    def set_semanticRelation(self, semantic_relation):
        """! @brief Set semantic relation.
        @param semantic_relation The semantic relation to set.
        @return RelatedForm instance.
        """
        error_msg = "Semantic relation value '%s' is not allowed" % semantic_relation
        # Check semantic relation type
        check_attr_type(semantic_relation, [str, unicode], error_msg)
        # Check range of semantic relation
        value = check_attr_range(semantic_relation, semanticRelation_range, error_msg)
        self.semanticRelation = value
        return self

    def get_semanticRelation(self):
        """! @brief Get semantic relation.
        @return RelatedForm attribute 'semanticRelation'.
        """
        return self.semanticRelation

    def get_lexeme(self):
        """! @brief Get related LexicalEntry lexeme.
        @return RelatedForm attribute 'targets'.
        """
        return self.targets

    def set_lexical_entry(self, lexical_entry):
        """! @brief Set pointer to the related lexical entry instance. This function can only be called once the full dictionary has been parsed.
        @param lexical_entry The related LexicalEntry.
        @return RelatedForm instance.
        """
        self.__lexical_entry = lexical_entry
        return self

    def get_lexical_entry(self):
        """! @brief Get related LexicalEntry.
        @return RelatedForm private attribute '__lexical_entry'.
        """
        return self.__lexical_entry

    def create_and_add_form_representation(self, written_form=None, language=None):
        """! @brief Create and add a form representation to the related form.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @return RelatedForm instance.
        """
        self.form_representation.append(FormRepresentation().set_writtenForm(written_form).set_language(language))
        return self

    def find_written_forms(self, language):
        """! @brief Find written forms.
        This attribite is owned by FormRepresentation.
        @param language The language to consider to retrieve the written forms.
        @return A Python list of found FormRepresentation attributes 'writtenForm'.
        """
        found_written_forms = []
        for form_representation in self.form_representation:
            if form_representation.get_language() == language:
                found_written_forms.append(form_representation.get_writtenForm())
        return found_written_forms
