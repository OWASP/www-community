---

title: OWASP Community Meetings
layout: col-sidebar
permalink: meetings/

---

<!-- 
    This information is taken from _data/community_events.json which is itself automatically generated nightly.  
    This information posted here is taken from the meetup groups for chapters and projects. 
    To have your information displayed, make sure your chapter, project, or committee:
        1.) Has an meetup group which is under the OWASP organization's meetup
        2.) Has the meetup group name in the front matter of the index.md file as meetup-group: [Group Name]
            ex.) meetup-group: OWASP-Delaware-Chapter
-->

<br>
{% assign events = site.data.community_events | sort: 'date' %}
{% assign prevdate = nil %}

<!-- Index list -->

## Quick List (Details below)
{% assign i = 0 %}
{% for event in events %}
  {% assign evdate = event.date | date: "%b %d" %}
  * <a href='#{{i}}_item'>{{ event.name }}</a> - {{ event.group }}, {{ evdate }}
  {% assign i = i | plus: 1 %}
{% endfor %}

<!-- Full list -->
{% assign i = 0 %}
{% for event in events %}
{% assign evdate = event.date | date: "%B %d, %Y" %}
{% if evdate <> prevdate %}
---
## {{ evdate }}
---
{% assign prevdate = evdate %}
{% endif %}
### Event: <a name="{{ i }}_item">{{ event.name }} </a>
#### Group: [{{ event.group }}](/{{ event.repo }}/)
#### Time: {{ event.time }} ({{ event.timezone }})
#### Link: [{{ event.link }}]({{ event.link }})
<div>
<strong>Description</strong>: {{ event.description }}
</div>
<br>
  {% assign i = i | plus: 1 %}
{% endfor %}
