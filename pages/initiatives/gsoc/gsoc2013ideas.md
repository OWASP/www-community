---
layout: full-width
title: GSoC 2013 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2013ideas
---
# GSoC 2013 Ideas

## OWASP Project Requests

###OWASP WebGoatPHP

#### Description

Webgoat is a deliberately insecure open source software made by OWASP using Java programming language. It has a set of challenges and steps, each providing the user with one or more web application vulnerability which user tries to solve. There are also hints and auto-detection of correct solutions. 
Since Java is not the most common web application programming language, and it doesn't have many of the bugs other languages such as PHP have when it comes to security, OWASP has OWASP_WebGoat_Reboot2012 dedicated in 2012 an amount of $5000 for promotion of WebGoatPHP.

If you want to know more about WebGoatPHP, I suggest downloading and giving WebGoat a try. It is one of OWASP prides (about 200000 downloads).

#### Expected Results:

WebGoatPHP will be a deliberately insecure PHP web application which operates in different modes. A contest mode where challenges are selected by an admin and the system starts a contest. Admins can open up hints for participants and manage everything. A workshop mode, where the educator has control of the most of application features, as well as feedback of user activities and is ideal for learning environments, and a single mode where someone can browse challenges and solve them.

#### Knowledge prerequisite:

You just need to know PHP. You are supposed to define flawed systems, which is not the hardest thing. Familiarity with web application security and SQL is recommended.

**Mentor:** Abbas Naderi

### OWASP CSRF Guard

#### Description

Cross-Site_Request_Forgery_(CSRF) is a complicated yet very effective web attack. The most important thing about CSRF is that it's hard to properly defend against it, specially when it comes to Web 2 and AJAX. We have had discussions on means of mitigating CSRF for years at OWASP, and are now ready to develop libraries for it. Many of the key ideas of this library can be found at [jcsrf.pdf](http://www.cs.sunysb.edu/~rpelizzi/jcsrf.pdf).

#### Expected Results:

A transparent Apache 2 module properly mitigating all POST CSRF attacks, as well as a lightweight PHP library doing the same.

#### Knowledge prerequisites:

Knowing CSRF and at least one way to defend against it, PHP, C/C++, Linux.

**Mentor:** Abbas Naderi

### OWASP PHP Security Project

#### Description

OWASP PHP Security project plans to gather around secure PHP libraries, and provide a full featured framework of libraries for secure web applications in PHP, both as separate de-coupled libraries and as a whole secure web application framework. Many aspects of this project are already handled, and are being added to OWASP.

#### Expected Results:

Result of this project is much more security among PHP applications. Most PHP applications are vulnerable and there's no central approach to secure them (due to open source nature). Many people look at OWASP for such information.

#### Knowledge prerequisite:

Anyone with adequate PHP programming language experience (possibly web application development in PHP).  There are hard and easy parts of this project. For tougher parts, familiarity with security concepts, advanced SQL, and advanced PHP and web server configuration is required. 

**Mentor:** Abbas Naderi

### OWASP RBAC Project

#### Description

For the last 6 years, improper access control has been the issue behind two of the Top Ten lists. 

RBAC stands for Role Based Access Control and is the de-facto access control and authorization standard. It simplifies access control and its maintenance for small and enterprise systems alike. NIST RBAC standard has four levels, the second level hierarchical RBAC is intended for this project.

Unfortunately because of many performance and development problems, no suitable RBAC implementation was available until recently, so developers and admins mostly used ACLs and other forms of simple access control methods, which leads to broken and unmaintainable access control over the time. 

OWASP provides the RBAC project, as a stand-alone library with very fast access control checks and standard mature code-base. Currently "PHPRBAC"" which is the PHP version of the RBAC project is released.

#### Expected Results:

Standard NIST level 2 hierarchical RBAC libraries for different programming languages, specially web-based ones such as C/C++/Java/ASP/ASPX/Python/Perl/etc.

#### Knowledge prerequisite:

Good SQL knowledge, library development schemes, familiarity with one of the programming languages.

**Mentor:** Abbas Naderi

**Skill Level:** Advanced

