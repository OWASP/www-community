---

title: 'Embedding Null Code'
layout: col-sidebar
author: Nsrav
contributors: 
  - 'Till Maas'
  - ADubhlaoich
tags: attack
permalink: /attacks/Embedding_Null_Code

---

{% include writers.html %}

## Description

The Embedding NULL Bytes/characters technique exploits applications that
don’t properly handle postfix NULL terminators. This technique can be used 
to perform other attacks such as directory browsing, path traversal, SQL 
injection, execution of arbitrary code, and others. It can be found in lots 
of vulnerable applications and there are lots of exploits available to 
abuse systems.

This technique includes several variations to represent the postfix NULL
terminator:

`PATH%00`  
`PATH[0x00]`  
`PATH[alternate representation of NULL character]`  
`<script></script>%00`  

## Examples

### PHP Script

The following example shows the use of this technique to modify a URL and 
access arbitrary files on a filesystem due a PHP script vulnerability.

`$whatever = addslashes($_REQUEST['whatever']);`  
`include("/path/to/program/" . $whatever . "/header.htm");`

By manipulating the URL using postfix NULL bytes, one can access the
UNIX password file:

`http://vuln.example.com/phpscript.php?whatever=../../../etc/passwd%00`

### Adobe PDF ActiveX Attack

Another attacks consists of exploitating buffer overflow in ActiveX components
 (pdf.ocx) to allow remote code execution.

The attack occurs when a link is requested as follows:

`GET /some_dir/file.pdf.pdf%00[long string] HTTP/1.1`  

This exploit can be used against a web server that truncates the request at 
the null byte `%00`, such as Microsoft IIS and Netscape Enterprise web servers. 
Though the requested URI is truncated when locating the file, the full string 
is still passed to the Adobe ActiveX component. It then triggers a buffer 
overflow within `RTLHeapFree()`, allowing an attacker to overwrite arbitrary
memory.

It can be performed by adding malicious content to the end of any embedded link 
that references a Microsoft IIS or Netscape Enterprise web server.  

## External References

http://capec.mitre.org/data/definitions/52.html

http://nvd.nist.gov/nvd.cfm?cvename=CVE-2004-0629
