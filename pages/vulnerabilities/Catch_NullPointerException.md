---

layout: col-sidebar
title: Catch NullPointerException
author: 
contributors: Abdullah Al-Khalaf
permalink: /vulnerabilities/Catch_NullPointerException
tags: vulnerability, Catch NullPointerException

---

{% include writers.html %}

## NVD Categorization

> [CWE-395: Use of NullPointerException Catch to Detect NULL Pointer Dereference](https://cwe.mitre.org/data/definitions/395.html): Catching NullPointerException should not be used as an alternative to programmatic checks to prevent dereferencing a null pointer.

## Description

Catching NullPointerException (NPE) by using a `try`-`catch` statement is a bad practice. It should be avoided whenever possible because catching an NPE creates a new object, which consumes more memory than alternative methods.

Programmers typically catch NullPointerException under three circumstances:

1.  The program contains a null pointer dereference. Catching the resulting exception was easier than fixing the underlying problem.
2.  The program explicitly throws a NullPointerException to signal an error condition.
3.  The code is part of a test harness that supplies unexpected input to the classes under test.

Of these three circumstances, only the last is acceptable.

## Risk Factors

TBD

## Examples

The following code is what a programmer might mistakenly do and should avoid (this is an oversimplified example).

```
try {
		UserSession user = Server.Session.getUserLoginSession();
		Server.sendText("Hello "+ user.getName());
} catch (NullPointerException npe) {
		Server.sendText("Please login")
}
```

The following code is a better alternative that uses an `if` statement and avoids creating an NPE object.
```
UserSession user = Server.Session.getUserLoginSession();
if(user != null){
		Server.sendText("Hello "+ user.getName());
} else {
		Server.sendText("Please login")
}
```

## Related [Attacks](../attacks/)
* [Denial of Service](https://owasp.org/www-community/attacks/Denial_of_Service): Creating NPE object requires computing power and memory

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

- [CWE-395](https://cwe.mitre.org/data/definitions/395.html).

