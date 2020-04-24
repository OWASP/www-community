---

layout: col-sidebar
title: Missing XML Validation
author: 
contributors: 
permalink: /vulnerabilities/Missing_XML_Validation
tags: vulnerability, Missing XML Validation

---

{% include writers.html %}

## Description

Failure to enable validation when parsing XML gives an attacker the opportunity to supply malicious input.

Most successful attacks begin with a violation of the programmer's assumptions. By accepting an XML document without validating it against a DTD or XML schema, the programmer leaves a door open for attackers to provide unexpected, unreasonable, or malicious input. It is not possible for an XML parser to validate all aspects of a document's content; a parser cannot understand the complete semantics of the data. However, a parser can do a complete and thorough job of checking the document's structure and therefore guarantee to the code that processes the document that the content is well-formed.

## Risk Factors

- Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology) that make this vulnerability likely or unlikely to actually happen
- Discuss the technical impact of a successful exploit of this vulnerability
- Consider the likely business impacts of a successful attack

## Examples

## Related [Attacks](../attacks/)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References