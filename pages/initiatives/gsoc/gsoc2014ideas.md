---
layout: full-width
title: GSoC 2014 Ideas
tags: gsoc
permalink: /initiatives/gsoc/gsoc2014ideas
---
# GSoC 2014 Ideas

## OWASP Hackademic Challenges

### OWASP Hackademic Challenges - New challenges and Improvements to the existing ones

#### Brief Explanation:

The challenges that have been implemented so far include: web application challenges covering several vulnerabilities included in the OWASP Top 10, cryptographic challenges, and entire virtual machines including several vulnerabilities.
New challenges need to be created in order to cover a broader set of vulnerabilities.
Also existing challenges can be modified to accept a broader set of valid answers, e.g. by using regular expressions.

Ideas on the project:

* Simulated simple buffer overflows
* SQL injections
* Man in the middle simulation
* Bypassing regular expression filtering
* Your idea here

#### Expected Results:

New cool challenges

#### Knowledge Prerequisites:

Comfortable in PHP, HTML and possibly Javascript. Good understanding of Application Security and related vulnerabilities. 

**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### OWASP Hackademic Challenges - Source Code testing environment

#### Brief Explanation:

Existing challenges are based on a dynamic application testing concept. We would like to work on a project that will give the capability to the attacker to review a vulnerable piece of source code, make corrections and see the result in a realistic (but yet safe) runtime environment. The code can either be run if needed or tested for correctness and security. The implementation challenges of such a project can be numerous, including creating a realistic but also secure environment, testing submitted solutions and grading them in an automatic manner. At the same time there are now numerous sites that support submitting code and then simulate or implement a compiler's functionality.

#### Expected Results:

A source code testing and improvement environment where a user will be able to review, improve and test the result of a piece of source code.

#### Knowledge Prerequisites:

Comfortable in PHP, HTML and possibly Java. Good understanding of Application Security, source code analysis and related vulnerabilities. 

**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

### OWASP Hackademic Challenges - Challenge Sandbox

Now, in order to create a challenge, one has to validate the solution with regular expressions (or just plaintext comparison) and report success or failure to the backend,
we'd like the ability to write a normal vulnerable web application as a challenge and leave it to hackademic to make sure that the server is not affected.
Since this is probably the most difficult task proposed, if you are considering it, please get in touch with us early on so we can discuss about it and plan it correctly.

Ideas on the project:

*Administrator's point of view*

Create an infrastructure that spawns virtual environments for users while keeping the load reasonable on the server(s).
Or configure apache,php,mysql in a way that allows for multiple instances of the programms to run in parallel completely seperated from the rest of the server.
The student is expected to provide configuration scripts that do the above

*Coder's Way*

This is better explained with an example:
In order to create an sql injection challenge one should be able to call a common unsecure mysql execute statement function.
The student can override common functions like this providing their own implementation of a very temporary database (based on flat files or nosql solutions e.t.c.).
The new functions should be able to detect the sqli and apply its results in a secure way(if the student drops a table no actual tables should be dropped but the table should not be visible to the student anymore).

* Your solution here *

The above solutions are by no way complete,their intention is to start you thinking.
This is a difficult task so if you consider takling it talk to us early on so we can reach a good solution which is possible in the GSoC timeframe.

#### Expected results

You should be able to run a big enough subset of OWASP WebGoat PHP with minimal modification as a Hackademic Challenge

### OWASP Hackademic Challenges - CMS improvements

#### Brief Explanation:

The new CMS was created during last year's GSOC. We have received feedback from users that suggest various improvements regarding functionality e.g. better user, teacher and challenges management. There are also some security improvements that are needed and in general any functionality that adds up to the educational nature of the project is more than welcome.

Ideas on this project:

* Template *

Since it's creation the project has received a good number of new features, but the visual/ux/ui part has never gotten much love.
It would be good if we had a new template with proper ui design.

* Questionaire creation plugin *

We'd like the admin to be able to create questionaires, assign rules for each question (e.g. correct answer +2pts incorrect answer -2, no answer 0)  and assign them to students as homework/exams.
The grading can either be done automatically (for multiple choice) or be submitted to the creator of the questionaire.

* Ability to show different articles on the user's home screen 

Now each user is served the latest article in their home screen. We need the ability for either the teacher/admin to be able to define what article each class is served.

* Gamification of the user's progress *

A series of plugins and a template which allow the user to earn badges as they solve challenges and a better visual representation of their progress.

* Ability to define series of challenges *

The teacher/admin should be able to define a series of challenges (e.g. 2,5,3,1) which are meant to be solved in that order and if one is not solved then the student can't try the next one.

* Tagging of articles, users, challenges *

A user should be able to put tags on articles and challenges if they are a student and on users, classes, articles and challenges if they are a teacher.
Also the user should be able to search according to the tags.

* Your idea here *

We welcome new ideas to make the project look awesome.

#### Expected Results:

New features  and security improvements on the CMS part of the project.

#### Knowledge Prerequisites:

Comfortable in PHP and HTML. Good understanding of Application Security and related vulnerabilities if you undertake security improvements. 

**Mentors:** Konstantinos Papapanagiotou, Spyros Gasteratos - Hackademic Challenges Project Leaders

## OWASP WebGoatPHP

### OWASP WebGoatPHP

#### Description:

Webgoat is a deliberately insecure open source software made by OWASP using Java programming language. It has a set of challenges and steps, each providing the user with one or more web application vulnerability which user tries to solve. There are also hints and auto-detection of correct solutions. 
Since Java is not the most common web application programming language, and it doesn't have many of the bugs other languages such as PHP have when it comes to security, OWASP has dedicated in 2012 an amount of $5000 for promotion of WebGoatPHP.

