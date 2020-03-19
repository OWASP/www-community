---

layout: full-width
title: GSoC 2020 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2020ideas

---
# GSoC2020 Ideas
<!-- Template: Use a format like below to add your project:
### [Project Name]

##### [Explanation of Ideas]

##### [Expected Results]

##### [Getting Started]

##### [Mentors]
-->

## OWASP Project Requests

Tips to get you started in no particular order:
- Read the [Student Guidelines](gsoc2020).
- Check our [github organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [OWASP Python Honeypot](https://github.com/zdresearch/OWASP-Honeypot)

##### Explanation of Ideas

OWASP Honeypot is an open source software in Python language which designed for creating honeypot and honeynet in an easy and secure way! This project is compatible with Python 2.x and 3.x and tested on Windows, Mac OS X and Linux.

##### Expected Results

* Zero Bugs: Currently we may have several bugs in different conditions, and it's best to test the all functions and fix them
* New modules: add some creative ICS/Network/Web/Database modules andvulnerable web applications, services and stuff
* API: update API sync to all features
* WebUI: Demonstrate and add API on WebUI and Live version with all features
* WebUI Special Reports: Track the attacks more creative and provide high risk IPs
* Database: Better database structure, faster and use queue
* Data analysis: Analysis stored data and attack signatures
* OWASP Top 10: Preparing useful processed/raw data for OWASP top 10 project

##### Getting Started

It's best to start from GitHub [wiki page](https://github.com/zdresearch/OWASP-Honeypot/wiki), we are looking forward to adding more modules and optimize the core.

##### Students Requirements

* Python
* Packet Analysis & Tshark & Libpcap
* Docker
* Database
* Web Development Skills
* Honeypot and Deception knowledge

##### Mentors
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [SRI HARSHA Gajavalli](mailto:sriharsha.g@owasp.org)

----

### [Zed Attack Proxy (ZAP)](https://www.zaproxy.org)

#### Idea One: GraphQL Support

ZAP does not currently detect [GraphQL weaknesses](https://github.com/zaproxy/zaproxy/issues/5153) such as injection, auth problems, or information exposures.

##### Expected Results

* Implement functionality to allow ZAP to inspect and attack given GraphQL endpoints.
* Code that conforms to our Development Rules and Guidelines

##### Getting Started

* Have a look at the ZAP [CONTRIBUTING](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) guideline, especially the 'Coding' section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/labels/IdealFirstBug).

##### Mentors
* [Simon Bennetts](mailto:psiinon@gmail.com) and the ZAP core team.

#### Idea Two: SSRF Detection/Handling

ZAP is currently able to detect vulnerabilities with limited local network callback support (such as XXE).
ZAP could benefit from enhanced callback support in the form of a configurable or deployable daemon/listener to facilitate 
more external or public callbacks in order to improve [detection of SSRF](https://github.com/zaproxy/zaproxy/issues/3022) and other related vulnerabilities.

https://ssrfdetector.com/ was an online service for detecting Server Side Request Forgery (SSRF) vulnerabilities.
It was developed and maintained by Jake Reynolds and is open source https://github.com/jacobreynolds/ssrfdetector 
It may be used for inspiration/ideas as well as other projects such as sleepy-puppy (Netflix), etc. 

##### Expected Results

* Create or suggest a suitable alternative to SSRFDetector, and integrate it with ZAP in order to be able to detect SSRF vulnerabilities
* Code that conforms to our Development Rules and Guidelines

##### Getting Started

* Have a look at the ZAP [CONTRIBUTING](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) guideline, especially the 'Coding' section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/labels/IdealFirstBug).

##### Mentors
* [Simon Bennetts](mailto:psiinon@gmail.com) and the ZAP core team.

#### Idea Three: Re-test Functionality

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

#### Idea Four: Your Idea

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

### [OWASP Juice Shop](https://owasp-juice.shop)

OWASP Juice Shop is probably the most modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications!

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP Organization on Google's GSoC page in "Draft Shared" mode. 
- Please pick "juice shop" as Proposal Tag to make them easier to find for us. Thank you!

#### Your idea

##### Brief Explanation:

You have an awesome idea to improve OWASP Juice Shop that is not on this list? Great, please submit it!

##### Getting started
* Get in touch with [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) to discuss your idea

##### Expected Results:
* A new feature that makes OWASP Juice Shop even better
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

##### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Angular and NodeJS/Express, some security knowledge would be preferable.

##### Mentors:
* [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) - OWASP Juice Shop Project Leader

----

### [OWASP Security Knowledge Framework](https://github.com/zdresearch/OWASP-Honeypot)

##### Explanation of Ideas

OWASP-SKF is an open source security knowledgebase including manageble projects with checklists (ASVS / MASVS) and best practice code examples in multiple programming languages showing you how to prevent hackers gaining access and running exploits on your application. Develop your projects secure by design from the start using SKF.

In a nutshell
* Training your developers in writing secure code
* Security by design, early feedback of possible security issues
* Code examples for secure coding guidance
* Knowledge base items for deeper understanding of the security controls
* Security labs to improve your verification skills
* Machine learning chatbot for easy support

##### Expected Results

* New Angular (7/8) GUI for the SKF project. We have this style and GUI for some years now and it could use a major revamp.
* * Create a new style / design for the SKF project
* * We want to keep the color schema that we currently have
* * Create new styles for the different pages and functionality we have in SKF
* * Make it also mobile friendly
* Test cases for the new created Angular application.
* * We believe strongly in automation and testing of the quality of our project, we want to have at least 90% coverage of automated testing for the new Angular frond-end application of SKF


##### Getting Started

Have a look at our GitHub [wiki page](https://github.com/blabla1337/skf-flask), run the SKF project and have a look at the Angular interface and the functionality. If you have questions or want to contact us please join us on Slack or Gitter:
[![Join the chat at https://gitter.im/Security-Knowledge-Framework/Lobby](https://badges.gitter.im/Security-Knowledge-Framework/Lobby.svg)](https://gitter.im/Security-Knowledge-Framework/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Join the chat at https://owasp.slack.com/messages/C0F7L9X6V](https://img.shields.io/badge/chat-on%20slack-blueviolet)](https://owasp.slack.com/messages/C0F7L9X6V)

##### Students Requirements

* Python 3.x
* Angular 7/8
* Web Development Skills
* Docker

##### Mentors
* [Glenn ten Cate](mailto:glenn.ten.cate@owasp.org)
* [Riccardo ten Cate](mailto:riccardo.ten.cate@owasp.org)

<hr>

### [OWASP SAMM](https://github.com/OWASP/SAMM)

##### Explanation of Ideas

The mission of OWASP Software Assurance Maturity Model (SAMM) is to be the prime maturity model for software assurance that provides an effective and measurable way for all types of organizations to analyze and improve their software security posture. OWASP SAMM supports the complete software lifecycle, including development and acquisition, and is technology and process agnostic. It is intentionally built to be evolutive and risk-driven in nature.

More details are available on https://owaspsamm.org/

##### Expected Results

* OWASP benchmark coding
* An API to consume the data model 
* An on-line evaluation tool for SAMM assessments
* In the SAMM model, link all related OWASP projects
* Add mappings to various standards (ASVS, NIST, PCI, ...)


##### Getting Started

Have a look at our GitHub [wiki page](https://github.com/OWASP/SAMM), and OWASP SAMM on https://owaspsamm.org/

##### Students Requirements

* Web Development Skills
* Docker
* Interest in secure coding practices

##### Mentors
* [Seba Deleersnyder](mailto:seba@owasp.org)
* [Bart De Win](mailto:bart.de.win@owasp.org)

<hr>

### OWASP Honeypot Project

The goal of the OWASP Honeypot Project is to identify emerging attacks against web applications and report them to the community, in order to facilitate protection against such targeted attacks. The main challenge of this project is to facilitate the deployment of a HoneyPot by embedding the generation of HoneyTokens into web applications, especially with the most used CMS (like Wordpress, Joomla and Drupal).

##### Expected results
- Design HoneyTokens for Web applications
- Develop a mechanism to implant HoneyTokens in web application based on modsecurity and CRS3 (https://github.com/OWASP/Honeypot-Project/issues/3)
- Generate threat intelligence data (based on attacker interactions and honey tokens modifications) and integrate this with MISP
- Use case: integrate HoneyTokens using at least one of the most used CMS (Wordpress, Joomla or Drupal) (https://github.com/OWASP/Honeypot-Project/issues/9)
- Automate the deployment of both VM and Docker based honeypots into AWS

##### Getting started
- Have a look at the [GitHub project](https://github.com/OWASP/Honeypot-Project) and  [wiki page](https://github.com/OWASP/Honeypot-Project/wiki).
- Join OWASP Slack and contact us on channel #honeypot-project

##### Student Requirements
- PHP
- Python
- Honeypots and HoneyTokens
- ModSecurity and OWASP CRS v3
- HTTP Protocol
- AWS Account

##### Mentor
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)
* [Adrian Winckles](mailto:Adrian.Winckles@owasp.org)

<hr>

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).

##### Expected results
- Add support for other linux variants
- Improve features (IDS,Firewall)
- Complete the web GUI and remote monitoring
- Zero bugs - Fix the current identifed bugs
- Improve Detecting Website Defacements Based on Machine Learning Techniques and Attack Signatures

##### Getting started
- Check[GitHub project](https://github.com/OWASP/SecureTea-Project) and [Website](https://owasp.org/www-project-securetea/).
- Join OWASP Slack and contact us on channel #project-securetea

##### Student Requirements
- Python
- Angular

##### Mentor
* [Rejah Rehim](mailto:rejah.rehim@owasp.org)
* [Ade Yoseman](mailto:edikdoank@gmail.com)

<hr>

### [OWASP Risk Assessment Framework](https://github.com/OWASP/RiskAssessmentFramework)

##### Explanation of Ideas

The OWASP Risk Assessment Framework consist of Static application security testing and Risk Assessment tools. By using OWASP Risk Assessment Framework's Static Appilication Security Testing tool Testers will be able to analyse and review their code quality and vulnerabilities without any additional setup. OWASP Risk Assessment Framework can be integrated in the DevSecOps toolchain to help developers to write and produce secure code.

##### Expected Results
* A new features make this project will be better 
* Make some improvement in scanner for Source Code Analysis
* Add another tool other than sonarqube (Integrate other tools to Raf)
* Make some generate report into pdf, excel, word etc
* put the OWASP RAF into cloud so it's accessible
* Make our tool support few other languages as well
* work in docker so our tools can install by docker

#### 1st Idea
* add other tools features like IAST, RASP etc

#### 2nd Idea
* please see my Expected Results 

#### 3rd Idea
submit you idea!

##### Students Requirements
* Python 3.x
* Angular 7/8
* Typescript
* Web Development Skills
* Docker
* Java
* Mongodb

##### Getting started:
* good knowledge about secure coding and other tools https://owasp.org/www-community/Source_Code_Analysis_Tools
* contact mentor for discuss your ideas with [Ade Yoseman Putra](mailto:ade.putra@owasp.org)

##### Mentors:
* [Ade Yoseman Putra](mailto:ade.putra@owasp.org) - OWASP Risk Assessment Framework Project Leader
* [Azzeddine RAMRAMI](mailto:azzeddine.ramrami@owasp.org) - OWASP Risk Assessment Framework Project Leader


<hr>

### [OWASP Nettacker](https://github.com/zdresearch/OWASP-Nettacker)

##### Explanation of Ideas

OWASP Nettacker is an open source software in Python language which lets you automated penetration testing and automated Information Gathering. This software can be run on Windows/Linux/OSX under Python.

##### Getting started

* You may read the available documents in the [wiki page](https://github.com/zdresearch/OWASP-Nettacker/wiki). Developers and users documents are separated.

#### Expected Results

* The expected results are to contribute the OWASP Nettacker framework [issues](https://github.com/zdresearch/OWASP-Nettacker/issues) (mostly help wanted or enhancement). Please check the GitHub repo to learn more.
* The framework does not have good code base, it needs to fix and clean up.

#### Knowledge Prerequisites

* The whole framework was written in Python language. You must be familiar with Python 2.x, 3.x.
* Good knowledge of computer security (and penetration testing)
* Knowledge of OS (Linux, Windows, Mac...) and Services
* Familiar with IDS/IPS/Firewalls and ...
* To develop the API you should be familiar with HTTP, Database...

##### Mentors
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [Sam Stepanyan](mailto:sam.stepanyan@owasp.org)


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

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

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

#### OWASP OWTF - MiTM proxy interception and replay capabilities
##### Brief Explanation:

The OWTF man-in-the-middle proxy is written completely in Python (based on the excellent Tornado framework) and was benchmarked to be the fastest MiTM python proxy. However it lacks the useful and much need interception and replay capabilities of [mitmproxy](https://github.com/mitmproxy/mitmproxy).

The current implementation of the MiTM proxy serves its purpose very well. Its fast but its not extensible. There are a number of good use cases for being extensible
- ability to intercept the transactions
- modify or replay transaction on the fly
- add additional capabilities to the proxy (such as session marking/changing) without polluting the main proxy code

Bonus:
- Design and implement a proxy plugin (middleware) architecture so that the plugins can be defined separately and the user can choose what plugins to include dynamically (from the web interface).
- Replace the current Requester (based on urllib, urllib2) with a more robust Requester based on the new urllib3 with support for a real headless browser factory. The typical flow when requested for an authenticated browser instance (using PhantomJS)

- The "Requester" module checks if there is any login parameters provided (i.e form-based or script - look at the [login-sessions-plugin]( https://github.com/owtf/login-sessions-plugin) )
- Create a browser instance and do the necessary login procedure
- Handle the browser for the URI
- When called to close the browser, do a clean logout and kill the browser instance.

##### Expected results:

- IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
- IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
- IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
- CRITICAL: Excellent reliability
- Good performance
- Unit tests / Functional tests
- Good documentation

#### Getting Started:
- Have a look at the GitHub project and wiki page, get familiar with the codebase.
- Join OWASP Slack and contact us on channel #project-owtf.
- Submit PRs for the issues listed on our github page.

##### Knowledge Prerequisite:

- Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

##### OWASP OWTF Mentors:
* [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
* Viyat Bhalodia
* Bharadwaj Machiraju 
OWASP OWTF Project Leaders

#### OWASP OWTF - Web interface enhancements

##### Brief Explanation:

The current owtf web interface is implemented in ReactJs with Redux as the state manager. The project involves integration of Typescript in the code to ease the refactoring process. Complete implementation of the Login Page (APIs + frontend) with additional unit/functional tests will also be a deliverable for this project. Check out the current implementation of the web interface at [OWTF on GitHub](https://github.com/owtf/owtf/tree/develop).

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

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
* Bharadwaj Machiraju
* [Mohit Sharma](mailto:ms892075@gmail.com)

#### OWASP OWTF - New plugin architecture

##### Brief Explanation:

The current plugin system is not very useful and it is painful to browse many plugins. Most of the plugins do have much code and most of is repeated - much refactoring needed there.

This issue is documented in detail at [905](https://github.com/owtf/owtf/issues/905).

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

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
* Bharadwaj Machiraju 
OWASP OWTF Project Leaders

#### OWASP OWTF - General Improvements

##### Brief Explanation:

There are many small but important enhancements in the issue tracker which are too small to make a single project, but they can be grouped together to make a suitable GSoC project.
The aim of the project is to implement some of the enhancements suggested in the issue tracker to improve user experience (adding new useful features and making the owtf tool easier to use), security and performance.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

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
* Bharadwaj Machiraju 
* [Mohit Sharma](mailto:ms892075@gmail.com)
----

### [OWASP Bug Logging Tool](https://github.com/OWASP/BLT)

##### Brief Explanation:

BLT lets anyone report issues they find on the internet. Found something out of place on Amazon.com ? Let them know. Companies are held accountable and shows their response time and history. Get points for reporting bugs and help keep the internet bug free.

Check OWASP WIKI PAGE https://www.owasp.org/index.php/OWASP_Bug_Logging_Tool for some reference;

##### Getting started
* Get in touch with [Sourav Badami](mailto:sourav.badami@owasp.org) to discuss your idea.

##### Expected Results:
* A fully functional and out of the box toolkit for bug hunting and crowd sourcing hunters with bounty support on top of the existing platform.
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

##### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) ReactJS, Python, Django some security knowledge would be preferable.

##### Mentors:
* [Sourav Badami](mailto:sourav.badami@owasp.org) - OWASP Bug Logging Tool Project Leader
* [Sean Auriti](mailto:sean.auritii@owasp.org) - OWASP Bug Logging Tool Project Leader

----
