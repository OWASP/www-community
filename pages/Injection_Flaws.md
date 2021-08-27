---

title: Injection Flaws
layout: col-sidebar
author:
contributors: Jeremy Ferragamo, Wichers, Eofedal, kingthorin
tags:
permalink: /Injection_Flaws

---

{% include writers.html %}

## Description

Attackers can relay malicious code through an application to another system
with injection flaws. These attacks include:

- Calls to the operating system through system calls.
- Use of external programs with shell commands.
- Calls to backend databases through SQL (such as for an SQL injection).

With these methods, an attacker can inject and execute scripts written in languages
such as Perl and Python into poorly designed applications. Whenever an application
uses an interpreter, there's a danger of introducing an injection vulnerability.

Many web applications depend on operating system features and external
programs, such as Sendmail. When a web application passes information
from an HTTP request as part of an external request, set up a way
to scrub the message. Otherwise an attacker can inject special (meta)
characters, malicious commands, or command modifiers into the message.
The web application blindly passes these on to the external system for
execution.

SQL injection is a particularly widespread and dangerous form of
injection. To exploit an SQL injection flaw, an attacker needs to find
a parameter that the web application passes through to a database. An
attacker can then embed malicious SQL commands into the content of the
parameter, to trick the web application to forward a malicious query to
the database.

While these attacks are not difficult to attempt, we have an increasing number of
tools that scan for these flaws. An attacker can use these techniques to obtain,
corrupt, or destroy the contents of your database.

Some attackers find it easy to discover and exploit injection vulnerabilities.
Such vulnerabilities may be extremely obscure for the rest of us. Successful
injection attacks may completely compromise or destroy a system. As many apps
use external calls, there's a high probability of an injection flaw.

## Environments Affected

Every web application environment allows the execution of external
commands such as system calls, shell commands, and SQL requests. The
susceptibility of an external call to command injection depends on how
the call is made and the specific component that is being called, but
almost all external calls can be attacked if the web application is not
properly coded.

## Examples

1. A malicious parameter could modify the actions taken by a system
call that normally retrieves the current user’s file to access
another user’s file (e.g., by including path traversal `../`
characters as part of a filename request). Additional commands could
be tacked on to the end of a parameter that is passed to a shell
script to execute an additional shell command (e.g., `; rm –r \*`)
along with the intended command.
2. SQL queries could be modified by adding additional ‘constraints’ to
a where clause (e.g., `OR 1=1`) to gain access to or modify
unauthorized data.

## How to Determine If You Are Vulnerable

The best way to determine if your applications are vulnerable to
injection attacks is to search the source code for all calls to external
resources (e.g., system, exec, fork, Runtime.exec, SQL queries, or
whatever the syntax is for making requests to interpreters in your
environment). Note that many languages have multiple ways to run
external commands. Developers should review their code and search for
all places where input from an HTTP request could possibly make its way
into any of these calls. You should carefully examine each of these
calls to be sure that the protection steps outlined below are followed.

## How to Protect Yourself

1. Avoid Accessing External Interpreters
   
   The simplest way to protect against injection is to avoid accessing
external interpreters wherever possible. For many shell commands and
some system calls, there are language specific libraries that perform
the same functions. Using such libraries does not involve the operating
system shell interpreter, and therefore avoids a large number of
problems with shell commands.

2. Validate Input
  
   For those calls that you must still employ, such as calls to backend
databases, you must carefully validate the data provided to ensure that
it does not contain any malicious content. You can also structure many
requests in a manner that ensures that all supplied parameters are
treated as data, rather than potentially executable content. The use of
stored procedures or prepared statements will provide significant
protection, ensuring that supplied input is treated as data. These
measures will reduce, but not completely eliminate the risk involved in
these external calls. You still must always validate such input to make
sure it meets the expectations of the application in question. For more
details on how to specifically defend against SQL Injection, please
refer to OWASP's [SQL Injection Prevention Cheat
Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html).

3. Apply Least Privilege
   
   Another strong protection against injection attacks is to ensure that
the web application runs with only the privileges it absolutely needs to
perform its function. So you should not run the webserver as root or
access a database as DBADMIN, otherwise an attacker can abuse these
administrative privileges granted to the web application. Some of the
J2EE environments allow the use of the Java sandbox, which can prevent
the execution of system commands.

4. Handle Exceptions and Returned Status Codes
   
   If an external command must be used, any user information that is being
inserted into the command should be rigorously checked. Mechanisms
should be put in place to handle any possible errors, timeouts, or
blockages during the call. All output, return codes and error codes from
the call should be checked to ensure that the expected processing
actually occurred. At a minimum, this will allow you to determine that
something has gone wrong. Otherwise, the attack may occur and never be
detected.

5. Leverage the OWASP's Filters Project
   
   The OWASP Filters project is producing reusable components in several
languages to help prevent many forms of injection.

## References

- OWASP [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- [NOSQL-injection](http://erlend.oftedal.no/blog/?blogid=110)
