---
layout: full-width
title: GSoC 2021 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2021ideas
---

# GSoC2021 Ideas

<!-- Template: Use a format like below to add your project:
### [Project Name]

##### [Explanation of Ideas]

##### [Expected Results]

##### [Getting Started]

##### [Mentors]
-->

## OWASP Project Requests

Tips to get you started in no particular order:
- Read the
  [Student Guidelines](gsoc2021).
- Check our
  [github organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [OWASP Juice Shop](https://owasp-juice.shop)

OWASP Juice Shop is probably the most modern and sophisticated insecure
web application! It can be used in security trainings, awareness demos,
CTFs and as a guinea pig for security tools! Juice Shop encompasses
vulnerabilities from the entire OWASP Top Ten along with many other
security flaws found in real-world applications!

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "juice shop" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Explanation of Ideas

###### Score Board

Juice Shop's existing Score Board has been rewritten from scratch once
when the project moved from AngularJS/Bootstrap to Angular/Material.
Since then, new features, filters and information has been added to it
over the years. It has grown to a point where it can be confusing for
beginners. It also became pretty slow to render over time.

After a big facelift project for all the other UI screens, the Score
Board now is the one screen left to require some special attention. As
it is the heart and soul of the Juice Shop, any redesign or usability
improvements must be thoroughly tested and strive for the best possible
user experience.

###### Your own idea

You have an awesome idea to improve OWASP Juice Shop that is not on this
list? Great, please submit it!

##### Expected Results

* A new feature or improvement of an existing one that makes OWASP Juice
  Shop even better
* Your code follows our existing styleguides and passes all existing
  quality gates regarding code smells, test coverage etc.
* Code that you write comes with automated tests that fit into
  [our available test suites](https://pwning.owasp-juice.shop/part3/contribution.html#testing).

##### Getting started

* Make sure your JavaScript/TypeScript is sufficient to work on the
  Juice Shop codebase. Check our
  [Codebase 101](https://pwning.owasp-juice.shop/part3/codebase.html)
  here. Students with some experience with (or willingness to learn)
  Angular and NodeJS/Express are usually prefered.
* Read our
  [Contribution Guidelines](https://pwning.owasp-juice.shop/part3/contribution.html)
  very carefully. Best make some small contributions before GSoC, so we
  can see how you work and help you dive into the code even better.
* Get in touch with
  [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) to discuss any
  of the listed or your own idea for GSoC!

##### Mentors

* [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) - OWASP Juice
  Shop Project Leader

----


### [OWASP Maryam](https://github.com/saeeddhqan/maryam)

##### Explanation of Ideas
OWASP Maryam is a modular open-source OSINT based framework. Maryam is written in Python and it’s designed to provide a powerful environment to harvest data from open-sources and search-engines and collect data quickly and thoroughly.

##### Getting Started

* You may read the available documents in the [wiki page](https://github.com/saeeddhqan/maryam/wiki). Especially the Development Guide section.
* Any question, problem, and discussion? contact with [Saeed Dehqan](mailto:saeed.dehghan@owasp.org).

##### Expected Results

* You may want to add a new module, search-engine, or a util class.
* The framework does not have a web user-interface.
* Rewrite the core of framework.
* A new feature or enhancement that makes OWASP Maryam better.

###### Knowledge Prerequisites

* Familiar with Python 3.x.
* Knowledge of OS (Linux, Mac...) and Services
* Object-Oriented Programming
* Web programming is an advantage

##### Mentors
* [Saeed Dehqan](mailto:saeed.dehghan@owasp.org)

----

### [Zed Attack Proxy (ZAP)](https://www.zaproxy.org)

#### Idea One: APIBlueprint or RAML Support (or both)

ZAP does not currently support parsing and subsequent testing of [APIBlueprint](https://apiblueprint.org/) or [RAML](https://raml.org/) definitions.

##### Expected Results

* Implement functionality to allow ZAP to inspect and attack given APIBlueprint/RAML endpoints.
* Code that conforms to our Development Rules and Guidelines.

##### Getting Started

* Have a look at the ZAP [CONTRIBUTING](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) guideline, especially the 'Coding' section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/labels/IdealFirstBug).

##### Mentors
* [Simon Bennetts](mailto:psiinon@gmail.com) and the ZAP core team.

#### Idea Two: Re-test Functionality

ZAP is currently able to detect vulnerabilities of various types, however it doesn't have a user friendly mechanism for re-testing or re-validating identified weaknesses.

Refer to [Issue 375](https://github.com/zaproxy/zaproxy/issues/375) for further details, and to this [User Group thread](https://groups.google.com/forum/#!searchin/zaproxy-users/retest%7Csort:date/zaproxy-users/qNKz6cNhYDg/Jw6hWi-oAwAJ) for discussion and staged implementation ideas.

##### Expected Results

* Add core or extension functionality to facilitate re-test of various results/alerts.
* Code that conforms to our Development Rules and Guidelines

##### Getting Started

* Have a look at the ZAP [CONTRIBUTING](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) guideline, especially the 'Coding' section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/labels/IdealFirstBug).

##### Mentors
* [Simon Bennetts](mailto:psiinon@gmail.com) and the ZAP core team.

#### Idea Three: Your Idea

ZAP is a great framework for building new and innovative security testing solutions. If you have an idea that is not on this list then don’t worry, you can still submit it, we have accepted original projects in previous years and have even paid a student to work on their idea when we did not get enough GSoC slots to accept all of the projects we wanted.

##### Expected Results

* A new feature that makes ZAP even better
* Code that conforms to our Development Rules and Guidelines

##### Getting Started

* Have a look at the ZAP [CONTRIBUTING](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) guideline, especially the 'Coding' section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/labels/IdealFirstBug).

##### Mentors
* [Simon Bennetts](mailto:psiinon@gmail.com) and the ZAP core team.

----

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).

##### Expected results
- Add Web Application Firewall Feature (expected)
- Improve features (IDS,Firewall)
- Complete the web GUI and remote monitoring
- Zero bugs - Fix the current identifed bugs
- Improve Detecting Website Defacements Based on Machine Learning Techniques and Attack Signatures

##### Getting started
- Check[GitHub project](https://github.com/OWASP/SecureTea-Project) and [Website](https://owasp.org/www-project-securetea/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-securetea

##### Student Requirements
- Python
- Angular

##### Mentor
* [Rejah Rehim](mailto:rejah.rehim@owasp.org)
* [Ade Yoseman](mailto:edikdoank@gmail.com)

<hr>

### [OWASP Intelligent Intrusion Detection System](https://github.com/OWASP/Intelligent-Intrusion-Detection-System)

##### Explanation of Ideas

OWASP IIDS is an open source software that leverages the benefits of Artificial Intelligence to detect the intrusion and alert the respective network administrator.

##### Getting started

* You may read the available documents in the [wiki page](https://owasp.org/www-project-intelligent-intrusion-detection-system/).

#### Expected Results

* The expected results are to work for V1.0 release.


#### Knowledge Prerequisites

* The whole framework will be written in Python language. You must be familiar with Python 3.x and Django
* Good knowledge of Network security (and Software Security)
* Knowledge of OS (Linux, Windows, Mac).
* Familiar with OSI model and security at each layer.
* Familiar with Deep Learning mainly LSTMs and different types of RNNs.
* You should also be familiar with RESTful framework and Databases

##### Mentors
* [Sri Harsha Gajavalli](mailto:sriharsha.g@owasp.org)

<hr>


----
