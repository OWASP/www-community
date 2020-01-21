---

layout: col-sidebar
title: Free for Open Source Application Security Tools
author: 
contributors: 
tags: application security tools, tools
permalink: /Free_for_Open_Source_Application_Security_Tools
auto-migrated: 1

---


## Introduction

OWASP's mission is to help the world improve the security of its
software. One of the best ways OWASP can do that is to help Open Source
developers improve the software they are producing that everyone else
relies on. As such, the following lists of **automated vulnerability
detection tools** that are **free for open source** projects have been
gathered together here to raise awareness of their availability.

We would encourage open source projects to use the following types of
tools to improve the security and quality of their code:

  - Static Application Security Testing ([SAST](Source_Code_Analysis_Tools)) Tools
  - Dynamic Application Security Testing ([DAST](Vulnerability_Scanning_Tools)) Tools
    - (Primarily for web apps)
  - Interactive Application Security Testing (IAST) Tools - (Primarily
    for web apps and web APIs)
  - Keeping Open Source libraries up-to-date (to avoid [Using Components
    with Known Vulnerabilities (OWASP Top 10-2017
    A9)](/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities))
  - Static Code Quality Tools


**Disclaimer:** <b>OWASP does not endorse any of the Vendors or Scanning
Tools by listing them below. They are simply listed if we believe they
are free for use by open source projects. We have made every effort to
provide this information as accurately as possible. If you are the
vendor of a free for open source tool and think this information is
incomplete or incorrect, please send an e-mail to dave.wichers (at)
owasp.org and we will make every effort to correct this information.</b>

## Free for Open Source Tools

Tools that are free for open source projects in each of the above
categories are listed below.

### SAST Tools

