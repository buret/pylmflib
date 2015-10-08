<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema" xmlns="http://www.tei-c.org/ns/1.0"
    exclude-result-prefixes="xs" version="2.0">
    <xsl:output encoding="UTF-8" method="xml" indent="yes"/>
    <xsl:strip-space elements="*"/>


    <xsl:template match="/">
        <TEI>
            <teiHeader>
                <fileDesc>
                    <titleStmt>
                        <title>
                            <xsl:value-of
                                select="LexicalResource/GlobalInformation/feat[@att='description']/@val"
                            />
                        </title>
                        <author>
                            <xsl:value-of
                                select="LexicalResource/GlobalInformation/feat[@att='author']/@val"
                            />
                        </author>
                        <respStmt>
                            <resp>Editor</resp>
                            <name>Céline Buret</name>
                        </respStmt>
                        <funder>
                            <xsl:value-of
                                select="LexicalResource/GlobalInformation/feat[@att='projectName']/@val"
                            />
                        </funder>
                    </titleStmt>
                    <publicationStmt>
                        <distributor> XX </distributor>
                        <availability>
                            <xsl:choose>
                                <xsl:when
                                    test="LexicalResource/GlobalInformation/feat[@att='license']/@val='GPL'">
                                    <licence target="http://www.gnu.org/licenses/gpl.html">
                                        <p>The GNU General Public License applies to this
                                            document.</p>
                                        <p>The material contained in this document must be quoted as
                                            follows: <q><xsl:value-of
                                                  select="LexicalResource/GlobalInformation/feat[@att='bibliographicCitation']/@val"
                                                /></q>.</p>

                                    </licence>
                                </xsl:when>
                                <xsl:otherwise>
                                    <licence target="http://creativecommons.org/licenses/by/4.0/">
                                        <p>The Creative Commons Attribution 4.0 International (CC BY
                                            4.0) Licence applies to this document.</p>
                                        <p>The material contained in this document must be quoted as
                                            follows: <q><xsl:value-of
                                                  select="LexicalResource/GlobalInformation/feat[@att='bibliographicCitation']/@val"
                                                /></q>.</p>
                                    </licence>
                                </xsl:otherwise>
                            </xsl:choose>
                        </availability>
                    </publicationStmt>
                    <sourceDesc>
                        <recordingStmt>
                            <recording>
                                <media mimeType="audio/wav" url="audioSource.wav" dur="PT13M">
                                    <desc>The speech source file for this dialogue</desc>
                                </media>
                            </recording>
                        </recordingStmt>
                    </sourceDesc>
                </fileDesc>
                <profileDesc>
                    <particDesc>
                        <person xml:id="ARI">
                            <persName>
                                <forename>X</forename>
                                <surname>Y</surname>
                            </persName>
                        </person>

                    </particDesc>
                </profileDesc>
                <revisionDesc>
                    <change
                        when="{LexicalResource/GlobalInformation/feat[@att='creationDate']/@val}">
                        last update </change>
                    <change when="{LexicalResource/GlobalInformation/feat[@att='lastUpdate']/@val}">
                        creation date </change>
                </revisionDesc>
            </teiHeader>
            <text>
                <body>
                    <xsl:apply-templates select="LexicalResource/Lexicon"/>
                </body>
            </text>
        </TEI>
    </xsl:template>

    <xsl:template match="Lexicon">
        <div type="lexicon" xml:lang="{feat[@att='language']/@val}">
            <xsl:if test="feat[@att='label']">
                <head>
                    <xsl:value-of select="feat[@att='label']/@val"/>
                </head>
            </xsl:if>
            <xsl:if test="feat[@att='lexiconType']">
                <head type="sub">
                    <xsl:value-of select="feat[@att='lexiconType']/@val"/>
                </head>
            </xsl:if>
            <xsl:apply-templates/>

        </div>
    </xsl:template>

    <xsl:template match="LexicalEntry">
        <entry xml:id="{@id}">
            <xsl:apply-templates/>
        </entry>
    </xsl:template>

    <xsl:template match="LexicalEntry/feat[@att='bibliography']">
        <note type="bibliography">
            <xsl:value-of select="@val"/>
        </note>
    </xsl:template>



    <xsl:template match="Lemma">
        <form>
            <orth>
                <xsl:value-of select="feat[@att='lexeme']/@val"/>
            </orth>
            <xsl:apply-templates select="FormRepresentation"/>
            <gramGrp>
                <xsl:apply-templates select="parent::LexicalEntry/feat[@att='partOfSpeech']"
                    mode="inForm"/>
            </gramGrp>
        </form>
    </xsl:template>

    <xsl:template match="FormRepresentation">
        <xsl:choose>
            <xsl:when test="feat[@att='type']/@val='phonetics'">
                <!-- Il s'agit juste d'une variante phonétique -->
                <pron> </pron>
            </xsl:when>
        </xsl:choose>
    </xsl:template>

    <xsl:template match="Audio">
        <media mimeType="{feat[@att='mediaType']/@val}/{feat[@att='audioFileFormat']/@val}"
            url="{feat[@att='fileName']/@val}" dur="PT10S">
            <desc>Ten seconds of bellringing sound</desc>
        </media>
    </xsl:template>


    <xsl:template match="LexicalEntry/feat[@att='partOfSpeech']"/>

    <xsl:template match="LexicalEntry/feat[@att='partOfSpeech']" mode="inForm">
        <pos>
            <xsl:value-of select="@val"/>
        </pos>
    </xsl:template>


    <xsl:template match="Sense">
        <sense xml:id="{@id}">
            <xsl:apply-templates/>
        </sense>
    </xsl:template>

    <xsl:template match="Sense/Definition[feat/@att='gloss']">
        <gloss xml:lang="{feat[@att='language']/@val}">
            <xsl:value-of select="feat[@att='gloss']/@val"/>
        </gloss>
    </xsl:template>

    <xsl:template match="Sense/Context[feat/@val='example']">
        <cit type="example">
            <quote xml:lang="{TextRepresentation[1]/feat[@att='language']/@val}">
                <xsl:value-of select="TextRepresentation[1]/feat[@att='writtenForm']/@val"/>
            </quote>
            <xsl:apply-templates select="TextRepresentation[position()>1]"/>
        </cit>
    </xsl:template>

    <xsl:template match="TextRepresentation">
        <cit type="translation" xml:lang="{feat[@att='language']/@val}">
            <quote>
                <xsl:value-of select="feat[@att='writtenForm']/@val"/>
            </quote>
        </cit>
    </xsl:template>
    
    <xsl:template match="SubjectField">
        <usg type="dom" xml:lang="{feat[@att='language']/@val}">
            <xsl:value-of select="feat[@att='semanticDomain']/@val"></xsl:value-of>
        </usg>
    </xsl:template>


</xsl:stylesheet>
