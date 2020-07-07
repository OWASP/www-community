---

layout: col-sidebar
title: Virtual Patching Best Practices
author: 
contributors: 
tags: virtual patching
permalink: /Virtual_Patching_Best_Practices
auto-migrated: 1

---

{% include writers.html %}

# Introduction

This paper presents a virtual patching framework that organizations can
follow to maximize the timely implementation of virtual patches. It also
demonstrates, as an example, how a web application firewall,
([WAF](WAF "wikilink")) such as ModSecurity, can be used to remediate a
sampling of vulnerabilities in the OWASP WebGoat application. This
document was initially developed as a collaborative outcome from the
OWASP Global [Summit 2011](Summit_2011 "wikilink").

# What is a Virtual Patch?

The term virtual patching was originally coined by Intrusion Prevention
System (IPS) vendors a number of years ago. It is not a web application
specific term, and may be applied to other protocols however currently
it is more generally used as a term for Web Application Firewalls (WAF).
It has been known by many different names including both *External
Patching* and *Just-in-time Patching*. Whatever term you choose to use
is irrelevant. What is important is that you understand exactly what a
virtual patch is.

## Definition

***A security policy enforcement layer which prevents the exploitation
of a known vulnerability.***

The virtual patch works since the security enforcement layer analyzes
transactions and intercepts attacks in transit, so malicious traffic
never reaches the web application. The resulting impact of virtual patch
is that, while the actual source code of the application itself has not
been modified, the exploitation attempt does not succeed.

# Value of Virtual Patching

When you consider the numerous situations when organizations can’t
simply immediately edit the source code, the value of virtual patching
becomes apparent. From an organizations perspective, the benefits are:

  - It is a scalable solution as it is implemented in few locations vs.
    installing patches on all hosts.
  - It reduces risk until a vendor-supplied patch is released or while a
    patch is being tested and applied.
  - There is less likelihood of introducing conflicts as libraries and
    support code files are not changed.
  - It provides protection for mission-critical systems that may not be
    taken offline.
  - It reduces or eliminates time and money spent performing emergency
    patching.
  - It allows organizations to maintain normal patching cycles.

From a web application security consultant’s perspective, virtual
patching opens up another avenue for providing services to your clients.
Traditionally, if source code could not be updated for any of the
reasons previously specified, there wasn’t much else a consultant could
do to help. Now, a consultant can offer to create virtual patches to
externally address the issues outside of the application code.

# Why Not Just Fix the Code?

From a purely technical perspective, the number one remediation strategy
would be for an organization to correct the identified vulnerability
within the source code of the web application. This concept is
universally agreed upon by both web application security experts and
system owners. Unfortunately, in real world business situations, there
arise many scenarios where updating the source code of a web application
is not easy. Common roadblocks to source code fixes include:

## Patch Availability

If a vulnerability is identified within a commercial application, the
customer most likely will not be able to modify the source code
themselves. In this situation, the customer is held at the mercy of the
Vendor as they have to wait for an official patch to be released.
Vendors usually have extremely rigid patch release dates, which mean
that an officially supported patch may not be available for an extended
period of time.

## Installation Time

Even in situations where an official patch is available, or a source
code fix could be applied to a custom coded application, the normal
patching processes of most organizations is time consuming. This is
usually due to the extensive regression testing required after code
changes. It is not uncommon for these testing gates to be measured in
months. For example, the Symantec Internet Threat Report \[1\] stated
that the average time it took for organizations to patch their systems
was 55 days, while the Whitehat Security Web Security Statistics Report
\[2\] documented that their customers time-to-fix average was 138 days
to remediate SQL Injection vulnerabilities found in their web
applications. Now contrast this patching data with the fact that
Symantec also reported that it only took an average of 6 days for
exploit code to be released to the public and it becomes clear that
traditional source code patching processes are not adequate.

## Fixing Custom Code May Be Cost Prohibitive

