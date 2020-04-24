---

layout: col-sidebar
title: Unsafe use of Reflection
author: 
contributors: 
permalink: /vulnerabilities/Unsafe_use_of_Reflection
tags: vulnerability, Unsafe use of Reflection
auto-migrated: 1

---

{% include writers.html %}
Last revision (mm/dd/yyyy): **06-29-2016**

## Description

This vulnerability is caused by unsafe use of the reflection mechanisms
in programming languages like Java or C\#.

An attacker may be able to create unexpected control flow paths through
the application, potentially bypassing security checks. Exploitation of
this weakness can result in a limited form of code injection.

## Risk Factors

If an attacker can supply values that the application then uses to
determine which class to instantiate or which method to invoke, the
potential exists for the attacker to create control flow paths through
the application that were not intended by the application developers.
This attack vector may allow the attacker to bypass authentication or
access control checks or otherwise cause the application to behave in an
unexpected manner.

This situation becomes a doomsday scenario if the attacker can upload
files into a location that appears on the application's classpath or add
new entries to the application's classpath. Under either of these
conditions, the attacker can use reflection to introduce new, presumably
malicious, behavior into the application.

## Examples

A common reason that programmers use the reflection API is to implement
their own command dispatcher. The following example shows a command
dispatcher that does not use reflection:

```
    String ctl = request.getParameter("ctl");
    Worker ao = null;
    if (ctl.equals("Add")) {
      ao = new AddCommand();
    } else if (ctl.equals("Modify")) {
      ao = new ModifyCommand();
    } else {
      throw new UnknownActionError();
    }
    ao.doAction(request);
```

A programmer might refactor this code to use reflection as follows:

```
    String ctl = request.getParameter("ctl");
    Class cmdClass = Class.forName(ctl + "Command");
    Worker ao = (Worker) cmdClass.newInstance();
    ao.doAction(request);
```

The refactoring initially appears to offer a number of advantages. There
are fewer lines of code, the if/else blocks have been entirely
eliminated, and it is now possible to add new command types without
modifying the command dispatcher.

However, the refactoring allows an attacker to instantiate any object
that implements the Worker interface. If the command dispatcher is still
responsible for access control, then whenever programmers create a new
class that implements the Worker interface, they must remember to modify
the dispatcher's access control code. If they fail to modify the access
control code, then some Worker classes will not have any access control.

One way to address this access control problem is to make the Worker
object responsible for performing the access control check. An example
of the re-refactored code follows:

```
    String ctl = request.getParameter("ctl");
    Class cmdClass = Class.forName(ctl + "Command");
    Worker ao = (Worker) cmdClass.newInstance();
    ao.checkAccessControl(request);
    ao.doAction(request);
```

Although this is an improvement, it encourages a decentralized approach
to access control, which makes it easier for programmers to make access
control mistakes.

This code also highlights another security problem with using reflection
to build a command dispatcher. An attacker can invoke the default
constructor for any kind of object. In fact, the attacker is not even
constrained to objects that implement the Worker interface; the default
constructor for any object in the system can be invoked. If the object
does not implement the Worker interface, a ClassCastException will be
thrown before the assignment to ao, but if the constructor performs
operations that work in the attacker's favor, the damage will already
have been done. Although this scenario is relatively benign in simple
applications, in larger applications where complexity grows
exponentially it is not unreasonable that an attacker could find a
constructor to leverage as part of an attack.

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

1.  CWE-470: Use of Externally-Controlled Input to Select Classes or
    Code ('Unsafe Reflection')
    <https://cwe.mitre.org/data/definitions/470.html>
2.  Wikipedia: Reflection
    <https://en.wikipedia.org/wiki/Reflection_%28computer_programming%29>

__NOTOC__

[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:Use of Dangerous
API](Category:Use_of_Dangerous_API "wikilink")
[Category:Java](Category:Java "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")