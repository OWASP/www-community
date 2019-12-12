---

layout: col-sidebar
title: Insecure Third Party Domain Access
author: 
contributors: 
permalink: /vulnerabilities/Insecure_Third_Party_Domain_Access
tags: vulnerability, Insecure Third Party Domain Access
auto-migrated: 1

---

Last revision (mm/dd/yy): **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Occurs when an application contains content provided from a 3rd party
resource that is delivered without any type of content scrub.

**Environments Affected**

  - Web servers
  - Application servers
  - Client Machines

## Risk Factors

  - Allowing hosted content from an untrusted server into a trusted
    application: affecting the server, server environment, and client
    machine.
  - No confirmation of Third Party Controls.

## Examples

This following example is a common method to insert third party hosted
content into a trusted an application. If the hosting site is vulnerable
to attack, all content delivered to an application would be vulnerable
malicious changes.

    <iframe src="http://site.com/share/Action.swf" width="720" height="420"
    marginwidth="0" marginheight="0" scrolling="Auto" frameborder="0"></iframe>

## Related [Attacks](Attacks "wikilink")

[Cross-Site_Request_Forgery](Cross-Site_Request_Forgery "wikilink")

## Related [Vulnerabilities](Vulnerabilities "wikilink")

TBD

## Related [Controls](Controls "wikilink")

TBD

## References

[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")