Web assessments that include source code reviews, vulnerability scanning
and penetration tests will most assuredly identify vulnerabilities in
your web application. Identification of the vulnerability is only the
first half of the battle with the second half being the remediation
actions. What many organizations are finding out is that the cost
associated with the identification of the vulnerabilities often pales in
comparison to that of actually fixing the issues. This is especially
true when vulnerabilities are not found early in the design or testing
phases but rather after an application is already in production. In
these situations, it is usually deemed that it is just too expensive to
recode the application.

## Legacy Code

An organization may be using a commercial application and the vendor has
gone out of business, or they are using a version that is no longer
supported by the vendor. In these situations, legacy application code
can’t be patched. An additional situation is when an organization is
forced into using outdated vendor code due to in-house custom coded
functionality being added on top of the original vendor code. This
functionality is tied to a mission critical business application and
prior upgrade attempts broke functionality.

## Outsourced Code

As more and more businesses opt to outsource their application
development, they are finding that executing vulnerability fixes would
require an entirely new project. Many organizations are facing the harsh
reality that poor contractual language oftentimes does on cover “secure
coding” issues but only functional defects.

# Virtual Patching Tools

There are a number of different tools that may be used for virtual
patching efforts.

  - Intermediary device such as a WAF or IPS
  - Web server plugin such as ModSecurity
  - Application layer filter such as ESAPI WAF

## Robust HTTP and HTML Parsing

The tool must use an HTTP and HTML parser to analyze the input stream.
The parser must be able to understand specific protocol features
including content encoding such as chunked encoding or
multipart/form-data encoding, request and response compression and even
XML payload.

In addition the parser must be flexible as the environment protected as
many headers and protocol elements are not used according to RFC
requirements. For example, while the RFC requires a single space between
the method and the URI in the HTTP request line, Apache allows any
sequence of whitespace between them. Another example is PHP unique use
of parameters: in PHP leading and trailing spaces are removed from
parameter names. In a proxy deployment a stricter parsing may be
acceptable, however the tool has to be at least as flexible as the web
server in order to prevent evasion. IDS/IPS systems that fail to do so
can be easily evaded by attackers.

## Protocol Analysis

Based on the parsed info, the tool must break up the HTTP stream into
logical entities that can be inspected, such as headers, parameters and
uploaded files. Each element is inspected separately not just for its
content, but also for its length and count. In addition the tool must
correctly divide the network stream when keep-alive HTTP connections are
used to unique request and replies, and correctly match requests and
replies.

## Anti-Evasion Capabilities

Modern protocols such as HTTP and HTML allow the same information to be
presented in multiple ways. As a result signature based detection of
attacks must inspect the attack vector in any form it may be in.
Attackers evade detection systems by using a less common presentation of
the attack vector. Some common evasion techniques include using
different character encodings for the attack vector or using none
canonized path names. In order to prevent evasion the tool must
transform the request to a normalized form before inspection.

The tools should be able to selectively employ normalization functions
for different input fields for each inspection performed. For example,
the tools should be able to normalize an HTML form field that accepts
path names as input.

## Rules instead of Signatures

Virtual patches must implement complex logic, as it cannot rely solely
on signatures and requires a more robust rules language to define the
tests. For example, the following features exist in the ModSecurity
rules language: • Operators and logical expressions – can check an input
field for attributed other than its content, such as its size or
character distribution. Additionally ModSecurity can combine such atoms
to create more complex conditions using logical operators. For example,
it may inspect if a field length is too long only for a specific value
of another field, or alternatively check if two different fields are
empty. • Selectable anti-evasion transformation functions – as discussed
above, each rule can employ specific transformation function. •
Variables, sessions & state management – since the protocols inspected
keep state, the rules language needs to include variables. Such
variables can persist for a single transaction, for the life of a
session, or globally. Using such variables enables ModSecurity to
aggregate information and therefore detect an attack based on multiple
indications during the life span of a transaction or a session. Attacks
that require such mechanisms to detect are brute force attacks,
application layer denial of service attacks and business logic flaws. •
Control structures – the ModSecurity rules language includes control
structures such as conditional execution. Such structures enable
ModSecurity to perform different rules based on transaction content. For
example, if the transaction payload is XML, an entirely different set of
rules may be used.

