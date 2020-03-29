---

layout: col-sidebar
title: Static Code Analysis
author: 
contributors: 
tags: controls, source code analysis, static code analysis
permalink: /controls/Static_Code_Analysis
auto-migrated: 1

---

## Description

Static Code Analysis (also known as Source Code Analysis) is usually
performed as part of a Code Review (also known as white-box testing) and
is carried out at the Implementation phase of a Security Development
Lifecycle (SDL). Static Code Analysis commonly refers to the running of
Static Code Analysis tools that attempt to highlight possible
vulnerabilities within 'static' (non-running) source code by using
techniques such as Taint Analysis and Data Flow Analysis.

Ideally, such tools would automatically find security flaws with a high
degree of confidence that what is found is indeed a flaw. However, this
is beyond the state of the art for many types of application security
flaws. Thus, such tools frequently serve as aids for an analyst to help
them zero in on security relevant portions of code so they can find
flaws more efficiently, rather than a tool that simply finds flaws
automatically.

Some tools are starting to move into the Integrated Development
Environment (IDE). For the types of problems that can be detected during
the software development phase itself, this is a powerful phase within
the development lifecycle to employ such tools, as it provides immediate
feedback to the developer on issues they might be introducing into the
code during code development itself. This immediate feedback is very
useful as compared to finding vulnerabilities much later in the
development cycle.

The UK Defense Standard 00-55 requires that Static Code Analysis be used
on all 'safety related software in defense equipment'.<sup>\[0\]</sup>

## Techniques

There are various techniques to analyze static source code for potential
vulnerabilities that maybe combined into one solution. These techniques
are often derived from compiler technologies.

### Data Flow Analysis

Data flow analysis is used to collect run-time (dynamic) information
about data in software while it is in a static state (Wögerer, 2005).

There are three common terms used in data flow analysis, basic block
(the code), Control Flow Analysis (the flow of data) and Control Flow
Path (the path the data takes):

Basic block: A sequence of consecutive instructions where control enters
at the beginning of a block, control leaves at the end of a block and
the block cannot halt or branch out except at its end (Wögerer, 2005).

Example PHP basic block:

    1. $a = 0;
    2. $b = 1;
    3.
    4. if ($a == $b)
    5. { # start of block
    6.   echo “a and b are the same”;
    7. } # end of block
    8. else
    9. { # start of block
    10. echo “a and b are different”;
    11.} # end of block

### Control Flow Graph (CFG)

An abstract graph representation of software by use of nodes that
represent basic blocks. A node in a graph represents a block; directed
edges are used to represent jumps (paths) from one block to another. If
a node only has an exit edge, this is known as an ‘entry’ block, if a
node only has a entry edge, this is know as an ‘exit’ block (Wögerer,
2005).

Example Control Flow Graph; ‘node 1’ represents the entry block and
‘node 6’ represents the exit block.

￼![Control_flow_graph.png](Control_flow_graph.png
"Control_flow_graph.png")

### Taint Analysis

Taint Analysis attempts to identify variables that have been 'tainted'
with user controllable input and traces them to possible vulnerable
functions also known as a 'sink'. If the tainted variable gets passed to
a sink without first being sanitized it is flagged as a vulnerability.

Some programming languages such as Perl and Ruby have Taint Checking
built into them and enabled in certain situations such as accepting data
via CGI.

### Lexical Analysis

Lexical Analysis converts source code syntax into ‘tokens’ of
information in an attempt to abstract the source code and make it easier
to manipulate (Sotirov, 2005).

Pre tokenised PHP source code:

    <?php $name = "Ryan"; ?>

Post tokenised PHP source code:

```
T_OPEN_TAG
T_VARIABLE
=
T_CONSTANT_ENCAPSED_STRING
;
T_CLOSE_TAG

```

## Strengths and Weaknesses

### Strengths

  - Scales Well (Can be run on lots of software, and can be repeatedly
    (like in nightly builds))
  - For things that such tools can automatically find with high
    confidence, such as buffer overflows, SQL Injection Flaws, etc. they
    are great.

