#! /usr/bin/env python

"""! @package core
"""

from core.representation import Representation
from resources.audio import Audio
from utils.attr import check_attr_type, check_attr_range
from common.range import type_variant_range

class FormRepresentation(Representation):
    """! "Form Representation is a class representing one variant orthography of a Form." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        FormRepresentation instances are owned by Form.
        @return A FormRepresentation instance.
        """
        # Initialize Representation attributes: 'comment', 'writtenForm', 'language' and 'scriptName'
        self.__new__()
        self.variantForm = None
        self.type = None
        self.transliteration = None
        self.tone = None
        self.geographicalVariant = None
        self.phoneticForm = None
        self.contextualVariation = None
        self.spellingVariant = None
        self.citationForm = None
        self.dialect = None
        ## Audio instance is owned by FormRepresentation
        # There is zero or one Audio instance per FormRepresentation
        self.audio = None
        # Speaker id
        self.targets = None
        ## Pointers to an existing Speaker
        # There is zero to many pointers per FormRepresentation instance
        self.__speaker = []

    def __del__(self):
        """! @brief Destructor.
        Release Audio instances.
        """
        if self.audio is not None:
            del self.audio
        # Decrement the reference count on pointed objects
        del self.__speaker[:]

    def get_speakers(self):
        """! @brief Get speakers.
        @return FormRepresentation private attribute '__speaker', a Python list of Speaker instances.
        """
        return self.__speaker

    def set_writtenForm(self, written_form, script_name=None):
        """! @brief Set written form and script.
        @param written_form The written form to set.
        @param script_name Script used for the written form.
        @return FormRepresentation instance.
        """
        error_msg = "Written form value '%s' is not allowed" % written_form
        check_attr_type(written_form, [str, unicode], error_msg)
        self.writtenForm = written_form
        if script_name is not None:
            self.set_scriptName(script_name)
        return self

    def get_writtenForm(self, script_name=None):
        """! @brief Get written form.
        @param script_name If this argument is given, get written form only if written using this script.
        @return The filtered Representation attribute 'writtenForm'.
        """
        if script_name is None or script_name == self.get_scriptName():
            return self.writtenForm

    def set_variantForm(self, variant_form):
        """! @brief Set variant form.
        @param variant_form The variant form to set.
        @return FormRepresentation instance.
        """
        error_msg = "Variant form value '%s' is not allowed" % variant_form
        check_attr_type(variant_form, [str, unicode], error_msg)
        self.variantForm = variant_form
        return self

    def get_variantForm(self):
        """! @brief Get variant form.
        @return FormRepresentation attribute 'variantForm'.
        """
        return self.variantForm

    def set_type(self, type):
        """! @brief Set variant type.
        @param type Type of variant, in range 'type_variant_range' defined in 'common/range.py'.
        @return FormRepresentation instance.
        """
        error_msg = "Variant type value '%s' is not allowed" % type
        value = None
        if type is not None:
            # Check value
            check_attr_type(type, [str, unicode], error_msg)
            value = check_attr_range(type, type_variant_range, error_msg)
        self.type = value
        return self

    def get_type(self):
        """! @brief Get variant type.
        @return FormRepresentation attribute 'type'.
        """
        return self.type

    def set_comment(self, comment, language=None):
        """! @brief Set variant form comment.
        @param comment Comment about the variant form.
        @param language Language used for the comment.
        @return FormRepresentation instance.
        """
        error_msg = "Variant form comment value '%s' is not allowed" % comment
        # Check attribute type
        check_attr_type(comment, [str, unicode], error_msg)
        self.comment = comment
        if language is not None:
            self.set_language(language)
        return self

    def get_comment(self, language=None):
        """! @brief Get variant form comment.
        @param language If this argument is given, get comment only if written in this language.
        @return The filtered Representation attribute 'comment'.
        """
        if language is None:
            return self.comment
        if self.get_language() == language:
            return self.comment

    def set_language(self, language):
        """! @brief Set language used for comment.
        @param language Language used for the comment.
        @return FormRepresentation instance.
        """
        error_msg = "Language value '%s' is not allowed" % language
        # Check value
        check_attr_type(language, [str, unicode], error_msg)
        self.language = language
        return self

    def get_language(self):
        """! @brief Get language used for comment.
        @return Representation attribute 'language'.
        """
        return self.language

    def set_tone(self, tone):
        """! @brief Set tone.
        @param tone The tone to set.
        @return FormRepresentation instance.
        """
        error_msg = "Tone value '%s' is not allowed" % tone
        check_attr_type(tone, [str, unicode], error_msg)
        self.tone = tone
        return self

    def get_tone(self):
        """! @brief Get tone.
        @return FormRepresentation attribute 'tone'.
        """
        return self.tone

    def set_geographicalVariant(self, geographical_variant):
        """! @brief Set geographical variant.
        @param geographical_variant The geographical variant to set.
        @return FormRepresentation instance.
        """
        error_msg = "Geographical variant value '%s' is not allowed" % geographical_variant
        check_attr_type(geographical_variant, [str, unicode], error_msg)
        self.geographicalVariant = geographical_variant
        return self

    def get_geographicalVariant(self):
        """! @brief Get geographical variant.
        @return FormRepresentation attribute 'geographicalVariant'.
        """
        return self.geographicalVariant

    def set_phoneticForm(self, phonetic_form):
        """! @brief Set phonetic form.
        @param phonetic_form The phonetic form to set.
        @return FormRepresentation instance.
        """
        error_msg = "Phonetic form value '%s' is not allowed" % phonetic_form
        check_attr_type(phonetic_form, [str, unicode], error_msg)
        self.phoneticForm = phonetic_form
        return self

    def get_phoneticForm(self):
        """! @brief Get phonetic form.
        @return FormRepresentation attribute 'phoneticForm'.
        """
        return self.phoneticForm

    def set_contextualVariation(self, contextual_variation):
        """! @brief Set contextual variation.
        @param contextualVariation The contextual variation to set.
        @return FormRepresentation instance.
        """
        error_msg = "Contextual variation value '%s' is not allowed" % contextual_variation
        check_attr_type(contextual_variation, [str, unicode], error_msg)
        self.contextualVariation = contextual_variation
        return self

    def get_contextualVariation(self):
        """! @brief Get contextual variation.
        @return FormRepresentation attribute 'contextualVariation'.
        """
        return self.contextualVariation

    def set_spellingVariant(self, spelling_variant):
        """! @brief Set spelling variant.
        @param spelling_variant The spelling variant to set.
        @return FormRepresentation instance.
        """
        error_msg = "Spelling variant value '%s' is not allowed" % spelling_variant
        check_attr_type(spelling_variant, [str, unicode], error_msg)
        self.spellingVariant = spelling_variant
        return self

    def get_spellingVariant(self):
        """! @brief Get spelling variant.
        @return FormRepresentation attribute 'spellingVariant'.
        """
        return self.spellingVariant

    def set_citationForm(self, citation_form):
        """! @brief Set citation form.
        @param citation_form The citation form to set.
        @return FormRepresentation instance.
        """
        error_msg = "Citation form value '%s' is not allowed" % citation_form
        check_attr_type(citation_form, [str, unicode], error_msg)
        self.citationForm = citation_form
        return self

    def get_citationForm(self):
        """! @brief Get citation form.
        @return FormRepresentation attribute 'citationForm'.
        """
        return self.citationForm

    def set_dialect(self, dialect):
        """! @brief Set dialect.
        @param dialect The dialect to set.
        @return FormRepresentation instance.
        """
        error_msg = "Dialect value '%s' is not allowed" % dialect
        check_attr_type(dialect, [str, unicode], error_msg)
        self.dialect = dialect
        return self

    def get_dialect(self):
        """! @brief Get dialect.
        @return FormRepresentation attribute 'dialect'.
        """
        return self.dialect

    def set_transliteration(self, transliteration):
        """! @brief Set transliteration.
        @param transliteration The transliteration to set.
        @return FormRepresentation instance.
        """
        error_msg = "Transliteration value '%s' is not allowed" % transliteration
        check_attr_type(transliteration, [str, unicode], error_msg)
        self.transliteration = transliteration
        return self

    def get_transliteration(self):
        """! @brief Get transliteration.
        @return FormRepresentation attribute 'transliteration'.
        """
        return self.transliteration

    def set_scriptName(self, script_name):
        """! @brief Set script name.
        @param script_name The script name to set.
        @return FormRepresentation instance.
        """
        error_msg = "Script name value '%s' is not allowed" % script_name
        check_attr_type(script_name, [str, unicode], error_msg)
        self.scriptName = script_name
        return self

    def get_scriptName(self):
        """! @brief Get script name.
        @return Representation attribute 'scriptName'.
        """
        return self.scriptName

    def create_audio(self):
        """! @brief Create an Audio instance.
        @return Audio instance.
        """
        return Audio()

    def get_audio(self):
        """! @brief Get the audio resource maintained by the form representation.
        @return Audio instance.
        """
        return self.audio

    def set_audio(self, media_type, file_name, author, quality, start_position, duration, external_reference, audio_file_format):
        """! @brief Set audio resource.
        Attributes 'mediaType', 'fileName', 'author', 'quality', 'startPosition', 'durationOfEffectiveSpeech', 'externalReference', 'audioFileFormat' are owned by Material/Audio.
        @param media_type The media type to set.
        @param file_name Name of the audio file.
        @param author Author of the recording.
        @param quality Quality of the recording, in range 'quality_range' defined in 'common/range.py'.
        @param start_position Start position of the form in the recording, in format 'Thh:mm:ss,msms', e.g. "T00:05:00".
        @param duration Duration of the effcetive speech, in format 'PThhHmmMssS', e.g. "PT00:05:00".
        @param external_reference Reference of the audio file, if not directly provided.
        @param audio_file_format Format of the audio file, e.g. "wav".
        @return FormRepresentation instance.
        """
        # Create an Audio instance
        self.audio = self.create_audio()
        # Set all attributes
        if media_type is not None:
            self.audio.set_mediaType(media_type)
        if file_name is not None:
            self.audio.set_fileName(file_name)
        if author is not None:
            self.audio.set_author(author)
        if quality is not None:
            self.audio.set_quality(quality)
        if start_position is not None:
            self.audio.set_startPosition(start_position)
        if duration is not None:
            self.audio.set_durationOfEffectiveSpeech(duration)
        if external_reference is not None:
            self.audio.set_externalReference(external_reference)
        if audio_file_format is not None:
            self.audio.set_audioFileFormat(audio_file_format)
        return self