# A Virtual Patching Methodology

Virtual Patching, like most other security processes, is not something
that should be approached haphazardly. Instead, a consistent, repeatable
process should be followed that will provide the best chances of
success. The following virtual patching workflow mimics the industry
accepted practice for conducting IT Incident Response and consists of
the following phases: Preparation, Identification, Analysis, Virtual
Patch Creation, Implementation/Testing, and Recovery/Follow T Up.

## Preparation Phase

The importance of properly utilizing the preparation phase with regards
to virtual patching cannot be overstated. The idea is that you need to
do a number of things to setup the virtual patching processes and
framework prior to actually having to deal with an identified
vulnerability, or worse yet, react to a live web application intrusion.
The point is that during a live compromise is not the ideal time to be
proposing installation of a web application firewall and the concept of
a virtual patch. Tension is high during real incidents and time is of
the essence, so lay the foundation of virtual patching when the waters
are calm and get everything in place and ready to go when an incident
does occur. Here are a few critical items that should be addressed
during the preparation phase: • Ensure that you are signed up for on all
vendor alert mail-lists for commercial software that you are using. This
will ensure that you will be notified in the event that the vendor
releases vulnerability information and patching data. • Virtual Patching
Pre-Authorization – Virtual Patches need to be implemented quickly so
the normal governance processes and authorizations steps for standard
software patches need to be expedited. Since virtual patches are not
actually modifying source code, they do not require the same amount of
regression testing as normal software patches. I have found that
categorizing virtual patches in the same group as Anti-Virus updates or
Network IDS signatures helps to speed up the authorization process and
minimize extended testing phases. • Deploy ModSecurity In Advance - As
time is critical during incident response, it would be a poor time to
have to get approvals to install new software. You can install
ModSecurity in embedded mode on your Apache servers, or an Apache
reverse proxy server. The advantage with this deployment is that you can
create fixes for non-Apache back-end servers. Even if you do not use
ModSecurity under normal circumstances, it is best to have it “on deck”
ready to be enabled if need be. • Increase Audit Logged – The standard
Common Log Format (CLF) utilized by most web servers does not provide
adequate data for conducting proper incident response. Consider the
following Apache access_log entry:

80.87.72.6 - - \[22/Apr/2007:18:55:53 --0400\] \\ "POST /xmlrpc.php
HTTP/1.1" 200 293

We see that this request uses a POST Request Method. This means that
critical data such as the Request Body (where the client is passing
parameter data) is not logged. Without the full request payloads, it is
next to impossible to accurately confirm either an attack attempt or a
successful compromise. Fortunately, ModSecurity has a robust audit
logging engine that is able to capture the entire request and response
payloads. The following audit log entry is for the same xmlrpc.php
request we showed from the Apache access_log file.

\--ddb9bf17-A-- \[22/Apr/2007:18:55:53 --0400\] dGgsYX8AAAEAABJkpY8AAACG
80.87.72.6 41376 192.168.1.133 80 --ddb9bf17-B-- POST /xmlrpc.php
HTTP/1.1 TE: deflate,gzip;q=0.3 Connection: TE, close Host:
www.example.com User-Agent: libwww-perl/5.805 Content-Length: 201
--ddb9bf17-C--

<?xml version="1.0"?>

