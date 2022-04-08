---
layout: full-width
title: GSoC 2022 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2022ideas
---

# {{page.title}}

[JuiceShop](#owaspjuiceshop) - [ZAP](#owaspzap) - [Maryam](#owasp-maryam) - [DSOMM](#owasp-dsomm) - [SecureTea](#owasp-securetea) - [PyGoat](#owasp-pygoat) - [PurpleTeam](#owasppurpleteam) - [Threat Dragon](#owasp-threat-dragon) - [Coraza Web Application Firewall](#owasp-coraza-web-application-firewall) - [ModSecurity Core Rule Set](#owasp-modsecurity-core-rule-set) - [OWTF](#owasp-owtf) - [Python Honeypot](#owasp-python-honeypot) - [Nettacker](#owasp-nettacker) - [Security Knowledge Framework](#security-knowledge-framework-skf) - [Bug Logging Tool (BLT)](#bug-logging-tool-blt)

<!-- Template: Use a format like below to add your project:
### [Project Name]

##### Explanation of Ideas

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Expected Results

##### Getting Started

##### Mentors
-->

Tips to get you started in no particular order:
- Read the
  [Student Guidelines](gsoc2022).
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

###### Score Board UI/UX

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

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

###### Replacement for Protractor end-to-end test suite

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

> The Angular team plans to end development of Protractor at the end of 2022 (in conjunction with Angular v15).
> 
> _(Source: https://github.com/angular/protractor/issues/5502)_

With the Angular 15 release end of 2022, development support for Protractor will be terminated by the Angular team.
In order to not get stuck on a <15 version of Angular or running into a probably increasing number of issues with Protractor,
it is time for Juice Shop to look into end-to-end testing alternatives. This project would migrate all existing
Protractor tests to a new test framework. The framework choice should follow recommendations of the Angular team in order
to avoid incompatibility issues in the future.

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
* [Timo Pagel](mailto:timo.pagel@owasp.org) - OWASP Juice Shop Core Team

### [OWASP ZAP](https://zaproxy.org/)

ZAP is the world’s most widely used web scanner. Previous GSoC contributors have added key features and are all listed in the [ZAP Student Hall of Fame](https://www.zaproxy.org/student-hall-of-fame/).

To get started with ZAP contributions see the [ZAP Contributing Guide](https://www.zaproxy.org/docs/contribute/). We expect GSoC contributors who apply to work on ZAP to have had at least one code PR merged into one of the ZAP repos.

##### Import PCAP/PCAPNG Files

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

Import PCAP/PCAPNG Files into ZAP as per [#4812](https://github.com/zaproxy/zaproxy/issues/4812)

##### Modern Web App Framework Handling: Angular / VueJS / React

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Enhance ZAP to handle one modern framework better - either Angular, VueJS or React. This project should allow ZAP to extract more information from one of the top JavaScript frameworks and potentisally tune attacks to target known issues with that framework.

##### Browser Recorder

![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Create a new ZAP add-on which will allow the user to record and replay browser interactions, for example during authentication as per [#7139](https://github.com/zaproxy/zaproxy/issues/7139)

##### Param Miner

![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Implement the equivalent on the Burp Pram Miner add-on which identifies hidden, unlinked parameters. It's particularly useful for finding web cache poisoning vulnerabilities as per [#7140](https://github.com/zaproxy/zaproxy/issues/7140)

##### Your Own Idea

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

We are always delighted to hear from contributors who have their own ideas for projects. You are encouraged to discuss these with the ZAP project leaders.

##### Mentors

All ZAP projects will be mentored by the ZAP Project Leaders:

* [Simon Bennetts](mailto:psiinon@gmail.com)
* Rick Mitchell
* thc202

### [OWASP Maryam](https://github.com/saeeddhqan/Maryam)

OWASP Maryam is a modular open-source framework based on OSINT and data gathering. It is designed to provide a robust environment to harvest data from open sources and search engines quickly and thoroughly.

##### Explanation of Ideas

###### Iris

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

Iris currently has been added to Maryam as some basic Natural Language Processing Operations. We want to improve it.
It has a simple document clustering module, a simple meta search engine, and sentiment analysis. What we want to do add
new clustering methods that use neural networks(CNN, RNN, LSTM, ...) in order to create clusters, a topic modeling module to extract
topics from documents, and a model that recognizes the most relevant documents by the given query.

##### Getting Started

* Besides Python, make sure to be familiar with word vectors, neural networks, document retrieval, and NLP models.
* Please read our [wiki page](https://github.com/saeeddhqan/Maryam/wiki), especially the Development Guide. previous PRs would be very helpful.

##### Mentors

* [Saeed Dehqan](mailto:saeed.dehghan@owasp.org) - OWASP Maryam Project Leader

### [OWASP DSOMM](https://github.com/wurstbrot/DevSecOps-MaturityModel)

##### New Application
The OWASP DevSecOps Maturity Model is used to assess and present the devsecops maturity of an organization. It consits of an application and devsecops maturity model information. The application is used to present and assess the model itself. As it is aged, a new modern application with a frontend in angular is to be developed. 
Please also add your own ideas for enhancements in the propsal.
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

* The application should work in the browser only and is created with angular.
* The application should be able to assess multiple teams and present some statistics so that it is easy to get an overview of the maturity of all teams within an organization.
* The application has the current abilities and more 

##### Your Own Idea
You have an awesome idea to improve OWASP DSOMM? Great, please submit it!

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

##### Getting Started
* [Model](https://dsomm.timo-pagel.de/)
It is recommended to add links to existing PRs (also in other open source projects) in your propsal.

##### Mentors

* [Timo Pagel](mailto:timo.pagel@owasp.org) - OWASP DevSecOps Maturity Model Leader

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
##### Expected results
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
- Improve Web Application Firewall GUI based on AI 
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

### OWASP PyGoat

Intentionally vuln web Application Security in django.

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

##### Expected results

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

- Improve Vulnerabilities based on OWASP Top 10 - 2021
- Fixing all issues and work with Docker


##### Getting started
- Check[GitHub project](https://github.com/adeyosemanputra/pygoat) and [Website](https://owasp.org/www-project-pygoat/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-pygoat

##### Student Requirements
- Python
- Django

##### Mentor
* [Ade Yoseman](mailto:edikdoank@gmail.com)
 
### [OWASP PurpleTeam](https://purpleteam-labs.com/)

PurpleTeam is a Developer focussed security regression testing CLI and SaaS targeting Web applications and APIs.
The [CLI](https://github.com/purpleteam-labs/purpleteam) is specifically targeted at sitting within your build pipelines but can also be run manually.
The SaaS that does the security testing of your applications and APIs can be deployed anywhere.

The core components are detailed [here](https://purpleteam-labs.com/product/#composition).

#### Getting Started

* To get started contributing review the [Contributing Guide](https://github.com/purpleteam-labs/purpleteam/blob/main/CONTRIBUTING.md)
* Review the high level architecture [here](https://purpleteam-labs.com/doc/local/set-up/#purpleteam-local-architecture)
* Review the [Product Backlog](https://github.com/purpleteam-labs/purpleteam/projects/2)
* Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-purpleteam
* View other [community](https://purpleteam-labs.com/community/) options
* Dive into the [documentation](https://purpleteam-labs.com/doc/)

#### Idea 1: Fork docker-compose-ui

##### Description

PurpleTeam `local` relies on [docker-compose-ui](https://github.com/francescou/docker-compose-ui) to start [stage two containers](https://github.com/purpleteam-labs/purpleteam-s2-containers).
docker-compose-ui is now no longer maintained.
In order to use the latest versions of docker-compose docker-compose-ui needs to be forked and made to support the latest docker-compose version. Additional getting started resources [here](https://github.com/purpleteam-labs/purpleteam/issues/107/#85af9354087).

##### Expected Outcomes

* Consumers of PurpleTeam `local` and Developers will be able to use the latest version of docker-compose to start the stage two containers
* The [workflow](https://purpleteam-labs.com/doc/local/workflow/) should remain largely the same
* All related documentation should be up-to-date
* The forked docker-compose-ui and the rest of the PurpleTeam components will need to be Thoroughly tested

##### Skills Required/Preferred

* A reasonable level of JavaScript (NodeJS) experience
* A reasonable understanding of docker-compopse, Docker and containers
* A reasonable level of Python experience or understanding
* You will need to have PurpleTeam `local` [set-up](https://purpleteam-labs.com/doc/local/set-up/) and [running](https://purpleteam-labs.com/doc/local/workflow/) on your Linux development machine

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

#### Idea 2: Add Authentication Techniques

##### Description

Most of this work would be added to [`EmissaryAuthentication`](https://purpleteam-labs.com/doc/next-steps/#3-emissaryauthentication), as per [#44](https://github.com/purpleteam-labs/purpleteam/issues/44).
We will point you in the right direction for the Zaproxy authentication documentation.
This functionality will require modifications to the [_Job_](https://purpleteam-labs.com/doc/jobfile/) file, schema which resides in the CLI and _orchestrator_ and a separate schema in the _App Tester_.
Changes will need to be made for both [Browser App and API _Job_ file schemas](https://purpleteam-labs.com/doc/jobfile/) and documentation.

##### Expected Outcomes

* One or more of the authentication techniques could be implemented
* Add additional authentication techniques to the [existing strategies](https://github.com/purpleteam-labs/purpleteam-app-scanner/tree/main/src/sUtAndEmissaryStrategies)
* Add documentation around the new authentication techniques, we'll help point you in the right direction
* Thoroughly tested

##### Skills Required/Preferred

* Potentially work with a customer to make sure that their authentication need is meet and at the same time not break any other existing authentication techniques
* A reasonable level of JavaScript (NodeJS) experience
* A reasonable level of experience working with docker-compose, Docker and debugging containerised micro-services. Don't worry, we have good documentation around [debugging](https://purpleteam-labs.com/doc/local/workflow/)
* Some experience with Zaproxy scripting would be highly advantageous
* We will work with you to help you understand what Zaproxy (The _App Tester_ _Emissary_) supports and how to leverage the support within the _App Tester_
* You will need to have PurpleTeam `local` [set-up](https://purpleteam-labs.com/doc/local/set-up/) and [running](https://purpleteam-labs.com/doc/local/workflow/) on your Linux development machine

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

#### Idea 3: Create Better Dockerfiles

##### Description

Take the working stage one PurpleTeam `local` Dockerfiles and make them as small and fast as possible to build and run.
The Dockerfiles are core to how PurpleTeam is developed and debugged.
The smaller and faster these are, the faster PurpleTeam can be developed and deployed to both `local` and `cloud` environments.
As per issue [#92](https://github.com/purpleteam-labs/purpleteam/issues/91)

##### Expected Outcomes

* Stage one docker images are as small as possible
* Stage one docker images build and deploy as fast as possible
* The overall experience of developing and debugging PurpleTeam is significantly improved due to smaller wait times
* Deployments to both `local` and `cloud` environments are faster

##### Skills Required/Preferred

* Basic knowledge of building lean and fast Dockerfiles, don't worry, it's actually pretty easy
* Some knowledge of docker-compose, although not essential
* Ideally have PurpleTeam `local` [set-up](https://purpleteam-labs.com/doc/local/set-up/) and [running](https://purpleteam-labs.com/doc/local/workflow/) on your Linux development machine, although we could do the testing for you

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

#### Idea 4: Create API System Under Test (SUT)

##### Description

Find a purposely vulnerable API ideally that offers multiple authentication types and multiple types of API (openApi, SOAP, graphQl, generic).
Containerise it if it isn't already.
Add it to the [purpleteam-iac-sut](https://github.com/purpleteam-labs/purpleteam-iac-sut) project so that it can be deployed (with `terragrunt apply`) and destroyed (with `terragrunt destroy`).
This is so that the PurpleTeam core team can test against a vulnerable set of APIs to confirm that PurpleTeam (via Zaproxy) is producing the correct results.

##### Expected Outcomes

* As per the [Deployment Steps](https://github.com/purpleteam-labs/purpleteam-iac-sut#deployment-steps-regular-tf-workflow), it will be trivial to spin up and bring down again a purposely vulnerable API System Under Test (SUT) that sits within a container on AWS ECS

##### Skills Required/Preferred

* Ideally some knowledge of Terraform and Terragrunt
* You will need to have an understanding of how the [purpleteam-iac-sut](https://github.com/purpleteam-labs/purpleteam-iac-sut) works. Don't worry, we can help with this
* A reasonable level of experience working with microservices in Docker containers, as you will be adding a System Under Test that runs in a Docker container to the [purpleteam-iac-sut](https://github.com/purpleteam-labs/purpleteam-iac-sut) project

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

#### Idea 5: Provide the ability to remove alerts from reports by marking as false positive

##### Description

This is another way for PurpleTeam users to manage false positives. 
There's an option in the Zap API to `updateAlertsConfidence` for specific alerts.
We can change the confidence level to 0 - False Positive. This doesn't change the number of alerts raised, but the specific alert won't be included in the reports.
We've tested (PoC) this HTML and JSON reports.
Full details on the backlog item [#100](https://github.com/purpleteam-labs/purpleteam/issues/100).

##### Expected Outcomes

* [Documentation](https://purpleteam-labs.com/doc/jobfile/api/#updatealertsconfidence) will be updated. This will be mostly on the [_Job_](https://purpleteam-labs.com/doc/jobfile/) file, but may touch some other areas as well
* [_Build Users_](https://purpleteam-labs.com/doc/definitions/) will be able to remove alerts that they consider to be false positives by modifying the _Job_ file
* Thoroughly tested

##### Skills Required/Preferred

* You will need to have PurpleTeam `local` [set-up](https://purpleteam-labs.com/doc/local/set-up/) and [running](https://purpleteam-labs.com/doc/local/workflow/) on your Linux development machine
* A reasonable level of JavaScript (NodeJS) experience
* A reasonable level of experience working with microservices in Docker containers and debugging containerised micro-services. Don't worry, we have good documentation around [debugging](https://purpleteam-labs.com/doc/local/workflow/)
* Some experience with Zaproxy on the desktop along with it's API would be highly advantageous

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

#### Idea 6: Implement Server Scanner

##### Description

Implement the Server Scanner as the third PurpleTeam _Tester_ as per [#61](https://github.com/purpleteam-labs/purpleteam/issues/61).
We're going to be using Nikto. The majority of the code will be in https://github.com/purpleteam-labs/purpleteam-server-scanner.
This is mostly green fields work. We have the [app-scanner](https://github.com/purpleteam-labs/purpleteam-app-scanner) and [tls-scanner](https://github.com/purpleteam-labs/purpleteam-tls-scanner) fully implemented to use as a reference for what [_Testers_](https://purpleteam-labs.com/doc/definitions/) look like.
The diagram [here](https://purpleteam-labs.com/product/#composition) shows where _Testers_ fit into the architecture.

##### Expected Outcomes

* The Server Scanner will be implemented and users will be able to start getting results of the defects in the various server platforms they use
* Unit tests will be written where required, we will work though this with you
* The [CLI](https://github.com/purpleteam-labs/purpleteam) will now have a screen and log file showing the scanning of users servers in real-time as per the other _Testers_
* The [_orchestrator_](https://github.com/purpleteam-labs/purpleteam-orchestrator) will need to be modified to support the new _Tester_
* All related documentation should be up-to-date, this includes the project README and the [documentation](https://purpleteam-labs.com/doc/). The best way to find the places where additions and modifications need to be made is to search for the other testers (app-scanner, tls-scanner). We will work through this with you anyway

##### Skills Required/Preferred

* A reasonable level of JavaScript (NodeJS) experience
* A reasonable level of experience with docker-compose, Docker and containerising micro-services
* You will need to have PurpleTeam `local` [set-up](https://purpleteam-labs.com/doc/local/set-up/) and [running](https://purpleteam-labs.com/doc/local/workflow/) on your Linux development machine
* Thoroughly tested

##### Mentors

* [Kim Carter](mailto:gsoc2022@purpleteam-labs.com)

##### Expected Size of Project

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

#### Pick idea from [Product Backlog](https://github.com/purpleteam-labs/purpleteam/projects/2)

Pick an idea that we already have listed or supply one of your own. Please talk with us about what you're thinking of.

### [OWASP Threat Dragon](https://github.com/OWASP/threat-dragon)

Threat Dragon is a threat modeling tool that is widely used by many organisations and companies to create threat model diagrams.
It is an OWASP Lab project and is in the process of developing a new version 2.0 using Vue and Node.

##### Explanation of Ideas

Of the various features that are waiting to be implemented for Threat Dragon,
the one chosen for GSoC is self contained and directly visible to users of the project.

###### Enable Threat Dragon as a part of CI/CD Pipelines

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

It is not easy to use Threat Dragon in a CI/CD pipeline, and it would be great if CI/CD pipeline integration was provided by Threat Dragon.
This is a feature that is at the beginning of development, which allows the developer to design it from scratch and see it all the way through
to acceptance by the Threat Dragon community.

##### Expected Results

* Decide on what functionality is suitable for a CI/CD pipeline
* Architect and Document the API
* Incrementally implement the feature as a GitHub action
* Respond to feedback from the Threat Dragon community
* If a Jenkins Plugin can be provided then that is an added brownie

##### Getting started

* The project is written in Javascript, so some experience in this language is beneficial
* There is a [feature request](https://github.com/OWASP/threat-dragon/issues/88) for this work, and this will give some idea of the scope
* There are some [developer notes](https://github.com/OWASP/threat-dragon/blob/main/README.md) that give a flavour of our development process

##### Mentors

* [Arnold Kokoroko](mailto:awkokoroko@gmail.com) - OWASP Threat Dragon main contributor
* [Leo Reading](mailto:leo.reading@owasp.org) - OWASP Threat Dragon Project Leader

### [OWASP Coraza Web Application Firewall](https://github.com/corazawaf/coraza)

OWASP Coraza is a golang enterprise-grade Web Application Firewall framework that supports Modsecurity's seclang language and is 100% compatible with OWASP Core Ruleset. OWASP Coraza is super extensible; each feature from seclang can be easily extended and integrated with other technologies.

##### Getting Started
- To get started contributing review the [Contributing Guide](https://github.com/corazawaf/coraza/blob/v2/master/CONTRIBUTING.md)
- Review the [high level architecture](https://coraza.io/docs/reference/internals/)
- Review the [Product Backlog](https://github.com/orgs/corazawaf/projects/1)
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #coraza

##### Explanation of Ideas

###### Implement new directive for rate limiting

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

Rate limiting is a feature that needs to be concocted using a combination of SecRules that adds complexity and it is mandatory for the today Web. While you have the scaffolding to create it, is should be easy to create and maintain.

**Basic example**

The proposal is to add a new directive, maybe SecRuleRateLimit, where you define:

- the url to protect
- the rate limit per second/minute/etc.
- the action when the limit is reached:
  - return http code 429
  - send it to a tarpit
- also, when to clear the rate limit

**Advanced example**

The advanced setting should be able to synchronize this limit using a persistent storage or other communication method. Depending on the load, it will be very common to run a cluster of Coraza protected servers. Hence the need for syncing between all deployed servers.

There are many examples on how to do this using, for example, in memory or Redis. We should discuss if this requires additional go modules, which one is the best for this case.

**Expected Results**
- a new plugin that implements the feature
- documentation for configuration
- automated testing using CI/CD

**Student Requirements**

- Golang
- Key-value engines, like redis

**Mentors**
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

###### Apache module

Most OWASP Core Ruleset users are currently running their ruleset using apache 2 and mod_security2. In order to bring OWASP Coraza features to these users, we should provide a production-ready Apache module.

![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

**Expected Outcomes**

This project has two parts, making [libcoraza](https://github.com/corazawaf/libcoraza) stable enough to support the Apache implementation, and implementing an Apache module PoC that can evaluate seclang rules using Coraza and process the 5 Coraza phases efficiently.

**Some considerations:**
- libcoraza is a draft project, but the C bindings are already working
- The module name is mod_coraza
- The module must be able to evaluate the 5 phases of seclang
- The module must not support nesting rules across directories

The following project can be used as a baseline, but there is no stable release yet: https://github.com/SpiderLabs/ModSecurity-apache

**Student Requirements**
- C
- Apache internals

**Mentors**
* [Juan Pablo Tosso](mailto:jptosso@gmail.com)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

###### coraza-server

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

coraza-server was originally created as an experiment, but it has been the most successful sub-project. It allows to run OWASP Coraza as an HPOA server for HAProxy, but it was originally designed to support multiple protocols, like GRPC and Rest. Currently, it only supports SPOA.

**Expected Outcomes**

- Design proto files and rest API for GRPC and REST modules
- Implement the concurrent-safe modules for grpc and rest

**Student Requirements**
- Golang
- GRPC (Protobuf)

**Mentors**
* [Juan Pablo Tosso](mailto:jptosso@gmail.com)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

###### GraphQL body processor
![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Not recommended for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

OWASP Coraza supports multiple body processors, they are used to read the request body and transform the content into a processable format, for example, it can transform multipart data into a list of temporary files and arguments, or it can transform a JSON payload into arguments.

**Expected Results**

The GraphQL Body Processor must provide a safe way to read the GraphQL from JSON and create a simple introspection that could feed the ARGS_POST variable.

- We must consider if there is a safe library to parse graphql, or we must design a parser
- The ARGS structure should be similar to JSON (```json.somearg.0.id```)
- The body processor must be enforced, like:
```
SecRule REQUEST_METHOD "POST" "id:100, chain, nolog, msg:'Enforcing graphql', phase:1" 
SecRule REQUEST_URI "^/api/graphql$" "ctl:requestBodyProcessor=GRAPHQL"
```

**Student Requirements**
- Golang
- GraphQL

**Mentors**
* [Juan Pablo Tosso](mailto:jptosso@gmail.com)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

### [OWASP ModSecurity Core Rule Set](https://coreruleset.org)

The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

#### Getting Started

* Familiarize yourself with the project and its [basics](https://coreruleset.org/docs). Make sure you understand core concepts such as anomaly scoring, paranoia levels and false positives.
* Check out the [CRS Sandbox](https://coreruleset.org/docs/development/sandbox/)
* Check out the separate CRS GSoC [wiki page](https://github.com/coreruleset/coreruleset/wiki/Google-Summer-of-Code-2022)
* Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #coreruleset

#### CRS 💡 #1

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Machine Learning plugin integration

#####  Summary

Enhance / finish / develop / integrate the machine learning plugin, including the documentation and showcase project for people to reproduce

##### Description

There have been a few diploma or master thesis working with ModSecurity / CRS and machine learning. Most of the students really struggled to understand ModSecurity and were hardly able to concentrate on the more interesting ML research. The idea of this project is to finish / polish the existing proposal for a ML framework for CRS, so that future students have an easier time getting started with ML and ModSecurity / CRS.

##### Expected Outcomes

- Move the approach to the new [plugin framework](https://github.com/coreruleset/dummy-plugin)
- Review the current approach and see if the information sent works for all cases.
- Define the configuration vars needed for the plugin to work
- Write tests to test that the plugin works with a mocked ML server/service that will receive the parameters
- Document all changes and usage

##### Skills required/preferred

- Good writing skills
- Basic knowledge of programming languages

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

#### CRS 💡 #2 

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

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

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

#### CRS 💡 #3

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

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

#### CRS 💡 #4

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

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

#### CRS 💡 #5

![Preferred for "Small" GSoC 2022 project](https://img.shields.io/badge/small%20size%20(~100h)-preferred-green)
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)

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

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

#### CRS 💡 #6

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Automated WAF CVE testing and reporting

##### Summary

Setup automatic workflow to scan existing CVE PoC repository and run PoCs against sandbox

##### Description

This takes threat intelligence and threat analysis to the next level. The idea is to hook up on the [Trickest GitHub Repo with Proof of Concept exploits of CVEs](https://github.com/trickest/cve), extract them automatically, run them against our sandbox and report; namely if we do not catch the exploit.

If you manage to pull this off, this would be real milestone for the WAF / security industry. On top, this looks like a lot of fun.

##### Expected Outcomes

- Define and implemente a process for automating extraction of web attacks from CVE exploits
- Scaffolding for testing against existing WAF testing implementations
- Once the test is executed, write reports on the result
- Reports in SARIF format or equivalent are a plus
- Automation should be the primary focus (e.g. CI/CD)

##### Skills required/preferred

- Knowledge of Programming Languages (e.g Python)
- Knowledge of testing frameworks (e.g. pytest or similar)
- Knowledge on pipelines execution (e.g. Github Actions or similar)
- Basic knowledge on CVE and the ecosystem around it

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

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

#### Knowledge Prerequisites

* Docker
* Python
* CyberSecurity
* MongoDB
* Web Design knowledge

##### Mentors
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [Dhiren Serai](mailto:dhirensr@gmail.com)

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
* [Dhiren Serai](mailto:dhirensr@gmail.com)

### [Security Knowledge Framework (SKF)](https://owasp.org/www-project-security-knowledge-framework/)

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Explanation of Ideas
OWASP SKF is an open source web application that explains secure coding and its goal is to help you learn and integrate security by design in your software development and build applications that are secure by design.
We have more then 70 SKF Labs for developers to practice the skills in security in terms of identifying and testing vulnerabilities. Apart from that, we also have writeup written for every lab [here](https://github.com/blabla1337/skf-labs/tree/master/md) and this Markdown files have images and text explicitly.

So now the idea is to create a Video Editor, which is a web-based application for OWASP SKF, which will take those Markdown
files as an input and separate those images and text, and will convert them into a Video or Presentation. 

In technical Terms, We can do is to make a video editor in React or some other Framework, that will take a file like writeup.pdf or in other format. Then in the UI side you have options to put text in blocks. A block will contain text, time interval in video and an image which we will show at that time interval.
That's how we can make multiple blocks and after submitting the data. We will call the backend RestAPIs in django or flask, which will take those blocks data which contain time intervals images and text. And convert that text into speech and ultimately combine all those into a MP3 or any video file which user can get  after the request is complete.

This will be the initial version of the project. We can advance it more using deep learning and some video editor libraries.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

##### Getting Started

* [SKF-Labs](https://github.com/blabla1337/skf-labs/)

#### Expected Results

* A UI, where we can set the parameters like time interval, image and text or any other feature in video, which we want to show in that interval and multiple blocks should be created which is separated with time intervals.
* Backend Application, which will have the logic to convert all the blocks into a single video file and give the video to UI as a response for the request.
* Well structured code with proper unit testing.

#### Knowledge Prerequisites

* Python
* React or Any Web Based UI Framework
* Django or Flask for Backend
* DevOps (AWS or GCP for hosting the APIs using Docker)
* WaveNets, DeepLearning (Optional)

##### Mentors
* [Ankit Choudhary](mailto:ankitchoudhary202.ac@gmail.com)
* [Glenn ten Cate](mailto:glenn.ten.cate@owasp.org)

### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Explanation of Ideas
* Crypto - create a proof of stake coin called BUG
* Flutter - ideas to improve the app? Launch it on the App Store.
* Django - Website integration of new design
* Private issue reporting - allow companies to switch on private issue reporting.
* Payments for issues reported - allow companies or individuals to pay big hunters
* Browser plug-in to check bug reports - scan each site visited against a database to see if any bugs were found - we have a plug-in for chrome, let’s update it.
* Allow for the detection of banned apps in different countries. How would the internet look like if I was in country x.
* Allow for customers to track their online presence and help take down links where they did not approve their personal info on.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

##### Getting Started

* [BLT Core](https://github.com/owasp/blt/)
* [Flutter App](https://github.com/Bugheist/Flutter/)

#### Expected Results

* Proof of stake coin on the testnet and mainnet.
* Release Flutter app on App Store and Play Store.
* Implementation of private issues reporting.
* Update of browser plugins to support showing bugs on relative sites in a secure way
* Ability to choose a country from a selected list and see what apps are banned there
* Ability for users to report links online with personal information where they can have it removed

Reach out to us on Slack to discuss further on the scope, changes required, or if you have any other proposal.

#### Knowledge Prerequisites

* Python / Django for Backend
* Flutter for Mobile
* Blockchain / Bitcoin clone for the coin

##### Mentors
* Donnie on slack (lead mentor)
* [Sourav Badami](mailto:sourav.badami@owasp.org) - Django Mentor  
* Rahul Badami - Payments Mentor  
* [Ankit Choudhary](mailto:ankitchoudhary202.ac@gmail.com) - Flutter Mentor  
* [Sparsh Agrawal](mailto:sparshagrawal1212@gmail.com) - Flutter Mentor
