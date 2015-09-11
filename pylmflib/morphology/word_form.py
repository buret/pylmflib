#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form
from core.form_representation import FormRepresentation
from utils.attr import check_attr_range
from common.range import person_range, anymacy_range, grammaticalNumber_range, clusivity_range
from config.mdf import pd_person, pd_anymacy, pd_grammaticalNumber, pd_clusivity

class WordForm(Form):
    """! "Word Form is a Form subclass representing a form that a lexeme can take when used in a sentence or a phrase." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        WordForm instances are owned by LexicalEntry.
        @return A WordForm instance.
        """
        # Initialize Form attribute 'form_representation'
        self.__new__()
        self.grammaticalNumber = None
        self.grammaticalGender = None
        self.person = None
        self.anymacy = None
        self.clusivity = None
        self.tense = None
        self.case = None
        self.degree = None
        self.voice = None
        self.verbFormMood = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def create_form_representation(self):
        """! @brief Create a form representation.
        @return FormRepresentation instance.
        """
        return FormRepresentation()

    def add_form_representation(self, form_representation):
        """! @brief Add a form representation to the word form.
        @param form_representation The FormRepresentation instance to add to the word form.
        @return WordForm instance.
        """
        self.form_representation.append(form_representation)
        return self

    def get_form_representations(self):
        """! @brief Get all form representations maintained by the word form.
        @return A Python list of form representations.
        """
        return self.form_representation

    def set_written_form(self, written_form, script_name=None):
        """! @brief Set written form.
        This attribute is owned by Representation.
        @param written_form Written form.
        @param script_name Script used for the written form.
        @return WordForm instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no written form
        for repr in self.get_form_representations():
            if repr.get_writtenForm() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_writtenForm(written_form, script_name)
        return self

    def get_written_forms(self, script_name=None):
        """! @brief Get all written forms.
        This attribute is owned by Representation.
        @param script_name If this argument is given, get written form only if written using this script.
        @return A Python list of FormRepresentation attributes 'writtenForm'.
        """
        written_forms = []
        for repr in self.get_form_representations():
            if repr.get_writtenForm(script_name) is not None:
                written_forms.append(repr.get_writtenForm(script_name))
        return written_forms

    def set_variant_form(self, variant_form):
        """! @brief Set variant form.
        This attribute is owned by FormRepresentation.
        @param variant_form Variant form.
        @return WordForm instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no variant form
        for repr in self.get_form_representations():
            if repr.get_variantForm() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_variantForm(variant_form)
        return self

    def get_variant_forms(self):
        """! @brief Get all variant forms.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'variantForm'.
        """
        variant_forms = []
        for repr in self.get_form_representations():
            if repr.get_variantForm() is not None:
                variant_forms.append(repr.get_variantForm())
        return variant_forms

    def set_person(self, person):
        """! @brief Set grammatical person.
        @param person The grammatical person to set.
        @return WordForm instance.
        """
        error_msg = "Person value '%s' is not allowed" % str(person)
        # Check range of person value (also try with converted value from MDF to LMF)
        value = check_attr_range(person, person_range, error_msg, mapping=pd_person)
        self.person = value
        return self

    def get_person(self):
        """! @brief Get grammatical person.
        @return WordForm attribute 'person'.
        """
        return self.person

    def set_anymacy(self, anymacy):
        """! @brief Set grammatical anymacy.
        @param anymacy The grammatical anymacy to set.
        @return WordForm instance.
        """
        error_msg = "Anymacy value '%s' is not allowed" % str(anymacy)
        # Check range of anymacy value (also try with converted value from MDF to LMF)
        value = check_attr_range(anymacy, anymacy_range, error_msg, mapping=pd_anymacy)
        self.anymacy = value
        return self

    def get_anymacy(self):
        """! @brief Get anymacy.
        @return WordForm attribute 'anymacy'.
        """
        return self.anymacy

    def set_grammaticalNumber(self, grammatical_number):
        """! @brief Set grammatical number.
        @param grammatical_number The grammatical number to set.
        @return WordForm instance.
        """
        error_msg = "Grammatical number value '%s' is not allowed" % grammatical_number
        # Check range of grammatical number value (also try with converted value from MDF to LMF)
        value = check_attr_range(grammatical_number, grammaticalNumber_range, error_msg, mapping=pd_grammaticalNumber)
        self.grammaticalNumber = value
        return self

    def get_grammaticalNumber(self):
        """! @brief Get grammatical number.
        @return WordForm attribute 'grammaticalNumber'.
        """
        return self.grammaticalNumber

    def set_clusivity(self, clusivity):
        """! @brief Set grammatical clusivity.
        @param clusivity The grammatical clusivity to set.
        @return WordForm instance.
        """
        error_msg = "Clusivity value '%s' is not allowed" % clusivity
        # Check range of clusivity value (also try with converted value from MDF to LMF)
        value = check_attr_range(clusivity, clusivity_range, error_msg, mapping=pd_clusivity)
        self.clusivity = value
        return self

    def get_clusivity(self):
        """! @brief Get grammatical clusivity.
        @return WordForm attribute 'clusivity'.
        """
        return self.clusivity
