---

layout: col-sidebar
title: Forced browsing
author: 
contributors: 
permalink: /attacks/Forced_browsing
tags: attack, Forced browsing
auto-migrated: 1

---

{% include writers.html %}

## Description

Forced browsing is an attack where the aim is to enumerate and access
resources that are not referenced by the application, but are still
accessible.

An attacker can use [Brute Force](Brute_force_attack "wikilink")
techniques to search for unlinked contents in the domain directory, such
as temporary directories and files, and old backup and configuration
files. These resources may store sensitive information about web
applications and operational systems, such as source code, credentials,
internal network addressing, and so on, thus being considered a valuable
resource for intruders.

This attack is performed manually when the application index directories
and pages are based on number generation or predictable values, or using
automated tools for common files and directory names.

This attack is also known as Predictable Resource Location, File
Enumeration, Directory Enumeration, and Resource Enumeration.

## Examples

### Example 1

This example presents a technique of Predictable Resource Location
attack, which is based on a manual and oriented identification of
resources by modifying URL parameters. The user1 wants to check their
on-line agenda through the following URL:

` www.site-example.com/users/calendar.php/user1/20070715 `

In the URL, it is possible to identify the username (âuser1â) and
the date (mm/dd/yyyy). If the user attempts to make a forced browsing
attack, they could guess another user's agenda by predicting user
identification and date, as follow:

` www.site-example.com/users/calendar.php/user6/20070716 `

The attack can be considered successful upon accessing other user's
agenda. A bad implementation of the authorization mechanism contributed
to this attack's success.

### Example 2

This example presents an attack of static directory and file enumeration
using an automated tool.

A scanning tool, like [Nikto](http://www.cirt.net/code/nikto.shtml), has
the ability to search for existing files and directories based on a
database of well-know resources, such as:

`/system/`
`/password/`
`/logs/`
`/admin/`
`/test/`

When the tool receives an âHTTP 200â message it means that such
resource was found and should be manually inspected for valuable
information.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [Internal software
    developer](Internal_software_developer "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Path Traversal (Path Manipulation)](Path_Traversal "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:Access Control
    Vulnerability](:Category:Access_Control_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Access Control](:Category:_Access_Control "wikilink")

## References

  - Forceful Browsing â Imperva Application Data Security and
    Compliance
    <http://www.imperva.com/application_defense_center/glossary/forceful_browsing.html>
  - Parameter fuzzing and forced browsing â WebAppSec -
    <http://seclists.org/webappsec/2006/q3/0182.html>
  - <http://www.webappsec.org/projects/threat/classes/predictable_resource_location.shtml>
  - <http://cwe.mitre.org/data/definitions/425.html>

[category:Resource
Manipulation](category:Resource_Manipulation "wikilink") __NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[need content](Category:FIXME "wikilink")
[Category:Attack](Category:Attack "wikilink")
