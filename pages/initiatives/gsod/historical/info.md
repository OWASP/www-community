### Important Community Links

* [Community]({{ site.baseurl }}/)
  * [Initiatives]({{ site.baseurl }}/initiatives/)
    * [Code Sprints]({{ site.baseurl }}/initiatives/code_sprint/)
    * [Google Summer of Code]({{ site.baseurl }}/initiatives/gsoc/)
    * [Google Season of Docs]({{ site.baseurl }}/initiatives/gsod/)

#### Historical
{% assign pages = site.pages | sort: 'title' | where_exp: "page", "page.path contains 'gsod/historical'" | where_exp: "page", "page.name != 'info.md'" %}
{% for historical in pages %}
{% if page.name == historical.name %}
* {{historical.title}}(You are here)
{% else %}
* [{{historical.title}}]({{historical.url}})
{% endif %}
{% endfor %} 