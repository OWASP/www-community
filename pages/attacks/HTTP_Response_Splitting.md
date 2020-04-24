---

layout: col-sidebar
title: HTTP Response Splitting
author: 
contributors: 
permalink: /attacks/HTTP_Response_Splitting
tags: attack, HTTP Response Splitting
auto-migrated: 1

---

{% include writers.html %}

## Description

HTTP response splitting occurs when:

  - Data enters a web application through an untrusted source, most
    frequently an HTTP request.
  - The data is included in an HTTP response header sent to a web user
    without being validated for malicious characters.

HTTP response splitting is a means to an end, not an end in itself. At
its root, the attack is straightforward: an attacker passes malicious
data to a vulnerable application, and the application includes the data
in an HTTP response header.

To mount a successful exploit, the application must allow input that
contains CR (carriage return, also given by %0d or \\r) and LF (line
feed, also given by %0a or \\n)characters into the header AND the
underlying platform must be vulnerable to the injection of such
characters. These characters not only give attackers control of the
remaining headers and body of the response the application intends to
send, but also allow them to create additional responses entirely under
their control.

The example below uses a Java example, but this issue has been fixed in
virtually all modern Java EE application servers. If you are concerned
about this risk, you should test on the platform of concern to see if
the underlying platform allows for CR or LF characters to be injected
into headers. We suspect that, in general, this vulnerability has been
fixed in most modern application servers, regardless of what language
the code has been written in.

## Examples

The following code segment reads the name of the author of a weblog
entry, author, from an HTTP request and sets it in a cookie header of an
HTTP response.

```
    String author = request.getParameter(AUTHOR_PARAM);
    ...
    Cookie cookie = new Cookie("author", author);
        cookie.setMaxAge(cookieExpiration);
        response.addCookie(cookie);
```

Assuming a string consisting of standard alpha-numeric characters, such
as "Jane Smith", is submitted in the request the HTTP response including
this cookie might take the following form:

```
    HTTP/1.1 200 OK
    ...
    Set-Cookie: author=Jane Smith
    ...
```

However, because the value of the cookie is formed of unvalidated user
input, the response will only maintain this form if the value submitted
for AUTHOR_PARAM does not contain any CR and LF characters. If an
attacker submits a malicious string, such as "Wiley
Hacker\\r\\nContent-Length:45\\r\\n\\r\\n...", then the HTTP response
would be split into an imposter response followed by the original
response, which is now ignored:

```
    HTTP/1.1 200 OK
    ...
    Set-Cookie: author=Wiley Hacker
    Content-Length: 999

    <html>malicious content...</html> (to 999th character in this example)
    Original content starting with character 1000, which is now ignored by the web browser...
```

The ability of the attacker to construct arbitrary HTTP responses
permits a variety of resulting attacks, including: [Cross-User
Defacement](Cross-User_Defacement "wikilink"), [Cache
Poisoning](Cache_Poisoning "wikilink"), [Cross-site Scripting
(XSS)](Cross-site_Scripting_\(XSS\) "wikilink") and [Page
Hijacking](Page_Hijacking "wikilink").

__NOTOC__

[Category: Attack](Category:_Attack "wikilink")