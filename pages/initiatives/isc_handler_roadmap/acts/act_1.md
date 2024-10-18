---

layout: col-sidebar
title: "Act I - Observing Behind the Curtain"
author: "Raphael Moreira"
contributors: 
permalink: /initiatives/isc_handler_roadmap/acts
tags: ["cybersecurity", "protocol", "http", "network", "response header", "xss", "csrf", "clickjacking", hsts", "csp", "ssl"]

---

{% include writers.html %}

🇺🇸 | [🇧🇷](act_1.pt-BR.md)

# Act I - Observing Behind the Curtain
Whenever a website is accessed, a series of processes occurs behind the scenes through the [🔍HTTP protocol](https://en.wikipedia.org/wiki/HTTP). 
This dynamic is easily visible through your browser's developer tools. It is possible to monitor all traffic related to a 
specific site, including features such as [🔍Status Code](https://www.rfc-editor.org/rfc/rfc9110.html#name-status-codes) 
and [🔍many others](https://developer.chrome.com/docs/devtools/network).

Each entry in the request list represents a unique interaction, and a website can have dozens of them for content formation. 
Among the various pieces of information provided, we will highlight one of the [🔍HTTP Headers](https://developer.mozilla.org/en-US/docs/Glossary/HTTP_header) 
that says a lot about your server: the **Response Header**.

>**Disclaimer:** OWASP does not endorse any vendor or tool by mentioning it. If it is cited, it is because we believe it 
> is available for free use in open-source projects. Feel free to use the tool that best suits your needs.

## Response Header
It refers to a set of information exchanged between the client and the server. Although it is customizable, there is a 
[🔍well-defined standard](https://developer.mozilla.org/en-US/docs/Glossary/Response_header) regarding its structure, content, 
and usage. Due to this flexibility, it is commonly manipulated by attackers, so it is important for developers to be cautious 
and not blindly trust this content.

To observe them, we will use the browser's [🔍DevTools](https://developer.chrome.com/docs/devtools) from [Brave](https://brave.com/download/). 
With the browser open, activate the [🔍Network](https://developer.chrome.com/docs/devtools/network) tab and keep it open 
while visiting a site, such as https://owasp.org/. By [inspecting one of the items](https://developer.chrome.com/docs/devtools/network#details) 
that appear in the request list, you'll have access to the **Headers** tab, where you'll find the **Response Headers** section.

The information contained there will vary depending on the configuration of the server, application, or service accessed. 
There is no correct list of what should exist or its composition, as it generally depends on each site's needs. However, 
we know what definitely <u>should not exist</u> when we talk about cybersecurity.

In its list of best practices, [OWASP](https://owasp.org/) gathers a series of recommendations, such as [🔍suggested secure content](https://owasp.org/www-project-secure-headers/index.html) 
and [🔍what to avoid](https://owasp.org/www-project-secure-headers/index.html#prevent-information-disclosure-via-http-headers) 
in the **Response Headers**.

## Verifying if it was effective
There are online tools that help you identify and check not only the **Response Headers**, but also other significant data:

- [Security Header](https://securityheaders.com/?q=https%3A%2F%2Fowasp.org%2F&followRedirects=on): In addition to a score, 
the site gives you a brief description and the importance of each header.
- [Protocol Guard](https://protocolguard.com/scan/owasp.org): Besides guidance on each header, it also mentions some issues 
related to [🔍SSL/TLS Ciphers](https://www.ssl.com/article/what-is-ssl-tls-an-in-depth-guide/).

Among the **Response Headers**, two stand out: [🔍HTTP Strict Transport Security (HSTS)](https://www.ssl.com/article/what-is-http-strict-transport-security-hsts/) 
and [🔍Content Security Policies (CSP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CSP).

While HSTS aims to protect sites from protocol downgrade attacks and cookie hijacking by enforcing interaction only via 
secure HTTPS, CSP seeks to do the same with the static content your server provides (e.g., JavaScript), mitigating cross-site attacks. 
Both headers share a common trait: they must be implemented gradually and carefully, monitoring the final behavior, as this 
depends heavily on how the application and/or site was designed.

To support this analysis, here are some useful tools:

- [CSP Policy Evaluator](https://csper.io/evaluator): Based on a URL, this tool highlights the issues and provides details 
on how to properly resolve them.
- [Google CSP Evaluator](https://csp-evaluator.withgoogle.com/): From a URL or a set of CSP policies, this tool offers 
guidance on each rule.
- [Qualys SSLLabs](https://www.ssllabs.com/ssltest/analyze.html?d=owasp.org): Deeply analyzes SSL configurations, detailing 
certificates and keys, as well as the existence of the HSTS header.
- [HSTS Preload](https://hstspreload.org/): Evaluates whether your HSTS policies are eligible for the preload attribute, 
a feature that, while not part of the original specification, provides security value by ensuring your application is included 
in centralized lists like the [🔍Chromium list](https://www.chromium.org/hsts/) or the [🔍Firefox list](https://searchfox.org/comm-central/source/mozilla/security/manager/ssl/nsSTSPreloadList.inc).

## Why is this important?
Correctly configuring the **Response Headers** is crucial for several reasons:

- **Security:** Improper configuration can expose sensitive information about the server or application, making it easier 
for attacks like information disclosure or injection attacks.
- **Privacy:** Some response headers may contain personal user information, such as cookies or authentication tokens. Configuring 
them correctly helps protect user privacy and prevents data leaks.
- **Attack prevention:** Well-configured headers can help prevent attacks like 🔍[🔍Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/),
[🔍 Cross-Site Request Forgery (CSRF)](https://owasp.org/www-community/attacks/csrf), and [🔍Clickjacking](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html), 
by providing appropriate security policies.
- **Performance improvement:** Some response headers can influence browser caching, improving site performance by reducing 
the number of requests made to the server.
- **Compatibility:** Configuring the response headers ensures compatibility with different browsers and devices, providing 
a consistent user experience.

## Summary
Paying attention to **Response Headers** is a good starting point for ensuring the protection of your application or website. 
Although these are simple configurations – _and in some cases, trivial) – they are crucial for adding an extra layer of security 
to your environment. It’s important to remember that improper configuration can reveal sensitive characteristics of your 
environment, which could be exploited by attackers.

Following OWASP guidelines will help you on the journey to keep your systems protected against certain attack vectors. Proper 
configuration of **Response Headers** also contributes to user privacy, improves performance, and ensures site compatibility.

---

| [⬆️Return to index](../index.md) | Go to Act 2 (soon) |
|----------------------------------|--------------------|
