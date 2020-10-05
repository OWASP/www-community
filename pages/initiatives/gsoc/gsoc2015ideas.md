---
layout: full-width
title: GSoC 2015 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2015ideas
---
# GSoC 2015 Ideas

## OWASP Project Requests

Tips to get you started in no particular order:
- Read the [GSoC SAT](gsoc_sat).
- Contact us through the mailing list or irc channel.
- Check our [github organization](https://github.com/OWASP).

## OWASP Hackademic Challenges

OWASP Hackademic Challenges Project]]  helps you test your knowledge on web application security. You can use it to actually attack web applications in a realistic but also controllable and safe environment. After a wonderfull 2014 GSoC with 100 new challenges and a couple of new plugins we're mainly looking to get new features in and maybe a couple of challenges. Bellow is a list of proposed features.

### Web Sandbox

#### Brief Explanation:

After a very successfull OWASP Winter Code Sprint we have a brand new Sandbox feature which uses Linux Containers to create virtual space for each user. So we can host properly vulnerable challenges and maybe execute some code server side. However, the sandbox is not fully complete, we need many features here and there to make it easily deployable and improve it's administration.

Ideas on the project:

* Simple sandbox administration frontend for the web. -- An admin console to start and kill sandboxes manually and to list the status and resources used by each one.
* Secure the implementation -- Now we have a functioning prototype, we know that Linux Containers are quite safe but we haven't explicitly tested our configuration and use of them.
* Your idea here...

#### Expected Results:

Better sandboxing

#### Knowledge Prerequisites:

Comfortable in Linux administration and some security knowledge depending on the specific project.

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### Source Code testing environment - Defensive Challenges

#### Brief Explanation:

Existing challenges are based on a dynamic application testing concept. We would like to work on a project that will give the capability to the attacker to review a vulnerable piece of source code, make corrections and see the result in a realistic (but yet safe) runtime environment. The code can either be run if needed or tested for correctness and security. The implementation challenges of such a project can be numerous, including creating a realistic but also secure environment, testing submitted solutions and grading them in an automatic manner. At the same time there are now numerous sites that support submitting code and then simulate or implement a compiler's functionality.

#### Expected Results:

A source code testing and improvement environment where a user will be able to review, improve and test the result of a piece of source code.

#### Knowledge Prerequisites:

Comfortable in PHP, HTML. Good understanding of Application Security, source code analysis and related vulnerabilities. 

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### Student performance analytics

#### Brief Explanation:

We need a better way to measure the student's performance and how it varies depending on the problem. You will write a plugin (or make changes to the core depending on your implementation proposal) to gather all sorts of performance data and present them in a meaningfull way.

#### Expected Results:

A page to view performance metrics of differenct students.
( Hackalytics )

#### Knowledge Prerequisites:

Comfortable in PHP, HTML, javascript. Some understanding of analytics.

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### New Template

#### Brief Explanation:

We need a cool new template since the old one is getting pretty old.
You can do it  using the latest frontend bells and whistles (like angular,bootstrap or the tools of your choice).

#### Expected Results:

A new template.

#### Knowledge Prerequisites:

Comfortable in Css, HTML, javascript and/or the tools you plan on using.

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### Gamification

#### Brief Explanation:

Gamification is a feature widely used in many learning platforms out there and it would be nice if we could have it too.
You will need to design and implement the awards, badges and whatever other feature you have in mind. You will also implement the front and backend changes necessary to present the results.

#### Expected Results:

Gamification of the platform. ( Hackademicification )

#### Knowledge Prerequisites:

Comfortable in Css, HTML, javascript and/or the tools you plan on using.

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### Your idea

#### Brief Explanation:

Hackademic is it's community, we always welcome new ideas and cool features. Come over to the irc channel or mailing list and propose something.
We'd be happy to help you get it done.

#### Expected Results:

Features we didn't know we needed. ;-)

#### Knowledge Prerequisites:

Comfortable in whatever tools and languages you plan on using.

#### Mentors:
Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

## OWASP WebGoat .NET - Vulnerable Website

#### Brief Explanation:

The actual WebGoat .NET is a vulnerable website built in ASP.NET using C#. There are some challenges already built in but we would like to add more vulnerable features
https://www.owasp.org/index.php/Category:OWASP_WebGoat.NET#tab=Overview

#### Expected Results:

We want  to add more modules such as 
*WebSockets
*CSRF challenge
*Finalise testing an upgrade to the .NET framework 4.5
*Retest and clean up actual modules

#### Knowledge Prerequisites:

Comfortable in .NET, HTML and C#. Good understanding of Application Security, source code analysis and related vulnerabilities. 

#### Mentors:
Johanna Curiel, Jerry Hoff - OWASP WebGoat Project Leaders

## OWASP WebGoatPHP

### OWASP WebGoatPHP

