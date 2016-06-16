#! /usr/bin/env python

"""! @package resources
"""

from material import Material
from common.range import mediaType_range
from utils.attr import check_attr_type, check_attr_range
from utils.io import ENCODING

class Picture(Material):
    """! Picture is a Material subclass representing a picture.
    """
    def __init__(self):
        """! @brief Constructor.
        Picture instances are owned by FormRepresentation.
        @return A Picture instance.
        """
        # Initialize Material attributes: 'mediaType', 'fileName' and 'author'
        self.__new__()
        #self.filename = None
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

    def set_mediaType(self, media_type):
        """! @brief Set media type.
        @param media_type Type to set.
        @return Picture instance.
        """
        error_msg = "Media type value '%s' is not allowed" % media_type.encode(ENCODING)
        check_attr_type(media_type, [str, unicode], error_msg)
        self.mediaType = check_attr_range(str(media_type), mediaType_range, error_msg)
        return self

    def get_mediaType(self):
        """! @brief Get media type.
        @return Picture attribute 'mediaType'.
        """
        return self.mediaType

    def set_fileName(self, file_name):
        """! @brief Set file name.
        @param file_name Name to set.
        @return Picture instance.
        """
        error_msg = "File name value '%s' is not allowed" % file_name.encode(ENCODING)
        check_attr_type(file_name, [str, unicode], error_msg)
        self.fileName = file_name
        return self

    def get_fileName(self):
        """! @brief Get file name.
        @return Picture attribute 'fileName'.
        """
        return self.fileName

    def set_author(self, author):
        """! @brief Set author of the material resource.
        @param author Author to set.
        @return Picture instance.
        """
        error_msg = "Author value '%s' is not allowed" % author.encode(ENCODING)
        check_attr_type(author, [str, unicode], error_msg)
        self.author = author
        return self

    def get_author(self):
        """! @brief Get author of the material resource.
        @return Picture attribute 'author'.
        """
        return self.author

    def set_format(self, format):
        """! @brief Set picture file format.
        @param format Picture file format to set.
        @return Picture instance.
        """
        error_msg = "Picture file format value '%s' is not allowed" % format.encode(ENCODING)
        check_attr_type(format, [str, unicode], error_msg)
        self.format = format
        return self

    def get_audioFileFormat(self):
        """! @brief Get picture file format.
        @return Picture attribute 'format'.
        """
        return self.audioFileFormat
