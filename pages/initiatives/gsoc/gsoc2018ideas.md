---
layout: full-width
title: GSoC 2018 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2018ideas
---

# GSoC 2018 Ideas

OWASP Foundation has been selected as an organization to be part of the GOOGLE SUMMER CODE 2018

## OWASP Project Requests

### Tips to get you started in no particular order:

* Read [Google Summer of Code Program(GSOC)](https://developers.google.com/open-source/gsoc/)
* Read the [GSoC SAT](gsoc_sat)
* Read the GSOC Student Guidelines
* Contact us through the mailing list or irc channel.
* Check our [github organization](https://github.com/OWASP)

## OWASP ZAP

 OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers. Previous GSoC students have implemented key parts of the ZAP core 
 functionality and have been offered (and accepted) jobs based on their work on ZAP.

We have just included a few of the ideas we have here, for a more complete list see the issues on the ZAP bug tracker with the [project)[https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3Aproject) label.

### Active Scanning WebSockets

#### Brief Explanation:

ZAP has good support for websockets, and allows them to be intercepted, changed and fuzzed. Unfortunately it doesnt current support active scanning (automated attacking) of websockets.

We would like to add active scanning support to websockets, ideally in a generic way which would allow us to reuse as many of our existing rules as are relevant. Adding additional websocket specific attacks would 
also be very useful.

#### Expected Results:

* An plugable infrastructure that allows us to active scan websockets
* Converting the relevant existing scan rules to work with websockets
* Implementing new websocket specific scan rules

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  React Handling  

#### Brief Explanation:

ZAP doesnt understand React applications as well as it should be able to.

It would be great if ZAP had a much better understanding of such applications, including how to explore and attack them more effectively.

#### Expected Results:

* ZAP able to explore React applications more effectively
* ZAP able to attack React applications more effectively

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* As React is written in JavaScript, good knowledge of this language is recommended. ZAP is written in Java, so some knowledge of this language would be useful. Some knowledge of application security would be useful, but 
not essential.

#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  Backslash Powered Scanner 

#### Brief Explanation:

This is a brand new technique developed by one of the Burp guys: http://blog.portswigger.net/2016/11/backslash-powered-scanning-hunting.html
Their implementation is open source: https://github.com/PortSwigger/backslash-powered-scanner so hopefully shouldn't be too hard to port to ZAP :)

#### Expected Results

* Extend ZAP's active scanner to leverage Backslash type scanning. (Including adapting some of the existing scan rules to leverage the new component.)
* Code that conforms to our [https://github.com/zaproxy/zaproxy/wiki/DevGuidelines Development Rules and Guidelines]
 **Note** This issue was previously undertaken, however, only partial progress was made. The [Pull Request](https://github.com/zaproxy/zap-extensions/pull/1014) is still open and can be built upon. The 2018 effort needs to 
 ensure the code builds and is successfully put to use in some of the existing scan rules and unit tests.

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be very useful.

#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  Automated authentication detection and configuration  

#### Brief Explanation:

Currently a user must manually configure ZAP to handle authentication, eg as per https://github.com/zaproxy/zaproxy/wiki/FAQformauth

This is time consuming and error prone.

Ideally ZAP would help detect login and registration pages and provide more assistance when configuring authentication, ideally being able to completely automate the task for as many sort of webapps as possible.

#### Expected Results:
* Detect login and registration pages
* Provide a wizard to walk users through the process of setting up authentication, with as much assistance as possible
* An option to completely automate the authentication process, for as many authentication mechanisms as possible

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.
#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  Zest Text Representation and Parser 
#### Brief Explanation:

Zest is a graphical scripting language from the Mozilla Security team, and is used as the ZAP macro language.

A standardized text representation and parser would be very useful and help its adoption.

#### Expected Results:
* A documented definition of a text representation for Zest
* A parser that converts the text representation into a working Zest script
* An option in the Zest java implementation to output Zest scripts text format

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* The Zest reference implementation is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.
#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  Develop Bamboo Addon 
#### Brief Explanation:

It would be great to have an official ZAP add-on for [Bamboo](https://www.atlassian.com/software/bamboo), equivalent to the one we now have for [Jenkins](https://plugins.jenkins.io/zap/)

For more information about Bamboo plugins see the [Bamboo plugin guide](https://developer.atlassian.com/server/bamboo/bamboo-plugin-guide/).

#### Expected Results:

A Bamboo addon that supports:
* Spidering (using the traditional and Ajax spiders)
* Active Scanning
* Authentication

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* ZAP and Bamboo are written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.
#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

###  Your Idea 
#### Brief Explanation:

ZAP is a great framework for building new and innovative security testing solutions. If you have an idea that is not on this list then don't worry, you can still submit it, we have accepted original projects in 
previous years and have even paid a student to work on their idea when we did not get enough GSoC slots to accept all of the projects we wanted.

#### Expected Results:
* A new feature that makes ZAP even better
* Code that conforms to our Development Rules and Guidelines

#### Getting started:

* Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding section.
* We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

* ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.
#### Mentors:

Simon Benetts and the rest of the ZAP Core Team

##  OWASP Juice Shop 

OWASP Juice Shop Project is an intentionally insecure webapp for security trainings written entirely in Javascript which encompasses the entire OWASP Top Ten and other severe security flaws. Juice Shop is written in 
Node.js, Express and AngularJS. The application contains more than 30 challenges of varying difficulty where the user is supposed to exploit the underlying vulnerabilities. Apart from the hacker and awareness training use 
case, pentesting proxies or security scanners can use Juice Shop as a "guinea pig"-application to check how well their tools cope with Javascript-heavy application frontends and REST APIs.
 The best way to get in touch with us is the community chat on https://gitter.im/bkimminich/juice-shop. You can also send PMs to the mentors (@bkimminich, @wurstbrot and @J12934) there if you like!

 To receive early feedback please put your proposal on Google Docs and submit it to the OWASP Organization on Google's GSoC page in Draft Shared mode. Please pick juice shop as Proposal Tag to make them 
 easier to find for us. Thank you!

###  Challenge Pack 2018 

#### Brief Explanation:

Ideas for potential new hacking challenges are collected in [GitHub issues labeled "challenge"](https://github.com/bkimminich/juice-shop/issues?q=is%3Aissue+is%3Aopen+label%3Achallenge). This project could implement a whole 
bunch of challenges one by one and release them over the course of several small releases. This would allow the student to work in a professional Continuous Delivery kind of way while bringing benefit to the Juice Shop over 
the duration of the project.

Coming up with additional ideas for challenges would be part of the project scope, as the list of pre-existing ideas might not be sufficient for a GSoC project.

#### Expected Results:

* 10 or more new challenges for OWASP Juice Shop (including required functional enhancements to place the challenges in, e.g. the [Order Dashboard](https://github.com/bkimminich/juice-shop/issues/244) user story])
* Each challenge comes with full functional unit and integration tests
* Each challenge is verified to be exploitable by corresponding end-to-end tests
* Hint and solution sections for each new challenge are added to the "Pwning OWASP Juice Shop" ebook
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Getting started:

* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

#### Knowledge Prerequisites:

* Javascript, Unit/Integration testing, experience with (or willingness to learn) AngularJS (1.x) and NodeJS/Express, some security knowledge would be preferable.

#### Mentors:

* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Timo Pagel - OWASP Juice Shop Project Collaborator
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator

###  Frontend Technology Update 

#### Brief Explanation:

Development of OWASP Juice Shop started in 2014 and was based on - back then - quite recent Javascript frontend framework AngularJS 1.x along with Bootstrap 3. Several major releases later, there now 
are [Angular 5](https://github.com/bkimminich/juice-shop/issues/165) and [Bootstrap 4](https://github.com/bkimminich/juice-shop/issues/400) available as well as other mature web frontend frameworks. 
Migrating the OWASP Juice Shop to the latest version of Angular and Bootstrap is an important step to keep the application relevant as the most modern intentionally broken web application. Moving to entirely 
different frameworks might be taken into considerationas well.

#### Expected Results:

* High-level target client-architecture overview including a migration plan with intermediary milestones
* Execution of migration without breaking functionality or losing tests along the way
* Code follows existing (or new) styleguides and passes all existing (or new) quality gates regarding code smells, test coverage etc.

#### Getting started:

* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

#### Knowledge Prerequisites:

* Javascript, experience with latest Javascript frameworks for frontend, testing and building

Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator

###  UI/Graphics Design Update 

#### Brief Explanation:

The UI of OWASP Juice Shop was written following recommendations from Twitter Bootstrap to be responsive, but it never had an actual designer or graphics artist take a look or add some insight. Currently the look & feel comes "out of the box" from a [https://bootswatch.com Bootswatch] theme and [https://fontawesome.com Font Awesome 5] icons. This gives it a quite modern look, but also leaves it very generic. The project could greatly benefit from involvement of someone with actual UI/UX Design expertise. Having a matching theme for [https://ctfd.io CTFd] would be another big achievement for the Juice Shop.

#### Expected Results:
* Design concepts to pick or have the user community vote on (including color schemes, sample screens, icons etc.)
* Overhauling the overall UI look & feel, e.g. by making an individual Bootswatch theme or designing some individual icons
* <del>Getting rid of the stock images by providing individually designed product images for the standard inventory of the shop</del> ([#315](https://github.com/bkimminich/juice-shop/issues/315) in progress)
* Add more flexibility and options to the existing theming/customization of the UI (see [#379](https://github.com/bkimminich/juice-shop/issues/379))
* Design a ["Juice Shop" CTFd-theme](https://github.com/bkimminich/juice-shop-ctf/issues/9) playing well with the look & feel of the application
* Execution of migration without breaking functionality or client-side unit and end-to-end tests along the way

#### Getting started:

* Get familiar with the existing HTML views and CSS of the frontend
* Get a feeling for the high quality bar by inspecting the existing client-side unit and e2e test suites

#### Knowledge Prerequisites:

* Strong web and graphic design experience
* Sophisticated HTML and CSS experience

Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Timo Pagel - OWASP Juice Shop Project Collaborator
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator

###  Your idea 

#### Brief Explanation:

You have an awesome idea to improve OWASP Juice Shop that is not on this list? Great, please submit it!

#### Getting started
 
* Get in touch with [Bjoern Kimminich

#### Expected Results:

* A new feature that makes OWASP Juice Shop even better
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Knowledge Prerequisites:

* Javascript, Unit/Integration testing, experience with (or willingness to learn) AngularJS and NodeJS/Express, some security knowledge would be preferable.

#### Mentors:

* Bjoern Kimminich - OWASP Juice Shop Project Leader

## OWASP Security Knowledge Framework - Chatbot machine learning feature

####  Brief Explanation 

We want to create a SKF Chatbot service using the knowledge already inside SKF like the knowledge base items, code examples and the security controls like ASVS and PCI DSS.
The chatbot service and core of this new feature can be consumed by website’s as an addon, IDE of developers and website chat channels like Gitter.im.
The core of the SKF Chatbot will be using machine learning to accomplish the hard task of correlating data and merging different sources as a response/answer.

####  Expected Results 

 A Defined Knowledge Base (Data Structure / DB) which can be used to define and search for entities. For example: if a query is:
 How to mitigate CSRF in PHP   the system should be able to understand or translate it to:  {How: intent} to {mitigate: solution} {CSRF: attack} in {PHP: programming language}  This kind of query can be further user to 
 fetch right information in the knowledge base and provide right solution (code example) for mitigating CSRF in PHP.
 What is CSRF?   the system should be able to understand or translate it to:  {What: intent} is {CSRF: attack/defense}  This kind of query can be further user to fetch right information in the knowledge base that 
 explains CSRF and provide the security control from example ASVS
 An ETL process to convert existing SKF Knowledge data and ASVS data to above mentioned data structure.
 A Chatbot (using existing frameworks) to:
 Understand at least two intent like (How to, What is …..) and be able to enrich the user query as mentioned above.
 Based on enriched query fetch relevant information from knowledge base and return.
 An integration to some chat system like Gitter.im, IRC, Slack etc.

####  Knowledge Prerequisites

* Programming languages:
  * OWASP-SKF API is build in Python 3.6/3.7
  * OWASP-SKF Frontend is build with Angular 4 TS
* Machine learning enthusiastic/interest

####  Proposal from student 

* We want to ask from the student to write a proposal on how to approach the problem we described.

#### Mentors:

Riccardo ten Cate, Glenn ten Cate, Minhaz

## OWASP Nettacker

### Brief Explanation
OWASP Nettacker project is created to automate information gathering, vulnerability scanning and eventually generating a report for networks, including services, bugs, vulnerabilities, misconfigurations, and other information. 
This software will utilize TCP SYN, ACK, ICMP and many other protocols in order to detect and bypass Firewall/IDS/IPS devices. By leveraging a unique method in OWASP Nettacker for discovering protected services and devices 
such as SCADA. It would make a competitive edge compared to other scanner making it one of the bests.

if you need more details please visit the [GitHub page](https://github.com/viraintel/OWASP-Nettacker) or contact a leader (Ali Razmjoo Qalaei, Reza Espargham).

#### Getting started

* You may read the available documents in the [wiki page](https://github.com/viraintel/OWASP-Nettacker/wiki). Developers and users documents are separated.

A Better Penetration Testing Automated Framework

#### Expected Results

The expected results are to contribute the OWASP Nettacker framework [issues](https://github.com/viraintel/OWASP-Nettacker/issues) (mostly help wanted or enhancement). Please check the GitHub repo to learn more.

#### Knowledge Prerequisites

* The whole framework was written in Python language. You must be familiar with Python 2.x, 3.x.
* Good knowledge of computer security (and penetration testing)
* Knowledge of OS (Linux, Windows, Mac...) and Services
* Familiar with IDS/IPS/Firewalls and ...
* To develop the API you should be familiar with HTTP, Database...

#### Mentors

Mentors are: Ali Razmjoo Qalaei, Abbas Naderi Afooshteh, SRI HARSHA Gajavalli

## OWASP OWTF

[Offensive Web Testing Framework (OWTF)](https://github.com/owtf/owtf) is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide (v3 and v4), 
the OWASP Top 10, PTES and NIST. Most of the ideas below focus on rewrite of some major components of OWTF to make it more modular. OWTF is moving to a fresh codebase with a fully Docker testing and deployment environment. 
If you want to get a jumpstart, check out https://github.com/owtf/owtf/tree/new.

### OWASP OWTF - MiTM proxy interception and replay capabilities

#### Brief Explanation:

The OWTF man-in-the-middle proxy is written completely in Python (based on the excellent Tornado framework) and was benchmarked to be the fastest MiTM python proxy. However it lacks the useful and much need interception and 
replay capabilities of mitmproxy (https://github.com/mitmproxy/mitmproxy).

The current implementation of the MiTM proxy serves its purpose very well. Its fast but its not extensible. There are a number of good use cases for being extensible
*ability to intercept the transactions
*modify or replay transaction on the fly
*add additional capabilities to the proxy (such as session marking/changing) without polluting the main proxy code
Bonus:
*Design and implement a proxy plugin (middleware) architecture so that the plugins can be defined separately and the user can choose what plugins to include dynamically (from the web interface).
*Replace the current Requester (based on urllib, urllib2) with a more robust Requester based on the new urllib3 with support for a real headless browser factory. The typical flow when requested for an authenticated browser 
instance (using PhantomJS)

*The "Requester" module checks if there is any login parameters provided (i.e form-based or script - look at https://github.com/owtf/login-sessions-plugin)
*Create a browser instance and do the necessary login procedure
*Handle the browser for the URI
*When called to close the browser, do a clean logout and kill the browser instance.

#### Expected Results:

*IMPORTANT: [compliant code PEP-8](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
*IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
*IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
*CRITICAL: Excellent reliability
*Good performance
*Unit tests / Functional tests
*Good documentation
Knowledge Prerequisite: Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

OWASP OWTF Mentors: Contact: Abraham Aranguren,Viyat Bhalodia,Bharadwaj Machiraju OWASP OWTF Project Leaders

### OWASP OWTF - Web interface enhancements

#### Brief Explanation:

The current web interface is a mixture of Tornado Jinja templates and ReactJS. A complete UI change to a stable ReactJS-based interface should be the deliverable for this project.  Most of the hard part for the change has 
already been done and added in a separate branch at https://github.com/owtf/owtf/tree/develop.

For background on OWASP OWTF please see: https://www.owasp.org/index.php/OWASP_OWTF

#### Expected Results:

*IMPORTANT:Clean, maintainable (ES6 compatible and using recommended design patterns) React (JavaScript) code. ([This](https://github.com/getsentry/zeus/tree/master/webapp) is a good example!)
*IMPORTANT: Thoroughly documented code along with API examples and example future components.
*CRITICAL: Excellent reliability and performance.
*Unit tests / Functional tests and easy to setup testing environment (preferably automated).

#### Knowledge Prerequisite: 

Python (reading API source code and endpoints), React.JS (high proficiency) and general JavaScript proficiency.

OWASP OWTF Mentors: Contact: Abraham Aranguren,Viyat Bhalodia,Bharadwaj Machiraju OWASP OWTF Project Leaders

### OWASP OWTF - New plugin architecture

#### Brief Explanation:

The current plugin system is not very useful and it is painful to browse many plugins. Most of the plugins do have much code and most of is repeated - much refactoring needed there.

This issue is documented in detail at https://github.com/owtf/owtf/issues/905.

For background on OWASP OWTF please see: https://www.owasp.org/index.php/OWASP_OWTF

#### Expected Results:

*IMPORTANT: [compliant code PEP-8](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
*IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
*IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
*CRITICAL: Excellent reliability
*Good performance
*Unit tests / Functional tests
*Good documentation

##  OWASP CSRF Protector 

OWASP CSRF Protector Project is a project started with the goal to help developer to mitigate CSRF in web applications with ease. It's based on 
the Synchronizer Token Pattern and leverages an injected java-script code to provide CSRF mitigation without much developer intervention. So far it has been implemented as a 
[PHP Library](https://github.com/mebjas/CSRF-Protector-PHP) and an CSRFProtector Project Apache 2.2.x module. Although different libraries and frameworks provide CSRF mitigation these days - all of them require 
developer to explicitly inject tokens with every form. 

### OWASP CSRF Protector - Extending the design as a python package to work with Flask and an Express JS (Node.JS) middleware

#### Brief Explanation:

The design of CSRF Protector involves a server side middle-ware that intercepts every incoming request and validates them for CSRF attacks. If the validation is successful the flow of control goes to business logic and the tokens are refreshed. In case of failed validation configured actions are taken. Post that, another middle ware takes care of injecting a JavaScript code (refer [https://github.com/mebjas/CSRF-Protector-PHP/blob/master/js/csrfprotector.js CSRF Protector PHP JS Code]) to HTML output. On the client side this code ensures that, for every request that require validation - the correct token is sent along with the request.

Check [GitHub Wiki](https://github.com/mebjas/CSRF-Protector-PHP/wiki) for some reference;

The goal of this project would be to:
- Port this design to a python module that can be used easily with Flask - [Kanban Board](https://github.com/mebjas/CSRF-Protector-py/projects/1?add_cards_query=is%3Aopen)
- Port this design to a node js module that can work well with express js (a popular Node.JS based framework). - [Initial Repo Link](https://github.com/mebjas/CSRF-Protector-JS)
- Fix some outstanding issues with java-script code used in library: [Issues](https://github.com/mebjas/CSRF-Protector-PHP/issues?q=is%3Aopen+is%3Aissue+label%3AJS) 

#### Expected Results:

*IMPORTANT: Clean, maintainable (ES6 compatible and using recommended design patterns) in case of Node.JS
*IMPORTANT: [compliant code PEP-8](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
*IMPORTANT: Thoroughly documented code along with API examples and example future components.
*CRITICAL: Excellent reliability and performance.
*Unit tests / Functional tests and easy to setup testing environment (preferably automated).
Knowledge Prerequisite: Javascript (Client Side), Python (having worked with flask preferable), Node.JS (having worked with node.js and middle wares preferable)

#### Mentors:

Contact: Minhaz A V

##  OWASP BLT (Bug Logging Tool) 

### Brief Explanation:

BLT lets anyone report issues they find on the internet. Found something out of place on Amazon.com ?  Let them know.  Companies are held accountable and shows their response time and history.  Get points for reporting 
bugs and help keep the internet bug free.

Check OWASP WIKI PAGE https://www.owasp.org/index.php/OWASP_Bug_Logging_Tool for some reference;

### Expected Results:

* Fuse app to allow easy bug reporting from phone.
* BUG cryptocurrency rewarded for each bug reported - requires a way to verify bugs are valid and not duplicates
* Allow for companies to do private (paid) bug bounties
* allow for bug reporting via email 
* build a referral program
* integrate an idea / suggestion feature

### Knowledge Prerequisite:

BLT is written in Python / Django, so a good knowledge of this language and framework is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. Fusetools will be 
used for the app and C++ (Bitcoin based) or Ethereum will be used for the cryptocurrency part.

### Proposals from student:

* Proposal on new features 
* Recommendations on how to use social applications to promote OWASP BLT

Mentors:
* Sean Auriti 
* Sourav Badami 

## OWASP RailsGoat - 2017 OWASP Top Ten

### Brief Explanation:

Add support for multiple OWASP Top Ten versions, such as 2017 and 2010.
Currently RailsGoat supports only the 2013 version of OWASP Top Ten.

### Expected Results:

* Wonderful experience for Student Developers, Mentors, and Technical Advisors
* A new feature that supports additional version(s) of OWASP Top Ten
* Code that conforms to our Development Rules and Guidelines

### Getting Started

* Have a look at the RailsGoat https://github.com/OWASP/railsgoat/blob/master/README.md file, especially the 'Getting Started' section. We like to see student developers who have already contributed to RailsGoat, so try 
fixing one of the bugs.
* We have created a dedicated wiki for the OWASP GSOC initiative: https://github.com/OWASP/railsgoat/wiki/RailsGoat-Summer-of-Code-Type-Project-Information
* Issue 305 [https://github.com/OWASP/railsgoat/issues/305] has more details. 

### Knowledge Prerequisite:

* RailsGoat is written in Ruby and Ruby-on-Rails, so a good knowledge of this language ecosystem is recommended. Some knowledge of application security would be useful, but not essential.

### Mentors:

* Frank Rietta [mailto:frank@rietta.com] - OWASP RailsGoat Mentor
* Ken Johnson - OWASP RailsGoat "Technical Advisor, Mentor"
* John Poulin  - OWASP RailsGoat Mentor
* Al Snow  - OWASP RailsGoat Project Coordinator

## OWASP RailsGoat - Capture-The-Flag RailsGoat Image Creation Automation

### Brief Explanation:
Create automation to build a Capture-The-Flag competition (CTF) image (VM, ISO, etc) which contains everything needed, such as [Operating System, Rails Stack, RailsGoat], so RailsGoat can easily be used in more 
Capture-The-Flag competitions.

### Expected Results:
* Wonderful experience for Student Developers, Mentors, and Technical Advisors
* A new feature that automates the process of building RailsGoat CTF images.
* Code that conforms to our Development Rules and Guidelines

### Getting Started
* Have a look at the RailsGoat https://github.com/OWASP/railsgoat/blob/master/README.md file, especially the 'Getting Started' section. We like to see student developers who have already contributed to RailsGoat, so 
try fixing one of the bugs.
* We have created a dedicated wiki for the OWASP GSOC initiative: https://github.com/OWASP/railsgoat/wiki/RailsGoat-Summer-of-Code-Type-Project-Information
* Issue 306 https://github.com/OWASP/railsgoat/issues/306 has more details. 

### Knowledge Prerequisite:

* Some background in creating VMs/ISOs would be helpful.
* RailsGoat is written in Ruby and Ruby-on-Rails, so a good knowledge of this language ecosystem is recommended. Some knowledge of application security would be useful, but not essential.

### Mentors:

* Matt Robinson [mailto:brimstone@the.narro.ws] - OWASP RailsGoat Mentor
* Frank Rietta [mailto:frank@rietta.com] - OWASP RailsGoat Mentor
* Ken Johnson - OWASP RailsGoat "Technical Advisor, mentor"
* Al Snow  - OWASP RailsGoat Project Coordinator

## OWASP RailsGoat - Merge "Security on Rails" book's lunchedin examples into RailsGoat

### Brief Explanation:

Merge "Security on Rails" book's lunchedin examples into RailsGoat. Need to get permission from publisher. @jasnow got permission previously.

### Expected Results:

* Wonderful experience for Student Developers, Mentors, and Technical Advisors
* More teaching RailsGoat examples based on "Security on Rails" book's lunchedin project.
* Code that conforms to our Development Rules and Guidelines

### Getting Started

* Have a look at the RailsGoat https://github.com/OWASP/railsgoat/blob/master/README.md file, especially the 'Getting Started' section. We like to see student developers who have already contributed to RailsGoat, so 
try fixing one of the bugs.
* We have created a dedicated wiki for the OWASP GSOC initiative: https://github.com/OWASP/railsgoat/wiki/RailsGoat-Summer-of-Code-Type-Project-Information
* Issue 307 https://github.com/OWASP/railsgoat/issues/307 has more details. 

### Knowledge Prerequisite:

* RailsGoat is written in Ruby and Ruby-on-Rails, so a good knowledge of this language ecosystem is recommended. Some knowledge of application security
would be useful, but not essential.

### Mentors:

* Frank Rietta [mailto:frank@rietta.com] - OWASP RailsGoat Mentor
* Ken Johnson - OWASP RailsGoat "Technical Advisor, mentor"
* Al Snow  - OWASP RailsGoat Project Coordinator

## OWASP RailsGoat - Add Devise Gem Support and Vulnerabilities to RailsGoat

### Brief Explanation:

Add Devise Support to RailsGoat along with adding Devise-related vulnerabilities.

### Expected Results:

* Wonderful experience for Student Developers, Mentors, and Technical Advisors
* Using Devise gem inside RailsGoat plus Devise-related vulnerabilities.
* Code that conforms to our Development Rules and Guidelines

### Getting Started

* Have a look at the RailsGoat https://github.com/OWASP/railsgoat/blob/master/README.md file, especially the 'Getting Started' section. We like to see student developers who have already contributed to RailsGoat, so try 
fixing one of the bugs.
* We have created a dedicated wiki for the OWASP GSOC initiative: https://github.com/OWASP/railsgoat/wiki/RailsGoat-Summer-of-Code-Type-Project-Information
* Issue 207 [https://github.com/OWASP/railsgoat/issues/207] and * Issue 243 [https://github.com/OWASP/railsgoat/issues/243] has more details.

### Knowledge Prerequisite:

* RailsGoat is written in Ruby and Ruby-on-Rails, so a good knowledge of this language ecosystem is recommended. Some knowledge of application security would be useful, but not essential.

### Mentors:

* Frank Rietta [mailto:frank@rietta.com] - OWASP RailsGoat Mentor
* John Poulin  - OWASP RailsGoat Mentor
* Ken Johnson - OWASP RailsGoat "Technical Advisor, mentor"
* Al Snow  - OWASP RailsGoat Project Coordinator

## OWASP RailsGoat - Your Idea

### Brief Explanation:

RailsGoat is a great framework for learning about OWASP Top 10 2013 using a vulnerable version of the Ruby on Rails (versions 3 to 5), as well as some "extras" that the initial project contributors felt worthwhile to share. This project is designed to educate both developers, as well as security professionals. Feel free to check out the [Railsgoat Github site](https://github.com/OWASP/railsgoat) for more details. If you have an idea that is not on this list then don't worry, you can still submit it.

### Expected Results:

* Wonderful experience for Student Developers, Mentors, and Technical Advisors
* A new feature that makes RailsGoat even better
* Code that conforms to our Development Rules and Guidelines

###  Needs: 

* Student Developers

### Getting Started

* Have a look at the RailsGoat https://github.com/OWASP/railsgoat/blob/master/README.md file, especially the 'Getting Started' section. We like to see student developers who have already contributed to RailsGoat, so try fixing one of the bugs.

### Knowledge Prerequisite:
* RailsGoat is written in Ruby and Ruby-on-Rails, so a good knowledge of this language ecosystem is recommended. Some knowledge of application security would be useful, but not essential.
Mentors:
* Frank Rietta [mailto:frank@rietta.com] - OWASP RailsGoat Mentor
*  Ken Johnson - OWASP RailsGoat "Technical Advisor, mentor"
* John Poulin  - OWASP RailsGoat Mentor
* Al Snow  - OWASP RailsGoat Project Coordinator
