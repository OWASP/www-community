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

###### Coding Challenges

Juice Shop's upcoming [Vulnerable Code Snippets](http://bkimminich.github.io/juice-shop/#/5/7) serve as a foundation for an ambitious new
training aspect: Coding challenges. In their current implementation the
snippets come with a spoiler area for the actually vulnerable line(s) of code. Instead, they could
offer a list of lines from which the user must select the actually vulnerable one, whereas the others simply
act as ruses. This enhancement alone would obviously not fill the time available in a GSoC project.

It could be extended by a code fixing aspect, where the user must select the right fix
from a list of choices. Or even more ambitious, a code editor could be offered where the vulnerable line(s) must
actually be fixed, and the code is then executed or statically checked in the background, to see if the vulnerability is gone.

Both parts - finding and fixing - could yield points on the Score Board, where the "hacking" and "coding" challenges
could be tracked separately. It should be configurable, if the user must first solve the hacking challenge to be offered
the corresponding coding challenge or if they are available all the time. It is even thinkable to provide CTF flags for
fixed code, so that hacking and fixing could be both offered as CTF challenges - effectively doubling the number of challenges
in a Juice Shop-powered CTF event.

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
* Jannik Hollenbach - OWASP Juice Shop Core Team
* Timo Pagel - OWASP Juice Shop Core Team

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

----

### [OWASP Intelligent Intrusion Detection System](https://github.com/OWASP/Intelligent-Intrusion-Detection-System)

##### Explanation of Ideas

OWASP IIDS is an open source software that leverages the benefits of Artificial Intelligence to detect intrusions and alert the respective network administrator.

##### Getting Started

