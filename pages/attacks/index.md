# What is an attack?

Attacks are the techniques that attackers use to exploit the vulnerabilities in applications. Attacks are often confused with vulnerabilities, so please try to be sure that the attack you are describing is something that an attacker would do, rather than a weakness in an application.

## List of Attacks
<ul>
{% for page in site.pages %}
    {% if page.path contains 'pages/attacks/' %}
    <li><a href='/www-community{{ page.url }}'>{{ page.title }}</a>{% if page.author %} by {{ page.author }}{% endif %}{% endif %}{% endfor %}</li>
</ul>