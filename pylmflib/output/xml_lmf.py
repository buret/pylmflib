#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""! @package output
"""

from utils.xml_format import write_result, Element, SubElement
from utils.io import ENCODING

def xml_lmf_write(object, filename):
    """! @brief Write an XML LMF file.
    @param object The LMF instance to write as XML.
    @param filename The name of the XML LMF file to write with full path, for instance 'user/output.xml'.
    """
    # Create the root XML element
    root = Element(object.__class__.__name__)
    # Create all XML sub-elements
    build_sub_elements(object, root)
    # Write all created XML elements in the output file
    write_result(root, filename)

def build_sub_elements(object, element):
    """! @brief Create XML sub-elements to an existing XML element by parsing an LMF object instance.
    @param object An LMF object instance.
    @param element XML element for which sub-elements have to be created according to LMF object attributes.
    """
    # Parse instance attributes
    for item in object.__dict__.items():
        attr_name = item[0]
        attr_value = item[1]
        # For each defined public attribute, create an XML sub-element
        if not attr_name.startswith('_'):
            if attr_value is not None:
                # Handle boolean values
                if type(attr_value) is bool:
                    attr_value = unicode(attr_value)
                # Check if the attribute is itself a class instance
                if type(attr_value) is list:
                    # We suppose that a list always contains objects
                    for item in attr_value:
                        sub_element = SubElement(element, item.__class__.__name__)
                        build_sub_elements(item, sub_element)
                elif type(attr_value) not in [int, str, unicode]:
                    # If this is the case, create an XML element and restart the same operation recursively on this object
                    sub_element = SubElement(element, attr_value.__class__.__name__)
                    build_sub_elements(attr_value, sub_element)
                elif attr_name in ["dtdVersion", "id", "targets"]:
                    # If this is a specical attribute ("id" or "targets"), it must be inserted as an XML element attribute
                    if type(attr_value) is int:
                        attr_value = unicode(attr_value)
                    element.attrib.update({attr_name: attr_value})
                    if attr_name == "targets":
                        add_link(object, element)
                else:
                    # In all other cases, an XML sub-element must be created with the keyword name "feat"
                    feat = SubElement(element, "feat", att=attr_name, val=attr_value)
                    # Handle reserved characters and fonts
                    handle_reserved(feat)
                    handle_styles(feat)
                    #handle_font(feat)
                    # Special formatting
                    #handle_pinyin(feat)
                    #handle_tones(feat)
                    #handle_caps(feat)

## Functions to process XML/XHTML layout

def add_link(object, element):
    """Insert an hyperlink <a href=xxx>xxx<a/> in XML.
    """
    # To access options
    from pylmflib import options
    global options
    if options.cross_references:
        # Retrieve identifier
        try:
            id = object.get_lexical_entry().get_id()
        except AttributeError:
            id = None
        if id is not None:
            # Create link
            a = Element("a")
            a.attrib["href"] = id
            if len(element.attrib["targets"]) > 1 and element.attrib["targets"][-2] in ['1', '2', '3', '4', '5']:
                a.text = element.attrib["targets"][:-2] + " [" + element.attrib["targets"][-2] + element.attrib["targets"][-1] + "]"
            elif element.attrib["targets"][-1] in ['1', '2', '3', '4', '5', 'A', 'B', 'C', 'D', 'E']:
                a.text = element.attrib["targets"][:-1] + " [" + element.attrib["targets"][-1] + "]"
            else:
                a.text = element.attrib["targets"]
            # Insert link in element
            element.insert(0, a)
    return (object, element)

def handle_reserved(element):
    """ Handle reserved characters.
    """
    return element

def get_pattern(style):
    """ Return regular expression pattern from style.
    """
    return r"((((?!" + style + ").)*)" + style + ":([^\s\.,)]*)(.*))|((.*)\|" + style + "{([^}]*)}(.*))"

def handle_styles(element):
    """Replace:
    - 'fv:xxx' and '|fv{xxx}' by '<span class="vernacular">xxx</span>' ;
    - 'fn:xxx' and '|fn{xxx}' by '<span class="national">xxx</span>' ;
    - 'fl:xxx' and '|fl{xxx}' by '<span class="char_fl">xxx</span>' ;
    - 'fi:xxx' and '|fi{xxx}' by '<span class="char_fi">xxx</span>' ;
    - 'fr:xxx' and '|fr{xxx}' by '<span class="char_fr">xxx</span>' ;
    - 'ax:xxx' and '|ax{xxx}' by '<span class="char_ax">xxx</span>' ;
    - 'fs:xxx' and '|fs{xxx}' by '<span class="char_fs">xxx</span>';
    - 'vl:xxx' and '|vl{xxx}' by '<span class="char_vl">xxx</span>';
    - 'fe:xxx' and '|fe{xxx}' by '<span class="char_fe">xxx</span>';
    - 'hm:xxx' and '|hm{xxx}' by '<span class="char_hm">xxx</span>'.
    """
    import re
    element.text = element.attrib["val"]
    styles = ["fv", "fn", "fl", "fi", "fr", "ax", "fs", "vl", "fe", "hm"]

    # Initialize loop variable
    children = dict()
    for style in styles:
        # Find text to display in specific font
        pattern = get_pattern(style)
        result = re.match(pattern, element.text)
        while result:
            if result.group(1) is not None:
                before = result.group(2)
                text = result.group(4)
                after = result.group(5)
            elif result.group(6) is not None:
                before = result.group(7)
                text = result.group(8)
                after = result.group(9)
            # Create span
            new_element = Element("span")
            if style == "fv":
                new_element.attrib["class"] = "vernacular"
            elif style == "fn":
                new_element.attrib["class"] = "national"
            else:
                new_element.attrib["class"] = "char_" + style
            element.text = before
            new_element.text = text
            new_element.tail = after
            # Add new element to children
            children[len(before)] = new_element
            # Update result
            result = re.match(pattern, element.text)

    for style in styles:
        # Initialize loop variables
        index = 0
        new_element = None
        has_new_element = True
        while(has_new_element):
            # Reset loop variable
            has_new_element = False
            if new_element is not None:
                # Add new element to children
                children[index] = new_element
            for key in sorted(children):
                subelement = children[key]
                # Find text to display in specific font
                pattern = get_pattern(style)
                result = re.match(pattern, subelement.tail)
                if result:
                    if result.group(1) is not None:
                        before = result.group(2)
                        text = result.group(4)
                        after = result.group(5)
                    elif result.group(6) is not None:
                        before = result.group(7)
                        text = result.group(8)
                        after = result.group(9)
                    # Create span
                    new_element = Element("span")
                    if style == "fv":
                        new_element.attrib["class"] = "vernacular"
                    elif style == "fn":
                        new_element.attrib["class"] = "national"
                    else:
                        new_element.attrib["class"] = "char_" + style
                    subelement.tail = before
                    new_element.text = text
                    new_element.tail = after
                    # Update loop variables
                    index = key + len(before)
                    has_new_element = True

    # Insert new elements in element
    for key in sorted(children):
        element.append(children[key])

    if element.text == element.attrib["val"]:
        element.text = ""
    return element

def handle_font(element):
    """Replace '{xxx}' by '<span class="ipa">xxx</span>'.
    """
    import re
    # Find text to display in IPA
    pattern = r"([^{}]*){([^}]*)}(.*)"
    result = re.match(pattern, element.attrib["val"])
    # Initialize loop variables
    previous_span = None
    index = 0
    while result:
        before = result.group(1)
        ipa = result.group(2)
        after = result.group(3)
        # Handle previous span or element
        if previous_span is None:
            element.text = before
        else:
            previous_span.tail = before
        # Create span
        span = Element("span")
        span.attrib["class"] = "ipa"
        span.text = ipa
        # Insert span in element
        element.insert(index, span)
        # Update result
        result = re.match(pattern, after)
        if not result:
            span.tail = after
        # Update loop variables
        previous_span = span
        index += 1
    return element

def handle_pinyin(element):
    """Replace '@xxx' by '<span class="pinyin">xxx</span>'.
    """
    import re
    # Find pinyin
    pattern = r"([^@]*)@(\w*)(.*)"
    result = re.match(pattern, element.attrib["val"])
    # Initialize loop variables
    previous_span = None
    index = 0
    while result:
        before = result.group(1)
        pinyin = result.group(2)
        after = result.group(3)
        # Handle previous span or element
        if previous_span is None:
            element.text = before
        else:
            previous_span.tail = before
        # Create span
        span = Element("span")
        span.attrib["class"] = "pinyin"
        span.text = pinyin
        # Insert span in element
        element.insert(index, span)
        # Update result
        result = re.match(pattern, after)
        if not result:
            span.tail = after
        # Update loop variables
        previous_span = span
        index += 1
    return element

def handle_caps(element):
    """Handle small caps.
    Replace '°xxx' by '<span class="sc">xxx</span>'.
    """
    import re
    pattern = r"([^°]*)°([^\s\.,)+/:]*)(.*)"
    # Find text to display in small caps
    result = re.match(pattern, element.attrib["val"].encode(ENCODING))
    # Initialize loop variables
    previous_span = None
    index = 0
    while result:
        before = result.group(1).decode(ENCODING)
        sc = result.group(2).decode(ENCODING)
        after = result.group(3).decode(ENCODING)
        # Handle previous span or element
        if previous_span is None:
            element.text = before
        else:
            previous_span.tail = before
        # Create span
        span = Element("span")
        span.attrib["class"] = "sc"
        span.text = sc
        # Insert span in element
        element.insert(index, span)
        # Update result
        result = re.match(pattern, after.encode(ENCODING))
        if not result:
            span.tail = after
        # Update loop variables
        previous_span = span
        index += 1
    return element

def handle_tones(element):
    """Replace tones subscripts by '<sub>xxx</sub>'.
    """
    from utils.io import ENCODING
    import re
    if element.attrib["att"] == "tone":
        # Initialize loop variables
        previous_sub = None
        if element.text is None:
            element.text = ""
        index = 0
        for c in element.attrib["val"]:
            if c in set("abcd123"):
                # Create sub
                sub = Element("sub")
                sub.text = c
                # Insert sub in element
                element.insert(index, sub)
                # Update loop variables
                previous_sub = sub
                previous_sub.tail = ""
                index += 1
            else:
                # Handle previous sub or element
                if previous_sub is None:
                    element.text += c
                else:
                    previous_sub.tail += c
        if element.text == element.attrib["val"]:
            # Reset if identical
            element.text = None
        return element
    if element.attrib["att"] != "lexeme":
        return element
    # Find text to display as subscript
    tones = "˩˧˥".decode(encoding=ENCODING)
    # Monosyllabic
    current_pattern = "([^" + tones + "#$]+)(#?[" + tones + "]{1,2}[$#]?)([abcd123]?)"
    pattern = "^" + current_pattern + "$"
    if re.search(pattern, element.attrib["val"]):
        result = re.match(pattern, element.attrib["val"])
        before = result.group(1) + result.group(2)
        subscript = result.group(3)
        element.text = before
        if len(subscript) != 0:
            # Create sub
            sub = Element("sub")
            sub.text = subscript
            # Insert sub in element
            element.insert(0, sub)
        if element.text == element.attrib["val"]:
            # Reset if identical
            element.text = None
        return element
    # Disyllabic: add a constraint on other syllables which must have at least 2 characters (maximum 5)
    syllable = "([^" + tones + "#$]{2,5})(#?[" + tones + "]{1,2}[$#]?)([abcd123]?)"
    # Handle words composed of 2, 3, 4, 5 syllables
    for syllable_nb in range (2, 6):
        current_pattern += syllable
        pattern = "^" + current_pattern + "$"
        if re.search(pattern, element.attrib["val"]):
            result = re.match(pattern, element.attrib["val"])
            # Initialize loop variables
            previous_sub = None
            if element.text is None:
                element.text = ""
            for i in range (0, syllable_nb):
                before = result.group(i*3+1) + result.group(i*3+2)
                subscript = result.group(i*3+3)
                if i != syllable_nb - 1:
                    before += subscript
                    subscript = ""
                # Handle previous sub or element
                if previous_sub is None:
                    element.text += before
                else:
                    previous_sub.tail += before
                if len(subscript) != 0:
                    # Create sub
                    sub = Element("sub")
                    sub.text = subscript
                    # Insert sub in element
                    element.insert(i, sub)
                    # Update loop variable
                    previous_sub = sub
                    previous_sub.tail = ""
    if element.text == element.attrib["val"]:
        # Reset if identical
        element.text = None
    return element
