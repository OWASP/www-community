---

layout: col-sidebar
title: Missing XML Validation
author: 
contributors: 
permalink: /vulnerabilities/Missing_XML_Validation
tags: vulnerability, Missing XML Validation
auto-migrated: 1

---

Last page edit: **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Failure to enable validation when parsing XML gives an attacker the
opportunity to supply malicious input.

Most successful attacks begin with a violation of the programmer's
assumptions. By accepting an XML document without validating it against
a DTD or XML schema, the programmer leaves a door open for attackers to
provide unexpected, unreasonable, or malicious input. It is not possible
for an XML parser to validate all aspects of a document's content; a
parser cannot understand the complete semantics of the data. However, a
parser can do a complete and thorough job of checking the document's
structure and therefore guarantee to the code that processes the
document that the content is well-formed.

## Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

## Examples

### Short example name

  -
    A short example description, small picture, or sample code with
    [links](http://www.site.com)

### Short example name

  -
    A short example description, small picture, or sample code with
    [links](http://www.site.com)

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TODO

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:XML](Category:XML "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")