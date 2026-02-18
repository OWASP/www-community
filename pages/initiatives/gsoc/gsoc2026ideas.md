---
layout: full-width
title: GSoC 2026 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2026ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull; [OWASP DevSecOps Maturity Model](#owasp-devsecops-maturity-model) &bull; [OWASP Nettacker](#owasp-nettacker) &bull; [OWASP Nest](#owasp-nest) &bull; [OWASP Juice Shop](#owasp-juice-shop) &bull; [Pygoat](#pygoat) &bull; [OpenCRE](#opencre) &bull; [OWASP OWTF](#owtf) &bull; [OWASP Cornucopia](#owasp-cornucopia)

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

OWASP BLT (Bug Logging Tool) is a community-driven OWASP Foundation project that develops and maintains open-source tools for structured vulnerability reporting, bug tracking, security automation, contributor engagement, and related infrastructure. The BLT ecosystem includes modular services, APIs, dashboards, browser and mobile applications, automation bots, and research initiatives, all developed transparently under OWASP governance and open-source licensing. 

BLT has evolved into a growing ecosystem that combines **modern full-stack engineering, AI-assisted security workflows, hands-on security education, distributed scanning infrastructure, and blockchain-backed incentive systems**. The platform functions both as a production-grade vulnerability management system and as a practical learning environment where contributors build real-world security expertise.

This year’s GSoC projects center on **core platform modernization, AI-native interfaces, automation-first workflows, distributed security infrastructure, hands-on security education, and meaningful gamification**. Our goal is to make BLT faster, more scalable, AI-agent ready, and deeply educational—turning real security work into structured learning pathways.

> Preference will be given to students who have at least **5 merged PRs** before GSoC selection.  

---

### 🔹 **2026 GSoC Ideas / All Large Projects**  
---

## [BLT-Next](https://github.com/OWASP-BLT/BLT-Next) : Core BLT Migration to GitHub Pages and Cloudflare Python workers

**Revamp BLT website with a fresh, modern design by removing non-core components to create a clear, enjoyable user experience focused on core value.** The project involves migrating the complete OWASP BLT platform from its current Django-based monolithic architecture to a lightweight static frontend deployed on GitHub Pages using plain HTML, vanilla JavaScript, and HTMX, with dynamic functionality powered by Cloudflare Python Workers at the edge. This migration will replace Django template rendering with modular static components and progressive enhancement, achieving sub-200ms global response times, simplified architecture, improved maintainability, and production-grade reliability while preserving full feature parity and positioning BLT as a fast, contributor-friendly reference implementation.

---

## [BLT-Preflight](https://github.com/OWASP-BLT/BLT-Preflight) : Pre-Contribution Security Intent & Risk Guidance

**Provide security intent and risk guidance before contributors submit code to prevent common mistakes and improve contributor understanding.** This pre-contribution advisory system helps contributors understand security expectations before opening a pull request by evaluating security context through issue labels, repository metadata, and historical patterns, then providing plain-language guidance linked to relevant documentation. The system includes optional contributor intent capture (planned work areas, components to modify, AI assistance usage), a maintainer visibility dashboard for early identification of risky contributions, and a learning feedback loop that refines guidance rules over time. BLT-Preflight operates on a purely advisory basis with no blocking or enforcement mechanisms, focusing on prevention and clarity to reduce maintainer workload and improve the quality of security contributions.

---

## [BLT-Rewards](https://github.com/OWASP-BLT/BLT-Rewards) : BACON Rewards & Security Contribution Gamification

**Security contribution gamification with BACON tokens, badges, reputation tiers, and leaderboards to increase contributor retention and engagement.** The system listens for verified security contributions and awards rewards idempotently including BACON cryptocurrency tokens (with existing blockchain mint infrastructure), achievement badges for different security domains, progressive reputation tiers (Beginner → Expert), severity-weighted leaderboards, and a swag redemption marketplace where tokens convert to physical merchandise. Built with robust anti-gaming architecture (idempotent rewards, fraud detection, admin oversight), the platform includes comprehensive audit trails, an education bridge API layer for learning platform integration, and tokenomics analysis to ensure long-term sustainability. BLT-Rewards transforms security work into an engaging, progression-based experience that prioritizes impact over volume while enabling education platforms to leverage BLT contribution data for personalized learning paths.

---

## [BLT-NetGuardian](https://github.com/OWASP-BLT/BLT-NetGuardian) : Distributed Autonomous Security Scanning Platform

**Community-powered security scanning platform with distributed scanning, real vulnerability detection, and responsible disclosure workflows.** NetGuardian replaces stubbed scanners with real vulnerability detection (XSS, SQLi, CSRF, security headers plus Semgrep SAST), introduces distributed scanning via secure volunteer CLI clients with local resource caps, and implements Zero-Trust encrypted ingestion where sensitive evidence stays encrypted end-to-end until authorized organization users decrypt it client-side. The platform includes result validation and false-positive filtering with confidence scoring, basic deduplication using fingerprints, triage-lite UI with evidence viewer and "Convert to Issue" workflow, security.txt detection for improved responsible disclosure, and professional remediation reports (CSV/PDF) for organizations. NetGuardian emphasizes accuracy through curated evaluation targets and rule tuning, privacy-preserving architecture with signed and timestamped submissions, and lower reviewer workload through normalized findings and streamlined triage.

---

## [BLT University](https://github.com/OWASP-BLT/BLT-University) : Security-Focused Education Platform

**Security-focused education tool that teaches users about security through hands-on, code-centric labs and community-driven knowledge sharing.** The platform transforms BLT's existing theory-heavy labs into interactive exercises where learners analyze real vulnerable code, identify security flaws, explain exploitation scenarios, and apply secure fixes using a three-step workflow (Identify → Explain → Fix) with partial credit and progress tracking. BLT University establishes a safe, anonymized security intelligence pipeline that aggregates vulnerability patterns from BLT issues/PRs into public dashboards, monthly/quarterly reports with two-person approval workflows, and remediation playbooks that convert into mini interactive challenges. The unified architecture creates a feedback loop where real vulnerability patterns improve labs and playbooks, helping contributors learn security thinking inspired by OWASP Top 10 and CTF-style reasoning, with optional integration to badges/BACON gamification and future connections to NetGuardian findings for automatically mapped learning recommendations.

---

## [BLT-MCP](https://github.com/OWASP-BLT/BLT-MCP) : Model Context Protocol Server for Complete BLT Interface

**An interface to the BLT ecosystem enabling AI agents and developers to log bugs, triage issues, query data, and manage workflows from IDEs or chat interfaces.** BLT-MCP implements the Model Context Protocol (MCP) standard to provide comprehensive, AI-agent-friendly access to all aspects of BLT through three layers: Resources (read-only access to issues, repos, contributors, workflows, leaderboards, rewards via `blt://` URIs), Tools (actions like submit_issue, award_bacon, update_issue_status, add_comment), and Prompts (reusable task templates like triage_vulnerability, plan_remediation, review_contribution). The system uses JSON-RPC 2.0 over stdio or HTTP/SSE with OAuth 2.0/API key authentication, enabling natural integration with Claude Desktop, custom AI agents, and third-party tools without requiring custom API documentation since agents discover capabilities automatically. BLT-MCP positions BLT as an AI-agent-first platform with standardized protocol access that unifies fragmented REST/GraphQL endpoints, creates novel use cases (autonomous issue triage, automated reward distribution, workflow tracking), and synergizes with other BLT ideas by exposing RAG bot capabilities, AI-guided recommendations, reputation scores, and gamification data through a single consistent interface.

---

### ✅ **Expected Results**  
- Successfully implementing a **fully functional, production-ready** feature.  
- Contributions must align with **BLT’s core security and performance goals**.  
- Code should adhere to best practices, including **security testing, CI/CD integration, and documentation**.  

---

### 📌 **Knowledge Prerequisites**  
To contribute effectively, familiarity with at least one or more of the following is recommended:  

- **Back-End:** Python, Django, Django Ninja, SQL  
- **Front-End:** HTMX, Tailwind CSS, HTML/CSS  
- **Blockchain:** Bitcoin Ordinals, Solana, Smart Contracts  
- **AI/ML:** NLP, Machine Learning for security analytics  
- **DevOps & Security:** GitHub API, REST API, OAuth, Authentication  

---

### 👥 **Mentors**  

📌 _Confirmed Mentors:_  (we're all on the OWASP Slack in the [#project-blt](https://owasp.slack.com/archives/project-blt)  channel)
- **Donnie Brown**
- **Ahmed ElSheikh**
- **Manikandan Chandran**
- **Rinkit Adhana**
- **Raj Gupta**
- **Vinamra Vaswani**
- **Carla Voorhees**
- **Jigyasu Rajput**
- **Rishab Kumar Jha**
- **Akshay Behl**


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

- improve/redesign WebUI / add a dashboard
- implement more tests, get 85% code coverage level
- implement more modules, focus on more coverage of CISA KEV CVEs
- implement external API keys configuration using a config file, API and WebUI
- implement module workflows e.g. run module B after module A only if module A returns any result/result matching condition
- improve documentation
- improve scan engine efficiency

##### Your Own Ideas
Do you have an idea to improve OWASP Nettacker?
We'd love to hear it, please reach out in OWASP Slack on channel [#project-nettacker](https://app.slack.com/client/T04T40NHX/CQZGG24FQ) to ensure that the idea fits OWASP Nettacker roadmap and goals. 

##### Getting Started

Repositories:

- [OWASP Nettacker on OWASP GitHub](https://github.com/OWASP/Nettacker)
- [Documentation](https://nettacker.readthedocs.io)
- Join OWASP Slack and contact us on channel [#project-nettacker](https://app.slack.com/client/T04T40NHX/CQZGG24FQ)

##### Knowldege  Requirements

- Python
- Flask
- HTML/CSS/JavaScript
- previous vulnerability scanning/bug bounty hunting experience, vulnerability scanning tools use (nmap, metasploit, other kali linux tools)

##### Mentors

* [Sam Stepanyan](mailto:sam.stepanyan@owasp.org)
* [Ali Razmjoo](mailto:ali.razmjoo@owasp.org)
* [Arkadii Yakovets](mailto:arkadii.yakovets@owasp.org)

### [OWASP Nest](https://nest.owasp.org)

OWASP Nest is a comprehensive, community-first platform built to enhance collaboration and contribution across the OWASP community. Acting as a central hub, it helps users discover chapters and projects, find contribution opportunities, and connect with like-minded individuals based on their interests and expertise.

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

#### Getting Started

- Check out our [contributing guidelines](https://github.com/OWASP/Nest/blob/main/CONTRIBUTING.md)
- Join OWASP Nest channel [#project-nest](https://owasp.slack.com/archives/project-nest)
- Consider `good first issue` from OWASP Nest [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3A%22good%20first%20issue%22)

#### Projects / Ideas

![Possible for "Small" GSoC 2026 project](https://img.shields.io/badge/small%20size%20(90h)-possible-green) ![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(175h)-preferred-green) ![Possible for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(350h)-possible-green)

- [OWASP Board Activity Standardization and Data Programmatic Access](https://github.com/OWASP/Nest/milestone/20): This milestone focuses on standardizing how OWASP Board activities are recorded, structured, and published.

- [OWASP Board Candidate Information Transparency and Fact-Checking](https://github.com/OWASP/Nest/milestone/19): This milestone focuses on improving the transparency, accuracy, and trustworthiness of information related to OWASP board candidates.

- [OWASP Community Snapshots](https://github.com/OWASP/Nest/milestone/16): Creating a summary of activities within OWASP projects, chapters, and events, including new blog posts and news, to keep the community informed about recent developments.

- [OWASP Contributor Recognition Program](https://github.com/OWASP/Nest/milestone/22): This milestone introduces an OWASP-wide Contributor Recognition system in OWASP Nest to make contributions visible, measurable, and shareable across projects and chapters, inspired by community platforms like ContribCard, with potential integration into existing OWASP Nest badges and certificate delivery via services like Certifier.

- [OWASP NestBot AI Assistant Improvement](https://github.com/OWASP/Nest/milestone/8): Develop an AI-powered OWASP NestBot Slack assistant that acts as an auto-responder for frequently asked questions, guides users to the appropriate OWASP channels, and handles typical OWASP community queries.

- [OWASP Nest Monitoring and Observability](https://github.com/OWASP/Nest/milestone/21): Implement modern monitoring and observability practices across OWASP Nest infrastructure on AWS to ensure reliability, performance visibility, and proactive issue detection.

- [OWASP Nest UI/UX Revamp](https://github.com/OWASP/Nest/milestone/23): This milestone delivers a comprehensive UI/UX revamp of OWASP Nest to improve usability, accessibility, visual consistency, and the overall contributor experience across the platform.

- [OWASP Pulse](https://github.com/OWASP/Nest/milestone/24): This milestone introduces the OWASP Pulse page in OWASP Nest as a unified, near real-time activity feed that aggregates events across repositories with filters by user, project, repository, and chapter to improve visibility and engagement.

Please visit our planned [milestones page](https://github.com/OWASP/Nest/milestones) or `gsoc2026` labeled [issues page](https://github.com/OWASP/Nest/issues?q=is%3Aissue%20state%3Aopen%20label%3Agsoc2026).

#### Your own ideas

Do you have an idea to improve OWASP Nest?
We'd love to hear it, please reach out in Slack to ensure that the idea fits OWASP Nest goals.

#### Expected Results

- Your proposal projects/ideas are fully completed.
- Your code follows our existing style guides and passes quality checks, test coverage, etc.

#### Mentors

Please contact [Arkadii Yakovets](https://owasp.slack.com/team/U060W3NKLTF) or [Kate Golovanova](https://owasp.slack.com/team/U07PWB1JZ6Z) if you're interested in participating as a mentor.

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/arkid15r.png" alt="Arkadii Yakovets" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Arkadii Yakovets</strong><br>
Cybersecurity Lead, CCSP, CISSP, CSSLP | OWASP Nest Project Leader<br>
<i class="fab fa-github"></i> <a href="https://github.com/arkid15r/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/arkid15r/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U060W3NKLTF">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/ioleksiuk.png" alt="Illia Oleksiuk" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Illia Oleksiuk</strong><br>
DevOps Engineer at Pow.bio<br>
<i class="fab fa-github"></i> <a href="https://github.com/ioleksiuk">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/ioleksiuk/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0AAP59RN87">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/emaybu.png" alt="Ime Iyonsi" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Ime Iyonsi</strong><br>
Software Engineer / Application Security Engineer, CC, GSEC<br>
<i class="fab fa-github"></i> <a href="https://github.com/emaybu/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://linkedin.com/in/imeiyonsi/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U06H942K9UY">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kasya.png" alt="Kateryna Golovanova" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kate Golovanova</strong><br>
Senior Software Engineer at Skill Struck, CC | OWASP Nest Project Leader<br>
<i class="fab fa-github"></i> <a href="https://github.com/kasya/">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kate-golovanova/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U07PWB1JZ6Z">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kerlynNkep.png" alt="Kerlyn Manyi" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kerlyn Manyi</strong><br>
Cybersecurity Engineer | GSoC'25 mentor at Mifos Initiative<br>
<i class="fab fa-github"></i> <a href="https://github.com/kerlynNkep">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kerlyn-manyi-a80201123/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U06M01ARG3V">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/theinfosecguy.png" alt="Keshav Malik" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Keshav Malik</strong><br>
Senior Security Engineer at LinkedIn<br>
<i class="fab fa-github"></i> <a href="https://github.com/theinfosecguy">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/keshav-malik/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0AB7UGB1NV">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/kritibirda.png" alt="Kriti Birda" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Kriti Birda</strong><br>
AI/ML enthusiast | GSoC'25 contributor at PSF<br>
<i class="fab fa-github"></i> <a href="https://github.com/kritibirda">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/kritibirda/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U08KZ9Z7MFX">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/TheCyberLeader.png" alt="Marie Wang" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Marie Wang</strong><br>
Senior GRC & Technology Risk Leader, CISSP<br>
<i class="fab fa-github"></i> <a href="https://github.com/TheCyberLeader">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/mariezw/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0A23223B8B">Slack</a>
</div>
</div>

<div style="margin-bottom: 20px; display: flex; align-items: center;">
<img src="https://github.com/noland-crane.png" alt="Noland Crane" width="64" height="64" style="border-radius: 50%; margin-right: 12px; flex-shrink: 0;" />
<div>
<strong>Noland Crane</strong><br>
Application Security Analyst at Bloomreach, CISSP<br>
<i class="fab fa-github"></i> <a href="https://github.com/noland-crane">GitHub</a> &bull; <i class="fab fa-linkedin"></i> <a href="https://www.linkedin.com/in/nolandcrane/">LinkedIn</a> &bull; <i class="fab fa-slack"></i> <a href="https://owasp.slack.com/team/U0ABF22MQ2Z">Slack</a>
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
- Add interactive dashboard for user performance and completion status.
- UI consistency
- Expand challenge section and playgrounds.
- Extend labs to other languages as well.
- Prepare for `OWASP Top 10:2026` section

#### Mentors
- [ardiansyah](mailto:pakdesawangan@gmail.com)
- [Rupak Biswas](https://github.com/RupakBiswas-2304)([Rupak](https://owasp.slack.com/team/U036WSR1684) on slack)
- [Garvita Kataria](https://github.com/Garvita-k) ([Slack](https://owasp.slack.com/team/U08BJEKS5KQ))

  
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

---

#### 🔹 **OpenCRE Scraper & Indexer (Project OIE) - Module Projects**

The OpenCRE Scraper & Indexer is an autonomous ETL pipeline that ingests OWASP security knowledge from various sources, filters noise, and links content to the OpenCRE knowledge graph. This project consists of four independent modules, each suitable for a GSoC project.

**Important Requirements:**
- **Contributor Eligibility**: Applicants must have **at least 3 merged pull requests** to the OpenCRE repository before GSoC selection. This demonstrates familiarity with the codebase, contribution workflow, and project standards.
- **Code of Conduct**: All contributors must read and agree to follow the [OpenCRE Code of Conduct](https://github.com/OWASP/OpenCRE/blob/main/CODE_OF_CONDUCT.md). Violations will result in immediate project termination.
- **Pre-Code Experiments**: Each module requires completion of specific pre-code experiments before implementation begins. These experiments validate the approach and ensure technical feasibility.

For detailed architecture and requirements, see the [RFC: The OpenCRE Scraper & Indexer](https://raw.githubusercontent.com/OWASP/OpenCRE/1539e0a209b7891c2363b4aa9be407cad87fe319/docs/designs/owasp-pane-of-glass.md).

---

##### 🔸 **Module A: Information Harvesting**

![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)

**Primary Objectives:**
- Build a GitHub Actions-based cron job that runs nightly at 02:00 UTC
- Implement a config reader that parses a `repos.yaml` file containing a list of high-value OWASP repositories (ASVS, WSTG, etc.)
- Develop a diff fetcher that uses `git log --since="24h"` to identify changes in the last 24 hours
- Create a temporary storage system (Raw Change Bucket) to store raw diffs before processing
- Handle GitHub API rate limits gracefully
- Parse files to extract meaningful text changes (not raw diff syntax)

**Technical Requirements:**
- **Tech Stack**: Python (requests, PyGithub), GitHub Actions (Cron)
- **Pre-Code Experiment**: 
  - Manually inspect 10 random OWASP repositories to identify common junk files (package-lock.json, CNAME, _config.yml, etc.)
  - Create a regex exclusion list that eliminates 90% of noise without downloading files
  - Write a 10-line script to fetch only modified paragraphs from a large Markdown file using git diff, returning clean text (not raw diff syntax)

**Expected Results:**
- A production-ready GitHub Action that runs nightly
- Configurable repository list via YAML
- Efficient diff extraction that filters out noise files
- Comprehensive error handling and logging
- Unit tests with >70% code coverage
- Documentation for configuration and maintenance

**Difficulty Characterization:**
This is a **Medium** difficulty project requiring:
- Understanding of GitHub API and rate limiting
- Git operations and diff parsing
- YAML configuration parsing
- GitHub Actions workflow development
- Incremental crawling strategies

---

##### 🔸 **Module B: Noise/Relevance Filter**

![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

**Primary Objectives:**
- Implement a two-stage filtering system: regex-based filtering followed by LLM-based relevance checking
- Create regex filters to reject common noise files (*.css, lockfiles, tests/, etc.)
- Integrate with managed LLM APIs (Gemini Flash or GPT-4o-mini) for semantic relevance checking
- Design and tune prompts to accurately identify security knowledge vs. noise (formatting, linting, bureaucracy)
- Build a knowledge queue system that routes relevant content to Module C

**Technical Requirements:**
- **Tech Stack**: Python (langchain or raw API calls), Managed LLM APIs (Gemini Flash/GPT-4o-mini)
- **Pre-Code Experiment**:
  - Extract 100 real commit messages/diffs from OWASP repositories
  - Manually tag them in a spreadsheet: Relevant (Security Info) vs Noise (Typos, Admin, Formatting)
  - Run these 100 items through the proposed LLM prompt
  - Success Criteria: LLM must match manual tags >97% of the time

**Expected Results:**
- A filtering pipeline that processes raw changes and outputs relevant security knowledge
- Tuned LLM prompts with >97% accuracy on validation dataset
- Cost-effective implementation using managed LLM APIs
- Comprehensive logging of filtered vs. accepted content
- Unit tests with >70% code coverage
- Documentation of prompt engineering process and results

**Difficulty Characterization:**
This is an **Easy** difficulty project suitable for:
- Entry-level developers interested in prompt engineering
- Developers comfortable with API integration
- Those who enjoy iterative prompt tuning ("vibe coding")
- No advanced ML knowledge required

---

##### 🔸 **Module C: The Librarian (Smart Content Mapping)**

![Preferred for "Large" GSoC 2026 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

**Primary Objectives:**
- Implement a two-stage retrieval system: vector search (bi-encoder) followed by cross-encoder re-ranking
- Set up vector search using pgvector to retrieve top 20 candidate CRE nodes
- Integrate sentence-transformers library with ms-marco-MiniLM-L-6-v2 model for cross-encoder re-ranking
- Handle the "Negation Problem" (e.g., "Do NOT use MD5" should map correctly)
- Implement update detection logic to identify when content is an update to existing content
- Add security gates to detect adversarial updates or contradictions to previous content
- Set threshold-based routing: score > 0.8 links to CRE, score < 0.8 flags for human review

**Technical Requirements:**
- **Tech Stack**: sentence-transformers (HuggingFace), pgvector, Python
- **Prerequisites**: Understanding of Embeddings, Bi-Encoders vs Cross-Encoders, Vector Similarity
- **Pre-Code Experiment**:
  - Select 50 random ASVS requirements and strip metadata
  - Feed them into basic Vector Search (Cosine Similarity)
  - Check mapping accuracy to correct CRE nodes
  - Run through Cross-Encoder and compare results
  - Success Criteria: Cross-Encoder must show 20% accuracy improvement over Cosine Similarity, especially for "Negative" requirements

**Expected Results:**
- Production-ready content mapping system with >80% accuracy on validation dataset
- Vector search integration with pgvector
- Cross-encoder re-ranking pipeline
- Update detection and security gate implementation
- Comprehensive evaluation metrics and logging
- Unit tests with >70% code coverage
- Documentation of model selection, tuning process, and accuracy metrics

**Difficulty Characterization:**
This is a **Hard** difficulty project requiring:
- Deep understanding of embeddings and semantic similarity
- Experience with vector databases (pgvector)
- Knowledge of bi-encoders vs cross-encoders
- Ability to tune thresholds and evaluate model performance
- Understanding of information retrieval concepts
- Strong Python skills for ML/AI integration

**Bonus/Pro-Mode**: Implement Hybrid Search (Vector + Keyword/BM25) for exact keyword matching (e.g., CVE IDs).

---

##### 🔸 **Module D: Human-in-the-Loop (HITL) & Logging**

![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-green)

**Primary Objectives:**
- Build a simple admin UI for reviewing flagged content from Module C
- Implement a fast review interface optimized for "Tinder-swipe" speed (keybind 'y' for yes, 'n' for no)
- Create a logging system that appends corrections to JSONL files (stored in S3/MinIO)
- Design the UI to allow review, approve/reject, and save corrections in under 3 seconds per item
- Implement user authentication and authorization for maintainers
- Build a dashboard showing review queue status and statistics

**Technical Requirements:**
- **Tech Stack**: Flask/React, S3/MinIO for storage
- **Pre-Code Experiment**:
  - Draw wireframe or build 10-line HTML prototype
  - Test: Can a user review, approve/reject, and save a correction in under 3 seconds per item?
  - Success Criteria: UI must require minimal clicks (ideally keyboard shortcuts)

**Expected Results:**
- A production-ready admin UI for content review
- Fast, keyboard-optimized review workflow
- JSONL logging system integrated with S3/MinIO
- User authentication and role-based access control
- Review queue dashboard with statistics
- Unit tests with >70% code coverage
- Documentation for maintainers

**Difficulty Characterization:**
This is an **Easy** difficulty project suitable for:
- Junior developers or frontend contributors
- Developers comfortable with standard CRUD web applications
- Those interested in UX optimization
- Full-stack developers (Flask + React)

**Bonus/Pro-Mode**: Implement "Loss Warehousing" to capture structured loss events (Input + Wrong Prediction + Correct Label) for future model retraining.

---
  
#### Mentors

**For OpenCRE Scraper & Indexer (Project OIE) Module Projects (A, B, C, D):**
- [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org)
- [Rob Van Der Veer](mailto:rob.van.der.veer@owasp.org)
- [Paola Gardenas](mailto:paola.gardenas@owasp.org)
- [Parth Sohaney](mailto:parth.sohaney@owasp.org)


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

### [OWASP Cornucopia](https://cornucopia.owasp.org/)

#### Repository
- [OWASP Cornucopia]([https://github.com/adeyosemanputra/pygoat](https://github.com/owasp/cornucopia))

#### Skills Required
- HTML/CSS/JavaScript
- Python
- Docker
- No security knowledge required

##### Getting started
- Check[GitHub project]([https://github.com/adeyosemanputra/pygoat](https://github.com/owasp/cornucopia?tab=readme-ov-file#building-and-deploying-the-cornucopia-website))
- Get in touch with one of the project leaders [Sydseter](https://www.linkedin.com/in/sydseter/)
- Join [OWASP Slack](https://owasp.org/slack/invite) and contact us on channel #cornucopia-project

#### Projects / Ideas
![Preferred for "Medium" GSoC 2026 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
- Ensure the OWASP Cornucopia converter can create print-ready proofs for print-on-demand jobs. See: [Description](https://github.com/OWASP/cornucopia/issues/583).
- Add the EoP Game to the card browser. See: [Description](https://github.com/OWASP/cornucopia/issues/1322).
- Redesign for cornucopia.owasp.org. See: [Description](https://github.com/OWASP/cornucopia/issues/2194).

#### Mentors
- [Johan Sydseter](mailto:johan.sydseter@owasp.com)
- [Colin Watson](colin.watson@owasp.org)
