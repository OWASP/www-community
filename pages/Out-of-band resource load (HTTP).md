---

layout: col-sidebar
title: Out-of-band resource load (HTTP)
author: Rishu Ranjan
contributors: 
permalink: /Out-of-band resource load (HTTP)
tags: attack, Out-of-band resource load (HTTP), OBRL

---


# Description

Out-of-band resource load arises when it is possible to induce an application to fetch content from an arbitrary external location, and incorporate that content into the application's own response(s). The ability to trigger arbitrary out-of-band resource load does not constitute a vulnerability in its own right, and in some cases might even be the intended behavior of the application. However, in many cases, it can indicate a vulnerability with serious consequences.

The ability to request and retrieve web content from other systems can allow the application server to be used as a two-way attack proxy. By submitting suitable payloads, an attacker can cause the application server to attack, or retrieve content from, other systems that it can interact with. This may include public third-party systems, internal systems within the same organization, or services available on the local loopback adapter of the application server itself. Depending on the network architecture, this may expose highly vulnerable internal services that are not otherwise accessible to external attackers.

Additionally, the application's processing of web content that is retrieved from arbitrary URLs exposes some important and non-conventional attack surface. An attacker can deploy a web server that returns malicious content, and then induce the application to retrieve and process that content. This processing might give rise to the types of input-based vulnerabilities that are normally found when unexpected input is submitted directly in requests to the application. The out-of-band attack surface that the application exposes should be thoroughly tested for these types of vulnerabilities.

> Attack Type: Server-Side

# Audit Guideline

1) Capture the base request of the vulnerable website in the burp community and send the request to the repeater.
2) Change the request path to any internal or external URL. For eg. change the request path to https://www.attacker.com.
3) The application will include the response of https://www.attacker.com with the response headers of vulnerable website.


# Remediation

You should review the purpose and intended use of the relevant application functionality, and determine whether the ability to trigger arbitrary out-of-band resource load is intended behavior. If so, you should be aware of the types of attacks that can be performed via this behavior and take appropriate measures. These measures might include blocking network access from the application server to other internal systems, and hardening the application server itself to remove any services available on the local loopback adapter. You should also ensure that content retrieved from other systems is processed in a safe manner, with the usual precautions that are applicable when processing input from direct incoming web requests.

If the ability to trigger arbitrary out-of-band resource load is not intended behavior, then you should implement a whitelist of permitted URLs, and block requests to URLs that do not appear on this whitelist.

# References
- [PortSwigger: Out-of-band resource load (HTTP)](https://portswigger.net/kb/issues/00100a00_out-of-band-resource-load-http)
- [Medium: Audit Guideline and example of Out-of-band resource load (HTTP)](https://medium.com/@rishuranjan6/web-application-security-assessment-using-burp-community-edition-part-1-audit-guidelines-51f05cf31fb0)