If you want to know more about WebGoatPHP, I suggest downloading and giving WebGoat a try. It is one of OWASP prides (about 200000 downloads).

#### Expected Results:

WebGoatPHP will be a deliberately insecure PHP web application which operates in different modes. A contest mode where challenges are selected by an admin and the system starts a contest. Admins can open up hints for participants and manage everything. A workshop mode, where the educator has control of the most of application features, as well as feedback of user activities and is ideal for learning environments, and a single mode where someone can browse challenges and solve them.

#### Knowledge prerequisite:

You just need to know PHP. You are supposed to define flawed systems, which is not the hardest thing. Familiarity with web application security and SQL is recommended.

**Mentor:** Abbas Naderi

## OWASP CSRF Guard

### OWASP CSRF Guard

#### Description: 

Cross-Site_Request_Forgery_(CSRF) is a complicated yet very effective web attack. The most important thing about CSRF is that it's hard to properly defend against it, specially when it comes to Web 2 and AJAX. We have had discussions on means of mitigating CSRF for years at OWASP, and are now ready to develop libraries for it. Many of the key ideas of this library can be found at [jcsrf](http://www.cs.sunysb.edu/~rpelizzi/jcsrf.pdf).

#### Expected Results:A transparent Apache 2 module properly mitigating all POST CSRF attacks, as well as a lightweight PHP library doing the same.

#### Knowledge prerequisites: Knowing CSRF and at least one way to defend against it, PHP, C/C++, Linux.

**Mentor:** Abbas Naderi, Rahul Chaudhary 

## OWASP PHP Security Project

### OWASP PHP Security Project

#### Description:

OWASP PHP Security project plans to gather around secure PHP libraries, and provide a full featured framework of libraries for secure web applications in PHP, both as separate de-coupled libraries and as a whole secure web application framework. Many aspects of this project are already handled, and are being added to OWASP.

#### Expected Results:

Result of this project is much more security among PHP applications. Most PHP applications are vulnerable and there's no central approach to secure them (due to open source nature). Many people look at OWASP for such information.

Last year, we got GSoC people working on OWASP PHPSEC, and we were the most active OWASP project. A lot of the libraries are in place, and this year, we will mostly work on the framework.

#### Knowledge prerequisite: 

Anyone with adequate PHP programming language experience (possibly web application development in PHP).  There are hard and easy parts of this project. For tougher parts, familiarity with security concepts, advanced SQL, and advanced PHP and web server configuration is required. 

**Mentor:** Abbas Naderi, Rahul Chaudhary, Johanna Curiel

## OWASP RBAC Project

### OWASP RBAC Project

#### Description:

For the last 6 years, improper access control has been the issue behind two of the Top Ten lists.

RBAC stands for Role Based Access Control and is the de-facto access control and authorization standard. It simplifies access control and its maintenance for small and enterprise systems alike. NIST RBAC standard has four levels, the second level hierarchical RBAC is intended for this project.

Unfortunately because of many performance and development problems, no suitable RBAC implementation was available until recently, so developers and admins mostly used ACLs and other forms of simple access control methods, which leads to broken and unmaintainable access control over the time. 

OWASP provides the RBAC project, as a stand-alone library with very fast access control checks and standard mature code-base. Currently PHPRBAC which is the PHP version of the RBAC project is released.

#### Expected Results:

Standard NIST level 2 hierarchical RBAC libraries for different programming languages, specially web-based ones such as C/C++/Java/ASP/ASPX/Python/Perl/etc.

#### Knowledge prerequisite:

Good SQL knowledge, library development schemes, familiarity with one of the programming languages.

**Mentor:** Abbas Naderi, Rahul Chaudhary 

**Skill Level:** Advanced

