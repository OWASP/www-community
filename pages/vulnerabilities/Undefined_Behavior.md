---

layout: col-sidebar
title: Undefined Behavior
author: 
contributors: 
permalink: /vulnerabilities/Undefined_Behavior
tags: vulnerability, Undefined Behavior
auto-migrated: 1

---

{% include writers.html %}

## Description

The behavior of this function is undefined unless its control parameter
is set to a specific value.

The Linux Standard Base Specification 2.0.1 for libc places constraints
on the arguments to some internal functions \[1\]. If the constraints
are not met, the behavior of the functions is not defined.

It is unusual for this function to be called directly. It is almost
always invoked through a macro defined in a system header file, and the
macro ensures that the following constraints are met:

The value 1 must be passed to the third parameter (the version number)
of the following file system function:

```
    __xmknod
```

The value 2 must be passed to the third parameter (the group argument)
of the following wide character string functions:

```
    __wcstod_internal
    __wcstof_internal
    __wcstol_internal
    __wcstold_internal
    __wcstoul_internal
```

The value 3 must be passed as the first parameter (the version number)
of the following file system functions:

```
    __xstat
    __lxstat
    __fxstat
    __xstat64
    __lxstat64
    __fxstat64
```

## Risk Factors

TBD

## Examples

### Short example name

  -
    A short example description, small picture, or sample code with
    [links](http://www.site.com)

### Short example name

  -
    A short example description, small picture, or sample code with
    [links](http://www.site.com)

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

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

  - \[1\] The Linux Standard Base Specification 2.0.1, Interfaces
    Definitions for libc.
    <http://www.linuxbase.org/spec/refspecs/LSB_1.2.0/gLSB/libcman.html>.

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
[Category:General Logic Error
Vulnerability](Category:General_Logic_Error_Vulnerability "wikilink")
[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:Unix](Category:Unix "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")