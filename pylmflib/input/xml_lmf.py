#! /usr/bin/env python

"""! @package input
"""

from utils.xml_format import parse_xml
from utils.error_handling import InputError

def compute_name(object_name):
    """! @brief Compute attribute/module name from object name as follows: 'ObjectName' attribute/module name is 'object_name'.
    @param object_name String containing name of the object, e.g. 'LexicalEntry'.
    @return The corresponding attribute/module name, e.g. 'lexical_entry'.
    """
    name = ''
    for c in object_name:
        # Detect first letter of a word: it is an uppercase letter
        if c.isupper():
            # Add an underscore separator between words if needed
            if name != '':
                name += '_'
        name += c.lower()
    return name

def factory(object_name, attributes):
    """! @brief This function is an object factory. Indeed, from an object name and its attributes, it creates a Python object and sets its attributes.
    @param object_name A Python string containing the object name, for instance 'LexicalEntry'.
    @param attributes A Python dictionary containing pairs of attribute name (as a Python string) and value, for instance {'partOfSpeech': 'n'}.
    """
    # Compute module name from object name
    module_name = compute_name(object_name)
    # Find the package in which the object class is defined, in order to be able to import the correct Python module
    import sys, os, glob
    running_path = sys.path[0]
    if os.name == 'posix':
        # Unix-style path
        separator = '/'
    else:
        # Windows-style path
        separator = '\\'
    full_path = glob.glob(running_path + separator + ".." + separator + ".." + separator + "pylmflib" + separator + "*" + separator + module_name + ".py")
    if len(full_path) < 1:
        # No file with this name exists
        raise InputError(module_name + ".py", "No file named '%s' exists in the library. It is not allowed, so please solve this issue by renaming files correctly." % (module_name + ".py"))
    elif len(full_path) > 1:
        # Several files with this name exist
        raise InputError(module_name + ".py", "Several files named '%s' exist in the library. It is not allowed, so please solve this issue by renaming files correctly. Here is the list of found files with this name: %s" % ((module_name + ".py"), str(full_path)))
    # Retrieve package name from full path
    package_name = full_path[0].split(separator)[-2]
    # Import object module: "package.module"
    object_module = __import__(package_name + "." + module_name)
    # Retrieve object class from module
    object_class = getattr(object_module, object_name)
    # Create an instance of it
    instance = object_class()
    # Set class attributes
    for attribute in attributes.iteritems():
        setattr(instance, attribute[0], attribute[1])
    return instance

def xml_lmf_read(filename):
    """! @brief Read an XML LMF file.
    @param filename The name of the XML LMF file to read with full path, for instance 'user/input.xml'.
    @return A Lexical Resource instance containing all lexicons.
    """
    root = parse_xml(filename)
    # Create an object instance corresponding to the XML root element
    root_instance = factory(root.tag, root.attrib)
    # Parse XML sub-elements and create instance childs
    get_sub_elements(root_instance, root)
    return root_instance

def get_sub_elements(instance, element):
    """! @brief This function recursively parses the given XML element and creates corresponding LMF instances with their attributes.
    @param instance An LMF object instance.
    @param element An XML element.
    """
    for sub_element in element:
        # XML elements "feat" are modelized by LMF class attributes
        if sub_element.tag == "feat":
            # "feat" elements have 2 XML attributes: one for LMF attribute name ("att"), a second for LMF attribute value ("val")
            setattr(instance, sub_element.attrib["att"], sub_element.attrib["val"])
        elif sub_element.tag == "a":
            # "a" elements are HTML links => do not consider them
            pass
        else:
            # Create LMF instances corresponding to XML sub-elements
            sub_instance = factory(sub_element.tag, sub_element.attrib)
            # Root LMF object must own the child objects
            attr_name = compute_name(sub_element.tag)
            attr_value = getattr(instance, attr_name)
            if type(attr_value) is list:
                # If this attribute is a list, append the new value to the list
                attr_value.append(sub_instance)
            else:
                # Simply set the value
                setattr(instance, attr_name, sub_instance)
            # Repeat the same operation recursively
            get_sub_elements(sub_instance, sub_element)