OWASP already maintains a page of known SAST tools: [Source Code
Analysis Tools](Source_Code_Analysis_Tools), which includes a
list of those that are "Open Source or Free Tools Of This Type". Any
such tools could certainly be used. One such cloud service that looks
promising is:

  - [LGTM.com](https://lgtm.com/help/lgtm/about-lgtm) - A free for open
    source static analysis service that automatically monitors commits
    to publicly accessible code in: Bitbucket Cloud, GitHub, or GitLab.
    Supports C/C++, C\#, COBOL (in beta), Java, JavaScript/TypeScript,
    Python

In addition, we are aware of the following commercial SAST tools that
are free for Open Source projects:

  - [Coverity Scan Static Analysis](https://scan.coverity.com/) - Can be
    lashed into Travis-CI so it's done automatically with online
    resources. Supports over a dozen programming languages as documented
    here in the section [Comprehensive support for these programming
    languages and
    frameworks](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html).
  - [reshift](https://www.softwaresecured.com/reshift) - A CI/CD tool
    that uses static code analysis to scan for vulnerabilities and uses
    machine learning to give a prediction on false positives. Supports
    Java with future support for NodeJS and JavaScript planned for
    sometime in 2019. If you go to the Pricing section on this page, it
    says it is free for public repositories.

### DAST Tools

If your project has a web application component, we recommend running
automated scans against it to look for vulnerabilities. OWASP maintains
a page of known DAST Tools: [Vulnerability Scanning
Tools](Vulnerability_Scanning_Tools), and the
**Licence** column on this page indicates which of those tools have free
capabilities. Our primary recommendation is to use one of these:

  - [OWASP ZAP](OWASP_Zed_Attack_Proxy_Project "wikilink") - A full
    featured free and open source DAST tool that includes both automated
    scanning for vulnerabilities and tools to assist expert manual web
    app pen testing.
      - The ZAP team has also been working hard to make it easier to
        integrate ZAP into your CI/CD pipeline. (e.g., here's a [blog
        post on how to integrate ZAP with
        Jenkins](https://www.we45.com/blog/how-to-integrate-zap-into-jenkins-ci-pipeline-we45-blog)).
  - [Arachni](http://www.arachni-scanner.com/) - Arachni is a
    commercially supported scanner, but its free for most use cases,
    including scanning open source projects.

We are not aware of any other commercial grade tools that offer their
full featured DAST product free for open source projects.

### IAST Tools

IAST tools are typically geared to analyze Web Applications and Web
APIs, but that is vendor specific. There may be IAST products that can
perform good security analysis on non-web applications as well.

We are aware of only one IAST Tool that is free after registration at
this time:

  - [Contrast Community Edition
    (CE)](https://www.contrastsecurity.com/contrast-community-edition) -
    Fully featured version for 1 app and up to 5 users (some Enterprise
    features disabled). Contrast CE supports Java only.

### Open Source Software (OSS) Security Tools

OSS refers to the open source libraries or components that application
developers leverage to quickly develop new applications and add features
to existing apps. Gartner refers to the analysis of the security of
these components as software composition analysis (SCA). So OSS Analysis
and SCA are the same thing.

OWASP recommends that all software projects generally try to keep the
libraries they use as up-to-date as possible to reduce the likelihood of
[Using Components with Known Vulnerabilities (OWASP Top 10-2017
A9)](Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities "wikilink").
There are two recommended approaches for this:

#### Keeping Your Libraries Updated

Using the latest version of each library is recommended because security
issues are frequently fixed 'silently' by the component maintainer. By
silently, we mean without publishing a [CVE](https://cve.mitre.org/) for
the security fix.

  - [Maven Versions
    plugin](https://www.mojohaus.org/versions-maven-plugin/)
      - For Maven projects, can be used to generate a report of all
        dependencies used and when upgrades are available for them.
        Either a direct report, or part of the overall project
        documentation using: mvn site.
  - Dependabot - <https://dependabot.com/>
      - A GitHub only service that creates pull requests to keep your
        dependencies up-to-date. It automatically generates a pull
        request for each dependency you can upgrade, which you can then
        ignore, or accept, as you like. It supports tons of languages.
      - Recommended for all open source projects maintained on GitHub\!

#### Detecting Known Vulnerable Components

As an alternative, or in addition to, trying to keep all your components
up-to-date, a project can specifically monitor whether any of the
components they use have known vulnerable components.

Free tools of this type:

  - OWASP has its own free open source tool [OWASP Dependency
    Check](OWASP_Dependency_Check "wikilink") that is free for anyone to
    use.
  - GitHub: Security alerts for vulnerable dependencies -
    <https://help.github.com/articles/about-security-alerts-for-vulnerable-dependencies/>
      - A native GitHub feature that reports known vulnerable
        dependencies in your GitHub projects. Supports: Java, .NET,
        JavaScript, Ruby, and Python. Your GitHub projects are
        automatically signed up for this service.

Commercial tools of this type that are free for open source:

  - Contrast Community Edition (CE) (mentioned earlier) also has both
    Known Vulnerable Component detection and Available Updates reporting
    for OSS. CE supports Java only.
  - Snyk - <https://www.snyk.io> - Supports Node.js, Ruby, Java, Python,
    Scala, Golang, .NET, PHP - Latest list here: <https://snyk.io/docs>
      - A Commercial tool that identifies vulnerable components and
        integrates with numerous CI/CD pipelines. It is free for open
        source: <https://snyk.io/plans>
      - If you don't want to grant Snyk write access to your repo (see
        it can auto-create pull requests) you can use the Command Line
        Interface (CLI) instead. See: <https://snyk.io/docs/using-snyk>.
        If you do this and want it to be free, you have to configure
        Snyk so it know its open source:
        <https://support.snyk.io/snyk-cli/how-can-i-set-a-snyk-cli-project-as-open-source>
          - Another benefit of using the Snyk CLI is that it won't auto
            create Pull requests for you (which makes these 'issues'
            more public than you might prefer)
      - They also provide detailed information and remediation guidance
        for known vulnerabilities here: <https://snyk.io/vuln>
  - SourceClear - <https://www.sourceclear.com/> - Supports: Java, Ruby,
    JavaScript, Python, Objective C, GO, PHP
      - They have a free trial right from their [home
        page](https://www.sourceclear.com/). When the 30 day trial
        expires, it converts into a free "Personal Account" per:
        "Upgrade at any time to get the features that matter most to
        you, or choose the Personal plan when your trial ends." Personal
        Account described here: <https://www.sourceclear.com/pricing/>
      - They also make their component vulnerability data (for publicly
        known vulns) free to search:
        <https://www.sourceclear.com/vulnerability-database/search#_>
        (Very useful when trying to research a particular library)
  - WhiteSource Bolt - Supports 200+ programming languages.
    <https://www.whitesourcesoftware.com/>
      - Azure version:
        <https://marketplace.visualstudio.com/items?itemName=whitesource.ws-bolt>
      - GitHub version:
        <https://github.com/apps/whitesource-bolt-for-github> Available
        starting in Nov. 2018.

### Code Quality tools

Quality has a significant correlation to security. As such, we recommend
open source projects also consider using good code quality tools. A few
that we are aware of are:

  - SpotBugs (https://github.com/spotbugs/spotbugs) - Open source code
    quality tool for Java
      - This is the active fork for FindBugs, so if you use Findbugs,
        you should switch to this.
      - SpotBugs users should add the FindSecBugs plugin
        (http://find-sec-bugs.github.io/) to their SpotBugs setup, as it
        significantly improves on the very basic security checking
        native to SpotBugs.

<!-- end list -->

  - SonarQube (https://www.sonarqube.org/)
      - This is a commercially supported, very popular, free (and
        commercial) code quality tool. It includes most if not all the
        FindSecBugs security rules plus lots more for quality, including
        a free, internet online CI setup to run it against your open
        source projects. SonarQube supports numerous languages:
        <https://www.sonarqube.org/features/multi-languages/>

Please let us know if you are aware of any other high quality
application security tools that are free for open source (or simply add
them to this page). We are particularly interested in identifying and
listing commercial tools that are free for open source, as they tend to
be better and easier to use than open source (free) tools. If you are
aware of any missing from this list, please add them, or let us know
(dave.wichers (at) owasp.org) and we'll confirm they are free, and add
them for you. Please encourage your favorite commercial tool vendor to
make their tool free for open source projects as well\!\!

Finally, please forward this page to the open source projects you rely
on and encourage them to use these free tools\!