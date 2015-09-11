#! /usr/bin/env python

"""! @package core
"""

from representation import Representation
from utils.attr import check_attr_type

class TextRepresentation(Representation):
    """! "Text Representation is a class representing the textual content of definition or statement. When there is more than one variant orthography, the Text Representation instance contains a Unicode string representing the textual content as well as unique attribute-value pairs that describe the specific language, script and orthography." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        TextRepresentation instances are owned by Definition and Statement.
        @return A TextRepresentation instance.
        """
        # Initialize Representation attributes: 'comment', 'writtenForm', 'language' and 'scriptName'
        self.__new__()
        self.font = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def set_comment(self, comment):
        """! @brief Set written form comment.
        @param comment Comment about the written form.
        @return TextRepresentation instance.
        """
        error_msg = "Written form comment value '%s' is not allowed" % comment
        check_attr_type(comment, [str, unicode], error_msg)
        self.comment = comment
        return self

    def get_comment(self):
        """! @brief Get written form comment.
        @return Representation attribute 'comment'.
        """
        return self.comment

    def set_writtenForm(self, written_form, language=None):
        """! @brief Set written form and language.
        @param written_form The written form to set.
        @param language Language used for the written form.
        @return TextRepresentation instance.
        """
        error_msg = "Written form value '%s' is not allowed" % written_form
        check_attr_type(written_form, [str, unicode], error_msg)
        self.writtenForm = written_form
        if language is not None:
            self.set_language(language)
        return self

    def get_writtenForm(self, language=None):
        """! @brief Get written form.
        @param language If this argument is given, get written form only if written in this language.
        @return The filtered Representation attribute 'writtenForm'.
        """
        if language is None or language == self.get_language():
            return self.writtenForm

    def set_language(self, language):
        """! @brief Set language used for written form.
        @param language Language used for the written form.
        @return TextRepresentation instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for written form.
        @return Representation attribute 'language'.
        """
        return self.language

    def set_scriptName(self, script_name):
        """! @brief Set script name.
        @param script_name The script name to set.
        @return TextRepresentation instance.
        """
        error_msg = "Script name value '%s' is not allowed" % script_name
        check_attr_type(script_name, [str, unicode], error_msg)
        self.scriptName = script_name
        return self

    def get_scriptName(self):
        """! @brief Get script name.
        @return Representation attribute 'scriptName'.
        """
        return self.scriptName
