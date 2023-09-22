---
title: OWASP Favicon Database
layout: col-sidebar
author:
contributors:
tags: favicons, oss
permalink: /favicons_database
---

{% include writers.html %}

So, project has started the adventure of getting the statistics of MD5 fingerprints of most usual favicons.ico. We have faced problems how to enumerate http(s) hosts on Internet. Currently, we have recognized two types of http servers which we want to cover. First type is http servers on network devices and appliances and the second type is normal web servers with virtual hosts support. Idea is to have software enumerated via favicon.ico. How to do that? Take hash (in our case MD5) of favicon.ico and compare it against the known database. This project is about the favicon database itself and process in how to get the database of most frequent ones by crawling internet.

## OWASP Favicons

{% include favicons-database.html %}

#### Adding Favicons

To add items, please add a stanza to the yaml file [here](https://github.com/OWASP/www-community/blob/master/_data/favicons-database.yml).
