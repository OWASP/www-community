---

layout: col-sidebar
title: Unicode Encoding
author: 
contributors: 
permalink: /attacks/Unicode_Encoding
tags: attack, Unicode Encoding
auto-migrated: 1

---

{% include writers.html %}

## Description

The attack aims to explore flaws in the decoding mechanism implemented
on applications when decoding Unicode data format. An attacker can use
this technique to encode certain characters in the URL to bypass
application filters, thus accessing restricted resources on the Web
server or to force browsing to protected pages.

## Examples

Consider a web application which has restricted directories or files
(e.g. a file containing application usernames: appusers.txt). An
attacker can encode the character sequence “../” ([Path
Traversal](Path_Traversal "wikilink") Attack) using Unicode format and
attempt to access the protected resource, as follows:

Original Path Traversal attack URL (without Unicode Encoding):

`http://vulneapplication/../../appusers.txt`

Path Traversal attack URL with Unicode Encoding:

`http://vulneapplication/%C0AE%C0AE%C0AF%C0AE%C0AE%C0AFappusers.txt`

The Unicode encoding for the URL above will produce the same result as
the first URL (Path Traversal Attack). However, if the application has
an input security filter mechanism, it could refuse any request
containing “../” sequence, thus blocking the attack. However, if this
mechanism doesn’t consider character encoding, the attacker can bypass
and access protected resource.

Other consequences of this type of attack are privilege escalation,
arbitrary code execution, data modification, and denial of service.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Command
    Execution](:Category:Command_Execution "wikilink")
  - [:Category:Information
    Disclosure](:Category:Information_Disclosure "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Path Traversal](Path_Traversal "wikilink")
  - [Embedding Null Code](Embedding_Null_Code "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:Input Validation
    Vulnerability](:Category:Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## References

  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2000-0884> -
    CVE-2000-0884
  - <http://capec.mitre.org/data/definitions/71.html> - Using Unicode
    Encoding to Bypass Validation Logic
  - <http://www.microsoft.com/technet/security/bulletin/MS00-078.mspx> -
    Patch Available for 'Web Server Folder Traversal' Vulnerability
  - <http://www.kb.cert.org/vuls/id/739224> - HTTP content scanning
    systems full-width/half-width Unicode encoding bypass
  - <http://www.cgisecurity.com/lib/URLEmbeddedAttacks.html> - URL
    encoded attacks, by Gunter Ollmann

\[\[Category:FIXME|link not working

  - <http://scissec.scis.ecu.edu.au/conferences2007/documents/cheong_kai_wai_1.pdf>
    - Penetration testing of cross site scripting and SQL injection on
    web application by Cheong Kai Wee

\]\]

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[these links don't exist](Category:FIXME "wikilink") [Category:Resource
Manipulation](Category:Resource_Manipulation "wikilink")
[Category:Attack](Category:Attack "wikilink")