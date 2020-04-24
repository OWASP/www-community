---

layout: col-sidebar
title: Session Variable Overloading
author: 
contributors: 
permalink: /vulnerabilities/Session_Variable_Overloading
tags: vulnerability, Session Variable Overloading
auto-migrated: 1

---

{% include writers.html %}

## Description

Session Variable Overloading (also known as Session Puzzling) is an
application level vulnerability which can enable an attacker to perform
a variety of malicious actions not limited to:

  - Bypass efficient authentication enforcement mechanisms, and
    impersonate legitimate users.
  - Elevate the privileges of a malicious user account, in an
    environment that would otherwise be considered foolproof.
  - Skip over qualifying phases in multiphase processes, even if the
    process includes all the commonly recommended code level
    restrictions.
  - Manipulate server-side values in indirect methods that cannot be
    predicted or detected.
  - Execute traditional attacks in locations that were previously
    unreachable, or even considered secure.

This vulnerability occurs when an application uses the same session
variable for more than one purpose. An attacker can potentially access
pages in an order unanticipated by the developers so that the session
variable is set one one context and then used in another.

For example an attacker could use session variable overloading to bypass
authentication enforcement mechanisms of applications that enforce
authentication by validating the existence of session variables that
contain identity–related values, which are usually stored in the session
after a successful authentication process. The authentication bypass
attack vector could be executed by accessing a publicly accessible entry
point (e.g. a password recovery page) that populates the session with an
identical session variable, based on fixed values or on user originating
input.

### Environments Affected

All web servers, application servers, and web application environments
are susceptible to session variable overloading.

### How to Determine If You Are Vulnerable

The most effective way to detect these vulnerabilities is to enumerate
all of the session variables used and in which context they are valid.
In practice this can only be effectively done via a source code review.

## Prevention

Session variables should only be used for a single consistent purpose.

## Examples

## Related [Attacks](https://owasp.org/www-community/attacks/)

## References

  - Session Puzzles:
    <http://puzzlemall.googlecode.com/files/Session%20Puzzles%20-%20Indirect%20Application%20Attack%20Vectors%20-%20May%202011%20-%20Whitepaper.pdf>
  - Session Puzzling and Session Race Conditions:
    <http://sectooladdict.blogspot.com/2011/09/session-puzzling-and-session-race.html>

__NOTOC__

[Category:Session Management
Vulnerability](Category:Session_Management_Vulnerability "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Externally Linked
Page](Category:Externally_Linked_Page "wikilink")