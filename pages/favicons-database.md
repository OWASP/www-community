---
title: OWASP Favicon Database
layout: col-sidebar
author: Vlatko Kosturjak
contributors: Ryan Dewhurst, Paulino Calderon, Brian Martin, Darius Freamon, Nikhil Raj
tags: favicons, oss
permalink: /favicons_database
---

{% include writers.html %}

This content represents a community attempt to enumerate/document fingerprints of known favicons (favicon.ico) used on the web. We have faced problems how to enumerate http(s) hosts on the Internet. Currently, we have recognized two types of HTTP servers which we want to cover. The first type are HTTP servers on network devices and appliances. The second type is normal web servers with virtual hosts support. A portion of this effort is to have software enumerated via favicon.ico. How to do that? Take hash (MD5, etc) of favicon.ico and compare it against a known database (such as this one).

## OWASP Favicons

{% include favicons-database.html %}

#### Adding Favicons

To add items, please add a stanza to the yaml file [here](https://github.com/OWASP/www-community/blob/master/_data/favicons-database.yml).
