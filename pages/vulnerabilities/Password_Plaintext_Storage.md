---

layout: col-sidebar
title: Password Plaintext Storage
author:
contributors:
permalink: /vulnerabilities/Password_Plaintext_Storage
tags: vulnerability, Password Plaintext Storage

---

{% include writers.html %}

## NVD Categorization

> [CWE-256: Plaintext Storage of a Password](https://cwe.mitre.org/data/definitions/256.html): Storing a password in plaintext may result in a system compromise.

> [CWE-312: Cleartext Storage of Sensitive Information](https://cwe.mitre.org/data/definitions/312.html): The application stores sensitive information in cleartext within a resource that might be accessible to another control sphere.

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
