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

### Logger Not Declared Static Final

Loggers should be declared to be static and final.

It is good programming practice to share a single logger object between
all of the instances of a particular class and to use the same logger
for the duration of the program.

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

Using `System.out` or `System.err` rather than a dedicated logging facility
makes it difficult to monitor the behavior of the program. It can also
cause log messages to accidentally be returned to the end users, revealing
internal information to attackers.

The first Java program that a developer learns to write often looks like
this:

```java
    public class MyClass
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

## References

Note: A reference to related [CWE](http://cwe.mitre.org/) or
[CAPEC](http://capec.mitre.org/) article should be added when exists.
Eg:

  - [CWE 79](http://cwe.mitre.org/data/definitions/79.html).
  - <http://www.link1.com>
  - [Title for the link2](http://www.link2.com)
