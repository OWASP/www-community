---

layout: col-sidebar
title: Poor Logging Practice
author: Weilin Zhong 
contributors: Imifos, KirstenS, kingthorin
permalink: /vulnerabilities/Poor_Logging_Practice
tags: vulnerability, Poor Logging Practice

---

{% include writers.html %}

## Description

Poor logging practices can introduce security risks beyond code quality concerns. 
Improperly implemented logging may lead to information disclosure, log injection or 
forging, insufficient security monitoring, and weakened incident response. 
Because logs are often used for detection, auditing, and forensic analysis, poor 
logging practices can directly impact an organization’s ability to detect and 
respond to attacks.

### Logger Not Declared Static Final

Loggers should be declared to be static and final.

It is good programming practice to share a single logger object between
all of the instances of a particular class and to use the same logger
for the duration of the program.

From a security perspective, inconsistent logger instantiation can result in 
unpredictable logging behavior and missing security-relevant events. This can 
complicate centralized logging, monitoring, and correlation of events during 
incident detection and forensic analysis.

The following statement errantly declares a non-static logger.

```java
    private final Logger logger =
                Logger.getLogger(MyClass.class);
```

### Multiple Loggers

It is a poor logging practice to use multiple loggers rather than
logging levels in a single class.

Good logging practice dictates the use of a single logger that supports
different logging levels for each class.

Using multiple loggers within the same class can fragment log output and make it 
harder to correlate events across components. This may reduce visibility into 
security incidents and weaken audit trails required for monitoring and 
post-incident investigations.

The following code errantly declares multiple loggers.

```java
    public class MyClass {
      private final static Logger GOOD =
                Logger.getLogger(MyClass.class);
      private final static Logger BAD =
                Logger.getLogger(MyClass.class);
      private final static Logger UGLY =
                Logger.getLogger(MyClass.class);
      ...
    }
```

### Use of a System Output Stream

In security-sensitive environments, system output streams may be directly exposed
to users, container logs, or shared infrastructure, increasing the risk of
unintentional data leakage.

Using `System.out` or `System.err` rather than a dedicated logging facility
makes it difficult to monitor the behavior of the program. It can also
cause log messages to accidentally be returned to the end users, revealing
internal information to attackers.

The first Java program that a developer learns to write often looks like
this:

```java
    public class MyClass {
      public static void main(String[] args) {
        System.out.println("hello world");
      }
    }
```

While most programmers go on to learn many nuances and subtleties about
Java, a surprising number hang on to this first lesson and never give up
on writing messages to standard output using `System.out.println()`.

The problem is that writing directly to standard output or standard
error is often used as an unstructured form of logging. Structured
logging facilities provide features like: Logging levels, uniform
formatting, a logger identifier, timestamps, and perhaps most
critically; the ability to direct the log messages to the right place.
When the use of system output streams is jumbled together with code
that uses loggers properly, the result is often a well-kept log that is
missing critical information. In addition, using system output streams
and can also cause log messages to accidentally be returned to end users,
revealing an application's internal information to attackers.

Developers widely accept the need for structured logging, but many
continue to use system output streams in their "pre-production"
development. If the code you are reviewing is past the initial phases of
development, use of `System.out` or `System.err` may indicate an oversight
in the move to a structured logging system.

### Security Example

```java
// BAD: User-controlled input written directly to logs
logger.error("Login failed for user: " + username);
```
## Risk Factors

- **Information Disclosure**  
  Log messages written to standard output or improperly managed logging systems 
  may expose internal application details such as stack traces, configuration 
  values, file paths, or user data.

- **Log Injection / Log Forging**
  When untrusted user input is written to logs without neutralization, attackers 
  may inject forged log entries, manipulate log files, or obscure malicious 
  activity.

- **Insufficient Logging and Monitoring**  
  Inconsistent or fragmented logging practices can prevent effective monitoring, 
  alerting, and detection of security incidents.

- **Impaired Incident Response and Forensics**  
  Poorly structured or incomplete logs reduce the ability to investigate security 
  incidents, perform audits, or meet compliance requirements.

## References

Note: A reference to related [CWE](http://cwe.mitre.org/) or
[CAPEC](http://capec.mitre.org/) article should be added when exists.
Eg:

- [CWE-532: Information Exposure Through Log Files](https://cwe.mitre.org/data/definitions/532.html)
- [CWE-117: Improper Output Neutralization for Logs](https://cwe.mitre.org/data/definitions/117.html)
- [OWASP Logging Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html)
- [OWASP Top 10 – Security Logging and Monitoring Failures](https://owasp.org/Top10/A09_2021-Security_Logging_and_Monitoring_Failures/)
