---

layout: col-sidebar
title: Source Code Analysis Tools
author: 
contributors: 
  - Dave Wichers, itamarlavender, will-obrien, Eitan Worcel, Prabhu Subramanian, kingthorin, coadaflorin, hblankenship, GovorovViva64, pfhorman, GouveaHeitor, Clint Gibler, DSotnikov, Ajin Abraham, Noam Rathaus, Mike Jang
tags: source code analysis, static code analysis, tools
permalink: /Source_Code_Analysis_Tools

---

{% include writers.html %}

[Source code analysis](Static_Code_Analysis) tools, also known as Static Application Security Testing (SAST) Tools, can help analyze source code or compiled versions of code to help find security flaws.

SAST tools can be added into your IDE. Such tools can help you detect issues during software development.
SAST tool feedback can save time and effort, especially when compared to finding vulnerabilities later in the development cycle.

## Strengths and Weaknesses

### Strengths

- Scales well -- can be run on lots of software, and can be run repeatedly (as with nightly builds or continuous integration).
- Identifies certain well-known vulnerabilities, such as:
  - Buffer overflows
  - SQL injection flaws
- Output helps developers, as SAST tools highlight the problematic code, by filename,
  location, line number, and even the affected code snippet.

### Weaknesses

- Difficult to automate searches for many types of security vulnerabilities, including:
  - Authentication problems
  - Access control issues
  - Insecure use of cryptography
- Current SAST tools are limited. They can automatically identify only a relatively
  small percentage of application security flaws.
- High numbers of false positives.
- Frequently unable to find configuration issues, since they are not represented in the code.
- Difficult to 'prove' that an identified security issue is an actual vulnerability.
- Many SAST tools have difficulty analyzing code that can't be compiled.
  - Analysts frequently cannot compile code unless they have:
    - Correct libraries
    - Compilation instructions
    - All required code

## Important Selection Criteria

- Prerequisite: Support your programming language.
- Ability to detect vulnerabilities, based on:
  - The [OWASP Top Ten](/www-project-top-ten/)
  - Other criteria such as:
      - [OSSTMM](https://www.isecom.org/OSSTMM.3.pdf)
      - [CHECK](https://www.ncsc.gov.uk/information/check-penetration-testing)
- Accuracy:
  - False Positive/False Negative rates
  - OWASP [Benchmark](/www-project-benchmark/) score
- Ability to understand the libraries/frameworks you need
- Requirement for buildable source code
- Ability to run against binaries (instead of source)
- Availability as a plugin into preferred developer IDEs
- Ease of setup/use
- Ability to include in Continuous Integration/Deployment tools
- License cost (May vary by user, organization, app, or lines of code)
- Interoperability of output:
  - See OASIS [SARIF (Static Analysis Results Interchange Format)](https://rawgit.com/sarif-standard/sarif-spec/master/ standard)

## Disclaimer

**The tools listed in the tables below are presented in alphabetical order. *OWASP does not endorse any of the vendors or tools by listing them in the table below.* We have made every effort to provide this information as accurately as possible. If you are the vendor of a tool below and think that this information is incomplete or incorrect, please send an e-mail to our mailing list and we will make every effort to correct this information.**

{% include tools.html type="SAST" %}

## More info

- [NIST's list of Source Code Security Analysis Tools](https://samate.nist.gov/index.php/Source_Code_Security_Analyzers.html).
- [DAST Tools](/www-community/Vulnerability_Scanning_Tools) - Similar info on Dynamic Application Security Testing (DAST) Tools.
- [Free for Open Source Application Security Tools](/www-community/Free_for_Open_Source_Application_Security_Tools) - This page lists the Commercial Source Code Analysis Tools (SAST) we know of that are free for Open Source.
