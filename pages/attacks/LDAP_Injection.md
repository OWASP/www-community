---

layout: col-sidebar
title: LDAP Injection
author: 
contributors: 
permalink: /attacks/LDAP_Injection
tags: attack, LDAP Injection

---

{% include writers.html %}

## Description

LDAP Injection is an attack used to exploit web based applications that construct LDAP statements based on user input. When an application fails to properly sanitize user input, it’s possible to modify LDAP statements using a local proxy. This could result in the execution of arbitrary commands such as granting permissions to unauthorized queries, and content modification inside the LDAP tree. The same advanced exploitation techniques available in [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection) can be similarly applied in LDAP Injection. 


## References

- [https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html](https://cheatsheetseries.owasp.org/cheatsheets/LDAP_Injection_Prevention_Cheat_Sheet.html)