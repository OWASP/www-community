---

layout: col-sidebar
title: Insecure Transport
author: 
contributors: 
permalink: /vulnerabilities/Insecure_Transport
tag: vulnerability, Insecure Transport
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

The application configuration should ensure that SSL is used for all
access controlled pages.

If an application uses SSL to guarantee confidential communication with
client browsers, the application configuration should make it impossible
to view any access controlled page without SSL. However, it is not an
uncommon problem that the configuration of the application fails to
enforce the use of SSL on pages that contain sensitive data.

There are three common ways for SSL to be bypassed:

  - A user manually enters the URL and types "HTTP" rather than "HTTPS".
  - Attackers intentionally send a user to an insecure URL.
  - A programmer erroneously creates a relative link to a page in the
    application, failing to switch from HTTP to HTTPS. (This is
    particularly easy to do when the link moves between public and
    secured areas on a web site.)

## Risk Factors

TBD

## Examples

  - Login pages are not SSL protected
  - A publicly accessible page contains a relative link to a protected
    page which forgets to switch to SSL.

## Related [Attacks](Attacks "wikilink")

  - Attackers that are trying to steal login credentials, session IDs or
    other sensitive information
  - Bypassing SSL by entering HTTP instead of HTTPS
  - Sending insecure URLs of protected pages to the victim (e.g. login
    page) to trick the victim into accessing the privileged pages via
    HTTP

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
[Category:Deployment](Category:Deployment "wikilink")
[Category:Java](Category:Java "wikilink") [Category:Environmental
Vulnerability](Category:Environmental_Vulnerability "wikilink")
[Category:Communication](Category:Communication "wikilink")
[Category:SSL](Category:SSL "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")