* You may read the available documents in the [wiki page](https://owasp.org/www-project-intelligent-intrusion-detection-system/).

#### Expected Results

* The expected results are to work for V1.0 release.

#### Knowledge Prerequisites

* The whole framework will be written in Python language. You must be familiar with Python 3.x and Django
* Good knowledge of Network security (and Software Security)
* Knowledge of OS (Linux, Windows, Mac)
* Familiar with OSI model and security at each layer
* Familiar with Deep Learning mainly LSTMs and different types of RNNs
* You should also be familiar with RESTful framework and Databases

##### Mentors
* [Sri Harsha Gajavalli](mailto:sriharsha.g@owasp.org)

----

### [OWASP OWTF](https://github.com/owtf/owtf)
Offensive Web Testing Framework (OWTF) is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST. Most of the ideas below focus on rewrite of some major 
components of OWTF to make it more modular. OWTF is moving to a fresh codebase with a fully Docker testing and deployment environment.

#### OWASP OWTF - Passive Online scanner improvements

##### Brief Explanation

OWTF allows many passive tests, such as those using third party websites like Google, Bing, etc. searches, as well as handy "Search for vulnerability" search boxes (i.e. Fingerprinting plugin). This feature involves the creation of a "script" that produces an interactive OWTF report with the intention of hosting it in the github.io site. The idea here is to have a passive, JavaScript-only interactive report available on the owtf.github.io site, so that people can try OWTF "without installing anything", simply visiting a URL.

This would be a normal OWTF interactive report where the user can:
* Enter a target
* Try passive plugins (only the parts that use no tools)
* Play with boilerplate templates from the OWTF interactive report
An old version of the passive online scanner is hosted [here](https://owtf.github.io/online-passive-scanner).

##### LEGAL CLARIFICATION (Just in case!): 
The passive online scanner, simply makes OWTF passive testing through third party websites more accessible to anybody, however it is the user that must 
1. click the link manually + 
2. do something bad with that afterwards + 
3. doing 1 + 2 WITHOUT permission :). 
Therefore this passive online scanner does not do anything illegal 
[More information about why this is not illegal here](http://www.slideshare.net/abrahamaranguren/legal-and-efficient-web-app-testing-without-permission) 
(recommended reading!)

For background on OWASP OWTF please see: [OWASP OWTF](https://owasp.org/www-project-owtf/)

##### Expected results:
* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/)/ES6 JavaScript code in all modified code and surrounding areas.
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

##### Knowledge Prerequisite:

A good knowledge of JavaScript and writing ES6 compliant React/TypeScript is needed. Previous exposure to security concepts and penetration testing is not required but recommended and some lack of this can be compensated with pre-GSoC involvement and will to learn.

##### OWASP OWTF Mentors:
* [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
* Viyat Bhalodia
* [Mohit Sharma](mailto:ms892075@gmail.com)


#### OWASP OWTF - Web interface enhancements

##### Brief Explanation:

The current owtf web interface is implemented in ReactJs with Redux as the state manager. The project involves - (1) integration of Typescript in the code to ease the refactoring process, (2) upgrading the UI to remove additional dependencies and improve user experience . Check out the current implementation of the web interface at [OWTF on GitHub](https://github.com/owtf/owtf/tree/develop).

For background on OWASP OWTF please see: [OWASP_OWTF](https://owasp.org/www-project-owtf/)

##### Expected results:
- IMPORTANT:Clean, maintainable (ES6 compatible and using recommended design patterns) React (TypeScript) code.
- IMPORTANT: Thoroughly documented code along with API examples and example future components.
- CRITICAL: Excellent reliability and performance.
- Unit tests / Functional tests.

##### Getting Started:
- Have a look at the GitHub project and wiki page, get familiar with the codebase.
- Join OWASP Slack and contact us on channel #project-owtf.
- Submit PRs for the issues listed on our github page.

##### Knowledge Prerequisite:

- Python proficiency, React-Redux (high proficiency), TypeScript proficiency and general JavaScript proficiency.

##### OWASP OWTF Mentors: 
* [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
* Viyat Bhalodia
* [Mohit Sharma](mailto:ms892075@gmail.com)


#### OWASP OWTF - Login/Signup Implementation

##### Brief Explanation:

Some pages of the new OWTF interface has been under progess for a very long time.  Complete implementation of the Login/Signup Page (APIs + frontend) with proper unit/functional tests will be deliverable for this project. Check out the current implementation of the web interface at [OWTF on GitHub](https://github.com/owtf/owtf/tree/develop).

For background on OWASP OWTF please see: [OWASP_OWTF](https://owasp.org/www-project-owtf/)

##### Expected results:
- IMPORTANT:Clean, maintainable (ES6 compatible and using recommended design patterns) React (TypeScript) code.
- IMPORTANT: Thoroughly documented code along with API examples and example future components.
- CRITICAL: Excellent reliability and performance.
- Unit tests / Functional tests.

##### Getting Started:
- Have a look at the GitHub project and wiki page, get familiar with the codebase.
- Join OWASP Slack and contact us on channel #project-owtf.
- Submit PRs for the issues listed on our github page.

##### Knowledge Prerequisite:

- Python proficiency, React-Redux (high proficiency), TypeScript proficiency and general JavaScript proficiency.

##### OWASP OWTF Mentors: 
* [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
* Viyat Bhalodia
* [Mohit Sharma](mailto:ms892075@gmail.com)


#### OWASP OWTF - General Improvements

##### Brief Explanation:

There are many small but important enhancements in the issue tracker which are too small to make a single project, but they can be grouped together to make a suitable GSoC project.
The aim of the project is to implement some of the enhancements suggested in the issue tracker to improve user experience (adding new useful features and making the owtf tool easier to use), security and performance.

For background on OWASP OWTF please see: [OWASP_OWTF](https://owasp.org/www-project-owtf/)

##### Expected results:
- IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
- IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
- IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
- CRITICAL: Excellent reliability
- Good performance
- Unit tests / Functional tests
- Good documentation

##### Knowledge Prerequisite:

- Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

##### OWASP OWTF Mentors:
* [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
* Viyat Bhalodia
* [Mohit Sharma](mailto:ms892075@gmail.com)

----

### [OWASP Python Honeypot](https://github.com/OWASP/Python-Honeypot)

##### Explanation of Ideas

OWASP Honeypot is an open-source software in Python language which designed for creating honeypot and honeynet in an easy and secure way! This project is compatible with Python 3.x and tested on Mac OS X, and Linux.

##### Getting Started

* [Wiki](https://github.com/OWASP/Python-Honeypot/wiki)

#### Expected Results

* Zero Bugs
* Extend functionalities
* Enhance Performance
* Re-Design WebUI Graphs

#### Knowledge Prerequisites

* Docker
* Python
* CyberSecurity
* MongoDB
* Web Design knowledge

##### Mentors
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [Sam Stepanyan](sam.stepanyan@owasp.org)

---

### [OWASP Nettacker](https://github.com/OWASP/Nettacker)

##### Explanation of Ideas

OWASP Nettacker project is created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and other information. This software will utilize TCP SYN, ACK, ICMP, and many other protocols in order to detect and bypass Firewall/IDS/IPS devices. By leveraging a unique method in OWASP Nettacker for discovering protected services and devices such as SCADA. It would make a competitive edge compared to other scanner making it one of the bests.

##### Getting Started

* [Wiki](https://github.com/OWASP/Nettacker/wiki)

#### Expected Results

* Migrate fully to Python 3
* Re-architect the framework and all existing funtionalities/modules
* Zero Bugs
* Re-Design WebUI

#### Knowledge Prerequisites

* Docker
* Python
* CyberSecurity
* SQLite
* Web Design knowledge

##### Mentors
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [Sam Stepanyan](sam.stepanyan@owasp.org)

----

### [Security Knowledge Framework (SKF)](https://owasp.org/www-project-security-knowledge-framework/)

#### Idea One: Extending the SKF Labs with code fixing functionality

We have more then 70 SKF Labs for developers to practice the skills in security in terms of identifying and testing vulnerabilities.
Now the idea is to also create the capability to make code changes in all of the Labs using a browser editor and displaying log output.

With this editor in the labs we can now also use it to train and get experience in applying the secure design patterns and mitigating the vulnerabilities in the labs.

##### Idea One: Expected Results

* Implement a HTML Editor functionality to allow all the files within the Docker image to be updated
* Implement a application log window to see stacktraces or errors
* The component that is running next to the Lab application needs to be build so it can be used for all type of Languages we use in the Labs, for example Python, Java, Ruby, Nodejs


#### Idea Two: Your own idea

Let us know if you have a strong other idea! :)


#### Knowledge Prerequisites

* Docker
* HTML
* Angular9
* Javascript
* Design / styling
* Python
* Kubernetes

##### Getting Started
Have a look at the SKF Labs and inspect the Docker files, source code of the Labs and get an idea how we build them.
These are then all used in the OWASP-SKF project where people can launch the Labs from there in a Kubernetes Cluster.

* [SKF-Labs](https://github.com/blabla1337/skf-labs)

##### Mentors
* [Glenn ten Cate](glenn.ten.cate@owasp.org)
* [Riccardo ten Cate](riccardo.ten.cate@owasp.org)

----

### [OWASP DefectDojo](https://github.com/DefectDojo/django-DefectDojo)

##### Explanation of Ideas
OWASP DefectDojo is a security program and vulnerability management tool.

Our UI is old and crancky. Many JS libraries used at the start of the project are old and not maintained for many years.

Our web interface needs a brand new modern UI. 
We want a light modern UI based on ReactJS that will leverage our API (a SPA that uses an OpenAPI).

It's a blank page to write and would help us in propulsing DefectDojo in a new UI/UX era.

##### Getting Started

* You may read the available documents in the [wiki page](https://defectdojo.github.io/django-DefectDojo/), especially the Development Guide section.
* Any questions, problems, and want an introduction? Contact both [Damien Carol](mailto:damien.carol@gmail.com) and [Fred Blaise](mailto:fred.blaise@owasp.org).

##### Expected Results

* New SPA that covers at least 30% of the features of the current UI.

###### Knowledge Prerequisites

* Web programming with ReactJS.
* Some knowledge of OpenAPI/Swagger 
* Python programming is an advantage

##### Mentors
* [Damien Carol](mailto:damien.Carol@gmail.com)
* [Fred Blaise](mailto:fred.blaise@gmail.com)

----

### [OWASP Bug Logging Tool](https://github.com/OWASP/BLT)

##### Brief Explanation

BLT lets anyone report issues they find on the internet. Found something out of place on Amazon.com ? Let them know. Companies are held accountable and shows their response time and history. Get points for reporting bugs and help keep the internet bug free.

##### Getting Started
* Get in touch with [Sourav Badami](mailto:sourav.badami@owasp.org) to discuss your idea.

##### Expected Results
* Flutter app for bug hunting and crowd sourcing hunters with bounty support on top of the existing platform.
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

##### Knowledge Prerequisites
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Flutter, Python, Django some security knowledge would be preferable.

##### Mentors
* [Sourav Badami](mailto:sourav.badami@owasp.org) - OWASP Bug Logging Tool Project Leader
* [Sean Auriti](mailto:sean.auritii@owasp.org) - OWASP Bug Logging Tool Project Leader

----
