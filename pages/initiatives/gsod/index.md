---

layout: col-sidebar
title: Google Season of Docs
tags: gsod, Google Season of Docs
permalink: /initiatives/gsod/

---

{% if site.host == "127.0.0.1" %}
{% assign root_path = "" %}
{%- else -%}
{% assign root_path = "/www-community" %}
{%- endif -%}

## Information

OWASP was part of the initial Google Season of Docs last year

### Current
{% assign current = site.pages | where: 'url', '/initiatives/gsod/current/' | first %}
* [{{current.title}}]({{root_path}}{{current.url}})

### Historical
{% assign pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains 'gsod/historical'" | where_exp: "page", "page.name != 'info.md'" %}
{% for historical in pages %}
* [{{historical.title}}]({{root_path}}{{historical.url}})
{% endfor %} 
