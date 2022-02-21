---

layout: col-sidebar
title: Cross-User Defacement
author: 
contributors: Zhong, Rezos, KristenS
permalink: /attacks/Cross-User_Defacement
tags: attack, Cross-User Defacement

---

{% include writers.html %}

## Description

An attacker can make a single request to a vulnerable server that will
cause the server to create two responses, the second of which may be
misinterpreted as a response to a different request, possibly one made
by another user sharing the same TCP connection with the server. This can
be accomplished by convincing the user to submit the malicious request
themselves, or remotely in situations where the attacker and the user
share a common TCP connection to the server, such as a shared proxy
server. In the best case, an attacker can leverage this ability to
convince users that the application has been hacked, causing users to
lose confidence in the security of the application. In the worst case,
an attacker may provide specially crafted content designed to mimic the
behavior of the application but redirect private information, such as
account numbers and passwords, back to the attacker.

This attack is rather difficult to carry out in the real environment.
The list of conditions is long and hard to accomplish by the attacker.

Cross-User Defacement attack is possible because of [HTTP Response
Splitting]({{ site.baseurl }}/attacks/HTTP_Response_Splitting) and flaws in the web
application. It is crucial from the attacker's point of view that the
application allows for filling the header field with more than one
header using CR (Carriage Return) and LF (Line Feed) characters.

## Risk Factors

TBD

## Examples

We have found a web page, which gets service name from the "page"
argument and then redirects (302) to this service.

Example: <http://testsite.com/redir.php?page=http://other.testsite.com/>

And exemplary code of the redir.php:

```
rezos@spin ~/public_html $ cat redir.php
<?php
header ("Location: " . $_GET['page']);
?>
```

Crafting appropriate requests:

```
/redir.php?page=http://other.testsite.com%0d%0aContent-
Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aContent-
Type:%20text/html%0d%0aContent-
Length:%2019%0d%0a%0d%0a<html>deface</html>
```

HTTP server will respond with two (not one!) following headers:

1

```
HTTP/1.1 302 Moved Temporarily
Date: Wed, 24 Dec 2003 15:26:41 GMT
Location: http://testsite.com/redir.php?page=http://other.testsite.com
Content-Length: 0
```

2

```
HTTP/1.1 200 OK
Content-Type: text/html
Content-Length: 19
<html>deface</html>
```

If user shares a TCP connection (e.g. proxy cache) and will send a
request:` /index.html`
the response 2 will be sent to them as an answer to their request.

This way it was possible to replace the web page, which was served to
the specified user.

More information can be found in one of the presentations under
<http://wiki.owasp.org/images/1/1a/OWASPAppSecEU2006_HTTPMessageSplittingSmugglingEtc.ppt>

## Related [Attacks]({{ site.baseurl }}/attacks/)

- [HTTP Response Splitting]({{ site.baseurl }}/attacks/HTTP_Response_Splitting)
- [Cache Poisoning]({{ site.baseurl }}/attacks/Cache_Poisoning)

## Related [Controls]({{ site.baseurl }}/controls/)

- Validation of the input data (CR and LF).
- Forbid HTTP headers nesting in one header's field.
