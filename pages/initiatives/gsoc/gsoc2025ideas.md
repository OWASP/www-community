---
layout: full-width
title: GSoC 2025 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2025ideas
---

# {{page.title}}

[Bug Logging Tool (BLT)](#bug-logging-tool-blt) &bull; [DevSecOps Maturity Model](#owaspdevsecops-maturity-model) &bull; [OWASP Website](#owasp-website) &bull; [OWASP Nest](#owasp-nest)


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

OWASP BLT is a _bug-hunting & logging_ tool which allows users and companies to hunt for bugs, claim bug bounties and also to start bug-hunting sprees/contests respectively. It is preferred if the potential GSoC contributors get at least 5 PRs merged for the project. Preference will be given to students
who get the most work done, and this is usually by submitting the most PRs.

##### 2025 GSOC Ideas / Projects

1. **Redesign with Dark Mode** – A UI/UX overhaul using Tailwind, potentially Figma files, and HTML implementation to create a modern, accessible design with dark mode as the default.  

2. **BLT Light Front-End in React** – A lightweight React-based front-end designed to stay under 100MB, ensuring high performance and accessibility with an optimized component structure.  

3. **Organization Dashboard – Better Integration Between Website & Orgs** – Enhancing the organization dashboard to allow management of vulnerability reports, bug reports, contributor metrics, and various content types for better oversight.  

4. **Full API with Security Tests and Definitions to Support New Light Front-End (Migrate to Django Ninja?)** – Developing a secure, well-documented API with automated security tests to support the new front-end, potentially migrating to Django Ninja for improved performance and maintainability.  

5. **Gamification and Integration with Ordinals & Solana (Combined with GitHub-Integrated Contribution Tracking)** – A GitHub-integrated platform that tracks open-source contributions and rewards users with Bitcoin Ordinals and Solana-based incentives, introducing gamification elements like badges and leaderboards.  

6. **Bid on Issues (Using Bitcoin Cash, No BLT Financial Transactions)** – A decentralized bidding system where developers can bid on GitHub issues using Bitcoin Cash, with a verification system ensuring direct fund transfers between project owners and contributors without BLT handling transactions.  

7. **Build the Flagship** – A comprehensive effort to gather information, refine platform features, ensure compliance, and collaborate with the board, executive director, and project committee to establish BLT's flagship product.  

8. **Slack Bot Enhancements – Integrate More Features** – Expanding the Slack bot's functionality to integrate more features from the website, enabling better automation, notifications, and user interactions.  

9. **AI-Driven Open-Source Grant & Funding Tracker** – A platform that helps OWASP projects and other open-source initiatives discover, apply for, and manage grant and funding opportunities using AI-powered recommendations.  

10. **AI-Powered Open-Source Code Review & Quality Assurance Bot** – A GitHub-integrated AI assistant that analyzes pull requests, detects security vulnerabilities and inefficiencies, and provides actionable code improvement suggestions.  

11. **A Smart Prioritization System for Open-Source Maintainers** – A system that prioritizes GitHub issues based on best open-source value, community needs, urgency, and dependencies, assisting maintainers in resolving critical tasks efficiently.

More projects here: https://github.com/OWASP-BLT/BLT/milestones


#### Expected Results

* We would expect that any projects you choose to include in your proposal are fully completed.


#### Knowledge Prerequisites

* Python / Django 
* Flutter
* Blockchain / Bitcoin / Ordinals / Solana / NFT
* UI / UX design
* React

##### Mentors
* Donnie (@DonnieBLT on Slack)
* Yash Pandey
* Bishal Das
* Ahmed ElSheikh
* Patricia Waiyego
* looking for 5 more mentors this year (if you are knowledgeable in any of the prerequisites and can review PRs, you can watch any of our videos https://blt.owasp.org/bltv/ and be up to speed and ready to mentor)

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

### [OWASP Website](https://owasp.org)

This project for Google Summer of Code (GSoC) aims to enhance the OWASP website by improving its mobile responsiveness, updating its styling, and refining navigation for a more modern and user-friendly experience. Key objectives include revamping the project’s and chapter’s discovery features to make them more intuitive and accessible, creating comprehensive “Getting Started” pages to guide new users, and streamlining the site’s overall structure to ensure it is well-organized and easy to maintain. The project will focus on delivering a clean, cohesive design that aligns with current web standards, improving accessibility and usability across all devices.

#### knowledge required

Jekyl

#### Mentors

DonnieBLT on Slack
(looking for more mentors, signup here)

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
