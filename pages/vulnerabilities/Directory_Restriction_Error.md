---

layout: col-sidebar
title: Directory Restriction Error
author: 
contributors: 
permalink: /vulnerabilities/Directory_Restriction_Error
tags: vulnerability, Directory Restriction Error
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Improper use of the chroot() system call may allow attackers to escape a
chroot jail.

The application fails to enforce the intended restricted directory
access policy. By using relative paths or other path traversal attack
mechanisms, an attacker can access unauthorized files outside the
restricted directory.

## Examples

Improper use of the chroot() system call may allow attackers to access
files that are outside the new root directory, and therefore breaks the
intended access control policy.

The chroot() system call allows a process to change its perception of
the root directory of the file system. After properly invoking chroot(),
a process cannot access any files outside the directory tree defined by
the new root directory. Such an environment is called a chroot jail, and
is commonly used to prevent the possibility that a processes could be
subverted and used to access unauthorized files. For instance, many FTP
servers run in chroot jails to prevent an attacker who discovers a new
vulnerability in the server from being able to download the password
file or other sensitive files on the system.

Improper use of chroot() may allow attackers to escape from the chroot
jail. The chroot() function call does not change the process's current
working directory, so relative paths may still refer to file system
resources outside of the chroot jail after chroot() has been called.

Consider the following source code from a (hypothetical) FTP server:

` chroot("/var/ftproot");`
` ...`
` fgets(filename, sizeof(filename), network);`
` localfile = fopen(filename, "r");`
` while ((len = fread(buf, 1, sizeof(buf), localfile)) != EOF) {`
`   fwrite(buf, 1, sizeof(buf), network);`
` }`
` fclose(localfile);`

This code is responsible for reading a filename from the network,
opening the corresponding file on the local machine, and sending the
contents over the network. This code could be used to implement the FTP
GET command. The FTP server calls chroot() in its initialization
routines in an attempt to prevent access to files outside of
/var/ftproot. But because the server fails to change the current working
directory by calling chdir("/"), an attacker could request the file
"../../../../../etc/passwd" and obtain a copy of the system password
file.

## Risk Factors

TBD

## Examples

TBD

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Path Traversal Attacks](Path_Traversal_Attacks "wikilink")
  - Attackers try to access unauthorized files, such as password files
    or configuration files.

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Input Validation](Input_Validation "wikilink")
  - [Access Control](Access_Control "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

\[\[Category:FIXME|add links

In addition, one should classify vulnerability based on the following
subcategories:
Ex:\[\[Category:Error_Handling_Vulnerability|Category:Error Handling
Vulnerability\]\]

Availability Vulnerability

Authorization Vulnerability

Authentication Vulnerability

Concurrency Vulnerability

Configuration Vulnerability

Cryptographic Vulnerability

Encoding Vulnerability

Error Handling Vulnerability

Input Validation Vulnerability

Logging and Auditing Vulnerability

Session Management Vulnerability\]\]

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:C/C++](Category:C/C++ "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink") [Category:Use
of Dangerous API](Category:Use_of_Dangerous_API "wikilink")
[Category:API Abuse](Category:API_Abuse "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")