---

layout: col-sidebar
title: Information exposure through query strings in URL
author: Robert Gilbert (amroot)
contributors: Michal Biesiada
permalink: /vulnerabilities/Information_exposure_through_query_strings_in_url
tags: vulnerability, Information exposure through query strings in url

---

{% include writers.html %}

## Description

Information exposure through query strings in URL is when sensitive data is passed to parameters in the URL. This allows attackers to obtain sensitive data such as usernames, passwords, tokens (authX), database details, and any other potentially sensitive data. Simply using HTTPS does not resolve this vulnerability.

## Risk Factors

- Threat Agents: App Specific
- Attack Vectors: Average
- Security Weakness (prevalence): Common
- Security Weakness (detectability): Difficult
- Technical Impacts: Moderate
- Business Impacts: App Specific

## Examples

Regardless of using encryption, the following URL will expose information in the locations detailed below: <https://vulnerablehost.com/authuser?user=bob&authz_token=1234&expire=1500000000>

The parameter values for `user`, `authz_token`, and `expire` will be exposed in the following locations when using HTTP or HTTPS:

- Referer Header
- Web Logs
- Shared Systems
- Browser History
- Browser Cache
- Shoulder Surfing

When not using an encrypted channel, all of the above and the following:

- Man-in-the-Middle

### Exposure Proof-of-Concept

The following figure displays how an internal attacker can potentially exploit this vulnerability as the request above is captured in the server logs even when requested via an encrypted channel: <https://vulnerablehost.com/information-exposure-log.png>

### Other Real-World Example

A web application sent a one-time password (OTP) and the user's email address in the query string of a login URL delivered by email:

`https://vulnerablesite/sign_in?email_otp=true&otp_code=123456&user%5Bemail%5D=john.doe%40example.com`

This approach exposes sensitive information (OTP token and personally identifiable information) in browser history, server logs, and third-party monitoring tools. Even if the OTP is short-lived, the exposure window creates a security risk and violates secure session management practices. 
An OTP must be treated as a secret credential equivalent to a password, since exposure during its validity window can enable unauthorized account access.
Email addresses are confidential PII, and in many applications they also serve as a login identifier (part of the user's credentials). Exposing them in query strings therefore poses both privacy and authentication risks.

## Related [Attacks](../attacks/)

- [Forced browsing](../attacks/Forced_browsing)

## References

- [Top 10-2017 A3-Sensitive Data Exposure](https://www.owasp.org/index.php/Top_10-2017_A3-Sensitive_Data_Exposure)
- [Top 10 2013-A6-Sensitive Data Exposure](https://www.owasp.org/index.php/Top_10_2013-A6-Sensitive_Data_Exposure)
- [CWE-598: Information Exposure Through Query Strings in GET Request](https://cwe.mitre.org/data/definitions/598.html)
- [4.4.1.1. Threat: Eavesdropping or Leaking Authorization "codes"](https://tools.ietf.org/html/rfc6819#section-4.4.1)
- [Passwords Submitted Using GET Method](https://portswigger.net/knowledgebase/issues/details/00400300_passwordsubmittedusinggetmethod)
