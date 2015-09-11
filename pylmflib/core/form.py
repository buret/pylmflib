#! /usr/bin/env python

"""! @package core
"""

class Form():
    """! "Form is an abstract class representing a lexeme, a morphological variant of a lexeme or a morph. The Form class allows subclasses." (LMF)
    """
    def __init__(self):
        """! @brief As Form is an abstract class, constructor raises an error.
        """
        raise NotImplementedError

    def __del__(self):
        """! @brief As Form is an abstract class, desctructor raises an error.
        """
        raise NotImplementedError

    def __new__(self):
        """! @brief Private initialization called from Form subclasses.
        Form subinstances are owned by LexicalEntry.
        """
        ## FormRepresentation instances are owned by Form subclasses
        # There is zero to many FormRepresentation instances per Form subclass
        self.form_representation = []
