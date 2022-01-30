---

title: API Security Tools
layout: col-sidebar
author: Matt Tesauro
contributors:
tags: api, tools, oss
permalink: /api_security_tools

---

APIs are becoming an increasingly large portion of the software that powers the Internet including mobile applications, single-page applications (SPAs) and cloud infrastructure. While APIs share much of the same security controls and software security issues with traditional web applications, they are different enough to make a distinction between 'normal' AppSec tools and ones that were built with APIs in mind.  This page was created to list tools known to support APIs natively and by design.

### Types of API Tools

Tools for API Security can be broken down into 3 broad categories.

* **API Security Posture**: Creates an inventory of APIs, the methods exposed and classifies the data used by each method.
  * Goal: Provide visibility into the security state of a collection of APIs.
* **API Runtime Security**: provides protection to APIs during their normal running and handling of API requests.
  * Goal: Detect and prevent malicious requests to an API.
* **API Security Testing**: Dynamic assessment of an API's security state.
  * Goal: Evaluate the security of a running API by interacting with the API dynamically (DAST-like behavior)

For more detailed information on the 3 categories, see slides 14 to 17 of [this presentation](https://www.slideshare.net/mtesauro/peeling-the-onion-making-sense-of-the-layers-of-api-security).

The goal is to provide as comprehensive a list of API tools as possible using the input of the diverse perspectives of the OWASP community.

## API Tools List

<section id="tool-list">
<div>
 {% for tool in site.data.api-tools %}
    <div>
        <div style="background: #f2f2f2;width: 80%">
          <h4><a href="{{tool.link}}">{{ tool.name }}</a> from {{tool.from}}</h4>
        </div>
        <div style="background: #cccccc;width: 80%">
            <img src="{{tool.license}}" alt="License"> |
            <img src="{{tool.platforms}}" alt="Platform"> |
            <img src="{{tool.posture}}" alt="API Posture"> |
            <img src="{{tool.runtime}}" alt="API Runtime"> |
            <img src="{{tool.testing}}" alt="API Testing">
            {{tool.notes}}
        </div>
    </div>
    <div style="height:18px;"></div>
{% endfor %}
</div>
<br/><br/>
</section>

#### Adding Tools

To add items, please add a stanza to the yaml file [here](https://github.com/OWASP/www-community/blob/master/_data/api-tools.yml) or email me at matt.tesauro AT owasp.org
<div style="height:18px;"></div>
