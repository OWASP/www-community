---

layout: col-sidebar
title: Mobile code non-final public field
author: 
contributors: 
permalink: /attacks/Mobile_code_non-final_public_field
tags: attack, Mobile code non-final public field
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack aims to manipulate non-final public variables used in mobile
code, by injecting malicious values on it, mostly in Java and C++
applications.

When a public member variable or class used in mobile code isn’t
declared as final, its values can be maliciously manipulated by any
function that has access to it in order to extend the application code
or acquire critical information about the application.

## Risk Factors

TBD

## Examples

A Java applet from a certain application is acquired and subverted by an
attacker. Then, they make the victim accept and run a Trojan or malicious
code that was prepared to manipulate non-final objects’ state and
behavior. This code is instantiated and executed continuously using
default JVM on the victim’s machine. When the victim invokes the Java
applet from the original application using the same JVM, the malicious
process could be mixed with original applet, thus it modifies values of
non-final objects and executes under victim’s credentials.

In the following example, the class “any_class” is declared as final
and “server_addr” variable is not:

`public final class any_class extends class_Applet {`
`public URL server_addr;`
`…`
`}`

In this case, the value of “server_addr” variable could be set by any
other function that has access to it, thus changing the application
behavior. A proper way to declare this variable is:

`public class any_class extends class_Applet {`
`public final URL server_addr;`
`…`
`}`

When a variable is declared as final its value cannot be modified.

## Related [Threat Agents](Threat_Agents "wikilink")

TBD

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Mobile code: invoking untrusted mobile
    code](Mobile_code:_invoking_untrusted_mobile_code "wikilink")
  - [Mobile code: object hijack](Mobile_code:_object_hijack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Unsafe Mobile
    Code](:Category:_Unsafe_Mobile_Code "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Access Control](:Category:_Access_Control "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/493.html> – Mobile Code:
    non-final public field
  - <http://www.fortifysoftware.com/vulncat/> - Unsafe Mobile Code:
    Access Violation
  - <http://www.fortifysoftware.com/vulncat/> - Unsafe Mobile Code:
    Public finalize() Method

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[the last two links are the same](Category:FIXME "wikilink")
[Category:Abuse of
Functionality](Category:Abuse_of_Functionality "wikilink")
[Category:Attack](Category:Attack "wikilink")
