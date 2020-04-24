---

layout: col-sidebar
title: Function Injection
author: 
contributors: 
permalink: /attacks/Function_Injection
tags: attack, Function Injection
auto-migrated: 1

---

{% include writers.html %}

## Overview

A [Function Injection](Function_Injection "wikilink") attack consists of
insertion or "injection" of a function name from client to the
application. A successful function injection exploit can execute any
built-in or user defined function. Function injection attacks are a type
of injection attack, in which arbitrary function names, in sometimes
with parameters are injected into the application and executed. If
parameters are passed to the injection function it leads to remote code
execution.

## Risk Factors

  - These types of vulnerabilities can range from very hard to find, to
    easy to find
  - If found, are usually moderately hard to exploit, depending on
    scenario.
  - If successfully exploited, impact could cover loss of
    confidentiality, loss of integrity, loss of availability, and/or
    loss of accountability

## Examples

**Example 1**

If an application passes a parameter sent via a GET request to PHP and
then the parameter is evaluated as a function by including () after the
variable name, the variable will be treated as a function and will be
executed.

The URL below passes a function name to the script.

<http://testsite.com/index.php?action=edit>

The index.php file contains the following code.

    <?php

    $action = $_GET['action'];

    $action();

    ?>

In this case the attacker can pass any function name to the script for
example phpinfo

<http://testsite.com/index.php?action=phpinfo>

**Example 2**

This example is an extended and more dangerous version of "Example 1",
in this case, the application not only allows the function name to be
provided but also the parameters to that function.

<http://testsite.com/index.php?action=edit&pageid=1>

The index.php contains the following code.

    <?php

    $action = $_GET['action'];
    $pageid = $_GET['pageid'];

    $action($pageid);

    ?>

In this case the attacker not only passing the function name but also
the parameter to that function which can lead to remote code execution
by passing the system function with arbitrary commands.

<http://testsite.com/index.php?action=system&pageid=ls>

This will execute the "ls" command on the system.

**Example 3**

This example shows another way of evaluating user functions by using
call_user_func instead of using brackets.

<http://testsite.com/index.php?action=edit>

The index.php contains the following code.

    <?php

    $action = $_GET['action'];

    call_user_func($action);
    ?>

Similar to "example 1" the attacker can pass any function name to the
script for example phpinfo

<http://testsite.com/index.php?action=phpinfo>

**Example 4**

This example is an extended and more dangerous version of "Example 3",
in this case, the application passes another parameter for
call_user_func which will be passed as a parameter to the function
provided in the first argument of call_user_func, multiple parameters
can passed to call_user_func in the form of an array.

<http://testsite.com/index.php?action=edit&pageid=1>

The index.php contains the following code.

    <?php

    $action = $_GET['action'];
    $pageid = $_GET['pageid'];

    call_user_func($action,$pageid);

    ?>

In this case the attacker not only passing the function name but also
the parameter to that function which can lead to remote code execution
by passing the system function with arbitrary commands.

<http://testsite.com/index.php?action=system&pageid=ls>

This will execute the "ls" command on the system.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:
    Internet_attacker](:Category:_Internet_attacker "wikilink")
  - [Internal_software_developer](Internal_software_developer "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Command Injection](Command_Injection "wikilink")
  - [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
  - [LDAP injection](LDAP_injection "wikilink")
  - [SSI injection](https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection)
  - [Cross-site Scripting
    (XSS)](Cross-site_Scripting_\(XSS\) "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Input Validation](Input_Validation "wikilink")
  - [Canonicalization](Canonicalization "wikilink")

## References

  - [call_user_func](http://php.net/manual/en/function.call-user-func.php)
    - PHP documentation for call_user_func.
  - [call_user_func_array](http://php.net/manual/en/function.call-user-func-array.php)
    - PHP documentation for call_user_func.

[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
[Category:Attack](Category:Attack "wikilink")