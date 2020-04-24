---

layout: col-sidebar
title: Log Injection
author: 
contributors: 
permalink: /attacks/Log_Injection
tags: attack, Log Injection
auto-migrated: 1

---

{% include writers.html %}

## Description

Applications typically use log files to store a history of events or
transactions for later review, statistics gathering, or debugging.
Depending on the nature of the application, the task of reviewing log
files may be performed manually on an as-needed basis or automated with
a tool that automatically culls logs for important events or trending
information.

Writing invalidated user input to log files can allow an attacker to
forge log entries or inject malicious content into the logs. This is
called log injection.

Log injection vulnerabilities occur when:

1.  Data enters an application from an untrusted source.
2.  The data is written to an application or system log file.

Successful log injection attacks can cause:

1.  Injection of new/bogus log events (log forging via log injection)
2.  Injection of XSS attacks, hoping that the malicious log event isviewed in a vulnerable web application
3.  Injection of commands that parsers (like PHP parsers) could execute

## Log Forging

In the most benign case, an attacker may be able to insert false entries
into the log file by providing the application with input that includes
appropriate characters. If the log file is processed automatically, the
attacker can render the file unusable by corrupting the format of the
file or injecting unexpected characters. A more subtle attack might
involve skewing the log file statistics. Forged or otherwise, corrupted
log files can be used to cover an attacker's tracks or even to implicate
another party in the commission of a [malicious act](http://doc.novsu.ac.ru/oreilly/tcpip/puis/ch10_05.htm).

### Log Forging Example

The following web application code attempts to read an integer value
from a request object. If the value fails to parse as an integer, then
the input is logged with an error message indicating what happened.

```
    ...
    String val = request.getParameter("val");
    try {
        int value = Integer.parseInt(val);
    }
    catch (NumberFormatException) {
        log.info("Failed to parse val = " + val);
    }
    ...
```

If a user submits the string "twenty-one" for val, the following entry
is logged:

```
    INFO: Failed to parse val=twenty-one
```

However, if an attacker submits the string
"twenty-one%0a%0aINFO:+User+logged+out%3dbadguy", the following entry is
logged:

```
    INFO: Failed to parse val=twenty-one

    INFO: User logged out=badguy
```

Clearly, attackers can use this same mechanism to insert arbitrary log
entries.

## Code Execution via Log Injection

PHP code can easily be added to a log file, for example:

```
    https://www.somedomain.tld/index.php?file=`
    <?php echo phpinfo(); ?>`
```

This stage it is called **log file poisoning**. If the log file is
staged on a public directory and can be accessed via a HTTP GET request,
the embedded PHP command may execute in certain circumstances. This is a
form of [Command Injection](Command_Injection) via Log
Injection.

## References

- G. Hoglund and G. McGraw. Exploiting Software: How to BreakCode. Addison-Wesley, February 2004.
- [https://medium.com/@shatabda/security-log-injection-what-how-a510cfc0f73b](https://medium.com/@shatabda/security-log-injection-what-how-a510cfc0f73b)
- [https://www.geeksforgeeks.org/log-injection/](https://www.geeksforgeeks.org/log-injection/)
- [https://affinity-it-security.com/what-is-log-injection/](https://affinity-it-security.com/what-is-log-injection/)