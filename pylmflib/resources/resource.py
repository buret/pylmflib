#! /usr/bin/env python

"""! @package resources
"""

class Resource():
    """! Resource is an abstract class representing a material or a human resource. The Resource class allows subclasses.
    """
    def __init__(self):
        """! @brief As Resource is an abstract class, constructor raises an error.
        """
        raise NotImplementedError
    
    def __del__(self):
        """! @brief As Resource is an abstract class, desctructor raises an error.
        """
        raise NotImplementedError
    
    def __call__(self):
        """! @brief Private initialization called from Resource subclasses.
        Resource subinstances are owned by LexicalResource.
        """
        pass
