---

layout: col-sidebar
title: PRNG Seed Error
author: 
contributors: 
permalink: /vulnerabilities/PRNG_Seed_Error
tags: vulnerability, PRNG Seed Error
auto-migrated: 1

---

{% include writers.html %}

## Description

The incorrect use of a seed by a Psuedo Random Number Generator
[1](http://cwe.mitre.org/data/definitions/335.html). A seed error is
usually brought on through the erroneous generation or application of a
seed state.

## Risk Factors

TBD

## Examples

TBD

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

The application of a seed state that is known to an attacker can lead to
a permanent compromise attack
[2](http://www.schneier.com/paper-prngs.html).

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Control 1](Control_1 "wikilink")
  - [Control 2](Control_2 "wikilink")

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
[Category:Cryptographic
Vulnerability](Category:Cryptographic_Vulnerability "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")