---

layout: full-width
title: GSoC 2019 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2019ideas

---
# GSoC2019 Ideas

## OWASP Project Requests

Tips to get you started in no particular order:
- Read the [Student Guidelines](gsoc2019).
- Contact us through the mailing list or irc channel.
- Check our [github organization](https://github.com/OWASP).

## OWASP-SKF

### Idea 1 Improving the Machine Learning chatbot:

We want to extend the functionality of SKF Bot. (Security Knowledge Framework Chatbot):

Some improvements or the suggestions which we can do to improve the functionality are:

1. Create a desktop version of the chatbot. Where people can install the setup file on their local machine.
2. Create a Plugin or website bot which we can add in the website for better chat experience for the user.
3. Extend the bots capability to do the google search (using web scraping) for the things which are not available in the database. So, it will have a wider scope of knowledge.
4. Add basic conversation flow which makes SKF Bot friendly and provides the better user experience. Example: Replies to the general queries like How are you? What is your Name etc?
5. Extend the bot capability to reply to what security controls should be followed from the ASVS and MASVS or other custom checklists that are present in SKF.
6. Extend the bot to different platforms like Facebook, telegram, slack, Google Assistant etc.
Existing chatbot implementation is on Gitter. You can test the bot by typing @skfchatbot on Gitter Community.

#### Getting started:

- Get familiar with the architecture and code base of SKF (Security Knowledge Framework)
- Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
- Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

#### Knowledge Prerequisites:

- Python 3+, Flask, Coffee Script

#### Mentors and Leaders

Glenn ten Cate (Mentor, Project leader)
Riccardo ten Cate (Mentor, Project leader)
Priyanka Jain (Mentor)

### Idea 2 Improving and building Lab challenges and write-ups:

Build lab examples and write-ups (how to test) for different vulnerabilities over different technology stacks. These challenges are to be delivered in Docker so they can be easily deployed.

In the current situation the security knowledge framework ultimately presents a list of security controls with correlating knowledge base items that contain a description and a solution. The new labs are used to give the software developers or application security specialists a more in depth understanding and approach on how to test the vulnerabilities in their own code.
- For example we have now around 20 lab challenges in Docker container build in Python:
  - A Local File Inclusion Docker app example:
    - [skf-labs LFI](https://github.com/blabla1337/skf-labs/tree/master/LFI)
  - A write-up example:
    - [skf write-up filename-injection](https://owasp-skf.gitbook.io/asvs-write-ups/filename-injection)

The images that are pushed to the Github repository are already automatically build and pushed to a docker registry where the SKF users can easily pull the images from to get their labs running. Of course they can download it and build it themselves from source by pulling the original repository. 

### Idea 3 Addition of exploitation framework + labs + challenges and write ups

The proposal for SKF (Security Knowledge Framework) involves addition of “Exploit Development Framework” , the idea revolves around how does one start with Linux exploit development from basic string format attacks to advance buffer overflows.

The idea is to develop an addition (framework) which intergrates SKF, that now gives you an hands on experience for writing exploit code deployed over various containers with the help of dockers for easy and instant deployment.

The framework will involve a browser based environmental (shell) and inbuilt chat utility that will be guiding you on how to go from an absolute beginner with gdb basics to all the way to how to bypass various protections like ASLR/NX/Canaries on Linux environment.

Each challenge will have a dedicated container to easily maintain various challenges, also it will give you an option to connect to binary running on a particular port if you want to access it via your own machine, and also the source to the vulnerable code. This idea gives user a flexibility to experiment with the idea and even automate the attacks in python via socket programs or user intermediate framework like pwntools.

The whole idea of challenges isn’t limited to stack based buffer overflows, but includes various challenges like format string attacks, double frees, heap overflows and privilege escalations.

Total number will be deploying 20 challenges, the whole idea isn’t limited to exploit development but also to try out some very advance exploitation techniques like blind ROPs and lots of experimentation.

The whole add on also comes with a dedicated document with very well written ways to exploit challenges in various flavours like manual, automated, advanced.

Upon completion of labs and write ups the NLP model can be trained now to know not just web, but also all about various languages like C / C++ coding best practices and risk involved with calls like free (); puts(); and not just only tell the theory on why is it bad but also train you and guide you why it is bad and how you can write an exploit from a vulnerable code.

Upon completion of labs with ASLR turned off on (non ASLR) stages they can be turned on and lead to ROP with ASLR and even more challenging questions.

#### Mentors and Leaders

Glenn ten Cate (Mentor, Project leader)
Riccardo ten Cate (Mentor, Project leader)
Priyanka Jain (Mentor)

## OWASP DefectDojo

OWASP DefectDojo is a popular open source vulnerability management tool and is used as the backbone for security programs. It is easy to get started with to work on! We welcome volunteers of all experience levels and are happy to provide mentorship.

### Issue Tracking:

[Enhancement](https://github.com/DefectDojo/django-DefectDojo/issues?q=is%3Aissue+is%3Aopen+label%3Aenhancement requests) and [bugfixes](https://github.com/DefectDojo/django-DefectDojo/issues?q=is%3Aissue+is%3Aopen+label%3Abug) are located in Github issues. This project could implement a whole bunch of new features one by one and release them over the course of several small releases.

#### Expected Results:
- 5 or more new features or functional enhancements of significant scope for OWASP DefectDojo
- Each feature comes with full functional unit and integration tests

#### Getting started:
- Get familiar with the architecture and code base of the application built on Django
- Review the application functionality and familiarize yourself with Products, Engagements, Tests and Findings.
- Get familiar with the CI/CD process based on Travis-CI

#### Knowledge Prerequisites:
- Python, Django, Javascript, Unit/Integration testing.

#### Potential Mentors:
* Aaron Weaver - DefectDojo Project Leader
* Greg Anderson - DefectDojo Project Leader
* Matt Tesauro - DefectDojo Project Leader

### Option 1: Unit Tests - Difficulty: Easy
- If you're new to programming, unit tests are short scripts designed to test a specific function of an application.
- The project needs additional unit tests to ensure that new code functions properly.
- Review the current [unit tests](https://github.com/DefectDojo/django-DefectDojo/tree/dev/dojo/unittests)
- Complete Code Coverage Testing
  - Validate Tests exist for the following (create any that are missing):
    - Finding, Test, Engagement, Reports, Endpoints 
    - Import from all scanners 
    
### Option 2: Python3 Completion
- DefectDojo is finishing up a migration to Python3, Test the current [state](https://github.com/DefectDojo/django-DefectDojo/tree/python3/dojo/unittests) of Python3
- Ensure all features work
- Travis testing works correctly

### Option 3: Scan 2.0 / Launch Containers

Scan 2.0 consists of automating the scanning orchestration within DefectDojo. Several proof of concepts exist for this using the AppSecpPipeline to launch containers and then push those finding into the appropriate product. 
- Use the [AppSecPipeline](https://github.com/appsecpipeline/AppSecPipeline-Specification) containers to build a scanning pipeline built on top of [OpenFaaS](https://www.openfaas.com/)
- Scans should be able to be scheduled by DefectDojo and then invoked via the REST API call to OpenFaaS
- Upon scan completion the results will be posted back to DefectDojo via DefectDojo's REST API and consumed as an engagement/test.
- Pick 2 or 3 popular open source scanners such as NMAP, ZAP and Nikto to start out with.

## OHP (OWASP Honeypot)

OWASP Honeypot is an open source software in Python language which designed for creating honeypot and honeynet in an easy and secure way! This project is compatible with Python 2.x and 3.x and tested on Windows, Mac OS X and Linux.

### Getting Start

It's best to start from the [GitHub wiki page](https://github.com/zdresearch/OWASP-Honeypot/wiki), we are looking forward to adding more modules and optimize the core.

#### Technologies

Currently we are using

* Docker
* Python
* MongoDB
* TShark
* Flask
* ChartJS
* And more linux services

### Expected Results

* Zero Bugs: Currently we may have several bugs in different conditions, and it's best to test the all functions and fix them
* Monitoring: Right now monitoring limited to the connections (send&recieve) and it's best to store and analysis the contents for farther investigations and recognizing incoming attacks.
* Duplicated codes: codes are complicated and duplicated in engine, should be fixed/clean up
* New modules: add some creative ICS/Network/Web modules andvulnerable web applications, services and stuff
* API: update API sync to all features
* WebUI: Demonstrate and add API on WebUI and Live version with all features
* WebUI Special Reports: Track the attacks more creative and provide high risk IPs
* Database: Better database structure, faster and use queue
* Data analysis: Analysis stored data and attack signatures
* OWASP Top 10: Preparing useful processed/raw data for OWASP top 10 project

### Students Requirements

* Python
* Packet Analysis & Tshark & Libpcap
* Docker
* Database
* Web Development Skills
* Honeypot and Deception knowledge

### Mentors and Leaders

* Ali Razmjoo (Mentor & Project Leader)
* Ehsan Nezami (Mentor & Project Leader)
* Reza Espargham(Mentor)
* Abbas Naderi (Mentor)

## OWASP Juice Shop

OWASP Juice Shop Project is an intentionally insecure webapp for security trainings written entirely in Javascript which encompasses the entire OWASP Top Ten and other severe security flaws. Juice Shop is written in Node.js, Express and Angular. The application contains more than 30 challenges of varying difficulty where the user is supposed to exploit the underlying vulnerabilities. Apart from the hacker and awareness training use case, pentesting proxies or security scanners can use Juice Shop as a "guinea pig"-application to check how well their tools cope with Javascript-heavy application frontends and REST APIs.
 The best way to get in touch with us is the [community chat](https://gitter.im/bkimminich/juice-shop). You can also send PMs to the potential mentors (@bkimminich, @J12934 and @CaptainFreak) there if you like!

To receive early feedback please:
- put your proposal on Google Docs and submit it to the OWASP Organization on Google's GSoC page in "Draft Shared" mode. 
- Please pick "juice shop" as Proposal Tag to make them easier to find for us. Thank you!

### Feature Pack 2019

#### Brief Explanation:

Ideas for potential new functionality and "business" features are collected in [GitHub issues labeled "feature"](https://github.com/bkimminich/juice-shop/issues?q=is%3Aissue+is%3Aopen+label%3Afeature). This project could implement a whole bunch of new features one by one and release them over the course of several small releases. This would allow the student to work in a professional Continuous Delivery kind of way while bringing benefit to the Juice Shop over the duration of the project.

Coming up with good additional ideas for features and new functionality in the proposal could make the difference between being selected or declined as a student for this project!

#### Expected Results:
* 5 or more new features or functional enhancements of significant scope for OWASP Juice Shop (not necessarily including corresponding challenges)
* Each feature comes with full functional unit and integration tests
* Extending the functional walk-through chapter of the "Pwning OWASP Juice Shop" ebook
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Getting started:
* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

#### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Angular and NodeJS/Express, security knowledge is optional.

#### Potential Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator
* Shoeb Patel - OWASP Juice Shop Contributor (and former GSoC 2018 Student)


### Juice Shop Mobile

#### Brief Explanation:

A complete mobile client for Juice-Shop API which will serve a legit mobile experience for Juice-Shop user as well as a plethora of Mobile app vulnerabilities and challenges around them to solve. Should in the best case translate the idea of Juice Shop's hacking challenges with a score board and success notifications into the mobile world.

Coming up with a sophisticated proposal (optimally even with a good initial sample implementation) could make the difference between being selected or declined as a student for this project!

#### Getting started
* Get familiar with the architecture and code base of the application's RESTful backend
* Get familiar with Native App developement
* Get familiar with Mobile vulnerabilities

#### Expected Results:
* A mobile App with consistent UI/UX for Juice-Shop with standard client side vulnerabilities.
* Sufficient initial release quality (en par with Juice Shop and Juice Shop CTF) to make it an official extension project hosted in its own GitHub repository bkimminich/juice-shop-mobile
* Code follows existing styleguides and applies similar quality gates regarding code smells, test coverage etc. as the main project.

#### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) React Native and NodeJS/Express, some Mobile security knowledge would be preferable.

#### Potential Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator
* Shoeb Patel - OWASP Juice Shop Contributor (and former GSoC 2018 Student)

### Challenge Pack 2019

#### Brief Explanation:

Ideas for potential new hacking challenges are collected in [GitHub issues labeled "challenge"](https://github.com/bkimminich/juice-shop/issues?q=is%3Aissue+is%3Aopen+label%3Achallenge). This project could implement a whole bunch of challenges one by one and release them over the course of several small releases. This would allow the student to work in a professional Continuous Delivery kind of way while bringing benefit to the Juice Shop over the duration of the project.

Coming up with good additional ideas for challenges in the proposal could make the difference between being selected or declined as a student for this project!

#### Expected Results:
* 10 or more new challenges for OWASP Juice Shop (including required functional enhancements to place the challenges)
* Each challenge comes with full functional unit and integration tests
* Each challenge is verified to be exploitable by corresponding end-to-end tests
* Hint and solution sections for each new challenge are added to the "Pwning OWASP Juice Shop" ebook
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Getting started:
* Get familiar with the architecture and code base of the application's rich Javascript frontend and RESTful backend
* Get a feeling for the high code & test quality bar by inspecting the existing test suites and static code analysis results
* Get familiar with the CI/CD process based on Travis-CI and several associated 3rd party services

#### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Angular and NodeJS/Express, some security knowledge would be preferable.

#### Potential Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader
* Jannik Hollenbach - OWASP Juice Shop Project Collaborator
* Shoeb Patel - OWASP Juice Shop Contributor (and former GSoC 2018 Student)


### Your idea

#### Brief Explanation:

You have an awesome idea to improve OWASP Juice Shop that is not on this list? Great, please submit it!

#### Getting started
* Get in touch with [Bjoern Kimminich](https://www.owasp.org/index.php/User:Bjoern_Kimminich)

#### Expected Results:
* A new feature that makes OWASP Juice Shop even better
* Code follows existing styleguides and passes all existing quality gates regarding code smells, test coverage etc.

#### Knowledge Prerequisites:
* Javascript, Unit/Integration testing, experience with (or willingness to learn) Angular and NodeJS/Express, some security knowledge would be preferable.

#### Mentors:
* Bjoern Kimminich - OWASP Juice Shop Project Leader

## OWASP-Securetea Tools Project
The OWASP SecureTea Project is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server. This application uses the touchpad/mouse/wireless mouse to determine activity and is developed in Python and tested on various machines (Linux, Mac & Windows).
The software is still under development, and will eventually have it's own IDS(Intrusion Detection System) / IPS(Instrusion Prevention System), firewall, anti-virus, intelligent log monitoring capabilities with web defacement detection, and support for much more communication medium.
- [SecureTea-Project on GitHub](https://github.com/OWASP/SecureTea-Project/blob/master/README.md)

#### Brief Explanation
We are looking any awesome idea to improve Securetea Project that is not on this list? We are expecting make this project will be useful to everyone to secure their Small IoT. 

#### Idea
Below roadmap and expect  results you can choose to improve Securetea Project . 
if any bugs please help to fix it

#### Roadmap
[See Our Roadmap](https://github.com/OWASP/SecureTea-Project#roadmap)


#### Expect Results
- Securetea Protection /firewall
- Securetea Antivirus
- Notify by Whatsapp
- Notify by SMS Alerts
- Notify by Line
- Notify by Telegram
- Intelligent Log Monitoring  include Web Deface Detection
- Detection of malicious devices 
- Login History

#### Students Requirement

* Python
* Javascript 
* Angular and NodeJS/Express
* Database
* Linux

#### Mentors

* Yoseman Putra - (OWASP Securetea Project Leader)
* Rehim.A.A- (OWASP Securetea Project Leader)

## OWASP OWTF
[Offensive Web Testing Framework (OWTF](https://github.com/owtf/owtf) is a project focused on penetration testing efficiency and alignment of security tests 
to security standards like the OWASP Testing Guide (v3 and v4), the OWASP Top 10, PTES and NIST. Most of the ideas below focus on rewrite of some major 
components of OWTF to make it more modular. OWTF is moving to a fresh codebase with a fully Docker testing and deployment environment. If you want to get a 
jumpstart, check out: [new arch](https://github.com/owtf/owtf/tree/new).

### OWASP OWTF - Passive Online scanner improvements

#### Brief Explanation

OWTF allows many passive tests, such as those using third party websites like Google, Bing, etc. searches, as well as handy "Search for vulnerability" search boxes (i.e. Fingerprinting plugin). This feature involves the creation of a "script" that produces an interactive OWTF report with the intention of hosting it in the github.io site. The idea here is to have a passive, JavaScript-only interactive report available on the owtf.github.io site, so that people can try OWTF "without installing anything", simply visiting a URL.

This would be a normal OWTF interactive report where the user can:
* Enter a target
* Try passive plugins (only the parts that use no tools)
* Play with boilerplate templates from the OWTF interactive report
An old version of the passive online scanner is hosted [here](https://owtf.github.io/online-passive-scanner).

#### LEGAL CLARIFICATION (Just in case!): 
The passive online scanner, simply makes OWTF passive testing through third party websites more accessible to anybody, however it is the user that must 
1. click the link manually + 
2. do something bad with that afterwards + 
3. doing 1 + 2 WITHOUT permission :). 
Therefore this passive online scanner does not do anything illegal 
[More information about why this is not illegal here](http://www.slideshare.net/abrahamaranguren/legal-and-efficient-web-app-testing-without-permission) 
(recommended reading!)

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:
* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/)/ES6 JavaScript code in all modified code and surrounding areas.
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge Prerequisite:

A good knowledge of JavaScript and writing ES6 compliant React/TypeScript is needed. Previous exposure to security concepts and penetration testing is not required but recommended and some lack of this can be compensated with pre-GSoC involvement and will to learn.

#### OWASP OWTF Mentors:
Contact: Abraham Aranguren or Viyat Bhalodia

## OWASP OWTF - MiTM proxy interception and replay capabilities
### Brief Explanation:

The OWTF man-in-the-middle proxy is written completely in Python (based on the excellent Tornado framework) and was benchmarked to be the fastest MiTM python proxy. However it lacks the useful and much need interception and replay capabilities of [mitmproxy](https://github.com/mitmproxy/mitmproxy).

The current implementation of the MiTM proxy serves its purpose very well. Its fast but its not extensible. There are a number of good use cases for being extensible
- ability to intercept the transactions
- modify or replay transaction on the fly
- add additional capabilities to the proxy (such as session marking/changing) without polluting the main proxy code

Bonus:
- Design and implement a proxy plugin (middleware) architecture so that the plugins can be defined separately and the user can choose what plugins to include dynamically (from the web interface).
- Replace the current Requester (based on urllib, urllib2) with a more robust Requester based on the new urllib3 with support for a real headless browser factory. The typical flow when requested for an authenticated browser instance (using PhantomJS)

- The "Requester" module checks if there is any login parameters provided (i.e form-based or script - look at the [login-sessions-plugin]( https://github.com/owtf/login-sessions-plugin) )
- Create a browser instance and do the necessary login procedure
- Handle the browser for the URI
- When called to close the browser, do a clean logout and kill the browser instance.

#### Expected results:

- IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
- IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
- IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
- CRITICAL: Excellent reliability
- Good performance
- Unit tests / Functional tests
- Good documentation

#### Knowledge Prerequisite:

- Python proficiency, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentors:
Contact: 
Abraham Aranguren
Viyat Bhalodia
Bharadwaj Machiraju
OWASP OWTF Project Leaders

## OWASP OWTF - Web interface enhancements

### Brief Explanation:

The current web interface is a mixture of Tornado Jinja templates and ReactJS. A complete UI change to a stable ReactJS-based interface should be the deliverable for this project.  Most of the hard part for the change has already been done and added in a separate branch at [OWTF on GitHub](https://github.com/owtf/owtf/tree/develop)

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:
- IMPORTANT:Clean, maintainable (ES6 compatible and using recommended design patterns) React (JavaScript) code. [This](https://github.com/getsentry/zeus/tree/master/webapp) is a good example!)
- IMPORTANT: Thoroughly documented code along with API examples and example future components.
- CRITICAL: Excellent reliability and performance.
- Unit tests / Functional tests and easy to setup testing environment (preferably automated).

#### Knowledge Prerequisite:

- Python (reading API source code and endpoints), React.JS (high proficiency) and general JavaScript proficiency.

#### OWASP OWTF Mentors:
Contact: 
Abraham Aranguren
Viyat Bhalodia
Bharadwaj Machiraju
OWASP OWTF Project 

## OWASP OWTF - New plugin architecture

### Brief Explanation:

The current plugin system is not very useful and it is painful to browse many plugins. Most of the plugins do have much code and most of is repeated - much refactoring needed there.

This issue is documented in detail at [905](https://github.com/owtf/owtf/issues/905).

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:
- IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
- IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
- IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
- CRITICAL: Excellent reliability
- Good performance
- Unit tests / Functional tests
 Good documentation

## OWASP iGoat

### Idea 1:
Completing OWASP iGoat documentation at [docs.igoatapp.com](https://docs.igoatapp.com/) and creating demo videos at for OWASP iGoat YouTube channel for learning purpose.

### Idea 2:
Adding new challenge pack / CTF for iGoat. It should be one point solution for learning iOS app security

## OWASP Seraphimdroid

OWASP Seraphimdroid is Android security and privacy app, with features to enhance user's knowledge about security and privacy on their mobile device. If you are interested in this project and working on it during Google Summer of Code, please contact Nikola Milosevic and express your interest.

### Idea 1: Anomaly detection of device state

The idea is that certain features of a device would be constantly monitored (battery use, internet usage, opp calls, etc.). Initially, the usual behaviour of the device would be learned. Later, anomalies normal behavior would be reported to the user. This should involve some explanations, such as which applications are causing an anomaly the device behaviors 

### Idea 2: On device machine learning of maliciousness of an app

Tensor-flow for on-device processing and some other libraries have been released that enable machine learning. We have previously applied a system, that based on permissions, is able to distinguish malicious apps from non-malicious. Now, we would like to learn also from other outputs and things one can monitor about application whether it can be malicious. 

### Idea 3:  Enhansing privacy features

The vision of Seraphimdroid is to be aware of privacy threats. This may be achieved throug knowing which applications are using user accounts or other information that uthe user has on phone to send to the server, or just by knowing which applications may be doing it. Knowledgebase shouldbbeextending with the suggestions on how to improve privacy. Also, automated settings of various apps to use encryption should be proposed.

## OWASP ZAP
The OWASP Zed Attack Proxy (ZAP) is one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers. Previous GSoC students have implemented key parts of the ZAP core functionality and have been offered (and accepted) jobs based on their work on ZAP.

### Active Scanning WebSockets

#### Brief Explanation:

ZAP has good support for websockets, and allows them to be intercepted, changed and fuzzed. Unfortunately it doesn't currently support active scanning (automated attacking) of websocket traffic (messages).
We would like to add active scanning support to websockets, ideally in a generic way which would allow us to reuse as many of our existing rules as are relevant. Adding additional websocket specific attacks would also be very useful.
This project will be a continuation of the work that was started as part of last year's GSoC.

#### Expected results:

- An pluggable infrastructure that allows us to active scan websockets
- Converting the relevant existing scan rules to work with websockets
- Implementing new websocket specific scan rules

#### Getting Started:

- Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding' section.
- We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

- ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors:

Simon Bennetts and the rest of the ZAP Core Team

## Automated Authentication Detection and Configuration

### Brief Explanation:

Currently a user must manually configure ZAP to handle authentication, eg as per [FAQformauth](https://github.com/zaproxy/zaproxy/wiki/FAQformauth)
This is time consuming and error prone.
Ideally ZAP would help detect login and registration pages and provide more assistance when configuring authentication, ideally being able to completely automate the task for as many sort of webapps as possible.
This project will be a continuation of the work that was started as part of last year's GSoC.

#### Expected results:
- Detect login and registration pages
- Provide a wizard to walk users through the process of setting up authentication, with as much assistance as possible
- An option to completely automate the authentication process, for as many authentication mechanisms as possible

#### Getting Started:

- Have a look at the ZAP [CONTRIBUTING.md](https://github.com/zaproxy/zaproxy/blob/develop/CONTRIBUTING.md) file, especially the 'Coding' section.
- We like to see students who have already contributed to ZAP, so try fixing one of the bugs flagged as [IdealFirstBug](https://github.com/zaproxy/zaproxy/issues?q=is%3Aopen+is%3Aissue+label%3AIdealFirstBug).

#### Knowledge Prerequisites:

- ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors:

## IoT Goat

IoT Goat will be a deliberately insecure firmware based on OpenWrt. The project’s goal is to teach users about the most common vulnerabilities typically found in IoT devices. The vulnerabilities will be based on the [IoT Top 10 2018](https://www.owasp.org/images/1/1c/OWASP-IoT-Top-10-2018-final.pdf). 

### Idea 1: Insecure firmware web application ecosystem

#### Brief Explanation:

A vulnerable web application, and backend API/web services deployed in OpenWrt containing critical vulnerabilities showcasing the traditional IoT problems.

#### Getting Started:

- Have a look at the getting started page to get familiar with [virtualizing OpenWrt](https://github.com/scriptingxss/IoTGoat/blob/master/BuildEnvironment.md)
- Create a GitHub account to be a collaborator to the repository
- Review the [example vulnerabilities and challenges](https://github.com/scriptingxss/IoTGoat/blob/master/Examples/Weak%2C%20Guessable%2C%20or%20Hardcoded%20Passwords.md)

#### Expected results:

Development of a simple web application user interface with web services and API's deployed locally on the OpenWrt firmware. Documented challenges of how to discover and remediate web software security vulnerabilities. The insecure web application services must contain the following vulnerabilities to be used with the IoT testing guide: 
- Command injection
- SQL injection
- Local file inclusion 
- XXE injection,Insufficient Authentication
- Transfer sensitive data using insecure channels
- Store sensitive data insecurely
Vulnerable SOAP web services and REST API implementations are in-scope. 

#### Knowledge Prerequisites:

- Working Linux knowledge
- Embedded and/or web development (nice to have)
  - Web application code can be developed using the following common embedded programming languages:
      - Lua
      - PHP
      - C/C++
      - JavaScript

### Idea 2: Insecure network services

#### Brief Explanation:

Deliberately insecure services configured within OpenWrt such as an miniupnp daemon configured with secure_mode off (Secure mode; client can only redirect an incoming port to the client itself (same IP as the request comes from), to demonstrate a port mapping attack where an attacker from inside the network exposes a service that typically should be behind a LAN to the internet). 

#### Getting Started:

- Have a look at the getting started page to get familiar with [virtualizing OpenWrt](https://github.com/scriptingxss/IoTGoat/blob/master/BuildEnvironment.md)
- Create a GitHub account to be a collaborator to the repository
- Review the [example vulnerabilities and challenges](https://github.com/scriptingxss/IoTGoat/blob/master/Examples/Weak%2C%20Guessable%2C%20or%20Hardcoded%20Passwords.md)

#### Expected results:

Documented challenges of how to discover and remediate insecure network service vulnerabilities. The network services can be inherently insecure or have insecure configurations that can be abused during the challenges.
- Example of network insecure services include:
  - FTP
  - Telnet
  - miniupnpd
  - HTTP

#### Knowledge Prerequisites:

- Working Linux knowledge
- Network security

### Idea 3: Insecure firmware build system

#### Brief Explanation:

Develop custom firmware builds of the latest OpenWrt version (18.06) demonstrating the process of incorporating debug services/tools, misconfigurations, and usage of vulnerable software packages. 

#### Getting Started:

- Review OpenWrt's developer guide to get familiar with creating custom firmware builds
  - [OpenWRT Developer start](https://openwrt.org/docs/guide-developer/start)
  - [OpenWRT Build System](https://openwrt.org/docs/guide-developer/build-system/install-buildsystem)
  - [OpenWRT](https://github.com/openwrt/openwrt)

#### Expected results:

- Provide walkthrough examples of insecure design choices for building firmware. 
- Provide suggested mitigation security controls

#### Knowledge Prerequisites:

- Working Linux knowledge
- Embedded development (C/C++)

### Suggest your own ideas

You may suggest additional challenges or ideas that fit this project's objectives.

### Mentors and Leaders
- Aaron Guzman - OWASP IoT Goat Contributor (Project leader of the IoT and Embedded AppSec project)
- Fotios Chantzis - OWASP IoT Goat Contributor (and former GSoC Student/GSoc Mentor)
- Paulino Calderon - OWASP IoT Goat Contributor (and former GSoC 2011 Student/GSoc Mentor in 2015 and 2017)

## OWASP Web Honeypot Project

The goal of the OWASP Honeypot Project is to identify emerging attacks against web applications and report them to the community, in order to facilitate protection against such targeted attacks. Within this project, Anglia Ruskin University is leading the collection, storage and analysis of threat intelligence data. 

[OWASP_Honeypot_Project](https://www.owasp.org/index.php/OWASP_Honeypot_Project)

[Honeypot-Project on GitHub](https://github.com/OWASP/Honeypot-Project/)

### Brief Explanation
The purpose of this part of the project is to capture intelligence on attacker activity against web applications and utilise this intelligence as ways to protect software against attacks. Honeypots are an established industry technique to provide a realistic target to entice a criminal, whilst encouraging them to divulge the tools and techniques they use during an attack. Like bees to a honeypot. These honeypots are safely designed to contain no information of monetary use to an attacker, and hence provide no risk to the businesses implementing them.

The project will create honeypots that the community can distribute within their own networks. With enough honeypots globally distributed, we will be in a position to aggregate attack techniques to better understand and protect against the techniques used by attackers. With this information, we will be in a position to create educational information, such as rules and strategies, that application writers can use to ensure that any detected bugs and vulnerabilities are closed.

### Idea

Project progression: 
- Honeypot software. The honeypot software that is to be provided to the community to place in their networks has been written. Honeypots are available in a variety of forms, to make deployment as flexible as possible and appeal to a diverse a user set as possible.
- Collection software. The centralised collection software has been written and evaluated in a student driven proof-of-concept project. Honeypots have been attacked in a laboratory situation and have reported both the steps taken by the attacker and what they have attacked, back to the collection software.
- Rollout to the Community. The project now needs a dedicated infrastructure platform in place that is available to the entire community to start collecting intelligence back from community deployed honeypots. This infrastructure will run the collector software, analysis programmes and provide a portal for communicating our finds and recommendations back to the community in a meaningful manner.
- Going Forward. Toolkits and skills used by attackers do not stand still.  As existing bugs are plugged, others open. Follow up stages for the project will be to create a messaging system to automatically update the community on findings of significant risk in their existing code that requires attention. 

### Expect Results

Some of the ideas from last year's summit

- Setup Proof of Concept to understand how Mod Security baed Honeypot/Probe interacts with a receiving console (develop a VM and/or Docker based test solution to store logs from multiple probes).
- Evaluate console options to visualise threat data received from ModSecurity Honeypots/probes in MosSecurity Audit Console, WAF-FLE, Fluent and bespoke scripts for single and multiple probes.
- Develop a mechanism to convert from stored MySQL to JSON format.
- Provide a mechanism to convert ModSecurity mlogc audit log output into JSON format.
- Provide a mechanism to convert mlogc audit log output directly into ELK (ElasticSearch/Logstash/Kibana) to visualise the data.
- Provide a mechanism to forward honest output into threat intelligence format such as STIX using something like the MISP project(https://www.misp-project.org) to share Threat data coming from the Honeypots making it easy to export/import data from formats such as STIX and TAXII., may require use of concurrent logs in a format that MISP can deal with.
- Consider new alternatives for log transfer including the use of MLOGC-NG or other possible approaches.
- Develop a new VM based honeypot/robe based on CRS v3.0.
- Develop new alternative small footprint honeypot/probe formats utilising Docker & Raspberry Pi.
- Develop machine learning approach to automatically be able to update the rule set being used by the probe based on cyber threat intelligence received.

### Students Requirements

Some of the skills we are looking for:

- Apache/Tomcat 
- Any experience of MISP
- MySQL & JSON
- ELK 
- STIX/TAXII
- Python
- ModSecurity/mlogc
- OWASP Core RuleSet (CRS)
- Linux
- VM/Docker

### Mentors

- Adrian Winckles - (OWASP Web Honeypot Project Leader)

### Suggest your own ideas

You may suggest additional challenges or ideas that fit this project's objectives.

## OWASP Risk Assessment Framework

Tool projects aim to assessment more than one or many web application using owasp risk rating mathodologies.

[RiskAssessmentFramework on GitHub](https://github.com/OWASP/RiskAssessmentFramework)

### Idea 1:

make dashboard with database and can assess many website based owasp risk rating mathodologies, create graph  and report in pdf,word & excel format.

### Ideas 2 : Static Application Security Testing. 

### Students Requirements

- Python
- Java
- Javascript 
- Angular and NodeJS/Express
- Database
- Linux

### Mentors

* Ade Yoseman Putra - (Mentor)
* Rejah Rehim.A.A - (Mentor)
* Azzeddine Ramrami - (Mentor)