#### Description:
Webgoat]] is a deliberately insecure open source software made by OWASP using Java programming language. It has a set of challenges and steps, each providing the user with one or more web application vulnerability which user tries to solve. There are also hints and auto-detection of correct solutions. 
Since Java is not the most common web application programming language, and it doesn't have many of the bugs other languages such as PHP have when it comes to security, OWASP has an amount of $5000 for promotion of WebGoatPHP.

If you want to know more about WebGoatPHP, I suggest downloading and giving WebGoat a try. It is one of OWASP prides (about 200000 downloads).

#### Expected Results: WebGoatPHP first version is ready, it needs thorough testing and delivery. It also needs new challenges added and a CTF hosted on it.

#### Knowledge Prerequisite: 
You just need to know PHP and SQL. Familiarity with web application security is recommended.

#### Mentor:
Abbas Naderi

## OWASP PureCaptcha

### OWASP PureCaptcha

#### Description: 
OWASP PureCaptcha is an OWASP project aiming to simplify CAPTCHA usage. Instead of proving rigorous APIs and many dependencies, it is a single source code file (library) that does not depend on anything and generates secure and fast CAPTCHAs, with little memory and processor footprint.
PureCaptcha is currently released for PHP. The candidate will port this to several other programming languages (priority on web languages) and provide full test coverage.

#### Expected Results: 
PureCaptcha library for at least 3 new programming languages. Unit testing for the core version. A study on security of the generated captcha can also be performed.

#### Knowledge Prerequisites: 
Any programming language you want to port into, as well as PHP.

#### Mentor:
Abbas Naderi, Jesse Burns

## OWASP PHP Framework

### OWASP PHP Framework

#### Description:
OWASP PHP Security project plans to gather around secure PHP libraries, and provide a full featured framework of libraries for secure web applications in PHP, both as separate de-coupled libraries and as a whole secure web application framework. Many aspects of this project are already handled, and are being added to OWASP.
The project has been done in the last two years, and now a framework has been built upon these libraries and security best practices. The framework intends to merge security practices with practical frameworks, and aims to be simple and lightweight.

#### Expected Results:
A secure yet robust and practical framework for PHP developers.

#### Knowledge Prerequisite:
This project requires at least one year of experience working with different PHP projects and frameworks. It will be too hard for someone with average PHP experience.

#### Mentor:
Abbas Naderi, Rahul Chaudhary

#### Skill Level:
Advanced

## OWASP RBAC Project

### OWASP RBAC Project

#### Description: For the last 7 years, improper access control has been the issue behind two of the Top Ten lists.

RBAC stands for Role Based Access Control and is the de-facto access control and authorization standard. It simplifies access control and its maintenance for small and enterprise systems alike. NIST RBAC standard has four levels, the second level hierarchical RBAC is intended for this project.

Unfortunately because of many performance and development problems, no suitable RBAC implementation was available until recently, so developers and admins mostly used ACLs and other forms of simple access control methods, which leads to broken and unmaintainable access control over the time. 

OWASP RBAC project has already implemented this, has a wide audience and has released several minor and two major versions. Many new features and modifications are expected by the community behind this.

#### Expected Results: OWASP RBAC project more mature by porting from PHP to other programming languages, OR adding new features and testing on the PHP version.

#### Knowledge Prerequisite: 
Good SQL knowledge, library development skills, familiarity with one of the programming languages as well as PHP. We recommend average experience and high skills.

#### Mentor:
Abbas Naderi, Rahul Chaudhary, Jesse Burns

#### Skill Level:
Advanced

