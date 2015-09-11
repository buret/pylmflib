#! /usr/bin/env python

"""! @package resources
"""

from material import Material
from common.range import mediaType_range, quality_range
from utils.attr import check_attr_type, check_attr_range, check_time_format, check_duration_format
from utils.io import ENCODING

class Audio(Material):
    """! Audio is a Material subclass representing an audio recording.
    """
    def __init__(self):
        """! @brief Constructor.
        Audio instances are owned by FormRepresentation.
        @return An Audio instance.
        """
        # Initialize Material attributes: 'mediaType', 'fileName' and 'author'
        self.__new__()
        self.quality = None
        self.sound = None
        self.startPosition = None
        self.durationOfEffectiveSpeech = None
        self.externalReference = None
        self.audioFileFormat = None
        self.transcription = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def set_mediaType(self, media_type):
        """! @brief Set media type.
        @param media_type Type to set.
        @return Audio instance.
        """
        error_msg = "Media type value '%s' is not allowed" % media_type.encode(ENCODING)
        check_attr_type(media_type, [str, unicode], error_msg)
        self.mediaType = check_attr_range(str(media_type), mediaType_range, error_msg)
        return self

    def get_mediaType(self):
        """! @brief Get media type.
        @return Audio attribute 'mediaType'.
        """
        return self.mediaType

    def set_fileName(self, file_name):
        """! @brief Set file name.
        @param file_name Name to set.
        @return Audio instance.
        """
        error_msg = "File name value '%s' is not allowed" % file_name.encode(ENCODING)
        check_attr_type(file_name, [str, unicode], error_msg)
        self.fileName = file_name
        return self

    def get_fileName(self):
        """! @brief Get file name.
        @return Audio attribute 'fileName'.
        """
        return self.fileName

    def set_author(self, author):
        """! @brief Set author of the material resource.
        @param author Author to set.
        @return Audio instance.
        """
        error_msg = "Author value '%s' is not allowed" % author.encode(ENCODING)
        check_attr_type(author, [str, unicode], error_msg)
        self.author = author
        return self

    def get_author(self):
        """! @brief Get author of the material resource.
        @return Audio attribute 'author'.
        """
        return self.author

    def set_quality(self, quality):
        """! @brief Set audio recording quality.
        @param quality Quality to set.
        @return Audio instance.
        """
        error_msg = "Quality value '%s' is not allowed" % quality.encode(ENCODING)
        check_attr_type(quality, [str, unicode], error_msg)
        self.quality = check_attr_range(str(quality), quality_range, error_msg)
        return self

    def get_quality(self):
        """! @brief Get audio recording quality.
        @return Audio attribute 'quality'.
        """
        return self.quality

    def set_sound(self, sound):
        """! @brief Set sound.
        @param sound Sound to set.
        @return Audio instance.
        """
        error_msg = "Sound value '%s' is not allowed" % sound.encode(ENCODING)
        check_attr_type(sound, [str, unicode], error_msg)
        self.sound = sound
        return self

    def get_sound(self):
        """! @brief Get sound.
        @return Audio attribute 'sound'.
        """
        return self.sound

    def set_transcription(self, transcription):
        """! @brief Set transcription of the audio recording.
        @param Transcription to set.
        @return Audio instance.
        """
        error_msg = "Transcription value '%s' is not allowed" % transcription.encode(ENCODING)
        check_attr_type(transcription, [str, unicode], error_msg)
        self.transcription = transcription
        return self

    def get_transcription(self):
        """! @brief Get transcription of the audio recording.
        @return Audio attribute 'transcription'.
        """
        return self.transcription

    def set_startPosition(self, start_position):
        """! @brief Set start position.
        @param start_position Start position to set.
        @return Audio instance.
        """
        error_msg = "Start position value '%s' is not allowed" % start_position.encode(ENCODING)
        check_attr_type(start_position, [str, unicode], error_msg)
        if start_position[0] != 'T':
            # Add 'T' for Time
            start_position = 'T' + start_position
        check_time_format(start_position)
        self.startPosition = start_position
        return self

    def get_startPosition(self):
        """! @brief Get start position.
        @return Audio attribute 'startPosition'.
        """
        return self.startPosition

    def set_durationOfEffectiveSpeech(self, duration):
        """! @brief Set duration of effective speech.
        @param duration Duration of effective speech to set.
        @return Audio instance.
        """
        error_msg = "Duration of effective speech value '%s' is not allowed" % duration.encode(ENCODING)
        check_attr_type(duration, [str, unicode], error_msg)
        if duration[0] != 'P':
            if duration[0] != 'T':
                # Add 'T' for Time
                duration = 'T' + duration
            # Add 'P' for Period
            duration = 'P' + duration
        check_duration_format(duration)
        self.durationOfEffectiveSpeech = duration
        return self

    def get_durationOfEffectiveSpeech(self):
        """! @brief Get duration of effective speech.
        @return Audio attribute 'durationOfEffectiveSpeech'.
        """
        return self.durationOfEffectiveSpeech

    def set_externalReference(self, external_reference):
        """! @brief Set external reference.
        @param external_reference External reference to set.
        @return Audio instance.
        """
        error_msg = "External reference value '%s' is not allowed" % external_reference.encode(ENCODING)
        check_attr_type(external_reference, [str, unicode], error_msg)
        self.externalReference = external_reference
        return self

    def get_externalReference(self):
        """! @brief Get external reference.
        @return Audio attribute 'externalReference'.
        """
        return self.externalReference

    def set_audioFileFormat(self, audio_file_format):
        """! @brief Set audio file format.
        @param audio_file_format Audio file format to set.
        @return Audio instance.
        """
        error_msg = "Audio file format value '%s' is not allowed" % audio_file_format.encode(ENCODING)
        check_attr_type(audio_file_format, [str, unicode], error_msg)
        self.audioFileFormat = audio_file_format
        return self

    def get_audioFileFormat(self):
        """! @brief Get audio file formay.
        @return Audio attribute 'audioFileFormat'.
        """
        return self.audioFileFormat
