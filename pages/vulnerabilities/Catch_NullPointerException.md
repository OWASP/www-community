---

layout: col-sidebar
title: Catch NullPointerException
author: 
contributors: 
permalink: /vulnerabilities/Catch_NullPointerException
tags: vulnerability, Catch NullPointerException
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

It is generally a bad practice to catch NullPointerException.

Programmers typically catch NullPointerException under three
circumstances:

1.  The program contains a null pointer dereference. Catching the
    resulting exception was easier than fixing the underlying problem.
2.  The program explicitly throws a NullPointerException to signal an
    error condition.
3.  The code is part of a test harness that supplies unexpected input to
    the classes under test.

Of these three circumstances, only the last is acceptable.

## Risk Factors

TBD

## Examples

The following code mistakenly catches a NullPointerException.

```
      try {
        mysteryMethod();
      }
      catch (NullPointerException npe) {
      }
```

## Related [Attacks](Attacks "wikilink")

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](Controls "wikilink")

  - [:Category:Error Handling](:Category:Error_Handling "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

Note: A reference to related [CWE](http://cwe.mitre.org/) or
[CAPEC](http://capec.mitre.org/) article should be added when exists.
Eg:

  - [CWE 79](http://cwe.mitre.org/data/definitions/79.html).
  - <http://www.link1.com>
  - [Title for the link2](http://www.link2.com)

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Error Handling
Vulnerability](Category:Error_Handling_Vulnerability "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")