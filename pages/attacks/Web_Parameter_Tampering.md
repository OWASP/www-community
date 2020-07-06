---

layout: col-sidebar
title: Web Parameter Tampering
author: 
contributors: 
permalink: /attacks/Web_Parameter_Tampering
tags: attack, Web Parameter Tampering
auto-migrated: 1

---

{% include writers.html %}

## Description

The Web Parameter Tampering attack is based on the manipulation of
parameters exchanged between client and server in order to modify
application data, such as user credentials and permissions, price and
quantity of products, etc. Usually, this information is stored in
cookies, hidden form fields, or URL Query Strings, and is used to
increase application functionality and control.

This attack can be performed by a malicious user who wants to exploit
the application for their own benefit, or an attacker who wishes to
attack a third-person using a [Man-in-the-middle
attack](Man-in-the-middle_attack "wikilink"). In both cases, tools likes
Webscarab and Paros proxy are mostly used.

The attack success depends on integrity and logic validation mechanism
errors, and its exploitation can result in other consequences including
[XSS](Cross-site_Scripting_\(XSS\) "wikilink"), [SQL
Injection](https://owasp.org/www-community/attacks/SQL_Injection), file inclusion, and path
disclosure attacks.

For a short video clip describing the vulnerability, [click
here](http://www.youtube.com/watch?v=l5LCDEDn7FY&hd=1) (Courtesy of
[Checkmarx](http://www.checkmarx.com/))

## Examples

### Example 1

The parameter modification of form fields can be considered a typical
example of Web Parameter Tampering attack.

For example, consider a user who can select form field values (combo
box, check box, etc.) on an application page. When these values are
submitted by the user, they could be acquired and arbitrarily
manipulated by an attacker.

### Example 2

When a web application uses hidden fields to store status information, a
malicious user can tamper with the values stored on their browser and
change the referred information. For example, an e-commerce shopping
site uses hidden fields to refer to its items, as follows:

<input type=”hidden” id=”1008” name=”cost” value=”70.00”>

In this example, an attacker can modify the “value” information of a
specific item, thus lowering its cost.

### Example 3

An attacker can tamper with URL parameters directly. For example,
consider a web application that permits a user to select their profile
from a combo box and debit the account:

`http://www.attackbank.com/default.asp?profile=741&debit=1000`

In this case, an attacker could tamper with the URL, using other values
for profile and debit:

`http://www.attackbank.com/default.asp?profile=852&debit=2000`

Other parameters can be changed including attribute parameters. In the
following example, it’s possible to tamper with the status variable and
delete a page from the server:

`http://www.attackbank.com/savepage.asp?nr=147&status=read`

Modifying the status variable to delete the page:

`http://www.attackbank.com/savepage.asp?nr=147&status=del`

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Client-side
    Attacks](:Category:Client-side_Attacks "wikilink")
  - [:Category:Logical Attacks](:Category:Logical_Attacks "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
  - [XSS Attacks](XSS_Attacks "wikilink")
  - [Path Traversal](Path_Traversal "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Input
    Validation](:Category:_Input_Validation "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/472.html> - Web Parameter
    Tampering
  - <http://www.imperva.com/application_defense_center/glossary/parameter_tampering.html>
    - Parameter Tampering Imperva - Application Defense Center
  - <http://www.cgisecurity.com/owasp/html/ch11s04.html> - Parameter
    Manipulation - Chapter 11. Preventing Common Problems

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category: Injection](Category:_Injection "wikilink") [Category:
Attack](Category:_Attack "wikilink")