---

layout: col-sidebar
title: Free for Open Source Application Security Tools
author: Dave Wichers
contributors: 
  - Sherif Koussa
  - Dirk Wetter
  - kingthorin
  - Niclas Gustafsson
  - Jason Hills
  - Thomas Rooijakkers
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
  - Automatic Remediation Tools

**Disclaimer:** <b>OWASP does not endorse any of the Vendors or Scanning
Tools by listing them below. They are simply listed if we believe they
are free for use by open source projects. We have made every effort to
provide this information as accurately as possible. If you are the
vendor of a free for open source tool and think this information is
incomplete or incorrect, please send an e-mail to dave.wichers (at)
owasp.org and we will make every effort to correct this information.</b>

## Free for Open Source Tools

Tools that are free for open source projects in each of the above categories are listed below.

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

  - [Contrast CodeSec - Scan & Serverless](https://www.contrastsecurity.com/developer/codesec/) - Web App and API code scanners via command line or through GitHub actions. CodeSec - Scan supports Java, JavaScript and .NET, while CodeSec - Serverless supports AWS Lambda Functions (Java + Python). These tools are actually free for all projects, not just open source.
  - [Coverity Scan Static Analysis](https://scan.coverity.com/) - Can be lashed into Travis-CI so it's done automatically with online resources. Supports over a dozen programming languages.
  - [HCL AppScan CodeSweep](https://hclsw.co/codesweep) - This is a SAST community edition version of HCL AppScan. Free for everyone to use. The tool currently supports Python, Ruby, JS (Vue, Node, Angular, JQuery, React, etc), PHP, Perl, Go, TypeScript & more, with new languages being added frequently.
    - [CodeSweep - VS Code Plugin](https://hclsw.co/codesweep) -  Scans files upon saving them. The results show the location of a finding, type, and remediation advice. Auto-fix available with free trial or subscription.
    - [CodeSweep - JetBrains Plugin](https://hclsw.co/codesweep-jetbrains) -  Scans files upon saving them. The results show the location of a finding, type, and remediation advice. Auto-fix available with free trial or subscription.
    - [CodeSweep - GitHub Action](https://hclsw.co/codesweepgithub) - Scan the new code on a push/pull request using a GitHub action. Findings are highlighted in the `Files Changed` view and details about the issue and mitigation steps can be found in the `Actions` page. Unrestricted usage allowed with a free trial account.
  - [Aikido](https://www.aikido.dev/product) - Combines open source software with custom rules & features into a single dashboard with all your security findings. Includes both SAST and Library Analysis tools. [Free for small teams](https://www.aikido.dev/pricing).
  - [AppSweep](https://www.guardsquare.com/appsweep-mobile-application-security-testing) - a free for everyone mobile application security testing tool for Android and iOS. It analyzes the compiled application and does not require access to the source code. The tool performs security assessment not only of the executable code but also of application resources and configuration file. Integration into CI/CD is supported.
  - [Arnica](https://www.arnica.io/solution/code-security) - Scans all source code repositories for code risks (SAST, SCA, IaC, license violations, and low 3rd party reputation) and hardcoded secrets. The platform comes with a [freemium plan](https://www.arnica.io/pricing) for unlimited time and users count. The [pipelineless security approach](https://www.arnica.io/blog/ci-cd-pipeline-security-vs-ide-plugins-vs-pipelineless-security) is the value the company charges for, so the visibility remains always free.

### DAST Tools

If your project has a web application component, we recommend running
automated scans against it to look for vulnerabilities. OWASP maintains
a page of known [DAST Tools](Vulnerability_Scanning_Tools), and the
**License** column on this page indicates which of those tools have free
capabilities. Our primary recommendation is to use one of these:

  - [ZAP](https://www.zaproxy.org/) - A full
    featured free and open source DAST tool that includes both automated
    scanning for vulnerabilities and tools to assist expert manual web app pen testing.
  - [OWASP PurpleTeam](/www-project-purpleteam) - A security regression testing SaaS and CLI,
    perfect for inserting into your build pipelines. You don't need to write any tests yourself.
    PurpleTeam is smart enough to know how to test, you just need to provide a Job file which tells PurpleTeam what you want tested.
    It has two main environments `local` and `cloud`.
      - `local` is OWASP - set everything up yourself in your own environment.
      - `cloud` is a proprietary offering with everything hosted for you in the cloud.
        You just need to [configure and run the CLI](https://github.com/purpleteam-labs/purpleteam).  
    PurpleTeam is pluggable, if it doesn't have a tester that you need you can add your own.
    One of the testers (the web application tester) uses ZAP under the hood.
  - [Akto](https://www.akto.io/) - Akto is an open-source and commercial DAST and API Security tool that includes both automated API Discovery and
    scanning of vulnerabilities in CI/CD with the highest test coverage.
  - [Arachni](http://www.arachni-scanner.com/) - Arachni is a commercially supported scanner, but its free for most use cases, including scanning open source projects.
  - [CI Fuzz CLI](https://www.code-intelligence.com/cli-tool) - An open source command line tool for creating fuzz tests. The tool is tightly integrated with various build systems, enabling developers to create fuzz tests as easily as unit tests.
  - [Code Intelligence App](https://www.code-intelligence.com/guided-product-tour) - This application security testing platform enables CI/CD-integrated fuzz testing at each pull request. It helps developers to measure and maximize code coverage and to prioritize all findings based on severity. All of this information is then aggregated in a usable dashboard. The testing platform integrates directly into popular ticketing systems and issue trackers.
  - [StackHawk](https://stackhawk.com/) - StackHawk is a commercially supported DAST
    tool built on ZAP and optimized to run in CI/CD (almost every CI supported) to test web applications during
    development and in CI/CD. The StackHawk platform allows you to manage findings over time in
    different environments. StackHawk is free for Open Source projects and free to use on a single application.
  - [VWT Digital's sec-helpers](https://github.com/vwt-digital/sec-helpers/tree/master) -
    Collection of dynamic security related helpers.
    Sec-helpers is a bundle of useful tests and validators to ensure the security of a given domain.
  - [WuppieFuzz](https://github.com/TNO-S3/WuppieFuzz) is a coverage-guided REST API fuzzer developed on top of LibAFL, targeting a wide audience of end-users, with a strong focus on ease-of-use, explainability of the discovered flaws and modularity. WuppieFuzz supports all three settings of testing (black box, grey box and white box).

We are not aware of any other commercial grade tools that offer their
full featured DAST product free for open source projects.

### IAST Tools

IAST tools are typically geared to analyze Web Applications and Web
APIs, but that is vendor specific. There may be IAST products that can
perform good security analysis on non-web applications as well.

We are aware of only one IAST Tool that is free after registration at this time:

  - [Contrast Community Edition
    (CE)](https://www.contrastsecurity.com/contrast-community-edition) -
    Fully featured version for 1 app and up to 5 users (some Enterprise
    features disabled). Contrast CE supports Java and .NET only.
    
### API Web Scanners

For tools which are API specific please refer to the OWASP community [API Security Tools](api_security_tools) page.

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
silently, we mean without publishing a [CVE](https://cve.mitre.org/) for the security fix.

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
  - [Bytesafe Dependency Firewall](https://bytesafe.dev/): Free for Open Source projects 
    - Detects known vulnerabilities in source code dependencies, 
    - Blocks dependencies based on policies such as vulnerabilities, type of license, release dates and more
  - Debricked: free for open source projects or smaller teams.
     - Identifies, fixes and prevents known vulnerabilities. Read more at [https://debricked.com](https://debricked.com)
     - [Create a free account](https://app.debricked.com/en/register)
   - [retire.js](https://github.com/RetireJS/retire.js): free open source tool for finding javascript libraries with known vulnerabilities. Originally a command line tool, and there are plugins for browsers and scanners.


Commercial tools of this type that are free for open source:

  - [Aikido](https://www.aikido.dev/product) - Combines open source software with custom rules & features into a single dashboard with all your security findings. Includes both Library Analysis and SAST tools. [Free for small teams](https://www.aikido.dev/pricing).
  - [Bytesafe](https://bytesafe.dev/) - Bytesafe Dependency Firewall manages source code dependencies securely
    - Detects Known Vulnerabilities in dependencies
    - [Identifies OSS licenses](https://bytesafe.dev/compliance/) used in dependencies and prevents use of problematic licenses.
    - Provides [SCA capabilities](https://bytesafe.dev/software-composition-analysis/) such as SBOM creation
    - Free for Open Source Projects and [individual users](https://bytesafe.dev/pricing/)
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
  - [OX Security](https://www.ox.security) - Stop Attacks Across Your Software Supply Chain
     - Complete Software Supply Chain Security Solution, based on [Pipeline Bill Of Materials](https://www.pbom.dev/)
     - Manage your findings from a single location
       - Full visibility and end to end traceability over your software pipeline security from cloud to code.
       - Manage your findings, orchestrate DevSecOps activities, prevent risks and maintain software pipeline integrity 
     - Automatically block risks introduced into the pipeline and ensure the integrity of each workload
     - Close Gaps in Security Tooling & Coverage
       - Avoid known security risks like Log4j and Codecov.
       - Prevent new attack types based on proprietary research and threat intel.
     - Improve CI/CD Security & Processes
        - Ensure the security and integrity of all cloud artifacts
        - Undertake security gap analysis and identify any blind spots.
     - Free tier for Open-Source projects
  - [SOOS](https://soos.io) - [Free Community Edition](https://app.soos.io/register?registrationType=community) - Our no-hassle enrollment process for open source projects brings practical supply chain security to the masses.
     - Use with any public GitHub repository
     - C++, Node, Ruby, Python, Java, .Net, and more
     - Integrates with GitHub
     - Connect to Jira, Azure DevOps, or GitHub Issues
     - Robust license policies
     - Rich vulnerability dashboard
     - SBOM generation (SPDX/CycloneDX)
  - [Snyk](https://www.snyk.io) - Supports Node.js, Ruby, Java, Python,
    Scala, Golang, .NET, PHP - Latest list here: 
    <https://docs.snyk.io/products/snyk-open-source/language-and-package-manager-support>
      - A Commercial tool that identifies vulnerable components and
        integrates with numerous CI/CD pipelines. Free for open
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
  - [Software Health Indicator](https://software-health-indicator.com) by YourSky.blue
    - The real time indicator that promotes supply chain transparency
      Free for FOSS projects: <https://software-health-indicator.com/order/>
  - [SourceClear](https://www.veracode.com/products/software-composition-analysis)
    Now owned by Veracode. Supports: Java, Ruby, JavaScript, Python, Objective C, GO, PHP
      - They make their component vulnerability data (for publicly known vulns) free to search:
        <https://www.sourceclear.com/vulnerability-database/search#_>
        (Very useful when trying to research a particular library)
  - [Vulert](https://vulert.com) - Vulert's Software Composition Analysis (SCA) keeps an eye on the open source dependencies for new risks (vulnerabilities), recommends fixes, and ensures license compliance – all without requiring installation or access to the codebase. Supports Node.js, Ruby, Java, Python, Scala, Golang, .Net, PHP, C/C++ and many more.
      - At Vulert Playground, one can test an app's security without any sign-ups. Visit [Vulert Playground](https://vulert.com/abom)
      - Free for open source and small companies.
  - [WhiteSource](https://www.whitesourcesoftware.com/) - Supports 200+ programming languages.
      - Azure version:
        <https://marketplace.visualstudio.com/items?itemName=whitesource.ws-bolt>
      - GitHub version: <https://github.com/marketplace/whitesource-bolt>
  - [Arnica](https://www.arnica.io/solution/code-security) - Provides full visibility for code risks (SAST, SCA, IaC, license violations, and low 3rd party reputation) and hardcoded secrets across all source code repositories.
      - The platform comes with a [freemium plan](https://www.arnica.io/pricing) for unlimited time and users count.The [pipelineless security approach](https://www.arnica.io/blog/ci-cd-pipeline-security-vs-ide-plugins-vs-pipelineless-security) is the value the company charges for, so the visibility remains always free.
      - [SBOMs]([https://www.arnica.io/solution/sbom](https://docs.arnica.io/arnica-documentation/inventory/software-bill-of-materials-sbom)) are generated and automatically updated across all source code repositories.
      - [Supported languages](https://docs.arnica.io/arnica-documentation/code-risks/software-composition-analysis-sca): .Net, C, C++, L, Go, Java, JavaScript (including various frameworks), PHP, Python, Ruby, Rust, Scala, Swift.
      - Simplifies the risk prioritization by automatically classifying the business important of each product and correlating the potential exploitability with open source threat feeds (e.g. EPSS).

### Code Quality tools

Quality has a significant correlation to security. As such, we recommend
open source projects also consider using good code quality tools. A few that we are aware of are:

  - [SpotBugs](https://spotbugs.github.io/) - Open source code quality tool for Java
      - This is the active fork for FindBugs, so if you use Findbugs, you should switch to this.
      - SpotBugs users should add the [FindSecBugs plugin](https://find-sec-bugs.github.io/) to their SpotBugs setup, as it
        significantly improves on the very basic security checking native to SpotBugs.
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
   - [MegaLinter](https://www.megalinter.io) - Multi-language Code Quality and Security checker
      - MegaLinter is an Open-Source tool that analyzes the
        consistency of your code, IAC, configuration, and scripts in your repository
        sources, to ensure all your projects repositories are clean and formatted whatever
        IDE/toolbox is used by their developers
      - [More than 100 linters](https://megalinter.io/latest/supported-linters/) supporting 52
        languages, 24 formats, 21 tooling formats, spelling and security
      - Ready to use out of the box, compliant with GitHub Actions, GitLab CI, Azure Pipelines,
        Jenkins, Concourse, Drone CI, or even locally with
        [mega-linter-runner](https://megalinter.io/latest/mega-linter-runner/)
      - Highly configurable, without registration
      - 100% Open-Source and free for all uses, powered and backed by by [OX Security](https://www.ox.security/)

### Defense Tools
  - [AWS Firewall Factory](https://github.com/globaldatanet/aws-firewall-factory) - An open source solution that makes it easy to deploy, update, and provision OWASP TOP 10 compliant web application firewalls (WAFs) at scale while centrally managing them with AWS Firewall Manager. This solution streamlines security management by enabling customisation of WAF configurations and adherence to AWS best practices.

### Security Tools Built into DevOps/CI Environments
  - GitLab - is building security into their platform and it is quickly evolving [as described here](https://about.gitlab.com/direction/secure/#security-paradigm).
      - They are leveraging the best free open source tools they can find
        and building them into the GitLab CI pipeline to make it easy to
        enable them. [This includes many categories of security tools](https://about.gitlab.com/stages-devops-lifecycle/secure/):
        - [SAST](https://docs.gitlab.com/ee/user/application_security/sast/)
        - [DAST](https://docs.gitlab.com/ee/user/application_security/dast/)
        - Code Quality
        - [Dependency Analysis](https://docs.gitlab.com/ee/user/application_security/dependency_scanning/)
        - [Container Scanning](https://docs.gitlab.com/ee/user/application_security/container_scanning/)
      - The specific tools enabled are language specific.
      - These security features are free for public open source projects on [GitLab.com](https://gitlab.com/)
  - [Faraday](https://www.faradaysec.com/) - Open Source Vulnerability Manager
      - Security has two difficult tasks: designing smart ways of getting new information, and keeping track of findings to improve remediation efforts. With Faraday, you may focus on discovering vulnerabilities while we help you with the rest. Just use it in your terminal and get your work organized on the run. Faraday was made to let you take advantage of the available tools in the community in a truly multiuser way.
      - Community Version: public open source projects on [GitHub](https://github.com/infobyte/faraday)

### Secrets Detection Tools

Secrets detection is often confused with SAST because both scan through static source code. Secrets detection scan the default branch before deployment but can also scan through every single commit of the git history, covering every branch, even development or test ones.

  - [GitGuardian](https://gitguardian.com/) 
    - A commercial tool that scans your Git repositories’ history and monitors new contributions in real-time for secrets. It examines secret exposure trends over time and monitors team performance.
      [Free for open source repositories hosted under your GitHub Organization](https://www.gitguardian.com/pricing)
    - [Container Scanning](https://www.gitguardian.com/ggshield) ggshield is a command-line interface application to help developers detect and prevent vulnerabilities like hard coded secrets (like API keys, certificates, database connection URLs) before pushing their code to shared repositories. ggshield is integrated with GitGuardian Internal Monitoring, the automated secrets detection and remediation platform. Recently, ggshield has also integrated the capability of scanning Terraform files for infrastructure-as-code for security misconfigurations (public beta).
  - [Gitleaks](https://github.com/zricethezav/gitleaks) - Gitleaks is a fast, light-weight, portable, and open-source secret scanner for git repositories, files, and directories
    - All code is open-source (gitleaks) or source-available (Gitleaks-Action).
    - [Over 140 secret types with new types being added all the time](https://github.com/zricethezav/gitleaks/tree/master/cmd/generate/config/rules)
  - [SAP/Credential Digger](https://github.com/SAP/credential-digger) - Open Source
    - A GitHub scanning tool that identifies hardcoded credentials (Passwords, API Keys, Secret Keys, Tokens, personal information, etc.), filtering the false positive data through machine learning models.
  - [TruffleHog](https://github.com/trufflesecurity/trufflehog) - Open Source (supported by an enterprise product: [Truffle Security](https://trufflesecurity.com))
    - Find credentials in repositories (git, GitHub, GitLab), filesystem, S3 buckets, GCS buckets, syslog, CircleCI, Docket Images
    - Eliminates false positives using 700+ credential detectors that support active verification against their respective APIs
    - Available as a [GitHub Action](https://github.com/marketplace/actions/trufflehog-oss)
  - [Yelp/detect-secrets](https://github.com/Yelp/detect-secrets) - Open Source
    - detect-secrets is an aptly named module for detecting secrets within a code base. Unlike other similar packages that solely focus on finding secrets, this package is designed with the enterprise client in mind: providing a backwards compatible means to prevent new secrets from entering the code base.
  - [Arnica](https://www.arnica.io/solution/secrets) - provides full visibility for code risks (SAST, SCA, IaC, license violations, and low 3rd party reputation) and hardcoded secrets across all source code repositories.
      - The platform comes with a [freemium plan](https://www.arnica.io/pricing) for unlimited time and users count.The [pipelineless security approach](https://www.arnica.io/blog/ci-cd-pipeline-security-vs-ide-plugins-vs-pipelineless-security) is the value the company charges for, so the visibility remains always free.
      - Hardcoded [secrets validation](https://docs.arnica.io/arnica-documentation/hardcoded-secrets/secret-detection) and [custom regex](https://docs.arnica.io/arnica-documentation/hardcoded-secrets/secrets-policy-settings#custom-secrets) configuration are built in.
      - [Secrets mitigation](https://docs.arnica.io/arnica-documentation/hardcoded-secrets/realtime-secret-mitigation) is provided with a developer experience focus.
   
### Privacy Engineering Tools

- [xCOMPASS](https://github.com/Comcast/xCOMPASS/) - a simple tool that allows developers to determine their privacy engineering requirements early in the product development lifecycle. xCOMPASS has also been listed by [NIST in their Privacy Engineering Program Collaboration Space as one of four Risk Assessment Tools](https://www.nist.gov/itl/applied-cybersecurity/privacy-engineering/collaboration-space/privacy-risk-assessment/tools) and [CISA as one of the open-source tools that promote cybersecurity best practices](https://www.cisa.gov/resources-tools/services/xcompass).

### Intel and Repository Analysis Tools

- [Gitxray](https://github.com/kulkansecurity/gitxray/) - Gitxray (short for Git X-Ray) is an opensource tool designed for use on GitHub repositories. It leverages public GitHub REST APIs to gather information on Contributors and Repositories that would otherwise be very time-consuming to obtain manually. It can identify fake or shared contributor accounts, collect sensitive information in contributor profiles by looking in unconventional places (e.g. by parsing GPG key blobs), flag dangerous repository activity, and a lot more available in [its documentation](https://www.gitxray.com).

### Automatic Remediation Tools

- [Mobb](https://mobb.ai/) - Mobb is an automatic code fixer for security issues. It runs manually or as part of a pipeline, digests your SAST reports, and generates ready-to-be-merged pull requests that fix your issues.


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
