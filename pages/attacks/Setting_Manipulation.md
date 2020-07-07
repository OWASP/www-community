---

layout: col-sidebar
title: Setting Manipulation
author: 
contributors: 
permalink: /attacks/Setting_Manipulation
tags: attack, Setting Manipulation
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack aims to modify application settings in order to cause
misleading data or advantages on the attacker's behalf. They may
manipulate values in the system and manage specific user resources of
the application or affect its functionalities.

An attacker can exploit several functionalities of the application using
this attack technique, but it would not possible to describe all the
ways of exploration, due to innumerable options that attacker may use to
control the system values.

Using this attack technique, it is possible to manipulate settings by
changing the application functions, such as calls to the database,
blocking access to external libraries, and/or modification log files.

## Risk Factors

TBD

## Example

### Example 1

An attacker needs to identify the variables without input validation or
those improperly encapsulated to obtain success in the attack.

The following example was based on those found in the Individual CWE
Dictionary Definition (Setting Manipulation-15).

Consider the following piece of Java code:

` …`
` conn.setCatalog(request.getParameter(“catalog”));`
` ...`

This fragment reads the string “catalog” from “HttpServletRequest” and
sets it as the active catalog for a database connection. An attacker
could manipulate this information and cause a connection error or
unauthorized access to other catalogs.

### Example 2 – Block Access to Libraries

The attacker has the privileges to block application access to external
libraries to execute this attack. It is necessary to discover what
external libraries are accessed by the application and block them. The
attacker needs to observe if the behavior of the system goes into an
insecure/inconsistent state.

In this case the application uses a third party cryptographic random
number generation library to generate user Session IDs. An attacker may
block access to this library by renaming it. Then the application will
use the weak pseudo random number generation library. The attacker can
use this weakness to predict the Session ID user; they attempt to
perform elevation of privilege escalation and gains access to the user's
account.

For more details about this attack, see:
<http://capec.mitre.org/data/definitions/96.html>

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category: Logical Attacks](:Category:_Logical_Attacks "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Denial of Service](Denial_of_Service "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:General Logic Error
    Vulnerability](:Category:General_Logic_Error_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Error Handling](:Category:_Error_Handling "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/15.html> - Setting
    Manipulation
  - <http://capec.mitre.org/data/definitions/13.html> - Subverting
    Environment Variable Values
  - <http://capec.mitre.org/data/definitions/96.html> - Block Access to
    Libraries

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category: Resource
Manipulation](Category:_Resource_Manipulation "wikilink") [Category:
Attack](Category:_Attack "wikilink")