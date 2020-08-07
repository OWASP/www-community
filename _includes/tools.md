{% assign tools = site.data.tools | | where: "type", include.type %}

{% for tool in tools %}
* [{{ tool.title }}]({{ tool.url }})
    - Owner: {{ tool.owner }}
    - License: {{ tool.license }}
    - Platforms: {{ tool.platforms }}
    - Note: {{ tool.note }}
{% endfor %}
