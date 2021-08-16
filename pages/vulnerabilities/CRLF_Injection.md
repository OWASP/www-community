---

layout: col-sidebar
title: CRLF Injection
author: 
contributors: 
permalink: /vulnerabilities/CRLF_Injection
tags: vulnerability, CRLF Injection

---

{% include writers.html %}

## Description

The term CRLF refers to **C**arriage **R**eturn (ASCII 13, `\r`) **L**ine **F**eed (ASCII 10, `\n`). They're used to note the termination of a line, however, dealt with differently in today’s popular Operating Systems. For example: in Windows both a CR and LF are required to note the end of a line, whereas in Linux/UNIX a LF is only required. In the HTTP protocol, the CR-LF sequence is always used to terminate a line.

A CRLF Injection attack occurs when a user manages to submit a CRLF into an application. This is most commonly done by modifying an HTTP parameter or URL.

## Examples

Depending on how the application is developed, this can be a minor problem or a fairly serious security flaw. Let's look at the latter because this is after all a security related post.

Let's assume a file is used at some point to read/write data to a log of some sort. If an attacker managed to place a CRLF, then can inject some sort of programmatic read method to the file. This could result in the contents being written to screen on the next attempt to use this file.

Another example is the "response splitting" attacks, where CRLFs are injected into an application and included in the response. The extra CRLFs are interpreted by proxies, caches, and maybe browsers as the end of a packet, causing mayhem.

## Related [Attacks](../attacks/)

- [HTTP Response Splitting](../attacks/HTTP_Response_Splitting)
- [Log Injection](../attacks/Log_Injection)
