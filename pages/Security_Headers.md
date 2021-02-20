---

title: Security Headers
layout: col-sidebar
author:
contributors:
tags:
auto-migrated: 1
permalink: /Security_Headers

---

{% include writers.html %}

HTTP headers which should be included by default. Methods for modifying
or removing the headers for specific instances should be provided, but
by default there are secure settings which should be enabled unless
there are other overriding concerns.

  - X-Frame-Options: SAMEORIGIN
    [(for more info)](https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options)
  - X-XSS-Protection: 0 [(for more info)](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html#x-xss-protection-header)
  - X-Content-Type-Options: nosniff
  - Content-Type: text/html; charset=utf-8

Additionally, no headers should be included that needlessly divulge
information about the server or it's configuration that an end user
wouldn't need.
