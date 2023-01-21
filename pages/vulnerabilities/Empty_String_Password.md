---

layout: col-sidebar
title: Empty String Password
author:
contributors:
permalink: /vulnerabilities/Empty_String_Password
tags: vulnerability, Empty String Password

---

{% include writers.html %}

## NVD Categorization

> [CWE-20: Improper Input Validation](https://cwe.mitre.org/data/definitions/20.html): The product receives input or data, but it does not validate or incorrectly validates that the input has the properties that are required to process the data safely and correctly.

## Description

Using an empty string as a password is insecure. It is never appropriate to use an empty string as a password. It is too easy to guess. An empty string password makes the authentication as weak as the user names, which are normally public or guessable. This makes a brute-force attack against the login interface much easier.
