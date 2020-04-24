---

layout: col-sidebar
title: Secure Software Contract Annex
author: Jeff Williams
contributors:
permalink: /OWASP_Secure_Software_Contract_Annex

---

{% include writers.html %}

**SECURE SOFTWARE DEVELOPMENT CONTRACT ANNEX**

` WARNING: THIS DOCUMENT SHOULD BE CONSIDERED GUIDANCE ONLY.`
` OWASP STRONGLY RECOMMENDS THAT YOU CONSULT A QUALIFIED`
` ATTORNEY TO HELP YOU NEGOTIATE A SOFTWARE CONTRACT.`

## INTRODUCTION

This contract Annex is intended to help software developers and their
clients negotiate and capture important contractual terms and conditions
related to the security of the software to be developed or delivered.
The reason for this project is that most contracts are silent on these
issues, and the parties frequently have dramatically different views on
what has actually been agreed to. We believe that clearly articulating
these terms is the best way to ensure that both parties can make
informed decisions about how to proceed.

`"The security of commercial software will improve when the market demands better security.`
`At a minimum, every software request for proposal should ask vendors to detail how they`
`test their products for security vulnerabilities. This step will start convincing vendors`
`of off-the-shelf software and outsourced developers that enterprises value security."`
`      -- As John Pescatore, research director with Gartner`

We urge Clients and Developers to use this document as a framework for
discussing expectations and negotiating responsibilities. This Annex is
intended to be appended to a software development contract. These terms
are negotiable, meaning they can and should be discussed by the Client
and Developer.

## ABOUT THE PROJECT

This document was created by The Open Web Application Security Project
(OWASP) Foundation, a not-for-profit charitable organization dedicated
to creating free and open tools and documentation related to secure
software. To facilitate easy use in private contracting, this document
is offered under the CC Share Alike 3.0 license. You may modify and use
as you see fit. We welcome comment from both producers and consumers of 
software, as well as the legal community.

OWASP gratefully acknowledges the special contribution from Aspect
Security for their role in the research and preparation of this document.

## OBJECTIONS

The following few pages cover some frequently heard objections to using
this language in software development contracts:

### BUT NOT ALL THE TERMS ARE RIGHT FOR US`...`

This document should be considered a starting point for your agreement.
You may not like all the activities, or may want to propose more. You
may want to assign responsibilities differently. This document is not
intended to exactly capture the needs of all software Clients and
Developers. It is intended to provide a framework for discussing the key
topics that are important to ensuring that software ends up secure.
After you have a security discussion and reach agreement, you should
tailor this agreement to match.

### BUT WHO SHOULD PAY FOR THESE ACTIVITIES`...`

This contract is NOT about putting more burden on the software
developer. The question is not whether there are costs associated with
security -- of course there are. Rather, the right question is what
activities should be performed by both parties to minimize those costs,
and when should they happen.

This annex is intentionally silent on the issue of who should pay for
the activities described herein. While many of these activities should
already be happening, and are expected by many Clients, they are not
regularly practiced in the software industry. The question of who pays
(and how much) should be part of the negotiation.

Calculating the costs of security is very difficult. While there are
costs associated with performing security activities, there are also
significant costs associated with ignoring them. We are convinced that
the most cost-effective way to develop software is to reduce the
likelihood that security flaws are introduced and to minimize the time
between introducing a flaw and fixing it.

One important distinction to make when calculating costs is between
building security mechanisms and the assurance activities that make sure
those mechanisms are correct and effective. Attempting to add mechanisms
at the end of the lifecycle can cause serious design issues and will
increase costs dramatically. This agreement encourages early decisions
on mechanisms to minimize these costs. Similarly, waiting until just
before deployment to do assurance activities, such as code review and
penetration testing, will also dramatically increase costs. We believe
that the most cost-effective way to gain assurance is to put a constant
level of effort into assurance throughout the lifecycle.

