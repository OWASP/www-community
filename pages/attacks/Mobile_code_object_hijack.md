---

layout: col-sidebar
title: Mobile code object hijack
author: 
contributors: 
permalink: /attacks/Mobile_code_object_hijack
tags: attack, Mobile code object hijack
auto-migrated: 1

---

{% include writers.html %}

## Description

This attack consists of a technique to create objects without
constructors’ methods by taking advantage of the clone() method of
Java-based applications.

If a certain class implements cloneable() method declared as public, but
doesn’t has a public constructor method nor is declared as final, it is
possible to extend it into a new class and create objects using the
clone() method.

The clonable() method certifies that the clone() method functions
correctly. A cloned object has the same attributes (variables values) of
the original object, but the objects are independent.

## Risk Factors

TBD

## Examples

In this example, a public class “BankAccount” implements the clonable()
method which declares “Object clone(string accountnumber)”:

`public class BankAccount implements Cloneable{`
`public Object clone(String accountnumber) throws                                                                                                  `
`CloneNotSupportedException`
`     {`
`      Object returnMe = new BankAccount(account number);`
`      …`
`     }`
`}`

An attacker can implement a malicious public class that extends the
parent BankAccount class, as follows:

`public class MaliciousBankAccount extends BankAccount implements   `
`                                                      Cloneable{`
`public Object clone(String accountnumber) throws CloneNotSupportedException `
`              {`
`               Object returnMe = super.clone();`
`               …`
`              }`
`}`

A Java applet from a certain application is acquired and subverted by an
attacker. Then, they make the victim accept and run a
[Trojan](Trojan_Horse "wikilink") or malicious code that was prepared to
manipulate objects’ state and behavior. This code is instantiated and
executed continuously using default JVM on victim’s machine. When the
victim invokes the Java applet from the original application using the
same JVM, then the attacker clones the class, they manipulate the
attributes values, and then substitutes the original object for the
malicious one.

## Related [Threat Agents](Threat_Agents "wikilink")

  - TBD

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Mobile code: invoking untrusted mobile
    code](Mobile_code:_invoking_untrusted_mobile_code "wikilink")
  - [Mobile code: non-final public
    field](Mobile_code:_non-final_public_field "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Unsafe Mobile
    Code](:Category:_Unsafe_Mobile_Code "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Session
    Management](:Category:_Session_Management "wikilink")

## References

  - <http://cwe.mitre.org/data/definitions/491.html> - Mobile Code:
    Object Hijack
  - <http://www.fortifysoftware.com/vulncat/> - Object Model Violation:
    Erroneous clone() Method

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Abuse of
Functionality](Category:Abuse_of_Functionality "wikilink")
[Category:Attack](Category:Attack "wikilink")
