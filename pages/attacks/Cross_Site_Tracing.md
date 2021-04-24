---

layout: col-sidebar
title: Cross Site Tracing
author: 
contributors: Kcghost, KristenS, Ryan Dewhurst, Andrew Smith
permalink: /attacks/Cross_Site_Tracing
tags: attack, Cross Site Tracing

---

{% include writers.html %}

## Description

A **Cross-Site Tracing (XST)** attack involves the use of [Cross-site
Scripting (XSS)]({{ site.baseurl }}/attacks/xss) and the TRACE
or TRACK HTTP methods. According to
[RFC 2616](http://www.w3.org/Protocols/rfc2616/rfc2616-sec9.html),
"TRACE allows the client to see what is being received at the other end
of the request chain and use that data for testing or diagnostic
information.", the TRACK method works in the same way but is specific to
Microsoft's IIS web server. XST could be used as a method to steal
user's cookies via [Cross-site Scripting
(XSS)]({{ site.baseurl }}/attacks/xss) even if the cookie has
the "[HttpOnly](../HttpOnly)" flag set or exposes the user's
Authorization header.

The TRACE method, while apparently harmless, can be successfully
leveraged in some scenarios to steal legitimate users' credentials. This
attack technique was discovered by Jeremiah Grossman in 2003, in an
attempt to bypass the [HttpOnly](../HttpOnly) tag that Microsoft
introduced in Internet Explorer 6 sp1 to protect cookies from being
accessed by JavaScript. As a matter of fact, one of the most recurring
attack patterns in Cross Site Scripting is to access the document.cookie
object and send it to a web server controlled by the attacker so that
they can hijack the victim's session. Tagging a cookie as
[HttpOnly](../HttpOnly) forbids JavaScript to access it,
protecting it from being sent to a third party. However, the TRACE
method can be used to bypass this protection and access the cookie even
in this scenario.

Modern browsers now prevent TRACE requests being made via JavaScript,
however, other ways of sending TRACE requests with browsers have been
discovered, such as using Java.

## Examples

An example using cURL from the command line to send a TRACE request to a
web server on the localhost with TRACE enabled. Notice how the web
server responds with the request that was sent to it.

```console
$ curl -X TRACE 127.0.0.1
TRACE / HTTP/1.1
User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5
Host: 127.0.0.1
Accept: */*
```

In this example notice how we send a Cookie header with the request and
it is also in the web server's response.

```console
$ curl -X TRACE -H "Cookie: name=value" 127.0.0.1
TRACE / HTTP/1.1
User-Agent: curl/7.24.0 (x86_64-apple-darwin12.0) libcurl/7.24.0 OpenSSL/0.9.8r zlib/1.2.5
Host: 127.0.0.1
Accept: */*
Cookie: name=value
```

In this example the TRACE method is disabled, notice how we get an error
instead of the request we sent.

```console
$ curl -X TRACE 127.0.0.1
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html><head>
<title>405 Method Not Allowed</title>
</head><body>
<h1>Method Not Allowed</h1>
<p>The requested method TRACE is not allowed for the URL /.</p>
</body></html>
```

Example JavaScript XMLHttpRequest TRACE request. In Firefox 19.0.2 it
will not work and return a "Illegal Value" error. In Google Chrome
25.0.1364.172 it will not work and return a "Uncaught Error:
SecurityError: DOM Exception 18" error. This is because modern browsers
now block the TRACE method in XMLHttpRequest to help mitigate XST.

```html
<script>
  var xmlhttp = new XMLHttpRequest();
  var url = 'http://127.0.0.1/';

  xmlhttp.withCredentials = true; // send cookie header
  xmlhttp.open('TRACE', url, false);
  xmlhttp.send();
</script>
```

## Remediation

### Apache

In Apache versions 1.3.34, 2.0.55 and later, set the TraceEnable
directive to "off" in the main configuration file and then restart
Apache. See
[TraceEnable](http://httpd.apache.org/docs/2.2/mod/core.html#traceenable)
for further information.

`TraceEnable off`

## Related [Attacks]({{ site.baseurl }}/attacks/)

  - [Cross-site Scripting(XSS)]({{ site.baseurl }}/attacks/xss)

## References

  - Cross-Site Tracing (XST):
    <http://www.cgisecurity.com/whitehat-mirror/WH-WhitePaper_XST_ebook.pdf>
  - [Testing for HTTP Methods and XST
    (OWASP-CM-008)](Testing_for_HTTP_Methods_and_XST_\(OWASP-CM-008\) "wikilink")
  - [OSVDB 877](https://vulners.com/osvdb/OSVDB:877)
  - [CVE-2005-3398](https://nvd.nist.gov/vuln/detail/CVE-2005-3398)
  - [XSS: Gaining access to HttpOnly Cookie
    in 2012](http://seckb.yehg.net/2012/06/xss-gaining-access-to-httponly-cookie.html)
  - [Mozilla
    Bug 302489](https://bugzilla.mozilla.org/show_bug.cgi?id=302489)
  - [Mozilla
    Bug 381264](https://bugzilla.mozilla.org/show_bug.cgi?id=381264)