For more info, visit [phprbac.net](http://phprbac.net)

## OWASP PHP Widgets

### OWASP PHP Widgets

#### Description:
Pull MVC (widget-based web views) has been available for many years on all major web programming languages, and even for Javascript. PHP on the other hand, lacks these and suffers a lot from forcing push MVC on its developers. There are a few libraries around, not secure and not mature at all. Providing a robust set of widgets for PHP developers not only smoothes web development process, it automatically mitigates a lot of web attacks that are based on user inputs to forms and other web elements (e.g CSRF, SQL Injection, XSS).

#### Expected Results: 
OWASP PHP Widgets is currently in beta, and the candidate will spend time testing the functionalities, providing test coverage, adding new widgets and features, and building a user community.

#### Knowledge Prerequisite: 
Average PHP programming. Good experience with web applications.

#### Mentor:
Abbas Naderi

## OWASP Seraphimdroid

#### Description:
SeraphimDroid is educational application for android devices that helps users learn about risks and threats coming from other android applications. SeraphimDroid scans your devices and teaches you about risks and threats coming from application permissions. Also this project will deliver paper on android permissions, their regular use, risks and malicious use. In second version SeraphimDroid will evolve to application firewall for android devices not allowing malicious SMS or MMS to be sent, USSD codes to be executed or calls to be called without user permission and knowledge.

#### Expected Results:
After last year's GSoC first version of project was released on Google play. However, educational component, setting check, potential android widgets are still missing and would be beneficial. Also, malicious behavior prevention mechanisms should be added and some bugs should be fixed.

#### Knowledge Prerequisite: 
Average Android and JAVA programming. Knowledge of XML and SQLite Good experience with mobile applications.

#### Mentor:
Nikola Milosevic

## OWASP OWTF

### OWASP OWTF - VMS - OWTF Vulnerability Management System

#### Brief Explanation:

Background problem to solve:

We are trying to reduce the human work burden where there will be hundreds of issues listing apache out of date or php out of date. 

Proposed solution:

We can meta aggregate these duplicate issues into one issue of "outdated software / apache / php detected". with XYZ list of issues in them.

A separate set of scripts that allows for grouping and management of vulnerabilities (i.e. think huge assessments), to be usable *both* from inside + outside of OWTF in a separate sub-repo here: https://github.com/owtf 

VMS will have the following features:
* Vulnerability correlation engine which will allow for quick identification of unique vulnerability and deduplication.
* Vulnerability table optimization : combining redundant vulnerabilities like example : PHP <5.1 , PHP < 5.2 , PHP < 5.3 all suggest upgrade php so if multiple issues are reported they should be combined.
* Integration with existing bug tracking system like example bugzilla, jira : Should not be too hard as all such system have one or the other method exposed (REST API or similar)
* Fix Validation : Since we integrate with bug tracking once dev fixed the bug and code deployed we can run specific checks via * OWTF or other tool (may be specific nessus or nexpose plugin or similar.)
* Management Dashboard : Could be exposed to Pentester, Higher Management where stats are shown with lesser details but more of high level overview.

[Similar previous work for Nessus](http://www.slideshare.net/null0x00/nessus-and-reporting-karma)

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability -i.e. the Health Monitor cannot crash! :)-
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - HTTP Request Translator Improvements

#### Brief Explanation:

Problem to solve:

There are many situations in web app pentests where just no tool will do the job and you need to script something, or mess around with the command line (classic example: sequence of steps where each step requires input from the previous step). In these situations, translating an HTTP request or a sequence of HTTP requests, takes valuable time which the pentester might just not really have.

Proposed solution:

An HTTP request translator, a *standalone* *tool* that can:

1) Be used from inside OR outside of OWTF.

2) Translate raw HTTP requests into curl commands or bash/python/php/ruby/PowerShell scripts

3) Provide essential quick and dirty transforms: base64 (encode/decode), urlencode (encode/decode)
* Transforms with boundary strings? (TBD)
* Individually or in bulk? (TBD)

Essential Function: "--output" argument

CRITICAL: The command/script should be generated so that the request is sent as literally as possible.

Example: NO client specific headers are sent. IF the original request had "User-Agent: X", the generated command/script should have EXACTLY that (i.e. NOT a curl user agent, etc.). Obviously, the same applies to ALL other headers.

NOTE: Ideally the following should be implemented using an extensible plugin architecture (i.e. NEW plugins are EASY to add)
* http request in => curl command out
* http request in => bash script out
* http request in => python script out
* http request in => php script out
* http request in => ruby script out
* http request in => PowerShell script out

Basic additional arguments:

- "--proxy" argument: generates the command/script with the relevant proxy option

		NOTE: With this the command/script may send requests through a MiTM proxy (i.e. OWTF, ZAP, Burp, etc.)

- "--string-search" argument: generates the command/script so that it:

		1) performs the request

		2) then searches for something in the response (i.e. literal match)

- "--regex-search" argument: generates the command/script so that it:
		1) performs the request

		2) then searches for something in the response (i.e. regex match)

OWTF integration

The idea here, is to invoke this tool from:

1) Single HTTP transactions:

For example, have a button to "export http request" + then show options equivalent to the flags

2) Multiple HTTP transactions:

Same as with Single transactions, but letting the user "select a number of transactions" first (maybe a checkbox?).

		
Desired input formats:

* Read raw HTTP request from stdin -Suggested default behaviour! :)-

	Example: cat path/to/http_request.txt | http-request-translator.py --output

* Interactive mode: read raw HTTP request from keyboard + "hit enter when ready"

	Suggestion: This could be a "-i" (for "interactive") flag and/or the fallback option when "stdin is empty"

	Example:

	1) User runs tool with desired flags (i.e. "--output ruby --proxy 127.0.0.1:1234 ...", etc.)

	2) Tool prints: "Please paste a raw HTTP request and hit enter when ready"

	3) User pastes a raw HTTP requests + hits enter

	4) Tool outputs whatever is relevant for the flags + http request given

* For bulk processing: Maybe a directory of raw http request files?

Nice to have: Transforms

In the context of translating raw HTTP requests into commands/scripts, what we want here is to provide some handy "macros" so that the relevant command/script is generated accordingly.

