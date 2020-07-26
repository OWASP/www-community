---

layout: col-sidebar
title: Out-of-band resource load (HTTP)
author: Rishu Ranjan
contributors: 
permalink: /attacks/Out-of-band_resource_load_(HTTP)
tags: attack, Out-of-band resource load (HTTP), OBRL

---

{% include writers.html %}

# Description

In out-of-band resource load, an application include the content from an arbitrary external location into the application's response. It's not always a vulnerability to load out of band resource and can be intented behavior of the application in some cases. However, in many cases, it can lead a vulnerability with serious consequences.

An attacker can use this vulnerability to attack public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself and can also use as a two-way attack proxy to request and retrieve web content from other systems. An attacker can cause the application server to attack, or retrieve content from, other systems that it can interact by submitting suitable payloads. This may include depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers.

Additionally, the application's processing of web content that is retrieved from arbitrary URLs exposes some important and non-conventional attack surface. An attacker can deploy a web server that returns malicious content, and then induce the application to retrieve and process that content. This processing might give rise to the types of input-based vulnerabilities that are normally found when unexpected input is submitted directly in requests to the application. The out-of-band attack surface that the application exposes should be thoroughly tested for these types of vulnerabilities.

> Attack Type: Server-Side

# Audit Guideline

1) Capture the base request of the vulnerable website with a personal proxy and leverage that request via the proxy's resend functionality.
2) Change the request path to any internal or external URL. For example change the request path to `https://www.attacker.com`.
3) The application will include the response of `https://www.attacker.com` in the response of vulnerable website.

# Remediation

Determine and review the purpose and use of the relevant application functionality to trigger arbitrary out-of-band resource load is intended behavior. If so,
- Take appropriate measures that might include blocking network access from the application server to other internal systems
- Hardening the application server itself to remove any services available on the local loopback adapter. 
- Ensure that content retrieved from other systems is processed in a safe manner, with the usual precautions that are applicable when processing input from direct incoming web requests.

If the ability to trigger arbitrary out-of-band resource load is not intended behavior,
- Implement a whitelist of permitted URLs, and block requests to URLs that do not appear on this whitelist.

# References
- [PortSwigger: Out-of-band resource load (HTTP)](https://portswigger.net/kb/issues/00100a00_out-of-band-resource-load-http)
- [Medium: Audit Guideline and example of Out-of-band resource load (HTTP)](https://medium.com/@rishuranjan6/web-application-security-assessment-using-burp-community-edition-part-1-audit-guidelines-51f05cf31fb0)
