---

layout: col-sidebar
title: Unsafe JNI
author: 
contributors: 
permalink: /vulnerabilities/Unsafe_JNI
tags: vulnerability, Unsafe JNI
auto-migrated: 1

---

{% include writers.html %}

Last revision (mm/dd/yyyy): **05/27/2009**

## Description

Improper use of the Java Native Interface (JNI) can render Java
applications vulnerable to security flaws in other languages.

Unsafe JNI errors occur when a Java application uses JNI to call code
written in another programming language.

## Risk Factors

TBD

## Examples

The following Java code defines a class named Echo. The class declares
one native method (defined below), which uses C to echo commands entered
on the console back to the user.

```
    class Echo {
        public native void runEcho();

        static {
            System.loadLibrary("echo");
        }

        public static void main(String[] args) {
            new Echo().runEcho();
        }
    }
```

The following C code defines the native method implemented in the Echo
class:

```
    #include <jni.h>
    #include "Echo.h"//the java class above compiled with javah
    #include <stdio.h>

    JNIEXPORT void JNICALL
    Java_Echo_runEcho(JNIEnv *env, jobject obj)
    {
        char buf[64];
        gets(buf);
        printf(buf);
    }
```

Because the example is implemented in Java, it may appear that it is
immune to memory issues like buffer overflow vulnerabilities. Although
Java does do a good job of making memory operations safe, this
protection does not extend to vulnerabilities occurring in source code
written in other languages that are accessed using the Java Native
Interface. Despite the memory protections offered in Java, the C code in
this example is vulnerable to a buffer overflow because it makes use of
gets(), which does not perform any bounds checking on its input.

The Sun Java(TM) Tutorial provides the following description of JNI
\[2\]:

*The JNI framework lets your native method utilize Java objects in the
same way that Java code uses these objects. A native method can create
Java objects, including arrays and strings, and then inspect and use
these objects to perform its tasks. A native method can also inspect and
use objects created by Java application code. A native method can even
update Java objects that it created or that were passed to it, and these
updated objects are available to the Java application. Thus, both the
native language side and the Java side of an application can create,
update, and access Java objects and then share these objects between
them.*

The vulnerability in the example above could easily be detected through
a source code audit of the native method implementation. This may not be
practical or possible depending on the availability of the C source code
and the way the project is built, but in many cases it may suffice.
However, the ability to share objects between Java and native methods
expands the potential risk to much more insidious cases where improper
data handling in Java may lead to unexpected vulnerabilities in native
code or unsafe operations in native code corrupt data structures in
Java.

Vulnerabilities in native code accessed through a Java application are
typically exploited in the same manner as they are in applications
written in the native language. The only challenge to such an attack is
for the attacker to identify that the Java application uses native code
to perform certain operations. This can be accomplished in a variety of
ways, including identifying specific behaviors that are often
implemented with native code or by exploiting a system information leak
in the Java application that exposes its use of JNI \[2\].

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [Buffer Overflow](Buffer_Overflow "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

  - \[1\] B. Stearns. The Java™ Tutorial: The Java Native Interface. Sun
    Microsystems, 2005.
    <http://java.sun.com/docs/books/tutorial/native1.1/>
  - \[2\] Fortify Descriptions. <http://vulncat.fortifysoftware.com>.

__NOTOC__

[The first link works, but the page says the content is going to be
removed at some point. Need to change link](Category:FIXME "wikilink")
[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:Use of Dangerous
API](Category:Use_of_Dangerous_API "wikilink")
[Category:Java](Category:Java "wikilink")
[Category:C/C++](Category:C/C++ "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")