#! /usr/bin/env python

"""! @package morphology
"""

from morphology.component import Component

class ListOfComponents():
    """ "List of Components is a class representing the aggregative aspect of a multiword expression (MWE). The mechanism can also be applied recursively, so that an MWE way be comprised of components that are themselves MWEs. This class is used in the morphological pattern and MWE pattern packages." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        ListOfComponents instance is owned by LexicalEntry.
        @return A ListOfComponents instance.
        """
        ## Component instances are owned by ListOfComponents
        # There are two or more Component instances per ListOfComponents
        self.component = [] # ordered list

    def __del__(self):
        """! @brief Destructor.
        Release Component instances.
        """
        for component in self.component:
            del component
        del self.component[:]

    def create_and_add_component(self, position, lexeme):
        """! @brief Create and add a component to the list.
        @param position The position of the component in the multiword expression.
        @param lexeme Related lexeme.
        @return ListOfComponents instance.
        """
        self.component.append(Component(position, lexeme))
        return self

    def get_components(self):
        """! @brief Get the list of components.
        @return ListOfComponents attribute 'component'.
        """
        return self.component
