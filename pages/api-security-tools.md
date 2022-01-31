---

title: API Security Tools
layout: col-sidebar
author: Matt Tesauro
contributors: kingthorin
tags: api, tools, oss
permalink: /api_security_tools

---

{% include writers.html %}

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

{% include api-tools.html %}

#### Adding Tools

To add items, please add a stanza to the yaml file [here](https://github.com/OWASP/www-community/blob/master/_data/api-tools.yml) or email me at matt.tesauro AT owasp.org
