#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form

class Stem(Form):
    """! "Stem is a Form subclass representing a morph, thus manages the sublexme parts" (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        Stem instances are owned by LexicalEntry.
        @return A Stem instance.
        """
        # Initialize Form attribute 'form_representation'
        self.__new__()

    def __del__(self):
        """! @brief Destructor.
        """
        pass
