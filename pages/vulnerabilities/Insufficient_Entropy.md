---

layout: col-sidebar
title: Insufficient Entropy
author: 
contributors: 
permalink: /vulnerabilities/Insufficient_Entropy
tags: vulnerability, Insufficient Entropy
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

When an undesirably low amount of entropy is available. Psuedo Random
Number Generators are susceptible to suffering from insufficient entropy
when they are initialized, because entropy data may not be available to
them yet.

## Risk Factors

TBD

## Examples

TBD

## Related [Attacks](Attacks "wikilink")

  - In many case,s a PRNG uses a combination of the system clock and
    entropy to create seed data. If insufficient entropy is available,
    an attacker can reduce the size magnitude of the seed value
    considerably. Furthermore, by guessing values of the system clock,
    they can create a manageable set of possible PRNG outputs.

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](Controls "wikilink")

  - Many PRNG's (/dev/random and /dev/urandom for example) store their
    last value before shutdown. By using this value at intialization,
    they can sometimes avoid insufficient or predictable starting
    entropy.

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Cryptographic
Vulnerability](Category:Cryptographic_Vulnerability "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")