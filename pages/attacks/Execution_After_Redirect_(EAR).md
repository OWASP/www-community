---

layout: col-sidebar
title: Execution After Redirect (EAR)
author: Robert Gilbert (amroot)
contributors: 
permalink: /attacks/Execution_After_Redirect_(EAR)
tags: attack, Execution After Redirect (EAR)
auto-migrated: 1

---

## Overview

Execution After Redirect (EAR) is an attack where an attacker ignores
redirects and retrieves sensitive content intended for authenticated
users. A successful EAR exploit can lead to complete compromise of the
application.

## How to Test for EAR Vulnerabilities

Using most proxies it is possible to ignore redirects and display what
is returned. In this test we use Burp Proxy.
Intercept request `https://vulnerablehost.com/managment_console`

1.  Send to repeater.
2.  View response.

## How to Prevent EAR Vulnerabilities

Proper termination should be performed after redirects. In a function a
return should be performed. In other instances functions such as die()
should be performed. This will tell the application to terminate
regardless of if the page is redirected or not.

## Examples

The following code will check to see if the parameter "loggedin" is
true. If it is not true, it uses JavaScript to redirect the user to the
login page. Using the "How to Test for EAR Vulnerabilities" section or
by disabling JavaScript in the browser, the same request is repeated
without following the JavaScript redirect and the "Admin" section is
accessible without authentication.

```php
<?php if (!$loggedin) {
     print "<script>window.location = '/login';</script>\n\n"; 
} ?>
<h1>Admin</h1>
<a href=/mu>Manage Users</a><br />
<a href=/ud>Update Database Settings</a>
```

## References

- [CWE-698: Execution After Redirect (EAR)](https://cwe.mitre.org/data/definitions/698.html)
- [Fear the EAR: Discovering and Mitigating Execution After Redirect Vulnerabilities](http://cs.ucsb.edu/~bboe/public/pubs/fear-the-ear-ccs2011.pdf)
- [CVE-2013-1402: DigiLIBE Management Console | Execution After Redirect (EAR) Vulnerability](https://nvd.nist.gov/vuln/detail/CVE-2013-1402)
