#! /usr/bin/env python

"""! @package resources
"""

from resource import Resource

class HumanResource(Resource):
    """! HumanResource is a Resource subclass. HumanResource is an abstract class representing a speaker. The HumanResource class allows subclasses.
    """
    def __init__(self):
        """! @brief As HumanResource is an abstract class, constructor raises an error.
        """
        raise NotImplementedError
    
    def __del__(self):
        """! @brief As HumanResource is an abstract class, desctructor raises an error.
        """
        raise NotImplementedError
    
    def __new__(self):
        """! @brief Private initialization called from HumanResource subclasses.
        HumanResource subinstances are owned by LexicalResource.
        """
        self.name = None
        self.anonymizationFlag = None # boolean
        self.reference = None
        self.source = None
