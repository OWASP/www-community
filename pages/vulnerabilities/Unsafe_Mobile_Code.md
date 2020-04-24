---

layout: col-sidebar
title: Unsafe Mobile Code
author: 
contributors: 
permalink: /vulnerabilities/Unsafe_Mobile_Code
tags: vulnerability, Unsafe Mobile Code
auto-migrated: 1

---

{% include writers.html %}

## Description

Mobile code, such as a Java Applet, is code that is transmitted across a
network and executed on a remote machine. Because mobile code developers
have little if any control of the environment in which their code will
execute, special security concerns become relevant. One of the biggest
environmental threats results from the risk that the mobile code will
run side-by-side with other, potentially malicious, mobile code. Because
all of the popular web browsers execute code from multiple sources
together in the same JVM, many of the security guidelines for mobile
code are focused on preventing manipulation of your objects' state and
behavior by adversaries who have access to the same virtual machine
where your program is running.

### Access Violation

The program violates secure coding principles for mobile code by
returning a private array variable from a public access method.

Returning a private array variable from a public access method allows
the calling code to modify the contents of the array, effectively giving
the array public access and contradicting the intentions of the
programmer who made it private.

**Example**

The following Java Applet code mistakenly returns a private array
variable from a public access method.

```
    public final class urlTool extends Applet {
        private URL[] urls;
        public URL[] getURLs() {
            return urls;
        }
            ...
    }
```

.

### Dangerous Array Declaration

The program violates secure coding principles for mobile code by
declaring an array public, final, and static.

In most cases an array declared public, final, and static is a bug.
Because arrays are mutable objects, the final constraint requires that
the array object itself be assigned only once, but makes no guarantees
about the values of the array elements. Since the array is public, a
malicious program can change the values stored in the array. In most
situations the array should be made private.

**Example**

The following Java Applet code mistakenly declares an array public,
final, and static.

```
    public final class urlTool extends Applet {
        public final static URL[] urls;
        ...
    }
```

### Dangerous Public Field

The program violates secure coding principles for mobile code by
declaring a member variable public but not final.

All public member variables in an Applet and in classes used by an
Applet should be declared final to prevent an attacker from manipulating
or gaining unauthorized access to the internal state of the Applet.

**Example**

The following Java Applet code mistakenly declares a member variable
public but not final.

```
    public final class urlTool extends Applet {
        public URL url;
        ...
    }
```

### Inner Class

The program violates secure coding principles for mobile code by making
use of an inner class.

Inner classes quietly introduce several security concerns because of the
way they are translated into Java bytecode. In Java source code, it
appears that an inner class can be declared to be accessible only by the
enclosing class, but Java bytecode has no concept of an inner class, so
the compiler must transform an inner class declaration into a peer class
with package level access to the original outer class. More insidiously,
since an inner class can access private fields in their enclosing class,
once an inner class becomes a peer class in bytecode, the compiler
converts private fields accessed by the inner class into protected
fields.

**Example**

The following Java Applet code mistakenly makes use of an inner class.

```
    public final class urlTool extends Applet {
        private final class urlHelper {
            ...
        }
        ...
    }
```

### Public finalize() Method

The program violates secure coding principles for mobile code by
declaring a finalize()method public.

A program should never call finalize explicitly, except to call
super.finalize() inside an implementation of finialize(). In mobile code
situations, the otherwise error prone practice of manual garbage
collection can become a security threat if an attacker can maliciously
invoke one of your finalize() methods because it is declared with public
access. If you are using finalize() as it was designed, there is no
reason to declare finalize() with anything other than protected access.

**Example**

The following Java Applet code mistakenly declares a public finalize()
method.

```
    public final class urlTool extends Applet {
        public void finalize() {
            ...
        }
        ...
    }
```

## Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

## Examples

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Vulnerability 1](Vulnerability_1 "wikilink")
  - [Vulnerabiltiy 2](Vulnerabiltiy_2 "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Use encapsulation](Use_encapsulation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

TBD

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:Authentication
Vulnerability](Category:Authentication_Vulnerability "wikilink")
[Category:Java](Category:Java "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")