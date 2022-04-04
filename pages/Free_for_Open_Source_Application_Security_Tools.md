---

layout: col-sidebar
title: Free for Open Source Application Security Tools
author: Dave Wichers
contributors: 
  - Sherif Koussa
  - Dirk Wetter
  - kingthorin
tags: application security tools, tools
permalink: /Free_for_Open_Source_Application_Security_Tools

---

{% include writers.html %}

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
such tools could certainly be used. One such cloud service is:

  - [GitHub code scanning](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/about-code-scanning) - A free for open
    source static analysis service that uses [GitHub Actions](https://docs.github.com/en/actions) and [CodeQL](https://codeql.github.com/)
    to scan public repositories on GitHub.
    Supports C/C++, C\#, Ruby (beta), Java, JavaScript/TypeScript,
    Python, and Go (see [here](https://codeql.github.com/docs/codeql-overview/supported-languages-and-frameworks/) for more information)
    - If you do not want to use GitHub Actions, you may use the [CodeQL CLI](https://github.com/github/codeql-cli-binaries); however, be sure to read the license terms in full.
    - By default, CodeQL only looks for high fidelity security related results (well known true positives), so your results may look different from LGTM.
    - To achieve the same or similar results provided by LGTM, try enabling the `security-and-quality` query suite within the [CodeQL query pack](https://docs.github.com/en/code-security/code-scanning/automatically-scanning-your-code-for-vulnerabilities-and-errors/configuring-code-scanning#using-queries-in-ql-packs).
    
In addition, we are aware of the following commercial SAST tools that are free for Open Source projects:

  - [Coverity Scan Static Analysis](https://scan.coverity.com/) - Can be
    lashed into Travis-CI so it's done automatically with online
    resources. Supports over a dozen programming languages.
  - [reshift](https://www.softwaresecured.com/reshift) - A CI/CD tool
    that uses static code analysis to scan for vulnerabilities and uses
    machine learning to give a prediction on false positives. Supports
    Java with future support for NodeJS and JavaScript planned. If you 
    go to the Pricing section on this page, it says it is free for public repositories.
  - [Xanitizer](https://www.xanitizer.com/xanitizer-pricing/) - A SAST tool
    for Java, Scala, and JavaScript/TypeScript. Per this pricing page, it
    is free for Open Source projects if you contact the vendor.
  - [HCL AppScan CodeSweep](https://hclsw.co/codesweep) - This is a SAST community edition version of HCL AppScan. Free for everyone to use. The tool currently supports Python, Ruby, JS (Vue, Node, Angular, JQuery, React, etc), PHP, Perl, Go, TypeScript & more, with new languages being added frequently.
    - [CodeSweep - VS Code Plugin](https://hclsw.co/codesweep) -  Scans files upon saving them. The results show the location of a finding, type, and remediation advice. 
    - [CodeSweep - GitHub Action](https://hclsw.co/codesweepgithub) - Scan the new code on a push/pull request using a GitHub action. Findings are highlighted in the `Files Changed` view and details about the issue and mitigation steps can be found in the `Actions` page. Unrestricted usage allowed with a free trial account. 

### DAST Tools

If your project has a web application component, we recommend running
automated scans against it to look for vulnerabilities. OWASP maintains
a page of known [DAST Tools](Vulnerability_Scanning_Tools), and the
**License** column on this page indicates which of those tools have free
capabilities. Our primary recommendation is to use one of these:

  - [OWASP ZAP](/www-project-zap) - A full
    featured free and open source DAST tool that includes both automated
    scanning for vulnerabilities and tools to assist expert manual web
    app pen testing.
      - The ZAP team has also been working hard to make it easier to
        integrate ZAP into your CI/CD pipeline. (e.g., here's a [blog
        post on how to integrate ZAP with
        Jenkins](https://www.we45.com/blog/how-to-integrate-zap-into-jenkins-ci-pipeline-we45-blog)).
  - [StackHawk](https://stackhawk.com/) - StackHawk is a commercially supported DAST 
    tool built on OWASP ZAP and optimized to run in CI/CD (almost every CI supported) to test web applications during 
    development and in CI/CD. The StackHawk platform allows you to manage findings over time in 
    different environments. StackHawk is free for Open Source projects and free to use on a single application.
  - [Arachni](http://www.arachni-scanner.com/) - Arachni is a
    commercially supported scanner, but its free for most use cases,
    including scanning open source projects.
  - [VWT Digital's sec-helpers](https://github.com/vwt-digital/sec-helpers/tree/master) -
    Collection of dynamic security related helpers.
    Sec-helpers is a bundle of useful tests and validators to ensure the security of
    a given domain.
  - [OWASP purpleteam](/www-project-purpleteam) - A security regression testing SaaS and CLI,
    perfect for inserting into your build pipelines. You don't need to write any tests yourself.
    purpleteam is smart enough to know how to test,
    you just need to provide a Job file which tells purpleteam what you want tested.
    It has two main environments `local` and `cloud`.
      - `local` is OWASP - set everything up yourself in your own environment.
      - `cloud` is a proprietary offering with everything hosted for you in the cloud.
        You just need to [configure and run the CLI](https://github.com/purpleteam-labs/purpleteam).  
        
    purpleteam is pluggable, if it doesn't have a tester that you need you can add your own.
    One of the testers (the web application tester) uses OWASP ZAP under the hood.


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
    features disabled). Contrast CE supports Java and .NET only.
    
### API Web Scanners

For tools which are API specific please refer to the OWASP community [/api_security_tools](API Security Tools) page.

### Open Source Software (OSS) Security Tools

OSS refers to the open source libraries or components that application
developers leverage to quickly develop new applications and add features
to existing apps. Gartner refers to the analysis of the security of
these components as software composition analysis (SCA). So OSS Analysis
and SCA are the same thing.

OWASP recommends that all software projects generally try to keep the
libraries they use as up-to-date as possible to reduce the likelihood of
[Using Components with Known Vulnerabilities (OWASP Top 10-2017
A9)](/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A9-Using_Components_with_Known_Vulnerabilities).
There are two recommended approaches for this:

#### Keeping Your Libraries Updated

Using the latest version of each library is recommended because security
issues are frequently fixed 'silently' by the component maintainer. By
silently, we mean without publishing a [CVE](https://cve.mitre.org/) for
the security fix.

  - [Maven Versions plugin](https://www.mojohaus.org/versions-maven-plugin/)
      - For Maven projects, can be used to generate a report of all
        dependencies used and when upgrades are available for them.
        Either a direct report, or part of the overall project
        documentation using: mvn site.
  - [Dependabot](https://dependabot.com/)
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

  - OWASP has its own free open source tools:
    - [OWASP Dependency Check](/www-project-dependency-check/)
    - [OWASP Dependency Track](/www-project-dependency-track/)
  - GitHub: [Security alerts for vulnerable 
    dependencies](https://help.github.com/articles/about-security-alerts-for-vulnerable-dependencies/)
      - A native GitHub feature that reports known vulnerable
        dependencies in your GitHub projects. Supports: Java, .NET,
        JavaScript, Ruby, and Python. Your GitHub projects are
        automatically signed up for this service.
  - Debricked: free for open source projects or smaller teams.
     - Identifies, fixes and prevents known vulnerabilities. Read more at [https://debricked.com](https://debricked.com)
     - [Create a free account](https://app.debricked.com/en/register)
       

Commercial tools of this type that are free for open source:

  - Contrast Community Edition (CE) (mentioned earlier) also has both
    Known Vulnerable Component detection and Available Updates reporting
    for OSS. CE supports Java and .NET only.
  - [Debricked](https://debricked.com) - over 90% true positive rate in supported languages
     - Identifies, fixes and prevents known vulnerabilities through automation without the need
       to give access to your source code. Read more at [https://debricked.com](https://debricked.com)
     - Allows for vulnerability management and license compliance in the same tool
     - Features automated fix pull request to automatically fix vulnerabilities (currently only for javascript)
     - Features one of the most complete [vulnerability databases](https://app.debricked.com/en/vulnerability-database) 
     - GitHub version: [https://github.com/apps/debricked/](https://github.com/apps/debricked/) 
  - [Snyk](https://www.snyk.io) - Supports Node.js, Ruby, Java, Python,
    Scala, Golang, .NET, PHP - Latest list here: 
    <https://docs.snyk.io/products/snyk-open-source/language-and-package-manager-support>
      - A Commercial tool that identifies vulnerable components and
        integrates with numerous CI/CD pipelines. It is free for open
        source: <https://snyk.io/plans>
      - If you don't want to grant Snyk write access to your repo (see
        it can auto-create pull requests) you can use the Command Line
        Interface (CLI) instead. See: <https://snyk.io/docs/using-snyk>.
        If you do this and want it to be free, you have to configure
        Snyk so it knows it's open source:
        <https://support.snyk.io/hc/en-us/articles/360000910597-How-can-I-set-a-Snyk-CLI-project-as-open-source>
          - Another benefit of using the Snyk CLI is that it won't auto
            create Pull requests for you (which makes these 'issues'
            more public than you might prefer)
      - They also provide detailed information and remediation guidance
        for known vulnerabilities here: <https://snyk.io/vuln>
  - [SourceClear](https://www.veracode.com/products/software-composition-analysis)
    Now owned by Veracode. Supports: Java, Ruby, JavaScript, Python, Objective C, GO, PHP
      - They make their component vulnerability data (for publicly
        known vulns) free to search:
        <https://www.sourceclear.com/vulnerability-database/search#_>
        (Very useful when trying to research a particular library)
  - [Vulert](https://vulert.com) - Supports Node.js, Ruby, Java, Python, Scala, Golang, .Net, PHP
      - A Commercial tool that identifies vulnerable components. It is free for open
        source.
  - [WhiteSource](https://www.whitesourcesoftware.com/) - Supports 200+ programming languages.
      - Azure version:
        <https://marketplace.visualstudio.com/items?itemName=whitesource.ws-bolt>
      - GitHub version:
        <https://github.com/apps/whitesource-bolt-for-github>

### Code Quality tools

Quality has a significant correlation to security. As such, we recommend
open source projects also consider using good code quality tools. A few
that we are aware of are:

  - [SpotBugs](https://spotbugs.github.io/) - Open source code
    quality tool for Java
      - This is the active fork for FindBugs, so if you use Findbugs,
        you should switch to this.
      - SpotBugs users should add the FindSecBugs plugin
        (http://find-sec-bugs.github.io/) to their SpotBugs setup, as it
        significantly improves on the very basic security checking
        native to SpotBugs.

  - [SonarQube](https://www.sonarqube.org/)
      - This is a commercially supported, very popular, free (and
        commercial) code quality tool. It includes most if not all the
        FindSecBugs security rules plus lots more for quality, including
        a free, internet online CI setup to run it against your open
        source projects. SonarQube supports numerous languages:
        <https://www.sonarqube.org/features/multi-languages/>

  - [DeepScan](https://deepscan.io/) - Supports JavaScript, TypeScript
      - DeepScan is a static code analysis tool and hosted service for 
        inspecting JavaScript code. It checks possible run-time errors 
        and poor code quality using data-flow analysis and provides 
        results for the project's code quality.
      - DeepScan is free for open source projects on GitHub.

### Security Tools Built into DevOps/CI Environments
  - GitLab - is building security into their platform and it is quickly
    evolving as described here:
    <https://about.gitlab.com/direction/secure/#security-paradigm>
      - They are leveraging the best free open source tools they can find
        and building them into the GitLab CI pipeline to make it easy to
        enable them. [This includes many categories of security 
        tools](https://about.gitlab.com/stages-devops-lifecycle/secure/):
        - [SAST](https://docs.gitlab.com/ee/user/application_security/sast/)
        - [DAST](https://docs.gitlab.com/ee/user/application_security/dast/)
        - Code Quality
        - [Dependency Analysis](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/)
        - [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/)
      - The specific tools enabled are language specific.
      - These security features are free for public open source projects on [GitLab.com](https://gitlab.com/)

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
