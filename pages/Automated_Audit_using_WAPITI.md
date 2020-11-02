---

title: Automated Audit using WAPITI
layout: col-sidebar
author:
contributors:
tags: python, audit
permalink: /Automated_Audit_using_WAPITI

---

{% include writers.html %}

## Description

WAPITI is a simple command line to tool to automate the audit of a web application. It's free and open source and has had some recent edits and updates ([WAPITI homepage](http://wapiti.sourceforge.net/)). The pplication is available for contribution at ([WAPITI
Repository](http://sourceforge.net/projects/wapiti/)).

Please be aware this command line does not replace a manual audit but can be useful to perform a first validation or exploration of legacy
projects.

## Requirements

Python 2.6+

It is also recommended that you perform a build of the app:

`python setup.py install`

## Command

`python wapiti http://mysite.com -n 10 -b folder -u -v 1 -f html -o /tmp/scan_report`

**Options used:**

- `-n`: Define a limit of urls to read with the same pattern (prevent endless loops), here limit to 10.
- `-b`: Set the scope of the scan, here we analyze all the links to the pages which are in the same domain as the URL passed.
- `-u`: Use color to highlight vulnerables parameters in output.
- `-v`: Define verbosity level, here we print each url.
- `-f`: Define report type, here we choose HTML format.
- `-o`: Define report destination, in our case it must be a directory because we choose HTML format.

**Attack modules used by WAPITI:**

- *backup*: This module search backup of scripts on the server.
- *blindsql*: Time-based blind sql scanner.
- *crlf*: Search for CR/LF injection in HTTP headers.
- *exec*: Module used to detect command execution vulnerabilities.
- *file*: Search for include()/fread() and other file handling vulns.
- *htaccess*: Try to bypass weak htaccess configurations.
- *nikto*: Use a Nikto database to search for potentially dangerous files.
- *permanentxss*: Look for permanent XSS.
- *sql*: Standard error-based SQL injection scanner.
- *xss*: Module for XSS detection.
- *buster*: Module for a file and directory buster attack - checking for "bad" files.
- *shellshock*: Module for Shellshock bug detection.

## Report

A sample TXT report is available [here](http://wapiti.sourceforge.net/example.txt).
