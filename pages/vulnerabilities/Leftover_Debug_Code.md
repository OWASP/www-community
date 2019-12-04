---

layout: col-sidebar
title: Leftover Debug Code.md
author: 
contributors: 
permalink: /vulnerabilities/Leftover_Debug_Code
tag: vulnerability, Leftover Debug Code.md
auto-migrated: 1

---

Last revision (mm/dd/yy): **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Debug code can create unintended entry points in a deployed web
application.

A common development practice is to add "back door" code specifically
designed for debugging or testing purposes that is not intended to be
shipped or deployed with the application. When this sort of debug code
is accidentally left in the application, the application is open to
unintended modes of interaction. These back door entry points create
security risks because they are not considered during design or testing
and fall outside of the expected operating conditions of the
application.

## Risk Factors

TBD

## Examples

The most common example of forgotten debug code is a main() method
appearing in a web application. Although this is an acceptable practice
during product development, classes that are part of a production J2EE
application should not define a main().

## Related [Attacks](Attacks "wikilink")

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](Vulnerabilities "wikilink")

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](Controls "wikilink")

  - [Control 1](Control_1 "wikilink")
  - [Control 2](Control_2 "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

  - [Use encapsulation](Use_encapsulation "wikilink")

\[\[Category:FIXME|add links

In addition, one should classify vulnerability based on the following
subcategories:
Ex:\[\[Category:Error_Handling_Vulnerability|Category:Error Handling
Vulnerability\]\]

Availability Vulnerability

Authorization Vulnerability

Authentication Vulnerability

Concurrency Vulnerability

Configuration Vulnerability

Cryptographic Vulnerability

Encoding Vulnerability

Error Handling Vulnerability

Input Validation Vulnerability

Logging and Auditing Vulnerability

Session Management Vulnerability\]\]

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Java](Category:Java "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")