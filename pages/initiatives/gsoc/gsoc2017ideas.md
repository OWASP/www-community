---
layout: full-width
title: GSoC 2017 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2017ideas
---
# GSoC 2017 Ideas

## OWASP Project Requests

Tips to get you started in no particular order:
 * Read the [[GSoC SAT]]
 * Check out the suggested projects below
 * Contact the mentors and teams of the projects that you are interested in

## OWASP Juice Shop

[[OWASP Juice Shop Project]] is an intentionally insecure webapp for security trainings written entirely in Javascript which encompasses the entire OWASP Top Ten and other severe security flaws. Juice Shop is written in Node.js, 
Express and AngularJS. The application contains more than 30 challenges of varying difficulty where the user is supposed to exploit the underlying vulnerabilities. Apart from the hacker and awareness training use case, 
pentesting proxies or security scanners can use Juice Shop as a "guinea pig"-application to check how well their tools cope with Javascript-heavy application frontends and REST APIs.

### Challenge Pack 2017

#### Brief Explanation:

Ideas for potential new hacking challenges are collected in [GitHub issues labeled "challenge"](https://github.com/bkimminich/juice-shop/issues?q=is%3Aissue+is%3Aopen+label%3Achallenge). This project could implement a whole 
bunch of challenges one by one and release them over the course of several small releases. This would allow the student to work in a professional Continuous Delivery kind of way while bringing benefit to the Juice Shop over 
the duration of the project.

Coming up with additional ideas for challenges would be part of the project scope, as the list of pre-existing ideas might not be sufficient for a GSoC project.

#### Expected Results:

* 10 or more new challenges for OWASP Juice Shop (including required functional enhancements to place the challenges in, e.g. the [Order Dashboard](https://github.com/bkimminich/juice-shop/issues/244) and 
[Pomace Recycling user stories](https://github.com/bkimminich/juice-shop/issues/243))
* Each challenge comes with full functional unit and integration tests
* Each challenge is verified to be exploitable by corresponding end-to-end tests
* Hint and solution sections for each new challenge are added to the "Pwning OWASP Juice Shop" ebook
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Getting started:

* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services
* Check out the corresponding GitHub milestone for this project: https://github.com/bkimminich/juice-shop/milestone/3

#### Knowledge Prerequisites:

* Javascript, Unit/Integration testing, experience with (or willingness to learn) AngularJS (1.x) and NodeJS/Express, some security knowledge would be preferable.

#### Mentors

* Bjoern Kimminich - OWASP Juice Shop Project Leader

### Tech Stack Update

#### Brief Explanation:

Development of OWASP Juice Shop started in 2014 and was based on - back then - quite recent Javascript frameworks and modules:

* AngularJS 1.x with Bootstrap in the client
* Express on top of NodeJS on the server with
** SQLite as a database
** Sequelize as an OR-Mapper
*** sequelize-restful as an automatic API-generator on top of the DB entities
* Jasmine 1.x to specify behavioral tests
** Karma as a test runner for the client-side unit tests
** Frisby.js for API tests on a dynamically launched server
** Protractor for end-to-end testing of the challenge exploits
* NPM for running/testing the application
* Grunt for some of the custom build scripts

Several of the above frameworks or modules have moved on to new (runtime incompatible) major releases, namely [Angular 2](https://github.com/bkimminich/juice-shop/issues/165), 
[Sequelize](https://github.com/bkimminich/juice-shop/issues/167), [Frisby and Jasmine](https://github.com/bkimminich/juice-shop/issues/164). Other modules are out of maintenance entirely, e.g. 
[sequelize-restful](https://github.com/bkimminich/juice-shop/issues/167).

Migrating the OWASP Juice Shop to the latest versions of the mentioned frameworks & modules is an important step to keep the application relevant as 'the most modern' intentionally broken web application. 
Moving to entirely different frameworks might be taken into considerationas well.

#### Expected Results:

* High-level target architecture overview including a migration plan with intermediary milestones
* Execution of migration without breaking functionality or losing tests along the way
* Code follows existing (or new) styleguides and passes all existing (or new) quality gates regarding code smells, test coverage etc.

#### Getting started:

* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services
* Check out the corresponding GitHub milestone for this project: https://github.com/bkimminich/juice-shop/milestone/2

#### Knowledge Prerequisites:

* Javascript, experience with latest Javascript frameworks for frontend, backend, testing and building (e.g. AngularJS 2.x, Jasmine 2.x, ...)

#### Mentors

* Bjoern Kimminich - OWASP Juice Shop Project Leader

### Your idea

#### Brief Explanation:

You have an awesome idea to improve OWASP Juice Shop that is not on this list? Great, please submit it!

#### Getting started

* Get in touch with Bjoern Kimminich

#### Expected Results:

* A new feature that makes OWASP Juice Shop even better
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Knowledge Prerequisites:

* Javascript, Unit/Integration testing, experience with (or willingness to learn) AngularJS (1.x) and NodeJS/Express, some security knowledge would be preferable.

#### Mentors
 
* Bjoern Kimminich - OWASP Juice Shop Project Leader

## OWASP Mobile Hacking Playground

The OWASP Mobile Hacking Playground (https://github.com/OWASP/OMTG-Hacking-Playground) is part of the OWASP Mobile universe, which consists at the moment of the following projects: 

* Mobile Application Security Verification (MASVS). The MASVS is a list of security requirements for mobile applications that can be used by architects, developers, testers, security professionals, 
and consumers to define what a secure mobile application is. (https://github.com/OWASP/owasp-masvs)
* Mobile Security Testing Guide (MSTG). The OWASP MSTG is a comprehensive manual for testing the security of mobile apps. It describes technical processes for verifying the controls listed in the OWASP Mobile 
Application Verification Standard (MASVS). The MSTG is meant to provide a baseline set of test cases for dynamic and static security tests, and to help ensure completeness and consistency of the tests. 
(https://github.com/OWASP/owasp-mstg)

In order to give also practical guidance to developers, security researches and penetration testers of mobile Apps, a hacking playground was created with the goal to create different mobile App’s that contain 
different vulnerabilities that map to the MSTG test cases. Every test case described in the MSTG will therefore be implemented in an Android and iOS App. This has two advantages:

* A developer can identify vulnerable code in the provided App’s and can see the implications and risks if such patterns are used and can look for the best practices in the MSTG to mitigate the vulnerabilities.
* Penetration testers / security researchers can identify bad practices, dangerous methods and classes they should look for when assessing a Mobile App and can gain more knowledge through the information provided in the OMTG.

It is also encouraged to use the App(s) for education purpose during trainings and workshops.

### Creation of Android Code Samples

#### Brief Explanation:

An Android App that maps to the MSTG test cases is already created. This App contains mostly test cases that are related to data storage on an Android device. In order to close the gap to the MSTG more test cases need 
to be added that show "bad practices" that lead to vulnerabilites, but also the latest security best practices to demonstrate how vulnerabilites can be mitigated. 

For examples of implemented test cases, see the Wiki of the Mobile Hacking Playground: https://github.com/OWASP/OMTG-Hacking-Playground/wiki/Android-App

#### Expected Results:

The following categories and their test cases are not fully added to the Android App:

* Cryptography (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x08-V3-Cryptography_Verification_Requirements.md)
* Authentication and Session Management (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x09-V4-Authentication_and_Session_Management%20Requirements.md)
* Network Communication (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x10-V5-Network_communication_requirements.md)
* Environmental Interaction (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x11-V6-Interaction_with_the_environment.md)
* Code Quality (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x12-V7-Code_quality_and_build_setting_requirements.md)

For some of the testcases this also includes creating an endpoint on server side in order to fully understand the test case and possible security concerns.

As not all missing test cases can be implemented during the GSOC a subset of them will be defined with the student together. 

#### Getting started:

Here are a few suggestion on how to get started.
* Check the Mobile Hacking Playground Android App, browse through the code and Wiki to get an understanding of what a test case look likes. 
* Browse through the MASVS and check the different areas and their defined requirements.
* Read about Security vulnerabilites and best practices for Android in areas you are interested in (e.g. Cryptography).

#### Knowledge Prerequisites:

General interest in Mobile and Security. Basic knowledge of Android and Java.

#### Mentors

 Sven Schleier - OWASP Slack: @sushi2k - OWASP Mobile Security Testing Guide and Mobile Hacking Playground Project Leader

### Write Mobile Crackmes and De-Obfuscation Guides 

#### Brief Explanation:

A key goal of the OWASP Mobile Testing Project is to build the ultimate learning resource and reference guide for mobile app reversers. As hands-on hacking is by far the best way to learn, we want to link most of the 
content to practical examples. We're therefore planning to add crackmes for Android and iOS to the GitHub repo that will then be used as examples throughout the guide. The goal is to collect enough resources for 
demonstrating the most important tools and techniques in our guide, plus additional crackmes for practicing.

In this project, the student creates multiple cracking exercises for Android and documents solutions to these exercises. The new crackmes developed in this project will be added to the existing list at:

https://github.com/OWASP/owasp-mstg/blob/master/OMTG-Files/02_Crackmes/List_of_Crackmes.md

Possible solutions will be added to the "Reverse Engineering" chapters in the Mobile Testing Guide along the following lines:

https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05b-Reverse-Engineering-and-Tampering-Android.md#symbolicexec

Additionally, the crackmes produced will be used as examples in other sections of the guide, such as test cases.

#### Expected Results:

* Several Apps that implemented different obfuscation techniques. 
* Evaluation of tools and techniques to de-obfuscate code. 

#### Getting started:

Here are a few suggestion on how to get started.
* Browse through the MASVS and check the Reverse Engineering requirements (https://github.com/OWASP/owasp-masvs/blob/master/Document/0x15-V8-Resiliency_Against_Reverse_Engineering_Requirements.md)
* Check out these wok-in-progress sections in the MSTG and the "obfuscation metrics" project:

- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05b-Reverse-Engineering-and-Tampering-Android.md
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05d-Reverse-Engineering-and-Tampering-iOS.md
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05-Testing-Processes-and-Techniques.md#tampering-and-reverse-engineering
- https://github.com/OWASP/owasp-mstg/blob/master/Document/0x05-Testing-Processes-and-Techniques.md#assessing-software-protections
- https://github.com/b-mueller/obfuscation-metrics

#### Knowledge Prerequisites:

General interest in Obfuscation techniques, Mobile and Security. Basic knowledge of Android and Java.

#### Mentors

 Bernhard Mueller - OWASP Slack: @bernhardm - OWASP Mobile Security Testing Guide and MASVS Project Leader

## OWASP ZAP

OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers. Previous GSoC students have implemented key parts of the ZAP core 
functionality and have been offered (and accepted) jobs based on their work on ZAP.

We have just included a few of the ideas we have here, for a more complete list see the issues on the ZAP bug tracker with the [project](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3Aproject) label.

### Field Enumeration

This would allow a user to iterate though a set of (user defined) characters in order to identify the ones that are filtered out and/or escaped.

The user should be able to define the character sets to test and will probably need to configure the success and failure conditions, as well as valid values for other fields in the form.

#### Expected Results

* User able to specify a specific field to enumerate via the ZAP UI
* A list of all valid characters to be returned from the sets of characters the user specifies
* Ability to configure a wide range of success and failure conditions to cope with as many possible situations as possible
* Code that conforms to our [Development Rules and Guidelines](https://github.com/zaproxy/zaproxy/wiki/DevGuidelines)

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors

Simon Bennetts and the rest of the ZAP Core Team

### Scripting Code Completion

ZAP provides a very powerful scripting interface. Unfortunately to use it effectively is only really possible with a good knowledge of the ZAP internals. Adding code completion (eg using a project 
like https://github.com/bobbylight/AutoComplete) would significantly help users.

#### Expected Results

* Code completion for all of the parameters for all available functions in the standard scripts
* Implementations for JavaScript, JRuby and Jython
* Helper classes with code completion for commonly required functionality
* Code that conforms to our [Development Rules and Guidelines](https://github.com/zaproxy/zaproxy/wiki/DevGuidelines)

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### SSRF Detector Integration

Currently ZAP does not detect SSRF vulnerabilities, due to the lack of this sort of service. https://ssrfdetector.com/ is an online service for detecting Server Side Request Forgery vulnerabilities (SSRF). It is 
developed and maintained by Jake Reynolds and is open source https://github.com/jacobreynolds/ssrfdetector

#### Expected Results

* Extend ZAP to detect SSRF vulnerabilities and interact with other services such as outlined above.
* Code that conforms to our [Development Rules and Guidelines](https://github.com/zaproxy/zaproxy/wiki/DevGuidelines)

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### Zest Text Representation and Parser

Zest is a graphical scripting language from the Mozilla Security team, and is used as the ZAP macro language.

A standardized text representation and parser would be very useful and help its adoption.

#### Expected Results

* A documented definition of a text representation for Zest
* A parser that converts the text representation into a working Zest script
* An option in the Zest java implementation to output Zest scripts text format

#### Knowledge Prerequisite:

The Zest reference implementation is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### Support Java as a Scripting Language

It would be very useful to support Java in addition to the JSR223 scripting languages within the ZAP script console'.

It should be possible to provide much better auto complete support than will be possible with dynamically typed scripting languages.

#### Expected Results

* The ability to run Java code in the ZAP Script Console to the same leval as other supported scripting languages
* Templates for all of the current script types
* Optionally auto complete supported

#### Knowledge Prerequisite:

The Zest reference implementation is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### Bamboo Support

ZAP already has an official plugin for Jenkins (https://plugins.jenkins.io/zap/). 

It would be great if we also had similar integration for Bamboo (https://www.atlassian.com/software/bamboo, https://en.wikipedia.org/wiki/Bamboo_(software))

#### Expected Results

* Facilitate the invocation and configuration of various ZAP functionalities from Bamboo CI. Including (but not limited to):
*Manage Sessions (Loading/Persisting)
*Define Context (Name, Include & Exclude URLs)
* Attack Contexts (Spider, Ajax Spider, Active Scan)
* Setup Autentication (Formed or Script Based)
* Generate Reports
* Templates for all of the current script types
* Optionally auto complete supported

#### Knowledge Prerequisite:

The Zest reference implementation is written in Java, so a good knowledge of this language is recommended. Some knowledge of CI/CD/Bamboo would be useful.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### Backslash Powered Scanner

This is a brand new technique developed by one of the Burp guys: http://blog.portswigger.net/2016/11/backslash-powered-scanning-hunting.html
Their implementation is open source: https://github.com/PortSwigger/backslash-powered-scanner so hopefully shouldn't be too hard to port to ZAP :)

#### Expected Results

* Extend ZAP's active scanner to leverage Backslash type scanning.
* Code that conforms to our [Development Rules and Guidelines](https://github.com/zaproxy/zaproxy/wiki/DevGuidelines)

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

### Your Idea

#### Brief Explanation:

ZAP is a great framework for building new and innovative security testing solutions. If you have an idea that is not on this list then don't worry, you can still submit it, we have accepted original projects in 
previous years and have even paid a student to work on their idea when we did not get enough GSoC slots to accept all of the projects we wanted.

#### Getting started

* Get in touch with us :)

#### Expected Results:

* A new feature that makes ZAP even better
* Code that conforms to our [Development Rules and Guidelines](https://github.com/zaproxy/zaproxy/wiki/DevGuidelines)

#### Knowledge Prerequisites:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Simon Bennetts and the rest of the ZAP Core Team

## BLT / Bugheist

#### Brief Explanation:

Bugheist lets anyone report issues they find on the internet. Found something out of place on Amazon.com ? Let them know. Companies are held accountable and shows their response time and history. Get points for 
reporting bugs and help keep the internet bug free.

#### Getting started

* Get in touch with us :)

#### Expected Results:

* A new feature that makes Bugheist even better

#### Knowledge Prerequisites:

BLT is written in Python / Django, so a good knowledge of this language and framework is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Sean Auriti and the rest of the BLT Core Team

## OWASP Security Knowledge framework

### Brief Explanation
The OWASP Security Knowledge Framework is intended to be a tool that is used as a guide for building and verifying secure software. It can also be used to train developers about application security. Education is the 
first step in the Secure Software Development Lifecycle. This software can be run on Windows/Linux/OSX using python-flask.

#### In a nutshell

- Training developers in writing secure code
- Security support pre-development ( Security by design, early feedback of possible security issues )
- Security support post-development ( Double check your code by means of the OWASP ASVS checklists )
- Code examples for secure coding

### Your idea / Getting started

* Please send an email to riccardo.ten.cate@owasp.org  or glenn.ten.cate@owasp.org  and we would love to tell you all about it! :-)

### Expected Results

* Adding features to SKF project
* Adding more function examples to pre-development phase
* Adding/updating code examples ( PHP, Java, .NET, Go, Python, NodeJS and more )
* Adding/updating Knowledgebase items
* Adding CWE references to knowledgebase items
* Adding low/medium level verification testing guides for developers to teach how to manually verify the existence of injection/logic flaws. (pen-testing)

### Knowledge Prerequisites

* For helping in the development of new features and functions Python flask would come in handy since the framework is written in python flask.
* For writing knowledgebase items only technical knowledge of application security is required
* For writing / updating code examples you need to know a programming language along with secure development.
* For writing the verification guide you need some penetration testing experience. 

#### Mentors
 

Riccardo ten Cate [mailto:riccardo.ten.cate@owasp.org]
Glenn ten Cate [mailto:glenn.ten.cate@owasp.org]

## OWASP ZSC

#### Brief Explanation:

OWASP ZSC is an open source software in python language which lets you generate customized shellcodes and convert scripts to an obfuscated script. This software can be run on Windows/Linux/OSX under python
https://www.owasp.org/index.php/OWASP_ZSC_Tool_Project

#### Getting started

* Get in touch with us on Github:
https://github.com/zscproject/OWASP-ZSC

Project Leaders:
* https://www.owasp.org/index.php/User:Ali_Razmjoo
* https://www.owasp.org/index.php/User:Johanna_Curiel

#### Expected Results:

We have a list of potential modules we want to build
To get familiar with the project, please check our installation and developer guidelines:
https://www.gitbook.com/book/ali-razmjoo/owasp-zsc/details

Contact us through Github, send us a question:
https://github.com/zscproject/OWASP-ZSC

* New obfuscation modules
* New shellcodes for OSX and Windows 

#### Knowledge Prerequisites:

OWASP ZSC is written in Python, so a good knowledge of this language and framework is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
 
Brian Beaudry & Patrik Patel
Please contact us through Github
https://github.com/zscproject/OWASP-ZSC

## OWASP Seraphimdroid mobile security project

### Behavioral malware and intrusion analysis 

#### Brief Explanation:

OWASP Seraphimdroid is an Android mobile app which already has a capability to statically analyze malware using machine learning (weka toolkit) relying on permissions. However, 
this is usually not enough and we intend to improve this with behavioral analysis. There are a number of paper in scientific literature describing how to detect malware and intrusions by dynamically analyzing 
its behavior (system calls, battery consumption, etc.). The idea of this project is to find the best approach that can be implemented on the device and implement it.

#### Expected Results:

* Reviewing scientific literature and find feasible approach we can take
* Implement and possibly improve the approach in Seraphimdroid
* Test the model and provide controls to switch algorithm on or off and possibly fine tune it
* Documenting approach as a technical report

#### Knowledge Prerequisites:

* Java
* Android
* CSV, XML
* Basic knowledge and interest in machine learning

#### Mentors
 
* Nikola Milosevic - OWASP Seraphimdroid Project Leader

### Framework for plugin development 

#### Brief Explanation:

OWASP Seraphimdroid is well rounded security and privacy app, however, it lacks some components community can provide. We would like to provide community the way to develop plugins 
that can add features to OWASP Seraphimdroid app. However, the way of integrating external components into Android app may be challenge. The way of presenting GUI and integration between processes need to be examined 
and developed. 

#### Expected Results:

* Examining the way of integrating third party apps through some provided API to OWASP Seraphimdroid
* Providing GUI integration with third party components
* Develop at least one test plugin
* Document the development process and API

#### Knowledge Prerequisites:

* Java
* Android
* CSV, XML

#### Mentors
 
* Nikola Milosevic - OWASP Seraphimdroid Project Leader

## OWASP DefectDojo

#### Brief Explanation:

DefectDojo is a security automation and vulnerability management tool. DefectDojo allows you to manage your application security program, maintain product and application information, schedule scans, triage 
vulnerabilities and push findings into defect trackers.

#### Expected Results:

* Multiple opportunities for students to get involved with DefectDojo ranging in difficulty from easy to advanced
* Students will receive hands-on experience in a full-stack software development project
* Students will have the opportunity to work on a project with multiple moving parts and third-party interactions

#### Knowledge Prerequisites:

* Python
* HTML, Bootstrap

#### Getting started:

* We have a [Read the Docs Site](http://defectdojo.readthedocs.io/en/latest/)

#### Mentors
 
* Greg Anderson - OWASP DefectDojo Project Leader

## OWASP AppSensor

The OWASP AppSensor project is a project to help you build self-defending applications through real-time event detection and response. Previous GSoC students have implemented key AppSensor contributions, and we've had 
very successful engagements. We look forward to hearing your ideas and hopefully working with you to execute them.

### Machine Learning Driven Web Server Log Analysis

#### Brief Explanation:

The goal of this project would be to build a web server log analysis tool suite based on ML (machine learning). This tool suite will accept as input web server logs (apache, nginx) and will provide as output a 
determination of requests that are considered "attacks" There are a number of key points for this project:
* Almost everybody has web server logs. It's a common format that is well understood, and is a good starting place for many security teams
* Because the format is well understood, the data points (features) are well understood. 
* This tool suite would have applicability far beyond just our project. The goal is to give away a tool that can process a set of log files, build a custom model for the traffic, and then be used to process future log 
files and find attacks (outliers / anomalies)

Note that this project would extend work done in last year's GSOC to get an initial machine learning capability developed. 

#### Expected Results

* User provides tool suite a set of web server logs (User has option to annotate data set with known attacks)
* System is pre-coded with knowledge of certain anomalous patterns (attacks)
* System builds ML model for processing future log files
* System provides mechanism for processing future logs using trained model.

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. The toolset used previously for the ML effort was scala/spark, but this is not a hard requirement. The preference would be to use either 
the JVM (java/scala), or possibly python, as both of these stacks are well understood and have significant ML capabilities. 

#### Mentors

John Melton and the rest of the AppSensor Team

### Your Idea

#### Brief Explanation:

AppSensor is a great tool and many organizations are starting to use it. If you have an idea that is not on this list, please submit it - we would love to give you the chance to work on an idea you came up with!

#### Getting started

* Get in touch with us :)

#### Expected Results:

* A new feature that makes AppSensor even better

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. 

#### Mentors

John Melton and the rest of the AppSensor Team

## OWASP OWTF

[Offensive Web Testing Framework (OWTF)](https://github.com/owtf/owtf) is a project focused on penetration testing efficiency and alignment of security tests to security standards like the OWASP Testing Guide 
(v3 and v4), the OWASP Top 10, PTES and NIST. Most of the ideas below focus on rewrite of some major components of OWTF to make it more modular.

### OWASP OWTF - MiTM proxy interception and replay capabilities

#### Brief Explanation:

The OWTF man-in-the-middle proxy is written completely in Python (based on the excellent Tornado framework) and was benchmarked to be the fastest MiTM python proxy. However it lacks the useful and much need interception 
and replay capabilities of mitmproxy (https://github.com/mitmproxy/mitmproxy). 

The current implementation of the MiTM proxy serves its purpose very well. Its fast but its not extensible. There are a number of good use cases for being extensible

* ability to intercept the transactions
* modify or replay transaction on the fly
* add additional capabilities to the proxy (such as session marking/changing) without polluting the main proxy code

Bonus: 

* Design and implement a proxy plugin (middleware) architecture so that the plugins can be defined separately and the user can choose what plugins to include dynamically (from the web interface).
* Replace the current Requester (based on urllib, urllib2) with a more robust Requester based on the new urllib3 with support for a real headless browser factory. The typical flow when requested for an authenticated browser 
instance (using PhantomJS)

* The "Requester" module checks if there is any login parameters provided (i.e form-based or script - look at https://github.com/owtf/login-sessions-plugin)
* Create a browser instance and do the necessary login procedure
* Handle the browser for the URI
* When called to close the browser, do a clean logout and kill the browser instance.

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentors:

Contact: Abraham Aranguren, Viyat Bhalodia, Bharadwaj Machiraju OWASP OWTF Project Leaders

### OWASP OWTF - Report enhancements

#### Brief Explanation:

The current OWTF report is very interactive but it cannot be exported in its current form. A reporter service can be written (which was in the very early releases of OWTF) which exports a nice report with template, findings, 
and additional pentester's notes into multiple formats. A small set of export formats should be supported such as:

* HTML (pure static html here)
* PDF
* XML (for processing)
* JSON (for processing)

For background on OWASP OWTF please see: https://www.owasp.org/index.php/OWASP_OWTF

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python, React.JS and general JavaScript proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentors:

Contact: Abraham Aranguren Viyat Bhalodia, Bharadwaj Machiraju OWASP OWTF Project Leaders

### OWASP OWTF - Distributed architecture

To be updated soon!

### OWASP OWTF - Off-line HTTP traffic uploader

#### Brief Explanation:

Although it is awesome that OWTF runs a lot of tools on behalf of the user, there are situations where uploading the HTTP traffic of another tool off-line can be very interesting for OWTF, for example:

* Tools that OWTF has trouble proxying right now: skipfish, hoppy
* Tools that the user may have run manually OR even from a tool aggregator -very common! :)-
* Tools that we just don't run from OWTF: ZAP, Burp, Fiddler

This project is about implementing an off-line utility able to parse HTTP traffic:

1) Figure out how to read output files from various tools like:
skipfish, hoppy, w3af, arachni, etc.
Nice to have: ZAP database, Burp database

2) Translate that into the following clearly defined fields:

* HTTP request
* HTTP response status code
* HTTP response headers
* HTTP response body

3) IMPORTANT: Implement a plugin-based uploader system

4) IMPORTANT: Implement ONE plugin, that uploads that into the OWTF database

5) IMPORTANT: OWTF should ideally be able to invoke the uploader right after running a tool
	Example: OWTF runs skipfish, skipfish finishes, OWTF runs the HTTP traffic uploader, all skipfish data is pushed to the OWTF DB.

6) CRITICAL: The off-line HTTP traffic uploader should be smart enough to read + push 1-by-1 instead of *stupidly* trying to load everything into memory first, you have been warned! :)

	Why? Because in a huge assessment, the output of "tool X" can be "10 GB", which is *stupid* to load into memory, this is OWTF, we *really* try to foresee the crash before it happens! ;)

CRITICAL: It is important to implement a plugin-based uploader system, so that other projects can benefit from this work (i.e. to be able to import third-party tool data to ZAP, Burp, and other tools in a 
similar fashion), and hence hopefully join us in maintaining this project moving forward.

For background on OWASP OWTF please see: https://www.owasp.org/index.php/OWASP_OWTF

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentors:

Contact: Abraham Aranguren Viyat Bhalodia, Bharadwaj Machiraju OWASP OWTF Project Leaders

## OWASP Hackademic Challenges Project

[[OWASP Hackademic Challenges Project]] The OWASP Hackademic Challenges project helps you test your knowledge on web application security. You can use it to actually attack web applications in a realistic but also 
controllable and safe environment.

### New CMS

#### Brief Explanation:

The CMS part of the project is really old and has accumulated a significant amount of technical debt.
In addition many design decisions are either outdated or could be improved. 
Therefore it may be a good idea to leverage the power of modern web frameworks to create a new CMS.
The new cms can be written in python using Django.

#### Expected Results:

* New cms with same functionality as the old one (3 types of users -- student, teacher, admin--, 3 types of resources -- article challenge, class--, ACL type permissions, CRUD operations on every resource/user, all 
functionality can be extended by Plugins.
* REST endpoints in addition to classic ones
* tests covering all routes implemented, also complete ACL unit tests, it would be embarassing if a cms by OWASP has rights vulnerabilities.
* PEP 8 code

''' Note: '''
This is a huge project, it is ok if the student implements a part of it. However whatever implemented must be up to spec.
If you decide to take on this project contact us and we can agree on a list of routes.
If you don't decide to take on this project contact us.
Generally contact us, we like it when students have insightful questions and the community is active

#### Getting started:

* Install and take a brief look around the old cms so you have an idea of the functionality needed
* It's ok to scream in frustration
* If you want to contribute to get a feeling of the platform a good idea would be lettuce tests for the current functionality (which won't change and you can port in the new cms eventually)

#### Knowledge Prerequisites:

Python, Django, what REST is, the technologies used, some security knowledge would be nice.

#### Mentors
 Spyros Gasteratos - Hackademic Challenges Project Leaders

### Course Type Challenge

#### Brief Explanation:
We have a sandbox engine which allows for complex guided challenges to be implemented.
We'd like to build a challenge that guides the user through a series of steps to an end goal and teaches more information on the subject matter on the way.
This is a very open-ended project on purpose to allow creative student to come up with nice ideas.
Bellow you will find some examples that we thought might be interesting.

Ideas on the project:
* Purposefully vulnerable web page that guides the user via javascript tooltips and hints to exploiting it using ZAP. ( Bonus: using ZAP via the ZAP api). The challenge is solved when the the student submits the contents 
of a text file located on the disk (obtained by exploited an RCE)

* Reversing a provided binary to extract information by providing step by step instructions to reversing using any popular reversing tool (well, you can't use IDA so gdb should have to do). Challenge is solved when the 
keys are extracted from the binary and submitted. Bonus points if each binary donwloaded has different keys.

* Guide to exploiting the TOP10. (Using ZAP?)

* Defensive Type challenges -- Here's how to create a patch for this kind of vulnerability -- Challenge is solved when the unit tests are run and the vulnerability isn't there.

#### Getting started

* Check popular javascript guide tools such as: (http://introjs.com/ and http://github.hubspot.com/shepherd/docs/welcome/ )
* If you're more interested in system or non-web challenges check serverspec and definitely check quest (https://github.com/puppetlabs/quest)
* If you think contributing is a good idea to make yourself familiar with the project you can either port one of the existing simpler 1-page challenges to a docker container and submit a pull request or write a guide on 
how to create such a challenge

#### Expected Results:

* One or more Course - style challenges provided either as a docker container or as a vagrant box.
* Concrete documentation on how to build a challenge like this.

#### Knowledge Prerequisites:

The technologies used.

#### Mentors
 Spyros Gasteratos - Hackademic Challenges Project Leaders
