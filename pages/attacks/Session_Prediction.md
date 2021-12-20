---

layout: col-sidebar
title: Session Prediction
author: 
contributors: 
permalink: /attacks/Session_Prediction
tags: attack, Session Prediction
auto-migrated: 1

---

{% include writers.html %}

## Description

The session prediction attack focuses on predicting session ID values
that permit an attacker to bypass the authentication schema of an
application. By analyzing and understanding the session ID generation
process, an attacker can predict a valid session ID value and get access
to the application.

In the first step, the attacker needs to collect some valid session ID
values that are used to identify authenticated users. Then, they must
understand the structure of session ID, the information that is used to
create it, and the encryption or hash algorithm used by application to
protect it. Some bad implementations use sessions IDs composed by
username or other predictable information, like timestamp or client IP
address. In the worst case, this information is used in clear text or
coded using some weak algorithm like base64 encoding.

In addition, the attacker can implement a brute force technique to
generate and test different values of session ID until they successfully
get access to the application.

## Examples

The session ID information for a certain application is normally
composed by a string of fixed width. Randomness is very important to
avoid its prediction. Looking at the example in Figure 1, the session ID
variable is represented by JSESSIONID and its value is “user01”, which
corresponds to the username. By trying new values for it, like “user02”,
it could be possible to get inside the application without prior
authentication.

![Predictable cookie](../assets/images/attacks/predictable-cookie.jpg)

*Figure 1. Predictable cookie*

## External References

<http://www.iss.net/security_center/advice/Exploits/TCP/session_hijacking/default.htm>

<http://en.wikipedia.org/wiki/HTTP_cookie>

## Related Threats

[:Category: Authorization](:Category:_Authorization "wikilink")

## Related Attacks

  - [Man-in-the-middle attack](Man-in-the-middle_attack "wikilink")
  - [Session hijacking attack](Session_hijacking_attack "wikilink")
  - [Manipulating User Permission
    Identifier](Manipulating_User_Permission_Identifier "wikilink")

## Related Vulnerabilities

[:Category:Input Validation
Vulnerability](:Category:Input_Validation_Vulnerability "wikilink")

## Related Countermeasures

[:Category:Session Management
Control](:Category:Session_Management_Control "wikilink")

## Categories

[Category:Exploitation of
Authentication](Category:Exploitation_of_Authentication "wikilink")
[Category:Attack](Category:Attack "wikilink")
