#! /usr/bin/env python

"""! @package core
"""

from utils.error_handling import Warning
from utils.io import ENCODING

class Lexicon():
    """! "Lexicon is a class containing all the lexical entries of a given language within the entire resource." (LMF)
    """
    def __init__(self, id=None):
        """! @brief Constructor.
        Lexicon instances are owned by LexicalResource.
        @return A Lexicon instance.
        """
        self.set_id(id)
        self.language = None
        self.languageScript = None
        self.label = None
        self.lexiconType = None
        self.entrySource = None
        self.vowelHarmony = None
        self.localPath = None
        ## All LexicalEntry instances are maintained by Lexicon
        # There is one or more LexicalEntry instances per Lexicon
        self.lexical_entry = []
        # To know if cross references have already been verified or not
        self.__checked = False

    def __del__(self):
        """! @brief Destructor.
        Release LexicalEntry instances.
        """
        for lexical_entry in self.lexical_entry:
            del lexical_entry
        del self.lexical_entry[:]

    def set_id(self, id):
        """! @brief Set lexicon identifier.
        @param id The identifier to set.
        @return Lexicon instance.
        """
        self.id = id
        return self

    def get_id(self):
        """! @brief Get identifier.
        @return Lexicon attribute 'id'.
        """
        return self.id

    def set_entrySource(self, entry_source):
        """! @brief Set lexicon entry source.
        @param entry_source The entry source to set.
        @return Lexicon instance.
        """
        self.entrySource = entry_source
        return self

    def get_entrySource(self):
        """! @brief Get entry source.
        @return Lexicon attribute 'entrySource'.
        """
        return self.entrySource

    def set_language(self, language):
        """! @brief Set lexicon language.
        @param language The language to set.
        @return Lexicon instance.
        """
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language.
        @return Lexicon attribute 'language'.
        """
        return self.language

    def set_languageScript(self, language_script):
        """! @brief Set lexicon language script.
        @param language_script The language script to set.
        @return Lexicon instance.
        """
        self.languageScript = language_script
        return self

    def get_languageScript(self):
        """! @brief Get language script.
        @return Lexicon attribute 'languageScript'.
        """
        return self.languageScript

    def set_label(self, label):
        """! @brief Set lexicon label.
        @param label The label to set.
        @return Lexicon instance.
        """
        self.label = label
        return self

    def get_label(self):
        """! @brief Get label.
        @return Lexicon attribute 'label'.
        """
        return self.label

    def set_lexiconType(self, lexicon_type):
        """! @brief Set lexicon type.
        @param lexicon_type The lexicon type to set.
        @return Lexicon instance.
        """
        self.lexiconType = lexicon_type
        return self

    def get_lexiconType(self):
        """! @brief Get lexicon type.
        @return Lexicon attribute 'lexiconType'.
        """
        return self.lexiconType

    def set_vowelHarmony(self, vowel_harmony):
        raise NotImplementedError

    def get_vowelHarmony(self):
        raise NotImplementedError

    def set_localPath(self, local_path):
        """! @brief Set lexicon local path.
        @param local_path The absolute path to audio files to set.
        @return Lexicon instance.
        """
        self.localPath = local_path
        return self

    def get_localPath(self):
        """! @brief Get lexicon local path.
        @return Lexicon attribute 'localPath'.
        """
        return self.localPath

    def get_lexical_entries(self):
        """! @brief Get all lexical entries maintained by the lexicon.
        @return A Python set of lexical entries.
        """
        return self.lexical_entry

    def add_lexical_entry(self, lexical_entry):
        """! @brief Add a lexical entry to the lexicon.
        @param lexical_entry A LexicalEntry instance to add to the Lexicon.
        @return Lexicon instance.
        """
        self.lexical_entry.append(lexical_entry)
        return self

    def remove_lexical_entry(self, lexical_entry):
        """! @brief Remove a lexical entry from the lexicon.
        @param lexical_entry The LexicalEntry instance to remove from the Lexicon.
        @return Lexicon instance.
        """
        self.lexical_entry.remove(lexical_entry)
        return self

    def count_lexical_entries(self):
        """! @brief Count number of lexical entries of the lexicon.
        @return The number of lexical entries without duplicates maintained by the lexicon.
        """
        return len(self.get_lexical_entries())

    def sort_homonym_numbers(self, items=lambda lexical_entry: lexical_entry.get_lexeme(), condition=lambda lexical_entry: True):
        """! @brief Sort similar given items of lexical entries contained in the lexicon according to their homonym number.
        @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
        @param condition Lambda function giving a condition to apply classification.
        @return The sorted Python list of lexical entries.
        """
        def compare(x, y):
            """Compare 2 elements between each other.
            """
            if items(x) == items(y) and condition(x):
                # Classify similar entries by homonym number
                nb_x = x.get_homonymNumber()
                if nb_x is None:
                    nb_x = 0
                nb_y = y.get_homonymNumber()
                if nb_y is None:
                    nb_y = 0
                # If the 1st one is lower than the 2nd one, its rank is decremented
                if nb_x < nb_y:
                    return -1
                # If the 1st one is greater than the 2nd one, its rank is incremented
                elif nb_x > nb_y:
                    return 1
                else:
                    print Warning("Several lexical entries '%s' exist. Please solve this issue by precising the homonym number." % items(x).encode(ENCODING))
            # Do nothing
            return 0
        self.lexical_entry.sort(cmp=compare)
        return self.lexical_entry

    def sort_lexical_entries(self, items=lambda lexical_entry: lexical_entry.get_lexeme(), sort_order=None, comparison=None):
        """! @brief Sort given items of lexical entries contained in the lexicon according to a certain order.
        @param items Lambda function giving the item to sort. Default value is 'lambda lexical_entry: lexical_entry.get_lexeme()', which means that the items to sort are lexemes.
        @param sort_order Default value is 'None', which means that the lexicographical ordering uses the ASCII ordering.
        @param comparison Function to compare items. If 'None', a default function to compare character by character is provided.
        @return The sorted Python list of lexical entries.
        """
        # To access options
        from pylmflib import options
        global options
        def compare(x, y):
            """Compare 2 elements between each other.
            """
            # Before comparing, remove acute accents from strings if any
            x = x.replace(u"\u0301", '').replace(u"\u0302", '')
            y = y.replace(u"\u0301", '').replace(u"\u0302", '')
            for i in range(min(len(x), len(y))):
                try:
                    if type(sort_order) is not type(dict()):
                        if sort_order(x[i]) == sort_order(y[i]):
                            continue
                        # If the 1st one is lower than the 2nd one, its rank is decremented
                        if sort_order(x[i]) < sort_order(y[i]):
                            return -1
                        # If the 1st one is greater than the 2nd one, its rank is incremented
                        elif sort_order(x[i]) > sort_order(y[i]):
                            return 1
                    else:
                        if sort_order[x[i]] == sort_order[y[i]]:
                            continue
                        # If the 1st one is lower than the 2nd one, its rank is decremented
                        if sort_order[x[i]] < sort_order[y[i]]:
                            return -1
                        # If the 1st one is greater than the 2nd one, its rank is incremented
                        elif sort_order[x[i]] > sort_order[y[i]]:
                            return 1
                # Handle other characters
                except KeyError:
                    if options.verbose:
                        print Warning("Cannot compare " + x[i].encode(ENCODING) + " and " + y[i].encode(ENCODING))
                    if x[i] == y[i]:
                        continue
                    if x[i] < y[i]:
                        return -1
                    elif x[i] > y[i]:
                        return 1
            # If both strings do not have the same length, they do not equal => the smallest string is the shortest one
            if len(x) < len(y):
                return -1
            elif len(x) > len(y):
                return 1
            # If all characters match, both equal => do nothing
            return 0
        # Create a list of tuples associating items and their lexical entries: [(item1, entry1), (item2, entry2), ...]
        items_and_entries = [(items(lexical_entry), lexical_entry) for lexical_entry in self.lexical_entry]
        if sort_order is None:
            # Sort given items in alphabetical order
            items_and_entries.sort()
        else:
            # sorted(iterable, cmp, key, reverse)
            # list.sort(cmp, key, reverse)
            if comparison is None:
                comparison = compare
            items_and_entries.sort(cmp=comparison, key=lambda l: l[0])
        # Retrieve lexical entries to create a sorted list
        sorted_entries = [item_and_entry[1] for item_and_entry in items_and_entries]
        # Delete the old list of lexical entries and set the new one
        del self.lexical_entry[:]
        self.lexical_entry = sorted_entries
        return self.lexical_entry

    def find_lexical_entries(self, filter):
        """! @brief Find all lexical entries which characteristics meet the given condition.
        @param filter Function or lambda function taking a lexical entry as argument, and returning True or False; for instance 'lambda lexical_entry: lexical_entry.get_lexeme() == "Hello"'.
        @return A Python list of LexicalEntry instances.
        """
        lexical_entries = []
        for lexical_entry in self.get_lexical_entries():
            if filter(lexical_entry):
                lexical_entries.append(lexical_entry)
        return lexical_entries

    def check_cross_references(self):
        """! @brief Check all cross-references in the lexicon.
        Fill the private attribute '__lexicalEntry' of each RelatedForm instance for all lexical entries.
        @return Lexicon instance.
        """
        import os
        from string import digits
        if self.__checked:
            return self
        # Verifiy cross references only once
        self.__checked = True
        for lexical_entry in self.get_lexical_entries():
            for related_form in lexical_entry.get_related_forms():
                # From RelatedForm targets attribute, retrieve the pointed LexicalEntry instance
                related_lexeme = related_form.get_lexeme()
                # Check if there is an homonym number at the end of the related lexeme
                related_homonym_number = None
                if related_lexeme[-1] in digits:
                    related_homonym_number = related_lexeme[-1]
                    related_lexeme = related_lexeme[:-1]
                found_entry = self.find_lexical_entries(lambda lexical_entry: lexical_entry.get_lexeme() == related_lexeme)
                # Remove duplicate subentries from check if any
                if len(found_entry) == 2:
                    if found_entry[0].is_subentry() and not found_entry[1].is_subentry():
                        # Keep only the first subentry
                        found_entry = found_entry[:1]
                    elif not found_entry[0].is_subentry() and found_entry[1].is_subentry():
                        # Keep only the second subentry
                        found_entry = found_entry[1:]
                if len(found_entry) < 1:
                    # No lexical entry with this lexeme exists
                    print Warning("Lexical entry '%s' does not exist. Please solve this issue by checking the related form of lexical entry '%s'." % (related_lexeme.encode(ENCODING), lexical_entry.get_lexeme().encode(ENCODING)))
                elif len(found_entry) > 1:
                    # Several lexical entries with this lexeme exist => consider homonym number if any
                    related_homonym = []
                    if related_homonym_number is not None:
                        for related_entry in found_entry:
                            if related_entry.get_homonymNumber() == related_homonym_number:
                                related_homonym.append(related_entry)
                    if len(related_homonym) != 1:
                        print Warning("Several lexical entries '%s' exist. Please solve this issue by renaming lexical entries correctly or by precising the homonym number." % related_lexeme.encode(ENCODING))
                    else:
                        # Save the found lexical entry
                        related_form.set_lexical_entry(related_homonym[0])
                else:
                    # Save the found lexical entry
                    related_form.set_lexical_entry(found_entry[0])
            for component in lexical_entry.get_components():
                # From Component targets attribute, retrieve the pointed LexicalEntry instance
                found_entries = self.find_lexical_entries(lambda lexical_entry: lexical_entry.get_lexeme() == component.get_lexeme())
                for found_entry in found_entries:
                    # Check that the found entry is a component
                    if found_entry.is_component():
                        # Save the found lexical entry
                        component.set_lexical_entry(found_entry)
                        break
        return self

    def reset_check(self):
        """! @brief Reset boolean to be able to check all cross-references in the lexicon again.
        Reset the private attribute '__checked'.
        @return Lexicon instance.
        """
        self.__checked = False
        return self

    def convert_to_latex(self):
        """This method converts the lexicon into LaTeX format.
        """
        pass
