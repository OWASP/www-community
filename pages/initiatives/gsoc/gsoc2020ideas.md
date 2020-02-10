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

### [OWASP Juice Shop](https://owasp-juice.shop)

OWASP Juice Shop is probably the most modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications!

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP Organization on Google's GSoC page in "Draft Shared" mode. 
- Please pick "juice shop" as Proposal Tag to make them easier to find for us. Thank you!

#### Challenge Pack 2020

##### Brief Explanation:

Ideas for potential new hacking challenges are collected in [GitHub issues labeled "challenge"](https://github.com/bkimminich/juice-shop/issues?q=is%3Aissue+is%3Aopen+label%3Achallenge). This project could implement a whole bunch of challenges one by one and release them over the course of several small releases. This would allow the student to work in a professional Continuous Delivery kind of way while bringing benefit to the Juice Shop over the duration of the project. Especially the added functionality from [GSoC Feature Pack 2019](https://agrawalarpit14.github.io/GSoC/) is still mostly void of challenges and offers a lot of interesting attack surface in the whole order and payment process.

Coming up with good additional ideas for challenges in the proposal could make the difference between being selected or declined as a student for this project!

##### Expected Results:
* 10 or more new challenges for OWASP Juice Shop (including required functional enhancements to place the challenges)
* Each challenge comes with full functional unit and integration tests
* Each challenge is verified to be exploitable by corresponding end-to-end tests
* Hint and solution sections for each new challenge are added to the "Pwning OWASP Juice Shop" ebook
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

##### Getting started:
* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

##### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Angular and NodeJS/Express, some security knowledge would be preferable.

##### Potential Mentors:
* [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) - OWASP Juice Shop Project Leader

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

##### Getting started
- Have a look at the [GitHub project](https://github.com/OWASP/Honeypot-Project) and  [wiki page](https://github.com/OWASP/Honeypot-Project/wiki).
- Join OWASP Slack and contact us on channel #honeypot-project

##### Student Requirements
- PHP
- Python
- Honeypots and HoneyTokens
- ModSecurity and OWASP CRS v3
- HTTP Protocol

##### Mentor
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

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
* [SRI HARSHA Gajavalli](mailto:sriharsha.g@owasp.org)
----
