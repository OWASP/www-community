---
layout: full-width
title: GSoC 2024 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2024ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull;  [Juice Shop](#owaspjuiceshop) &bull; [DevSecOps Maturity Model](#owaspdevsecops-maturity-model) &bull; [OWASP OWTF](#owasp-owtf) &bull; [OWASP secureCodeBox](#owasp-securecodebox) &bull; [OWASP Nettacker](#owasp-nettacker) &bull; [OWASP Threat Dragon](#owasp-threat-dragon)


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

We have over 40 projects available in 5 repositories to work on! Check the difficulty and project size in Github.

[View all BLT project ideas on Github](https://github.com/orgs/OWASP-BLT/projects) 


#### Expected Results

* We would expect that any projects you choose to include in your proposal are fully completed.

Reach out to us on Slack to discuss further on the scope, changes required, _or if you have any other proposal._
* Please submit your proposal on the [BLT GitHub discussion board](https://github.com/orgs/OWASP-BLT/discussions) in markdown language before you convert it to a PDF.  Because it will be easier for the team to review and give feedback there.
* Team meetings are every Saturday at 12pm EST on [Slack - Join here](https://owasp.slack.com/archives/C2FF0UVHU)

#### Knowledge Prerequisites

* Python / Django for Backend
* Flutter for Mobile app
* Blockchain development
* Some knowledge of UI designing for design related ideas.

##### Mentors
* Donnie (@DonnieBLT on Slack) -- lead mentor
* Swapnil Shinde (@AtmegaBuzz on Slack) -- Django and blockchain mentor
* Arkadii Yakovets (@arkid15r on Slack) -- Python/Django mentor
* We are looking for mentors, reach out to us on Slack

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

###### Test Suite Harmonization

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Not recommended for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~175h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

Juice Shop had a full replacement of its end-to-end test suite - from Protractor to Cypress - in its GSoC 2022 project. Now it is time to take on the remainin test suites, especially the Integration/API tests currently running on Frisby.js. That library as not seen updates in 2+ years and it became more and more flaky over the years, causing occasional CI/CD failures and time-consuming retry-mechanisms to keep those in check. A new foundation for these tests is needed. In scope is also to look at the frontend and backend unit test suites, and find a way to reduce the number of test frameworks being used in order to achieve higher consistency and less complexity for maintenance of the project.

###### Juice Shop CTF Tool Rennovation

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Not recommended for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~175h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

The Juice Shop CTF Tool is currently implemented in vanilla JavaScript. It should be migrated to TypeScript for consistency of maintenance with the main project. Furthermore, the code linting should be adapted to the main Juice Shop ESLint standards. Test coverage and relevance should be reviewed and strengthened where necessary. 

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
  [our available test suites](https://pwning.owasp-juice.shop/companion-guide/latest/part3/contribution.html#_testing).

##### Getting started

* Make sure your JavaScript/TypeScript is sufficient to work on the
  Juice Shop codebase. Check our
  [Codebase 101](https://pwning.owasp-juice.shop/companion-guide/latest/part3/codebase.html)
  here. Students with some experience with (or willingness to learn)
  Angular and NodeJS/Express are usually prefered.
* Read our
  [Contribution Guidelines](https://pwning.owasp-juice.shop/companion-guide/latest/part3/contribution.html)
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

### [OWASP DevSecOps Maturity Model](https://dsomm.owasp.org)

Join us in enhancing the DSOMM, a pivotal tool designed to improve the security and operational efficiency of software development processes. We are looking for passionate students to contribute to two major areas: our main application development in JavaScript and our metric analyzer and collector in Java. Whether you are looking to tackle medium-sized challenges or are ready to embark on a larger project, we have exciting opportunities for you.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "dsomm" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Medium Feature Pack for the DSOMM Main Application (JS)
![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
This pack includes tasks that are crucial for enhancing the user experience and functionality of the DSOMM main application. Contributors will address existing issues and add new features:
- Implement a **State or Tag for "Not yet assessed"**, addressing [Issue #241](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/241) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Enhance the **Excel download feature in "Mapping"** by adding assessment information, as discussed in [Issue #244](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/244#issuecomment-1811127472) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Refine the handling of **subcategories** to streamline the organization and presentation of maturity model elements, making the tool more intuitive. See [Issue #194](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/194) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Introduce the **Adding of Diagrams** feature to enhance the visualization of DevSecOps processes and maturity levels, as outlined in [Issue #183](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/183) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- **Your Idea:** Proposals that innovate or enhance the metric collection and analysis process are highly encouraged.

##### Large Feature Pack for the metric Analyzer and Collector (Java)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
This pack challenges students to develop the entire workflow from data collection to visualization for DSOMM metrics, including the implementation of a Kafka queue. Projects include:
- Design and implement a **collector for OWASP DefectDojo**, fetching Mean Time to Resolve (MTTR) and Mean Time to Patch (MTTP) via the [defectdjo-client](https://github.com/SDA-SE/defectdojo-client) which fetches MTTR/MTTP) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Develop a **collector for Confluence**, to retrieve essential documents such as threat modeling and pentest reports, with a focus on document management and identification. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Engineer a **collector for GitHub**, to calculate MTTP by tracking pull request opening and merge dates. In addition, check that _branch protection_ is enabled and a .gitignore exists in the root file system. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- **Your Idea:** Proposals that innovate or enhance the metric collection and analysis process are highly encouraged.

##### Large Feature Pack for the metric Analyzer and Collector (Java)
![Preferred for "Large" GSoC 2024 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
This pack challenges students to develop the entire workflow from data collection to visualization for DSOMM metrics, including the implementation of a Kafka queue. Projects include:
- Design and implement a **collector for OWASP DefectDojo**, fetching Mean Time to Resolve (MTTR) and Mean Time to Patch (MTTP) via the [defectdjo-client](https://github.com/SDA-SE/defectdojo-client) which fetches MTTR/MTTP) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Develop a **collector for Backstage, Jira and Confluence**, to retrieve essential documents such as threat modeling and pentest reports, with a focus on document management and identification. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Create a **collector for Jenkins**, aimed at measuring deployment frequency by team, a key metric in DevOps performance. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Engineer a **collector for GitHub**, to calculate MTTP by tracking pull request opening and merge dates. In addition, check that _branch protection_ is enabled and a .gitignore exists in the root file system. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Engineer a **collector for Dependency Track**, fetching Mean Time to Resolve (MTTR) and Mean Time to Patch (MTTP) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- **Your Idea:** Proposals that innovate or enhance the metric collection and analysis process are highly encouraged.

Please take a look at the [architecture digram of DSOMM metricCA](https://github.com/devsecopsmaturitymodel/metricCA). The whole way from the collector to grafana needs to be implemented. Please note that a queue Kafka and Prometheus is currently not implemented and needs to be implemented in the collector and in the metricAnalyzer.

For Backstage, Jira and Confluence a defined format and tags might be used to identify the corresponding team and type of document (e.g. threat modeling/pentest).

#### Prerequisites
- Proficiency in the corresponding programming language (JavaScript for the main application, Java for the metric analyzer and collector)
- Previous contributions to open-source projects are highly desirable, demonstrating your commitment and collaborative skills

##### Mentors
Reach out to us on Slack to discuss these and other ideas!

- [Timo Pagel](mailto:timo.pagel@owasp.org)
- [Aryan Prasad](mailto:aryan.prasad@owasp.org)

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

### [OWASP secureCodeBox](https://www.securecodebox.io)

secureCodeBox is a kubernetes based, modularized toolchain for continuous security scans of your software project.
The secureCodeBox comes with many different scanners officially integrated (from Amass to Zap) and integration 
with vulnerability management backends like DefectDojo.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "securecodebox" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Explanation of Ideas

###### Add a secureCodeBox CLI (scbctl)

![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

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
* Make sure that you have a solid golang knowledge to be able to complete the proposed project.
* Get in touch with
  [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) to discuss any
  of the listed or your own idea for GSoC!

##### Mentors

* [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) - OWASP secureCodeBox Core Team
* [Robert Felber](mailto:robert.seedorff@owasp.org) - OWASP secureCodeBox Project Lead

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
- implement testing framework, get 70% code coverage level

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
* [Arkadii Yakovets](mailto:arkadii.yakovets@owasp.org)

### [OWASP Threat Dragon](https://owasp.org/www-project-threat-dragon/)

OWASP Threat Dragon is a modeling tool used to create threat model diagrams as part of a secure development lifecycle.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Preferred for "Medium" GSoC 2024 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

##### Explanation of Ideas

The threat engine has two features that have not yet been carried over from version 1.x to the current version 2.x.
These need to be implemented and expanded from what is available in version 1.x; both ideas are independent GSoC projects:

- add threats by element for STRIDE/LINDDUN/PLOT4ai [issue #792](https://github.com/OWASP/threat-dragon/issues/792)
- add threats using OWASP Automated Threats (OATs) patterns [issue #501](https://github.com/OWASP/threat-dragon/issues/501)

##### Getting Started

- Browse the [documentation](https://owasp.org/www-project-threat-dragon/docs-2/) to see if Threat Dragon is for you
- Join OWASP Slack and contact the Threat Dragon community on channel [#project-threat-dragon](https://app.slack.com/client/T04T40NHX/CURE8PQ68)
- Refer to the Threat Dragon [contributing guidelines](https://github.com/OWASP/threat-dragon/blob/main/contributing.md)

Repositories:

- [OWASP Threat Dragon on OWASP GitHub](https://github.com/OWASP/threat-dragon)

##### Knowldege  Requirements

- Javascript
- Node.js
- git

##### Mentors

* [Jon Gadsden](mailto:jon.gadsden@owasp.org)