For more info, visit [phprbac.net](http://phprbac.net)

## OWASP OWTF

### OWASP OWTF - Flexible plugin mappings

#### Description:

Right now OWTF plugins are categorized based on [OWASP Testing Guide v3](https://www.owasp.org/index.php/OWASP_Testing_Guide_v3_Table_of_Contents) , the aim of this project would be to change the existing codebase to handle multiple standard mappings like [OWASP Testing Guide v3](https://www.owasp.org/index.php/OWASP_Testing_Guide_v3_Table_of_Contents), [OWASP Testing Guide v4](https://www.owasp.org/index.php/OWASP_Testing_Guide_v4_Table_of_Contents), [NIST 800-53 security controls](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf) (+nice to have: [PTES](http://www.pentest-standard.org/index.php/Main_Page), [OSSTMM](http://www.isecom.org/research/osstmm.html)) along with the facility to add more standards at a later stage.

[Largely from github:](https://github.com/7a/owtf/issues/113)

A huge thank you to Jim Kelly who provided a mapping of the NIST 800-53 security controls to the OWASP Testing Guide!

#### Background

OWTF is currently aligned to the OWASP Testing Guide v3, which is still OK since v4 is far from complete.
However, we need to make the mapping to standards a bit more flexible because:

1. OWASP is shuffling OWASP Testing Guide codes: This means we should move away from using OWASP codes in plugin names in the future.
2. There are other standards, like the NIST 800-53 security controls, that we should also try to map our plugins to.

[The final NIST 800-53 document, from April 2013, can be found here](http://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-53r4.pdf)

#### Project Overview:

The idea of this project is to map the existing plugins (we will worry about the OWASP Testing Guide v4 when that is complete) to the NIST 800-53 security controls.

To do this, (alt least) the following is involved:

1. Change the web_testgroups.cfg configuration file to have a NEW column with the relevant code of the associated NIST 800-53 security control (Jim provided a file with this mapping!)
2. Create a lookup config file for NIST 800-53 security control code <-> description pairs
3. Change the OWTF report so that UNDER the OWASP Testing Guide item, we also show the relevant NIST 800-53 security control (BOTH code + description, as we do with the OWASP Testing Guide). Aesthetics note on point 3): Maybe this could be shown with a smaller font so that it does not take a lot more space?
4. Nice touch: Add the NIST security controls to the advanced OWTF filter so that a user is able to filter by the security controls they are testing

For more information please see [the github issue](https://github.com/7a/owtf/issues/113)

#### Potential project coordination

This project should be coordinated with [OWASP OWTF - Free Passive Online scanner + Remediation Boilerplate Templates](https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Free_Passive_Online_scanner_.2B_Remediation_Boilerplate_Templates) if both projects are accepted.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python knowledge is very welcome but not strictly necessary if there is will to learn, previous exposure to security concepts and penetration testing is very important in this project but some lack of this can be compensated with pre-GSoC involvement and will to learn.

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Free Passive Online scanner + Remediation Boilerplate Templates

#### Description:

An unfortunate reality of penetration testing is the amount of time that is gone via reporting. Explaining vulnerabilities to non technical customers is difficult. Conveying the urgency of fixing XSS, CSRF and many other issues tends to be non-trivial. Especially when the overall security background from the customer is poor (which is common).

This project aims to:
* Provide boilerplate **vulnerability explanations** which can easily be copy-pasted into real-world reports
* Provide boilerplate **vulnerability fixing recommendations** which can easily be copy-pasted into real-world reports
For example: Linking to the [OWASP CheatSheets](https://www.owasp.org/index.php/Cheat_Sheets), providing platform-specific vulnerability fixing information (i.e. Apache vs. IIS vs. nginx), etc. is important here.
* Allow penetration testers to **easily** customise and work with alternative remediation templates
* (Obviously) map boilerplate templates to OWTF plugins so that OWTF can show/merge the templates together with the penetration tester notes :).
* Storing remediation template information in a database would be nice to provide additional flexibility to copy-paste into or even generate a msoft word doc, odt, etc.
* Implement **database import/export functionality** for the boilerplate templates
* Improve the OWTF interactive report to make this copy-pasting as simple as possible
* Improve the existing “magic bar” OWTF functionality (in the interactive report), which assembles all penetration tester notes in 1 easy to copy-paste page, so that it assembles the generated report like “vulnerability explanation + penetration tester notes + vulnerability fixing recommendations”.
* **IMPORTANT** community features:

Feature 1) Making templates available on github.io site

OWTF wants to help penetration testers use their time most effectively, **even if they don’t use OWTF directly**, for this reason, as part of this project, **we would like to setup a github.io website containing the boiler plate templates**. [Something like this](http://koto.github.io/blog-kotowicz-net-examples/cursorjacking/), but for OWTF and with the boilerplate templates there.

This achieves a number of positive effects in our opinion:

1. Any penetration tester can easily copy-paste anything from the templates into their report, just using a browser with an internet connection (i.e. even if not using OWTF).
2. The templates will be much more exposed to public scrutiny, which will hopefully improve their quality overtime.
3. Contributions to the templates will be easier, even for people without coding experience
4. If successful, this could be thought of a public wiki to explain vulnerabilities and remediation fixes to customers, which will help penetration testers to focus more on the testing aspects of their engagements. By testing more, penetration testers will be able to find more issues and provide more value for money to their customers, which can only help the greater good in the intertubes :).

Feature 2) Free passive online scanner on github.io site

OWTF allows many passive tests, such as those using third party websites like Google, Bing, etc. searches, as well as handy "Search for vulnerability" search boxes (i.e. Fingerprinting plugin). This feature involves the creation of a **script** that produces an interactive OWTF report with the intention of hosting it in the github.io site.

The idea here is to have a passive, JavaScript-only interactive report available on the github.io site, so that people can try OWTF **without installing anything**, simply visiting a URL.

This would be a normal OWTF interactive report where the user can:
* Enter a target
* Try passive plugins (only the parts that use no tools)
* Play with boilerplate templates from the OWTF interactive report
This would make all the third-party website tests from OWTF usable from any browser, without having to install anything, etc.

The thinking here is that this would make it even easier to use/try OWTF.

#### Script Ideas

**LEGAL CLARIFICATION (Just in case!)**:
The passive online scanner, simply makes OWTF passive testing "through third party websites" more accessible to anybody, however it is the user that must 1) click the link manually + 2) do something bad with that afterwards + 3) doing 1 + 2 WITHOUT permission :). Therefore this passive online scanner does not do anything illegal [More information about why this is not illegal here](http://www.slideshare.net/abrahamaranguren/legal-and-efficient-web-app-testing-without-permission) (recommended reading!)

The thought here is to have a script that does something like:
* Run "owtf.py -t passive http://demo.testfire.net"
* Modifies the output report to have a big "add target" at the beginning
* Adds necessary JavaScript to the report, so that demo.testfire.net can be changed to the value of Target field input
Essentially, anybody would be able to run (most of) the passive stuff in owtf without having anything installed, this applies mostly to third party website testing (i.e. Google/Bing/NIST/etc. searches), but also to leave the whole OWASP Testing Guide there so that people can use the reports from there too.

The placeholder becomes "demo.testfire.net" essentially, of course, things like theHarvester won't work for this, but Google/Bing/etc. searches will work.
This is somewhat like a JavaScript link generator for OWTF passive plugins, in a sense.

The script would need to "patch" the OWTF report so that the target of choice (i.e. demo.testfire.net) is replaced with a JavaScript function call, probably.
This might be slightly more complicated: Using JavaScript, the url has to be parsed and broken down into stuff like HOST_IP, HOST_PORT etc..
However, using JavaScript, we can loop through the DOM and change all links in the OWTF report, to produce the JavaScript-only, "cloud" version, to host on github.io.

This will make the OWASP Testing Guide, OWTF and the boilerplate templates much more accessible to anyone for trial, demonstration and/or learning purposes.

#### Project extent

Since OWTF aims to provides coverage of the [OWASP Testing guide](https://www.owasp.org/index.php/OWASP_Testing_Project) (via web plugins) and the [Penetration Testing Execution Standard](http://www.pentest-standard.org/index.php/Main_Page) (PTES) (via net and aux plugins) it is important to realise that a big component of this project is to **write QUALITY boilerplate templates for a VERY WIDE number of vulnerabilities** (i.e. all major vulnerabilities!).

#### Potential project coordination

This project should be coordinated with [OWASP OWTF - Flexible plugin mapping](https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Flexible_plugin_mappings) if both projects are accepted.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python knowledge is very welcome but not strictly necessary if there is will to learn, previous exposure to security concepts and penetration testing is very important in this project but some lack of this can be compensated with pre-GSoC involvement and will to learn.

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Automated Vulnerability Severity Rankings

#### Background

OWTF aims to provides coverage of the [OWASP Testing guide](tps://www.owasp.org/index.php/OWASP_Testing_Project)(via web plugins) and the [Penetration Testing Execution Standard](http://www.pentest-standard.org/index.php/Main_Page)(PTES) (via net and aux plugins).

While most tools focus on fully automated approaches such as “providing the user with a report that cannot be changed”, **a flawed approach plagued with false positives and false negatives**, OWTF tries to balance automation with the powerful out-of-the-box thinking that only a human can provide.

#### High Level Overview / Problem Introduction

At the moment in OWTF it is very useful that "the human can set the severity for each finding manually".
The reasoning here is that the human can take severity context into account, while tools cannot. For example, SQL Injection on a database that has no data, available mechanisms to send http requests/shell commands, etc., **cannot be ranked as “High” or “Critical”**, the risk in that context is near zero.

All the above being said, **automated severity rankings are critical for penetration testing efficiency**, this is particularly true when the size of the scope is significant: In a 30 websites assessment, **if OWTF provided an initial default severity ranking** (which right now, it does not, a serious limitation), the human should know which of the 30 websites appears to be the weakest and therefore be able to focus their analysis on that based on the partial results from the first 10-30 minutes.

The goal of this project, is therefore to provide the human with an initial automated severity ranking, that the human is able to override, but assists the human to focus analysis on seemingly weaker hosts/websites.

#### Technical Overview

IMPORTANT: An automated severity ranking is an initial “risk guess” based on parsing plugin output.

During analysis of this proposed project we identified some possible implementation approaches:

**Possible Approach 1) Change all OWTF plugins**

So that they produce:
* Their usual output (as currently)
* **An initial automated severity ranking (when possible)**

#### Potential Advantages:

A big advantage here is logic cohesion, the ranking logic is close to the scanning logic, which makes verification steps perhaps easier to perform (i.e. more context may be available)

#### Potential Drawbacks:

Parsing plugin output for ranking purposes during plugin execution might slow OWTF, which is a big concern in a project where efficiency is the top goal.

**Possible Approach 2) Have a background “severity ranker process”**

The idea here would be to have a process running in the background, plugins do not rank their own output, instead they send a message to the severity ranker process, when this happens, the process parses the output to produce an initial automated ranking.

#### Potential Advantages

Plugin ranking happens in the background without slowing OWTF, cool features such as “re-rank this plugin (may send verification tests against target)” become possible from the interactive report via Plug-n-Hack.

#### Potential Drawbacks

The ranking logic is de-coupled from the scanning logic (where perhaps more information is available or sending “another request to double-check” might be easier)

#### Expected Outcome and Reporting Implications

At the end of the automated plugin severity rankings OWTF should:
1. Provide a default, automated, plugin severity ranking for each plugin
2. Since default severity rankings are less reliable (automated) they will be highlighted as such in the report, for example, providing a confidence percentage or at least a clear visual clue that the ranking is automated such as black/gray background. 

If implementing a confidence percentage, OWTF would say "how sure" it is about a given automated ranking. For example "0%" would be "just guessing" and "100%" would be "exploitation verified".
3. When the human overrides or confirms the default ranking, the ranking is considered
"confirmed by a human" (i.e. more reliable) and this highlighting (i.e. black/gray background) is removed
4. A new filter to group vulnerabilities by target will be provided in the report.
5. A new filter to group vulnerabilities for all targets will be provided in the report

#### Potential project coordination

This project should be coordinated with [OWASP OWTF - Zest support and ZAP integration](https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Zest_support_and_ZAP_integration) if both projects are accepted.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python knowledge is very welcome but not strictly necessary if there is will to learn, previous exposure to security concepts and penetration testing is very important in this project but some lack of this can be compensated with pre-GSoC involvement and will to learn.

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Zest support and ZAP integration

#### Brief Explanation:

The Mozilla foundation has done great work with the Zest initiative, this provides a great automated mechanism to replicate exploitation of security vulnerabilities in a format that makes tool communication easier: For example, ZAP supports Zest, so if OWTF can create a Zest script for a vulnerability in an automated fashion, this may in turn be easier to import into ZAP and other tools.

[More information on Zest can be found here](https://developer.mozilla.org/en-US/docs/Zest)

#### High level overview

This project, introduces the risk of seriously damaging OWTF performance, therefore, at a high level, we believe there are the following choices:

Choice 1) **Background execution** - You try to see if a Zest script can be
created for each plugin in the *background* while owtf keeps running

Choice 2) **On-demand execution** - Using some Plug-n-Hack magic, we could
have a button in the report saying "Generate Zest Scripts for plugin"

