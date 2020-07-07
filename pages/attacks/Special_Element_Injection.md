---

layout: col-sidebar
title: Special Element Injection
author: 
contributors: 
permalink: /attacks/Special_Element_Injection
tags: attack, Special Element Injection
auto-migrated: 1

---

{% include writers.html %}

## Description

Special Element Injection is a type of injection attack that exploits a
weakness related to reserved words and special characters.

Every programming language and operating system has special characters
considered as reserved words for it. However, when an application
receives such data as user input, it is possible to observe unexpected
behavior in the application when parsing this information. This can lead
to information disclosure, access control and authorization bypass, code
injection, and many other variants.

According to the characters used, the Special Element Injection attack
can be performed using macro symbols, parameter delimiter and null
characters/null bytes, among others.

## Risk Factors

TBD

## Examples

### Example 1 - Macro symbol

The Special Element Injection attack based on macro symbols can be
performed by inserting macro symbols in input fields or user
configuration files. A known example of this attack can be represented
by vulnerability exploitation on Quake II server 3.20 and 3.21. This
vulnerability allows a remote user to access server console variables
(cvar), directory lists, and execute admin commands by a client on the
Quake II Server.

On this application, cvars are used by the client and server to store
configuration and status information. A cvar can be accessed by “$name”
syntax, where “name” is the name of the console variable to be expanded.

However, it is possible to modify the client console to send a malicious
command to the server, such as “say $rcon_password” to attempt to
discover the content server $rcon_password variables.

By discovering the password, it is possible to perform further actions
on the server, like discovering directory structures, command execution,
and visualization of file contents.

### Example 2 - Parameter delimiter

Parameter Delimiter is another variant of Special Element Injection. The
example below illustrates how this attack can be performed using a
vulnerability found on PHP posting system Poster version.two.

This application has a dangerous vulnerability that allows data
insertion into fields (username, password, email address and privileges)
of the “mem.php” file. This file is responsible for managing application
users.

An example of “mem.php” file is shown bellow, where user Jose has admin
privileges and Alice has just user access:

`<?`
`Jose|12345678|jose@attack.com|admin|`
`Alice|87654321|alice@attack.com|normal|`
`?>`

When a user wants to edit their profile, they must use "edit account" option
in the “index.php” page and enter their login information. However, using
“|” as a parameter delimiter on email field followed by “admin”
profile, the user could elevate their privileges to administrator.
Example:

`Username: Alice`
`Password: 87654321`
`Email: alice@attack.com |admin| `

This information will be recorded in “mem.php” file like this:

`Alice|87654321|alice@attack.com|admin|normal|`

The next time user Alice logs in, the application will acquire the
parameter “|admin|” as user profile, thus elevating Alice's privileges to
administrator profile.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category: Command
    Execution](:Category:_Command_Execution "wikilink")
  - [:Category: Authorization](:Category:_Authorization "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [:Category:Injection Attack](:Category:Injection_Attack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/75.html> - Special Element
    Injection (75)
  - <http://cwe.mitre.org/data/definitions/76.html> - Equivalent Special
    Element Injection (76)
  - <http://cwe.mitre.org/data/definitions/141.html> - Parameter
    Delimiter(141)
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=2002-0770> - Quake II
    Server Vulnerability
  - <http://www.kb.cert.org/vuls/id/970915> - Quake II Server performs
    console variable expansion on client-supplied input values
  - <http://archives.neohapsis.com/archives/bugtraq/2002-05/0118.html> -
    Quaker II Server problem
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2003-0307> -
    Attacker inserts field separator into input to specify admin
    privileges

\[\[Category:FIXME|link not working

  - <http://cve.mitre.org/docs/plover/SECTION.9.3.html> - PLOVER:
    SECTION.9.3. – Special Elements (Characters or Reserved Words)

\]\]

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[not threat agents](Category:FIXME "wikilink")
[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
[Category:Attack](Category:Attack "wikilink")