### BUT THE LEVEL OF RIGOR IS WRONG`...`

This agreement assumes that the software being developed is reasonably
important to a large enterprise or government agency. We've selected a
"level of rigor" for the agreement that is achievable by most software
development organizations, and will identify and handle the most common
risks.

However, for software that is going to be used in critical applications,
such as medical, financial, or defense related software, you may want to
increase the level of rigor. You may want to add additional reviews,
documentation, and testing activities. You may want to enhance the
processes for finding, diagnosing, and remediating vulnerabilities. For
less sensitive applications, you may want to reduce or remove
activities.

### BUT WE CAN'T TAKE SO MUCH RISK`...`

This agreement is intended to facilitate discussions about who will take
the risk for security vulnerabilities in the software. At one end of the
spectrum, the Client could take all the risk and the Developer could
deliver code with lots of vulnerabilities. At the other extreme, the
Developer could take all the risk and assume responsibility for
delivering perfect code. Both of these extremes are unworkable.

Currently, in this agreement, the Developer takes the risk for problems
that were covered in the requirements or should be covered by reasonable
testing efforts. But remediation of "novel" security issues is to be
paid for by the Client. We believe this is a useful balance, as the
Developer can bound their risk, and encourages Client to get the
security requirements correct up front. But there are many other
possible solutions to this problem. Please let us know if you have
alternative suggestions and we may include them in future versions of
this document.

Note that the discussion here only covers the risk associated with
fixing the security vulnerabilities in the code, and does not include
the costs associated with recovering from any security incidents based
on any exploits of these vulnerabilities. We are interested in best
practices in this area.

### BUT HOW CAN WE ASSURE THIRD PARTY CODE`...`

Almost all software projects use a significant amount of third party
code, such as libraries, frameworks, and products. This code is just as
important from a security perspective as custom code developed
specifically for your project. We believe that the responsibility for
ensuring the security of this code is best borne by Developer, although
they may not have the full capability themselves to guarantee this
security. However, security must be a part of the "build or buy"
decision, and this seems like the best way to encourage that.

Developer, of course, has the option of passing this responsibility
through to the providers of third party software. Developer can also
analyze the third party code themselves, or hire security experts to
analyze it for them.

### BUT WHY SHOULD I GO TO ALL THIS TROUBLE`...`

