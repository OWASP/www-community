---
layout: full-width
title: GSoC 2026 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2026ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull; [OWASP DevSecOps Maturity Model](#owasp-devsecops-maturity-model) &bull; [OWASP Nettacker](#owasp-nettacker) &bull; [OWASP Nest](#owasp-nest) &bull; [OWASP Juice Shop](#owasp-juice-shop) &bull; [Pygoat](#pygoat) &bull; [OpenCRE](#opencre) &bull; [OWASP OWTF](#owtf)

<!-- Template: Use a format like below to add your project, don't forget to add it to the anchor links above:
### [Project Name]

##### Explanation of Ideas

![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-possible-yellow)
![Not recommended for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)

![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Possible for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)
![Not recommended for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-not%20recommended-red)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

##### Expected Results

##### Getting Started

##### Mentors
-->

Tips to get you started in no particular order:
- Read the
  [Student Guidelines](gsoc2026).
- Check our
  [GitHub organization](https://github.com/OWASP).
- Contact one of the project mentors below.

## List of Project Ideas

### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

OWASP BLT is a **bug-hunting & logging platform** that enables users to hunt for vulnerabilities, participate in bug bounties, and contribute to open-source security. Organizations can leverage BLT to manage vulnerability reports, track security issues, and engage with ethical hackers.  

BLT is a large-scale project with a growing ecosystem, offering **full-stack development, security automation, AI-powered analysis, and blockchain-based incentives**. This year’s GSoC projects focus on **UI/UX improvements, API development, automation, and gamification** to enhance the platform's usability and impact.  

> Preference will be given to students who have at least **5 merged PRs** before GSoC selection.  

---

### 🔹 **2026 GSoC Ideas / Large Projects**  

#### 🔸 **New GSoC Projects coming soon for BLT**
Check out our ongoing projects [BLT projects](https://github.com/orgs/OWASP-BLT/projects?query=is%3Aopen)


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
- **Ahmed ElSheikh**  
- _More coming soon, Contact Donnie on Slack if you'd like to Mentor_  

🎥 _To get up to speed, check out our [BLT videos](https://owaspblt.org/education/)._


### [OWASP DevSecOps Maturity Model](https://dsomm.owasp.org)

Join us in enhancing the DSOMM, a pivotal tool designed to improve the security and operational efficiency of software development processes. We are looking for passionate students to contribute to two major areas: our main application development in JavaScript and our metric analyzer and collector in Java. Whether you are looking to tackle medium-sized challenges or are ready to embark on a larger project, we have exciting opportunities for you.

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP
  Organization on Google's GSoC page in "Draft Shared" mode.
- Please pick "dsomm" as Proposal Tag to make them easier to find
  for us. Thank you!

##### Update of the DSOMM Application (Angular)
![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
Primary Objectives:
- Upgrade Angular Framework: Migrate the DSOMM application from its current Angular version to Angular 21
- Updates: Update all related dependencies including TypeScript, RxJS, Angular CLI, and third-party libraries
- Code Modernization: Refactor deprecated APIs and adopt modern Angular patterns (standalone components, signals, etc.)
- Testing & Quality Assurance: Ensure all existing functionality works correctly after migration with comprehensive testing, this can lead to unit test optimization
- Documentation: Update developer documentation with new setup instructions and migration notes

#### Prerequisites
- Proficiency in the corresponding programming language (JavaScript and Angular for the main application)
- Previous contributions to open-source projects are highly desirable, demonstrating your commitment and collaborative skills

##### Mentors
Reach out to us on Slack to discuss these and other ideas!

- [Timo Pagel](mailto:timo.pagel@owasp.org)
- [Aryan Prasad](mailto:aryan.prasad@owasp.org)
- [Vegard Bakke](mailto:vegard.bakke@owasp.org)

### [OWASP Nettacker](https://owasp.org/www-project-nettacker/)

OWASP Nettacker is a Modular Automated Penetration Testing/ Information gathering Framework and Vulnerability Scanner fully written in Python. Nettacker can run a variety of scans discovering subdomains, open ports, services, vulnerabilities, misconfigurations, default credentials.

![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

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

OWASP Nest is a comprehensive platform built to enhance collaboration and streamline contributions across the OWASP community. Acting as a central hub, it helps users discover chapters and projects, find contribution opportunities, and connect with like-minded individuals based on their interests and expertise.

#### Repositories

- [OWASP Nest Backend](https://github.com/OWASP/Nest/tree/main/backend)
- [OWASP Nest Frontend](https://github.com/OWASP/Nest/tree/main/frontend)
- [OWASP Nest Schema](https://github.com/OWASP/nest-schema/)
- [API SDK Go](https://github.com/OWASP/nest-sdk)
- [API SDK Python](https://github.com/OWASP/nest-sdk-python)
- [API SDK TypeScript](https://github.com/OWASP/nest-sdk-typescript)

#### Technical Stack

- Python, Django, Pytest, Strawberry, Ninja
- TypeScript, React, Apollo, Next.js. Jest, PlayWright
- Hero UI, Tailwind CSS
- PostgreSQL, Algolia, Redis
- Docker, Ansible, Terraform, AWS

#### Projects / Ideas

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange) ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

- [OWASP Board Activity Standardization and Data Programmatic Access](https://github.com/OWASP/Nest/milestone/20): This milestone focuses on standardizing how OWASP Board activities are recorded, structured, and published.
- [OWASP Board Candidate Information Transparency and Fact-Checking](https://github.com/OWASP/Nest/milestone/19): This milestone focuses on improving the transparency, accuracy, and trustworthiness of information related to OWASP board candidates.
- [OWASP Chapter/Project Health Dashboard](https://github.com/OWASP/Nest/milestone/17): A dashboard for monitoring the health of OWASP chapters and projects. This includes tracking vital metrics such as meeting/release frequency, issue resolution, and contributor/member growth.
- [OWASP Community Snapshots](https://github.com/OWASP/Nest/milestone/16): Creating a summary of activities within OWASP projects, chapters, and events, including new blog posts and news, to keep the community informed about recent developments.
- [OWASP Nest Monitoring and Observability](https://github.com/OWASP/Nest/milestone/21): Implement modern monitoring and observability practices across OWASP Nest infrastructure on AWS to ensure reliability, performance visibility, and proactive issue detection.
- [OWASP NestBot AI Assistant](https://github.com/OWASP/Nest/milestone/8): Develop an AI-powered OWASP NestBot Slack assistant that acts as an auto-responder for frequently asked questions, guides users to the appropriate OWASP channels, and handles typical OWASP community queries.

Please visit our planned [milestones page](https://github.com/OWASP/Nest/milestones) or `gsoc2026` labeled [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3Agsoc2026).

#### Your own ideas

![Possible for "Small" GSoC 2026 project](https://img.shields.io/badge/small%20size%20(90h)-possible-yellow) ![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(175h)-preferred-green) ![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green) ![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange) ![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Do you have an idea to improve OWASP Nest?
We'd love to hear it, please reach out in Slack to ensure that the idea fits OWASP Nest goals.

#### Expected Results

- Your proposal projects/ideas are fully completed.
- Your code follows our existing style guides and passes quality checks, test coverage, etc.

#### Getting Started

- Check out our [contributing guidelines](https://github.com/OWASP/Nest/blob/main/CONTRIBUTING.md)
- Join OWASP Nest channel [#project-nest](https://owasp.slack.com/archives/project-nest)
- Consider `good first issue` from OWASP Nest [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)

#### Mentors

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/arkid15r.png" alt="Arkadii Yakovets" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Arkadii Yakovets</strong><br>
Cybersecurity Lead, CCSP, CISSP, CSSLP | OWASP Nest project leader<br>
<i class="fab fa-github"></i> <a href="https://github.com/arkid15r/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/arkid15r/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U060W3NKLTF">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kasya.png" alt="Kateryna Golovanova" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kateryna Golovanova</strong><br>
Senior Software Engineer at Skill Struck, CC | OWASP Nest project leader<br>
<i class="fab fa-github"></i> <a href="https://github.com/kasya/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kate-golovanova/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U07PWB1JZ6Z">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kerlynNkep.png" alt="Kerlyn Manyi" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kerlyn Manyi</strong><br>
Cybersecurity Engineer | GSoC'23 contributor at Mifos Initiative<br>
<i class="fab fa-github"></i> <a href="https://github.com/kerlynNkep">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kerlyn-manyi-a80201123/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U06M01ARG3V">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kritibirda.png" alt="Kriti Birda" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kriti Birda</strong><br>
AI/ML enthusiast | GSoC'25 contributor at Python Software Foundation<br>
<i class="fab fa-github"></i> <a href="https://github.com/kritibirda">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kritibirda/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U08KZ9Z7MFX">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/SalmanDeveloperz.png" alt="Muhammad Salman" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Muhammad Salman</strong><br>
Software Developer | GSoC'25 contributor at FOSSology<br>
<i class="fab fa-github"></i> <a href="https://github.com/SalmanDeveloperz/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/msalman199/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0A7YV0SPNE">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/noland-crane.png" alt="Noland Crane" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Noland Crane</strong><br>
Application Security Analyst at Bloomreach, CISSP<br>
<i class="fab fa-github"></i> <a href="https://github.com/noland-crane">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/nolandcrane/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0A4M7U056U">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/RAJANAGORI.png" alt="Raja Nagori" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Raja Nagori</strong><br>
Product Security Engineer at Splunk<br>
<i class="fab fa-github"></i> <a href="https://github.com/RAJANAGORI">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/raja-nagori/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U03HUR536TG">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/aramattamara.png" alt="Tamara Lazerka" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Tamara Lazerka</strong><br>
QA Analyst at Cart.com | GSoC'25 mentor at OWASP<br>
<i class="fab fa-github"></i> <a href="https://github.com/aramattamara/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/aramattamara/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0881RRPBDY">Slack</a>
</div>
</div>

Please contact Arkadii Yakovets or Kate Golovanova if you're interested in participating as a mentor.

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

> 🛑 Please be aware that the OWASP Juice Shop project will **not** consider or even review any proposals
> which fail to include an AI Tool Disclosure statement. We recommend you use the following templated that
> we derived from the one enforced on Pull Requests to OWASP Juice Shop:
>
> ```
> ### AI Tool Disclosure
>
> - [ ] My GSoC proposal does not include any AI-generated content
> - [ ] My GSoC proposal includes AI-generated content, as disclosed below:
>   - AI Tools: `[e.g. GitHub CoPilot, ChatGPT, JetBrains Junie etc.]`
>   - LLMs and versions: `[e.g. GPT-4.1, Claude Haiku 4.5, Gemini 2.5 Pro etc.]`
>   - Prompts: `[Summarize the key prompts or instructions given to the AI tools]`
> ```

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
![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Refactor the webapp, move away vulnarable labs from the main website.
- Deploy a microservice architecture based approch for the labs.
- Add new labs to the project.
- Improvment of interactive playgrounds.
- Extend labs to other languages as well.
- Prepare for `OWASP Top 10:2026` section

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
![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
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
![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
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


![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-medium-orange) MiTM proxy upgrade

OWTF's proxy was written almost 10 years ago based on the Tornado Web Framework. It is in rough shape and needs a lot of improvement on the transaction recording, storing, and modification side. We want to make it as good as [MiTM proxy](https://mitmproxy.org/).


###### Expected Outcomes
✔️ Modern mitm proxy that allows modificaiton of requests and responses on the fly<br/>
✔️ Better integration with the framework to record a variety of requests and responses.<br/>
✔️ Stability and performance.<br/>

##### Mentors
- [Viyat Bhalodia](mailto:viyat.bhalodia@owasp.org)
- [Abraham Aranguren](mailto:abraham.aranguren@owasp.org)
