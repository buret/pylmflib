#! /usr/bin/env python

"""! @package core
"""

from utils.attr import check_date_format

class GlobalInformation():
    """! "Global Information is a class for administrative information and other general attributes, such as /language coding/ or /script coding/, which are valid for the entire lexical resource." (LMF)
    """
    def __init__(self):
        """! @brief Constructor.
        GlobalInformation instance is owned by LexicalResource.
        @return A GlobalInformation instance.
        """
        self.languageCode = None
        self.author = None
        self.version = None
        self.lastUpdate = None
        self.license = None
        self.characterEncoding = None
        self.dateCoding = None
        self.creationDate = None
        self.projectName = None
        self.description = None
        self.bibliographicCitation = None

    def __del__(self):
        """! @brief Destructor.
        """
        pass

    def set_languageCode(self, language_code):
        """! @brief Set global information language code.
        @param language_code The language code to use.
        @return GlobalInformation instance.
        """
        self.languageCode = language_code
        return self

    def get_languageCode(self):
        """! @brief Get global information language code.
        @return GlobalInformation attribute 'languageCode'.
        """
        return self.languageCode

    def set_version(self, version):
        """! @brief Set global information version.
        @param version The version to set.
        @return GlobalInformation version.
        """
        self.version = version
        return self

    def get_version(self):
        """! @brief Get global information version.
        @return GlobalInformation attribute 'version'.
        """
        return self.version

    def set_license(self, license):
        """! @brief Set global information license.
        @param license The license to set.
        @return GlobalInformation instance.
        """
        self.license = license
        return self

    def get_license(self):
        """! @brief Get global information license.
        @return GlobalInformation attribute 'license'.
        """
        return self.license

    def set_characterEncoding(self, character_encoding):
        """! @brief Set global information character encoding.
        @param character_encoding The character encoding to use.
        @return GlobalInformation instance.
        """
        self.characterEncoding = character_encoding
        return self

    def get_characterEncoding(self):
        """! @brief Get global information character encoding.
        @return GlobalInformation attribute 'characterEncoding'.
        """
        return self.characterEncoding

    def set_dateCoding(self, date_coding):
        """! @brief Set global information date coding.
        @param date_coding The date coding to use.
        @return GlobalInformation instance.
        """
        self.dateCoding = date_coding
        return self

    def get_dateCoding(self):
        """! @brief Get global information date coding.
        @return GlobalInformation attribute 'dateCoding'.
        """
        return self.dateCoding

    def set_projectName(self, project_name):
        """! @brief Set global information project name.
        @param project_name The project name to set.
        @return GlobalInformation instance.
        """
        self.projectName = project_name
        return self

    def get_projectName(self):
        """! @brief Get global information project name.
        @return GlobalInformation attribute 'projectName'.
        """
        return self.projectName

    def set_creationDate(self, date):
        """! @brief Set global information creation date.
        @param date The date to set.
        @return GlobalInformation instance.
        """
        check_date_format(date)
        self.creationDate = date
        return self

    def get_creationDate(self):
        """! @brief Get global information creation date.
        @return GlobalInformation attribute 'creationDate'.
        """
        return self.creationDate

    def set_lastUpdate(self, date):
        """! @brief Set global information last update.
        @param date The date to set.
        @return GlobalInformation instance.
        """
        check_date_format(date)
        self.lastUpdate = date
        return self

    def get_lastUpdate(self):
        """! @brief Get global information last update.
        @return GlobalInformation attribute 'lastUpdate'.
        """
        return self.lastUpdate

    def set_author(self, author):
        """! @brief Set global information author.
        @param author The author's name to set.
        @return GlobalInformation instance.
        """
        self.author = author
        return self

    def get_author(self):
        """! @brief Get global information author.
        @return GlobalInformation attribute 'author'.
        """
        return self.author

    def set_description(self, description):
        """! @brief Set global information description.
        @param description The description to set.
        @return GlobalInformation instance.
        """
        self.description = description
        return self

    def get_description(self):
        """! @brief Get global information description.
        @return GlobalInformation attribute 'description'.
        """
        return self.description

    def compute_bibliographicCitation(self):
        """! @brief Compute bibliographic citation from date and author.
        Set GlobalInformation attribute 'bibliographicCitation'.
        """
        self.bibliographicCitation = "Online dictionaries"
        if self.get_author() is not None:
            self.bibliographicCitation += ", " + self.get_author()
        if self.get_lastUpdate() is not None:
            self.bibliographicCitation += ", " + self.get_lastUpdate()

    def get_bibliographicCitation(self):
        """! @brief Get global information bibliographic citation.
        @return GlobalInformation attribute 'bibliographicCitation'.
        """
        self.compute_bibliographicCitation()
        return self.bibliographicCitation