Choice 3) **Hybrid approach** - Implement choice 1 + 2, default to choice 2, but have choice 1
as an option (for example: owtf.py --zest on-demand/background/all)

#### Other project practicality considerations

1. **Background Zest script generation**

Makes sense on at least the output of scanner plugins (i.e. w3af finds a vuln, we create the Zest script for that vuln)

2. **On-demand Zest script generation from plugin output**

From the report, when you select a plugin, *could* be useful

3. **On-demand Zest script generation from HTTP transaction**

Selecting an HTTP transaction from the transaction log + click "generate Zest script" from there would also be very useful

4. **ZAP integration**

After generating the Zest script, the next step is to send the Zest script to ZAP, possibly using [the ZAP API](http://code.google.com/p/zaproxy/wiki/ApiDetails), and perhaps with some help from [Plug-n-Hack](https://blog.mozilla.org/security/2013/08/22/plug-n-hack/) (which allows us to send commands to our proxy, and from there, we could send commands to ZAP, or alternatively perhaps send commands to ZAP directly via Plug-n-Hack).

The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Potential project coordination

This project should be coordinated with [OWASP OWTF - Automated Plugin Severity Rankings](https://www.owasp.org/index.php/GSoC2014_Ideas#OWASP_OWTF_-_Automated_Vulnerability_Severity_Rankings) if both projects are accepted.

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Some previous exposure to security concepts, penetration testing, Python and development in general is important for this project.

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Improved Proxification and Plug-n-Hack support

#### Brief Explanation:

The Mozilla foundation has done great work with [the Plug-n-Hack standard (PnH)](https://blog.mozilla.org/security/2013/08/22/plug-n-hack/), which allows security tools to provide better interaction with web browsers. For example, it allows us to send commands from the browser to the OWTF proxy, which opens the door to a much better user experience. Please note that **OWTF already supports Plug-n-Hack Phase 1**. 

#### Overview

This project is divided in the following pieces of functionality:

### Plug-n-Hack v2/v3 support

There are many other features in Phase 2 that could be implemented and on top of that Plug-n-Hack v3 should be available this summer.
The aim of this project would be to try to cover as much as possible from the Plug-n-Hack standard as relevant to OWTF, for example:

**OWTF Plug-n-Hack mode**

OWTF starts in proxy mode, waiting for instructions, the user can drive OWTF from the browser (i.e. using the browser as a GUI, instead of the command line).

**OWTF improved report interactivity via Plug-n-Hack**

Provide new functions from the OWTF interactive report, for example “launch this plugin again”, “send this HTTP request again”, etc.

[Please see this demo to see the newest Plug-n-Hack additions](https://www.youtube.com/watch?v=pYFtLA2yTR8)

[For more information about plug and hack please see this](https://blog.mozilla.org/security/2013/08/22/plug-n-hack/)

### Improved Tool and Plugin proxification

At the moment, not all Tools or plugins are proxified in OWTF. This means that not all plugins send their requests through the OWTF MiTM proxy. This is a problem because OWTF performs analysis on HTTP transactions passively, and right now it cannot see **all HTTP requests sent** due to some unproxified tools and plugins.

An additional component of this project is therefore to proxify most of the tools and plugins. This may be possible using a utility like proxychains and/or tweaking the inbound proxy without disturbing current functionality.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python, experience is very welcome but not strictly necessary, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Stateful Browser with configurable authentication

#### Brief Explanation:

The automated functionality of OWASP OWTF is currently limited to the non-authenticated portion of a website. We would like to implement authentication support through:

1. OWTF parameters
2. Configuration files

What we would like to do here is to leverage the [powerful mechanize python library](http://wwwsearch.sourceforge.net/mechanize/) and build at least support for the following authentication options:
* Basic authentication [Already implemented here](https://github.com/7a/owtf/issues/9)
* Cookie based authentication
* Form-based authentication
* Client-side certificates

#### Other important features

* GUI mechanism to make authentication setup (super-)easy for the user via [Plug-n-Hack](https://blog.mozilla.org/security/2013/08/22/plug-n-hack/)
* Ability to **keep track of several user roles** and allow easy switching via [Plug-n-Hack](https://developer.mozilla.org/en-US/docs/Plug-n-Hack)

Additionally, we would welcome here a feature to detect when the user has been logged off, to log OWTF back in again before retrying the next request. <-- The proxy is probably a better place to implement this since external tools would also benefit from this. This feature will have to be coordinated with the MiTM proxy feature (already implemented).

The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* High performance
* Reliability
* Ease of use
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python, experience with the mechanize library or HTTP state is very welcome but not strictly necessary, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Testing Framework Improvements

#### Brief Explanation:

As OWASP OWTF grows it makes sense to build custom unit tests to automatically re-test that functionality has not been broken. In this project we would like to improve the existing unit testing framework so that creating OWASP OWTF unit tests is as simple as possible and all missing tests for new functionality are created. The goal of this project is to update the existing Unit Test Framework to create all missing tests as well as improve the existing ones to verify OWASP OWTF functionality in an automated fashion.

#### Top features

In this improvement phase, the Testing Framework should:
* (Top Prio) Focus more on functional tests
For example: Improve coverage of OWASP Testing Guide, PTES, etc. (lots of room for improvement there!)
* (Top Prio) Put together a great wiki documentation section for contributors
The goal here is to help contributors write tests for the functionality that they implement. This should be as easy as possible.
* (Top Prio) Fix the current Travis issues :)
* (Nice to have) Bring the unit tests up to speed with the codebase
This will be challenging but very worth trying after top priorities.
The wiki should be heavily updated so that contributors create their own unit tests easily moving forward.

#### General background

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

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* Performant and automated regression testing
* Unit tests for a wide coverage of OWASP OWTF, ideally leveraging the Unit Test Framework where possible
* Good documentation

#### Knowledge prerequisite:

Python, experience with unit tests and automated regression testing would be beneficial, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

### OWASP OWTF - Python version upgrade and compatibility

**IMPORTANT** WARNING: This project is considered to be < 2 weeks of effort BUT can be proposed to complement ANOTHER OWTF idea, the last few weeks of GSoC seems the best moment to start this

#### Brief Explanation:

Right now OWASP OWTF works on Python 2.6.5-2.7.3 (might work on surrounding versions too), the aim of this project would be to change the existing codebase so that it additionally works on newer python versions too, for example Python 3.3.
The intention here is to take advantage of improvements in newer python versions when available while letting OWASP OWTF work on older python versions too (i.e. 2.6.5) if that is the only option available.
The solution will ideally be as simple and extensible as possible so that the codebase does not become unmaintanable due to compatibility.

For background on OWASP OWTF please see: [OWASP_OWTF](https://www.owasp.org/index.php/OWASP_OWTF)

#### Expected Results:

* **IMPORTANT**: [PEP-8 compliant code](http://legacy.python.org/dev/peps/pep-0008/) in all modified code and surrounding areas.
* **IMPORTANT**: [OWTF contributor README compliant code](https://github.com/7a/owtf/wiki/Contributor%27s-README)
* Performant and reliable OWASP OWTF execution on multiple python versions, in particular the latest python version (i.e. 3.3.x) as well as the previous 2.6.5-2.7.3 range.
* Test cases
* Good documentation

#### Knowledge prerequisite:

Python, experience with python version upgrades and python version compatibility implementations, some previous exposure to security concepts and penetration testing is welcome but not strictly necessary as long as there is will to learn

**Mentor:** Abraham Aranguren - OWASP OWTF Project Leader - Contact: name.surname@owasp.org

## OWASP PCI TOOLKIT
### OWASP PCI TOOLKIT
OWASP PCI toolkit is an Open Source project built using Google Engine App, that will help organizations scope the PCI-DSS requirements for their System Components. The Payment Card Industry Data Security Standard (PCI DSS) is a proprietary information security standard for organizations that handle cardholder information for the major debit, credit, prepaid, e-purse, ATM, and POS cards.

In order to comply with this standard, organizations need to understand the PCI-DSS requirements. Many of these requirements use OWASP guidelines as their baseline.
 
The OWASP PCI toolkit is a project focused on helping organization understand how OWASP guidelines apply to the PCI-DSS requirements.

#### Expected Results:

4 complete modules built as a Google App Engine: 
[pci-toolkit.appspot.com](http://pci-toolkit.appspot.com/)

#### Knowledge prerequisite:

Skill Level: Easy-Medium
Python, HTML, CSS, Google App Engine.

Affinity with financial institutions, Web security and credit card-online transactions

#### OWASP project page:

[OWASP_PCI_Project](https://www.owasp.org/index.php/Category:OWASP_PCI_Project)

Mentor: Johanna Curiel - emai: firstname.lastname@owasp.org

## OWASP iGoat

### OWASP iGoat

#### Brief Explanation:

Right now OWASP iGoat works fine as a full universal iOS app on iPhone and iPads up to iOS 6.x and Xcode 4.x. It needs to be updated to properly function under iOS 7.x and Xcode 5.x, which will require some code maintenance, GUI changes, and so on.

Although it is primarily maintenance items that need the updating, the student will gain an intimate familiarity with how the iGoat platform works, including how to write and plug-in new exercise modules. Writing additional exercises, with all due credit, will also be encouraged in an optional second phase of this project.

For background on OWASP iGoat please see: [OWASP_iGoat_Project](https://www.owasp.org/index.php/OWASP_iGoat_Project)

#### Expected Results:

* iGoat functions properly in all current aspects under iOS 7.x, compiled under Xcode 5.x.
* All GUI, buttons, and other presentation layer aspects of iGoat are compliant with iOS 7.x look and feel.
* (Optionally) write one or more new iGoat exercise modules, based on existing design descriptions to be provided by the project mentor.

#### Knowledge prerequisite:

iOS app development in Xcode using Objective C will be quite necessary. Familiarity with iOS 7.x user interface updates additionally helpful.

**Mentor:** Ken van Wyk - OWASP iGoat Project Leader - Contact: ken@krvw.com

## [OWASP ZAP](https://www.owasp.org/index.php/ZAP)

### [OWASP ZAP - Advanced access control testing](https://www.owasp.org/index.php/ZAP)

#### Brief Explanation:

Access control testing is typically difficult for security tools to automate. However previous Google Summer of Code projects have added session, authentication, user and role handling to ZAP, which provide an ideal basis for advanced access control testing.

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

This development would allow (semi) automated access control testing by:
* Maintaining and displaying different site trees (application maps) for different users/roles
* Providing tools which access all of the content accessible via one user/role which should not be accessible via another user/role
* Ideally allow resources to be tied to users/roles to allow enable horizontal privilege testing 

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### [OWASP ZAP](https://www.owasp.org/index.php/ZAP) - Scripted Add-ons

#### Brief Explanation:

ZAP supports all JSR 223 scripting languages, but only for a limited number of purposes. This development would allow 'full' add-ons to be written in any JSR 223 language.

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

* Users will be able to 'full' add-ons in any JSR 233 scripting language
* A set of example add-ons demonstrating as much functionality as possible should be developed in at least Java Script, Jython and Jruby.

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### [OWASP ZAP](https://www.owasp.org/index.php/ZAP) - AMF Support

#### Brief Explanation:

ZAP has only very limited support for AMF and does not provide an effective graphical representation of it. 
This development will add full support for AMF.

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

* De-serialise and display AMF messages in ZAP graphically (based on existing POC code)
* Expose the AMF data as parameters so that ZAP can scan them
* Add new AMF specific scan rules as required
* Implement in a way that makes it easier for ZAP to support other technologies (such as Java applets, Silverlight) 

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Colm O'Flaherty - OWASP ZAP Core team

### [OWASP ZAP](https://www.owasp.org/index.php/ZAP) - Web Service (SOAP) scanning

#### Brief Explanation:

ZAP has only very limited support for web service scanning and has no understanding of WSDL.
This development will add full support for exploring and scanning SOAP based web services.

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

The development will allow ZAP to parse WSDL and populate the Sites tree with all of the end points defined. It should also enhance the ZAP scanning capabilities to specifically attack the end points for as wide a range of vulnerabilities. Test cases should be written in [http://code.google.com/p/wavsep/ wavsep] format and contributed back to that project.

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### [OWASP ZAP](https://www.owasp.org/index.php/ZAP) - As a long running service

#### Brief Explanation:

ZAP started out as a GUI only desktop tool. It now supports a headless 'daemon' mode but it is still not suitable for running as a long running service. This will require much heavier use of the database, and ideally will allow different databases to be used. 

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

ZAP able to run as a (very) long running service. There must be no memory leaks code and ideally there should still be very little latency while proxying through ZAP.

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

### [OWASP ZAP](https://www.owasp.org/index.php/ZAP) - GUI unit test framework

#### Brief Explanation:

While ZAP does have some low level unit tests it doesnt have any unit tests for the UI. This means that sometimes changes can break the UI without being immediately apparent.

ZAP is the [most active OWASP project](https://www.ohloh.net/orgs/OWASP) and was voted the [most popular security tool of 2013](http://www.toolswatch.org/2013/12/2013-top-security-tools-as-voted-by-toolswatch-org-readers/) by ToolsWatch.org readers.

#### Expected Results:

A unit test framework which will allow the GUI to be easily tested. A set of unit tests which test the main GUI features and can be easily extended.

#### Knowledge prerequisite:

ZAP is written in Java, so a good knowledge of this language is recommended, as is knowledge of HTML. Some knowledge of application security would be useful, but not essential. 

**Mentor:** Simon Bennetts - OWASP ZAP Project Leader

## [OWASP ESAPI](https://www.owasp.org/index.php/ESAPI) 2.x
### [OWASP ESAPI](https://www.owasp.org/index.php/ESAPI) 2.x - Security Configuration

#### Brief explanation:

There are currently more than a half-dozen of open Google Issues in ESAPI regarding the security configuration component (e.g., see [ESAPI Security Configuration Issues](http://code.google.com/p/owasp-esapi-java/issues/list?q=component%3DSecurityConfiguration)).  

The ESAPI interface for its configuration (SecurityConfiguration) is overly complicated; it has a 'getter' method specific to almost every ESAPI configuration property. The rules for how and where the ESAPI.properties file is found are overly complicated making questions about it one of the most frequently asked questions on forums such as Stack Exchange and the ESAPI mailing lists. This complication leads to a unduly intricate, non-modular reference implementation (DefaultSecurityConfiguration) that makes it difficult to extend in terms of new functionality.

A new, simpler security configuration interface and implementation is needed. Such an implementation would not only be useful for ESAPI 2.x, but could very well be used to build the configurator needed by ESAPI 3.  

As part of this GSoC project, expectations would not only to address as many of the open security configuration issues as possible, but to also go beyond this to allow a framework for additional extensions in terms of functionality.

#### Expected results:

1. An improved, but simpler API for the security configuration part of ESAPI.
2. Alternate configuration stores other than Java properties files (e.g., XML, database), to be supported.
3. The ability to split the ESAPI configuration data into smaller, more manageable chunks to result in more maintainibility and allow for better enforcement of corporate security policies.
4. Continued backward compatibility with ESAPI 2.1.x or an extremely simple migration path forward.

#### Knowledge Prerequisite:

Since the ESAPI 2.x project is written in Java, a good knowledge of Java is essential. A strong knowledge of JUnit will also be helpful in creating unit test cases. A working knowledge of XML or JDBC may also prove helpful.

**Mentor:** Kevin W. Wall - OWASP ESAPI for Java Project Leader

## [OWASP Seraphimdroid Project](https://www.owasp.org/index.php/OWASP_SeraphimDroid_Project)

### [OWASP Seraphimdroid Project](https://www.owasp.org/index.php/OWASP_SeraphimDroid_Project)

#### Brief explanation:

OWASP Seraphimdroid is relatively new OWASP project regarding Android security. Seraphimdroid Android application should become mobile device safeguard, while on the other hand it should also provide user information and knowledge about security risks on their phone (in personalized way). The idea of security guard is based solely on heuristics, that most of the risks costing money and damaging user's privacy can be stopped without huge online database with signatures, and huge malware analysis lab. As part of this GSoC project, focus will be on finding way to stop as many risks that can cost money (premium calls, sms, ussd...) or harm user privacy as possible and to enhance UX of mobile application.

#### Expected results:

* Building features for stopping threats that can cost money originating from third party applications (continue where it was stopped)
* Build and propose features that can stop third party application damage user's privacy by sending user's data out of the mobile device (using internet) 
* Enhance UI/UX

#### Knowledge Prerequisite:

Since the OWASP Seraphimdroid project is written in Java and Android SDK, a good knowledge of Java, Android OS and SDK are essential. Good knowledge of XML and IP protocol can be useful. 

**Mentor:** Nikola Milosevi] - OWASP Seraphimdroid Project Leader

## [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project)

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - ModSecurity Ruby API

#### Brief explanation:

Adding the capability of rapid prototyping to ModSecurity functionalities trough scripts will open the possibility for easy rules production and customization, It also opens the possibility for a large community such as Ruby developers to create their own customization on the top of ModSecurity and so customize their own rules, analog of today's Lua support.

#### Expected results:

An implementation able to handle Ruby scripts which will interact to ModSecurity as Lua does.

#### References:

[Embedding Ruby into C++ (ModSecurity is C, using C++ as reference)](http://aeditor.rubyforge.org/ruby_cplusplus/index.html)
[ModSecurity Reference Manual, Lua](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#wiki-SecRuleScript)

#### Knowledge prerequisite:

C and Ruby programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/).
Mentor: Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - ModSecurity Python API

#### Brief explanation:

Adding the capability of rapid prototyping to ModSecurity functionalities trough scripts will open the possibility for easy rules production and customization, It also opens the possibility for a large community such as Python developers to create their own customization on the top of ModSecurity and so customize their own rules, analog of today's Lua support.

#### Expected results:

An implementation able to handle Python scripts which will interact to ModSecurity as Lua does.

#### References:

[Embedding Python into C/C++:](http://docs.python.org/3.3/extending/embedding.html)
[ModSecurity Reference Manual, Lua:](https://github.com/SpiderLabs/ModSecurity/wiki/Reference-Manual#wiki-SecRuleScript)

#### Knowledge prerequisite:

C and Python programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/)
Mentor: Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - Create "Sniffer-Mode"

#### Brief explanation:

The ModSecurity code includes a "standalone" version that wraps a light weight Apache/APR around the ModSecurity code.  This is used as the basis for the ports to the IIS/Nginx web server platforms.  The goal for this project task is to extend this standalone version so that it can accept a data feed of network traffic (e.g. libpcap) data as input and apply the ModSecurity CRS rules.  Possible solutions could be:
* Create a ModSecurity "plugin" for the Snort IDS.
* Create a ModSecurity "plugin" for the Suricata IDS.
* Add libpcap sniffer wrapper to standalone ModSecurity code to directly pull data off the wire.

#### Expected Results:

This new sniffer mode would allow organizations to run ModSecurity/OWASP ModSecurity CRS in an out of line mode as they do IDS systems.

#### Knowledge prerequisite:

C programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - Implement DoS Prevention Code

#### Brief explanation: https://github.com/SpiderLabs/ModSecurity/issues/416

Implement a request velocity learning engine to identify dynamic DoS thresholds for both the site and for the particular URL.

#### Expected Results:

The new C code in ModSecurity will allow us to add new DoS Protection methods to the OWASP ModSecurity CRS.

#### Knowledge prerequisite:

C programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - Create a Positive Learning/Profile Engine

#### Brief explanation:

See this academic/research paper for ideas of the type of learning we are [looking for](http://www.cs.ucsb.edu/~vigna/publications/2003_kruegel_vigna_ccs03.pdf)

ModSecurity needs a profiling engine that implements the various [AppSensor Detection Points](http://blog.spiderlabs.com/2011/08/implementing-appsensor-detection-points-in-modsecurity.html)

#### Expected Results:

The new engine will implement more detection points to detect abnormal request attributes.

#### Knowledge prerequisite:

C programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

### [OWASP ModSecurity Core Rule Set (CRS)](https://www.owasp.org/index.php/Category:OWASP_ModSecurity_Core_Rule_Set_Project) - Create an Engine to Detect Application Flow Anomalies

#### Brief Explanation:

Need an engine that can track normal application flow paths (click-flows) for business logic transactions - such as transferring money from accounts.  After profiling normal application path flows, we want to then be able to alert to anomalies.  This type of logic can help to prevent Banking Trojan attacks.

Example - let's say an application has a multi-step checkout process to purchase an item.  This new engine would be able to profile/learn which URLs are accessed in what order and identify if clients skip steps or jump directly to other URLs in the flow.

#### Expected Results:

The engine will be able to alert on anomalous application flows.

#### Knowledge prerequisite:

C programming and ModSecurity Development [Guidelines](http://www.modsecurity.org/developers/).

**Mentor:** Felipe Zimmerle Costa and Ryan Barnett - OWASP ModSecurity Core Rule Set Project Leader

## [https://www.owasp.org/index.php/OWASP_Bywaf_Project OWASP ByWaf (CRS)]

### [https://www.owasp.org/index.php/OWASP_Bywaf_Project OWASP ByWaf (CRS)] - PEP-8 compliant

#### Brief Explanation:

Need someone who make our code more pep-8 compliant.

#### Expected Results:

Get our code with the most common accepted Python convention.

#### Knowledge prerequisite:

Advanced level in Python

Knowlage in PEP-8

**Mentor:** Roey Katz and Rafael Gil - OWASP Bywaf Project Leader

### [OWASP ByWaf (CRS)](https://www.owasp.org/index.php/OWASP_Bywaf_Project) - Plug-in maker

#### Brief Explanation:

Making some plug-ins for penetration testing, all of them with bywaf's template.

#### Expected Results:

The following plug-ins are expected:

- SQL Injection
- Cross Site Scripting
- Directory Traversal
- WebDav detector
- Put detector
- Default pages (IIS and Apache)

#### Knowledge prerequisite:

Python
OWASP TOP TEN
HTTP and HTML

**Mentor:** Roey Katz and Rafael Gil- OWASP Bywaf Project Leader
