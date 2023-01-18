---
layout: full-width
title: GSoC 2023 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2023ideas
---

# {{page.title}}

[ZAP](#owaspzap) | [Bug Logging Tool (BLT)](#bug-logging-tool-blt) | [Maryam](#owaspmaryam)

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

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

Import PCAP/PCAPNG Files into ZAP as per [#4812](https://github.com/zaproxy/zaproxy/issues/4812)

##### Browser Recorder

![Not recommended for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Create a new browser extension using Type Script which will allow the user to record and replay browser interactions, for example during authentication as per [#7139](https://github.com/zaproxy/zaproxy/issues/7139)

##### Your Own Idea

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

We are always delighted to hear from contributors who have their own ideas for projects. You are encouraged to discuss these with the ZAP project leaders.

##### Mentors

All ZAP projects will be mentored by the ZAP Project Leaders:

* [Simon Bennetts](mailto:psiinon@gmail.com)
* Rick Mitchell
* thc202


### [Bug Logging Tool (BLT)](https://owasp.org/www-project-bug-logging-tool/)

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Possible for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-possible-yellow)

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
* Please submit your proposal on the BLT GitHub discussion board.  Because it will be easier for the team to review and give feedback there.
* Team meetings are every Saturday at 1pm EST.  Check Slack for the google meet link.

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

### [OWASP Maryam](https://owasp.org/www-project-maryam/)

OWASP Maryam is a modular/optional open source framework based on OSINT and data gathering. Maryam is written in Python programming language and it’s designed to provide a powerful environment to harvest data from open sources and search engines and collect data quickly and thoroughly.

Please see [Development Guide](https://github.com/saeeddhqan/maryam/wiki/Development-Guide).

##### Web interface for meta searcher

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)

Implement a web interface for Iris module with JQuery. The interface is somehow like www.qwant.com.


##### Document Retrieval for Iris

![Not recommended for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-not%20recommended-red)
![Preferred for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

Implement a Document Retrieval Algorithm for Iris in order to rank web pages according to the Query.
You need to Understand Machine Learning classic algorithms for document retrieval or use Deep neural networks for 
implementation.

##### Your Own Idea

![Preferred for "Medium" GSoC 2023 project](https://img.shields.io/badge/medium%20size%20(~175h)-preferred-green)
![Preferred for "Large" GSoC 2023 project](https://img.shields.io/badge/large%20size%20(~350h)-preferred-green)

![Difficulty: Easy](https://img.shields.io/badge/difficulty-easy-yellow)
![Difficulty: Medium](https://img.shields.io/badge/difficulty-medium-orange)
![Difficulty: Hard](https://img.shields.io/badge/difficulty-hard-red)

If you have a new Idea regarding Iris(Meta searcher), let us chat.

##### Getting Started

* [OWASP Maryam](https://github.com/saeeddhqan/Maryam)
* [Documentation](https://github.com/saeeddhqan/Maryam/wiki)


##### Mentors

* [Saeed Dehqan](mailto:saeed.dehghan@owasp.org)
