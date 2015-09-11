#! /usr/bin/env python

"""! @package mrd
"""

from common.range import type_example_range
from utils.attr import check_attr_type, check_attr_range
from core.text_representation import TextRepresentation

class Context():
    """! "Context is a class representing a text string that provides authentic context for the use of the word form managed by the Lemma. This class is to be distinguished from Sense Example." (LMF)
    """
    def __init__(self, speakerID=None):
        """! @brief Constructor.
        Context instances are owned by Sense.
        @param speakerID Related speaker identifier. If not provided, default value is None.
        @return A Context instance.
        """
        self.language = None
        self.type = None
        ## TextRepresentation instances are owned by Context
        # There is zero to many TextRepresentation instances per Context
        self.text_representation = []
        # Speaker id
        self.targets = speakerID
        ## Pointer to an existing Speaker
        # There is zero or one Speaker pointer per Context instance
        self.__speaker = None

    def __del__(self):
        """! @brief Destructor.
        Release TextRepresentation instances.
        """
        for text_representation in self.text_representation:
            del text_representation
        del self.text_representation[:]
        # Decrement the reference count on pointed objects
        self.__speaker = None

    def set_type(self, type):
        """! @brief Set context type.
        @param type Type of text representations, in range 'type_example_range' defined in 'common/range.py'.
        @return Context instance.
        """
        error_msg = "Context type value '%s' is not allowed" % type
        value = None
        if type is not None:
            check_attr_type(type, [str, unicode], error_msg)
            value = check_attr_range(type, type_example_range, error_msg)
        self.type = value
        return self

    def get_type(self):
        """! @brief Get context type.
        @return Context attribute 'type'.
        """
        return self.type

    def create_text_representation(self):
        """! @brief Create a text representation.
        @return TextRepresentation instance.
        """
        return TextRepresentation()

    def add_text_representation(self, text_representation):
        """! @brief Add a text representation to the context.
        @param text_representation The TextRepresentation instance to add to the context.
        @return Context instance.
        """
        self.text_representation.append(text_representation)
        return self

    def get_text_representations(self):
        """! @brief Get all text representations maintained by the context.
        @return A Python list of text representations.
        """
        return self.text_representation

    def get_last_text_representation(self):
        """! @brief Get the previously registered TextRepresentation instance.
        @return The last element of Context attribute 'text_representation'.
        """
        if len(self.get_text_representations()) >= 1:
            return self.get_text_representations()[-1]

    def find_written_forms(self, language=None, script_name=None):
        """! @brief Find written forms.
        This attribute is owned by TextRepresentation.
        @param language If given, the language to consider to retrieve the written form.
        @param script_name If given, the script to consider to retrieve the written form.
        @return A Python list of found TextRepresentation attributes 'writtenForm'.
        """
        found_forms = []
        for repr in self.get_text_representations():
            if (language is None or repr.get_language() == language) and repr.get_writtenForm() is not None \
                and (script_name is None or repr.get_scriptName() == script_name):
                found_forms.append(repr.get_writtenForm())
        return found_forms

    def get_comments(self):
        """! @brief Get comments.
        This attribute is owned by TextRepresentation.
        @return A Python list of found TextRepresentation attributes 'comment'.
        """
        found_comments = []
        for repr in self.get_text_representations():
            if repr.get_comment() is not None:
                found_comments.append(repr.get_comment())
        return found_comments

    def set_written_form(self, written_form, language=None, script_name=None):
        """! @brief Set text representation written form, language and script.
        Attributes 'writtenForm', 'language' and 'scriptName' are owned by TextRepresentation.
        @param written_form The written form to set.
        @param language Language of the written form.
        @param script_name The name of the script used to write the form, e.g. devanagari.
        @return Context instance.
        """
        # Create a TextRepresentation instance, set it, and add it to the list
        repr = self.create_text_representation().set_writtenForm(written_form)
        if language is not None:
            repr.set_language(language)
        if script_name is not None:
            repr.set_scriptName(script_name)
        self.add_text_representation(repr)
        return self

    def set_comment(self, comment):
        """! @brief Set text representation comment.
        Attribute 'comment' is owned by TextRepresentation.
        @param comment The comment to set.
        @return Context instance.
        """
        # Retrieve the previsouly created text representation
        repr = self.get_last_text_representation()
        # Check if there is a comment already
        if repr is None or repr.get_comment() is not None:
            # Create a TextRepresentation instance and add it to the list
            repr = self.create_text_representation()
            self.add_text_representation(repr)
        repr.set_comment(comment)
        return self

    def get_speakerID(self):
        """! @brief Get related speaker identifier.
        @return Context attribute 'targets'.
        """
        return self.targets

    def get_speaker(self):
        """! @brief Get speaker.
        @return Context private attribute '__speaker'.
        """
        return self.__speaker
