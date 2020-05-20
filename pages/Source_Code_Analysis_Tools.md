---

layout: col-sidebar
title: Source Code Analysis Tools
author: 
contributors: 
tags: source code analysis, static code analysis, tools
permalink: /Source_Code_Analysis_Tools
auto-migrated: 1

---

{% include writers.html %}

[Source code analysis](Static_Code_Analysis) tools, also
referred to as Static Application Security Testing (SAST) Tools, are
designed to analyze source code and/or compiled versions of code to help
find security flaws.

Some tools are starting to move into the IDE. For the types of problems
that can be detected during the software development phase itself, this
is a powerful phase within the development life cycle to employ such
tools, as it provides immediate feedback to the developer on issues they
might be introducing into the code during code development itself. This
immediate feedback is very useful, especially when compared to finding
vulnerabilities much later in the development cycle.

## Strengths and Weaknesses

### Strengths

  - Scales well -- can be run on lots of software, and can be run
    repeatedly (as with nightly builds or continuous integration)
  - Useful for things that such tools can automatically find with high
    confidence, such as buffer overflows, SQL Injection Flaws, and so
    forth
  - Output is good for developers -- highlights the precise source
    files, line numbers, and even subsections of lines that are affected

### Weaknesses

  - Many types of security vulnerabilities are difficult to find
    automatically, such as authentication problems, access control
    issues, insecure use of cryptography, etc. The current state of the
    art only allows such tools to automatically find a relatively small
    percentage of application security flaws. However, tools of this
    type are getting better.
  - High numbers of false positives.
  - Frequently can't find configuration issues, since they are not
    represented in the code.
  - Difficult to 'prove' that an identified security issue is an actual
    vulnerability.
  - Many of these tools have difficulty analyzing code that can't be
    compiled. Analysts frequently can't compile code because they don't
    have the right libraries, all the compilation instructions, all the
    code, etc.

