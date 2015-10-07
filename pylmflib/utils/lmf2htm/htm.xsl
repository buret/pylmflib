<?xml version="1.0" encoding="utf-8"?>

<xsl:stylesheet version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

	<xsl:template match="/">
		<html>
			<head>
				<title>
					<!-- Tab title -->
					<xsl:value-of select="//Lexicon/@id"/>
				</title>
			</head>
			<body>
				<h3>
					<!-- Page title -->
					<xsl:value-of select="//Lexicon/feat[@att='label']//@val"/>
				</h3>
				<!-- Display number of entries -->
				<xsl:text>This dictionary contains </xsl:text>
				<xsl:value-of select="count(//Lexicon/LexicalEntry/Lemma)"/>
				<xsl:if test="count(//Lexicon/LexicalEntry/Lemma) = 1">
					<xsl:text> entry.</xsl:text>
				</xsl:if>
				<xsl:if test="count(//Lexicon/LexicalEntry/Lemma) > 1">
					<xsl:text> entries.</xsl:text>
				</xsl:if>
				<p/>
				<!-- Create table -->
				<xsl:element name="table">
					<xsl:attribute name="width">70%</xsl:attribute>
					<xsl:attribute name="border">1</xsl:attribute>
					<xsl:attribute name="align">center</xsl:attribute>
					<tbody>
						<!-- Name of columns -->
						<xsl:element name="tr">
							<xsl:element name="td">
								<xsl:attribute name="width">25%</xsl:attribute>
								<xsl:text>Lexeme</xsl:text>
							</xsl:element>
							<xsl:element name="td">
								<xsl:attribute name="width">20%</xsl:attribute>
								<xsl:text>Part of speech</xsl:text>
							</xsl:element>
							<xsl:element name="td">
								<xsl:attribute name="width">25%</xsl:attribute>
								<xsl:text>Gloss</xsl:text>
							</xsl:element>
							<xsl:element name="td">
								<xsl:attribute name="width">30%</xsl:attribute>
								<xsl:text>Example</xsl:text>
							</xsl:element>
						</xsl:element>
						<xsl:apply-templates select="//Lexicon/LexicalEntry">
							<xsl:sort select="@id" data-type="text"/>
						</xsl:apply-templates>
					</tbody>
				</xsl:element>
			</body>
		</html>
	</xsl:template>

	<xsl:template match="//Lexicon/LexicalEntry">
		<xsl:element name="tr">
			<xsl:for-each select=".">
				<!-- Display lexeme -->
				<xsl:element name="td">
					<xsl:attribute name="width">25%</xsl:attribute>
					<xsl:value-of select="./Lemma/feat[@att='lexeme']//@val"/>
					<!-- Display audio file name -->
					<xsl:for-each select="./Lemma/FormRepresentation/Audio">
						<audio controls="controls" preload="none">
							<source src="{./feat[@att='fileName']//@val}" type="audio/{./feat[@att='audioFileFormat']//@val}"/>
						</audio>
					</xsl:for-each>
				</xsl:element>
				<!-- Display part of speech or '-' if None -->
				<xsl:element name="td">
					<xsl:attribute name="width">20%</xsl:attribute>
					<xsl:value-of select="./feat[@att='partOfSpeech']//@val"/>
					<xsl:if test="not(./feat[@att='partOfSpeech']//@val)">
						<xsl:text>-</xsl:text>
					</xsl:if>
				</xsl:element>
				<!-- Display gloss and language if any -->
				<xsl:element name="td">
					<xsl:attribute name="width">25%</xsl:attribute>
					<xsl:if test="./Sense/Definition/feat[@att='gloss']//@val">
						<xsl:value-of select="./Sense/Definition/feat[@att='gloss']//@val"/>
						<xsl:if test="./Sense/Definition/feat[@att='language']//@val">
							<xsl:text> (</xsl:text>
							<xsl:value-of select="./Sense/Definition/feat[@att='language']//@val"/>
							<xsl:text>) </xsl:text>
						</xsl:if>
					</xsl:if>
					<xsl:if test="not(./Sense/Definition/feat[@att='gloss']//@val)">
						<xsl:text>-</xsl:text>
					</xsl:if>
				</xsl:element>
				<!-- Apply another template to display examples -->
				<xsl:element name="td">
					<xsl:attribute name="width">30%</xsl:attribute>
<!--					<xsl:call-template name="examples"/>-->
					<xsl:apply-templates select="./Sense/Context/TextRepresentation"/>
					<xsl:if test="not(./Sense/Context/TextRepresentation)">
						<xsl:text>-</xsl:text>
					</xsl:if>
				</xsl:element>
			</xsl:for-each>
		</xsl:element>
	</xsl:template>

<!--	<xsl:template name="examples"/>-->
	<xsl:template match="//Lexicon/LexicalEntry/Sense/Context/TextRepresentation">
		<xsl:value-of select="feat[@att='writtenForm']/@val"/>
		<xsl:text> (</xsl:text>
		<xsl:value-of select="feat[@att='language']/@val"/>
		<xsl:text>)</xsl:text>
		<xsl:element name="br"/>
<!--
		<xsl:choose>
			<xsl:when test="">
			</xsl:when>
			<xsl:otherwise>
			</xsl:otherwise>
		</xsl:choose>
-->
	</xsl:template>

</xsl:stylesheet>
