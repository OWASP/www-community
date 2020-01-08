---

title: Security Headers
layout: col-sidebar
author:
contributors:
tags:
auto-migrated: 1
permalink: /Security_Headers

---

HTTP headers which should be included by default. Methods for modifying
or removing the headers for specific instances should be provided, but
by default there are secure settings which should be enabled unless
there are other overriding concerns.

  - X-Frame-Options: SAMEORIGIN
    [1](https://developer.mozilla.org/en-US/docs/HTTP/X-Frame-Options%7Cref)
  - X-XSS-Protection: 1; mode=block
    [2](http://blogs.msdn.com/b/ieinternals/archive/2011/01/31/controlling-the-internet-explorer-xss-filter-with-the-x-xss-protection-http-header.aspx%7Cref)
  - X-Content-Type-Options: nosniff
  - Content-Type: text/html; charset=utf-8

Additionally, no headers should be included that needlessly divulge
information about the server or it's configuration that an end user
wouldn't need.
