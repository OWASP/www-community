---

layout: col-sidebar
title: Parameter Delimiter
author: 
contributors: 
permalink: /attacks/Parameter_Delimiter
tags: attack, Parameter Delimiter
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack is based on the manipulation of parameter delimiters used by
web application input vectors in order to cause unexpected behaviors
like access control and authorization bypass and information disclosure,
among others.

## Risk Factors

TBD

## Examples

In order to illustrate this vulnerability, we will use a vulnerability
found on Poster V2, a posting system based on PHP programming language.

This application has a dangerous vulnerability that allows inserting
data into user fields (username, password, email address and privileges)
in “mem.php” file, which is responsible for managing the application
user.

An example of the file “mem.php”, where user Jose has admin privileges
and Alice user access:

`<?`
`Jose|12345678|jose@attack.com|admin|`
`Alice|87654321|alice@attack.com|normal|`
`?>`

When a user wants to edit their profile, they must use the "edit account”
option in the “index.php” page and enter their login information. However,
using “|” as a parameter delimiter on email field followed by “admin”,
the user could elevate their privileges to administrator. Example:

`Username: Alice`
`Password: 87654321`
`Email: alice@attack.com |admin| `

This information will be recorded in “mem.php” file like this:

`Alice|87654321|alice@attack.com|admin|normal|`

In this case, the last parameter delimiter considered is “|admin|” and
the user could elevate their privileges by assigning administrator
profile.

Although this vulnerability doesn’t allow manipulation of other users'
profiles, it allows privilege escalation for application users.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category: Authorization](:Category:_Authorization "wikilink")
  - [:Category: Command
    Execution](:Category:_Command_Execution "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [:Category:Injection Attack](:Category:Injection_Attack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Input
    Validation](:Category:_Input_Validation "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/141.html>
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0307>

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
[Category:Attack](Category:Attack "wikilink")