#! /usr/bin/env python

"""! @package resources
"""

from material import Material

class Video(Material):
    """! Video is a Material subclass representing a video.
    """
    def __init__(self):
        """! @brief Constructor.
        Video instances are owned by ?.
        @return A Video instance.
        """
        # Initialize Material attributes: 'mediaType', 'fileName' and 'author'
        self.__new__()
        self.description = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass
