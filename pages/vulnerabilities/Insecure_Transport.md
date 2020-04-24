---

layout: col-sidebar
title: Insecure Transport
author: 
contributors: 
permalink: /vulnerabilities/Insecure_Transport
tags: vulnerability, Insecure Transport

---

{% include writers.html %}

## Description

The application configuration should ensure that SSL is used for all access controlled pages.

If an application uses SSL to guarantee confidential communication with client browsers, the application configuration should make it impossible to view any access controlled page without SSL. However, it is not an uncommon problem that the configuration of the application fails to enforce the use of SSL on pages that contain sensitive data.

There are three common ways for SSL to be bypassed:

- A user manually enters the URL and types "HTTP" rather than "HTTPS".
- Attackers intentionally send a user to an insecure URL.
- A programmer erroneously creates a relative link to a page in the application, failing to switch from HTTP to HTTPS. (This is particularly easy to do when the link moves between public and secured areas on a web site.)
## Examples

- Login pages are not SSL protected
- A publicly accessible page contains a relative link to a protected page which forgets to switch to SSL.

## Related [Attacks](../attacks/)

- Attackers that are trying to steal login credentials, session IDs or other sensitive information
- Bypassing SSL by entering HTTP instead of HTTPS
- Sending insecure URLs of protected pages to the victim (e.g. login page) to trick the victim into accessing the privileged pages via HTTP
