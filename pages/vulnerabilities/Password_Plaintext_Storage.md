---

layout: col-sidebar
title: Password Plaintext Storage
author: 
contributors: 
permalink: /vulnerabilities/Password_Plaintext_Storage
tag: vulnerability, Password Plaintext Storage
auto-migrated: 1

---

Last revision (mm/dd/yy): **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Storing a password in plaintext may result in a system compromise.

Password management issues occur when a password is stored in plaintext
in an application's properties or configuration file. A programmer can
attempt to remedy the password management problem by obscuring the
password with an encoding function, such as base 64 encoding, but this
effort does not adequately protect the password.

Storing a plaintext password in a configuration file allows anyone who
can read the file access to the password-protected resource. Developers
sometimes believe that they cannot defend the application from someone
who has access to the configuration, but this attitude makes an
attacker's job easier. Good password management guidelines require that
a password never be stored in plaintext.

## Risk Factors

TBD

## Examples

The following code reads a password from a properties file and uses the
password to connect to a database.

```
    ...
    Properties prop = new Properties();
    prop.load(new FileInputStream("config.properties"));
    String password = prop.getProperty("password");

    DriverManager.getConnection(url, usr, password);
    ...
```

## Related [Attacks](Attacks "wikilink")

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](Vulnerabilities "wikilink")

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](Controls "wikilink")

  - [Password Management
    Countermeasure](Password_Management_Countermeasure "wikilink")

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
[Category:Java](Category:Java "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink") [Category:Password Management
Vulnerability](Category:Password_Management_Vulnerability "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")