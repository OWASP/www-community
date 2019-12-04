---

layout: col-sidebar
title: OWASP Community Pages

---

OWASP Community Pages is a place where OWASP can accept community contributions for security-related content.
To contribute, go to the [repository for this site.](https://github.com/OWASP/www-community)
Go into the pages folder and create a new file.  Save and commit the file. 

Include the following front matter in your file (for examples, see pages/password-special-characters.md in this repository):

    ---

    layout: col-sidebar
    title: [title of page]
    author: [author name]
    contributors: [contributors]
    permalink: [direct link to page, removes /pages]
    tags: [Attacks, XSS, etc]
    
    ---

## Recently Submitted Files
{% assign pages = site.pages | sort: 'date' | limit: 10 %}
<ul>
{% for page in pages %}
    {% if page.path contains 'pages/' and page.name != 'index.md' %}
    <li><a href='/www-community{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}{% endif %}
    </li>
    {% endfor %}
</ul>