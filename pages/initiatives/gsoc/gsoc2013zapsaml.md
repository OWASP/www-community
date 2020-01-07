---
layout: full-width
title: GSoC 2013 - ZAP SAML Support Status Updates
tags: gsoc
permalink: /initiatives/gsoc/gsoc2013zapsaml
---
# GSoC2013 - OWASP ZAP SAML Support

**Student** : Pulasthi Mahawithana

**Mentors** : Prasad Shenoy, Kevin Wall

## Introduction
The OWASP Zed Attack Proxy (ZAP) is an easy to use integrated penetration testing tool for finding vulnerabilities in web applications. It is open-source under Apache License 2.0 and widely used by the computer security community.

SAML is an XML-based federated single sign-on (FSSO) protocol that uses security tokens containing assertions to pass information about a principal between a SAML authority (an identity provider), and a SAML consumer (a service provider). It enables web-based authentication and authorization scenarios including cross-domain single sign-on (SSO).

The Objective of this project is to develop a component for ZAP that will detect and fuzz various elements and attributes of a SAML Assertion.

## Project Goals, Scope and Deliverables, Implementation Plan
Please refer the [GSoC proposal](http://www.google-melange.com/gsoc/proposal/review/google/gsoc2013/pulasthi7/19001) for the project idea.

## Project Code, Documentation
Development will be done in an [external code repository](https://github.com/pulasthi7/zap-saml-extension) hosted at GitHub.

### Pre-Releases

* [0.1-alpha](https://github.com/pulasthi7/zap-saml-extension/releases/tag/0.1a) Jul 29, 2013
* [0.2-alpha](https://github.com/pulasthi7/zap-saml-extension/releases/tag/0.2a) Aug 12, 2013
* [1.0-alpha](https://github.com/pulasthi7/zap-saml-extension/releases/tag/v1.0-alpha) Sep 20, 2013

## Project Progress
### Community bonding period (before 17th June)

Agreed to have video conference twice a week on Monday and Thursday to discuss the project progress and any issues that may occur.

* Clarification of project idea
* Read the SAML specs to get familiar with SAML standards and usages
* Identifying the use cases that need to be implemented
* Setting up the development environment.

### Week 1 (17th June - 23rd June)

#### Week's progress
* Finalizing the use cases
* Setting up the Third party applications to generate SAML requests/responses
* Intercepting the SAML requests/responses from ZAP and get familiar with the parameters
* Studying on  ZAP core and extensions to start the coding

#### Plans for next week
* Intercept the requests and responses and log them to console/file

### Week 2 (24th June - 30th June)

#### Week's progress
* Created a project at GitHub for the development of the [extension](https://github.com/pulasthi7/zap-saml-extension)
* Created a passive scanner to intercept and log SAML requests/responses in their raw values 
* Wrote a component that can decode the SAMLRequest/ SAMLResponse parameters in a HTTP request
* Updated the passive scanner to log the decoded SAML messages to the console
* Studied on the ZAP's extension API

#### Plans for next week
* Design the UI for the extension
* Provide ability to view SAML messages in a GUI in readable XML format

### Week 3 (1st July - 7th July)

#### Week's progress
* Created an UI for resending Requests
* Added a hook to show the Extension Resender UI
* Added the ability to show the parameters and decoded SAML request in the resender UI

#### Plans for next week
* Implement Resend ability to the resender
* Parse and show the SAML parameters one by one and provide the ability to change parameters independently (Easier way than changing the whole message)

### Week 4 (8th July - 14th July)

#### Week's progress
* Worked on implementing the resender
* Designed mock UI for the active mode request editor

#### Plans for next week
* Finish the passive request resender
* Start the implementation of active request editor/resender.

### Week 5 (15th July - 21st July)

#### Week's progress
* Study on OpenSAML libraries
* Added the ability to view attribute name and value pairs for some frequently occurring attributes of SAML Auth requests
* Faced with a issue on packaging external libraries

#### Plans for next week
* Solve the issue with packaging the libraries
* Implement sending functionality for changed request
* Provide the ability to dynamically update attribute values and SAML message when either one changes
* Implement the ability to parse different SAML message types

### Week 6 (22nd July - 28th July)

#### Week's progress
* Got the issue with packaging the libraries fixed.
* Reset the development environment which was reverted to solve the packaging issue
* Added sending functionality for changed SAML message and retrieve the response
* Added the ability to update the SAML message/ Attributes dynamically on change of either.
* Added the ability to parse, view and edit SAML Response type messages
* Added a pre-release version (0.1-alpha) with the current progress. Source and binary are available at [temporary GitHub repository](https://github.com/pulasthi7/zap-saml-extension/releases/tag/0.1a)

#### Plans for next week
* Implement automatic attribute changing and resending
* Implement UI to set the automatic attribute changer settings

### Week 7 (29nd July - 04th August)

#### Week's progress
* Implemented the UIs for automatic attribute changer settings 

#### Plans for next week
* Implement automatic attribute changing and resending
* Implement passive SAML request scanner to edit the requests
* Add the ability to save/load the configurations

### Week 8 (05th August - 11th August)

#### Week's progress
* Implemented predefined automatic attribute changing and sending to endpoint
* Implemented the passive scanner to intercept the SAML messages to edit them
* Added ability to save/load configurations to the files for later user

#### Plans for next week
* Bug fixes for the passive scanner component
* Prepare presentation for AppSec EU

### Week 9 (12th August - 18th August)

#### Week's progress
* Prepared presentation for AppSec EU
* Some bug fixing for passive scanner component

#### Plans for next week
* Start working on the XSW attack implementation
* Add support to change relay state parameter

### Week 10 (19th August - 25th August)

#### Week's progress
* Research on XSW attacks
* Testing the SPs against signature exclutions

#### Plans for next week
* Implement and integrate XSW attack ability to extension
* Add support to change relay state parameter
* Start on testing the extension

### Week 11 (26th August - 01st September)

#### Week's progress
* Changed the extension to use JAXP and XPath to change the attribute values (Removing OpenSAML dependency)
* Combined the extension configurations to save to/ load from a single xml file.
* Introduced type validation to attributes when changing their values. (i.e. String, Integer, TimeStamp...)
* Started on unit and integration testing

#### Plans for next week
* Write unit tests and integration tests
* Update XSW attack ability to new architecture
* Add support to change relay state parameter

### Week 12 (02nd September - 08th September)

#### Week's progress
* Started on writing tests for extension
* Added XSW attack ablility

#### Plans for next week
* Improve test coverage
* Add support to change relay state
* Allow to set various configuration related to the extension
* Code clean up

### Week 13 (09th September - 15th September)

#### Week's progress
* Added more unit/integrations tests
* Added support to change relay state
* Added the ability to change various configurations
* Some Bug fixes/ UI fixes and clean up

#### Plans for next week
* Clean up the code
* Compose the documentation
