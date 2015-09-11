#! /usr/bin/env python

"""! @package resources
"""

from resource import Resource

class Material(Resource):
    """! Material is a Resource subclass. Material is an abstract class representing an audiovisual resource: an audio recording, a picture or a video. The Material class allows subclasses.
    """
    def __init__(self):
        """! @brief As Material is an abstract class, constructor raises an error.
        """
        raise NotImplementedError
    
    def __del__(self):
        """! @brief As Material is an abstract class, desctructor raises an error.
        """
        raise NotImplementedError
    
    def __new__(self):
        """! @brief Private initialization called from Material subclasses.
        Material subinstances are owned by FormRepresentation.
        """
        self.mediaType = None
        self.fileName = None
        self.author = None
