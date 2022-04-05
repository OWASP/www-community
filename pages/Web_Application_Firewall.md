---

layout: col-sidebar
title: Web Application Firewall
author:
contributors:
tags: WAF, Web Application Firewall
permalink: /Web_Application_Firewall
auto-migrated: 1

---

{% include writers.html %}

## Description
A '''web application firewall (WAF)''' is an [application firewall](https://en.wikipedia.org/wiki/Web_application_firewall) for HTTP applications. It applies a set of rules to an HTTP conversation. Generally, these rules cover common attacks such as [Cross-site Scripting (XSS)](attacks/xss) and [SQL Injection](attacks/SQL_Injection).

While proxies generally protect clients, WAFs protect servers. A WAF is deployed to protect a specific web application or set of web applications. A WAF can be considered a [reverse proxy](https://en.wikipedia.org/wiki/Reverse_proxy).

WAFs may come in the form of an appliance, server plugin, or filter, and may be customized to an application. The effort to perform this customization can be significant and needs to be maintained as the application is modified.

## OWASP Projects

* The [OWASP ModSecurity CRS Project's](/www-project-modsecurity-core-rule-set/) goal is to provide an easily "pluggable" set of generic attack detection rules that provide a base level of protection for any web application.
* The [OWASP Coraza WAF project](/www-project-coraza-web-application-firewall/) is a WAF framework that can be easily integrated into your applications. It supports the OWASP ModSecurity CRS rules and Modsecurity syntax.
* Consider the [WASC OWASP Web Application Firewall Evaluation Criteria Project (WAFEC)](/www-project-wafec) to help evaluate commercial and open source web application firewalls.
	
## References

[https://en.wikipedia.org/wiki/Web_application_firewall](https://en.wikipedia.org/wiki/Web_application_firewall)
