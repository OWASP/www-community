---

layout: col-sidebar
title: CRLF Injection.md
author: 
contributors: 
permalink: /vulnerabilities/CRLF_Injection
tag: vulnerability, CRLF Injection.md
auto-migrated: 1

---

Last revision (mm/dd/yy): **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

The term CRLF refers to **C**arriage **R**eturn (ASCII 13, \\r) **L**ine
**F**eed (ASCII 10, \\n). They're used to note the termination of a
line, however, dealt with differently in today’s popular Operating
Systems. For example: in Windows both a CR and LF are required to note
the end of a line, whereas in Linux/UNIX a LF is only required. In the
HTTP protocol, the CR-LF sequence is always used to terminate a line.

A CRLF Injection attack occurs when a user manages to submit a CRLF into
an application. This is most commonly done by modifying an HTTP
parameter or URL.

## Risk Factors

TBD

## Examples

Depending on how the application is developed, this can be a minor
problem or a fairly serious security flaw. Let's look at the latter
because this is after all a security related post.

Let's assume a file is used at some point to read/write data to a log of
some sort. If an attacker managed to place a CRLF then can then inject
some sort of read programmatic method to the file. This could result in
the contents being written to screen on the next attempt to use this
file.

Another example is the "response splitting" attacks, where CRLFs are
injected into an application and included in the response. The extra
CRLFs are interpreted by proxies, caches, and maybe browsers as the end
of a packet, causing mayhem.

## Related [Attacks](Attacks "wikilink")

  - [HTTP Response Splitting](HTTP_Response_Splitting "wikilink")
  - [Log Injection](Log_Injection "wikilink")

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

TBD

\[\[Category:FIXME|add links In addition, one should classify
vulnerability based on the following subcategories:
Ex:\[\[Category:Error_Handling_Vulnerability|Category:Error Handling
Vulnerability\]\]

Availability Vulnerability Authorization Vulnerability Authentication
Vulnerability Concurrency Vulnerability Configuration Vulnerability
Cryptographic Vulnerability Encoding Vulnerability Error Handling
Vulnerability Input Validation Vulnerability Logging and Auditing
Vulnerability Session Management Vulnerability\]\]

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Implementation](Category:Implementation "wikilink")