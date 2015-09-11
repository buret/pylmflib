#! /usr/bin/env python

"""! @package morphology
"""

from core.form import Form
from core.form_representation import FormRepresentation

class Lemma(Form):
    """! "Lemma is a Form subclass representing a form chosen by convention to designate the Lexical Entry. The lemma is usually equivalent to one of the inflected forms, the root, stem or compound phrase." (LMF).
    """
    def __init__(self):
        """! @brief Constructor.
        Lemma instance is owned by LexicalEntry.
        @return A Lemma instance.
        """
        # Initialize Form attribute 'form_representation'
        self.__new__()
        self.hyphenation = None
        self.lexeme = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def set_lexeme(self, lexeme):
        """! @brief Set lexeme.
        @param lexeme The lexeme to set.
        @return Lemma instance.
        """
        self.lexeme = lexeme
        return self

    def get_lexeme(self):
        """! @brief Get lexeme.
        @return Lemma attribute 'lexeme'.
        """
        return self.lexeme

    def create_form_representation(self):
        """! @brief Create a form representation.
        @return FormRepresentation instance.
        """
        return FormRepresentation()

    def add_form_representation(self, form_representation):
        """! @brief Add a form representation to the lemma.
        @param form_representation The FormRepresentation instance to add to the lemma.
        @return Lemma instance.
        """
        self.form_representation.append(form_representation)
        return self

    def find_form_representations(self, type):
        """! @brief Find variant forms.
        This attribute is owned by FormRepresentation.
        @param type The type to consider to retrieve the variant form.
        @return A Python list of found FormRepresentation attributes 'variantForm'.
        """
        found_forms = []
        for form_representation in self.get_form_representations():
            if form_representation.get_type() == type and form_representation.get_variantForm() is not None:
                found_forms.append(form_representation.get_variantForm())
        return found_forms

    def get_form_representations(self):
        """! @brief Get all form representations maintained by the lemma.
        @return A Python list of form representations.
        """
        return self.form_representation

    def get_form_representation(self, index):
        """! @brief Get a given form representation maintained by the lemma.
        @param index The index of the wanted form representation.
        @return The wanted FormRepresentation instance.
        """
        try:
            return self.form_representation[index]
        except IndexError:
            raise

    def set_variant_form(self, variant_form, type="unspecified"):
        """! @brief Set variant form and type.
        These attributes are owned by FormRepresentation.
        @param variant_form Variant form.
        @param type Type of variant, in range 'type_variant_range' defined in 'common/range.py'.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no variant form nor type
        for repr in self.get_form_representations():
            if repr.get_variantForm() is None and repr.get_type() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_variantForm(variant_form).set_type(type)
        return self

    def get_variant_forms(self, type="unspecified"):
        """! @brief Get all variant forms of specified type.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'variantForm' if type matches.
        """
        variant_forms = []
        for repr in self.get_form_representations():
            if repr.get_type() == type and repr.get_variantForm() is not None:
                variant_forms.append(repr.get_variantForm())
        return variant_forms

    def set_variant_comment(self, comment, language=None):
        """! @brief Set variant comment and language.
        These attributes are owned by FormRepresentation.
        @param comment Variant comment.
        @param language Language of comment.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no comment nor language
        for repr in self.get_form_representations():
            if repr.get_comment() is None and repr.get_language() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_comment(comment, language)
        return self
    
    def set_tone(self, tone):
        """! @brief Set tone.
        This attribute is owned by FormRepresentation.
        @param tone The tone to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no tone
        for repr in self.get_form_representations():
            if repr.get_tone() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_tone(tone)
        return self

    def get_tones(self):
        """! @brief Get all tones.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'tone'.
        """
        tones = []
        for repr in self.get_form_representations():
            if repr.get_tone() is not None:
                tones.append(repr.get_tone())
        return tones

    def set_geographical_variant(self, geographical_variant):
        """! @brief Set geographical variant.
        This attribute is owned by FormRepresentation.
        @param geographical_variant The geographical variant to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no geographical variant
        for repr in self.get_form_representations():
            if repr.get_geographicalVariant() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_geographicalVariant(geographical_variant)
        return self

    def set_phonetic_form(self, phonetic_form, script_name=None):
        """! @brief Set phonetic form.
        This attribute is owned by FormRepresentation.
        @param phonetic_form The phonetic form to set.
        @param script_name The name of the script used to write the phonetic form, e.g. pinyin.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no phonetic form and that uses the same script name
        for repr in self.get_form_representations():
            if repr.get_phoneticForm() is None and repr.get_scriptName() == script_name:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_phoneticForm(phonetic_form)
        if script_name is not None:
            form_representation.set_scriptName(script_name)
        return self

    def get_phonetic_forms(self, script_name=None):
        """! @brief Get all phonetic forms.
        This attribute is owned by FormRepresentation.
        @param script_name If provided, get only phonetic forms that are written using this script.
        @return A Python list of FormRepresentation attributes 'phoneticForm'.
        """
        phonetic_forms = []
        for repr in self.get_form_representations():
            if repr.get_phoneticForm() is not None and (script_name is None or repr.get_scriptName() == script_name):
                phonetic_forms.append(repr.get_phoneticForm())
        return phonetic_forms

    def set_contextual_variation(self, contextual_variation):
        """! @brief Set contextual variation.
        This attribute is owned by FormRepresentation.
        @param contextual_variation The contextual variation to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no contextual variation
        for repr in self.get_form_representations():
            if repr.get_contextualVariation() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_contextualVariation(contextual_variation)
        return self

    def get_contextual_variations(self):
        """! @brief Get all contextual variations.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'contextualVariation'.
        """
        contextual_variations = []
        for repr in self.get_form_representations():
            if repr.get_contextualVariation() is not None:
                contextual_variations.append(repr.get_contextualVariation())
        return contextual_variations

    def set_spelling_variant(self, spelling_variant):
        """! @brief Set spelling variant.
        This attribute is owned by FormRepresentation.
        @param spelling_variant The spelling variant to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no spelling variant
        for repr in self.get_form_representations():
            if repr.get_spellingVariant() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_spellingVariant(spelling_variant)
        return self

    def get_spelling_variants(self):
        """! @brief Get all spelling variants.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'spellingVariant'.
        """
        spelling_variants = []
        for repr in self.get_form_representations():
            if repr.get_spellingVariant() is not None:
                spelling_variants.append(repr.get_spellingVariant())
        return spelling_variants

    def set_citation_form(self, citation_form, script_name=None):
        """! @brief Set citation form.
        This attribute is owned by FormRepresentation.
        @param citation_form The citation form to set.
        @param script_name The name of the script used to write the citation form, e.g. devanagari.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no citation form and that uses the same script name
        for repr in self.get_form_representations():
            if repr.get_citationForm() is None and repr.get_scriptName() == script_name:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_citationForm(citation_form)
        if script_name is not None:
            form_representation.set_scriptName(script_name)
        return self

    def get_citation_forms(self, script_name=None):
        """! @brief Get all citation forms.
        This attribute is owned by FormRepresentation.
        @param script_name If provided, get only citation forms that are written using this script.
        @return A Python list of FormRepresentation attributes 'citationForm'.
        """
        citation_forms = []
        for repr in self.get_form_representations():
            if repr.get_citationForm() is not None and (script_name is None or repr.get_scriptName() == script_name):
                citation_forms.append(repr.get_citationForm())
        return citation_forms

    def set_dialect(self, dialect):
        """! @brief Set dialect.
        This attribute is owned by FormRepresentation.
        @param dialect The dialect to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no dialect
        for repr in self.get_form_representations():
            if repr.get_dialect() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_dialect(dialect)
        return self

    def set_transliteration(self, transliteration):
        """! @brief Set transliteration.
        This attribute is owned by FormRepresentation.
        @param transliteration The transliteration to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no dialect
        for repr in self.get_form_representations():
            if repr.get_transliteration() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_transliteration(transliteration)
        return self

    def get_transliterations(self):
        """! @brief Get all transliterations.
        This attribute is owned by FormRepresentation.
        @return A Python list of FormRepresentation attributes 'transliteration'.
        """
        transliterations = []
        for repr in self.get_form_representations():
            if repr.get_transliteration() is not None:
                transliterations.append(repr.get_transliteration())
        return transliterations

    def set_script_name(self, script_name):
        """! @brief Set script name.
        This attribute is owned by FormRepresentation.
        @param script_name The script name to set.
        @return Lemma instance.
        """
        form_representation = None
        # Set first FormRepresentation instance that has no dialect
        for repr in self.get_form_representations():
            if repr.get_scriptName() is None:
                form_representation = repr
                break
        if form_representation is None:
            # Create a FormRepresentation instance
            form_representation = self.create_form_representation()
            self.add_form_representation(form_representation)
        form_representation.set_scriptName(script_name)
        return self

    def set_audio(self, media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format):
        """! @brief Set audio resource.
        Attributes 'mediaType', 'fileName', 'author', 'quality', 'startPosition', 'durationOfEffectiveSpeech', 'externalReference', 'audioFileFormat' are owned by Material/Audio, which is owned by FormRepresentation.
        @param media_type The media type to set.
        @param file_name Name of the audio file.
        @param author Author of the recording.
        @param quality Quality of the recording, in range 'quality_range' defined in 'common/range.py'.
        @param start_position Start position of the form in the recording, in format 'Thh:mm:ss,msms', e.g. "T00:05:00".
        @param duration Duration of the effcetive speech, in format 'PThhHmmMssS', e.g. "PT00:05:00".
        @param external_reference Reference of the audio file, if not directly provided.
        @param audio_file_format Format of the audio file, e.g. "wav".
        @return Lemma instance.
        """
        # Create a FormRepresentation instance
        form_representation = self.create_form_representation()
        self.add_form_representation(form_representation)
        form_representation.set_audio(media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format)
        return self
