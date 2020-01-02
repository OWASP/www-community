---

layout: col-sidebar
title: OWASP Community Pages
tags: community

---

<!-- rebuild 2 -->

OWASP Community Pages is a place where OWASP can accept community contributions for security-related content.
To contribute, go to the [repository for this site.](https://github.com/OWASP/www-community)
Go into the pages folder and create a new file.  Save and commit the file. 

Include the following front matter in your file (for examples, see pages/password-special-characters.md in this repository):

    ---

    layout: col-sidebar
    title: [title of page]
    author: [author name]
    contributors: [contributors]
    permalink: [direct link to page, removes /pages] (this is optional and requires some care)
    tags: [attack, XSS, etc]
    
    ---

## File Listing

{% assign pages = site.pages | sort: 'name' | where_exp: "page", "page.path contains 'pages/'" | where_exp: "page", "page.name != 'index.md'" | where_exp: "page": "page.name != 'info.md'"%}
<ul>
{% for page in pages %}
       <li><a href='/www-community{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}</li>
{% endfor %}
</ul>

{% capture all_tags %}
{% for page in site.pages %}
{% for tag in page.tags %}
{{ tag }}{% if not forloop.last %},{% endif %}
{% endfor %}
{% endfor %}
{% endcapture %}
{% assign tag_list = all_tags | split: "," | uniq %}
{% for t in tag_list %}
{{ t }}
{% endfor %}
