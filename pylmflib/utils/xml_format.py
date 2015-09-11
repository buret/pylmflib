#! /usr/bin/env python

"""! @package utils
"""

from utils.io import open_write, ENCODING

try:
    from xml.etree.cElementTree import Element, SubElement, parse, dump, ElementTree, fromstring, tostring, XML
except ImportError:
    from xml.etree.ElementTree import Element, SubElement, parse, dump, ElementTree, fromstring, tostring, XML

def prettify(element, encoding=ENCODING):
    """! @brief Return a pretty-printed XML string for the given XML element.
    @param element An XML element.
    @param encoding Encoding mode. Default value is 'utf-8'.
    @return A Python string containing the printed version of the XML element.
    """
    from xml.dom import minidom
    rough_string = tostring(element, encoding=encoding)
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="    ", encoding=encoding)

def write_result(element, filename, encoding=ENCODING):
    """! @brief Write an XML element into a pretty XML output file.
    @param element An XML element.
    @param filename The name of the XML file to write with full path, for instance 'output.xml'.
    @param encoding Encoding mode. Default value is 'utf-8'.
    """
    unicode_str = prettify(element, encoding=encoding)
    output_file = open_write(filename, encoding=encoding)
    output_file.write(unicode_str.decode(encoding))
    output_file.close()

def parse_xml(filename):
    """! @brief Parse an XML file.
    @param filename The name of the XML file to parse with full path, for instance 'input.xml'.
    @return The root XML element.
    """
    tree = parse(filename)
    root = tree.getroot()
    return root
