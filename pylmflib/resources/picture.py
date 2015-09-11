#! /usr/bin/env python

"""! @package resources
"""

from material import Material

class Picture(Material):
    """! Picture is a Material subclass representing a picture.
    """
    def __init__(self):
        """! @brief Constructor.
        Picture instances are owned by ?.
        @return A Picture instance.
        """
        # Initialize Material attributes: 'mediaType', 'fileName' and 'author'
        self.__new__()
        self.filename = None
        self.reference = None
        self.width = None
        self.height = None
        self.format = None
        ## Statement instances are owned by Picture
        # There is zero to many Statement instances per Picture
        self.statement = []

    def __del__(self):
        """! @brief Destructor.
        Release Statement instances.
        """
        for statement in self.statement:
            del statement
        del self.statement[:]
