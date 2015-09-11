#! /usr/bin/env python

"""! @package utils
"""

from utils.error_handling import Error

## Define EOL depending on operating system
import os
if os.name == 'posix':
    # Unix-style end of line
    EOL = '\n'
else:
    # Windows-style end of line
    EOL = '\r\n'

# Define encoding
ENCODING = 'utf-8'

def open_file(filename, mode, encoding=ENCODING):
    """! @brief Open file in specified mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param mode Read or write mode.
    @param encoding Encoding mode. Default value is 'utf-8'.
    @return File handler.
    """
    try:
        try:
            return open(filename, mode, encoding=encoding)
        except TypeError:
            import codecs
            return codecs.open(filename, mode, encoding=encoding)
    except IOError as exception:
        raise Error("Cannot open file.", exception)

def open_read(filename, encoding=None):
    """! @brief Open file in read mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param encoding Encoding mode. Default value is None.
    @return File handler.
    """
    if encoding is None:
        return open_file(filename, 'rb')
    else:
        return open_file(filename, 'rb', encoding=encoding)

def open_write(filename, encoding=None):
    """! @brief Open file in write mode (automatically decode file in unicode).
    @param filename Full path to file to open.
    @param encoding Encoding mode. Default value is None.
    @return File handler.
    """
    if encoding is None:
        return open_file(filename, 'wb')
    else:
        return open_file(filename, 'wb', encoding=encoding)
