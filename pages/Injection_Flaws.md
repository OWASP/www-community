---

title: Injection Flaws
layout: col-sidebar
author:
contributors: Jeremy Ferragamo, Wichers, Eofedal, kingthorin, Charlie Worrell
tags:
permalink: /Injection_Flaws

---

{% include writers.html %}

## Description

An injection flaw is a vulnerability which allows an attacker to relay malicious code through an application to another system. This can include compromising both backend systems as well as other clients connected to the vunlerable application.

The effects of these attacks include:

- Allowing an attacker to execute operating system calls on a target machine
- Allowing an attacker to compromise backend data stores
- Allowing an attacker to compromise or hijack sessions of other users
- Allowing an attacker to force actions on behalf of other users or services

Many web applications depend on operating system features, external programs, and processing of data queries submitted by users. When a web application passes information from an HTTP request as part of an external request, set up a way to scrub and validate the message. Otherwise an attacker can inject special (meta) characters, malicious commands/code, or command modifiers into the message.

While these attacks are not difficult to attempt, there are an increasing number of tools that scan for these flaws. An attacker can use these techniques to obtain, corrupt, or destroy the contents of your database, compromise backend systems, or attack other users.

Successful injection attacks may completely compromise or destroy a system. It is important to test for and protect against these types of attacks.

## Examples

1. OS Command Injection - A malicious parameter could modify the actions taken by a system call that normally retrieves the current user's file to access another user's file (e.g., by including path traversal `../` characters as part of a filename request). Additional commands could be tacked on to the end of a parameter that is passed to a shell script to execute an additional shell command (e.g., `; rm –r \*`) along with the intended command.

2. SQL Injection - Is a particularly widespread and dangerous form of injection. To exploit a SQL injection flaw, an attacker needs to find a parameter that the web application passes through to a database interaction. An attacker can then embed malicious SQL commands into the content of the parameter, to trick the web application to forward a malicious query to the database. SQL queries could be modified by adding additional 'constraints' to a where clause (e.g., `OR 1=1`) to gain access to or modify unauthorized data.

3. Cross-Site Scripting (XSS) - A type of injection, in which malicious scripts are injected into otherwise benign and trusted websites. XSS attacks occur when an attacker uses a web application to send malicious code, generally in the form of a browser side script, to a different end user.<sup>1</sup> Attacks of this type can hijack user sessions, log keystrokes, or perform malicious actions on behalf of victim users.

## How to Determine If You Are Vulnerable

The best way to determine if your applications are vulnerable to injection attacks is to search the source code for all calls to external resources (e.g., system, exec, fork, Runtime.exec, SQL queries, XML and JSON parsers, or whatever the syntax is for making requests to interpreters in your environment). Additionally, validate that all user provided input is sanitized and user provided data that is output is properly encoded where applicable.

[OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide) contains details on how to test for common injection attacks. See the References section below for additional information.

## How to Protect Yourself

1. Validate Input

Input validation is performed to ensure only properly formed data is entering the workflow in an information system, preventing malformed data from persisting in the database and triggering malfunction of various downstream components. Input validation should happen as early as possible in the data flow, preferably as soon as the data is received from the external party.

Data from all potentially untrusted sources should be subject to input validation, including not only Internet-facing web clients but also backend feeds over extranets, from suppliers, partners, vendors or regulators, each of which may be compromised on their own and start sending malformed data.

Input Validation should not be used as the primary method of preventing XSS, SQL Injection, and other attacks which are covered in respective cheat sheets but can significantly contribute to reducing their impact if implemented properly.<sup>2</sup>

2. Apply Least Privilege
   
Another strong protection against injection attacks is to ensure that the web application runs with only the privileges it absolutely needs to perform its function. So you should not run the webserver as root or access a database as DBADMIN, otherwise an attacker can abuse these administrative privileges granted to the web application. Some of the J2EE environments allow the use of the Java sandbox, which can prevent the execution of system commands.

3. Handle Exceptions and Returned Status Codes
   
If an external command must be used, any user information that is being inserted into the command should be rigorously checked. Mechanisms should be put in place to handle any possible errors, timeouts, or blockages during the call. All output, return codes and error codes from the call should be checked to ensure that the expected processing actually occurred. At a minimum, this will allow you to determine that something has gone wrong. Otherwise, the attack may occur and never be detected.

4. Investigate Mitigation Techniques for Specific Technologies Your Application Uses

Different injection attack types require different mitigation strategies (e.g. XSS vs. Server-side template injection). Review what technologies your application uses and available information on steps to take on preventing attack classes that abuse those technologies.

5. Avoid Accessing External Interpreters
   
Another way to protect against injection is to avoid accessing external interpreters wherever possible. For many shell commands and some system calls, there are language specific libraries that perform the same functions. Using such libraries does not involve the operating system shell interpreter, and therefore avoids a large number of problems with shell commands.

## References

- <sup>1</sup>OWASP [Cross-Site Scripting (XSS)](https://owasp.org/www-community/attacks/xss/)
- <sup>2</sup>OWASP [Input Validation Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Input_Validation_Cheat_Sheet.html)
- OWASP [Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Injection_Prevention_Cheat_Sheet.html)
- OWASP [SQL Injection Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/SQL_Injection_Prevention_Cheat_Sheet.html)
- OWASP [Cross-Site Scripting (XSS) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- OWASP [GraphQL Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/GraphQL_Cheat_Sheet.html)
- [NOSQL-injection](http://erlend.oftedal.no/blog/?blogid=110)
- [PayloadAllTheThings Repository of Attack Payloads](https://github.com/swisskyrepo/PayloadsAllTheThings)
- [PortSwigger - Server-Side Template Injection](https://portswigger.net/research/server-side-template-injection)
- OWASP [Cross-Site Scripting (XSS) Filter Evasion Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/XSS_Filter_Evasion_Cheat_Sheet.html)
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/v42/)
   - [Testing for SQL Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/05-Testing_for_SQL_Injection)
   - [Testing for LDAP Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/06-Testing_for_LDAP_Injection)
   - [Testing for XML Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/07-Testing_for_XML_Injection)
   - [Testing for SSI Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/08-Testing_for_SSI_Injection)
   - [Testing for XPath Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/09-Testing_for_XPath_Injection)
   - [Testing for IMAP SMTP Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/10-Testing_for_IMAP_SMTP_Injection)
   - [Testing for Code Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/11-Testing_for_Code_Injection)
   - [Testing for Command Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/12-Testing_for_Command_Injection)
   - [Testing for Format String Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/13-Testing_for_Format_String_Injection)
   - [Testing for Host Header Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/17-Testing_for_Host_Header_Injection)
   - [Testing for Server-Side Template Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/07-Input_Validation_Testing/18-Testing_for_Server-side_Template_Injection)
   - [Testing for HTML Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/03-Testing_for_HTML_Injection)
   - [Testing for CSS Injection](https://owasp.org/www-project-web-security-testing-guide/v42/4-Web_Application_Security_Testing/11-Client-side_Testing/05-Testing_for_CSS_Injection)
