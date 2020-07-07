---
layout: full-width
title: GSoC 2012 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2012ideas
---
# GSoC 2012 Ideas

## Guidelines

### Information for Students
The ideas below were contributed by OWASP project leaders and users. They are sometimes vague or incomplete. If you wish to submit a proposal based on these ideas, you may wish to contact the corresponding project leaders and find out more about the particular suggestion you're looking at.
Being accepted as a Google Summer of Code student is quite competitive. Accepted students typically have thoroughly researched the technologies of their proposed project and have been in frequent contact with potential mentors. Simply copying and pasting an idea here will not work. On the other hand, creating a completely new idea without first consulting potential mentors is unlikely to work out.

### Adding a Proposal

### Project

#### Brief explanation:

#### Expected results:

#### Knowledge Prerequisite:

#### Mentor:

#### Ideas

How to find ideas? Obvious sources of projects are the OWASP project wiki, bugs database, and project mailing lists.

### Generic Sample Proposal

#### Accepted for GSoC 2011

#### Brief explanation:

KDE has developed a number of very interesting and powerful technologies, libraries and components but there is no easy way to show them to other people.

#### Expected results:

Something like Qt Demo but with KDE technologies.

#### Knowledge Prerequisite:

C++ is the main language of KDE, therefore the demo should be in C++. The more you know about C++, Qt, KDE and scripting (for Kross and KDE bindings demos), the better.
This idea encompasses so much different stuff the student is not expected to know everything before they start coding (but will certainly know a lot when they're done!).

**Skill level:** medium

**Mentor:** Pau Garcia i Quiles as general mentor and someone to ask for directions. Specific help for each technology will probably require help from its developers.

## OWASP Project Requests

### ZAP Proxy

The Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications.

It is designed to be used by people with a wide range of security experience and as such is ideal for developers and functional testers who are new to penetration testing.

ZAP provides automated scanners as well as a set of tools that allow you to find security vulnerabilities manually.

[website](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project)

[Mailing List](http://groups.google.com/group/zaproxy-develop)

### Project 001 - Compare crawling sessions for authentication issues

#### Brief explanation:

Develop a ZAP session crawler to be able to compare two crawling sessions of two logged in users and see what URLs or Actions could be performed from the other session.

#### Expected results:

ZAP will be able to recognise when requests are associated with different sessions.

ZAP should allow the user to view the crawled URLs for each session independantly, and show which URLs are unique to each session.

It should also be able to check if any of the 'unique' pages can in fact be accessed by the other session.

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of crawlers and/or aplication security would be useful, but not essential.

**Mentors** Simon Bennetts - OWASP ZAP Project Leader | Skyler Onken - OWASP ZAP Developer

### Project 002 - Dynamically Configurable actions

#### Brief explanation:

ZAP provides various mechanisms which allow HTTP requests and responses to be changed dynamically. So (for example) a string in an HTTP request can automatically be changed to another string.

It also supports a scripting interface, which is very powerful but at the moment difficult to use.

This project would introduce something inbetween thess 2 options - a powerful way of defining (potentially) complex rules using a wizard based interface.

The challenge will be to make it as usable as possible while still providing a wide range of functionality.

#### Expected results:

This component would provide a set of highly configurable 'actions' which the user would see up via a wizard.

So they would initially define when the action applies, based on things like regex matching on request elements. And they should be able to define multiple criteria with ANDs and ORs.

Then they would define the actions, which could include:
* Changing the request (adding, removing or replacing strings)
* Raising alerts
* Breaking (to replace existing break points)
* Running custom scripts (which could do pretty much anything)
They would then be able to switch the actions on and off from the full list of defined actions using checkboxes

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader | Skyler Onken - OWASP ZAP Developer

### Project 003 - Extend Web API to cover all of the ZAP functionality

#### Brief explanation:


ZAP provides a REST based API which can be used to control core aspects of the functionality provided by ZAP.

This project would extend that API to cover all/most of the ZAP functionality.

#### Expected results:

Comprehensive Web API that will cover all of the ZAP Proxy functionality.

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader | Skyler Onken - OWASP ZAP Developer

### Project 004 - Closer integration with OWASP AJAX

#### Brief explanation:

ZAP provides a basic spider that can be used to explore an application, however it is very limited, especially when used with AJAX based applications.

[The OWASP AJAX crawling tool](https://www.owasp.org/index.php/OWASP_AJAX_Crawling_Tool) is specifically designed to crawl AJAX applications and can already use ZAP as a proxy.

This project would develop a ZAP plugin which integrates ZAP with the OWASP AJAX crawling Tool.

#### Expected results:

A new ZAP plugin would be produced which allows ZAP to crawl AJAX applications using the OWASP AJAX crawling tool.

The plugin would allow the 2 tools to be tightly integrated, while still allowing them to work completely independently.

#### Knowledge Prerequisite:

Both ZAP and the AJAX tool are written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of crawlers and/or aplication security would be useful, but not essential.

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader | Skyler Onken - OWASP AJAX Tool Project Leader

### ESAPI Swingset Interactive

The ESAPI Swingset Interactive is a web application which demonstrates common security vulnerabilities and asks users to secure the application against these vulnerabilities using the ESAPI library. The application is intended for Java Developers. The goal of the application is to teach developers about the functionality of the ESAPI library and give users a practical understanding of how it can be used to protect web applications against common security vulnerabilities.

[Website](https://www.owasp.org/index.php/Projects/OWASP_ESAPI_Swingset_Interactive_Project)

[Mailing List](http://lists.owasp.org/pipermail/owasp-esapi-swingset/)

### Project 001 - Implement a solid Authenticator class

#### Brief explanation:

Provide Swingset Interactive with a simple but fully functional implementation of the ESAPI Authenticator Interface.

#### Expected results:

Swingset Interactive comes with a rudimentary implementation of the ESAPI Authenticator Interface, a FileBasedAuthenticator. This implementation needs to be fixed or replaced in order to allow users of the Swingset Interactive application all of the ESAPI Authenticator methods, including registration, login, a "remember me" feature and a persistence beyond server restart.

#### Knowledge Prerequisite:

A basic knowledge of Java, Java Servlets is necessary, as is knowledge of HTML.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

### Project 002 - Upgrade to ESAPI 2.0.x

#### Brief explanation:

Adapt Swingset Interactive to work with ESAPI 2.0.x. libraries.

#### Expected results:

Make the current Swingset Interactive application compatible with ESAPI 2.0.x. Swingset Interactive currently comes with ESAPI 1.4.Various changes and improvements were made with ESAPI 2.0.x and it is generally recommended not to use 1.4 any more for Java EE Projects.

#### Knowledge Prerequisite:

A basic knowledge of Java, Java Servlets is necessary, as is knowledge of HTML.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

### Project 003 - Improve the Swingset look and feel

#### Brief explanation:

Various minor bug fixes and improvements.

#### Expected results:

Fix and solve a number of documented bug fixes and improvement suggestions for the Swingset Interactive and bring in your own improvement suggestions.

#### Knowledge Prerequisite:

A basic knowledge of Java, Java Servlets is necessary, as is knowledge of HTML.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

### Project 004 - Platform-independent Swingset Interactive

#### Brief explanation:

Adapt Swingset Interactive to work with any OS.

#### Expected results:

Swingset Interactive currently runs only under Windows. Modify the Eclipse project and installation scripts to be easily installed on any OS that runs Eclipse. 

#### Knowledge Prerequisite:

Good knowledge of Java, Apache Tomcat and a broad knowledge of various Operating Systems are required.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

### Project005 - Mavenize the Swingset

#### Brief explanation:

Create a new Swingset Interactive Maven Archetype.

#### Expected results:

Offer the Swingset Interactive as a Maven Archetype.

#### Knowledge Prerequisite:

Good knowledge of Java, and Maven are required.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

### Project006 - New Lessons

#### Brief explanation:

Develop new coding lessons to learn the ESAPI Libraries.

#### Expected results:

A new set of interactive coding lessons for students to use.

#### Knowledge Prerequisite:

Good knowledge of Java, ESAPI, HTML and the Eclipse framework are required.

**Mentor:** Fabio Cerullo - OWASP ESAPI Swingset Interactive Project Leader

## AntiSamy

The AntiSamy project provides a Java library for developers to accept innocent HTML markup without exposing themselves to possible cross-site scripting (XSS) vulnerabilities.

[Website](https://www.owasp.org/index.php/AntiSamy)

[Mailing List](https://lists.owasp.org/mailman/listinfo/owasp-antisamy)

### Project001 - Add a Functional Testing Suite

#### Brief explanation:

Create a set of positive test cases designed to generate assurance that AntiSamy correctly processes inert HTML.

#### Expected results:

As of today, AntiSamy has a large set of test cases that prove that AntiSamy is resistant to a number of known attacks. There are also test cases that make sure it doesn't crash when given bad data. There are very few test cases that ensure that it properly handles good HTML. A set of test cases that confirm how expected good data is processed by AntiSamy generates a lot of assurance that it is functional as well as secure.

#### Knowledge Prerequisite:

Comfort with Java, Maven, SVN and JUnit are required.

**Mentor:** Arshan Dabirsiaghi - OWASP AntiSamy Project Leader

### Project002 - Various Bug Fixes

#### Brief explanation:

There are around 30 open defects from the issue tracker.

#### Expected results:

A set of patches that address defects or implement features from the accepted issues in the issue tracker.

#### Knowledge Prerequisite:

Comfort with Java, Maven, SVN and JUnit are required.

**Mentor:** Arshan Dabirsiaghi - OWASP AntiSamy Project Leader

## AppSensor

The AppSensor project defines a conceptual framework and methodology that offers prescriptive guidance to implement intrusion detection and automated response into an existing application. Current efforts are underway to create the AppSensor tool which can be utilized by any existing application interested in adding detection and response capabilities. 

[Website](https://www.owasp.org/index.php/OWASP_AppSensor_Project)

[Mailing List](https://lists.owasp.org/mailman/listinfo/owasp-appsensor-project)

### Project 001 - SOAP web service server implementation

#### Brief explanation:

AppSensor is implementing a new service based architecture for the next version. This project would involve implementing a SOAP based web service (based on the WS-I Basic Profile standard) as a front-end to the AppSensor processing engine. 

#### Expected results:

A new SOAP based web service would be produced which provides a front-end to the existing processing core built into AppSensor.

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. Additionally, some knowledge of SOAP-based web services (particularly the WS-I Basic Profile standard) would be useful, but not essential. Finally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 002 - REST web service server implementation

#### Brief explanation:

AppSensor is implementing a new service based architecture for the next version. This project would involve implementing a REST based web service as a front-end to the AppSensor processing engine. 

#### Expected results:

A new REST based web service would be produced which provides a front-end to the existing processing core built into AppSensor.

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. Additionally, some knowledge of REST-based web services would be useful, but not essential. Finally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 003 - SOAP/REST web service client implementation

#### Brief explanation:

AppSensor is implementing a new service based architecture for the next version. This project would involve implementing SOAP and REST based web service clients in various languages to communicate to a back-end server that represents the AppSensor core engine. 

#### Expected results:

New SOAP and REST based web service clients would be produced which communicate to a back-end server that represents the AppSensor core engine.

#### Knowledge Prerequisite:

AppSensor is written in Java, and the initial client will be for Java, so a good knowledge of this language is recommended. Proficiency in one or more of the following languages would also be beneficial: C#, PHP, Python, Ruby. Additionally, some knowledge of REST and SOAP based web services would be useful, but not essential. Finally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 004 - Detection Point Implementation Expansion

#### Brief explanation:

AppSensor has documentation outlining around 50 different detection points. We currently have an existing implementation that supports a small handful (5-7) of those. Implementing additional detection points would increase the value of the project. 

#### Expected results:

Implementations of existing detection points would be produced. This could be done in any number of languages.

#### Knowledge Prerequisite:

AppSensor is written in Java, and the initial client will be for Java, so a good knowledge of this language is recommended. Proficiency in one or more of the following languages would also be beneficial: C#, PHP, Python, Ruby. Finally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 005 - Implement new configuration file format

#### Brief explanation:

AppSensor currently uses a properties file format for configuration. A new XML file format is planned. Moving to an XML format would simplify the configuration and make it easier to extend.

#### Expected results:

A new implementation of the configuration file would be created. An XML file format would be created, along with the code to process that file format, as well as an XSD to validate the file.

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. Additionally, a basic understanding of XML and XSD would be useful, though not required.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 006 - Trend Monitoring

#### Brief explanation:

Several of the detection point concepts for AppSensor revolve around the idea of trend monitoring within an application. There is a trivial implementation currently that provides very little utility. An enhanced trend monitoring capability would allow for the implementation of more detection points and expand the capabilities of AppSensor.

#### Expected results:

A new implementation of the trend monitoring module would be implemented.

#### Knowledge Prerequisite:

AppSensor is written in Java, so a good knowledge of this language is recommended. Additionally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader 

### Project 007 - Reporting

#### Brief explanation:

AppSensor currently has very weak reporting capabilities. Enhanced reporting would provide users with better insight into the health of the applications being protected by AppSensor

#### Expected results:

New APIs for reporting would be implemented as SOAP and/or REST based web services. Additionally, a reference implementation of a reporting client UI would be developed.

#### Knowledge Prerequisite:

AppSensor is written in Java, and the initial client will be for Java, so a good knowledge of this language is recommended. Some knowledge of REST and SOAP based web services would also be useful, but not essential. Additionally, some experience in a modern UI development framework would be beneficial, presumably an RIA style framework. Finally, basic knowledge of application security would be very helpful.

**Mentor:** John Melton - OWASP AppSensor Development Leader

## ESAPI
ESAPI (The OWASP Enterprise Security API) is a free, open source, web application security control library that makes it easier for programmers to write lower-risk applications. The ESAPI libraries are designed to make it easier for programmers to retrofit security into existing applications. The ESAPI libraries also serve as a solid foundation for new development.

[Website](http://www.esapi.org)

[Mailing List](https://lists.owasp.org/mailman/listinfo/esapi-dev)

### Project 001 - Port ESAPI 2.0.x to ESAPI-PHP

#### Brief explanation:

The ESAPI-PHP Project has become outdated and needs to be brought up-to-date with the latest ESAPI 2.0 specification. 

#### Expected results:

PHP-Library with ESAPI 2.x functionality.

#### Knowledge Prerequisites:

ESAPI 2.0.x is written in Java, so an understanding of the Java programming language is required as well as proficiency in PHP. Additionally, a basic understanding of application security would be desireable.

**Mentor:** Chris Schmidt - ESAPI Project Leader

### Project 002 - Resolve Bugs for ESAPI 2.1.0 Roadmap

#### Brief explanation:

There are several outstanding issues in the [ESAPI Bugtracker](http://code.google.com/p/owasp-esapi-java/issues/list) that need to be addressed for the 2.1.0 release.

#### Expected results:

Patches and unit tests to resolve the outstanding ESAPI issues.

#### Knowledge Prerequisistes:

Comfortable working in Java, writing unit tests using JUnit and creating patch files using svn.

**Mentor:** Chris Schmidt - ESAPI Project Leader / Kevin Wall - ESAPI Java Development Leader

### Project 003 - Develop Struts2 Components

#### Brief explanation:

Struts2 is one of the most widely used Java MVC frameworks, users of ESAPI are regularly looking for pluggable components that they can drop into their application to utilize ESAPI within the context of their application framework. The goal of this task is to create a set of pluggable components that integrate ESAPI into Struts2 to utilize ESAPI Encoders, Validation, and Intrusion Detection with the least amount of manual work and configuration.

#### Expected results:

A standalone project that uses ESAPI Components in a Struts2 add-on.

#### Knowledge Prerequisites:

A solid understanding of Java and Apache Struts, comfort developing unit tests in JUnit and functional tests using Selenium as well as maintaining a Maven build.

**Mentor:** Chris Schmidt - ESAPI Project Leader

### Project 004 - JSR-303 Bean Validation Provider

#### Brief Explanation

JSR-303 is a huge step forward in the way that validation is performed. There are currently 2 implementations of the JSR-303 specification - Hibernate-Validator and Apache BVal. Both of these libraries have demonstrated a lack of security driven validation and focused on using Constraints for business validation purposes. There are also key steps missing in the implementations, most notably - canonicalization of data prior to validation. The goal of this task will be to create a proof of concept implementation of the JSR-303 specification that passes all tests in the Java Compatibility Kit and utilizes the ESAPI Validators to implement constraints.

#### Expected results:

A proof of concept implementation of the JSR-303 specification as a standalone JAR

#### Knowledge Prerequisites:

Comfortable in Java, especially utilizing advanced JDK5+ features such as Annotations and writing custom annotation processors.

**Mentor:** Chris Schmidt - ESAPI Project Leader

### Project 005 - Mobile Service Provider

#### Brief explanation:

The mobile platform continues to grow exponentially and there has been very little movement of exposing security functionality to mobile applications. Creation of a mobile service platform that exposes security controls to mobile applications would make great strides towards providing mobile application developers with the means to write more secure code on mobile clients.

#### Expected results:

A WebService container (Jersey or SOAP) that exposes key controls (output encoding, input validation, secure logging, security policy, access control, authentication) to clients using a simple interface.

#### Knowledge Prerequisites:

Familiarity with Java and Apache-WS or Jersey. An understanding of the mobile platform would also be extremely useful.

**Mentor:** Chris Schmidt - ESAPI Project Leader

## WebGoat
The OWASP WebGoat is an intentionally vulnerable web application in Java. It's purpose is to be educational and covers a wide variety of web vulnerabilities and attacks, plus hints and ideas on how to exploit them.

[Website](https://www.owasp.org/index.php/Category:OWASP_WebGoat_Project)

[Mailing List](https://lists.owasp.org/mailman/listinfo/owasp-webgoat)

### Project 001 - WebGoatPHP

#### Brief explanation:

WebGoatPHP intends to deliver WebGoat to PHP/MySQL (and other SQLs) platform, which is embraces by numerous developers, and also introduce more recent and common attacks.

#### Expected results:

WebGoatPHP will be a vulnerable application, which provides PHP (and any other web) developers to realize common web threats and security flaws.  

#### Knowledge Prerequisites:

PHP, Subversion, Some TDD

**Mentor:** Abbas Naderi - WebGoatPHP Project Leader

### Project 002 - WebGoat Workshop

#### Brief explanation:

This part of WebGoat project intends to deliver workshop functionality to WebGoat, where an instructor could review participants progress and provide them with hints and opportunities, as a means to a successful web application security workshop.

#### Expected results:

WebGoat would be used by numerous people around the globe to increase web application security awareness.

#### Knowledge Prerequisistes:

PHP, Subversion

**Mentor:** Abbas Naderi - WebGoatPHP Project Leader

### Project 003 - WebGoat Contest

#### Brief explanation:

Taking WebGoat to a new level, WebGoat Contest enables workshop/contest administrator to limit some access, creating a virtual contest environment for web application security, while having some control over the process of contestants. 

#### Expected results:

This would encourage the community to add new challenges/scenarios/vulnerabilities to WebGoat so that more contests could be held. It also needs to be considerably Generic so that a one-time experience won't suffice.

#### Knowledge Prerequisites:

PHP, Subversion, TDD, MVC

**Mentor:** Abbas Naderi - WebGoatPHP Project Leader

## Hackademic
The OWASP Hackademic Challenges Project is an open source project that helps you test your knowledge on web application security. You can use it to actually attack web applications in a realistic but also controllable and safe environment. The Hackademic Challenges implement realistic scenarios with known vulnerabilities in a safe, controllable environment. Users can attempt to discover and exploit these vulnerabilities in order to learn important concepts of information security through the attacker's perspective.

[Website](https://www.owasp.org/index.php/OWASP_Hackademic_Challenges_Project)

[Mailing List](https://lists.owasp.org/mailman/listinfo/owasp-hackademic-challenges)

### Project 001 - Hackademic Challenges Standardization

#### Brief explanation:

The current challenges have been implemented in a rather simple and ad-hoc way by the initial project team so that they work best with the existing joomla front-end. Since then other contributors have expressed interest to contribute new challenges, but also use these challenges with different front-ends. 

#### Expected results:

A standard for challenges. The purpose of this standard will be two-fold: Firstly, anyone wishing to submit a challenge will have specific instructions and submitted challenges will be easily checked, audited and added to the platform. Secondly, submitted challenges should be usable in multiple platforms (e.g. joomla, wordpress, drupal, moodle, etc.) with minor adjustments. In addition all relevant documentation (teacher's guide etc.) should be standardized as well.

#### Knowledge Prerequisites:

HTML, PHP

**Mentor:** Konstantinos Papapanagiotou - Hackademic Challenges Project Leader

### Project 002 - Hackademic Challenges Frontend

#### Brief explanation:

Currently the OWASP Hackademic Challenges are based on a Joomla frontend and a MySQL backend that is used for score-keeping and storing user information. This interface needs to be further developed in order to facilitate teacher-student interaction (possibly provide real-time interaction functionality) and even student-student interaction.

#### Expected results:

New, possibly custom, frontend for the challenges that can be easily installed and used.

#### Knowledge Prerequisistes:

HTML, PHP

**Mentor:** Konstantinos Papapanagiotou - Hackademic Challenges Project Leader

### Project 003 - Develop new challenges

#### Brief explanation:

The challenges that have been implemented so far include: web application challenges covering several vulnerabilities included in the OWASP Top 10, cryptographic challenges, entire virtual machines including several vulnerabilities. New challenges need to be created in order to cover a broader set of vulnerabilities.

#### Expected results:

New challenges

#### Knowledge Prerequisites:

Comfortable in PHP, HTML and possibly Java. Good understanding of Application Security and related vulnerabilities. 

**Mentor:** Konstantinos Papapanagiotou - Hackademic Challenges Project Leader

## GoatDroid
The OWASP GoatDroid Project pays homage to the OWASP WebGoat Project. It is a fully self-contained environment for learning more about vulnerabilities and security issues for the Android platform.

[Website](https://www.owasp.org/index.php/Projects/OWASP_GoatDroid_Project)

### Project 001 - Develop a Social Commerce Application

#### Brief explanation:

The current applications (a location-based social networking app and a banking app) are currently standalone applications. A social commerce application will be used to glue these applications and APIs together in a way that will expose a broader attack surface.

#### Expected results:

Build a mobile application (with holes) that integrates (with even more holes) with the existing applications for payments and sharing via social media. This will require both an Android app and a web service. The existing web service capabilities are implemented in Java using Jersey. While maintaining the same architecture is desirable, developing the web service in a different language or framework is fine as it will provide diversity.

#### Knowledge Prerequisites:

A solid understanding of Android and web services. Java expertise is desirable, but the ideal candidate can also be experienced with MonoDroid, PhoneGap, or any cross platform framework.

**Mentor:** Jack Mannino - OWASP Mobile Security Project Lead/GoatDroid Lead

### Project 002 - Secure Forks of GoatDroid Apps

#### Brief explanation:

Each GoatDroid application is intentionally built to be insecure. While the new lessons and solution guides demonstrate how to solve these problems, the applications themselves do not contain the actual fixes. 

#### Expected results:

Develop fixes for each security issue, and create forks of each application that have these fixes applied. These applications will then be included with future distributions of GoatDroid and will be heavily referenced through the solution guides.

#### Knowledge Prerequisites:

A solid understanding of Android and Java. The candidate should also have some exposure to Jersey and Swing.

**Mentor:** Jack Mannino - OWASP Mobile Security Project Lead/GoatDroid Lead

## ModSecurity Core Rule Set
The OWASP ModSecurity Core Rule Set (CRS) Project provides a base set of attack detection rules for the popular [open source web application firewall](http://www.modsecurity.org/). 

[Website](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project)

[Mailing List](https://lists.owasp.org/mailman/listinfo/owasp-modsecurity-core-rule-set)

### Project 001 - Update the Lua port of the PHPIDS Converter Module

#### Brief explanation:

PHPIDS has an advanced normalization code section called Converter.php which applies counter-evasion methods to obscured attack payloads.  We have an initial Lua script that mimics this functionality.  We need to have it updated and tested.

#### Expected results:

The new Lua script will normalize all payloads in the same manner as the PHPIDS Converter.php code does. It will also employ the Centrifuge generic attack detection logic.

#### Knowledge Prerequisite:

[Lua scripting](http://www.lua.org/) and PHP.

**Mentor:** Ryan Barnett - OWASP ModSecurity CRS Project Leader

### Project 002 - Update the Lua Implementation of AppSensor Detection Points

#### Brief explanation:

We want to update the existing Lua scripts that implement the various AppSensor Detection Points - [implementing-appsensor-detection-points-in-modsecurity](http://blog.spiderlabs.com/2011/08/implementing-appsensor-detection-points-in-modsecurity.html.)

#### Expected results:

The new Lua script will implement more detection points to detect abnormal request attributes.

#### Knowledge Prerequisite:

[Lua scripting](http://www.lua.org/).

**Mentor:** Ryan Barnett - OWASP ModSecurity CRS Project Leader 

### Project 003 - Lua Script to Detect Application Flow Anomalies

#### Brief explanation:

Need a Lua script that can track normal application flow paths (click-flows) for business logic transactions - such as transferring money from accounts.  After profiling normal application path flows, we want to then be able to alert to anomalies.  This type of logic can help to prevent Banking Trojan attacks.

#### Expected results:

The new Lua script will be able to alert on anomalous application flows.

#### Knowledge Prerequisite:

[Lua scripting](http://www.lua.org/).

**Mentor:** Ryan Barnett - OWASP ModSecurity CRS Project Leader 

### Project 004 - Lua Script(s) to Identify User/System Trend Anomalies

#### Brief explanation:

Need Lua scripts to be able to track normal request velocities of user for resources and identify when they are abnormal.  The goal of these scripts will be to identify brute force, DoS and CSRF worm propagations.

#### Expected results:

The new Lua scripts will monitor normal request usage ranges and alert on anomlies.

#### Knowledge Prerequisite:

[Lua scripting](http://www.lua.org/).

**Mentor:** Ryan Barnett - OWASP ModSecurity CRS Project Leader
