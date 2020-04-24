---

layout: col-sidebar
title: Process Control
author: 
contributors: 
permalink: /vulnerabilities/Process_Control
tags: vulnerability, Process Control
auto-migrated: 1

---

{% include writers.html %}

## Description

Executing commands from an untrusted source or in an untrusted
environment can cause an application to execute malicious commands on
behalf of an attacker.

Process control vulnerabilities take two forms:

  - An attacker can change the command that the program executes: the
    attacker explicitly controls what the command is.
  - An attacker can change the environment in which the command
    executes: the attacker implicitly controls what the command means.

We will first consider the first scenario, the possibility that an
attacker may be able to control the command that is executed. Process
control vulnerabilities of this type occur when:

1.  Data enters the application from an untrusted source.
2.  The data is used as or as part of a string representing a command
    that is executed by the application.
3.  By executing the command, the application gives an attacker a
    privilege or capability that the attacker would not otherwise have.

## Risk Factors

TBD

## Examples

### Example 1

The following Java code from a system utility uses the system property
APPHOME to determine the directory in which it is installed and then
executes an initialization script based on a relative path from the
specified directory.

```
    ...
    String home = System.getProperty("APPHOME");
    String cmd = home + INITCMD;
    java.lang.Runtime.getRuntime().exec(cmd);
    ...
```

The code in Example 1 allows an attacker to execute arbitrary commands
with the elevated privilege of the application by modifying the system
property APPHOME to point to a different path containing a malicious
version of INITCMD. Because the program does not validate the value read
from the environment, if an attacker can control the value of the system
property APPHOME, then they can fool the application into running
malicious code and take control of the system.

### Example 2

The following code is from an administrative web application designed to
allow users to kick off a backup of an Oracle database using a
batch-file wrapper around the rman utility and then run a cleanup.bat
script to delete some temporary files. The script rmanDB.bat accepts a
single command line parameter, which specifies what type of backup to
perform. Because access to the database is restricted, the application
runs the backup as a privileged user.

```
    ...
    String btype = request.getParameter("backuptype");
    String cmd = new String("cmd.exe /K
    \"c:\\util\\rmanDB.bat "+btype+"&&c:\\utl\\cleanup.bat\"")
    System.Runtime.getRuntime().exec(cmd);
    ...
```

The problem here is that the program does not do any validation on the
backuptype parameter read from the user. Typically the Runtime.exec()
function will not execute multiple commands, but in this case the
program first runs the cmd.exe shell first in order to run multiple
commands with a single call to Runtime.exec(). Once the shell is
invoked, it will happily execute multiple commands separated by two
ampersands. If an attacker passes a string of the form "&& del
c:\\\\dbms\\\\\*.\*", then the application will execute this command
along with the others specified by the program. Because of the nature of
the application, it runs with the privileges necessary to interact with
the database, which means whatever command the attacker injects will run
with those privileges as well.

### Example 3

The C code below is from a web-based CGI utility that allows users to
change their passwords. The password update process under NIS includes
running make in the /var/yp directory. Note that since the program
updates password records, it has been installed setuid root.

The program invokes make as follows:

```
    system("cd /var/yp && make &> /dev/null");
```

Unlike the previous examples, the command in this example is hardcoded,
so an attacker cannot control the argument passed to system(). However,
since the program does not specify an absolute path for make and does
not scrub any environment variables prior to invoking the command, the
attacker can modify their $PATH variable to point to a malicious binary
named make and execute the CGI script from a shell prompt. And since the
program has been installed setuid root, the attacker's version of make
now runs with root privileges.

The environment plays a powerful role in the execution of system
commands within programs. Functions like system() and exec() use the
environment of the program that calls them, and therefore attackers have
a potential opportunity to influence the behavior of these calls.

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Command Injection](Command_Injection "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

Note: A reference to related [CWE](http://cwe.mitre.org/) or
[CAPEC](http://capec.mitre.org/) article should be added when exists.
Eg:

  - [CWE 79](http://cwe.mitre.org/data/definitions/79.html).
  - <http://www.link1.com>
  - [Title for the link2](http://www.link2.com)

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")