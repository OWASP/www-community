---

layout: col-sidebar
title: Attacks
author:
contributors:
tags: 
permalink: /attacks/

---

{% include writers.html %}

# What is an attack?

Attacks are the techniques that attackers use to exploit the vulnerabilities in applications. Attacks are often confused with vulnerabilities, so please try to be sure that the attack you are describing is something that an attacker would do, rather than a weakness in an application.

## List of Attacks

<ul>
{% if site.host == "127.0.0.1" %}
{% assign root_path = "" %}
{%- else -%}
{% assign root_path = "/www-community" %}
{%- endif -%}
{% assign attackpages = site.pages | where_exp: "item", "item.tags contains 'attack'" %}
{% for page in attackpages %}
    <li><a href='{{root_path}}{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>
