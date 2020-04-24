---

title: Bytecode Obfuscation
layout: col-sidebar
author: Pierre Parrend
contributors:
tags: controls, java
auto-migrated: 1
permalink: /controls/Bytecode_obfuscation

---

{% include writers.html %}

## Status

Completely Updated: 7 March 2018
Released: 14/1/2008

## Principles

Java source code is typically compiled into Java bytecode -- the
instruction set of the Java virtual machine. The compiled Java bytecode
can be easily reversed engineered back into source code by a freely
available decompilers. Bytecode Obfuscation is the process of modifying
Java bytecode (executable or library) so that it is much harder to read
and understand for a hacker but remains fully functional. Almost all
code can be reverse-engineered with enough skill, time and effort.
However, for some platforms such as Java, Android, or.NET, free
decompilers can easily reverse-engineer source code from an executable
or library with no real time or effort. Automated bytecode obfuscation
makes reverse-engineering a program difficult and economically
unfeasible. Other advantages could include helping to protect licensing
mechanisms and unauthorized access, hiding vulnerabilities and shrinking
the size of the executable.

### How to recover Source Code from Bytecode?

There are a number of freely available Java decompilers that can
recreate source code from Java bytecode (executables or libraries).
Popular decompilers include:

  - [Bytecode Viewer](https://bytecodeviewer.com) - A Java 8 Jar &
    Android APK Reverse Engineering Suite (Decompiler, Editor, Debugger
    & More)
  - [CFR](http://www.benf.org/other/cfr/) - Another Java decompiler
  - [JDGui](http://jd.benow.ca/) - Yet another fast Java decompiler
  - [Fernflower](https://github.com/fesh0r/fernflower) - An analytical
    decompiler for Java

### How to help prevent Java source code from being Reverse-Engineered?

Java bytecode obfuscation consists of multiple complementary techniques
that can help create a layered defense against reverse engineering and
tampering. Some typical examples of obfuscation techniques include:

  - <b>Renaming</b> to alter the name of methods and variables to make
    the decompiled source much harder for a human to understand.
  - <b>Control Flow Obfuscation</b>creates conditional, branching, and
    iterative constructs that produce valid executable logic, but yield
    non-deterministic semantic results when decompiled.
  - <b>String Encryption</b> hides strings in the executable and only
    restores their original value when needed
  - <b>Instruction Pattern Transformation</b> converts common
    instructions to other, less obvious constructs potential confusing
    decompliers.
  - <b>Dummy Code Insertion</b> inserts code that does not affect the
    program’s logic, but breaks decompilers or makes reverse-engineered
    code harder to analyze.
  - <b>Unused Code and Metadata Removal</b> prunes out debug,
    non-essential metadata and used code from applications to reduce the
    information available to an attacker.
  - <b>Class file encryption</b> requires the JVM to decrypt the java
    executable before running confusing decompilers. Unlike some of the
    other transforms, this one is easy to circumvent by modifing the
    local JVM to simply write the executable to disk in its unencrypted
    form. See: [Javaworld
    article](http://www.javaworld.com/javaworld/javaqa/2003-05/01-qa-0509-jcrypt.html?page=2)).

### What obfuscation tools are available?

You can find popular tools for Java bytecode obfuscation below, or
simply type 'java obfuscator' in your favorite search engine.

  - [ProGuard Java
    Optimizer](https://sourceforge.net/projects/proguard/) is a very
    popular open source Java class file shrinker, optimizer, obfuscator,
    and preverifier.
  - [DashO Android & Java
    Obfuscator](https://www.preemptive.com/products/dasho/overview) a
    Java, Kotlin and Android application hardening and obfuscation tool
    that provides passive and active protection.
  - [KlassMaster Heavy Duty
    Protection](http://www.zelix.com/klassmaster/), shrinks and
    obfuscates both code and string constants. It can also translate
    stack traces back to readable form if you save the obfuscation log.
  - [Javaguard](http://sourceforge.net/projects/javaguard/), a simple
    obfuscator without a lot of documentation.

## Using Proguard

The following section provides a short tutorial for using
[Proguard](http://proguard.sourceforge.net/). First, download the code
under [following
url](http://sourceforge.net/project/showfiles.php?group_id=54750) and
unzip it.

For this tutorial, we use the [fr.inria.ares.sfelixutils-0.1.jar
package](http://www.rzo.free.fr/applis/fr.inria.ares.sfelixutils-0.1.jar).

Go to the main directory of Proguard. To launch it, use following script
and parameters:

`      java -jar lib/proguard.jar @config-genericFrame.pro`

config-genericFrame.pro is the option file (do not forget to adapt the
libraryjars parameter to your own system) :

`-obfuscationdictionary ./examples/dictionaries/compact.txt`
`-libraryjars /usr/java/j2sdk1.4.2_10/jre/lib/rt.jar`
`-injars fr.inria.ares.sfelixutils-0.1.jar`
`-outjar fr.inria.ares.sfelixutils-0.1-obs.jar`
`-dontshrink`
`-dontoptimize`
`-keep public class proguard.ProGuard {`
`public static void main(java.lang.String[]);`
`}`

Remark that the 'keep' option is mandatory, we use this default class
for not keep anything out.

The example dictionary (here compact.txt) is given with the code.

The output is stored in the package 'genericFrameOut.jar'.

You can observe the modifications implied by obfuscation with following
commands:

`jar xvf genericFrameOut.jar`
`cd genericFrame/pub/gui/`
`jad c.class`
`more c.jad more c.jad`

## Links

  - [Proguard](https://www.guardsquare.com/en/proguard)
  - [Javaguard](http://sourceforge.net/projects/javaguard/)
  - [Elements of Java Obfuscation](https://www.preemptive.com/obfuscation)
  - [Software Obfuscation](https://en.wikipedia.org/wiki/Obfuscation_\(software\))
