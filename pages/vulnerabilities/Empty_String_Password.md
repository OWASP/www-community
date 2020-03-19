---

layout: col-sidebar
title: Empty String Password
author: 
contributors: 
permalink: /vulnerabilities/Empty_String_Password
tags: vulnerability, Empty String Password
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Using an empty string as a password is insecure.

It is never appropriate to use an empty string as a password. It is too
easy to guess. An empty string password makes the authentication as weak
as the user names, which are normally public or guessable. This makes a
brute-force attack against the login interface much easier.

## Risk Factors

TBD

## Examples

TBD

## Related [Attacks](Attacks "wikilink")

  - [Brute force attack](Brute_force_attack "wikilink") against
    application log in interface.

## Related [Vulnerabilities](Vulnerabilities "wikilink")

  - [Weak Passwords](Weak_Passwords "wikilink")

## Related [Controls](Controls "wikilink")

  - [:Category:Authentication](:Category:Authentication "wikilink")
  - [Strong Password Policy](Strong_Password_Policy "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Password Management
Vulnerability](Category:Password_Management_Vulnerability "wikilink")
[Category:Authentication
Vulnerability](Category:Authentication_Vulnerability "wikilink")
[Category:Environmental
Vulnerability](Category:Environmental_Vulnerability "wikilink")
[Category:Deployment](Category:Deployment "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")