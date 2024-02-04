---
layout: full-width
title: GSoC 2024 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2024ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull; [Maryam](#owaspmaryam) &bull; [SecureTea](#owasp-securetea) &bull; [PyGoat](#owasp-pygoat) &bull; [RiskAssessmentFramework](#owasp-risk-assessment-framework) &bull; [Juice Shop](#owaspjuiceshop) &bull; [OWASP WrongSecrets](#owasp-wrongsecrets) &bull; [OWASP DevSecOps Maturity Model](#owaspdevsecops-maturity-model) &bull; [OWASP secureCodeBox](#owasp-securecodebox) &bull; [OWASP ModSecurity Core Rule Set](#owasp-modsecurity-core-rule-set) &bull; [OWASP Nettacker](#owasp-nettacker) &bull; [OWASP Threat Dragon](#owasp-threat-dragon)


<!-- Template: Use a format like below to add your project, don't forget to add it to the anchor links above:
### [Project Name]

##### Explanation of Ideas

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Expected Results

##### Getting Started

##### Mentors
-->

Tips to get you started in no particular order:
- Read the
  [Student Guidelines](gsoc2024).
- Check our
  [GitHub organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

OWASP BLT is a _bug-hunting & logging_ tool which allows users and companies to hunt for bugs, claim bug bounties and also to start bug-hunting sprees/contests respectively. It is preferred if the potential GSoC contributors get at least 5 PRs merged for the project. Preference will be given to students
who get the most work done, and this is usually by submitting the most PRs.

##### 2024 GSOC Ideas / Projects

We have over 40 projects available in 5 repositories to work on!

[View them all here](https://github.com/orgs/OWASP/projects/3) or individually:

| Repository | Description | Projects Link
|---------|------------|------------|
| [OWASP/BLT](https://github.com/OWASP/BLT/) | The Django backend core project | [View Projects](https://github.com/OWASP/BLT/labels/project) 
| [OWASP/BLT-Flutter](https://github.com/OWASP/BLT-Flutter/) |  The BLT Flutter APP (app store) | [View Projects](https://github.com/OWASP/BLT-Flutter/labels/project) 
| [OWASP/BLT-Bacon](https://github.com/OWASP/BLT-Bacon/) |  Coin that rewards bug hunters | [View Projects](https://github.com/OWASP/BLT-Bacon/labels/project)
| [OWASP/BLT-Extension](https://github.com/OWASP/BLT-Extension/) |  BLT Chrome Extension | [View Projects](https://github.com/OWASP/BLT-Extension/labels/project) 
| [OWASP/BLT-Action](https://github.com/OWASP/BLT-Action/) |  BLT Github Action | [View Projects](https://github.com/OWASP/BLT-Action/labels/project) 


#### Expected Results

* We would expect that any projects you choose to include in your proposal are fully completed.

Reach out to us on Slack to discuss further on the scope, changes required, _or if you have any other proposal._
* Please submit your proposal on the [BLT GitHub discussion board](https://github.com/OWASP/BLT/discussions) in markdown language before you convert it to a PDF.  Because it will be easier for the team to review and give feedback there.
* Team meetings are every Saturday at 12pm EST on [Slack - Join here](https://owasp.slack.com/archives/C2FF0UVHU)

#### Knowledge Prerequisites

* Python / Django for Backend
* Flutter for Mobile app
* Blockchain development
* Some knowledge of UI designing for design related ideas.

##### Mentors
* Donnie on slack (lead mentor)
* We are looking for mentors, reach out to us on slack

### [OWASP Maryam](https://owasp.org/www-project-maryam/)

OWASP Maryam is a modular/optional open source framework based on OSINT and data gathering. Maryam is written in Python programming language and it’s designed to provide a powerful environment to harvest data from open sources and search engines and collect data quickly and thoroughly.

Please see [Development Guide](https://github.com/saeeddhqan/maryam/wiki/Development-Guide).

##### Web interface for meta searcher

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

Implement a web interface for Iris module with JQuery. The interface is somehow like www.qwant.com.


##### Document Retrieval for Iris

![Not recommended for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Implement a Document Retrieval Algorithm for Iris in order to rank web pages according to the Query.
You need to Understand Machine Learning classic algorithms for document retrieval or use Deep neural networks for 
implementation.

##### Your Own Idea

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

If you have a new Idea regarding Iris(Meta searcher), let us chat.

##### Getting Started

* [OWASP Maryam](https://github.com/saeeddhqan/Maryam)
* [Documentation](https://github.com/saeeddhqan/Maryam/wiki)

##### Mentors

* [Saeed Dehqan](mailto:saeed.dehghan@owasp.org)

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).
![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
##### Expected results
![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
- Improve Web Application Firewall GUI based on AI 
- Improve all SecureTea features (IDS,Firewall)
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
* [Ardi](mailto:pakdesawangan@gmail.com)
* [Ade Yoseman](mailto:edikdoank@gmail.com)

### [OWASP PyGoat](https://owasp.org/www-project-pygoat/)
Intentionally vuln web Application Security in django.

![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

##### Expected results

![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

- Improve Vulnerability Challenges
- Improve Secure Coding Lab
- Build AI Chatbox
- Fixing all issues and work with Docker


##### Getting started
- Check[GitHub project](https://github.com/adeyosemanputra/pygoat) and [Website](https://owasp.org/www-project-pygoat/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-pygoat

##### Student Requirements
- Python
- Django
- NLP 

##### Mentor
* [Ade Yoseman](mailto:edikdoank@gmail.com)
* Nizam

### [OWASP Risk Assessment Framework](https://owasp.org/www-project-risk-assessment-framework/)
The OWASP Risk Assessment Framework consist of Dynamic application security testing (DAST) and Risk Assessment tools. By using OWASP Risk Assessment Framework's  Testers will be able to analyse and review their application and vulnerabilities without any additional setup. OWASP Risk Assessment Framework can be integrated in the DevSecOps toolchain to help developers to write and produce secure application.

![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

##### Expected results

![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
- Building API Scanner and Integrated other scanners
- Add Vulnerabilities based on OWASP Top 10 - 2021, CVE Mitre, SANS 25 Top error also ISO 27k
- Integrated to other pentest tool
- Scheduled scan

##### Getting started
- Check[GitHub project](https://github.com/Risk-Assessment-Framework) and [Website](https://owasp.org/www-project-risk-assessment-framework/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #risk-assessment

##### Student Requirements
- Python
- Flask
- React

##### Mentor
* [Ade Yoseman](mailto:edikdoank@gmail.com)
* [Ardi](mailto:pakdesawangan@gmail.com)

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

###### Your own idea

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

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
* [Shubham Palriwala](mailto:spalriwalau@gmail.com) - OWASP Juice Shop Core Team
* [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) - OWASP Juice Shop Core Team

### [OWASP WrongSecrets](https://owasp.org/www-project-wrongsecrets/)

![Preferred for "Medium" GSoC 2024 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Possible for "Large" GSoC 2024 project](<https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow>)

##### Explanation of Ideas

- Revise WrongSecrets frontend ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- Port WrongSecrets CTF to Azure ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Port WrongSecrets CTF to GCP ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Create Nomad support ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)
- Improve WrongSecrets CTF helm chart and release process ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

##### Getting Started

Repositories:

- [WrongSecrets](https://github.com/owasp/wrongsecrets)
- [WrongSecrets CTF](https://github.com/owasp/wrongsecrets-ctf-party)

Please use the repositories' issue tracker, GitHub discussions, and don't forget to read the [contributing guide](https://github.com/OWASP/wrongsecrets/blob/master/CONTRIBUTING.md).

#### Expected Results

Depending on the project:

- A revised WrongSecrets frontend
- Azure CTF support
- GCP CTF support
- WrongSecrets Nomad support
- A helm chart that's up to industry standards with an appropriate release pipeline

Reach out to us on Slack to discuss these and other ideas!

- Please submit your proposal on the WrongSecrets GitHub discussion board or issue tracker to make it easier for the team to review and give feedback.
- Team meetings are every friday 8.30 CET. Invite will be shared once GSoC application is approved.

#### Knowledge Prerequisites

- Terraform for infra as code
- Java for application
- Java/HTML/JavaScript/CSS for application frontend
- Kubernetes/helm for backend
- Azure (if extending Azure support)
- GCP (if extending GCP support)
- Nomad for backend (if building Nomad support)

##### Mentors

- [Ben de Haan](mailto:ben.dehaan@owasp.org)

### [OWASP DevSecOps Maturity Model](https://dsomm.owasp.org)

The OWASP DevSecOps Maturity Model provides opportunities to harden DevOps strategies and shows how these can be prioritized.
It contains of an application and the model data.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "dsomm" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Medium Feature Pack for the Application
![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

- [Comprehensive activity view](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/192) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- [Team-based asessment](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/211) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- [Enhancement of diagram](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/183) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- Your idea

##### Large Feature Pack for the Application
![Possible for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

- [Comprehensive activity view](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/192) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- [Team-based asessment](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/211) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- [Enhancement of diagram](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/183) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-easy-green)
- [Adding of graph support](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/210) ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)
- [Adding of tags](https://github.com/wurstbrot/DevSecOps-MaturityModel/issues/212) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Your idea

#### Prerequisites
- Angular for application
- Open Source contributions to Open Source projects

##### Mentors
Reach out to us on Slack to discuss these and other ideas!

- [Timo Pagel](mailto:timo.pagel@owasp.org)

### [OWASP OWTF](https://owasp.org/www-project-owtf/)

![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Explanation of Ideas

- Refactor and complete the web interface ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Update plugins to new recon, discovery and attack tools ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Design & implement deployment architecture ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Getting Started

Repositories:

- [OWTF](https://github.com/owtf/owtf)
- [OWTF Docker](https://github.com/owtf/owtf-docker)
- [OWTF Python client](https://github.com/owtf/owtf-python-client)

Please use the repositories' issue tracker, GitHub discussions, and don't forget to read the [contributing guide](https://github.com/owtf/owtf/blob/master/CONTRIBUTING.md). Join the community at #owtf on OWASP [Slack](https://owasp.slack.com/) and share your questions, project ideas.

#### Knowledge Prerequisites

- Terraform for infra as code
- Python for application
- React/React ecosystem for application frontend
- Kubernetes/helm for infrastructure deployment
- Basic knowledge of application security, tools used in bug bounty style hunting

##### Mentors

- [Viyat Bhalodia](mailto:viyat.bhalodia@owasp.org)
- [Abraham Aranguran](mailto:Abraham.Aranguren@owasp.org)

### [OWASP secureCodeBox](https://www.securecodebox.io)

secureCodeBox is a kubernetes based, modularized toolchain for continuous security scans of your software project.
The secureCodeBox comes with many different scanners officially integrated (from Amass to Zap) and integration 
with vulnerability management backends like DefectDojo.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "securecodebox" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Explanation of Ideas

###### Rewrite DefectDojo Hook in Go(lang)

![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-yellow)

The current implementation of our [DefectDojo hook](https://github.com/secureCodeBox/secureCodeBox/tree/main/hooks/persistence-defectdojo) is written in Java.
As the remainder of the project is written in Go & JavaScript the code does not fit into the remainder of the project and suffers from typical Java problems 
like a comparatively large memory footprint and slow boot times.

The goals of the project are:

- moving the implementation to a modern Go implementation
- extracting the DefectDojo api calls to reusable golang library
- expanding end-to-end testability of the hook with a real DefectDojo instance in the CI pipeline

###### Add a secureCodeBox CLI (scbctl)

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-yellow)

The primary interface to interact with the secureCodeBox is through it's Custom Resources (CRs) in the Kubernetes API.
Writing the resource (e.g. [Scans](https://www.securecodebox.io/docs/scanners/amass#examplecom)) is generally not hard but can be cumbersome as the require the creation of a new file / multi line string in the command line.

To make these interactions easier to use and more fun, a custom (but optional) secureCodeBox CLI should help by automatically connecting to the Kubernetes API.

- create a new command line client which connects to the Kubernetes API and interacts with the CRs of the secureCodeBox
- write tests & including integration / e2e test and the CI pipeline (GitHub Actions)

More context & information are listed in the [GitHub Issue](https://github.com/secureCodeBox/secureCodeBox/issues/189)

###### Your own idea

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

You have an awesome idea to improve the OWASP secureCodeBox?
We'd love to hear it, please reach out via email / owasp slack / github to ensure that the idea fits into the project. :)

##### Getting started

* Make yourself familiar with the project by going through our HowTo guides which will guide you through different parts of the secureCodeBox.
* Make sure that you have a solid golang knowledge to be able to complete the two proposed project.
* Get in touch with
  [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) to discuss any
  of the listed or your own idea for GSoC!

##### Mentors

* [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) - OWASP secureCodeBox Core Team
* [Robert Felber](mailto:robert.seedorff@owasp.org) - OWASP secureCodeBox Project Lead

### [OWASP ModSecurity Core Rule Set](https://coreruleset.org)

The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

#### Getting Started

* Familiarize yourself with the project and its [basics](https://coreruleset.org/docs). Make sure you understand core concepts such as anomaly scoring, paranoia levels and false positives.
* Check out the [CRS Sandbox](https://coreruleset.org/docs/development/sandbox/)
* Check out the separate CRS GSoC [wiki page](https://github.com/coreruleset/coreruleset/wiki/Google-Summer-of-Code-2024)
* Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #coreruleset

#### CRS 💡 #1

![Preferred for "Medium" GSoC 2032 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

#### CRS Transformations review

##### Summary

Systematic review of transformations, develop a guideline how to transform which parameters and in which order, implement the necessary changes

##### Description

This is one for the nerds, or for somebody who is not afraid to dig into the hairy details of language encodings and their implementation. The ModSecurity SecLang rule language that CRS uses comes with a few dozen of transformation that can help to simplify payloads that make it easier to detect attacks. Think of removing white space or perform base64 decoding. CRS uses this, but we have to admit in an not overly systematic way. So what we would need is somebody who looks at the various options, looks at frequent attacks and tells us which transformations / decodings should be used and in which situation, so we can follow this guideline in a systematic way.

##### Expected Outcomes

- A written guideline on how to transform which parameters
  - include the corresponding attacks if needed
  - and the precise order for all combinations based on the attack
- After discussion and approval, implement the necessary changes in the CRS

##### Skills required/preferred

- Good writing skills
- Basic knowledge about text conversion functions and Web encodings

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

#### CRS 💡 #2

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### SecLanguage platforms performance analysis

##### Summary

Systematic performance analysis on various SecLanguage platforms: Costs of operators, transformations and variables (depending on size of payload / varname+value and number of variables)

##### Description

This is a research project aiming to do a written report about the performance of the essential part of the SecRule language on various implementations, namely ModSecurity 2, libModSecurity 3, Coraza. The ModSecurity Handbook does not really go into enough detail of the performance impact of those constructs that CRS uses as its work horses. So we kind of depend on a gut feeling and a proper base and guideline would be very beneficial.

Without exaggerating too much, you need to keep in mind that CRS is running on millions of servers, some of them with hundreds of millions of requests per day (or more). If you now imagine that we could save some CPU cycles when we optimize the rules, then there is a big, big potential to good. Also to the planet in resource consumption.

##### Expected Outcomes

- Define a framework for testing performance for SecLanguage platforms
- Implement the framework so it can be used for testing 
- Write documentation on usage and techniques used to measure performance for the various constructs

##### Skills required/preferred

- Good writing skills
- Performance testing knowledge
- Basic programming language skills to implement the proposed framework

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

#### CRS 💡 #3

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

#### WAF Performance Testing Framework

##### Summary

Create a performance testing framework i. e. something like regression tests but for performance, so we can see impact on performance of every pull request.

##### Description

A frequent problem when developing new rules is their performance impact. Experience shows you do not really know the performance of a rule until you have tried it out. If you want to test it against a variety of payloads it's quite a lot of manual work and since we do not have a documented test procedure, it's all a bit random.

So the idea is to design a facility (typically a docker container) that is being configured with a rule and then used to test this rule with a variety of payloads and returns a standard report about the performance of the rule. Bonus points if multiple engines are covered (ModSecurity 2, libModSecurity 3, Coraza, ...)

##### Expected Outcomes

- Define a framework for testing performance for a generic WAF
- Implement the framework in a way that can be run in a pipeline for testing changes on configuratios/rules
- Write documentation on usage and techniques used to measure performance

##### Skills required/preferred

- Good writing skills
- Some performance testing knowledge would be useful
- Basic programming language skills to implement the proposed framework

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

#### CRS 💡 #4

![Preferred for "Small" GSoC 2024 project](https://img.shields.io/badge/small%20size%20(~100h)-preferred-green)
![Possible for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)

##### New plugin for &lt;enter-your-cool-idea&gt;

##### Summary

Write new plugins to prevent attacks.

##### Description

We have recently added plugin functionality to CRS. The [Plugin Registry](https://github.com/coreruleset/plugin-registry) has a decent overview of existing plugins and this [blog post](https://coreruleset.org/20220209/introducing-the-fake-bot-plugin/) does a good job describing a very cool plugin for inspiration.

Think about writing another cool plugin to complement the repository.

##### Expected Outcomes

- Expose your need for a new plugin that complements existing work in the CRS
- Create the plugin and document it

##### Skills required/preferred

- Good writing skills
- Knowledge about the problem your are trying to solve with this plugin ;)

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

### [OWASP Nettacker](https://owasp.org/www-project-nettacker/)

OWASP Nettacker is a Modular Automated Penetration Testing/ Information gathering Framework and Vulnerability Scanner fully written in Python. Nettacker can run a variety of scans discovering subdomains, open ports, services, vulnerabilities, misconfigurations, default credentials.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

##### Explanation of Ideas

- create comparison functionality for comparing the current scan with another scan using scanID
- fix scan engine multi-threading/queuing issues
- improve WebUI / add dashboard
- implement SSL/TLS modules to restore the functionality we had in Nettacker v0.0.2
- add DefectDojo integration / output report format
- add SARIF output report format

##### Getting Started

Repositories:

- [OWASP Nettacker on OWASP GitHub](https://github.com/OWASP/Nettacker)
- Join OWASP Slack and contact us on channel [#project-nettacker](https://app.slack.com/client/T04T40NHX/CQZGG24FQ)

##### Knowldege  Requirements

- Python
- Flask
- HTML/CSS/JavaScript
- previous vulnerability scanning/bug bounty hunting experience

##### Mentors

* [Sam Stepanyan](mailto:sam.stepanyan@owasp.org)
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)

### [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)

OWASP Threat Dragon is a modeling tool used to create threat model diagrams as part of a secure development lifecycle.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

##### Explanation of Ideas

The threat engine has some features that have not yet been carried over from version 1.x to the current version 2.x.
These need to be implemented and expanded from what is available in version 1.x;
each idea is probably a GSoC project in its own right:

- add threats by element for STRIDE/LINDDUN/PLOT4ai [issue #792](https://github.com/OWASP/threat-dragon/issues/792)
- add threats using OWASP Automated Threats (OATs) patterns [issue #501](https://github.com/OWASP/threat-dragon/issues/501)
- add descriptions and suggested mitigations for both LINDDUN and PLOT4ai threats
  [issue #797](https://github.com/OWASP/threat-dragon/issues/797)
  and [issue #796](https://github.com/OWASP/threat-dragon/issues/796)

##### Getting Started

- Browse the [documentation](https://owasp.org/www-project-threat-dragon/docs-2/) to see if Threat Dragon is for you
- Join OWASP Slack and contact the Threat Dragon community on channel [#project-threat-dragon](https://app.slack.com/client/T04T40NHX/CURE8PQ68)
- Refer to the Threat Dragon [contributing guidelines](https://github.com/OWASP/threat-dragon/blob/main/contributing.md)

Repositories:

- [OWASP Threat Dragon on OWASP GitHub](https://github.com/OWASP/threat-dragon)

##### Knowldege  Requirements

- JS & git

##### Mentors

* [Jon Gadsden](mailto:jon.gadsden@owasp.org)