Example:

NOTE: Assume something like the following arguments: "--transform-boundary=@@@@@@@ --transform-language=php"

Step 1) The user provides a raw HTTP request like this:

  GET /path/to/urlencode@@@@@@@abc d@@@@@@@/test
  Host: target.com
  ...

Step 2) The tool generates a bash script like the following:

  #!/bin/bash
  
  PARAM1=$(echo 'abc d' | php -r "echo urlencode(fgets(STDIN));")
  curl ...... "http://target.com/path/to/$PARAM1/test"

OR a "curl command" like the following:
  PARAM1=$(echo 'abc d' | php -r "echo urlencode(fgets(STDIN));"); curl ...... "http://target.com/path/to/$PARAM1/test"

This feature can be valuable to shave a bit more time in script writing.

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability -i.e. the Health Monitor cannot crash! :)-
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - JavaScript Library Sniper Improvements

#### Brief Explanation:
This is a project that tries to resolve a very common problem during penetration tests:

The customer is running a number of outdated JavaScript Libraries, but there is just not enough time to determine if something useful -i.e. something *really* bad! :)- can be done with that or not.

To solve this problem, we propose a *standalone* *tool* that can:

1) Be run BOTH from inside AND outside of OWTF

2) Build and *update* a fingerprint JavaScript library database of:
* Library File hashes => JavaScript Library version
* Library File lengths => JavaScript Library version
* (Nice to have:) As above, but for each individual github commit (possible drawback: too big?)

3) Build and *update* a vulnerability database of:
* JavaScript Library version => CVE - CVSS score - Vulnerability info

4) Given a [ JavaScript file OR hash OR length ], found in the database, provides:
* JavaScript Library version
* List of vulnerabilities sorted in descending CVSS score order

5) (very cool to have) Given a list of JavaScript files (maybe a directory), provides:
* ALL Library/vulnerability matches described on 4)
	
Once the standalone tool is built and verified to be working, OWTF should be able to:

Feature 1) GREP plugin improvement (Web Application Fingerprint):

Step 1) Lookup file lengths and hashes in the "JavaScript library database"

Step 2) If a match is found: provide the list of known vulnerabilities against "JavaScript library X" to the user

Feature 2) SEMI-PASSIVE plugin improvement (Web Application Fingerprint):

1) Requests all referenced BUT missing JavaScript files -i.e. scanners won't load JavaScript files! :)-

2) re-runs the GREP plugin on the new files (i.e. to avoid missing vulns due to unrequested JavaScript files)

Potential projects worth having a look for potential overlap/inspiration:
* [https://owasp.org/index.php/OWASP_Dependency_Check OWASP Dependency Check?]

How many JavaScript libraries should be included?
* As many as possible, but especially the major ones: jQuery, knockout, etc.
* "Nirvana" Nice to have: ALL Individual versions of ALL JavaScript files from ALL opensource projects, (ideally) even if the project is not a JavaScript library -i.e. JavaScript files from Joomla, Wordpress, etc.-

Common JavaScript library fingerprinting techniques include:
* Parse the JavaScript file and grab the version from there
* Determine the JavaScript version based on a hash of the file
* Determine the JavaScript version based on the length of the file

Other Challenges:
* "the file" could be "the minimised file", "the expanded file" or even "a specific JavaScript file from Library X"
* When the JavaScript file does not match a specific version:
	1) The commit that matches the closest should (ideally) be found
	2) The NEXT library version after that commit (if present) should be found
	3) From there, it is about reusing the knowledge to figure out public vulnerabilities, CVSS scores, etc. again

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability -i.e. the Health Monitor cannot crash! :)-
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

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

CRITICAL: It is important to implement a plugin-based uploader system, so that other projects can benefit from this work (i.e. to be able to import third-party tool data to ZAP, Burp, and other tools in a similar fashion), and hence hopefully join us in maintaining this project moving forward.

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability -i.e. the Health Monitor cannot crash! :)-
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - Health Monitor

#### Brief Explanation:

In some cases, especially on large assessments (think: > 30 URLs) a number of things often go wrong and OWTF needs to recover from everything, which is difficult.

For this reason, OWTF needs an independent module, which is completely detached from OWTF (a different process), to ensure the health of the assessment is in check at all times, this includes the following:

Feature 1) Alerting mechanisms

When any of the monitor alerts (see below) is triggered. The OWTF user will be notified immediately through ALL of the following means:
* Playing an mp3 song (both local and possibly remote locations)
* Scan status overview on the CLI
* Scan status overview on the GUI

NOTE: A configuration file from where the user can enable/disable/configure all these mechanisms is desired.

Feature 2) Corrective mechanisms

Corrective mechanisms are also expected in this project, these will be accomplished sending OWTF api messages such as:
* Stop this tool
* Freeze this process (to continue later)
* Freeze the whole scan (to continue later)

