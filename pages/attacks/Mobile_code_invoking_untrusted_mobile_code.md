---

layout: col-sidebar
title: Mobile code invoking untrusted mobile code
author: 
contributors: 
permalink: /attacks/Mobile_code_invoking_untrusted_mobile_code
tags: attack, Mobile code invoking untrusted mobile code
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack consists of a manipulation of a mobile code in order to
execute malicious operations at the client side. By intercepting client
traffic using the
[man-in-the-middle](Man-in-the-middle_attack "wikilink") technique, a
malicious user could modify the original mobile code with arbitrary
operations that will be executed on the client’s machine under their
credentials. In another scenario, the malicious mobile code could be
hosted in an untrustworthy web site or it could be permanently injected
on a vulnerable web site through an injection attack. This attack can be
performed over Java or C++ applications and affects any operating
system.

## Risk Factors

TBD

## Examples

The following code demonstrates how this attack could be performed using
a Java applet.

```
 // here declarer a object URL with the path of the malicious class
 URL[] urlPath= new URL[]{new URL("file:subdir/")};

 // here generate a object “loader” which is responsible to load a class in the URL path
 URLClassLoader  classLoader = new URLClassLoader(urlPath);

 //here declare a object of a malicious class contained in “classLoader”
 Class loadedClass = Class.forName("loadMe", true, classLoader);<br><br>
```

To solve this issue, it’s necessary to use some type of integrity
mechanism to assure that the mobile code has not been modified.

## Related [Threat Agents](Threat_Agents "wikilink")

  - TBD

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Mobile code: non-final public
    field](Mobile_code:_non-final_public_field "wikilink")
  - [Mobile code: object hijack](Mobile_code:_object_hijack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Unsafe Mobile
    Code](:Category:_Unsafe_Mobile_Code "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Hashing](Hashing "wikilink")
  - [Bounds Checking](Bounds_Checking "wikilink")
  - [Safe Libraries](Safe_Libraries "wikilink")
  - [Static Code Analysis](Static_Code_Analysis "wikilink")
  - [Executable space
    protection](Executable_space_protection "wikilink")
  - [Address space layout randomization
    (ASLR)](Address_space_layout_randomization_\(ASLR\) "wikilink")
  - [Stack-smashing Protection
    (SSP)](Stack-smashing_Protection_\(SSP\) "wikilink")

## References

  - <https://buildsecurityin.us-cert.gov/daisy/bsi/100/version/1/part/4/data/CLASP_ApplicationSecurityProcess.pdf?branch=main&language=default>
  - <http://cwe.mitre.org/data/definitions/494.html>

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category: Abuse of
Functionality](Category:_Abuse_of_Functionality "wikilink")
[Category:Attack](Category:Attack "wikilink")
