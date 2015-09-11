#! /usr/bin/env python

"""! @package core
"""

class Representation():
    """! "Representation class is an abstract class representing a Unicode string as well as, if needed, the unique attribute-value pairs that describe the specific language, script and orthography." (LMF)
    """
    def __init__(self):
        """! @brief As Representation is an abstract class, constructor raises an error.
        """
        raise NotImplementedError
    
    def __del__(self):
        """! @brief As Representation is an abstract class, desctructor raises an error.
        """
        raise NotImplementedError
    
    def __new__(self):
        """! @brief Private initialization called from Representation subclasses.
        """
        self.comment = None
        self.writtenForm = None
        self.language = None
        self.scriptName = None
