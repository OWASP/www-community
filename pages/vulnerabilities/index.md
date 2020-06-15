---

layout: col-sidebar
title: Vulnerabilities
author:
contributors:
tags: vulnerabilities
permalink: /vulnerabilities/

---

## What is a vulnerability?

A vulnerability is a hole or a weakness in the application, which can be
a design flaw or an implementation bug, that allows an attacker to cause
harm to the stakeholders of an application. Stakeholders include the
application owner, application users, and other entities that rely on
the application. 

Please **do not post any actual vulnerabilities** in products, services,
or web applications. Those disclosure reports should be posted to
bugtraq or full-disclosure mailing lists.

## Examples of vulnerabilities

  - Lack of input validation on user input
  - Lack of sufficient logging mechanism
  - Fail-open error handling
  - Not closing the database connection properly

For a great overview, check out the [OWASP Top Ten
Project](/www-project-top-ten). You can read about the top
vulnerabilities and download a paper that covers them in detail. Many
organizations and agencies use the Top Ten as a way of creating
awareness about application security.

**NOTE:** Before you add a vulnerability, please search and make sure
there isn't an equivalent one already. You may want to consider creating
a redirect if the topic is the same. Every vulnerability article has a
defined structure.

## List of Vulnerabilities


<ul>
{% assign vpages = site.pages | where_exp: "item", "item.tags contains 'vulnerability'" %}
{% for page in vpages %}
    <li><a href='/www-community{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>
