---

layout: col-sidebar
title: OWASP Community Pages
tags: community

---

<!-- rebuild 6 -->

OWASP Community Pages are a place where OWASP can accept community contributions for security-related content.
To contribute, go to the [repository for this site](https://github.com/OWASP/www-community).
Go into the `pages` folder and create a new file. Save and commit the file.

Include the following front matter and include in your file (for example, see: `pages/password-special-characters.md` in this repository):

{% raw %}
```md
---

layout: col-sidebar
title: [title of page]
author: [author name]
contributors: [contributors]
permalink: [direct link to page, removes /pages] (this is optional and requires some care)
tags: [attack, XSS, etc]

---

 {% include writers.html %}

```
{% endraw %}

**Please** ensure your content contribution is based on original work/thought and not plagiarised. Also, please ensure that contributions are vendor/product neutral.

## Content Listing

Client the triangle (or other control/character) to the left of the following headings to access an expanded list of community content pages.

<details>
<summary>Controls</summary>

{% assign control_pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains '/controls/'" | where_exp: "page", "page.name != 'index.md'" | where_exp: "page", "page.name != 'info.md'"%}
<ul>
{% for page in control_pages %}
       <li><a href='{{ site.url }}{{ site.baseurl }}{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>

</details>

<details>
<summary>Attacks</summary>

{% assign attack_pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains '/attacks/'" | where_exp: "page", "page.name != 'index.md'" | where_exp: "page", "page.name != 'info.md'"%}
<ul>
{% for page in attack_pages %}
       <li><a href='{{ site.url }}{{ site.baseurl }}{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>

</details>

<details>
<summary>Vulnerabilities</summary>

{% assign vuln_pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains '/vulnerabilities/'" | where_exp: "page", "page.name != 'index.md'" | where_exp: "page", "page.name != 'info.md'"%}
<ul>
{% for page in vuln_pages %}
       <li><a href='{{ site.url }}{{ site.baseurl }}{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>

</details>

<details>
<summary>Other</summary>

{% assign pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains 'pages/'" | where_exp: "page", "page.name != 'index.md'" | where_exp: "page", "page.name != 'info.md'"%}
{% assign already_displayed = control_pages | concat: attack_pages | concat: vuln_pages %}
<ul>
{% for page in pages %}
  {% assign display = true %}
  {% for checkpage in already_displayed %}
    {% if checkpage.url == page.url %}
      {% assign display = false %}
      {% break %}
    {% endif %}
  {% endfor %}

  {% if display %}
       <li><a href='{{ site.url }}{{ site.baseurl }}{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
  {% endif %}
{% endfor %}
</ul>

</details>
