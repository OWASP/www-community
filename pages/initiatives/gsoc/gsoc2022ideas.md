---
layout: full-width
title: GSoC 2022 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2022ideas
---

# {{page.title}}

<!-- Template: Use a format like below to add your project:
### [Project Name]

##### [Explanation of Ideas]

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

##### [Expected Results]

##### [Getting Started]

##### [Mentors]
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
* Timo Pagel - OWASP Juice Shop Core Team

### [OWASP ZAP](https://zaproxy.org/)

ZAP is the world’s most widely used web scanner. Previous GSoC contributors have added key features and are all listed in the [ZAP Student Hall of Fame](https://www.zaproxy.org/student-hall-of-fame/).

To get started with ZAP contributions see the [ZAP Contributing Guide](https://www.zaproxy.org/docs/contribute/). We expect GSoC contributors who apply to work on ZAP to have had at least one code PR merged into one of the ZAP repos.

##### Import PCAP/PCAPNG Files

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

Import PCAP/PCAPNG Files into ZAP as per [#4812](https://github.com/zaproxy/zaproxy/issues/4812)

##### Modern Web App Framework Handling: Angular / VueJS / React

![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

Enhance ZAP to handle one modern framework better - either Angular, VueJS or React. This project should allow ZAP to extract more information from one of the top JavaScript frameworks and potentisally tune attacks to target known issues with that framework.

##### Your Own Idea

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

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

##### [Mentors]

* Timo Pagel

### [OWASP SecureTea](https://securetea.org/)

The OWASP SecureTea Project provides a one-stop security solution for various devices (personal computers / servers / IoT devices).

##### Expected results
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

##### Expected results
- Improve Vulnerabilities based on OWASP Top 10 - 2021


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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
|      | ✅     |      |

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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
|      | ✅     |      |

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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
| ✅   |        |      |

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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
|      | ✅     |      |

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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
| ✅   |        |      |

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

##### Level of Difficulty

| easy | medium | hard |
|------|--------|------|
|      |        | ✅   |

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

**Student Requirements**

- Golang
- Key-value engines, like redis

**Mentors**
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

###### Apache module

Most OWASP Core Ruleset users are currently running their ruleset using apache 2 and mod_security2. In order to bring OWASP Coraza features to these users, we should provide a production-ready Apache module.

![Not recommended for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

**Expected Results**

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

###### coraza-server

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

coraza-server was originally created as an experiment, but it has been the most successful sub-project. It allows to run OWASP Coraza as an HPOA server for HAProxy, but it was originally designed to support multiple protocols, like GRPC and Rest. Currently, it only supports SPOA.

**Expected Results**

- Design proto files and rest API for GRPC and REST modules
- Implement the concurrent-safe modules for grpc and rest

**Student Requirements**
- Golang
- GRPC (Protobuf)

**Mentors**
* [Juan Pablo Tosso](mailto:jptosso@gmail.com)

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

### [OWASP ModSecurity Core Rule Set](https://coreruleset.org)

The OWASP ModSecurity Core Rule Set (CRS) is a set of generic attack detection rules for use with ModSecurity or compatible web application firewalls. The CRS aims to protect web applications from a wide range of attacks, including the OWASP Top Ten, with a minimum of false alerts.

#### Getting Started

* Familiarize yourself with the project and its [basics](https://coreruleset.org/docs). Make sure you understand core concepts such as anomaly scoring, paranoia levels and false positives.
* Check out the [CRS Sandbox](https://coreruleset.org/docs/development/sandbox/)
* Check out the separate CRS GSoC [wiki page](https://github.com/coreruleset/coreruleset/wiki/Google-Summer-of-Code-2022)
* Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #coreruleset

#### CRS Idea 1: Enhance / finish / develop / integrate the machine learning plugin, including the documentation and showcase project for people to reproduce

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Description

There have been a few diploma or master thesis working with ModSecurity / CRS and machine learning. Most of the students really struggled to understand ModSecurity and were hardly able to concentrate on the more interesting ML research. The idea of this project is to finish / polish the existing proposal for a ML framework for CRS, so that future students have an easier time getting started with ML and ModSecurity / CRS.

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

#### CRS Idea 2: Systematic review of transformations, develop a guideline how to transform which parameters and in which order, implement the necessary changes

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Description

This is one for the nerds, or for somebody who is not afraid to dig into the hairy details of language encodings and their implementation. The ModSecurity SecLang rule language that CRS uses comes with a few dozen of transformation that can help to simplify payloads that make it easier to detect attacks. Think of removing white space or perform base64 decoding. CRS uses this, but we have to admit in an not overly systematic way. So what we would need is somebody who looks at the various options, looks at frequent attacks and tells us which transformations / decodings should be used and in which situation, so we can follow this guideline in a systematic way.

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

#### CRS Idea 3: Systematic performance analysis on various SecLanguage platforms: Costs of operators, transformations and variables (depending on size of payload / varname+value and number of variables)

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Description

This is a research project aiming to do a written report about the performance of the essential part of the SecRule language on various implementations, namely ModSecurity 2, libModSecurity 3, Coraza. The ModSecurity Handbook does not really go into enough detail of the performance impact of those constructs that CRS uses as its work horses. So we kind of depend on a gut feeling and a proper base and guideline would be very beneficial.

Without exaggerating too much, you need to keep in mind that CRS is running on millions of servers, some of them with hundreds of millions of requests per day (or more). If you now imagine that we could save some CPU cycles when we optimize the rules, then there is a big, big potential to good. Also to the planet in resource consumption.

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

#### CRS Idea 4: Create a performance testing framework i. e. something like regression tests but for performance, so we can see impact on performance of every pull request.

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Description

A frequent problem when developing new rules is their performance impact. Experience shows you do not really know the performance of a rule until you have tried it out. If you want to test it against a variety of payloads it's quite a lot of manual work and since we do not have a documented test procedure, it's all a bit random.

So the idea is to design a facility (typically a docker container) that is being configured with a rule and then used to test this rule with a variety of payloads and returns a standard report about the performance of the rule. Bonus points if multiple engines are covered (ModSecurity 2, libModSecurity 3, Coraza, ...)

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

#### CRS Idea 5: New plugin for &lt;enter-your-cool-idea&gt;

![Preferred for "Small" GSoC 2022 project](https://img.shields.io/badge/small%20size%20(~100h)-preferred-green)
![Possible for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)

##### Description

We have recently added plugin functionality to CRS. The [Plugin Registry](https://github.com/coreruleset/plugin-registry) has a decent overview of existing plugins and this [blog post](https://coreruleset.org/20220209/introducing-the-fake-bot-plugin/) does a good job describing a very cool plugin for inspiration.

Think about writing another cool plugin to complement the repository.

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

#### CRS Idea 6: Setup automatic workflow to scan existing CVE PoC repository and run PoCs against sandbox

![Preferred for "Medium" GSoC 2022 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2022 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

##### Description

This takes threat intelligence and threat analysis to the next level. The idea is to hook up on the [Trickest GitHub Repo with Proof of Concept exploits of CVEs](https://github.com/trickest/cve), extract them automatically, run them against our sandbox and report; namely if we do not catch the exploit.

If you manage to pull this off, this would be real milestone for the WAF / security industry. On top, this looks like a lot of fun.

##### Mentors

The CRS team will assign a mentor to contributors. In the meantime, the following two CRS project leaders will be your contacts:

* [Christian Folini](mailto:christian.folini@owasp.org)
* [Felipe Zipitría](mailto:felipe.zipitria@owasp.org)

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