Additional mechanisms:
* Show a ranking of files that take the most space

Feature 3) Target monitor

Brief overview:

All target URLs are checked for availability periodically (i.e. once x 5 minutes?), if a URL in scope goes down the pentester is alerted (see above).

Potential approach: Check if length of 1st page changes every 60 seconds.

NOTE: It might be needed to change this on the fly.

More background

Consider the following scenario:

Current Situation aka "problem to solve":

1) Website X goes down during a scan

2) the customer notices

3) the customer tells the boss

4) the boss tells the pentester

5) the pentester stops the tool which was *still* trying to scan THAT target (!!!!)

Desired situation aka "solution":

It would be much more professional AND efficient that:

1) The pentester notices

2) The pentester tells the boss

3) The boss tells the customer

4) OWTF stops the tool because it knows that website is DEAD anyway

A target monitor could easily do this with heartbeat requests + playing mp3s

The target monitor will use the api to tell OWTF "this target is dead: freeze(stop?) current tests, skip target in future tests"

Feature 4) Disk space monitor

Another problem that is relatively common in large assessments, is that all disk space is used and the scanning box becomes unresponsive or crashes. When this happens it is too late, the pentester may also see this coming but wonder “which are the biggest files in the filesystem that I can delete”, it is not ideal to have to look for these files in a moment when the scanning box is about to crash :).

Proposed solution:

Regularly monitor how much disk space is left, especially on the partition where OWTF is writing the review (but also tool directories such as /home/username/.w3af/tmp, etc.). Keep track of files created by OWTF and all called tools and sort them by size in descending order. Then when the disk space is going low (i.e. predefined threshold), an mp3 or similar is played and this list is displayed to the user, so that they know what to delete to survive :).

Feature 5) Network/Internet Connectivity monitor

Sometimes it may also happen that ISP, etc. connectivity go down in the middle of a scan, this is often a very unfortunate situation since most tools are scanning in parallel and they won’t be able to produce a report OR even resume (i.e. A LOT is lost). The goal here is that OWTF does all of the following automatically:

1) Detects the lack of connectivity

2) Freezes all the tools (read: processes) in progress

3) Resumes the scan when the connectivity is back.

Feature 6) Tool crash detection

Sometimes, certain tools (most notably, ahem, w3af), when they crash they do NOT exit. This leaves OWTF in a difficult position where 1+ process is waiting for nothing, forever (i.e. because “Tool X” will never finish)

Feature 7) Tool (Plugin?) CPU/RAM/Bandwidth abuse detection and correction

OWTF needs to notice when some tools crash and/or “go beserk” with RAM/CPU/Bandwidth consumption, this is different from the existing built-in checks in OWTF like “do not launch a new tool if there is less than XYZ RAM free” and more like “if tool X is using > XYZ of the available RAM/CPU/Bandwidth” and this is (potentially) negatively affecting other tools/tests, then throttle it.

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability -i.e. the Health Monitor cannot crash! :)-
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - Installation Improvements and Package manager

#### Brief Explanation:

This project is to implement what was suggested in the following [github issue](https://github.com/owtf/owtf/issues/192)

Recently i tried to make a fresh installation of OWTF. The installation process takes too much time. Is there any way to make the installation faster?
Having a private server with:
* pre-installed files for VMs
* pre-configured and patched tools
* Merged Lists
* Pre-configured certificates
Additionally a minimal installation which will install the core of OWTF with the option of update can increase the installation speed. The update procedure will start fetching the latest file versions from the server and copy them to the right path.
Additional ideas are welcome.

-- They could be hosted on Dropbox or a private VPS :)

2 Installation Modes
* For high speed connections (Downloading the files uncompressed)
* For low speed connections (Downloading the files compressed)
and the installation crashed because i runned out of space in the vm
IMPORTANT NOTE: OWTF should check the available disk space BEFORE installation starts + warn the user if problems are likely

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* Excellent reliability (i.e. proper exception handling, etc.)
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - Testing Framework Improvements

#### Brief Explanation:

As OWASP OWTF grows it makes sense to build custom unit tests to automatically re-test that functionality has not been broken. In this project we would like to improve the existing unit testing framework so that creating OWASP OWTF unit tests is as simple as possible and all missing tests for new functionality are created. The goal of this project is to update the existing Unit Test Framework to create all missing tests as well as improve the existing ones to verify OWASP OWTF functionality in an automated fashion.

Top features

In this improvement phase, the Testing Framework should:
* (Top Prio) Focus more on functional tests
For example: Improve coverage of OWASP Testing Guide, PTES, etc. (lots of room for improvement there!)
* (Top Prio) Put together a great wiki documentation section for contributors
The goal here is to help contributors write tests for the functionality that they implement. This should be as easy as possible.
* (Top Prio) Fix the current Travis issues :)
* (Nice to have) Bring the unit tests up to speed with the codebase
This will be challenging but very worth trying after top priorities.
The wiki should be heavily updated so that contributors create their own unit tests easily moving forward.