Ultimately, we believe that there is no alternative to making security a
part of the software contracting process. Currently, we believe that
there are serious misunderstandings about the security of code being
delivered under many software development contracts. This can only lead
to expensive litigation and a decision made by individuals with little
software experience or understanding. Read the [Secure software
contracting hypothetical case
study](https://wiki.owasp.org/index.php/Secure_software_contracting_hypothetical_case_study)
for a full discussion of this problem.

There are many benefits to working through this agreement. The principal
one is that it will make expectations clear between the parties
involved. In some cases it will help to prevent lawsuits when difficult
security problems surface in the software. Also, these are the same
activities that are required by many legal and regulatory compliance
reasons.

### BUT IT'S TOO HARD TO PRODUCE ALL THIS DOCUMENTATION`...`

OWASP does not encourage documentation for documentation's sake. This
agreement is focused on encouraging quality, not quantity. We believe
that it would be possible (on some projects) to meet this contract with
a short risk assessment, a few pages of requirements, a short security
design document, a test plan, and some test results.

The goal of this documentation is simply to ensure, at each stage of the
lifecycle, that appropriate attention has been paid to security. An
additional benefit is that this documentation can be collected together
to form a "certification package" that essentially lays out the argument
for why this software should be trusted to do what it claims it does.

## CONTRACT ANNEX

### 1\. INTRODUCTION

This Annex is made to _____________________
("Agreement") between Client and Developer. Client and Developer agree
to maximize the security of the software according to the following
terms.

### 2\. PHILOSOPHY

This Annex is intended to clarify the security-related rights and
obligations of all the parties to a software development relationship.
At the highest level, the parties agree that:

  __(a) Security Decisions Will Be Based on Risk__ : Decisions about
    security will be made jointly by both Client and Developer based on
    a firm understanding of the risks involved.

<!-- end list -->

  __(b) Security Activities Will Be Balanced__ : Security effort will be
    roughly evenly distributed across the entire software development
    lifecycle.

<!-- end list -->

  __(c) Security Activities Will Be Integrated__ : All the activities and
    documentation discussed herein can and should be integrated into
    Developer's software development lifecycle and not kept separate
    from the rest of the project. Nothing in this Annex implies any
    particular software development process.

<!-- end list -->

  __(d) Vulnerabilities Are Expected__ : All software has bugs, and some
    of those will create security issues. Both Client and Developer will
    strive to identify vulnerabilities as early as possible in the
    lifecycle.

<!-- end list -->

  __(e) Security Information Will Be Fully Disclosed__ : All
    security-relevant information will be shared between Client and
    Developer immediately and completely.

<!-- end list -->

  __(f) Only Useful Security Documentation Is Required__ : Security
    documentation does not need to be extensive in order to clearly
    describe security design, risk analysis, or issues.

### 3\. LIFECYCLE ACTIVITIES

  __(a) Risk Understanding__ : Developer and Client agree to work together
    to understand and document the risks facing the application. This
    effort should identify the key risks to the important assets and
    functions provided by the application. Each of the topics listed in
    the requirements section should be considered.

<!-- end list -->

  __(b) Requirements__ : Based on the risks, Developer and Client agree to
    work together to create detailed security requirements as a part of
    the specification of the software to be developed. Each of the
    topics listed in the requirements section of this Annex should be
    discussed and evaluated by both Developer and Client. These
    requirements may be satisfied by custom software, third party
    software, or the platform.

<!-- end list -->

  __(c) Design__ : Developer agrees to provide documentation that clearly
    explains the design for achieving each of the security requirements.
    In most cases, this documentation will describe security mechanisms,
    where the mechanisms fit into the architecture, and all relevant
    design patterns to ensure their proper use. The design should
    clearly specify whether the support comes from custom software,
    third party software, or the platform.

<!-- end list -->

  __(d) Implementation__ : Developer agrees to provide and follow a set of
    secure coding guidelines and to use a set of common security control
    programming interfaces (such as the [OWASP Enterprise Security API
    (ESAPI)](https://owasp.org/www-project-enterprise-security-api/)).
    Guidelines will indicate how code should be formatted, structured,
    and commented. Common security control programming interfaces will
    define how security controls must be called and how security
    controls shall function. All security-relevant code shall be
    thoroughly commented. Specific guidance on avoiding common security
    vulnerabilities shall be included. Also, all code shall be reviewed
    by at least one other Developer against the security requirements
    and coding guideline before it is considered ready for unit test.

<!-- end list -->

  __(e) Security Analysis and Testing__ : Developer will perform
    application security analysis and testing (also called
    "verification") according to the verification requirements of an
    agreed-upon standard (such as the [OWASP Application Security
    Verification Standard
    (ASVS)](https://owasp.org/www-project-application-security-verification-standard/)).
    The Developer shall document verification findings according to the
    reporting requirements of the standard. The Developer shall provide
    the verification findings to Client.

<!-- end list -->

  __(f) Secure Deployment__ : Developer agrees to provide secure
    configuration guidelines that fully describe all security relevant
    configuration options and their implications for the overall
    security of the software. The guideline shall include a full
    description of dependencies on the supporting platform, including
    operating system, web server, and application server, and how they
    should be configured for security. The default configuration of the
    software shall be secure.

### 4\. SECURITY REQUIREMENT AREAS

The following topic areas must be considered during the risk
understanding and requirements definition activities. This effort should
produce a set of specific, tailored, and testable requirements Both
Developer and Client should be involved in this process and must agree
on the final set of requirements.

  __(a) Input Validation and Encoding__ : The requirements shall specify
    the rules for canonicalizing, validating, and encoding each input to
    the application, whether from users, file systems, databases,
    directories, or external systems. The default rule shall be that all
    input is invalid unless it matches a detailed specification of what
    is allowed. In addition, the requirements shall specify the action
    to be taken when invalid input is received. Specifically, the
    application shall not be susceptible to injection, overflow,
    tampering, or other corrupt input attacks.

<!-- end list -->

  __(b) Authentication and Session Management__ : The requirements shall
    specify how authentication credentials and session identifiers will
    be protected throughout their lifecycle. Requirements for all
    related functions, including forgotten passwords, changing
    passwords, remembering passwords, logout, and multiple logins, shall
    be included.

<!-- end list -->

  __(c) Access Control__ : The requirements shall include a detailed
    description of all roles (groups, privileges, authorizations) used
    in the application. The requirements shall also indicate all the
    assets and functions provided by the application. The requirements
    shall fully specify the exact access rights to each asset and
    function for each role. An access control matrix is the suggested
    format for these rules.

<!-- end list -->

  __(d) Error Handling__ : The requirements shall detail how errors
    occurring during processing will be handled. Some applications
    should provide best effort results in the event of an error, whereas
    others should terminate processing immediately.

<!-- end list -->

  __(e) Logging__ : The requirements shall specify what events are
    security-relevant and need to be logged, such as detected attacks,
    failed login attempts, and attempts to exceed authorization. The
    requirements shall also specify what information to log with each
    event, including time and date, event description, application
    details, and other information useful in forensic efforts.

<!-- end list -->

  __(f) Connections to External Systems__ : The requirements shall specify
    how authentication and encryption will be handled for all external
    systems, such as databases, directories, and web services. All
    credentials required for communication with external systems shall
    be stored outside the code in a configuration file in encrypted
    form.

<!-- end list -->

  __(g) Encryption__ : The requirements shall specify what data must be
    encrypted, how it is to be encrypted, and how all certificates and
    other credentials must be handled. The application shall use a
    standard algorithm implemented in a widely used and tested
    encryption library.

<!-- end list -->

  __(h) Availability__ : The requirements shall specify how it will
    protect against denial of service attacks. All likely attacks on the
    application should be considered, including authentication lockout,
    connection exhaustion, and other resource exhaustion attacks.

<!-- end list -->

  __(i) Secure Configuration__ : The requirements shall specify that the
    default values for all security relevant configuration options shall
    be secure. For audit purposes, the software should be able to
    produce an easily readable report showing all the security relevant
    configuration details.

<!-- end list -->

  __(j) Specific Vulnerabilities : The requirements shall include a set
    of specific vulnerabilities that shall not be found in the software.
    If not otherwise specified, then the software shall not include any
    of the flaws described in the current "OWASP Top Ten Most Critical
    Web Application Vulnerabilities."

### 5\. PERSONNEL AND ORGANIZATION

  __(a) Security Architect__ : Developer will assign responsibility for
    security to a single senior technical resource, to be known as the
    project Security Architect. The Security Architect will certify the
    security of each deliverable.

<!-- end list -->

  __(b) Security Training__ : Developer will be responsible for verifying
    that all members of the developer team have been trained in secure
    programming techniques.

<!-- end list -->

  __(c) Trustworthy Developers__ : Developer agrees to perform appropriate
    background investigation of all development team members.

### 6\. DEVELOPMENT ENVIRONMENT

  __(a) Secure Coding__ : Developer shall disclose what tools are used in
    the software development environment to encourage secure coding.

<!-- end list -->

  __(b) Configuration Management__ : Developer shall use a source code
    control system that authenticates and logs the team member
    associated with all changes to the software baseline and all related
    configuration and build files.

<!-- end list -->

  __(c) Distribution__ : Developer shall use a build process that reliably
    builds a complete distribution from source. This process shall
    include a method for verifying the integrity of the software
    delivered to Client.

### 7\. LIBRARIES, FRAMEWORKS, AND PRODUCTS

  __(a) Disclosure__ : Developer shall disclose all third party software
    used in the software, including all libraries, frameworks,
    components, and other products, whether commercial, free,
    open-source, or closed-source.

<!-- end list -->

  __(b) Evaluation__ : Developer shall make reasonable efforts to ensure
    that third party software meets all the terms of this agreement and
    is as secure as custom developed code developed under this
    agreement.

### 8\. SECURITY REVIEWS

  __(a) Right to Review__ : Client has the right to have the software
    reviewed for security flaws at their expense at any time within 60
    days of delivery. Developer agrees to provide reasonable support to
    the review team by providing source code and access to test
    environments.

<!-- end list -->

  __(b) Review Coverage__ : Security reviews shall cover all aspects of
    the software delivered, including custom code, components, products,
    and system configuration.

<!-- end list -->

  __(c) Scope of Review__ : At a minimum, the review shall cover all of
    the security requirements and should search for other common
    vulnerabilities. The review may include a combination of
    vulnerability scanning, penetration testing, static analysis of the
    source code, and expert code review.

<!-- end list -->

  __(d) Issues Discovered__ : Security issues uncovered will be reported
    to both Client and Developer. All issues will be tracked and
    remediated as specified in the Security Issue Management section of
    this Annex.

### 9\. SECURITY ISSUE MANAGEMENT

  __(a) Identification__ : Developer will track all security issues
    uncovered during the entire lifecycle, whether a requirements,
    design, implementation, testing, deployment, or operational issue.
    The risk associated with each security issue will be evaluated,
    documented, and reported to Client as soon as possible after
    discovery.

<!-- end list -->

  __(b) Protection__ : Developer will appropriately protect information
    regarding security issues and associated documentation, to help
    limit the likelihood that vulnerabilities in operational Client
    software are exposed.

<!-- end list -->

  __(c) Remediation__ : Security issues that are identified before
    delivery shall be fixed by Developer. Security issues discovered
    after delivery shall be handled in the same manner as other bugs and
    issues as specified in this Agreement.

### 10\. ASSURANCE

  __(a) Assurance__ : Developer will provide a "certification package"
    consisting of the security documentation created throughout the
    development process. The package should establish that the security
    requirements, design, implementation, and test results were properly
    completed and all security issues were resolved appropriately.

<!-- end list -->

  __(b) Self-Certification__ : The Security Architect will certify that
    the software meets the security requirements, all security
    activities have been performed, and all identified security issues
    have been documented and resolved. Any exceptions to the
    certification status shall be fully documented with the delivery.

<!-- end list -->

  __(c) No Malicious Code__ : Developer warrants that the software shall
    not contain any code that does not support a software requirement
    and weakens the security of the application, including computer
    viruses, worms, time bombs, back doors, Trojan horses, Easter eggs,
    and all other forms of malicious code.

### 11\. SECURITY ACCEPTANCE AND MAINTENANCE

  __(a) Acceptance__ : The software shall not be considered accepted until
    the certification package is complete and all security issues have
    been resolved.

<!-- end list -->

  __(b) Investigating Security Issues__ : After acceptance, if security
    issues are discovered or reasonably suspected, Developer shall
    assist Client in performing an investigation to determine the nature
    of the issue. The issue shall be considered "novel" if it is not
    covered by the security requirements and is outside the reasonable
    scope of security testing.

<!-- end list -->

  __(c) Novel Security Issues__ : Developer and Client agree to scope the
    effort required to resolve novel security issues, and to negotiate
    in good faith to achieve an agreement to perform the required work
    to address them.

<!-- end list -->

  __(d) Other Security Issues__ : Developer shall use all commercially
    reasonable efforts consistent with sound software development
    practices, taking into account the severity of the risk, to resolve
    all security issues not considered novel as quickly as possible.
