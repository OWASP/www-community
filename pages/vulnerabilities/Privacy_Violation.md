---

layout: col-sidebar
title: Privacy Violation
author: 
contributors: 
permalink: /vulnerabilities/Privacy_Violation
tags: vulnerability, Privacy Violation
auto-migrated: 1

---

{% include writers.html %}

## Description

Mishandling private information, such as customer passwords or social
security numbers, can compromise user privacy, and is often illegal.

Privacy violations occur when:

1.  Private user information enters the program.
2.  The data is written to an external location, such as the console,
    file system, or network.

Private data can enter a program in a variety of ways:

  - Directly from the user in the form of a password or personal
    information
  - Accessed from a database or other data store by the application
  - Indirectly from a partner or other third party

Sometimes data that is not labeled as private can have a privacy
implication in a different context. For example, student identification
numbers are usually not considered private because there is no explicit
and publicly-available mapping to an individual student's personal
information. However, if a school generates identification numbers based
on student social security numbers, then the identification numbers
should be considered private.

Security and privacy concerns often seem to compete with each other.
From a security perspective, you should record all important operations
so that any anomalous activity can later be identified. However, when
private data is involved, this practice can in fact create risk.

Although there are many ways in which private data can be handled
unsafely, a common risk stems from misplaced trust. Programmers often
trust the operating environment in which a program runs, and therefore
believe that it is acceptable to store private information on the file
system, in the registry, or in other locally-controlled resources.
However, even if access to certain resources is restricted, this does
not guarantee that the individuals who do have access can be trusted.
For example, in 2004, an unscrupulous employee at AOL sold approximately
92 million private customer e-mail addresses to a spammer marketing an
offshore gambling web site \[1\].

In response to such high-profile exploits, the collection and management
of private data is becoming increasingly regulated. Depending on its
location, the type of business it conducts, and the nature of any
private data it handles, an organization may be required to comply with
one or more of the following federal and state regulations:

  - Safe Harbor Privacy Framework \[2\]
  - Gramm-Leach Bliley Act (GLBA) \[3\]
  - Health Insurance Portability and Accountability Act (HIPAA) \[4\]
  - California SB-1386 \[5\]

Despite these regulations, privacy violations continue to occur with
alarming frequency.

## Examples

The following code contains a logging statement that tracks the contents
of records added to a database by storing them in a log file. Among
other values that are stored, the getPassword() function returns the
user-supplied plaintext password associated with the account.

```
    pass = getPassword();
    ...
    dbmsLog.println(id+":"+pass+":"+type+":"+tstamp);
```

The code in the example above logs a plaintext password to the
filesystem. Although many developers trust the filesystem as a safe
storage location for data, it should not be trusted implicitly,
particularly when privacy is a concern.

## References

  - \[1\] J. Oates. AOL man pleads guilty to selling 92m email
    addresses. The Register, 2005.
    <http://www.theregister.co.uk/2005/02/07/aol_email_theft/>
  - \[2\] Safe Harbor Privacy Framework. U.S. Department of Commerce.
    <http://www.export.gov/safeharbor/>.
  - \[3\] Financial Privacy: The Gramm-Leach Bliley Act (GLBA). Federal
    Trade Commission.
    <http://www.ftc.gov/privacy/privacyinitiatives/glbact.html>.
  - \[4\] Health Insurance Portability and Accountability Act (HIPAA).
    U.S. Department of Human Services. <http://www.hhs.gov/ocr/hipaa/>.
  - \[5\] California SB-1386. Government of the State of California,
    2002.
    <http://info.sen.ca.gov/pub/01-02/bill/sen/sb_1351-1400/sb_1386_bill_20020926_chaptered.html>.

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
[Category:Code Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")