For more info, visit [phprbac.net](http://phprbac.net)

### OWASP XSSer Project

XSSer has a correct engine implementation to search/exploit XSS vulnerabilities, but it is necessary to work on some different fields to obtain better results. Some of them are: to fight against "false positive" results, to implemenet a better human-readable output results and to develop some new features (like; CSSer, Code checks user inputs, etc...). Also, it will be nice to update the tool with more valid XSS vectors (DOM, DCP, reflected, etc...) and some "anti-anti-XSS" systems for more common browsers. 

There is a roadmap on a pdf file with all tasks required to advance to next release of 'XSSer' (v1.7b - Total Swarm!)

[Download](http://xsser.sourceforge.net/xsser/xsser-roadmap.pdf)

#### Brief explanation:

Below is shown a structure of phases and milestones code areas.

Milestones:
- Phase 1: Core:
  - Bugfixing:
    - False positives
    - Fix “swarm” results
    - Fix 'maximize' screen (bug reported)
    - Add auto-update revision
    - Fix multithreading (review)
    - Research 'glibc' corruption

        - Add crawlering for POST+GET (auto test 'whole' page forms)
        - Update XSS payloads (vectors.py / DOM.py / DCP.py / etc...)
        - Advance Statistics results (show more detailed outputs)
        - Advance Exporting methods (create 'whitehat' reports (xml/json))
        - Advance “WebSockets” technology on XSSer 'fortune' option
        - Update Interface (GTK+)

    - Phase 2: New features:
        - Add 'code pre-check' option: Users can set which code will return target's website, to try to evade false positive results.
        - Add 'CSSer' option: Payloads for CSS injections.
        - Research/Search anti-IDS/NIDS/IPS... codes to evade XSS filters.
        - BurpXSSer: Create a Burp plugin (with Jython libs)
        - ZAPXSSer: Create a ZAP plugin (with Jython libs)

#### Expected results:

* To deploy a new stable version of XSSer with GTk+/Web/Shell main features working propertly,

The code should be:

* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

#### Knowledge Prerequisite:

XSSer is written in Python, so a good knowledge of this language is recommended, as is knowledge of HTML and Javascript. Also, is necessary to have some knowledge of application security and more in concret about XSS techniques.

**Skill Level:** Medium

**Mentor:** epsylon (psy) - OWASP XSSer Project Leader

### OWASP ZAP: Dynamically Configurable actions

ZAP provides various mechanisms which allow HTTP requests and responses to be changed dynamically. So (for example) a string in an HTTP request can automatically be changed to another string.

It also supports a scripting interface, which is very powerful but at the moment difficult to use.

This project would introduce something inbetween thess 2 options - a powerful way of defining (potentially) complex rules using a wizard based interface.

The challenge will be to make it as usable as possible while still providing a wide range of functionality.

#### Brief explanation:

This component would provide a set of highly configurable 'actions' which the user would see up via a wizard.

So they would initially define when the action applies, based on things like regex matching on request elements. And they should be able to define multiple criteria with ANDs and ORs.

Then they would define the actions, which could include:

* Changing the request (adding, removing or replacing strings)
* Raising alerts
* Breaking (to replace existing break points)
* Running custom scripts (which could do pretty much anything) 

They would then be able to switch the actions on and off from the full list of defined actions using checkboxes

#### Expected results:

* A new ZAP add-on providing the above functionality

The code should be:
* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### OWASP ZAP: Enhanced HTTP Session Handling

#### Brief explanation:

ZAP can currently manage multiple sessions. This development would allow ZAP to better handle HTTP Sessions to provide different views of a given target depending on the different user's permissions that the targeted site supports.

This implementation such provide a set of methods to answer questions such as: 1)What nodes(pages) are available to a group of users and not to other groups of users 2)What nodes are available to different users but these contain significant differences in the HTTP headers and/or in the body content.

This will allow ZAP to be used to detect access control issues which would otherwise require manual testing.
Expected results:

* ZAP will have an understanding of both users and roles and be able to associate them with HTTP sessions.
* The user will be able to associate credentials with different roles allowing ZAP to automatically authenticate as any user / role.
* ZAP will be able to spider an application using a given user/role.
* ZAP will be able to report the differences between different HTTP sessions.
* ZAP will be able to show different views of the site in the site's tree tab with the pages visible for each session.
* ZAP will be able to attack one session based on the URLs accessed in another session and report which appear to work. 

#### Expected results:

Users will be able to:
* specify exactly which alerts are included, by context, site or on an individual alert basis
* specify what information is included and how it is layed out
* specify a range of output formats, at least including HTML and PDF
* include details of what testing has been performed (automatically generated where possible)
* apply their own branding
* save report templates, and apply templates downloaded from the ZAP marketplace 
The code should be:
* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML and the HTTP protocol specification. Some knowledge of application security would be useful, but not essential.

**Mentor:** Guifre Ruiz - OWASP ZAP Dev Team


### OWASP ZAP: Exploring Advanced reporting using BIRT

#### Brief explanation:

BIRT (Business Intelligence and Reporting Tools) is an open source development framework used for report development. The objective of the project is to explore the development of advance reports in OWASP ZAP using the BIRT Report Designer, which is a an Eclipse plug-in that utilizes BIRT technologies.

