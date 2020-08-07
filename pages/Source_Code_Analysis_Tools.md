---

layout: col-sidebar
title: Source Code Analysis Tools
author: 
contributors: 
  - Dave Wichers, itamarlavender, will-obrien, Eitan Worcel, Prabhu Subramanian, kingthorin, coadaflorin, hblankenship, GovorovViva64, pfhorman, GouveaHeitor, Clint Gibler, DSotnikov, Ajin Abraham, Noam Rathaus   
tags: source code analysis, static code analysis, tools
permalink: /Source_Code_Analysis_Tools

---

{% include writers.html %}

[Source code analysis](Static_Code_Analysis) tools, also referred to as Static Application Security Testing (SAST) Tools, are designed to analyze source code or compiled versions of code to help find security flaws.

Some tools are starting to move into the IDE. For the types of problems that can be detected during the software development phase itself, this is a powerful phase within the development life cycle to employ such tools, as it provides immediate feedback to the developer on issues they might be introducing into the code during code development itself. This immediate feedback is very useful, especially when compared to finding
vulnerabilities much later in the development cycle.

## Strengths and Weaknesses

### Strengths

- Scales well -- can be run on lots of software, and can be run repeatedly (as with nightly builds or continuous integration).
- Useful for things that such tools can automatically find with high confidence, such as buffer overflows, SQL Injection Flaws, and so forth.
- Output is good for developers -- highlights the precise source files, line numbers, and even subsections of lines that are affected.

### Weaknesses

- Many types of security vulnerabilities are difficult to find automatically, such as authentication problems, access control issues, insecure use of cryptography, etc. The current state of the art only allows such tools to automatically find a relatively small percentage of application security flaws. However, tools of this type are getting better.
- High numbers of false positives.
- Frequently can't find configuration issues, since they are not represented in the code.
- Difficult to 'prove' that an identified security issue is an actual vulnerability.
- Many of these tools have difficulty analyzing code that can't be compiled. Analysts frequently can't compile code because they don't have the right libraries, all the compilation instructions, all the code, etc.

## Important Selection Criteria

- Requirement: Must support your programming language, but not usually a key factor once it does.
- Types of vulnerabilities it can detect (out of the [OWASP Top Ten](/www-project-top-ten/) (plus more?))
- How accurate is it? False Positive/False Negative rates? - Does the tool have an OWASP [Benchmark](/www-project-benchmark/) score?
- Does it understand the libraries/frameworks you use?
- Does it require a fully buildable set of source?
- Can it run against binaries instead of source?
- Can it be integrated into the developer's IDE?
- How hard is it to setup/use?
- Can it be run continuously and automatically?
- License cost for the tool. (Some are sold per user, per organization, per application, per line of code analyzed. Consulting licenses are frequently different than end user licenses.)

## Disclaimer

**The tools listed in the tables below are presented in alphabetical order. *OWASP does not endorse any of the vendors or tools by listing them in the table below.* We have made every effort to provide this information as accurately as possible. If you are the vendor of a tool below and think that this information is incomplete or incorrect, please send an e-mail to our mailing list and we will make every effort to correct this information.**

{% include tools.md type="SAST" %}

## More info

- [NIST's list of Source Code Security Analysis Tools](https://samate.nist.gov/index.php/Source_Code_Security_Analyzers.html).
- [DAST Tools](/www-community/Vulnerability_Scanning_Tools) - Similar info on Dynamic Application Security Testing (DAST) Tools.
- [Free for Open Source Application Security Tools](/www-community/Free_for_Open_Source_Application_Security_Tools) - This page lists the Commercial Source Code Analysis Tools (SAST) we know of that are free for Open Source.
