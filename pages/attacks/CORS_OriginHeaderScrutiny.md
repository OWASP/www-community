---

layout: col-sidebar
title: CORS OriginHeaderScrutiny
author: 
contributors: 
permalink: /attacks/CORS_OriginHeaderScrutiny
tags: attack, CORS OriginHeaderScrutiny

---

{% include writers.html %}

## Introduction

**CORS** stands for **C**ross-**O**rigin **R**esource **S**haring.

Is a feature offering the possibility for:

- A web application to expose resources to all or restricted domain,
- A web client to make AJAX request for resource on other domain than is source domain.

This article will focus on the role of the **Origin** header in the
exchange between web client and web application.

The basic process is composed of the steps below (sample HTTP
request/response has been taken from [Mozilla
Wiki](https://developer.mozilla.org/en-US/docs/HTTP_access_control)):

- **Step 1 : Web client sends a request to get a resource from a different domain.**

```
GET /resources/public-data/ HTTP/1.1
Host: bar.other
User-Agent: Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.5; en-US; rv:1.9.1b3pre) Gecko/20081130 Minefield/3.1b3pre
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: en-us,en;q=0.5
Accept-Encoding: gzip,deflate
Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7
Connection: keep-alive
Referer: http://foo.example/examples/access-control/simpleXSInvocation.html
Origin: http://foo.example

[Request Body]
```

The web client tells the server its source domain using the HTTP request
header "**Origin**".

- **Step 2 : Web application response to request.**

```
HTTP/1.1 200 OK
Date: Mon, 01 Dec 2008 00:23:53 GMT
Server: Apache/2.0.61
Keep-Alive: timeout=2, max=100
Connection: Keep-Alive
Transfer-Encoding: chunked
Content-Type: application/xml
Access-Control-Allow-Origin: *

[Response Body]
```

The web application informs the web client of the allowed domains using
the HTTP response header **Access-Control-Allow-Origin**. The header can
contain either a '\*' to indicate that all domains are allowed OR a
specified domain to indicate the specified allowed domain.

- **Step 3 : Web client process web application response.**

According to the CORS W3C specification, it's up to the web client
(usually a browser) to determine, using the web application response
HTTP header **Access-Control-Allow-Origin**, if the web client is
allowed to access response data.

## Risk

*A reminder : This article will focus on the web application side
because it's the only part in which we have the maximum of control.*

The risk here is that a web client can put any value into the **Origin**
request HTTP header in order to force web application to provide it the
target resource content. In the case of a Browser web client, the header
value is managed by the browser but another "web client" can be used
(like Curl/Wget/Burp suite/...) to change/override the "Origin" header
value. For this reason it is not recommended to use the Origin header to
authenticate requests as coming from your site.

## Countermeasure

Enable authentication on the resources accessed and require that the
user/application credentials be passed with the [CORS
requests](https://developer.mozilla.org/en-US/docs/HTTP/Access_control_CORS#Requests_with_credentials).

It is not possible to be 100% certain that any request comes from an
expected client application, since all information of a HTTP request can
be faked.

## Informations links

- [W3C Specification](http://www.w3.org/TR/cors/)
- [Mozilla Wiki](https://developer.mozilla.org/en-US/docs/HTTP_access_control)
- [Wikipedia](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
- [CORS Abuse](http://blog.secureideas.com/2013/02/grab-cors-light.html)