Reports can be designed using the BIRT Report Designer; however a complete integration within OWASP ZAP is the ideal solution. This can be achieve integrating BIRT with OWASP ZAP since  the reporting application does not require the BIRT Report Designer user interface to generate a report.
The org.eclipse.birt.report.engine.api package contains the classes and interfaces that an application uses to generate reports. The main classes and interfaces are ReportEngine, EngineConfig, IReportRunnable, IRenderOption and its descendants, and IEngineTask and its descendants.

#### Expected results:

*Be able to Generate reports from the application using the BIRT report engine API.
*Creation of prototype reports regarding the results output of the Sessions & attacks such as: Alerts, History, Search etc.
*A new user interface for generating(design/configure) reports which is easy to use and provides the user with a wide range of options using the BIRT designer API
*Analysis report of the pros-and cons of using BIRT within OWASP ZAP as reporting tool

The code should be:
* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Johanna Curiel


### OWASP ZAP - SAML 2.0 Support

#### Brief explanation:

SAML 2.0 is an XML-based federated single sign-on (FSSO) protocol that uses security tokens containing assertions to pass information about a principal (usually an end user) between a SAML authority, that is an identity provider, and a SAML consumer, that is a service provider. SAML 2.0 enables web-based authentication and authorization scenarios including cross-domain single sign-on (SSO). SAML specifications support many ways, called profiles and bindings, to generate and transport assertions between trusted entities The Web Browser SSO profile is of particular interest here since it enables web applications from 2 separate domains to leverage SSO easily by exchanging assertions via a web browser session.

ZAP provides various mechanisms which allow HTTP requests and responses to be changed dynamically. This project will enhance those capabilities to be able to detect and fuzz various elements and attributes of a SAML Assertion.

The scope of this project is limited to the following SAML bindings, profiles and protocols:

Profiles :
* Web Browser SSO 

Bindings:
* HTTP POST
* HTTP Redirect 

Protocols:
* Authentication Request Protocol 

#### Expected results:

This component would enable ZAP to:
* Detect SAML Assertions in HTTP requests and responses
* Decode SAML Assertions
* Fuzz various entities and attributes within a SAML assertion
* Re-encode the assertion and send it forward 

The code should be:
* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

Users would have a choice either to fuzz the attributes within an assertion or just add/remove arbitrary attribute (to check for XML and SAML Schema Conformance).

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML and SAML 2.0 Protocol. Some knowledge of application security would be useful, but not essential. Understanding of SSO and Federated SSO is preferred.

**Mentor:** Prasad N. Shenoy

### OWASP ZAP: SOCKS support

This project is to extend ZAP to act as an intercepting proxy for SOCKS 4 and 5.

#### Brief explanation:

Suggested phases include:

* Identifying suitable Java SOCKS libraries
* Evaluating the SOCKS support other security tools provide (eg Mallory and Burp)
* Enhance ZAP to provide an option to use SOCKS for all outgoing connections
* Enhance ZAP to act as invisible SOCKS proxy
* Display the SOCKS data in ZAP
* Support searching of SOCKS data
* Support breaking and changing the data manually
* Support fuzzing SOCKS data
* Support SOCKS authentication 

The ZAP WebSockets addon should be used as an indication of how this could be achieved both technically and visually, but should not limit the implementation.

Each phase should be tested against 3rd party tools which use SOCKS and include stand alone unit tests. 

#### Expected results:

ZAP will be able to act as a SOCKS proxy, displaying the data sent and allowing it to be intercepted and changed. 

The code should be:
* Clean and easy to follow
* Include a full set of unit tests
* Include good documentation

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### OWASP ZAP: CMS Scanner 

#### Brief explanation:
A Content Management System (CMS) is a computer program that allows publishing, editing and modifying content as well as maintenance from a central interface. Such systems of content management provide procedures to manage workflow in a collaborative environment. These procedures can be manual steps or an automated cascade.

The first content management system (CMS) was announced at the end of the 1990s. This CMS was designed to simplify the complex task of writing numerous versions of code and to make the website development process more flexible. CMS platforms allow users to centralize data editing, publishing and modification on a single back-end interface. CMS platforms are often used as blog software.
in this project we are going to build a ZAP extension for CMS scanning (with enhanced search methdes)

#### Expected results:

A ZAP add-on to help the user in the process of identifying vulnerabilities in their CMS with a :
* version Fingerprinting
* Detecting Protection Measures Deployed by the site and there Vulns. (Firewalls ...) 
* Numeration of the version of the CMS
* Numeration of Plugins and Components in the CMS
* Enumerating different Vulns. in the core, plugins or templates    

#### Knowledge Prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

**Mentor:** Mennouchi Islam Azeddine

### OWASP Security Research and Development Framework 

#### Brief explanation:

This is a free open source Development Framework created to support writing security tools and malware analysis tools. And to convert the security researches and ideas from the theoretical approach to the practical implementation. 

