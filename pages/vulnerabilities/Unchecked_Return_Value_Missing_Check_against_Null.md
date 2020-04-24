---

layout: col-sidebar
title: Unchecked Return Value Missing Check against Null
author: 
contributors: 
permalink: /vulnerabilities/Unchecked_Return_Value_Missing_Check_against_Null
tags: vulnerability, Unchecked Return Value Missing Check against Null
auto-migrated: 1

---

{% include writers.html %}

## Description

Ignoring a method's return value can cause the program to overlook
unexpected states and conditions.

Just about every serious attack on a software system begins with the
violation of a programmer's assumptions. After the attack, the
programmer's assumptions seem flimsy and poorly founded, but before an
attack many programmers would defend their assumptions well past the end
of their lunch break.

Two dubious assumptions that are easy to spot in code are "this function
call can never fail" and "it doesn't matter if this function call
fails". When a programmer ignores the return value from a function, they
implicitly state that they are operating under one of these assumptions.

## Risk Factors

TBD

## Examples

The following code does not check to see if the string returned by
getParameter() is null before calling the member function compareTo(),
potentially causing a null dereference.

```
    String itemName = request.getParameter(ITEM_NAME);
    if (itemName.compareTo(IMPORTANT_ITEM)) {
        ...
    }
    ...
```

The traditional defense of this coding error is:

    "I know the requested value will always exist because ... If it does not exist, the program
    cannot perform the desired behavior so it doesn't matter whether I handle the error or simply
    allow the program to die dereferencing a null value."

But attackers are skilled at finding unexpected paths through programs,
particularly when exceptions are involved.

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Ignored function return
    value](Ignored_function_return_value "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
