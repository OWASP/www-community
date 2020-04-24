---

layout: col-sidebar
title: Using a broken or risky cryptographic algorithm
author: 
contributors: 
permalink: /vulnerabilities/Using_a_broken_or_risky_cryptographic_algorithm
tags: vulnerability, Using a broken or risky cryptographic algorithm
auto-migrated: 1

---

{% include writers.html %}

## Description

Attempting to create non-standard and non-tested algorithms, using weak
algorithms, or applying algorithms incorrectly will pose a high weakness
to data that is meant to be secure.

**Consequences**

  - Confidentiality: The confidentiality of sensitive data may be
    compromised by the use of a broken or risky cryptographic algorithm.
  - Integrity: The integrity of sensitive data may be compromised by the
    use of a broken or risky cryptographic algorithm.
  - Accountability: Any accountability to message content preserved by
    cryptography may be subject to attack.

**Exposure period**

  - Design: The decision as to what cryptographic algorithm to utilize
    is generally made at design time.

**Platform**

  - Languages: All
  - Operating platforms: All

**Required resources**

Any

**Severity**

High

**Likelihood of exploit**

Medium to High

Since the state of cryptography advances so rapidly, it is common to
find algorithms, which previously were considered to be safe, currently
considered unsafe. In some cases, things are discovered, or processing
speed increases to the degree that the cryptographic algorithm provides
little more benefit than the use of no cryptography at all.

## Risk Factors

  - Use of custom cryptographic algorithms.
  - Use of weak and/or untested public algorithms.

## Examples

In C/C++:

    EVP_des_ecb();

In Java:

    Cipher des=Cipher.getInstance("DES...);
    des.initEncrypt(key2);

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Failure to encrypt data](Failure_to_encrypt_data "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - Design: Use a cryptographic algorithm that is currently considered
    to be strong by experts in the field.

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Cryptographic
Vulnerability](Category:Cryptographic_Vulnerability "wikilink")