General background

The Unit Test Framework should be able to:
* Define test categories: For example, "all plugins", "web plugins", "aux plugins", "test framework core", etc. (please see [this presentation](http://www.slideshare.net/abrahamaranguren/introducing-owasp-owtf-workshop-brucon-2012) for more background)
* Allow to regression test isolated plugins (i.e. "only test _this_ plugin")
* Allow to regression test by test categories (i.e. "test only web plugins")
* Allow to regression test everything (i.e. plugins + framework core: "test all")
* Produce meaningful statistics and easy to navigate logs to identify which tests failed and ideally also hints on how to potentially fix the problem where possible
* Allow for easy creation of _new_ unit tests specific to OWASP OWTF
* Allow for easy modification and maintenance of _existing_ unit tests specific to OWASP OWTF
* Perform well so that we can run as many tests as possible in a given period of time
* Potentially leverage the [python unittest library](http://docs.python.org/2/library/unittest.html)

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* Performant and automated regression testing
* Unit tests for a wide coverage of OWASP OWTF, ideally leveraging the Unit Test Framework where possible
* Good documentation

#### Knowledge Prerequisite:

Python, experience with unit tests and automated regression testing would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

### OWASP OWTF - Tool utilities module

WARNING: This idea is taken from the 1st round of OWCS selections (Sept. 15th), please do NOT apply

#### Brief Explanation:

The spirit of this feature is something that may or may not be used from OWTF: These are utilities that may be chained together by OWTF OR a penetration tester using the command line. The idea is to automate mundane tasks that take time but may provide a lever to a penetration tester short on time.

Feature 1) Vulnerable software version database:

Implement a searchable vulnerable software version database so that a penetration tester enters a version and gets vulnerabilities sorted by criticality with MAX Impact vulnerabilities at the top (possibly: CVSS score in DESC order).

Example:
[Vulnerabilities against specific software version](http://www.cvedetails.com/vulnerability-list.php?vendor_id=74&product_id=128&version_id=149817&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=3&trc=17&sha=0d26af6f3ba8ea20af18d089df40c252ea09b711]

Feature 2) Nmap output file merger:

Unify nmap files *without* losing data: XML, text and greppable formats
For example: Sometimes 2 scans pass through the same port, one returns the server version, the other does not, we obviously do not want to lose banner information :).

Feature 3) Nmap output file vulnerability mapper

From an nmap output file, get the unique software version banners, and provide a list of (maybe in tabs?):

1) CVEs in reverse order of CVSS score, with links.

2) Metasploit modules available for each CVE / issue

NOTE: Can supply an *old* shell script for reference

3) Servers/ports affected (i.e. all server / port combinations using that software version)

Feature 4) URL target list creator:

Turn all “speaks http” ports (from any nmap format) into a list of URL targets for OWTF

Feature 5) Hydra command creator:

nmap file in => Hydra command list out

grep http auth / login pages in output files to identify login interfaces => Hydra command list out

Feature 6) WP-scan command creator:

look at all URLs (i.e. nmap file), check if they might be running word press, generate a list of suggested wp-scan commands for all targets that might be running word press

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* IMPORTANT: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/ ) in all modified code and surrounding areas.
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* Excellent reliability (i.e. proper exception handling, etc.)
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python, experience with unit tests and automated regression testing would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Abraham Aranguren - OWASP OWTF Project Leader - Contact: Abraham.Aranguren@owasp.org

## OWASP ZAP

We are in the process of deciding the set of ZAP projects for Google Summer of Code 2015.