### Weaknesses

  - Many types of security vulnerabilities are very difficult to find
    automatically, such as authentication problems, access control
    issues, insecure use of cryptography, etc. The current state of the
    art only allows such tools to automatically find a relatively small
    percentage of application security flaws. Tools of this type are
    getting better, however.
  - High numbers of false positives.
  - Frequently can't find configuration issues, since they are not
    represented in the code.
  - Difficult to 'prove' that an identified security issue is an actual
    vulnerability.
  - Many of these tools have difficulty analyzing code that can't be
    compiled. Analysts frequently can't compile code because they don't
    have the right libraries, all the compilation instructions, all the
    code, etc.

## Limitations

### False Positives

A static code analysis tool will often produce false positive results
where the tool reports a possible vulnerability that in fact is not.
This often occurs because the tool cannot be sure of the integrity and
security of data as it flows through the application from input to
output.

False positive results might be reported when analysing an application
that interacts with closed source components or external systems because
without the source code it is impossible to trace the flow of data in
the external system and hence ensure the integrity and security of the
data.

### False Negatives

The use of static code analysis tools can also result in false negative
results where vulnerabilities result but the tool does not report them.
This might occur if a new vulnerability is discovered in an external
component or if the analysis tool has no knowledge of the runtime
environment and whether it is configured securely.

## Important Selection Criteria

  - Requirement: Must support your language, but not usually a key
    factor once it does.
  - Types of Vulnerabilities it can detect (The OWASP Top Ten?) (more?)
  - Does it require a fully buildable set of source?
  - Can it run against binaries instead of source?
  - Can it be integrated into the developer's IDE?
  - License cost for the tool. (Some are sold per user, per org, per
    app, per line of code analyzed. Consulting licenses are frequently
    different than end user licenses.)
  - Does it support Object-oriented programming (OOP)?

## Examples

### RIPS PHP Static Code Analysis Tool

![Rips.jpg](Rips.jpg "Rips.jpg")

### OWASP LAPSE+ Static Code Analysis Tool

![LapsePlusScreenshot.png](LapsePlusScreenshot.png
"LapsePlusScreenshot.png")

## Tools

### OWASP Tools

| Software                                                                                | Language(s) |
| --------------------------------------------------------------------------------------- | ----------- |
| [OWASP Code Crawler](:Category:OWASP_Code_Crawler "wikilink")                           | .NET, Java  |
| [OWASP Orizon Project](:Category:OWASP_Orizon_Project "wikilink")                       | Java        |
| [OWASP LAPSE Project](OWASP_LAPSE_Project "wikilink")                                   | Java        |
| [OWASP O2 Platform](OWASP_O2_Platform "wikilink")                                       |             |
| [OWASP WAP-Web Application Protection](OWASP_WAP-Web_Application_Protection "wikilink") | PHP         |

### Open Source/Free

