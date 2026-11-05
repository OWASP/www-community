---

title: OWASP Community Meetings
layout: col-sidebar
permalink: meetings/

---
OWASP Community Meetings bring together chapters, projects, and committees for public online events.  
Use this page to quickly see upcoming meetings and jump to full details for each event.

<!-- 
    This information is taken from _data/community_events.json which is itself automatically generated nightly.  
    This information posted here is taken from the meetup groups for chapters and projects. 
    To have your information displayed, make sure your chapter, project, or committee:
        1.) Has an meetup group which is under the OWASP organization's meetup
        2.) Has the meetup group name in the front matter of the index.md file as meetup-group: [Group Name]
            ex.) meetup-group: OWASP-Delaware-Chapter
-->

<br>
{% comment %}
  Only show events dated today or later (as of the last site build), so past
  meetings are not listed as upcoming if the nightly data refresh stops.
{% endcomment %}
{% assign today = site.time | date: '%Y-%m-%d' %}
{% assign events = site.data.community_events | where_exp: 'event', 'event.date >= today' | sort: 'date' %}
{% assign prevdate = nil %}

<!-- Index list -->

## Quick list of upcoming events

{% if events.size == 0 %}
There are no upcoming community meetings listed right now. Please check [OWASP Events](https://owasp.org/events/) and the [OWASP Chapters](https://owasp.org/chapters/) pages for upcoming meetings.
{% else %}
The list below shows all upcoming OWASP community events ordered by date.  
Click an event name to jump to its detailed description further down this page.
{% endif %}

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
## Events on {{ evdate }}
---
{% assign prevdate = evdate %}
{% endif %}
### {{ event.name }} <a name="{{ i }}_item"></a>

**Group:** [{{ event.group }}](https://owasp.org/{{ event.repo }}/)  
**Time:** {{ event.time }} ({{ event.timezone }})  
**Link:** [{{ event.link }}]({{ event.link }})

**Description:** {{ event.description }}

<br>

{% assign i = i | plus: 1 %}
{% endfor %}
