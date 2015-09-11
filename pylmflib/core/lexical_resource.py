#! /usr/bin/env python

"""! @package core
"""

from core.global_information import GlobalInformation

class LexicalResource():
    """! "Lexical Resource is a class representing the entire resource and is a container for one or more lexicons. There is only one Lexical Resource instance." (LMF)
    """
    def __init__(self, dtd_version=16):
        """! @brief Constructor.
        @return A LexicalResource instance.
        """
        self.dtdVersion = dtd_version
        ## GlobalInformation instance is owned by LexicalResource
        # There is one GlobalInformation for one LexicalResource
        self.global_information = GlobalInformation()
        ## Lexicon instances are owned by LexicalResource
        # There is one or more Lexicon instances for one unique LexicalResource
        self.lexicon = []
        ## Speaker instances are owned by LexicalResource
        # There is zero to many Speaker instances for one unique LexicalResource
        self.speaker = []

    def __del__(self):
        """! @brief Destructor.
        Release GlobalInformation, Lexicon, Speaker instances.
        """
        for lexicon in self.lexicon:
            del lexicon
        del self.lexicon[:]
        for speaker in self.speaker:
            del speaker
        del self.speaker[:]
        if self.global_information is not None:
            del self.global_information

    def get_lexicons(self):
        """! @brief Get all lexicons maintained by the lexical resource.
        @return A Python list of lexicons.
        """
        return self.lexicon

    def add_lexicon(self, lexicon):
        """! @brief Add a lexicon to the lexical resource.
        @param lexicon A Lexicon instance to add to the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.append(lexicon)
        return self

    def remove_lexicon(self, lexicon):
        """! @brief Remove a lexicon from the lexical resource.
        @param lexicon The Lexicon instance to remove from the Lexical Resource.
        @return Lexical Resource instance.
        """
        self.lexicon.remove(lexicon)
        return self

    def get_lexicon(self, id):
        """Retrieve a lexicon from its identifier.
        @param id The identifier of the lexicon to retrieve.
        @result A Lexicon instance, or None if not found.
        """
        for lexicon in self.get_lexicons():
            if lexicon.id == id:
                return lexicon

    def set_dtdVersion(self, dtd_version):
        """! @brief Set DTD version.
        @param dtd_version The DTD version to use.
        @return LexicalResource instance.
        """
        self.dtdVersion = dtd_version
        return self

    def get_dtdVersion(self):
        """! @brief Get DTD version.
        @return LexicalResource attribute 'dtdVersion'.
        """
        return self.dtdVersion

    def set_language_code(self, language_code):
        """! @brief Set language code.
        Attribute 'languageCode' is owned by GlobalInformation.
        @param language_code The language code to use.
        @return LexicalResource instance.
        """
        self.global_information.set_languageCode(language_code)
        return self

    def get_language_code(self):
        """! @brief Get language code.
        Attribute 'languageCode' is owned by GlobalInformation.
        @return GlobalInformation attribute 'languageCode'.
        """
        return self.global_information.get_languageCode()

    def set_version(self, version):
        """! @brief Set version.
        Attribute 'version' is owned by GlobalInformation.
        @param version The version to set.
        @return LexicalResource instance.
        """
        self.global_information.set_version(version)
        return self

    def get_version(self):
        """! @brief Get version.
        Attribute 'version' is owned by GlobalInformation.
        @return GlobalInformation attribute 'version'.
        """
        return self.global_information.get_version()

    def set_license(self, license):
        """! @brief Set license.
        Attribute 'license' is owned by GlobalInformation.
        @param license The license to set.
        @return LexicalResource instance.
        """
        self.global_information.set_license(license)
        return self

    def get_license(self):
        """! @brief Get license.
        Attribute 'license' is owned by GlobalInformation.
        @return GlobalInformation attribute 'license'.
        """
        return self.global_information.get_license()

    def set_character_encoding(self, character_encoding):
        """! @brief Set character encoding.
        Attribute 'characterEncoding' is owned by GlobalInformation.
        @param character_encoding The character encoding to use.
        @return LexicalResource instance.
        """
        self.global_information.set_characterEncoding(character_encoding)
        return self

    def get_character_encoding(self):
        """! @brief Get character encoding.
        Attribute 'characterEncoding' is owned by GlobalInformation.
        @return GlobalInformation attribute 'characterEncoding'.
        """
        return self.global_information.get_characterEncoding()

    def set_date_coding(self, date_coding):
        """! @brief Set date coding.
        Attribute 'dateCoding' is owned by GlobalInformation.
        @param date_coding The date coding to use.
        @return LexicalResource instance.
        """
        self.global_information.set_dateCoding(date_coding)
        return self

    def get_date_coding(self):
        """! @brief Get date coding.
        Attribute 'dateCoding' is owned by GlobalInformation.
        @return GlobalInformation attribute 'dateCoding'.
        """
        return self.global_information.get_dateCoding()

    def set_project_name(self, project_name):
        """! @brief Set project name.
        Attribute 'projectName' is owned by GlobalInformation.
        @param project_name The project's name to set.
        @return LexicalResource instance.
        """
        self.global_information.set_projectName(project_name)
        return self

    def get_project_name(self):
        """! @brief Get project name.
        Attribute 'projectName' is owned by GlobalInformation.
        @return GlobalInformation attribute 'projectName'.
        """
        return self.global_information.get_projectName()

    def set_creation_date(self, date):
        """! @brief Set creation date.
        Attribute 'creationDate' is owned by GlobalInformation.
        @param date The date to set, in format YYYY-MM-DD.
        @return LexicalResource instance.
        """
        self.global_information.set_creationDate(date)
        return self

    def get_creation_date(self):
        """! @brief Get creation date.
        Attribute 'creationDate' is owned by GlobalInformation.
        @return GlobalInformation attribute 'creationdDate'.
        """
        return self.global_information.get_creationDate()

    def set_last_update(self, date):
        """! @brief Set last update.
        Attribute 'lastUpdate' is owned by GlobalInformation.
        @param date The date to set, in format YYYY-MM-DD.
        @return LexicalResource instance.
        """
        self.global_information.set_lastUpdate(date)
        return self

    def get_last_update(self):
        """! @brief Get last update.
        Attribute 'lastUpdate' is owned by GlobalInformation.
        @return GlobalInformation attribute 'lastUpdate'.
        """
        return self.global_information.get_lastUpdate()

    def set_author(self, author):
        """! @brief Set author.
        Attribute 'author' is owned by GlobalInformation.
        @param author The author's name to set.
        @return LexicalResource instance.
        """
        self.global_information.set_author(author)
        return self

    def get_author(self):
        """! @brief Get author.
        Attribute 'author' is owned by GlobalInformation.
        @return GlobalInformation attribute 'author'.
        """
        return self.global_information.get_author()

    def set_description(self, description):
        """! @brief Set description.
        Attribute 'description' is owned by GlobalInformation.
        @param description The description to set.
        @return LexicalResource instance.
        """
        self.global_information.set_description(description)
        return self

    def get_description(self):
        """! @brief Get description.
        Attribute 'description' is owned by GlobalInformation.
        @return GlobalInformation attribute 'description'.
        """
        return self.global_information.get_description()

    def get_bibliographic_citation(self):
        """! @brief Get bibliographic citation.
        Attribute 'bibliographicCitation' is owned by GlobalInformation.
        @return GlobalInformation attribute 'bibliographicCitation'.
        """
        return self.global_information.get_bibliographicCitation()
