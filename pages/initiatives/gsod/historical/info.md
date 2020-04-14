### Important Community Links

* [Community](/www-community/)
  * [Initiatives](/www-community/initiatives/)
    * [Code Sprints](/www-community/initiatives/code_sprint/)
    * [Google Summer of Code](/www-community/initiatives/gsoc/)
    * [Google Season of Docs](/www-community/initiatives/gsod/)

#### Historical
{% assign pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains 'gsod/historical'" | where_exp: "page", "page.name != 'info.md'" %}
{% for historical in pages %}
{% if page.name == historical.name %}
* {{historical.title}}(You are here)
{% else %}
* [{{historical.title}}]({{historical.url}})
{% endif %}
{% endfor %} 