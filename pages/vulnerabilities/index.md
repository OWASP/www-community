---

layout: col-sidebar
title: Vulnerabilities
author:
contributors:
tags: vulnerabilities
permalink: /vulnerabilities

---

## What is a vulnerability?

<categorytree hideroot="on" style="float:right; clear:right; margin-left:1ex; border:1px solid gray; padding:0.7ex; background-color:white;">Vulnerability</categorytree>
A vulnerability is a hole or a weakness in the application, which can be
a design flaw or an implementation bug, that allows an attacker to cause
harm to the stakeholders of an application. Stakeholders include the
application owner, application users, and other entities that rely on
the application. The term "vulnerability" is often used very loosely.
However, here we need to distinguish
[threats](:Category:Threat "wikilink"),
[attacks](/attacks), and
[countermeasures](:Category:Countermeasure "wikilink").

Please **do not post any actual vulnerabilities** in products, services,
or web applications. Those disclosure reports should be posted to
bugtraq or full-disclosure mailing lists.

## Examples of vulnerabilities

  - Lack of input validation on user input
  - Lack of sufficient logging mechanism
  - Fail-open error handling
  - Not closing the database connection properly

For a great overview, check out the [OWASP Top Ten
Project](OWASP_Top_Ten_Project "wikilink"). You can read about the top
vulnerabilities and download a paper that covers them in detail. Many
organizations and agencies use the Top Ten as a way of creating
awareness about application security.

**NOTE:** Before you add a vulnerability, please search and make sure
there isn't an equivalent one already. You may want to consider creating
a redirect if the topic is the same. Every vulnerability article has a
defined structure. Please read the details of [How To Add a
Vulnerability](How_To_Add_a_Vulnerability "wikilink") before creating a
new article.

## List of Vulnerabilities

<ul>
{% for page in site.pages %}
    {% if page.path contains 'pages/vulnerabilities/' and page.name != 'index.md' %}
    <li><a href='/www-community{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
    {% endif %}
{% endfor %}
</ul>