| Software                                                                                                           | Language(s)                                                                                                                                                        | OS(es)        |
| ------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------- |
| [Agnitio](https://sourceforge.net/projects/agnitiotool/)                                                           | ASP, ASP.NET, C\#, Java, Javascript, Perl, PHP, Python, Ruby, VB.NET, XML                                                                                          | Windows       |
| [Brakeman](https://brakemanscanner.org/)                                                                           | Ruby, Rails                                                                                                                                                        |               |
| [Google CodeSearchDiggity](https://www.bishopfox.com/resources/tools/google-hacking-diggity/attack-tools/)         | Multiple                                                                                                                                                           |               |
| [DevBug](http://www.devbug.co.uk)                                                                                  | PHP                                                                                                                                                                | web-based     |
| [FindBugs](http://findbugs.sourceforge.net/)                                                                       | Java                                                                                                                                                               |               |
| [SpotBugs](https://spotbugs.github.io/) (Successor of FindBugs)                                                    | Java                                                                                                                                                               |               |
| [Find Security Bugs](https://find-sec-bugs.github.io/)                                                             | Java, Scala, Groovy                                                                                                                                                |               |
| [FlawFinder](https://dwheeler.com/flawfinder/)                                                                     | C, C++                                                                                                                                                             |               |
| \[<https://docs.microsoft.com/en-us/previous-versions/dotnet/netframework-3.0/bb429476(v=vs.80>) Microsoft FxCop\] | .NET                                                                                                                                                               |               |
| [.NET Security Guard](https://security-code-scan.github.io/)                                                       | .NET, C\#, VB.net                                                                                                                                                  |               |
| [phpcs-security-audit](https://github.com/FloeDesignTechnologies/phpcs-security-audit)                             | PHP                                                                                                                                                                | Windows, Unix |
| [PMD](https://pmd.github.io/)                                                                                      | Java, JavaScript, Salesforce.com Apex and Visualforce, PLSQL, Apache Velocity, XML, XSL                                                                            |               |
| [Puma Scan](https://www.pumascan.com/)                                                                             | .NET, C\#                                                                                                                                                          |               |
| \[<https://docs.microsoft.com/en-us/previous-versions/windows/embedded/ms933794(v=msdn.10>) Microsoft PREFast\]    | C, C++                                                                                                                                                             |               |
| [RIPS Open Source](http://rips-scanner.sourceforge.net/)                                                           | PHP                                                                                                                                                                | any           |
| [SonarCloud](https://sonarcloud.io/about)                                                                          | ABAP, C, C++, Objective-C, COBOL, C\#, CSS, Flex, Go, HTML, Java, Javascript, Kotlin, PHP, PL/I, PL/SQL, Python, RPG, Ruby, Swift, T-SQL, TypeScript, VB6, VB, XML |               |
| [Splint](https://www.splint.org/)                                                                                  | C                                                                                                                                                                  |               |
| [VisualCodeGrepper](https://sourceforge.net/projects/visualcodegrepp/)                                             | C/C++, C\#, VB, PHP, Java, PL/SQL                                                                                                                                  | Windows       |

### Commercial

| Software                                                                                                                              | Language(s)                                                                                                                                                                                                                                                       | Notes                                        |
| ------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- |
| [RIPS](https://www.ripstech.com/product/)                                                                                             | Java, PHP                                                                                                                                                                                                                                                         | OWASP Member                                 |
| [Fortify](https://www.microfocus.com/en-us/products/static-code-analysis-sast/overview)                                               | ABAP/BSP, ActionScript/MXML (Flex), ASP.NET, VB.NET, C\# (.NET), C/C++, Classic ASP (w/VBScript), COBOL, ColdFusion CFML, HTML, Java (including Android), JavaScript/AJAX, JSP, Objective-C, PHP, PL/SQL, Python, T-SQL, Ruby, Swift, Visual Basic, VBScript, XML | OWASP Member                                 |
| [Veracode](https://www.veracode.com/)                                                                                                 | Android, ASP.NET, C\#, C, C++, Classic ASP, COBOL, ColdFusion/Java, Go, Groovy, iOS, Java, JavaScript, Perl, PhoneGap/Cordova, PHP, Python, React Native, RPG, Ruby on Rails, Scala, Titanium, TypeScript, VB.NET, Visual Basic 6, Xamarin                        | OWASP Member                                 |
| [CodeSonar](https://www.grammatech.com/)                                                                                              | C, C++, Java                                                                                                                                                                                                                                                      |                                              |
| [ParaSoft](https://www.parasoft.com/)                                                                                                 | C, C++, Java, .NET                                                                                                                                                                                                                                                |                                              |
| <s>[Armorize CodeSecure](http://www.armorize.com/codesecure/)</s>                                                                     |                                                                                                                                                                                                                                                                   | OWASP Member; acquired by Proofpoint in 2013 |
| [Checkmarx Static Code Analysis](https://www.checkmarx.com/)                                                                          | Android, Apex, ASP.NET, C\#, C++, Go, Groovy, HTML5, Java, JavaScript, JSP, .NET, Objective-C, Perl, PHP, PL/SQL, Python, Ruby, Scala, Swift, TypeScript, VB.NET, Visual Basic 6, Windows Phone                                                                   | OWASP Member                                 |
| [HCL AppScan on Cloud](https://cloud.appscan.com/)                                                                                 | Apex, ASP, C, C++, COBOL, ColdFusion, Go, Java, JavaScript(Client-side JavaScript, Kotlin, NodeJS, and AngularJS), .NET (C#, ASP.NET, VB.NET), .NET Core, Perl, PHP, PL/SQL, Python, Ruby, T-SQL, Swift, Visual Basic 6                                                                    | OWASP Member              |                                             
| [HCL AppScan Source](https://www.hcltechsw.com/wps/portal/products/appscan/offerings/source)                                                       | Android, Apex, ASP, C, C++, COBOL, ColdFusion, Go, Java, JavaScript(Client-side JavaScript, NodeJS, and AngularJS), .NET (C#, ASP.NET, VB.NET), .NET Core, Perl, PHP, PL/SQL, Python, Ruby, T-SQL, Visual Basic 6                                       | OWASP Member                                 |
| [Coverity](https://www.synopsys.com/software-integrity/security-testing/static-analysis-sast.html)                                    | Android, C\#, C, C++, Java, JavaScript, Node.js, Objective-C, PHP, Python, Ruby, Scala, Swift, VB.NET                                                                                                                                                             |                                              |
| [PVS-Studio](https://www.viva64.com/en/pvs-studio/)                                                                                   | C, C++, C\#                                                                                                                                                                                                                                                       |                                              |
| [Puma Scan Professional](https://pumascan.com/pricing/)                                                                               | .NET, C\#                                                                                                                                                                                                                                                         |                                              |
| [Klocwork](https://www.roguewave.com/products-services/klocwork/static-code-analysis)                                                 | C, C++, C\#, Java                                                                                                                                                                                                                                                 |                                              |
| [Polyspace Static Analysis](https://www.mathworks.com/products/polyspace.html)                                                        | C, C++, Ada                                                                                                                                                                                                                                                       |                                              |
| [CodeSec](http://www.seczone.cn/2018/06/27/codesec%E6%BA%90%E4%BB%A3%E7%A0%81%E5%AE%89%E5%85%A8%E6%A3%80%E6%B5%8B%E5%B9%B3%E5%8F%B0/) | C, C++, C\#, Java, JavaScript, PHP, Kotlin, Lua, Scala, TypeScript, Android                                                                                                                                                                                       |                                              |
| [Xanitizer](http://www.xanitizer.net)                                                                                                 | Java, Scala                                                                                                                                                                                                                                                       |                                              |

### Other Tool Lists

  - [NIST - Source Code Security
    Analyzers](http://samate.nist.gov/index.php/Source_Code_Security_Analyzers.html)
  - [Wikipedia - List of tools for static code
    analysis](http://en.wikipedia.org/wiki/List_of_tools_for_static_code_analysis)

## References

\[0\]

## Further Reading

  - [OWASP Code Review Guide
    v1.1](https://www.owasp.org/images/2/2e/OWASP_Code_Review_Guide-V1_1.pdf)
  - <http://www.crosstalkonline.org/storage/issue-archives/2003/200311/200311-German.pdf>
  - <http://www.ida.liu.se/~TDDC90/papers/industrial95.pdf>
  - <http://www.php-security.org/downloads/rips.pdf>
  - <http://www.seclab.tuwien.ac.at/papers/pixy.pdf>

\[\[Category:FIXME| In addition, one should classify control based on
the following subcategories:
Ex:\[\[Category:Error_Handling_Control|Category:Error Handling
Control\]\]

Availability Control Authorization Control Authentication Control
Concurrency Control Configuration Control Cryptographic Control Encoding
Control Error Handling Control Input Validation Control Logging and
Auditing Control Session Management Control \]\] __FORCETOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Control](Category:Control "wikilink")
