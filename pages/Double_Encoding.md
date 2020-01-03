---

title: Double Encoding
layout: col-sidebar
author:
contributors:
tags:
auto-migrated: 1
permalink: /Double_Encoding

---

## Description

This attack technique consists of encoding user request parameters twice
in hexadecimal format in order to bypass security controls or cause
unexpected behavior from the application. It's possible because the
webserver accepts and processes client requests in many encoded forms.

By using double encoding it’s possible to bypass security filters that
only decode user input once. The second decoding process is executed by
the backend platform or modules that properly handle encoded data, but
don't have the corresponding security checks in place.

Attackers can inject double encoding in pathnames or query strings to
bypass the authentication schema and security filters in use by the web
application.

There are some common characters sets that are used in Web applications
attacks. For example, [Path Traversal](/attacks/Path_Traversal)
attacks use “../” (dot-dot-slash) , while
[XSS](/attacks/xss) attacks use “\<” and “\>”
characters. These characters give a hexadecimal representation that
differs from normal data.

For example, “../” (dot-dot-slash) characters represent %2E%2E%2f in
hexadecimal representation. When the % symbol is encoded again, its
representation in hexadecimal code is %25. The result from the double
encoding process ”../”(dot-dot-slash) would be %252E%252E%252F:

  - The hexadecimal encoding of “../” represents "%2E%2E%2f"

<!-- end list -->

  - Then encoding the “%” represents "%25"

<!-- end list -->

  - Double encoding of “../” represents "%252E%252E%252F"

## Risk Factors

TBD

## Examples

### Example 1

This example presents an old well-known vulnerability found in IIS
versions 4.0 and 5.0, where an attacker could bypass an authorization
schema and gain access to any file on the same drive as the web root
directory due to an issue with the decoding mechanism. For more details
about folder traversal vulnerability, see
[CVE 2001-0333](http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-0333).

In this scenario, the victim has a published executable directory (e.g.
cgi) that’s stored on the same partition as the Windows system folder.
An attacker could execute arbitrary commands on the web server by
submitting the following URL:

Original URL:

`http://victim/cgi/../../winnt/system32/cmd.exe?/c+dir+c:\`

However, the application uses a security check filter that refuses
requests containing characters like “../”. By double encoding the URL,
it’s possible to bypass security the filter:

Double encoded URL:

`http://victim/cgi/%252E%252E%252F%252E%252E%252Fwinnt/system32/cmd.exe?/c+dir+c:\ `

### Example 2

A double encoded URL can be used to perform an XSS attack in order to
bypass a built-in XSS detection module. Depending on the implementation,
the first decoding process is performed by HTTP protocol and the
resultant encoded URL will bypass the XSS filter, since it has no
mechanisms to improve detection. A simple example XSS would be:

<script>

alert('XSS')

</script>

This malicious code could be inserted into a vulnerable application,
resulting in an alert window with the message “XSS”. However, the web
application can have a character filter which prohibits characters such
as “\< “, “\>” and “/”, since they are used to perform web application
attacks. The attacker could use a double encoding technique to bypass
the filter and exploit the client’s session. The encoding process for
this Java script is:

<table >

<tr>

<td colspan=30>

<b> Char </b>

</td>

<td colspan=40>

<b> Hex encode </b>

</td>

<td colspan=50%>

<b> Then encoding '%' </b>

</td>

<td colspan=50%>

<b> Double encode </b>

</td>

</tr>

<tr>

<td colspan=30>

“\<”

</td>

<td colspan=40>

“%3C”

</td>

<td colspan=50%>

“%25”

</td>

<td colspan=50%>

“%253C”

</td>

</tr>

<tr>

<td colspan=30>

“/”

</td>

<td colspan=40>

“%2F”

</td>

<td colspan=50%>

“%25”

</td>

<td colspan=50%>

“%252F”

</td>

</tr>

<tr>

<td colspan=30>

“\>”

</td>

<td colspan=40>

“%3E”

</td>

<td colspan=50%>

“%25”

</td>

<td colspan=50%>

“%253E”

</td>

</tr>

</table>

Finally, the malicious double encoding code is:

`%253Cscript%253Ealert('XSS')%253C%252Fscript%253E`

## Related [Attacks](Attacks "wikilink")

  - [SQL Injection](/attacks/SQL_Injection)
  - [Cross-site Scripting
    (XSS)](/attacks/xss)
  - [Path Traversal](/attacks/Path_Traversal)

## References

  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CAN-2005-1945>
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CAN-2005-0054>
