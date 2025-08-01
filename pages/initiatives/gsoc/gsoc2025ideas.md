---
layout: full-width
title: GSoC 2025 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2025ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull; [OWASP DevSecOps Maturity Model](#owasp-devsecops-maturity-model) &bull; [OWASP Nettacker](#owasp-nettacker) &bull; [OWASP Nest](#owasp-nest) &bull; [OWASP Juice Shop](#owasp-juice-shop) &bull; [Pygoat](#pygoat) &bull; [OpenCRE](#opencre) &bull; [OWASP OWTF](#owtf)

<!-- Template: Use a format like below to add your project, don't forget to add it to the anchor links above:
### [Project Name]

##### Explanation of Ideas

![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Expected Results

##### Getting Started

##### Mentors
-->

Tips to get you started in no particular order:
- Read the
  [Student Guidelines](gsoc2025).
- Check our
  [GitHub organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

OWASP BLT is a **bug-hunting & logging platform** that enables users to hunt for vulnerabilities, participate in bug bounties, and contribute to open-source security. Organizations can leverage BLT to manage vulnerability reports, track security issues, and engage with ethical hackers.  

BLT is a large-scale project with a growing ecosystem, offering **full-stack development, security automation, AI-powered analysis, and blockchain-based incentives**. This year’s GSoC projects focus on **UI/UX improvements, API development, automation, and gamification** to enhance the platform's usability and impact.  

> Preference will be given to students who have at least **5 merged PRs** before GSoC selection.  

---

### 🔹 **2025 GSoC Ideas / Large Projects**  

#### 🔸 **Modern UI/UX Overhaul & Lightweight Front-End in React** (~350h)  
A complete redesign of BLT’s interface, improving accessibility, usability, and aesthetics. The new front-end will be built with React and Tailwind CSS, ensuring high performance while maintaining a lightweight architecture under **100MB**. Dark mode will be the default, with full responsiveness and an enhanced user experience.  

#### 🔸 **Organization Dashboard – Enhanced Vulnerability & Bug Management** (~350h)  
Redesign and expand the **organization dashboard** to provide seamless management of **bug bounties, security reports, and contributor metrics**. Features will include **advanced filtering, real-time analytics, and improved collaboration tools** for security teams.  

#### 🔸 **Secure API Development & Migration to Django Ninja** (~350h)  
Migrate our existing and develop a **secure, well-documented API** with automated security tests to support the new front-end. This may involve migrating from Django Rest Framework to **Django Ninja** for improved performance, maintainability, and API efficiency.  

#### 🔸 **Gamification & Blockchain Rewards System (Ordinals & Solana)** (~350h)  
Introduce **GitHub-integrated contribution tracking** that rewards security researchers with **Bitcoin Ordinals and Solana-based incentives**. This will integrate with other parts of the website as well such as daily check-ins and code quality. Gamification elements such as **badges, leaderboards, and contribution tiers** will encourage engagement and collaboration in open-source security.  

#### 🔸 **Decentralized Bidding System for Issues (Bitcoin Cash Integration)** (~350h)  
Create a decentralized system where developers can bid on **GitHub issues** using **Bitcoin Cash**, ensuring **direct transactions** between contributors and project owners without BLT handling funds.  

#### 🔸 **AI-Powered Code Review & Smart Prioritization System for Maintainers** (~350h)  
Develop an **AI-driven GitHub assistant** that analyzes pull requests, detects security vulnerabilities, and provides **real-time suggestions** for improving code quality. A **smart prioritization system** will help maintainers rank issues based on **urgency, community impact, and dependencies**.  

#### 🔸 **Enhanced Slack Bot for Real-Time Security Alerts & Automation** (~175h)  
Expand the BLT **Slack bot** to automate vulnerability tracking, send real-time alerts for new issues, and integrate **GitHub notifications and contributor activity updates** for teams.  

🔗 **More projects & discussions:** [BLT Milestones](https://github.com/OWASP-BLT/BLT/milestones)  

---

### ✅ **Expected Results**  
- Successfully implementing a **fully functional, production-ready** feature.  
- Contributions must align with **BLT’s core security and performance goals**.  
- Code should adhere to best practices, including **security testing, CI/CD integration, and documentation**.  

---

### 📌 **Knowledge Prerequisites**  
To contribute effectively, familiarity with at least one or more of the following is recommended:  

- **Back-End:** Python, Django, Django Ninja, SQL  
- **Front-End:** React, Next.js, Tailwind CSS, HTML/CSS  
- **Blockchain:** Bitcoin Ordinals, Solana, Smart Contracts  
- **AI/ML:** NLP, Machine Learning for security analytics  
- **DevOps & Security:** GitHub API, REST API, OAuth, Authentication  

---

### 👥 **Mentors**  
We are actively looking for more mentors! If you have experience in **Django, React, Blockchain, or AI**, we’d love to have you onboard.  

📌 _Confirmed Mentors:_  
- **Donnie** (_@DonnieBLT on Slack_)  
- **Yash Pandey**  
- **Bishal Das**  
- **Ahmed ElSheikh**  
- **Patricia Waiyego**
- **Sudhir**
- _Looking for 4 more mentors!_  

🎥 _To get up to speed, check out our [BLT videos](https://blt.owasp.org/bltv/)._  


### [OWASP DevSecOps Maturity Model](https://dsomm.owasp.org)

Join us in enhancing the DSOMM, a pivotal tool designed to improve the security and operational efficiency of software development processes. We are looking for passionate students to contribute to two major areas: our main application development in JavaScript and our metric analyzer and collector in Java. Whether you are looking to tackle medium-sized challenges or are ready to embark on a larger project, we have exciting opportunities for you.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "dsomm" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Medium Feature Pack for the DSOMM Main Application (JS)
![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
This pack includes tasks that are crucial for enhancing the user experience and functionality of the DSOMM main application. Contributors will address existing issues and add new features:
- Implement a **State or Tag for "Not yet assessed"**, addressing [Issue #241](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/241) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Enhance the **Excel download feature in "Mapping"** by adding assessment information, as discussed in [Issue #244](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/244#issuecomment-1811127472) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Refine the handling of **subcategories** to streamline the organization and presentation of maturity model elements, making the tool more intuitive. See [Issue #194](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/194) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Introduce the **Adding of Diagrams** feature to enhance the visualization of DevSecOps processes and maturity levels, as outlined in [Issue #183](https://github.com/devsecopsmaturitymodel/DevSecOps-MaturityModel/issues/183) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- **Your Idea:** Proposals that innovate or enhance the metric collection and analysis process are highly encouraged.

##### Large Feature Pack for the metric Analyzer and Collector (Java)
![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
This pack challenges students to develop the entire workflow from data collection to visualization for DSOMM metrics, including the implementation of a Kafka queue. Projects include:
- Design and implement a **collector for OWASP DefectDojo**, fetching Mean Time to Resolve (MTTR) and Mean Time to Patch (MTTP) via the [defectdjo-client](https://github.com/SDA-SE/defectdojo-client) which fetches MTTR/MTTP) ![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
- Develop a **collector for Jira**, to retrieve information about security tasks. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Create a **collector for Jenkins and Kubernetes**, aimed at measuring deployment frequency by team, a key metric in DevOps performance. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Engineer a **collector for GitHub and Bitbucket**, to calculate MTTP by tracking pull request opening and merge dates. In addition, check that _branch protection_ is enabled and a .gitignore exists in the root file system. ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Engineer a **collector for gitleaks**, fetching Mean Time to Resolve (MTTR) and Mean Time to Patch (MTTP) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
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

### [OWASP Nettacker](https://owasp.org/www-project-nettacker/)

OWASP Nettacker is a Modular Automated Penetration Testing/ Information gathering Framework and Vulnerability Scanner fully written in Python. Nettacker can run a variety of scans discovering subdomains, open ports, services, vulnerabilities, misconfigurations, default credentials.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

##### Explanation of Ideas

- fix scan engine multi-threading/queuing issues
- improve WebUI / add dashboard
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

### [OWASP Nest](https://nest.owasp.org)

OWASP Nest is a comprehensive platform designed to enhance collaboration and contribution within the OWASP community. The application serves as a central hub for exploring OWASP projects and ways to contribute to them, empowering contributors to find opportunities that align with their interests and expertise. Our mission is to drive real-world collaboration and elevate the OWASP organization by addressing key challenges and streamlining processes.

#### Repository

- [backend](https://github.com/OWASP/Nest/tree/main/backend)
- [frontend](https://github.com/OWASP/Nest/tree/main/frontend)
- [schema](https://github.com/OWASP/Nest/tree/main/schema)

#### Technical Stack

- Python, Django, Pytest
- TypeScript, React, Jest
- Chakra UI, Tailwind CSS
- PostgreSQL, Algolia
- Docker, k8s, AWS

#### Projects / Ideas

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange) ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

- [OWASP Contribution Hub](https://github.com/OWASP/Nest/issues/710): Aiming to streamline the onboarding process and connect contributors with mentors and impactful projects. This milestone focuses on improving collaboration within the OWASP community.
- [OWASP Nest API](https://github.com/OWASP/Nest/issues/707): The development of REST and GraphQL API endpoints for OWASP Projects, Chapters, Events, and Committees. This milestone will standardize data access across OWASP’s resources.
- [OWASP Nest Kubernetes Adoption](https://github.com/OWASP/Nest/issues/706): This milestone focuses on migrating the OWASP Nest application to Kubernetes, ensuring scalability, reliability, and ease of deployment.
- [OWASP NestBot AI agent/assistant](https://github.com/OWASP/Nest/issues/908): Develop an AI-powered OWASP NestBot Slack assistant that acts as an auto-responder for frequently asked questions, guides users to the appropriate OWASP channels, and handles typical OWASP community queries.
- [OWASP Project Health Dashboard](https://github.com/OWASP/Nest/issues/711): A dashboard for monitoring the health of OWASP projects. This includes tracking vital metrics such as release frequency, issue resolution, and contributor growth.
- [OWASP Schema](https://github.com/OWASP/Nest/issues/709): Developing and extending a standardized schema for OWASP Projects and Chapters. This milestone aims to ensure consistency and ease of integration across OWASP resources.
- [OWASP Snapshots](https://github.com/OWASP/Nest/issues/708): Creating a summary of activities within OWASP projects, chapters, and events, including new blog posts and news, to keep the community informed about recent developments.

Please visit our planned [milestones page](https://github.com/OWASP/Nest/milestones) or `gsoc2025` labeled [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3Agsoc2025).

#### Your own ideas

![Possible for "Small" GSoC 2025 project](https://img.shields.io/badge/small%20size%20(90h)-possible-yellow) ![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(175h)-preferred-green) ![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange) ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Do you have an idea to improve OWASP Nest?
We'd love to hear it, please reach out in Slack to ensure that the idea fits OWASP Nest goals.

#### Expected Results

- Your proposal projects/ideas are fully completed.
- Your code follows our existing style guides and passes quality checks, test coverage, etc.

#### Getting Started

- Check out our [contributing guidelines](https://github.com/OWASP/Nest/blob/main/CONTRIBUTING.md)
- Join OWASP Nest channel [#project-nest](https://owasp.slack.com/archives/C07JLLG2GFQ)
- Consider `good first issue` (if there are any) from OWASP Nest [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)

#### Mentors

- [Arkadii Yakovets](https://github.com/arkid15r/) ([arkid15r](https://owasp.slack.com/team/U060W3NKLTF) on Slack)
- [Kateryna Golovanova](https://github.com/kasya/) ([Kate](https://owasp.slack.com/team/U07PWB1JZ6Z) on Slack)
- [Tamara Lazerka](https://github.com/aramattamara/) ([Tamara](https://owasp.slack.com/team/U0881RRPBDY) on Slack)


### [OWASP Juice Shop](https://owasp-juice.shop)

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

###### MultiJuicer as a CTF Platform

![Not recommended for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-hard-red)

MultiJuicer saw some enhancements of its Team Score Board last year. It now is not that far away from being a full-fledged CTF platform of its own. This project should focus on the remaining features needed to make MultiJuicer a fully functional CTF platform. This should include making the Team Score Board visually attractive, flavorfully unique and more competition-oriented. The existing Solution Webhook integration already marks solved challenges automatically, but other information like team cheat score, progress over time etc. are not tracked or displayed today. The MultiJuicer CTF should offer the same features as the Juice Shop CTF tool in order to configure the availability of hints. This should include a way to allow teams to pay for hints with some of their collected points. To avoid issues with bigger teams hacking on the same instance of Juice Shop, a team grouping mechanism could be considered as well. The progress on the CTF Score Board could then be aggregated on group level for different teams/instances.

###### Test suite harmonization

![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Not recommended for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

Juice Shop had a full replacement of its end-to-end test suite - from Protractor to Cypress - in its GSoC 2022 project. Now it is time to take on the remainin test suites, especially the Integration/API tests currently running on Frisby.js. That library as not seen updates in 2+ years and it became more and more flaky over the years, causing occasional CI/CD failures and time-consuming retry-mechanisms to keep those in check. A new foundation for these tests is needed. In scope is also to look at the frontend and backend unit test suites, and find a way to reduce the number of test frameworks being used in order to achieve higher consistency and less complexity for maintenance of the project. This project should include the test suites in the Juice Shop CTF tool as well. Proposals that also have the augmentation of MultiJuicer with end-to-end tests in scope, are specially welcome.  

###### Juice Shop side-project rennovation

![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Not recommended for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

The Juice Shop CTF Tool is currently implemented in vanilla JavaScript. It should be migrated to TypeScript for consistency of maintenance with the main project. Furthermore, the code linting should be adapted to the main Juice Shop ESLint standards. Test coverage and relevance should be reviewed and strengthened where necessary.

Similarly, the following other sub-projects should be rennovated and brought onto an identical tech stack: Juicy Statistics, Juicy Coupon Bot, Juicy Chat Bot, and Juicy Coupon Lambda.  

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
  Angular and Node.js/Express are usually prefered.
* Read our
  [Contribution Guidelines](https://pwning.owasp-juice.shop/companion-guide/latest/part3/contribution.html)
  very carefully. Best make some small contributions before GSoC, so we
  can see how you work and help you dive into the code even better.
* Get in touch [via Slack](https://owasp.slack.com/messages/project-juiceshop) or email (see below) to discuss any
  of the listed or your own idea for GSoC!

##### Mentors

* [Bjoern Kimminich](mailto:bjoern.kimminich@owasp.org) - OWASP Juice
  Shop Project Leader ([bkimminich](https://owasp.slack.com/team/U1S23SNE7) on Slack)
* [Jannik Hollenbach](mailto:jannik.hollenbach@owasp.org) - OWASP Juice Shop Project Leader ([Jannik](https://owasp.slack.com/team/UAM6MBY30) on Slack) 


### [PyGoat](https://owasp.org/www-project-pygoat/)
PyGoat is an open-source, intentionally vulnerable Python web application designed to help developers and security enthusiasts learn about web application security. It provides hands-on experience in identifying and mitigating common security vulnerabilities, making it a valuable resource for practicing secure coding and penetration testing techniques.

#### Repository
- [PyGoat](https://github.com/adeyosemanputra/pygoat)

#### Skills Required
- HTML/CSS/JavaScript
- Python 
- Django
- Docker
- Basic knowledge of application security

##### Getting started
- Check[GitHub project](https://github.com/adeyosemanputra/pygoat) and [Website](https://owasp.org/www-project-pygoat/).
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-pygoat

#### Projects / Ideas
![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Refactor the webapp, move away vulnarable labs from the main website.
- Deploy a microservice architecture based approch for the labs.
- Add new labs to the project.
- Improvment of interactive playgrounds.
- Extend labs to other languages as well.
- Prepare for `OWASP Top 10:2025` section

#### Mentors
- [ardiansyah](mailto:pakdesawangan@gmail.com)
- [Rupak Biswas](https://github.com/RupakBiswas-2304)([Rupak](https://owasp.slack.com/team/U036WSR1684) on slack)

  
### [OpenCRE](https://opencre.org/)
OpenCRE is the world's largest Cybersecurity knowledge graph.
It semantically links information between standards, knowledge bases and security tools.
Also, it allows users to extend the graph themselves and contains a RAG chatbot implementation.
OpenCRE is a great GSOC project if you're looking to add "Data science/engineering", "Knowledge Graph and AI" with a focus on Legal Tech and cybersecurity in your CV.

#### Repository
- [OpenCRE](https://github.com/OWASP/OpenCRE)

#### Skills Required
- HTML/CSS/React-Typescript
- Python 
- Flask
- Docker

##### Getting started
- Check the [GitHub project](https://github.com/OWASP/OpenCRE) and the issues marked as either `good first issue` , `help wanted` or `GSOC`
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #project-opencre

#### Projects / Ideas
![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2025 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- There are many small, medium and large project in the [Issues Page tagged with GSOC](https://github.com/OWASP/OpenCRE/issues?q=state%3Aopen%20label%3A%22GSOC%22) that we are interested in, depending on your background and interests they are split in the following categories: AI, Frontend, Backend, FullStack. They all contain a bit of frontend and data analysis and graph operations.
Priorities for us are:
- [Make the gap analysis functionality faster](https://github.com/OWASP/OpenCRE/issues/587)
- [MyOpenCRE](https://github.com/OWASP/OpenCRE/milestone/5)
- [Releasing the Explorer page](https://github.com/OWASP/OpenCRE/milestone/6)
  
#### Mentors
- [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org)
- [Rob Van Der Veer](mailto:rob.van.der.veer@owasp.org)
- [Paola Gardenas](mailto:paola.gardenas@owasp.org)


### [OWTF](https://owasp.org/www-project-owtf/)
OWTF attempts to solve the “penetration testers are never given enough time to test properly” problem, or in other words, OWTF = Test/Exploit ASAP, with this in mind, as of right now, the priorities are:

* To improve security testing efficiency (i.e. test more in less time)
* To improve security testing coverage (i.e. test more)
* Gradually integrate the best tools
* Unite the best tools and make them work together with the security tester
* Remove or Reduce the need to babysit security tools during security assessments
* Be a respository of PoC resource links to assist exploitation of vulnerabilities in order to illustrate risk to businesses.
* Help penetration testers save time on report writing

#### Repository
- [OWTF](https://github.com/owtf/owtf)

#### Skills Required
- Python 
- Tornado
- Docker
- React/React ecosystem for application frontend
- Basic knowledge of application security, tools used in bug bounty style hunting
- Some knowledge of how TLS works, man in the middle proxies, HTTP internals, etc.

##### Getting started
Please use the repositories’ issue tracker, GitHub discussions, and don’t forget to read the contributing guide. Join the community at #owtf on OWASP Slack and share your questions, project ideas.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "owtf" as Proposal Tag to make them easier to find for us. Thank you!

#### Projects / Ideas
![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-medium-orange) OWTF Modernization

OWTF has evolved over time, but parts of the codebase are outdated, have technical debt, and may not be optimized for newer Python versions or best practices. This project aims to modernize the OWTF codebase, ensuring long-term maintainability, security, and efficiency.
Key Objectives
1. Fix Long-Standing Bugs & Improve Stability
    * Audit and resolve GitHub issues related to stability, crashes, and performance bottlenecks.
    * Enhance logging and error handling for better debugging.
    * Improve unit tests and CI/CD pipelines to catch regressions early.
2. Optimize Plugin Execution & Dependency Management
    * Upgrade outdated third-party security tools used in plugins.
    * Reduce dependency bloat by removing redundant libraries.
    * Use async execution where applicable for better performance.

###### Expected Outcomes
✔️ OWTF will be cleaner, faster, and easier to maintain.<br/>
✔️ The project will be future-proofed with up-to-date dependencies.<br/>
✔️ Stability and performance will be significantly improved.<br/>


![Preferred for "Medium" GSoC 2025 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-medium-orange) MiTM proxy upgrade

OWTF's proxy was written almost 10 years ago based on the Tornado Web Framework. It is in rough shape and needs a lot of improvement on the transaction recording, storing, and modification side. We want to make it as good as [MiTM proxy](https://mitmproxy.org/).


###### Expected Outcomes
✔️ Modern mitm proxy that allows modificaiton of requests and responses on the fly<br/>
✔️ Better integration with the framework to record a variety of requests and responses.<br/>
✔️ Stability and performance.<br/>

##### Mentors
- [Viyat Bhalodia](mailto:viyat.bhalodia@owasp.org)
- [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