<methodCall><methodName>test.method</methodName><params><param><value><name>',''));echo'_begin_';echo
\`id;ls/;w\`;echo
'_end_';exit;/\*</name></value></param></params></methodCall>

As you can see, now that we can see the request body contents, we are
able to identify that the client is attempting to exploit the php
application and is attempting to execute OS command injection.

## Identification Phase

The Identification Phase occurs when an organization becomes aware of a
vulnerability within their web application. There are generally two
different methods of identifying vulnerabilities: Proactive and
Reactive. Proactive Identification This occurs when an organization
takes it upon themselves to assess their web security posture and
conducts the following tasks: • Vulnerability assessment (internal or
external) and penetration tests • Source code reviews These tasks are
extremely important for custom coded web applications as there would be
external entity that has the same application code. Reactive
Identification There are three main reactive methods for identifying
vulnerabilities: • Vendor contact (e.g. pre-warning) - Occurs when a
vendor discloses a vulnerability for commercial web application software
that you are using. • Public disclosure - Public vulnerability
disclosure for commercial/open source web application software that you
are using. The threat level for public disclosure is increased as more
people know about the vulnerability. • Security incident – This is the
most urgent situation as the attack is active. In these situations,
remediation must be immediate. Normal network security response measures
include blocking the source IP of the attack at a firewall or edge
security device. This technique does not work as well for web
application attacks as you may prevent legitimate users from accessing
the application. A virtual patch is more flexible as it is not
necessarily where an attacker is coming from but what they are sending.

## Analysis Phase

There are a number of tasks that must be completed during the analysis
phase. What is the name of the vulnerability? This means that you need
to have the proper CVE name/number identified by the vulnerability
announcement, vulnerability scan, etc… What is the impact of the
problem? It is always important to understand the level of criticality
involved with a web vulnerability. Information leakages may not be
treated in the same manner as an SQL Injection issue. What versions of
software are affected? You need to identify what versions of software
are listed so that you can determine if the version(s) you have
installed are affected. What configuration is required to trigger the
problem or how to tell if you are affected by the problem? Some
vulnerabilities may only manifest themselves under certain configuration
settings. Is proof of concept exploit code available? Many vulnerability
announcements have accompanying exploit code that shows how to
demonstrate the vulnerability. If this data is available, make sure to
download it for analysis. This will be useful later on when both
developing and testing the virtual patch. Is there a work around
available without patching or upgrading? This is where virtual patching
actually comes into play. It is a temporary work-around that will buy
organizations time while they implement actual source code fixes. Is
there a patch available? Unfortunately, vulnerabilities are often
announced without an accompanying patch. This leaves organizations
exposed and is why virtual patching has become an invaluable tool. If
there is a patch available, then you initiate the proper patch
management processes and simultaneously create a virtual patch.

## Virtual Patch Creation Phase

The process of creating an accurate virtual patch is bound by two main
tenants:

1\. No false positives. Do not ever block legitimate traffic under any
circumstances. This is always the top priority. 2. No false negatives.
Do not miss attacks, even when the attacker intentionally tries to evade
detection. This is a high priority.\[4\]

The virtual patch creator must keep these priorities, and their relative
ordering, in mind at all times. A key distinction between virtual patch
construction philosophies (log-only mode vs. a blocking mode) lies in
the relative ranking of these two goals. The art of creating blocking
virtual patches is generalizing the detection logic as much as possible
to rigorously meet rule \#2, without ever violating rule \#1. Deriving a
Zero False Negative Virtual Patch When performing technical
vulnerability research, the virtual patch writer must first search for
all of the necessary conditions for an attack to succeed. The researcher
starts by obtaining technical data that triggers the vulnerability
remotely (perhaps from proof of concept exploit code). The writer then
varies or fuzzes all the “interesting-looking” parts of the attack.
Changes are made one at a time, in steps, keeping careful notes.
(Strings, length values, character encoding, white space… the list goes
on. All are good things to vary.) If the attack succeeds even when a
particular variable is set to a random value, that variable is not
important for the virtual patch criteria. Eventually the researcher can
identify the complete set of variables that are important to the
attack’s success, and arrive at a set of criteria that must be
collectively satisfied for any attack to succeed. If there are multiple
distinct attack vectors, the researcher must perform this analysis on
each one separately.

Given a set of criteria that must be satisfied for an attack to succeed,
it is possible to describe virtual patching logic that has zero false
negatives. That is, an attack simply cannot succeed unless the
associated web application attack traffic has exactly the
characteristics that the virtual patch is looking for. Deriving a Zero
False Positive Virtual Patch Given a zero false negative virtual patch
as previously described, the writer must also evaluate the accuracy of
patch in terms of false positives. At this stage, the writer attempts to
identify at least one characteristic that would never occur in normal
web traffic. If a characteristic exists that is both anomalous compared
to normal traffic and critical to the attack’s success, then the zero
false negative virtual patch is also a zero false positive signature.
Negative Security Virtual Patches A negative security model (or misuse
based detection) is based on a set of rules that detect specific known
attacks rather than allow only valid traffic. It is important to note
that the differentiation between negative and positive security models
is subjective and reflects how tight the security envelope around the
application is. A good example would be limiting the characters allowed
in an input field. Since the character set is a closed set, providing an
allow list of permitted characters is actually similar to providing a
deny list of forbidden characters including the characters
complementing the 1st group. Positive Security Virtual Patches Positive
security model is a comprehensive security mechanism that provides an
independent input validation envelope to an application. The model
specifies the characteristics of valid input (character set, length,
etc…) and denies anything that does not conform. By defining rules for
every parameter in every page in the application the application is
protected by an additional security envelop independent from its code.
Which Method is Better for Virtual Patching – Positive or Negative
Security? A virtual patch may employ either a negative or positive
security model. Which one you decide to use depends on the situation and
a few different considerations. For example, negative security rules can
usually be implemented more quickly, however the possible evasions are
more likely.

Positive security rules, only the other hand, provides better protection
however it is often a manual process and thus is not scalable and
difficult to maintain for large/dynamic sites. While manual positive
security rules for an entire site may not be feasible, a positive
security model can be selectively employed when a vulnerability alert
identifies a specific location with a problem. Beware of
Exploit-Specific Virtual Patches You want to resist the urge to take the
easy road and quickly create an exploit-specific rule. While it may
provide some immediate protection, its long term value is significantly
decreased. A case study of this concept in the IDS world is "bleeding
edge" snort signature for Bugtraq vulnerability \#21799. This
vulnerability in the Cacti open source graphing software was picked
quite at random. The exploit references on Bugtraq vulnerabilities
archive is:

/cacti/cmd.php?1+1111)/\*\*/UNION/\*\*/SELECT/\*\*/2,0,1,1,127.0.0
.1,null,1,null,null,161,500, proc,null,1,300,0, ls -la \>
./rra/suntzu.log,null,null/\*\*/FROM/\*\*/host/\*+11111

And the Snort signature is:

alert tcp $EXTERNAL_NET any -\> $HTTP_SERVERS $HTTP_PORTS (
msg:"BLEEDING-EDGE WEB Cacti cmd.php Remote Arbitrary SQL Command
Execution Attempt"; flow:to_server,established; uricontent:"/cmd.php?";
nocase; uricontent:"UNION"; nocase; uricontent:"SELECT"; nocase;
reference:cve,CVE-2006-6799; reference:bugtraq,21799; classtype:
web-application-attack; sid:2003334; rev:1; )

While snort has some anti-evasion techniques such as case insensitivity
and URI decoding, this signature still falls short of detecting an
exploit of the vulnerability. It is gears only towards detecting the
specific attack vector shown above. Any other exploit such as blind SQL
injection would not be detected. It also searches for the keywords only
in the request line, while many development environments would allow for
parameters to be provided both in the POST and GET payload.

Additionally this signature is prone to false positives as both select
and union are common English words and since the signature do not
require any word delimiters the signature will also be satisfied by the
words "Selection" and "Reunion". In many cases such a signature has to
be turned off.

For examples of poorly written ModSecurity rules, let’s look at the
following GotRoot rule:

SecDefaultAction "log,deny,phase:2,status:500,t:urlDecodeUni, \\
t:htmlEntityDecode,t:lowercase"

1.  WEB-CGI csSearch.cgi arbitrary command execution attempt

SecRule REQUEST_URI "/csSearch\\.cgi\\?" chain SecRule REQUEST_URI
"\\\`"

In the first line, the SecDefaultAction is specifying the use of the
“t:lowercase” transformation function. This is often used to normalize
input data for anti-evasion. When this is used, care should be taken to
specify only lowercase letters in the operator payload section. In this
rule example, however, the rule writer mistakenly used mixed-case and
thus this rule would not trigger (false negative).

## Implementation/Testing Phase

In order to accurately test out the newly created virtual patches, it
may be necessary to use an application other than a web browser. Some
useful tools are: • Command line web clients such as Curl and Wget. •
Local Proxy Servers such as WebScarab
(http://www.owasp.org/index.php/Category:OWASP_WebScarab_Project) and
Burp Proxy (http://www.portswigger.net/suite/). • ModSecurity
AuditViewer (http://www.jwall.org/web/audit/viewer.jsp) – which allows
you to load a ModSecurity audit log file, manipulate it and then
re-inject the data back into any web server. These tools will allow you
to manipulate the request data in any way desired. ModSecurity’s Debug
Log File In order to verify exactly how your new rule is working, you
should review the ModSecurity SecDebugLog file data. The Debug log
provides extensive details on the rule processing order and in many
cases is the only true way to verify that the rule is working exactly as
you expected. You will most likely need to increase the SecDebugLogLevel
directive setting to get enough detail to validate the patch processing.
You can selectively increase the logging based on source IP address so
that you don’t impact performance on the entire web server. Below is an
excerpt of the debug log data during rule processing (some data deleted
for readibility):

Recipe: Invoking rule 82211d8. Executing operator \!rx with param
"^(POST)$" against REQUEST_METHOD. Target value: POST Operator
completed in 17 usec. Rule returned 0. No match, not chained -\> mode
NEXT_RULE. Recipe: Invoking rule 82214b0. Rule returned 0. No match,
not chained -\> mode NEXT_RULE. Recipe: Invoking rule 82360d0.
Executing operator \!rx with param "^(\\w{0,32})$" against
ARGS:username. Target value:
0000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000
Operator completed in 13 usec. Rule returned 1. Match, intercepted -\>
returning. Access denied with code 501 (phase 2). Match of "rx
^(\\w{0,32})$" against "ARGS:username" required. \[id "1"\] \[msg
"Postparameter username failed validity check. Value domain:
Username."\] \[severity "ERROR"\]

## Recovery/Follow-Up Phase

Although you may need to expedite the implementation of virtual patches,
you should still track them in your normal Patch Management processes.
This means that you should create proper change request tickets, etc… so
that their existence and functionality is documented.

You should also have periodic re-assessments to verify if/when you can
remove previous virtual patches if the web application code has been
updated with the real source code fix. I have found that many people opt
to keep virtual patches in place due to better identification/logging
vs. application or db capabilities.

### Authors

  - Ryan Barnett with collaboration from OWASP Global Summit Attendees:
    [Summit 2011 Working
    Sessions/Session091](Summit_2011_Working_Sessions/Session091 "wikilink")
  - Dan Cornell
  - [Achim Hoffmann](User:Achim "wikilink")
  - Martin Knobloch

## References

Detailed definitions and more in-depth descriptions concerning WAS - Web
Application Security - can be found at:

  - OWASP [Virtual Patching Cheat
    Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Virtual_Patching_Cheat_Sheet.html)
  - [OWASP Best Practices: Use of Web Application
    Firewalls](:Category:OWASP_Best_Practices:_Use_of_Web_Application_Firewalls "wikilink")
  - [OWASP Securing WebGoat using ModSecurity
    Project](:Category:OWASP_Securing_WebGoat_using_ModSecurity_Project "wikilink")
  - [OWASP ModSecurity Core Rule
    Set](:Category:OWASP_ModSecurity_Core_Rule_Set_Project "wikilink")

[ModSecurity Core Rule Set Project](Category:OWASP_Project "wikilink")
[ModSecurity Core Rule Set Project](Category:OWASP_WAF "wikilink")
[Category:OWASP Document](Category:OWASP_Document "wikilink")
[Category:How To](Category:How_To "wikilink")