This development framework created mainly to support the malware field to create malware analysis tools and anti-virus tools easily without reinventing the wheel and inspire the innovative minds to write their researches on this field and implement them using SRDF. 

#### Targeted Applications:

* Packet Analysis Tools (Personal Firewalls, HIDS/HIPS, WAF, Network Analysis, Network Capture)
* Malware Analysis Tools (Static, Dynamic, Behavioral)
* Antivirus and Virus Removal Tools (Signature-based, Behavioral-based)

#### Features:

The User Mode Features: 

* Assembler and Disassembler 
* x86 Emulator 
* Debugger 
* PE Analyzer 
* Process Analyzer (Loaded DLLs, Memory Maps … etc) 
* MD5, SSDeep and Wildlist Scanner (YARA) 
* API Hooker and Process Injection 
* Backend Database, XML Serializer 
* Packet Analysis Tool and Session Separation
* Protocol Analyzers for TCP,UDP,ICMP,ARP and Application Layer like HTTP and DNS
* and many more

The Kernel Mode Features:
 
* Object-oriented and easy to use development framework 
* Easy IRP dispatching mechanism 
* SSDT Hooker 
* Layered Devices Filtering 
* TDI Firewall 
* File and Registry Manager 
* Kernel Mode easy to use internet sockets 
* Filesystem Filter 

#### Future Plan
 
we need to do the following:

