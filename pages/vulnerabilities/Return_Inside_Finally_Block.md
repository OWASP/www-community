---

layout: col-sidebar
title: Return Inside Finally Block
author: 
contributors: 
permalink: /vulnerabilities/Return_Inside_Finally_Block
tags: vulnerability, Return Inside Finally Block
auto-migrated: 1

---

{% include writers.html %}

## Description

Returning from inside a finally block will cause exceptions to be lost.

A return statement inside a finally block will cause any exception that
might be thrown in the try block to be discarded.

## Risk Factors

TBD

## Examples

In the following code excerpt, the IllegalArgumentException will never
be delivered to the caller. The finally block will cause the exception
to be discarded.

```
    try {
      ...
      throw IllegalArgumentException();
    }
    finally {
      return r;
    }
```

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Error Handling](Error_Handling "wikilink")

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
[Category:Java](Category:Java "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")