You can follow (and join in) the discussions on the (ZAP Developer Group)[https://groups.google.com/d/msg/zaproxy-develop/Uy0JPkzsI_s/Bj7OTSkISCIJ]

### Advanced Plug-able Report Module

Currently ZAP provides only a limited set of report data. While this can be extended dynamically this feature is not currently used, and there is no way for users to choose what data they get back. It also provides a set of API calls, some of which return data that could be incorporated into reports, and some of which allow the fixed report to be accessed.

### = Expected Results =

* Report data will be a distinct type of data returned via API calls
* An add-on that provides report data - so this becomes 'plug-able'
* Report data and meta data should be fully internationalized
* Users can specify which sites / contexts report data should apply to

### = Knowledge Prerequisite: =
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

### = Mentors =
Johanna Curiel [johanna.curiel [at] owasp.org and Simon Bennetts

### Scanner Rule Implementation

The ZAP Active and Passive rules implement the functionality which allows ZAP to detect vulnerabilities. This project is aimed at significantly extending the existing set of rules and optionally rewriting existing rules in one or more of the supported scripting languages for extra flexibility.

### = Expected Results =

* New active and passive rules written in java and/or a supported scripting language
* Existing rules written in a supported scripting language
* ZAP to score significantly better against tools that evaluate scanners such as wavsep and Google Firing Range

### = Knowledge Prerequisite: =
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

### = Mentors =
Simon Bennetts and other members of the ZAP Core Team.

### Scripting Code Completion

ZAP provides a very powerful scripting interface. Unfortunately to use it effectively is only really possible with a good knowledge of the ZAP internals. Adding code completion (eg using a project (like)[https://github.com/bobbylight/AutoComplete] would significantly help users.

### = Expected Results =

* Code completion for all of the parameters for all available functions in the standard scripts
* Implementations for JavaScript, JRuby and Jython
* Helper classes with code completion for commonly required functionality

### = Knowledge Prerequisite: =
ZAP is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

### = Mentors =
Simon Bennetts and other members of the ZAP Core Team.

## OWASP Testing Guide

### OTG Web Testing Tool Integration
#### Brief Explanation:

We would like the OWASP Testing Guide to be much more easily consumable by web testing tools (such as ZAP). This would require adjustments to the Testing Guide, or separate Testing with X Guides, to explain how testing is completed with given tools. The tools would of course need to be changed to make full use of OTG  and this project could include such changes to OWASP tools like ZAP. 

Expected outputs:

Amended OTG or Testing with X Guides. Either option would require the document to integrate with all web testing tools (Using ZAP as the baseline).
Optional ZAP changes or add-on to make better use of the OTGs

Knowledge required:

Writing skills

OTG Web Testing Tool Integration mentor:'

Andrew Muller - OTG Project Co-Leader - Contact: Andrew.muller@owasp.org

## OWASP AppSensor

OWASP AppSensor Project provides real-time application layer intrusion detection. The software has recently hit v2.0. We have some ambitious plans across a variety of areas for the next year to build on the recent momentum.

 * Check the AppSensor wiki page linked above
 * Contact us through the mailing list.
 * Check our [github repository](https://github.com/jtmelton/appsensor) and the [open tickets](https://github.com/jtmelton/appsensor/issues)
 * Also see our [appsensor website](http://www.appsensor.org)

### Enterprise Integrations - Reporting

#### Brief Explanation:

This is a feature request that's been driven by the community. AppSensor provides great utility by allowing applications to defend themselves. AppSensor can/will also provide a UI (another possible GSOC project) to view and manage the information produced by the applications. However, larger organizations often already have a system in place for managing system security alerts. It would provide a lot of value if we can integrate with those systems and data formats. This project will involve a bit of up-front research, then primarily systems integration work. 

#### Expected Results:

We want  to support a number of integrations. Some that have been requested by our community are:  
* SNMP
* JMX
* SCOM
* syslog
* CEF
* AppDynamics

Source code and associated tests for these integrations will be created, along with the associated end user documentation for how to setup and configure them. 

#### Knowledge Prerequisites:

Comfortable in Java and unit testing. 

#### Mentors:
John Melton - OWASP AppSensor Project Leader (Development)

### Enterprise Integrations - Transport

#### Brief Explanation:

AppSensor currently supports a number of "execution modes", which are simply a reference to the transport protocol (REST, SOAP, thrift). There are a number of protocols that are popular in enterprises that we don't currently support, but could. This would simplify integration for many organizations who already use a set of approved communication protocols. This project would be primarily integration work and testing with a number of well-known systems integration / transport protocols and mechanisms. 

#### Expected Results:

We want  to support a number of integrations. Some that have been proposed are:  
* Kafka
* RabbitMQ
* ActiveMQ
* Avro
* Protobuf

Source code and associated tests for these integrations will be created, along with the associated end user documentation for how to setup and configure them. 

#### Knowledge Prerequisites:

Comfortable in Java and unit testing. Some familiarity with distributed systems in general and message brokers in particular would be helpful.

#### Mentors:
John Melton - OWASP AppSensor Project Leader (Development)

### Dashboard UI

#### Brief Explanation:

AppSensor provides a solid base of functionality to applications, but does not currently do a good job of presenting the resulting data. We are attacking that issue on 2 fronts. We plan to create a custom UI (this project) as well as various integrations to standard tools/formats for reporting to existing display systems. This project will involve creating the default/standard UI for the AppSensor project. As part of the project, you will learn about the domain model, iterating your mockup designs and share those with the project leader(s) and the community for feedback. We don't have an existing product, so you will have lots of responsibility for the design and implementation, as well as significant input to the decision around the technology stack.

#### Expected Results:

A modern, usable UI will be built that will have at least the following features (though there are many more features to build) : 
* Basic Dashboard UI (the UI for the OPS wall)
* Search
* Policy Management (edit server configuration)

Source code and associated tests for the UI will be created, along with the associated end user documentation for how to setup and configure the system. 

#### Knowledge Prerequisites:

Comfortable with UI design and development, particularly building dashboards. Comfortable with Java (with some assistance). Basic familiarity with security concepts related to intrusion detection and prevention as this is the basic domain.

#### Mentors:
John Melton - OWASP AppSensor Project Leader (Development)

### Trend Monitoring Analysis Engine

#### Brief Explanation:

AppSensor currently supports a basic policy-driven analysis engine to determine if a series of events represents an attack (if a user triggers 5 of this type of event in 10 minutes, it's an attack). While this supports many use cases, there are times when it would be helpful to know trending information. If a particular function of the application begins to see 10 times its normal amount of traffic, that might represent an attack. This project would add an additional analysis engine to support "trend monitoring". Development of this feature would require some initial research on alternative implementation strategies, followed by the development and testing of the feature in AppSensor. 

#### Expected Results:

The project should produce: 
* A trend monitoring analysis engine to be used either in place of or in addition to the existing policy-driven analysis engine
* Associated configuration mechanism to specify the trending rules/policy
* A small full sample demo application showing usage of the trend monitoring feature

Source code and associated tests for the feature will be created, along with the associated end user documentation for how to setup and configure it. 

#### Knowledge Prerequisites:

Comfortable in Java and unit testing.

#### Mentors:
John Melton - OWASP AppSensor Project Leader (Development)

## OWASP Passfault

### Passfault for Linux

#### Brief Explanation:

OWASP Passfault has the potential to be the best password policy available.  However, it's only available to java developers.  This effort will make Passfault available to every Linux administrator.  It would offer an alternative to the pam module libcrack to measure password complexity. 

#### Expected Results:

When complete an administrator should be able to do the following:
*  Enforce password complexity for all password changes with OWASP Passfault (for example when passwd is called)
*  Adjust password complexity threshold
*  (stretch goal) Install Passfault via package management: apt, yum, rpm, deb, etc.

#### Knowledge Prerequisites:
* Bash scripting
* Linux administration

#### Mentors:

* Cam Morris - OWASP Passfault Project Leader (Development)
* John Jolly - Linux Kernel Engineer for SUSE Linux on IBM System z Mainframes (Development)

### Passfault for Javascript via GWT

#### Brief Explanation:

OWASP Passfault has the potential to be the best password policy available.  However, it's only available to java developers.  This effort will make OWASP Passfault available as a javascript library.  The javascript library will be generated by GWT and made consumable by GWT Exporter.  The really cool result of this project will be that passwords can be analyzed client-side, and it will be easy for any web-page to use it.

#### Expected Results:
* GWT compiled Javascript derived from the OWASP Passfault core code
* javascript accessible APIs exported by GWT Exporter
* javascript bootstrap code to load wordlists
* scripted build with the excellent Gradle build tool
* (Stretch goal) Wrap everything up in a JQuery Plugin

#### Knowledge Prerequisites:
* Javascript
* Java
* (Nice to know) Gradle
* (Nice to know) JQuery
* (Nice to know) GWT

#### Mentors:
Cam Morris - OWASP Passfault Project Leader (Development)

## Web.config Security Analyzer v1.0 =>.NET Framework Config Security Analyzer v1.0

#### Brief Explanation:

[OWASP WCSA](https://code.google.com/p/wcsa/) is a very helpful tool to analyze proper security settings on ASP.NET applications. This [tool](http://www.troyhunt.com/2011/03/continuous-webconfig-security-analysis.html) once quoted by Troy Hunt, has important limitations such as rules support limited to single elements, a single condition, and just equals comparison. e.g. "Debug" attribute in "Compilation" Element should be "false". 

The tool requires a rules update (and potentially a UI refresh) to bring up many of the new security settings on .NET Framework 4.x to the tool including web service bindings and many others. Limitations described will not allow verification of web services bindings where you can have multiple elements named the same, one for each binding, and depending of a binding type the value (even if absent) is secure or not. 

Additionally, since conf files in .NET are pretty much universal to all framework application types and with the upgrade of IIS metabase to XML format for IIS 7.0 and 7.5, the tool could now be used for securing desktop applications and IIS 7.x servers. 

The proposal is then to empower the tool by creating XML based rules and using XQuery to overcome all the limitations of the current version and allowing support for new rules in a familiar language that would support multiple cases which can then be applied to all of the config files for .NET framework seamlessly.

#### Expected Results:
* Support for duplicated elements and multiple conditions
* Support for easily created custom rules via XQuery
* Updated rules for 4.0 and 4.5 frameworks
* Support for stand alone app.config files
* New Rules for IIS 7.x Web Server

#### Knowledge Prerequisites:
* C# programming
* Basic XQuery knowledge
* (Nice to know) Advanced Web.config knowledge
* (Nice to know) IIS 7.x configuration knowledge 

#### Mentors:
[[User:jcmax|Juan C Calderon]]  (Development)
