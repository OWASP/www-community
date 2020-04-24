---

layout: col-sidebar
title: Password Management Hardcoded Password
author: 
contributors: 
permalink: /vulnerabilities/Password_Management_Hardcoded_Password
tags: vulnerability, Password Management Hardcoded Password
auto-migrated: 1

---

{% include writers.html %}

## Description

Hardcoded passwords may compromise system security in a way that cannot
be easily remedied.

It is never a good idea to hardcode a password. Not only does hardcoding
a password allow all of the project's developers to view the password,
it also makes fixing the problem extremely difficult. Once the code is
in production, the password cannot be changed without patching the
software. If the account protected by the password is compromised, the
owners of the system will be forced to choose between security and
availability.

## Risk Factors

TBD

## Examples

The following code uses a hardcoded password to connect to a database:

```
    ...
    DriverManager.getConnection(url, "scott", "tiger");
    ...
```

This code will run successfully, but anyone who has access to it will
have access to the password. Once the program has shipped, there is no
going back from the database user "scott" with a password of "tiger"
unless the program is patched. A devious employee with access to this
information can use it to break into the system. Even worse, if
attackers have access to the bytecode for application, they can use the
javap -c command to access the disassembled code, which will contain the
values of the passwords used. The result of this operation might look
something like the following for the example above:

```
    javap -c ConnMngr.class

    22: ldc   #36; //String jdbc:mysql://ixne.com/rxsql
    24: ldc   #38; //String scott
    26: ldc   #17; //String tiger
```

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

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
[Category:Sensitive Data Protection
Vulnerability](Category:Sensitive_Data_Protection_Vulnerability "wikilink")
[Category:Password Management
Vulnerability](Category:Password_Management_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