* WOW64 Hooker (Hooking system calls on wow64 processes .. it will be like an API hooker in a wrapper dll inside the wow64 processes)
* Improve our Kernel-Mode part to work on 64-bits and to implement NDIS, Kernel Sockets and Packet Filtering System (as we support TDI only and it's out-date)
* We need to implement SRDF in linux ... implement the file parsers and the packet analysis is easy .. but we need to implement memory analysis on linux and so on 
* We need to improve the static analysis tools .. we need to implement the X-RAY and Recursive Disassembler Tool
* we need to improve our dynamic analysis tools ... we need to support more APIs in Pokas Emulator and need more beta-testing
* we need to create a tool that do emulation and debugging (we have a debugger in SRDF) for beta-testing
* we need to improve the Behavioral Analysis Tools ... if you have ideas in behavioral analysis that's will be great
* we need to implement more file formats like swf and rtf
* we need to implement srdf in python using SWIG
* we need more improvement on memory usage and detecting memory-leaks
* we need to implement OpenSBI virus classification file format
* we need to collect static unpacking codes (static means no debugger, no breakpoints, no kernel-mode and no emulator . just decrypt using equations) for known unpackers like upx, fsg and so on. as a library for developers
* we need to implement zip library to decompress and rar library for the same
* we need a Process Analyzer for 64 applications .. and could it be done by a wow64 process?


#### Knowledge Prerequisite:

We need variety of skills in different languages and platforms. We need a good knowledge in C++ in windows. We need a python developer for integrating SRDF in python. We need C++ developers have a good knowledge in Assembly (for working in disassembling part) and we need C++ developers have a knowledge in Kernel-Mode(for Kernel-Mode improvement and beta-testing)

**Mentor:** Amr Thabet - OWASP Security Research and Development Framework Project Leader

###  OWASP ModSecurity CRS - Create "Sniffer-Mode" 

#### Brief explanation: 

The ModSecurity code includes a "standalone" version that wraps a light weight Apache/APR around the ModSecurity code.  This is used as the basis for the ports to the IIS/Nginx web server platforms.  The goal for this project task is to extend this standalone version so that it can accept a data feed of network traffic (e.g. libpcap) data as input and apply the ModSecurity CRS rules.  One possible solution would be create a ModSecurity "plugin" for the Snort IDS.

#### Expected results:

This new sniffer mode would allow organizations to run ModSecurity/OWASP ModSecurity CRS in an out of line mode as they do IDS systems.

#### Knowledge Prerequisite:

(C programming and ModSecurity Development Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Breno Silva and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

###  OWASP ModSecurity CRS - Port to Java 

#### Brief explanation: 

The goal is to have a ModSecurity version that can be used within Java servers (e.g. Tomcat).  There may be methods to use JNI to call the standalone code from a filter in Tomcat.

#### Expected results:

This new version allow organizations to run ModSecurity/OWASP ModSecurity CRS in Java web servers.

#### Knowledge Prerequisite:

(C programming and ModSecurity Development Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Breno Silva and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

###  OWASP ModSecurity CRS - Implement DoS Prevention Code 

#### Brief explanation:

[MODSEC-265](https://www.modsecurity.org/tracker/browse/MODSEC-265)

Implement a request velocity learning engine to identify dynamic DoS thresholds for both the site and for the particular URL.

#### Expected results:

The new C code in ModSecurity will allow us to add new DoS Protection methods to the OWASP ModSecurity CRS.

#### Knowledge Prerequisite:

(C programming and ModSecurity Development Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Breno Silva and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

###  OWASP ModSecurity CRS - Create a Positive Learning/Profile Engine 

#### Brief explanation: https://www.modsecurity.org/tracker/browse/MODSEC-193

ModSecurity needs a profiling engine that implements the various [AppSensor Detection Points](http://blog.spiderlabs.com/2011/08/implementing-appsensor-detection-points-in-modsecurity.html).

#### Expected results:

The new engine will implement more detection points to detect abnormal request attributes.

#### Knowledge Prerequisite:

C programming and ModSecurity Development Guidelines - http://www.modsecurity.org/developers/.

**Mentor:** Breno Silva and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

###  OWASP ModSecurity CRS - Create an Engine to Detect Application Flow Anomalies 

#### Brief explanation:

Need an engine that can track normal application flow paths (click-flows) for business logic transactions - such as transferring money from accounts.  After profiling normal application path flows, we want to then be able to alert to anomalies.  This type of logic can help to prevent Banking Trojan attacks.

#### Expected results:

The engine will be able to alert on anomalous application flows.

#### Knowledge Prerequisite:

[C programming and ModSecurity Development Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Breno Silva and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

###  OWASP OWTF - Stateful Browser with configurable authentication 

#### Brief explanation:

The automated functionality of OWASP OWTF is currently limited to the non-authenticated portion of a website. We would like to implement authentication support through:

1) OWTF parameters

2) Configuration files

What we would like to do here is to leverage the [powerful mechanize python library](http://wwwsearch.sourceforge.net/mechanize/) and build at least support for the following authentication options:
* Basic authentication - As requested here: [Issue 91](https://github.com/7a/owtf/issues/91).
* Cookie based authentication
* Form-based authentication

Additionally, we would welcome here a feature to detect when the user has been logged off, to log OWTF back in again before retrying the next request. <-- The proxy is probably a better place to implement this since external tools would also benefit from this. This feature will have to be coordinated with the MiTM proxy project below.

The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:

* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge Prerequisite:

Python, experience with the mechanize library or HTTP state is very welcome but not strictly necessary, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP OWTF - Inbound Proxy with MiTM and caching capabilities 

#### Brief explanation:

At the moment one of the most seriously lacking features of OWASP OWTF is the Inbound proxy. Desired features here include:
* Proxy mode: Ability to start OWTF in "proxy mode" so that a human can review a site manually while taking advantage of all the OWTF grep plugins, without launching any tools.
* Proxy cache: At present, OWTF runs external tools to save time to a human pentester, the proxy cache would make OWTF smart enough to make external tools use the OWTF proxy and then avoid sending identical requests to the site (i.e. if 30 tools run by OWTF try to request X, OWTF will only make 1 request and not 30 anymore). OWTF should also be smart enough to use its own cache obviously :). The cache should be smart enough to detect lack of disk space and crashing :).
* Proxy throttling: We would like the proxy to auto-adjust speed to the speed of the target (i.e. based on how slower response times are getting) in a configurable fashion
* Proxy retry: We would like to have the ability to retry failed requests in an automated fashion for a configurable number of times 
* Proxy MiTM: Proxy Man in The Middle capabilities are a must on any web app security tool. We need the ability to create a fake certificate on the fly to intercept and be able to analyse communications going to and from an "https" site.
* HTTP Transaction storage: The whole point here is of course, to store the HTTP transactions in the same way 

Potential python libraries and references that could help here are: 
* [twisted web proxy](http://twistedmatrix.com/documents/10.0.0/api/twisted.web.proxy.Proxy.html)
* [sslstrip](https://github.com/moxie0/sslstrip)
* [Current WIP OWTF state in this regard](https://github.com/7a/owtf/tree/master/framework/http)

The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Additional Information and Suggestions (based on student questions):

* "Inbound" is used here to differenciate from the existing outbound proxy functionality in OWTF (-x switch), in practice, the "inbound" proxy will have to refactor/reimplement the "outbound" proxy functionality: Therefore this is both inbound and outbound obviously.


#### Expected results:

* Increased overall performance: We should only be sending each probe once ever if several tools try to send the same HTTP request multiple times.
* Additional HTTP transactions logged for analysis
* Test cases
* Good documentation

#### Knowledge Prerequisite:

Python, previous exposure to Twisted Proxy or other python HTTP proxies will be very welcome here, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP OWTF - Reporting 

#### Brief explanation:

A common complaint about OWASP OWTF so far has been that the report is not very shiny. The intention here is to:
* Move as much of the HTML away from python files into template files: This will facilitate web designer's work in the future.
* Apply some nice web design to the report so that it is more nice and comfortable to work with: Clear the HTML, CSS, etc
* Identify and fix areas of improvement in click flow: For example, try to reduce the distance to move the mouse (mouse is sweeping left to right all the time now to rank vulnerabilities and then click on the next plugin)
* Improve the interactive report load time: The report will be pretty big when you scan 30+ websites, we might have to change things so that each plugin is retrieved via AJAX instead of loading every iframe on load
* Reduce the interactive report load and improve responsiveness: Big reports can take a few seconds to load and warnings like "this site is not responding" are undesired, we would like to reduce the HTML and JavaScript load to make the report faster to use.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Additional Information and Suggestions (based on student questions):

* Play with the interactive reports to see where we are now (get the OWTF 0.15 one, <b>no need to install anything</b>): [demos](https://github.com/7a/owtf_demos)
* Reports are created with [report framework](https://github.com/7a/owtf/tree/master/framework/report) and [includes](https://github.com/7a/owtf/tree/master/includes) producing interactive reports such as [demos](https://github.com/7a/owtf_demos)
* How it works at the moment: Each plugin creates its own small report which is loaded by the main report in an iframe, this will make more sense when you play with the interactive demos and look at the source.
* How the report is meant to be used: I would suggest to watch the live demos in this talk to get the drift of this (Demos start after 1h approx.): [talk](http://www.rubcast.rub.de/index2.php?id=1009)
* How the report is created now: Each plugin report is created right after each plugin finishes, then the master report is reassembled again: This approach is not very efficient so I am open to alternatives. Not all plugins run tools, some plugins run OWTF checks. But the report will be re-written each time a plugin finishes (using the current approach)
* Report output file formats at the moment are: .txt (for tool output and some checks) and .html (for tool output and the report itself)
* Project documentation links: [readme](https://github.com/7a/owtf/tree/master/readme], [wiki](https://github.com/7a/owtf/wiki https://github.com/7a/owtf/wiki), [presentations](http://www.slideshare.net/abrahamaranguren/presentations)

#### Expected results:

* The first reaction when an OWASP OWTF users opens the report is now "wow"
* The report is reliable and easy to work with, even when more than 30 URLs have been assessed (i.e. a lot of data in the report does not crash or make the browser slow)
* The improved design is lightweight and keeps the browser responsive at all times

#### Knowledge Prerequisite:

HTML, JavaScript, CSS and a bit of Python. Web Designer background or experience would be beneficial for this.

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP OWTF - Multiprocessing 

#### Brief explanation:

OWASP OWTF can be quite slow when scanning multiple URLs simultanously due to not scanning several hosts in parallel. We would like to use the multiprocessing python library over the threading one to take full advantage of multi-core processors without the global interpreter lock (GIL) issues associated with the threading libary :)
* We would like to scan in parallel several websites when on a different IP: 
* We would like to monitor the host machine resources to avoid crashing it before spawning new processes :)
* We would like to run plugins in parallel as much as possible but without compromising integrity: Using file locks where appropriate and so on

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Additional Information (based on student questions):

OWTF works by targets, where a target can be:
* A URL: For web plugins
* Anything else (i.e. an email, an IP address): For aux plugins

This is done [here](https://github.com/7a/owtf/blob/master/framework/plugin/plugin_handler.py#L257)

For multiprocessing you would probably need to change the following so that a [new process is launched for each IP address](https://github.com/7a/owtf/blob/master/framework/plugin/plugin_handler.py#L271)

The way it works is that the plugin handler sends URLs to the plugins, so plugins are responsible for the checks while the plugin handler is responsible for distributing the work. This means multiprocessing will require changing the plugin handler but should not require to change the plugins (at least most of them).

#### Expected results:

* Reliability
* Test cases
* Good documentation

#### Knowledge Prerequisite:

Python, multiprocessing experience would be beneficial for this, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - SQL database

#### Brief explanation:

OWASP OWTF scans may take a large amount of disk space due to saving information in text files, we would like to add an option to use a SQL database, probably using the sqlalchemy python library.
* Keep the current text file format as an option
* Add a database storage option using the sqlalchemy library 

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:

* Reliability: Both with the sql database option and the text file options.
* Test cases
* Good documentation

#### Knowledge Prerequisite:

Python, sqlalchemy experience would be beneficial for this

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP OWTF - Unit Test Framework 

#### Brief explanation:

As OWASP OWTF grows it makes sense to build custom unit tests to automatically re-test that functionality has not been broken. In this project we would like to create a unit testing framework so that creating OWASP OWTF unit tests is as simple as possible. The goal of this project is to create the Unit Test Framework and as many unit tests as possible to verify OWASP OWTF functionality.

The Unit Test Framework should be able to:
* Define test categories: For example, "all plugins", "web plugins", "aux plugins", "test framework core", etc. (please see [this presentation](http://www.slideshare.net/abrahamaranguren/introducing-owasp-owtf-workshop-brucon-2012) for more background)
* Allow to regression test isolated plugins (i.e. "only test _this_ plugin")
* Allow to regression test by test categories (i.e. "test only web plugins")
* Allow to regression test everything (i.e. plugins + framework core: "test all")
* Produce meaningful statistics and easy to navigate logs to identify which tests failed and ideally also hints on how to potentially fix the problem where possible
* Allow for easy creation of _new_ unit tests specific to OWASP OWTF
* Allow for easy modification and maintenance of _existing_ unit tests specific to OWASP OWTF
* Perform well so that we can run as many tests as possible in a given period of time
* Potentially leverage the python [unittest library](http://docs.python.org/2/library/unittest.html)

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:

* Performant and automated regression testing
* Unit tests for a wide coverage of OWASP OWTF, ideally leveraging the Unit Test Framework where possible
* Good documentation

#### Knowledge Prerequisite:

Python, experience with unit tests and automated regression testing would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP OWTF - Python version upgrade and compatibility 

#### Brief explanation:

Right now OWASP OWTF works on Python 2.6.5-2.7.3 (might work on surrounding versions too), the aim of this project would be to change the existing codebase so that it additionally works on newer python versions too, for example Python 3.3.
The intention here is to take advantage of improvements in newer python versions when available while letting OWASP OWTF work on older python versions too (i.e. 2.6.5) if that is the only option available.
The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable due to compatibility.


For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected results:

* Performant and reliable OWASP OWTF execution on multiple python versions, in particular the latest python version (i.e. 3.3.x) as well as the previous 2.6.5-2.7.3 range.
* Test cases
* Good documentation

#### Knowledge Prerequisite:

Python, experience with python version upgrades and python version compatibility implementations, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

*Mentor:* Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

###  OWASP Hackademic Challenges - New challenges and Improvements to the existing ones 

#### Brief explanation:

The challenges that have been implemented so far include: web application challenges covering several vulnerabilities included in the OWASP Top 10, cryptographic challenges, and entire virtual machines including several vulnerabilities.
New challenges need to be created in order to cover a broader set of vulnerabilities.
Also existing challenges can be modified to accept a broader set of valid answers, e.g. by using regular expressions.

Ideas on the project:

* Simulated simple buffer overflows
* SQL injections
* Man in the middle simulation
* Bypassing regular expression filtering
* Your idea here

#### Expected results:

New cool challenges

#### Knowledge Prerequisites:

Comfortable in PHP, HTML and possibly Javascript. Good understanding of Application Security and related vulnerabilities. 

##### Note:
The ideas on each proposed project are examples, it would be good if you undertook any of these but we equally value creativity and we are always looking for awesome new features to add to the project, so if you have an idea don't be shy, contact us. :-)

**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

###  OWASP Hackademic Challenges - Source Code testing environment 

'#### Brief explanation:

Existing challenges are based on a dynamic application testing concept. We would like to work on a project that will give the capability to the attacker to review a vulnerable piece of source code, make corrections and see the result in a realistic (but yet safe) runtime environment. The code can either be run if needed or tested for correctness and security. The implementation challenges of such a project can be numerous, including creating a realistic but also secure environment, testing submitted solutions and grading them in an automatic manner. At the same time there are now numerous sites that support submitting code and then simulate or implement a compiler's functionality.

#### Expected results:

A source code testing and improvement environment where a user will be able to review, improve and test the result of a piece of source code.

#### Knowledge Prerequisites:

Comfortable in PHP, HTML and possibly Java. Good understanding of Application Security, source code analysis and related vulnerabilities. 

##### Note:
The ideas on each proposed project are examples, it would be good if you undertook any of these but we equally value creativity and we are always looking for awesome new features to add to the project, so if you have an idea don't be shy, contact us. :-)


**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

###  OWASP Hackademic Challenges - CMS improvements 

#### Brief explanation:

The new CMS was created during last year's GSOC. We have received feedback from users that suggest various improvements regarding functionality e.g. better user, teacher and challenges management. There are also some security improvements that are needed and in general any functionality that adds up to the educational nature of the project is more than welcome.

Ideas on this project:

* Plugin api and plugin actions interface

An easy way for users to code their own plugins which will modify the appearance of hackademic or add to the functionality.

* Ability to show different articles on the user's home screen

Now each user is served the latest article in their home screen. We need the ability for either the teacher/admin to be able to define what article each class is served.

* Ability to define series of challenges

The teacher/admin should be able to define a series of challenges (e.g. 2,5,3,1) which are meant to be solved in that order and if one is not solved then the student can't try the next one.

* Tagging of articles, users, challenges

A user should be able to put tags on articles and challenges if they are a student and on users, classes, articles and challenges if they are a teacher.
Also the user should be able to search according to the tags.

* Your idea here

We welcome new ideas to make the project look awesome.

#### Expected results:

New features  and security improvements on the CMS part of the project.

#### Knowledge Prerequisites:

Comfortable in PHP and HTML. Good understanding of Application Security and related vulnerabilities if you undertake security improvements. 

##### Note:
The ideas on each proposed project are examples, it would be good if you undertook any of these but we equally value creativity and we are always looking for awesome new features to add to the project, so if you have an idea don't be shy, contact us. :-)

**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### OWASP ESAPI/Java WAF - Release level

#### Description

OWASP_WAF_Project is an embedded WAF based on The_ESAPI_Web_Application_Firewall_(ESAPI_WAF) Web Application Firewall. Unlike other open source solutions. JAVA WAF works as a java filter and thus integrates with protected application in an natural way. Also, since the WAF is embedded into the application it "travels" with it, this is, migrating a protected application to another environment does not imply reinstallation, reconfiguration or any additional effort that might render the application unprotected at any time after WAF is initially configured.

#### Expected Results:

ESAPI WAF is beta level and provides good protection as it is. However, some synchronization issues identified, lack of compatibility with any other OWASP tools and massive lack of documentation, made it hard to use. Final result of the project will be a production/release level WAF with massive Unit testing of all functionality, ModSecurity log format, user friendly documentation (including a user guide, examples of protection using WebGoat or Swingset) and proven stability by doing basic performance testing.

#### Knowledge prerequisite:

Java Web and Java Filter programming, JUnit unit testing. Filter programming is simple so it is not really a prerequisite as could be learned in short time. It is desirable to be familiar with Request and response Wrappers, and mod-security logs.

**Mentor:** Juan Carlos Calderon

### OWASP Classic ASP ESAPI rewrite

#### Description

Classic_ASP_Security_Project is a port of the famous ESAPI for Java. In particular, Classic ASP version works with ASP.NET port by using Interop. However interop technology is not stable and has many issues like many requirements to  work properly, non understandable error messages, unexpected errors and dependencies to third party libraries. Also ASP.NET version of ESAPI is not release level.

25 years later there are still millions of applications on the wild as proven by the massive automated Sql injections targeting Classic ASP pages in later years. An effective solution that does not require complete rewriting of applications is still required.

#### Expected Results:

A new ESAPI for classic ASP applications that will be based on good old COM+ components or .NET HTTP Modules. This inital version should provide protection against most pervasive issues and thus will include functionality for input validation, output encoding, basic encryption, file and DB based authentication/authorization. If time is left additional ESAPI functionality might be also included. An installation Guide and a comparative of functionality with Java ESAPI. Proper Unit testing for all functionality. No user manual as Java version documentation will be used for that purpose.

#### Knowledge prerequisite:

Classic ASP, either COM+ (Visual Basic or any C++ COM framework) or ASP.NET HTTP Modules programming. NUnit unit testing. HTTP Module programming is simple so it is not really a prerequisite as could be learned in short time. Experience with JAVA ESAPI is a plus.

**Mentor:** Juan Carlos Calderon

###  ESAPI 
ESAPI (The OWASP Enterprise Security API) is a free, open source, web application security control library that makes it easier for programmers to write lower-risk applications. The ESAPI libraries are designed to make it easier for programmers to retrofit security into existing applications. The ESAPI libraries also serve as a solid foundation for new development.

[Website](http://www.esapi.org/)

[Mailing List:](https://lists.owasp.org/mailman/listinfo/esapi-dev)

### Project 001 - Port ESAPI 2.0.x (Java) to ESAPI .NET

#### Brief explanation:

The ESAPI .NET Projects has become outdated and need to be brought up-to-date with the latest ESAPI 2.0 specification. 

#### Expected results:

ESAPI .NET with ESAPI 2.x functionality.

#### Knowledge Prerequisites:

ESAPI 2.0.x is written in Java, so an understanding of the Java programming language is required as well as proficiency in .NET/C#. Additionally, a basic understanding of application security would be desirable.

[Website](http://code.google.com/p/owasp-esapi-dotnet/)

**Mentor:** Kevin Wall - ESAPI Java Project Leader

### Project 002 - Resolve Bugs for ESAPI 2.1.0 Roadmap ###

#### Brief explanation:

There are several outstanding issues in the [ESAPI Bugtracker](http://code.google.com/p/owasp-esapi-java/issues/list) that need to be addressed for the 2.1.0 release.

#### Expected results:

Patches and unit tests to resolve the outstanding ESAPI issues.

#### Knowledge Prerequisistes:

Comfortable working in Java, writing unit tests using JUnit and creating patch files using svn.

[Website](http://code.google.com/p/owasp-esapi-java/issues/list)

**Mentor:** Kevin Wall - ESAPI Java Project Leader
