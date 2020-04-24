---

layout: col-sidebar
title: Null Dereference
author: 
contributors: 
permalink: /vulnerabilities/Null_Dereference
tags: vulnerability, Null Dereference
auto-migrated: 1

---

{% include writers.html %}

# Description

The program can potentially dereference a null pointer, thereby raising
a NullPointerException. Null pointer errors are usually the result of
one or more programmer assumptions being violated. Most null pointer
issues result in general software reliability problems, but if an
attacker can intentionally trigger a null pointer dereference, the
attacker might be able to use the resulting exception to bypass security
logic or to cause the application to reveal debugging information that
will be valuable in planning subsequent attacks.

A null-pointer dereference takes place when a pointer with a value of
NULL is used as though it pointed to a valid memory area.

Null-pointer dereferences, while common, can generally be found and
corrected in a simple way. They will always result in the crash of the
process, unless exception handling (on some platforms) is invoked, and
even then, little can be done to salvage the process.

# Consequences

  - Availability: Null-pointer dereferences invariably result in the
    failure of the process.

# Exposure period

  - Requirements specification: The choice could be made to use a
    language that is not susceptible to these issues.
  - Implementation: Proper sanity checks at implementation time can
    serve to prevent null-pointer dereferences

# Platform

  - Languages: C, C++, Java, Assembly
  - Platforms: All

# Examples

## Example 1

In the following code, the programmer assumes that the system always has
a property named "cmd" defined. If an attacker can control the program's
environment so that "cmd" is not defined, the program throws a null
pointer exception when it attempts to call the trim() method.

`   String cmd = System.getProperty("cmd");`
`   cmd = cmd.trim();`

## Example 2

Null-pointer dereference issues can occur through a number of flaws,
including race conditions and simple programming omissions. While there
are no complete fixes aside from contentious programming, the following
steps will go a long way to ensure that null-pointer dereferences do not
occur.

Before using a pointer, ensure that it is not equal to NULL:

    if (pointer1 != NULL) {
      /* make use of pointer1 */
      /* ... */
    }

When freeing pointers, ensure they are not set to NULL, and be sure to
set them to NULL once they are freed:

    if (pointer1 != NULL) {
      free(pointer1);
      pointer1 = NULL;
    }

If you are working with a multi-threaded or otherwise asynchronous
environment, ensure that proper locking APIs are used to lock before the
if statement; and unlock when it has finished.

# Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Miscalculated null
    termination](Miscalculated_null_termination "wikilink")
  - [State synchronization
    error](State_synchronization_error "wikilink")

# Related [Controls](https://owasp.org/www-community/controls/)

  - Requirements specification: The choice could be made to use a
    language that is not susceptible to these issues.
  - Implementation: If all pointers that could have been modified are
    sanity-checked previous to use, nearly all null-pointer dereferences
    can be prevented.

# References

  - [CWE 79](http://cwe.mitre.org/data/definitions/79.html).
  - <http://www.link1.com>
  - [Title for the link2](http://www.link2.com)

[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")