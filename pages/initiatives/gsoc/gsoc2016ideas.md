---
layout: full-width
title: GSoC 2016 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2016ideas
---
# GSoC 2016 Ideas

## OWASP Project Requests

Tips to get you started in no particular order:
- Read the [GSoC SAT](gsoc_sat).
- Contact us through the mailing list or irc channel.
- Check our [github organization](https://github.com/OWASP).

## OWASP Hackademic Challenges

[[OWASP Hackademic Challenges Project]]  helps you test your knowledge on web application security. You can use it to actually attack web applications in a realistic but also controllable and safe environment. After a wonderfull 2014 GSoC with 100 new challenges and a couple of new plugins we're mainly looking to get new features in and maybe a couple of challenges. Bellow is a list of proposed features.

### REST API for the sandbox

#### Brief Explanation:

During the last summer code sprint Hackademic got challenge sandboxing in the form of vagrant and docker wrappers as well as an engine to start and stop the container or vm instances.
What is needed now is a rest api which supports endpoint authentication and authorization which enables the sandbox engine to be completely independed from the rest of the project.

Ideas on the project:
Since the sandbox is written in python, you will be using Django to implement the api.
The endpoint authorization can be done via certificates or plain signature or username/password type authentication. We would like to see what's your idea on the matter.
However the communication between the two has to be over a secure channel.

#### Expected Results:
* A REST style api which allows an authenticated remote entity control the parts of the  sandbox engine it has access to.
* PEP8 compliant code
* Acceptable unit test coverage

#### Getting started:
Since this has been a popular project here's a suggestion on how to get started.
* Check the excellent work done by mebjas and a0xnirudh in their respective brances in the project's repository
* Take a brief look at the code and try to get a feeling of the functionality included. (Essentially it's CRUD operations on vms or containers)
* Read on what Docker and Vagrant are and take a look at their respective py-libraries
* If you think that contributing helps perhaps it would be a good idea to start with lettuce tests on the current CRUD operations of the existing functionality(which won't change and can eventually be ported to the final project) 

#### Knowledge Prerequisites:
Python, test driven development, some idea what REST is, some security knowledge would be preferable.

#### Mentors:
[Konstantinos Papapanagiotou](mailto:konstantinos.papapanaqiotou@owasp.org) [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org) - Hackademic Challenges Project Leaders

### New CMS

#### Brief Explanation:

The CMS part of the project is really old and has accumulated a significant amount of technical debt.
In addition many design decisions are either outdated or could be improved. 
Therefore it may be a good idea to leverage the power of modern web frameworks to create a new CMS.
The new cms can be written in python using Django.

#### Expected Results:
* New cms with same functionality as the old one (3 types of users -- student, teacher, admin--, 3 types of resources -- article challenge, class--, ACL type permissions, CRUD operations on every resource/user, all functionality can be extended by Plugins.
* REST endpoints in addition to classic ones
* tests covering all routes implemented, also complete ACL unit tests, it would be embarassing if a cms by OWASP has rights vulnerabilities.
* PEP 8 code

#### Note:
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

#### Mentors:
[Konstantinos Papapanagiotou](mailto:konstantinos.papapanaqiotou@owasp.org) [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org) - Hackademic Challenges Project Leaders

### First Course Type Challenge

#### Brief Explanation:
We have a wonderful sandbox engine which allows for complex guided challenges to be implemented.
We'd like to build a challenge that guides the user through a series of steps to an end goal and teaches more information on the subject matter on the way.
This is a very open-ended project on purpose to allow creative student to come up with nice ideas.
Bellow you will find some examples that we thought might be interesting.

Ideas on the project:
* Purposefully vulnerable web page that guides the user via javascript tooltips and hints to exploiting it using ZAP. ( Bonus: using ZAP via the ZAP api). The challenge is solved when the the student submits the contents of a text file located on the disk (obtained by exploited an RCE)

* Reversing a provided binary to extract information by providing step by step instructions to reversing using any popular reversing tool (well, you can't use IDA so gdb should have to do). Challenge is solved when the keys are extracted from the binary and submitted. Bonus points if each binary donwloaded has different keys.

* Guide to exploiting the TOP10. (Using ZAP?)

* Defensive Type challenges -- Here's how to create a patch for this kind of vulnerability -- Challenge is solved when the unit tests are run and the vulnerability isn't there.

#### Getting started
* Check popular javascript guide tools such as: (http://introjs.com/ and http://github.hubspot.com/shepherd/docs/welcome/ )
* If you're more interested in system or non-web challenges check serverspec and definitely check quest (https://github.com/puppetlabs/quest)
* If you think contributing is a good idea to make yourself familiar with the project you can either port one of the existing simpler 1-page challenges to a docker container and submit a pull request or write a guide on how to create such a challenge

#### Expected Results:

* One or more Course - style challenges provided either as a docker container or as a vagrant box.
* Concrete documentation on how to build a challenge like this.

#### Knowledge Prerequisites:
The technologies used.

#### Mentors:
[Konstantinos Papapanagiotou](mailto:konstantinos.papapanaqiotou@owasp.org) [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org) - Hackademic Challenges Project Leaders

### Advanced Sandboxed Challenges

#### Brief Explanation:

In the spirit of the challenges above, we're looking for true ctf type challenges.
This is an open ended task. We're expecting awesome fresh ideas.

Ideas on the project:
* An application vulnerable to one or more TOP 10 elements.
* A logic flaws based ctf
* Your idea here

#### Getting started:
* Check what Vagrant/Docker is
* Port one simple 1-page challenge (you can use one we already have ) to docker or vagrant

#### Expected Results:
Docker containers or Vagrant boxes that contain complete new challenges.

#### Knowledge Prerequisites:
Knowledge of the technologies used

#### Mentors:
[Konstantinos Papapanagiotou](mailto:konstantinos.papapanaqiotou@owasp.org) [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org) - Hackademic Challenges Project Leaders

### Your idea

#### Brief Explanation:

Amazing students, in our experience, the best, most creative and unique ideas show up when we let students suggest their own feature in relation to the project.
The above should give you a general idea where we're going but don't let them constrain you.
Do you wanna do something that would fit into Hackademic? Send us an email!

Ideas on the project:
No idea, that's your turn to shine!

#### Getting started
* Be awesome
* Have an idea
* Be a student
* Explain definite proof of the p vs np solution(jk, an algorithm that breaks RSA in polynomial time would be totally acceptable)

#### Expected Results:
If it's code, code according to our coding standards.
If it's challenges, something new and interesting.
If it's something else, then written like the person who's going to maintain your code is a raging psychopath with an axe who knows where you live.

In short we'd like some quality. ;-)

#### Knowledge Prerequisites:

#### Mentors:
[Konstantinos Papapanagiotou](mailto:konstantinos.papapanaqiotou@owasp.org) [Spyros Gasteratos](mailto:spyros.gasteratos@owasp.org) - Hackademic Challenges Project Leaders

## OWASP OWTF 

### OWASP OWTF - Web UI Improvements

#### Brief Explanation:

The current OWTF web interface is not very optimized and needs some work to reduce the number of clicks. The OWTF report uses accordion style components to render plugin outputs. This not very efficient in terms of number of clicks, horizontal and vertical scrolling.  React.js offers a simple way to build complex interfaces with the help of OWTF ReST APIs. Another part of the project will involve creating a maintainable CSS/JS system with latest frontend technologies like SASS, Compass, Gulp, and React.js (Flux).
As part of the project, you will learn about iterating your mockup designs and share those with the project leader(s) and the community for feedback. The existing stack is based on simple ReST APIs and vanilla Javascript. There are lots of features to be added, and you'll work with the project leader(s) and the community to build the most-needed and requested capabilities. 

For background on OWASP OWTF please see: [OWASP OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:
* IMPORTANT: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* IMPORTANT: [Sphinx-friendly python comments](http://sphinx-doc.org/) [example Sphinx-friendly python comments here](http://owtf.github.io/ptp/_modules/ptp/tools/w3af/parser.html#W3AFXMLParser)
* CRITICAL: Excellent reliability and performance.
*Good documentation

#### Knowledge Prerequisite:
Python, HTML5/CSS3/JS and React.JS experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentors:
Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com) OWASP OWTF Project Leaders

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

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

### OWASP OWTF - HTTP Request Translator Improvements

[Link to the repository](https://github.com/owtf/http-request-translator/tree/dev)

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
* Good performance
* Unit tests / Functional tests
* Good documentation

#### Knowledge Prerequisite:

Python and bash experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

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

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

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

Feature 8) PostgreSQL (DB) health monitor

The pentester can should be able to see the metrics of how much RAM/CPU the DB operations like INSERT are taking so as to maintain a healthy DB (as all data is saved in DB)

Feature 9) Component health like MiTM proxy metrics, cache I/O, Log files

Ability to see the proxy metrics, cache files I/O, and point-and-click log files streaming

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

Python, bash and Golang experience would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

#### OWASP OWTF Mentor:

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

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
* Define test categories: For example, "all plugins", "web plugins", "aux plugins", "test framework core", etc. (please see [http://www.slideshare.net/abrahamaranguren/introducing-owasp-owtf-workshop-brucon-2012 this presentation] for more background)
* Allow to regression test isolated plugins (i.e. "only test _this_ plugin")
* Allow to regression test by test categories (i.e. "test only web plugins")
* Allow to regression test everything (i.e. plugins + framework core: "test all")
* Produce meaningful statistics and easy to navigate logs to identify which tests failed and ideally also hints on how to potentially fix the problem where possible
* Allow for easy creation of _new_ unit tests specific to OWASP OWTF
* Allow for easy modification and maintenance of _existing_ unit tests specific to OWASP OWTF
* Perform well so that we can run as many tests as possible in a given period of time
* Potentially leverage the python unittest library: [http://docs.python.org/2/library/unittest.html http://docs.python.org/2/library/unittest.html]

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

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

### OWASP OWTF - Intercepting proxy

#### Brief Explanation:

The OWTF MiTM proxy can proxify most of the traffic (inbound+outbound) but it doesn’t have an intercepting capability ie. it cannot pause the framework + let the user modify the transaction on the fly.
Most of the GUI proxy tools like Paros, mitmproxy, Burp and OWASP ZAP have this functionality.

This project is about adding intercepting proxy capabilities to OWTF which can be used through the Web UI. Unlike Burp or ZAP, OWTF can be running multiple proxified tools while the user attempts to intercept an HTTP request, which makes interception significantly more difficult. For this reason, the user will be offered several interception options

1)Intercept all the requests: Useful when user manually browses the target without any tools running in background 

2) Selective Interception (default):  The user here can select a number of conditions, similar to the "Break" menu in ZAP for selective interception. For example:
 - The request "User Agent" header contains "xyz"
 - The request "Accept" header contains "abc"
 - The request is a GET/POST/DELETE request 

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

Python, bash and experience with HTTP internals would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn.

#### OWASP OWTF Mentor:

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

### OWASP OWTF - Tool utilities module

#### Brief Explanation:

The spirit of this feature is something that may or may not be used from OWTF: These are utilities that may be chained together by OWTF OR a penetration tester using the command line. The idea is to automate mundane tasks that take time but may provide a lever to a penetration tester short on time.

Feature 1) Vulnerable software version database:

Implement a searchable vulnerable software version database so that a penetration tester enters a version and gets vulnerabilities sorted by criticality with MAX Impact vulnerabilities at the top (possibly: CVSS score in DESC order).

Example:
[http://www.cvedetails.com/vulnerability-list.php?vendor_id=74&product_id=128&version_id=149817&page=1&hasexp=0&opdos=0&opec=0&opov=0&opcsrf=0&opgpriv=0&opsqli=0&opxss=0&opdirt=0&opmemc=0&ophttprs=0&opbyp=0&opfileinc=0&opginf=0&cvssscoremin=0&cvssscoremax=0&year=0&month=0&cweid=0&order=3&trc=17&sha=0d26af6f3ba8ea20af18d089df40c252ea09b711 Vulnerabilities against specific software version]

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

Contact: [Abraham Aranguren](mailto:Abraham.Aranguren@owasp.org) [Bharadwaj Machiraju](mailto:bharadwaj.machiraju@gmail.com} OWASP OWTF Project Leaders

 OWASP Mentors 

## OWASP ZAP

ZAP is one of the top OWASP projects and the most active open source web security tools. 

You can follow (and join in) the GSoC discussions on the ZAP Developer Group: https://groups.google.com/d/msg/zaproxy-develop/Uy0JPkzsI_s/Bj7OTSkISCIJ

### Bug tracker support

This would allow ZAP users to raise issues in bug trackers directly within ZAP. Ideally it would be implemented as an extension with a generic framework and then adaptors for specific trackers, like github and bugzilla.

The info included in the issues raised should be as configurable as possible so that users can include whatever they want, and set things like custom fields.

#### Expected Results

* Raise issues in github and bugzilla from alerts within the ZAP UI
* Support for raising alerts using the ZAP API
* High level of customization so that users can tune to their requirements

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
Contact: [Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

### Field enumeration

This would allow a user to iterate though a set of (user defined) characters in order to identify the ones that are filtered out and/or escaped.

The user should be able to define the character sets to test and will probably need to configure the success and failure conditions, as well as valid values for other fields in the form.

#### Expected Results

* User able to specify a specific field to enumerate via the ZAP UI
* A list of all valid characters to be returned from the sets of characters the user specifies
* Ability to configure a wide range of success and failure conditions to cope with as many possible situations as possible

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
[Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

### Form Handling

The ZAP traditional and Ajax spiders explore an application by putting basic default values in all forms. These may often not be valid values, for example using "ZAP" when an email address is required.

The enhancement would allow the user to define default values based on pattern matching against the field names and/or ids.

It would also be very useful if it could show the user all forms and their associated fields for an application, and then allow the user to update the default values.

#### Expected Results

* User able to specify default values for all forms used by the ZAP spiders
* Display all of the forms and fields for an application and allow the user to update the default values to be used
* Full support for defining default values via the API

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
[Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

### Automated authentication detection and configuration

ZAP has extensive support for supporting application authentication, but configuring this is a manual process which can be tricky to get right.

The enhancement would allow ZAP to detect as many forms of authentication as possible and automatically configure them using the existing ZAP functionality.

#### Expected Results

* Automatically detect a wide range of authentication mechanisms
* Automatically configure ZAP to handle them
* Full support via the API

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
[Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

### Advanced padding oracle testing and exploitation

ZAP has currently has very minimal support in it's the (beta) [https://github.com/zaproxy/zap-extensions/blob/beta/src/org/zaproxy/zap/extension/ascanrulesBeta/PaddingOraclePlugin.java PaddingOraclePlugin] for identifying potential [https://en.wikipedia.org/wiki/Padding_oracle_attack padding oracle] vulnerabilities. Specifically, it only examines two indicators for possible oracles (changing the last byte of padding by XORing it with 0x1 and resubmitting the HTTP request with the new altered parameter to see if the HTTP response contains some error patter or to check if the returned HTTP status is a 500 error. Furthermore, it is limited to checking parameters, but encrypted values that may be susceptible to padding oracle attacks may also be in HTTP cookies or even HTTP request / response values. (In the latter case, these custom headers are usually manipulated via AJAX.) Lastly SOAP messages using [https://www.w3.org/TR/2002/REC-xmlenc-core-20021210/Overview.html W3C XML Encryption] and JSON are other potential sources of padding oracle vulnerabilities that might be examined.

The enhancement would extend the support to more a broader attack surface such as new attack vectors like cookies, HTTP headers, and possibly XML or JSON and also expand the identification of potential new oracles to not just keywords, but to any minute difference in responses (at least for idempotent GETs) or significant variations in time. Lastly, we would like to add the ability to exploit padding oracle vulnerabilities discovered which could lead to whole lot of other interesting discoveries.

#### Expected Results

* Detect oracle padding vulnerabilities in more situations
  *Expanded attack vectors: cookies, HTTP headers, XML, JSON
  *Expanded variation of recognized potential oracles: ''any'' output differences when padding correct vs. incorrect (takes much more than flipping a single padding bit), significant differences in timing, etc.
* Add the option to actually attempt to exploit discovered potential padding oracle vulnerabilities and report additional subsequent findings once the ciphertext is actually decrypted.
* Build test code to illustrate a working proof of concept

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. Reading up on basic details of how padding oracle attacks operate would also be extremely helpful.

#### Mentors
[mailto:kevin.w.wall@gmail.com Kevin Wall] (cryptography subject matter expert) and other members of the ZAP core team

### Zest text representation and parser

Zest is a graphical scripting language from the Mozilla Security team, and is used as the ZAP macro language.

A standardized text representation and parser would be very useful and help its adoption.

#### Expected Results

* A documented definition of a text representation for Zest
* A parser that converts the text representation into a working Zest script
* An option in the Zest java implementation to output Zest scripts text format

#### Knowledge Prerequisite:
The Zest reference implementation is written in Java, so a good knowledge of this language is recommended. Some knowledge of application security would be useful, but not essential.

#### Mentors
[Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

### Your idea

We're always open to students coming up with their own suggestions for ZAP projects, so if you have something you think would make ZAP better then please get in touch!

#### Expected Results

* That depends on your project, but clearly defined goals will be necessary

#### Knowledge Prerequisite:
ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential.

#### Mentors
[Simon Bennetts](mailto:psiinon@gmail.com) and other members of the ZAP core team

## OWASP AppSensor

[[OWASP AppSensor Project]] provides real-time application layer intrusion detection. 

 * Check the AppSensor wiki page linked above
 * Contact us through the mailing list.
 * Check our [https://github.com/jtmelton/appsensor github repository] and the [https://github.com/jtmelton/appsensor/issues open tickets]
 * Also see our [http://www.appsensor.org appsensor website]

### Dashboard UI Expansion

#### Brief Explanation:

AppSensor provides a solid base of functionality to applications, and we currently have a minimal application for data display. This project will involve expanding the default/standard UI for the AppSensor project. As part of the project, you will learn about the domain model, iterating your mockup designs and share those with the project leader(s) and the community for feedback. The existing stack is based on spring boot and reactjs. There are lots of features to be added, and you'll work with the project leader(s) and the community to build the most-needed and requested capabilities.

#### Expected Results:

The existing dashboard application will be expanded and will involve features like: 
* Search (could involve significant back-end work to configure indexing, etc.)
* Policy Management (edit server configuration in real-time)
* Data visualization / dashboarding

Source code, tests, and associated documentation for both the back-end and UI will be delivered for this effort.

#### Knowledge Prerequisites:

Comfortable with UI design and development, particularly building dashboards. Comfortable with Java (with some assistance). Basic familiarity with security concepts related to intrusion detection and prevention as this is the domain.

#### Mentors:
[mailto:jtmelton@gmail.com John Melton] - OWASP AppSensor Project Leader (Development)

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
[John Melton](mailto:jtmelton@gmail.co) - OWASP AppSensor Project Leader (Development)

### Expand language support for clients

#### Brief Explanation:

AppSensor supports various modes for communication with the server. The language and framework of the client application are required only to support the given mode. This flexibility is desirable, but having pre-built clients in various languages is useful for our user-base. This project would involve working with various popular languages and frameworks to build support for communicating with the appsensor server backend.

#### Expected Results:

The project should produce: 
* Clients in multiple popular languages for interaction with appsensor server
* Evaluate the possibility for generating clients from specification as opposed to writing and maintaining the code (ie. swagger for REST)
* At a minimum, coverage for the HTTP/REST mode should be supported. Other modes (thrift, soap, kafka, etc.) will be produced as time allows. 
* Several small demo applications showing usage of the given APIs

Source code and tests for the feature will be created, along with the associated end user documentation for how to setup and configure it. 

#### Knowledge Prerequisites:

Comfortable working in multiple popular languages and unit testing.

#### Mentors:
[mailto:jtmelton@gmail.com John Melton] - OWASP AppSensor Project Leader (Development)

### Implement Detection Points in Reverse Proxy

#### Brief Explanation:

AppSensor works by tracking events that are created by "detection points", essentially locations in the processing pipeline where suspicious or malicious intent is observed. This often requires business-specific detection within the application. However, the project has defined a number of detection points (https://www.owasp.org/index.php/AppSensor_DetectionPoints) and responses (https://www.owasp.org/index.php/AppSensor_ResponseActions), some of which can be generically applied across a broader set of applications, including those that are common to an entire organization or even cross-organization. For that reason, a sub-project has been created (https://github.com/jtmelton/appsensor-reverse-proxy) that provides support for detection points and responses that are generic enough to be broadly applicable. This project would expand support for these detection points and responses.

#### Expected Results:

The project should produce: 
* New detection points and responses
  *Examples: 
***Look at how many cookies a session has. There is a maximum between browsers. We need to check between browsers I think the max is 255 or something. The point of checking for more cookies than that is to prevent cookie overflow.
***Look at how many characters a cookie contains.
***Some header related checks.
* Documentation for how to deploy the project and any end-user considerations
* Load testing each function as this project front-ends applications, and traffic throughput characteristics are important to our user-base.
* A small sample demo application showing the utility of the proxy. A recording of the usage for community viewing would be beneficial.

Source code and associated tests for the feature will be created, along with the associated end user documentation for how to setup and configure it. 

#### Knowledge Prerequisites:

Comfortable in golang and unit testing.

#### Mentors:
[John Melton](mailto:jtmelton@gmail.com) - OWASP AppSensor Project Leader (Development)

## OWASP Seraphimdroid [[OWASP_SeraphimDroid_Project| ]]

### Behavioral malware and intrusion analysis 

#### Brief Explanation:

OWASP Seraphimdroid is an Android mobile app which already has a capability to statically analyze malware using machine learning (weka toolkit) relying on permissions. However, this is usually not enough and we intend to improve this with behavioral analysis. There are a number of paper in scientific literature describing how to detect malware and intrusions by dynamically analyzing its behavior (system calls, battery consumption, etc.). The idea of this project is to find the best approach that can be implemented on the device and implement it.

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

#### Mentors:
* [Nikola_Milosevic](mailto:nikola.milosevic86@gmail.com) - OWASP Seraphimdroid Project Leader

### Framework for plugin development 

#### Brief Explanation:

OWASP Seraphimdroid is well rounded security and privacy app, however, it lacks some components community can provide. We would like to provide community the way to develop plugins that can add features to OWASP Seraphimdroid app. However, the way of integrating external components into Android app may be challenge. The way of presenting GUI and integration between processes need to be examined and developed. 

#### Expected Results:

* Examining the way of integrating third party apps through some provided API to OWASP Seraphimdroid
* Providing GUI integration with third party components
* Develop at least one test plugin
* Document the development process and API

#### Knowledge Prerequisites:
* Java
* Android
* CSV, XML

#### Mentors:
* [Nikola_Milosevic](mailto:nikola.milosevic86@gmail.com)  - OWASP Seraphimdroid Project Leader

### Educational component 

#### Brief Explanation:

OWASP Seraphimdroid is well rounded security and privacy app. The initial idea of the project was to provide educational platform for common users, where by using the application, users can learn about risks for their privacy and security. Some components already has some sort of explanation, which is educational. However, it lacks of uneatable knowledge source and some of the components that monitor user's behavior do not provide sufficient information. Idea of this project is to develop monitoring of user activity and an component that can warn user about risks if they do something risky. Also, mobile security knowledge base that can be updated remotely will be a huge new asset to the application.

#### Expected Results:

* Develop uneatable knowledge base and GUI for it
* Develop web server where the knowledge base can be updated
* Improve current educational reporting
* Develop methodology for monitoring users and notifying them about risky activities

#### Knowledge Prerequisites:
* Java
* Android
* CSV, XML

#### Mentors:
* [Nikola_Milosevic](mailto:nikola.milosevic86@gmail.com)  - OWASP Seraphimdroid Project Leader

## OWASP ZSC Tool

#### Brief Explanation:

[[OWASP_ZSC_Tool_Project|OWASP ZSC]] is an open source software in python language which lets you generate customized shellcodes and convert scripts to an obfuscated script. This software can be run on Windows/Linux/OSX under python.

#### Expected Results:

Please take a look of our TODO list in Github to get some ideas:
https://github.com/Ali-Razmjoo/OWASP-ZSC/issues

Another ideas:
* Help us develop shellcode module for windows
* Develop shellcode module for OSX

Read about the project here:
https://ali-razmjoo.gitbooks.io/owasp-zsc/content/

Recommended reading:
http://www.vividmachines.com/shellcode/shellcode.html

#### Knowledge Prerequisites:
* Python
* Basic knowledge about Shellcode and assembly language

#### Mentors:
[Christo Goosen](mailto:Christo.goosen@owasp.org) [Timo Goosen](mailto:Timo.Goosen@owasp.org) [Brian Beaudry](mailto:Brian.Beaudry@owasp.org )- OWASP ZSC Contributors

Contact us through our mailing list for questions:
https://groups.google.com/d/forum/owasp-zsc

## OWASP-SKF (Security Knowledge Framework)

#### Brief Explanation:
The OWASP Security Knowledge Framework is intended to be a tool that is used as a guide for building and verifying secure software. It can also be used to train developers about application security. Education is the first step in the Secure Software Development Lifecycle. This software can be run on Windows/Linux/OSX under python.

The 4 Core usage of SKF:

    Security Requirements OWASP ASVS for development and for third party vendor applications
    Security knowledge reference (Code examples/ Knowledge Base items)
    Security is part of design with the pre-development functionality in SKF
    Security post-development functionality in SKF for verification with the OWASP ASVS

#### Expected Results:

    More code examples for different languages
    Better quality of the knowledge base items
    More items in the pre-development phase
    Editable checklists in the post-development phase

We really would love to improve the quality of the knowledge base items further, also we would love to have more code examples in the different languages like: Perl, Hack, Go, Node.js and more.

Please take a look of our TODO list in Github to get some ideas:
https://github.com/blabla1337/skf-flask/issues

Another ideas:
* Help us with stuff you think is missing in the SKF project

Read about the project here:
https://skf.readme.io

Recommended reading (here you find a link to the Online Demo):
https://www.owasp.org/index.php/OWASP_Security_Knowledge_Framework

#### Knowledge Prerequisites:
* Python, PHP, Hack, .NET, GO, Ruby, Perl, Java, Node.js
* Basic knowledge about programming in one of the above languages

#### Mentors:
*[Glenn ten Cate](mailto:glenn.ten.cate@owasp.org) and Riccardo ten Cate- OWASP-SKF project leaders
*[Martin Knobloch](martin.knobloch@owasp.org) Chapter leader of OWASP NL

## OWASP SSL advanced forensic tool - O-Saft

O-Saft is an easy to use tool to tests the SSL connection according given list of ciphers and various SSL configurations and show informations about the SSL certificate.

It has some unique features, like
* working in closed environments without internet connection
* checking availability of ciphers independent of installed SSL library
* checking for all possible ciphers (up to 65535 per SSL protocol)
* mainly same results on all supported platforms

To fulfill that, it comes with a very simple installation (just unpack the files)
and does not rely on additional installed libraries or frameworks.

### Modul to evaluate and verify the certitificate chain

#### Brief Explanation:
Currently o-Saft relies on the installed openssl to verify the certitificate and its trust chain. This implementation misses some functionality and important checks. There are also checks, which cannot be done with openssl properly.

The idea is to improve the certificate checks in sevaral steps

1) implement all checks openssl can do for the provided server certificate
2) implement checks, which are not supported by openssl
3) implement all checks using native perl, without any library and without openssl
4) nice to have: implement checks which simulate common browsers as client

#### Expected Results:
* Perl code which finally can be integrated into O-Saft's Net::SSLinfo module
* Perl without using additional modules
* Good documentation
* The code should respect the policies described in the "Program Code" section, see [https://github.com/OWASP/O-Saft/blob/master/o-saft-man.pm]
* Not all steps need to be done, 1) is the most important.

#### Knowledge Prerequisites:
Experiance with perl (programming) and openssl (usage). Experiance with Regex. Understaning the concept of the PKI model for certificates used in SSL/TLS. For step 3) good knowledge of ASN.1 is necessary, support for parsing the basic ASN.1 types could be provided.

#### Mentors:
Achim Hoffmann (achim @ owasp . org), Torsten Gigler - O-Saft project leaders

### Postprocess to format output

#### Brief Explanation:
O-Saft uses the --legacy=KEY option to provide the results in various formats. This concept - O-Saft can produce legacy format - is a historic relict and should be replaced by an independent postprocess script.

#### Expected Results:
* Script or program (one or more) which produces the same result as O-Saft when called with a --legacy option. Example:
  o-saft.pl some.tld +cipher --legacy=sslscan
: should be replaced with:
  o-saft.pl some.tld +cipher | legacy-script sslscan
: The results of above calls must be identical.
* The postprocess must support at least Linux, Mac OS X and Windows.
* If other programming languages are used, please respect the minimal approach: no additional libraries.
* More ideas are welcome ...

#### Knowledge Prerequisites:
Basic perl knowledge to understand the existing code.

#### Mentors:
Achim Hoffmann - O-Saft Project Leader

### Modul for persistant data storage

#### Brief Explanation:
O-Saft does not have a permanent storage for the computed results itself. The user needs to save the results in a file. Even the results are well formated, comparing tests is always a shell hack. Also there is currently no way to read previous results and perform checks again.

#### Expected Results:
* Writing a module or external program with a simple API for storing and fetching results.
* Prefered storage format is sqlite, or flat ASCII file(s). See:
 o-saft-pl some.tld +info --legacy=key
: how a data record might look like (it's an example, not the final format).
* The API for fetching results must have a method to get a complete data record.
* The API uses key=value pairs, where the key is provided by O-Saft and not the module or program.
* If other programming languages are used, please respect the minimal approach.

#### Knowledge Prerequisites:
None specific, but getting used to O-Saft's current out put would be good ;-)

#### Mentors:
Achim Hoffmann - O-Saft Project Leader

### More sexy GUI

#### Brief Explanation:
O-Saft's GUI is very simple and not yet intuitive enough. For example the buttons in the Commands and in the Options TAB look not very nice. As there are dozens of commands and options, it is also hard to find the proper window (button) where to change them. Some kind of "search" function would be nice.

#### Expected Results:
* GUI with a better look and feel.
* Language is Tcl/Tk 8.5. If additional installed packages are used, the functionality must be availabe without these packages too (safe fallback).
* Complete integrated doumentation with "help" button and ballon-help on any object.
* Nice to have: search function for commands and options. This could be implemented with TK's text:search capabilities, but a solution which also works on CLI would be prefered.
* The code should respect the policies described in the "HACKER's INFO" section, see [https://github.com/OWASP/O-Saft/blob/master/o-saft.tcl]
* More ideas are welcome ...

#### Knowledge Prerequisites:
Experiance with programming in Tcl/Tk.

#### Mentors:
Achim Hoffmann - O-Saft Project Leader
