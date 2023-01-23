---
layout: full-width
title: GSoC 2023 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2023ideas
---

# {{page.title}}

[ZAP](#owaspzap) | [Bug Logging Tool (BLT)](#bug-logging-tool-blt) | [Maryam](#owaspmaryam) | [SecureTea](#project-securetea) | [PyGoat](#project-pygoat) | [RiskAssessmentFramework](#risk-assessment) | [Juice Shop](#owaspjuiceshop)

<!-- Template: Use a format like below to add your project, don't forget to add it to the anchor links above:
### [Project Name]

##### Explanation of Ideas

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Expected Results

##### Getting Started

##### Mentors
-->

Tips to get you started in no particular order:

- Read the
  [Student Guidelines](gsoc2023).
- Check our
  [GitHub organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [OWASP ZAP](https://zaproxy.org/)

ZAP is the world’s most widely used web scanner. Previous GSoC contributors have added key features and are all listed in the [ZAP Student Hall of Fame](https://www.zaproxy.org/student-hall-of-fame/).

To get started with ZAP contributions see the [ZAP Contributing Guide](https://www.zaproxy.org/docs/contribute/). We expect GSoC contributors who apply to work on ZAP to have had at least one code PR merged into one of the ZAP repos.

##### Import PCAP/PCAPNG Files

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

Import PCAP/PCAPNG Files into ZAP as per [#4812](https://github.com/zaproxy/zaproxy/issues/4812)

##### Browser Recorder

![Not recommended for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Create a new browser extension using Type Script which will allow the user to record and replay browser interactions, for example during authentication as per [#7139](https://github.com/zaproxy/zaproxy/issues/7139)

##### Your Own Idea

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

We are always delighted to hear from contributors who have their own ideas for projects. You are encouraged to discuss these with the ZAP project leaders.

##### Mentors

All ZAP projects will be mentored by the ZAP Project Leaders:

- [Simon Bennetts](mailto:psiinon@gmail.com)
- Rick Mitchell
- thc202

### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Possible for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow>)

##### Explanation of Ideas

- Crypto - create a proof of stake coin called BUG
- Flutter - ideas to improve the app? Launch it on the App Store.
- Django - Website integration of new design
- Private issue reporting - allow companies to switch on private issue reporting.
- Payments for issues reported - allow companies or individuals to pay big hunters
- Browser plug-in to check bug reports - scan each site visited against a database to see if any bugs were found - we have a plug-in for chrome, let’s update it.
- Allow for the detection of banned apps in different countries. How would the internet look like if I was in country x.
- Allow for customers to track their online presence and help take down links where they did not approve their personal info on.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

##### Getting Started

- [BLT Core](https://github.com/owasp/blt/)
- [Flutter App](https://github.com/Bugheist/Flutter/)

#### Expected Results

- Proof of stake coin on the testnet and mainnet.
- Release Flutter app on App Store and Play Store.
- Implementation of private issues reporting.
- Update of browser plugins to support showing bugs on relative sites in a secure way
- Ability to choose a country from a selected list and see what apps are banned there
- Ability for users to report links online with personal information where they can have it removed

Reach out to us on Slack to discuss further on the scope, changes required, or if you have any other proposal.

- Please submit your proposal on the BLT GitHub discussion board. Because it will be easier for the team to review and give feedback there.
- Team meetings are every Saturday at 1pm EST. Check Slack for the google meet link.

#### Knowledge Prerequisites

- Python / Django for Backend
- Flutter for Mobile
- Blockchain / Bitcoin clone for the coin

##### Mentors

- Donnie on slack (lead mentor)
- [Sourav Badami](mailto:sourav.badami@owasp.org) - Django Mentor
- Rahul Badami - Payments Mentor
- [Ankit Choudhary](mailto:ankitchoudhary202.ac@gmail.com) - Flutter Mentor
- [Sparsh Agrawal](mailto:sparshagrawal1212@gmail.com) - Flutter Mentor

### [OWASP Maryam](https://owasp.org/www-project-maryam/)

OWASP Maryam is a modular/optional open source framework based on OSINT and data gathering. Maryam is written in Python programming language and it’s designed to provide a powerful environment to harvest data from open sources and search engines and collect data quickly and thoroughly.

Please see [Development Guide](https://github.com/saeeddhqan/maryam/wiki/Development-Guide).

##### Web interface for meta searcher

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

Implement a web interface for Iris module with JQuery. The interface is somehow like www.qwant.com.

##### Document Retrieval for Iris

![Not recommended for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Implement a Document Retrieval Algorithm for Iris in order to rank web pages according to the Query.
You need to Understand Machine Learning classic algorithms for document retrieval or use Deep neural networks for
implementation.

##### Your Own Idea

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

If you have a new Idea regarding Iris(Meta searcher), let us chat.

##### Getting Started

- [OWASP Maryam](https://github.com/saeeddhqan/Maryam)
- [Documentation](https://github.com/saeeddhqan/Maryam/wiki)

##### Mentors

- [Saeed Dehqan](mailto:saeed.dehghan@owasp.org)

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).
![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

##### Expected results

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

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

- [Rejah Rehim](mailto:rejah.rehim@owasp.org)
- [Ade Yoseman](mailto:edikdoank@gmail.com)

### [OWASP PyGoat](https://owasp.org/www-project-pygoat/)

Intentionally vuln web Application Security in django.

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

##### Expected results

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

- Improve Vulnerabilities based on OWASP Top 10 - 2021
- Fixing all issues and work with Docker

##### Getting started

- Check[GitHub project](https://github.com/adeyosemanputra/pygoat) and [Website](https://owasp.org/www-project-pygoat/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-pygoat

##### Student Requirements

- Python
- Django

##### Mentor

- [Ade Yoseman](mailto:edikdoank@gmail.com)
- Rupak

### [OWASP Risk Assessment Framework](https://owasp.org/www-project-risk-assessment-framework/)

The OWASP Risk Assessment Framework consist of Dynamic application security testing (DAST) and Risk Assessment tools. By using OWASP Risk Assessment Framework's Testers will be able to analyse and review their application and vulnerabilities without any additional setup. OWASP Risk Assessment Framework can be integrated in the DevSecOps toolchain to help developers to write and produce secure application.

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

##### Expected results

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

- Building API Scanner
- Add Vulnerabilities based on OWASP Top 10 - 2021 & CVE Mitre
- Fixing all issues and work with Docker
- Integrated to other pentest tool like brute force, ossint tool etc

##### Getting started

- Check[GitHub project](https://github.com/Risk-Assessment-Framework) and [Website](https://owasp.org/www-project-risk-assessment-framework/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #risk-assessment

##### Student Requirements

- Python
- Flask
- React

##### Mentor

- [Ade Yoseman](mailto:edikdoank@gmail.com)
- [Andriansyah](mailto:pakdesawangan@gmail.com)

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

###### Score Board UI/UX

![Possible for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

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

###### Companion Guide Tech Stack

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Not recommended for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red>)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

The official companion guide eBook ["Pwning OWASP Juice Shop"](https://pwning.owasp-juice.shop) is today written in Markdown
and compiled with the GitBook legacy CLI into HTML (for [online reading](https://pwning.owasp-juice.shop)) as well as EPUB/PDF (for the [free eBook on LeanPub](https://leanpub.com/juice-shop/)). As GitBook CLI is no longer maintained, it is only a question of time when the current build and publishing pipeline will
start failing from outdated tooling in general and specifically unsupported old versions of Node.js etc. The CI/CD pipeline for publishing
is currently running [on AppVeyor](https://ci.appveyor.com/project/bkimminich/pwning-juice-shop) whereas all other Juice Shop components are built with GitHub Actions.

With well over 12,000 readers on LeanPub alone, the eBook is definitely a cornerstone of Juice Shop's success, so it should receive a long-overdue
renewal of its technbology stack. This includes a modern and future-proof authoring format (that still supports both online-reading and eBook export) as well
as moving the CI/CD pipeline over to GitHub.

###### Your own idea

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Preferred for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-preferred-green>)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

You have an awesome idea to improve OWASP Juice Shop that is not on this
list? Great, please submit it!

##### Expected Results

- A new feature or improvement of an existing one that makes OWASP Juice
  Shop even better
- Your code follows our existing styleguides and passes all existing
  quality gates regarding code smells, test coverage etc.
- Code that you write comes with automated tests that fit into
  [our available test suites](https://pwning.owasp-juice.shop/part3/contribution.html#testing).

##### Getting started

- Make sure your JavaScript/TypeScript is sufficient to work on the
  Juice Shop codebase. Check our
  [Codebase 101](https://pwning.owasp-juice.shop/part3/codebase.html)
  here. Students with some experience with (or willingness to learn)
  Angular and NodeJS/Express are usually prefered.
- Read our
  [Contribution Guidelines](https://pwning.owasp-juice.shop/part3/contribution.html)
  very carefully. Best make some small contributions before GSoC, so we
  can see how you work and help you dive into the code even better.
- Get in touch with
  [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) to discuss any
  of the listed or your own idea for GSoC!

##### Mentors

- [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) - OWASP Juice
  Shop Project Leader

### [WrongSecrets](https://owasp.org/www-project-wrongsecrets/)

![Preferred for "Medium" GSoC 2023 project](<https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green>)
![Possible for "Large" GSoC 2023 project](<https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow>)

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

aaa
