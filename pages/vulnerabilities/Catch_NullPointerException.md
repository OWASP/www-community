---

layout: col-sidebar
title: Catch NullPointerException
author: 
contributors: 
permalink: /vulnerabilities/Catch_NullPointerException
tags: vulnerability, Catch NullPointerException

---

{% include writers.html %}

## Description

It is generally a bad practice to catch NullPointerException.

Programmers typically catch NullPointerException under three circumstances:

1.  The program contains a null pointer dereference. Catching the resulting exception was easier than fixing the underlying problem.
2.  The program explicitly throws a NullPointerException to signal an error condition.
3.  The code is part of a test harness that supplies unexpected input to the classes under test.

Of these three circumstances, only the last is acceptable.

## Risk Factors

TBD

## Examples

The following code mistakenly catches a NullPointerException.

```
try {
  mysteryMethod();
} catch (NullPointerException npe) {
  ...
}
```

## Related [Attacks](../attacks/)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

Note: A reference to related [CWE](http://cwe.mitre.org/) or [CAPEC](http://capec.mitre.org/) article should be added when exists.
Eg:

- [CWE 79](http://cwe.mitre.org/data/definitions/79.html).
