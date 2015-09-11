#! /usr/bin/env python

"""! @package morphology
"""

class Component():
    def __init__(self, position=None, lexeme=None):
        """! @brief Constructor.
        Component instances are owned by ListOfComponents.
        @param position The position of the component in the multiword expression.
        @param targets Related lexeme.
        @return A Component instance.
        """
        self.position = position
        # Composed LexicalEntry lexeme
        self.targets = lexeme
        ## Pointer to an existing LexicalEntry
        # There is one LexicalEntry pointer by Component instance
        self.__lexical_entry = None

    def __del__(self):
        """! @brief Destructor.
        """
        # Decrement the reference count on pointed objects
        self.__lexical_entry = None

    def set_lexical_entry(self, lexical_entry):
        """! @brief Set pointer to the component lexical entry instance. This function can only be called once the full dictionary has been parsed.
        @param lexical_entry The component LexicalEntry.
        @return Component instance.
        """
        self.__lexical_entry = lexical_entry
        return self

    def get_lexical_entry(self):
        """! @brief Get pointed lexical entry.
        @return Component private attribute '__lexical_entry'.
        """
        return self.__lexical_entry

    def get_lexeme(self):
        """! @brief Get component LexicalEntry lexeme.
        @return Component attribute 'targets'.
        """
        return self.targets
