---

title: Emedding Null Code
layout: col-sidebar
author:
contributors:
tags: attacks
auto-migrated: 1
permalink: /attacks/Embedding_Null_Code

---

## Description

The Embedding NULL Bytes/characters technique exploits applications that
don’t properly handle postfix NULL terminators. It is used as a
technique to perform other attacks, like directory browsing, path
traversal, SQL injection, execution of arbitrary code, among others. It
can be found lots of vulnerable applications and exploits available to
abuse systems using this technique.

This technique includes several variations to represent the postfix NULL
terminator:

`PATH%00`
`PATH[0x00]`
`PATH[alternate representation of NULL character]`

<script>

</script>

%00

## Example

### Example1 – PHP Script

In the following example, it’s shown the use of this technique to modify
an URL and access arbitrary files on a filesystem due a vulnerability on
PHP script.

`$whatever = addslashes($_REQUEST['whatever']);`
`include("/path/to/program/" . $whatever . "/header.htm");`

By manipulating the URL using postfix NULL bytes, one can have access to
UNIX password file:

`http://vuln.example.com/phpscript.php?whatever=../../../etc/passwd%00`

### Example2 – Adobe PDF ActiveX Attack

Another know attack, consists in the exploitation of buffer overflow in
the ActiveX component (pdf.ocx) that allows remote execution arbitrary
code.

The problem happens when a link is requested as:

`GET /some_dir/file.pdf.pdf%00[long string] HTTP/1.1`

In this case, the request must be made to a web server that truncates
the request at the null byte (%00), as Microsoft IIS and Netscape
Enterprise web servers. Though the requested URI is truncated for the
purposes of locating the file, the long string is still passed to the
Adobe ActiveX component. This component triggers a buffers overflow
within RTLHeapFree() allowing for an attacker to overwrite an arbitrary
word in memory.

This attack can be performed by adding malicious content to the end of
any embedded link and referencing any Microsoft IIS or Netscape
Enterprise web server. It is not necessary to establish a malicious web
site to execute this attack.

For more details about this attack, see External References topics.

## External References

<http://capec.mitre.org/data/definitions/52.html>

<http://nvd.nist.gov/nvd.cfm?cvename=CVE-2004-0629>