## Important Selection Criteria

  - Requirement: Must support your programming language, but not usually
    a key factor once it does.
  - Types of vulnerabilities it can detect (out of the [OWASP Top Ten](http://owasp.org/www-project-top-ten/) (plus more?)
  - How accurate is it? False Positive/False Negative rates?
      - Does the tool have an OWASP [Benchmark](http://owasp.org/www-project-benchmark/)
        score?
  - Does it understand the libraries/frameworks you use?
  - Does it require a fully buildable set of source?
  - Can it run against binaries instead of source?
  - Can it be integrated into the developer's IDE?
  - How hard is it to setup/use?
  - Can it be run continuously and automatically?
  - License cost for the tool. (Some are sold per user, per org, per
    app, per line of code analyzed. Consulting licenses are frequently
    different than end user licenses.)

## OWASP Tools Of This Type

  - [OWASP SonarQube Project](https://github.com/OWASP/sonarqube)
  - [OWASP Orizon Project](http://www.owasp.org/index.php/Category:OWASP_Orizon_Project)
  - [OWASP LAPSE Project](https://github.com/OWASP/lapse-plus)
  - [OWASP O2 Platform](http://owasp.org/www-project-o2-platform/)

## Disclaimer

Disclaimer: <b>The tools listed in the tables below are presented in
alphabetical order. <i>OWASP does not endorse any of the vendors or
tools by listing them in the table below.</i> We have made every effort
to provide this information as accurately as possible. If you are the
vendor of a tool below and think that this information is incomplete or
incorrect, please send an e-mail to our mailing list and we will make
every effort to correct this information.</b>

## Open Source or Free Tools Of This Type

  - [Bandit](https://wiki.openstack.org/wiki/Security/Projects/Bandit) -
    bandit is a comprehensive source vulnerability scanner for Python
  - [Brakeman](http://brakemanscanner.org/) - Brakeman is an open source
    vulnerability scanner specifically designed for Ruby on Rails
    applications
  - [Codesake Dawn](http://rubygems.org/gems/codesake-dawn) - Codesake
    Dawn is an open source security source code analyzer designed for
    Sinatra, Padrino for Ruby on Rails applications. It also works on
    non-web applications written in Ruby
  - [Deep Dive](https://discotek.ca/deepdive.xhtml) - Byte code analysis
    tool for discovering vulnerabilities in Java deployments (Ear, War,
    Jar).
  - [FindBugs](http://findbugs.sourceforge.net/) - (Legacy - NOT
    Maintained - Use SpotBugs (see below) instead) - Find bugs
    (including a few security flaws) in Java programs
  - [FindSecBugs](https://find-sec-bugs.github.io/) - A security
    specific plugin for SpotBugs that significantly improves SpotBugs's
    ability to find security vulnerabilities in Java programs. Works
    with the old FindBugs too,
  - [Flawfinder](http://www.dwheeler.com/flawfinder/) Flawfinder - Scans
    C and C++
  - [GolangCI-Lint](https://github.com/golangci/golangci-lint) - A Go
    Linters aggregator - One of the Linters is [gosec (Go
    Security)](https://github.com/securego/gosec), which is off by
    default but can easily be enabled.
  - [Google
    CodeSearchDiggity](https://www.bishopfox.com/resources/tools/google-hacking-diggity/attack-tools/)
    - Uses Google Code Search to identifies vulnerabilities in open
    source code projects hosted by Google Code, MS CodePlex,
    SourceForge, Github, and more. The tool comes with over 130 default
    searches that identify SQL injection, cross-site scripting (XSS),
    insecure remote and local file includes, hard-coded passwords, and
    much more. *Essentially, Google CodeSearchDiggity provides a source
    code security analysis of nearly every single open source code
    project in existence – simultaneously.*
  - [Graudit](https://github.com/wireghoul/graudit/) - Scans multiple
    languages for various security flaws.
  - [HCL AppScan CodeSweep](https://hclsw.co/codesweep) - This is the 
    first Community edition version of AppScan. It is delivered as a VS 
    Code plugin and scans files upon saving them. The results show the 
    location of a finding, type and remediation advice. The tool currently 
    supports Python, Ruby, JS (Node, Angular, JQuery, etc) , PHP, Perl, 
    COBOL, APEX & a few more. 
  - [Insider CLI](https://github.com/insidersec/insider) - A open source Static Application Security Testing tool (SAST)     written in GoLang for Java (Maven and Android), Kotlin (Android), Swift (iOS), .NET Full Framework, C# and Javascript (Node.js).
  - [LGTM](https://lgtm.com/help/lgtm/about-lgtm) - A free for open
    source static analysis service that automatically monitors commits
    to publicly accessible code in: Bitbucket Cloud, GitHub, or GitLab.
    Supports C/C++, C\#, COBOL (in beta), Java, JavaScript/TypeScript,
    Python
  - [.NET Security Guard](https://dotnet-security-guard.github.io/) -
    Roslyn analyzers that aim to help security audits on .NET
    applications. It will find SQL injections, LDAP injections, XXE,
    cryptography weakness, XSS and more.
  - [phpcs-security-audit](https://github.com/FloeDesignTechnologies/phpcs-security-audit)
    - phpcs-security-audit is a set of PHP_CodeSniffer rules that finds
    flaws or weaknesses related to security in PHP and its popular CMS
    or frameworks. It currently has core PHP rules as well as Drupal 7
    specific rules.
  - [PMD](http://pmd.sourceforge.net/) - PMD scans Java source code and
    looks for potential code problems (this is a code quality tool that
    does not focus on security issues)
  - [PreFast](http://msdn.microsoft.com/en-us/library/ms933794.aspx)
    (Microsoft) - PREfast is a static analysis tool that identifies
    defects in C/C++ programs. Last update 2006.
  - [Progpilot](https://github.com/designsecurity/progpilot) - Progpilot
    is a static analyzer tool for PHP that detects security
    vulnerabilities such as XSS and SQL Injection.
  - [Puma Scan](https://pumascan.com/) - Puma Scan is a .NET C\# open
    source static source code analyzer that runs as an IDE plugin for
    Visual Studio and via MSBuild in CI pipelines.
  - [Pyre](https://pyre-check.org/) - A performant type-checker for
    Python 3, that also has [limited security/data flow
    analysis](https://pyre-check.org/docs/static-analysis.html)
    capabilities.
  - [RIPS](http://rips-scanner.sourceforge.net/) - RIPS Open Source is a
    static source code analyzer for vulnerabilities in PHP web
    applications. Please see notes on the sourceforge.net site.
  - [ShiftLeft Scan](https://github.com/ShiftLeftSecurity/sast-scan) - Scan is a free open-source DevSecOps platform for detecting security issues in source code and dependencies. It supports a broad range of languages and CI/CD pipelines.
  - [Sink Tank](https://discotek.ca/sinktank.xhtml) - Byte code static
    code analyzer for performing source/sink (taint) analysis.
  - [SonarQube](http://www.sonarqube.org/) - Scans source code for more
    than 20 languages for Bugs, Vulnerabilities, and Code Smells.
    SonarQube IDE plugins for Eclipse, Visual Studio, and IntelliJ
    provided by [SonarLint](http://www.sonarlint.org/).
  - [SourceGuard](https://portal.checkpoint.com/) - Scans source code for Vulnerable Dependencies,
    Sensitive Content Leaking, Malicious Files Injection, Malicious IPs/URLs.
    designed to leverage Check Point's different prevention technologies and services, provide source code security and visibility into the risk analysis of projects through static analysis. cross-platform CLI tool (Docker available) with an easy integration to any pipeline.
    provided by [Check Point](https://www.checkpoint.com/).
  - [SpotBugs](https://spotbugs.github.io/) - This is the active fork
    replacement for FindBugs, which is not maintained anymore.
  - [VisualCodeGrepper
    (VCG)](http://sourceforge.net/projects/visualcodegrepp/) - Scans
    C/C++, C\#, VB, PHP, Java, and PL/SQL for security issues and for
    comments which may indicate defective code. The config files can be
    used to carry out additional checks for banned functions or
    functions which commonly cause security issues.

[GitLab has lashed a free SAST tool for a bunch of different languages
natively into GitLab. So you might be able to use that, or at least
identify a free SAST tool for the language you need from that
list](https://docs.gitlab.com/ee/user/application_security/sast/index.html#supported-languages-and-frameworks).

An even broader list of free static analysis tools (not just for
security) for lots of different languages is here called: [Awesome
Static Analysis](https://endler.dev/awesome-static-analysis/)

## Commercial Tools Of This Type

  - [Application
    Inspector](https://www.ptsecurity.com/ww-en/products/ai/) (Positive
    Technologies) - combines SAST, DAST, IAST, SCA, configuration
    analysis and other technologies, incl. unique abstract
    interpretation; has capability to generate test queries (exploits)
    to verify detected vulnerabilities during SAST analysis; Supported
    languages include: Java, C\#, PHP, JavaScript, Objective C, VB.Net,
    PL/SQL, T-SQL, and others.
  - [AppScan on
    Cloud](https://cloud.appscan.com/)
    (HCL Software) - Cloud-based application security testing suite to perform SAST, DAST, IAST & SCA on web and mobile application.
  - [AppScan
    Source](https://www.hcltechsw.com/wps/portal/products/appscan/offerings/source)
    (HCL Software) - Static application security testing solution that helps identify vulnerabilities early in the development lifecycle, understand their origin and potential impact and remediate the problem
  - [BlueClosure BC Detect](https://www.blueclosure.com) (BlueClosure) -
    Analyzes client-side JavaScript.
  - [bugScout](https://bugscout.io/en/) (Nalbatech, Formerly Buguroo)
  - [CAST
    AIP](https://www.castsoftware.com/products/application-intelligence-platform)
    (CAST) Performs static and architectural analysis to identify
    numerous types of security issues. Supports over 30 languages.
    [AIP's security specific coverage is
    here](https://www.castsoftware.com/solutions/application-security/cwe#SupportedSecurityStandards).
  - [Codacy](https://www.codacy.com/) Offers security patterns for
    languages such as Python, Ruby, Scala, Java, JavaScript and more.
    Integrates with tools such as Brakeman, Bandit, FindBugs, and
    others. (free for open source projects)
  - [CodeScan Cloud](https://www.codescan.io/) A Salesforce focused, SaaS code quality tool leveraging SonarQube's OWASP 
    security hotspots to give security visibility on Apex, Visualforce, and Lightning proprietary languages.
  - [CodeSonar](https://www.grammatech.com/products/codesonar) tool that
    supports C, C++, Java and C\# and maps against the OWASP top 10
    vulnerabilities.
  - [Contrast
    Assess](https://www.contrastsecurity.com/interactive-application-security-testing-iast)
    (Contrast Security) - Contrast performs code security without
    actually doing static analysis. Contrast does Interactive
    Application Security Testing (IAST), correlating runtime code & data
    analysis. It provides code level results without actually relying on
    static analysis.
  - [Coverity Code
    Advisor](http://www.coverity.com/products/code-advisor/) (Synopsys)
  - [CxSAST](https://www.checkmarx.com/technology/static-code-analysis-sca/)
    (Checkmarx)
  - [Fortify](https://www.microfocus.com/en-us/products/static-code-analysis-sast)
    (Micro Focus, Formerly HP)
  - [Hdiv
    Detection](https://hdivsecurity.com/interactive-application-security-testing-iast)
    (Hdiv Security) - Hdiv performs code security without actually doing
    static analysis. Hdiv does Interactive Application Security Testing
    (IAST), correlating runtime code & data analysis. It provides
    code-level results without actually relying on static analysis.
  - [Julia](http://www.juliasoft.com/solutions) (JuliaSoft) - SaaS Java
    static analysis
  - [KlocWork](http://www.klocwork.com/capabilities/static-code-analysis)
    (KlocWork)
  - [Kiuwan](https://www.kiuwan.com/) (a division of Idera, Inc.) provides an application security 
    testing and analytics platform –    including SAST and SCA solutions – that reduces risk and 
    improves change management and DevOps processes
  - [Parasoft
    Test](http://www.parasoft.com/jsp/capabilities/static_analysis.jsp?itemId=547)
    (Parasoft)
  - [PITSS.CON](https://pitss.com/products/pitss-con/) (PITTS)
  - [PT Application
    Inspector](https://www.ptsecurity.com/ww-en/products/ai/) combines
    SAST, DAST, IAST, SCA, configuration analysis and other
    technologies, incl. unique abstract interpretation for high accuracy
    rate with minimum false positives; has a unique capability to
    generate special test queries (exploits) to verify detected
    vulnerabilities during SAST analysis; integrates with CI/CD, VCS,
    etc. PT AI helps to easily understand, verify, and fix flaws; has a
    simple UI; is highly automated and easy to use. Supported languages
    are Java, C\#, PHP, JavaScript, Objective C, VB.Net, PL/SQL, T-SQL,
    and others.
  - [Puma Scan Professional](https://pumascanpro.com/) - A .NET C\#
    static source code analyzer that runs as a Visual Studio IDE
    extension, Azure DevOps extension, and Command Line (CLI)
    executable.
  - [PVS-Studio](http://www.viva64.com/en/) - PVS-Studio is a tool
    for detecting bugs and security weaknesses in the source code of programs
    written in C, C++, C#, and Java.
    It is a commercial B2B solution, but provides several free [licensing options](https://www.viva64.com/en/b/0614/).
  - [reshift](https://www.reshiftsecurity.com) - A CI/CD tool that uses
    static code analysis to scan for vulnerabilities and uses machine
    learning to give a prediction on false positives. Supports Java with
    future support for NodeJS and JavaScript planned for sometime in
    2019.
  - [RIPS Code Analysis](https://www.ripstech.com/) (RIPS Technologies)
    - A SAST solution specialized for Java and PHP that detects unknown
    security vulnerabilities and code quality issues.
  - [SecureAssist](https://www.synopsys.com/software-integrity/resources/datasheets/secureassist.html)
    (Synopsys) - Scans code for insecure coding and configurations
    automatically as an IDE plugin for Eclipse, IntelliJ, and Visual
    Studio etc. Supports (Java, .NET, PHP, and JavaScript)
  - [Sentinel
    Source](https://www.whitehatsec.com/products/static-application-security-testing/)
    (Whitehat)
  - [Seeker](https://www.synopsys.com/software-integrity/products/interactive-application-security-testing.html)
    (Synopsys) Seeker performs code security without actually doing
    static analysis. Seeker does Interactive Application Security
    Testing (IAST), correlating runtime code & data analysis with
    simulated attacks. It provides code level results without actually
    relying on static analysis.
  - [SmartDec Scanner](https://smartdecscanner.com/) (SmartDec) Capable
    of identifying vulnerabilities and backdoors (undocumented features)
    in over 30 programming languages by analyzing source code or
    executables, without requiring debug info.
  - [Source Patrol](http://www.sourcepatrol.co.uk/) (Pentest)
  - [Thunderscan SAST](https://www.defensecode.com/thunderscan.php)
    (DefenseCode)
  - [Veracode Static
    Analysis](http://www.veracode.com/products/binary-static-analysis-sast)
    (Veracode)
  - [Xanitizer](http://www.xanitizer.net) - Scans Java and Scala for
    security vulnerabilities, mainly via taint analysis. Free for
    academic and open source projects (see
    [1](https://www.rigs-it.com/xanitizer-pricing/)).

## More info

  - [NIST's list of Source Code Security Analysis Tools](http://samate.nist.gov/index.php/Source_Code_Security_Analyzers.html)
  - [DAST Tools](/www-community/Vulnerability_Scanning_Tools) - Similar info on Dynamic Application Security Testing (DAST) Tools
  - [Free for Open Source Application Security Tools](/www-community/Free_for_Open_Source_Application_Security_Tools) - This page lists the Commercial Source Code Analysis Tools (SAST) we know of that are free for Open Source
