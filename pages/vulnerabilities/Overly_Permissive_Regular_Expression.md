---

layout: col-sidebar
title: Overly Permissive Regular Expression
author: 
contributors: 
permalink: /vulnerabilities/Overly_Permissive_Regular_Expression
tags: vulnerability, Overly Permissive Regular Expression
auto-migrated: 1

---

{% include writers.html %}

## Description

The tested application is using a regular expression that is to broad in
scope for the sufficient restriction of the set of allowed values.

## Risk Factors

Overly Permissive Regular Expressions are a very common flaw in
applications where regular expressions are used to restrict user input.
Because of their overall complexity, developers using regular
expressions will often use the wildcard character, or fail to restrict
the number of characters allowed in the request.

This exploit is the opening that a malicious user needs to begin an
injection attack, either client or server side. When an attacker can get
inappropriate values into the backend processing system, there is much
more of a chance of finding an injection flaw in a system.

## Examples

For example, consider this expression to match a floating point number
in text:

`   [-+]?([0-9])*\.?([0-9]*)`

While it does allow for floating point numbers, the greedy \* token will
allow for the pattern to start anywhere in the string, leaving an
opening for injection.

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Cross-site Scripting
    (XSS)](Cross-site_Scripting_\(XSS\) "wikilink")
  - [Regular expression Denial of Service -
    ReDoS](Regular_expression_Denial_of_Service_-_ReDoS "wikilink")
  - [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Input Validation](Input_Validation "wikilink")

## References

  - [CWE 625](http://cwe.mitre.org/data/definitions/625.html)

[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")