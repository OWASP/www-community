---

title: Fuzzing
layout: col-sidebar
author:
contributors:
tags:
auto-migrated: 1
permalink: /Fuzzing

---

{% include writers.html %}

*Fuzz testing* or *Fuzzing* is a Black Box software testing technique,
which basically consists in finding implementation bugs using
malformed/semi-malformed data injection in an automated fashion.

## A trivial example

Lets's consider an integer in a program, which stores the result of a
user's choice between 3 questions. When the user picks one, the choice
will be 0, 1 or 2. Which makes three practical cases. But what if we
transmit 3, or 255 ? We can, because integers are stored a static size
variable. If the default switch case hasn't been implemented securely,
the program may crash and lead to "classical" security issues:
(un)exploitable buffer overflows, DoS, ...

Fuzzing is the art of automatic bug finding, and it's role is to find
software implementation faults, and identify them if possible.

## History

Fuzz testing was developed at the University of Wisconsin Madison in
1989 by Professor Barton Miller and his students. Their (continued) work
can be found at <http://www.cs.wisc.edu/~bart/fuzz/> ; it's mainly
oriented towards command-line and UI fuzzing, and shows that modern
operating systems are vulnerable to even simple fuzzing.

## Fuzzer implementations

A fuzzer is a program which injects automatically semi-random data into
a program/stack and detect bugs.

The data-generation part is made of generators, and vulnerability
identification relies on debugging tools. Generators usually use
combinations of static fuzzing vectors (known-to-be-dangerous values),
or totally random data. New generation fuzzers use genetic algorithms to
link injected data and observed impact. Such tools are not public yet.

## Comparison with cryptanalysis

The number of possible tryable solutions is *the explorable solutions
space*. The aim of cryptanalysis is to reduce this space, which means
finding a way of having less keys to try than pure bruteforce to decrypt
something.

Most of the fuzzers are:

  - protocol/file-format dependant

<!-- end list -->

  - data-type dependant

Why?

  - First, because the fuzzer has to connect to the input channel, which
    is bound to the target.

<!-- end list -->

  - Second, because a program only understands structured-enough data.
    If you connect to a web server in a raw way, it will only respond to
    listed commands such as GET (or eventually crash). It will take less
    time to start the string with "GET ", and fuzz the rest, but the
    drawback is that you'll skip all the tests on the first verb.

In this regard, Fuzzers try to reduce the number of unuseful tests, i.e.
the values we already know that there's little chance they'll work: you
reduce unpredictability, in favor of speed.

## Attack types

A fuzzer would try combinations of attacks on:

  - numbers (signed/unsigned integers/float...)

<!-- end list -->

  - chars (urls, command-line inputs)

<!-- end list -->

  - metadata : user-input text (id3 tag)

<!-- end list -->

  - pure binary sequences

A common approach to fuzzing is to define lists of
"known-to-be-dangerous values" (*fuzz vectors*) for each type, and to
inject them or recombinations.

  - for integers: zero, possibly negative or very big numbers

<!-- end list -->

  - for chars: escaped, interpretable characters / instructions (ex: For
    SQL Requests, quotes / commands...)

<!-- end list -->

  - for binary: random ones

Please refer to [OWASP's Fuzz Vector's
resource](OWASP_Testing_Guide_Appendix_C:_Fuzz_Vectors "wikilink") for
real-life fuzzing vectors examples and methodology.

Protocols and file formats imply norms, which are sometimes blurry, very
complicated or badly implemented : that's why developers sometimes mess
up in the implementation process (because of time/cost constraints).
That's why it can be interesting to take the opposite approach: take a
norm, look at all mandatory features and constraints, and try all of
them; forbidden/reserved values, linked parameters, field sizes. That
would be *conformance testing oriented* fuzzing.

## Application fuzzing

Whatever the fuzzed system is, the attack vectors are within it's I/O.
For a desktop app:

  - the UI (testing all the buttons sequences / text inputs)

<!-- end list -->

  - the command-line options

<!-- end list -->

  - the import/export capabilities (see file format fuzzing below)

For a web app: urls, forms, user-generated content, RPC requests, ...

## Protocol fuzzing

A protocol fuzzer sends forged packets to the tested application, or
eventually acts as a proxy, modifying requests on the fly and replaying
them.

## File format fuzzing

A file format fuzzer generates multiple malformed samples, and opens
them sequentially. When the program crashes, debug information is kept
for further investigation.

One can attack:

  - the parser layer (container layer): file format constraints,
    structure, conventions, field sizes, flags, ...

<!-- end list -->

  - the codec/application layer: lower-level attacks, aiming at the
    program's deeper internals

One example of file format related vulnerabilities:
[MS04-028](http://www.microsoft.com/technet/security/bulletin/ms04-028.mspx)
(KB833987) Microsoft's JPEG GDI+ vulnerability was a zero sized comment
field, without content.

Surprisingly, file format fuzzers are not that common, but tend to
appear these days; some examples:

  - A generic file format fuzzer : [Ilja van Sprundel's
    mangle.c](http://www.digitaldwarf.be/products/mangle.c); "it's usage
    is very simple, it takes a filename and headersize as input. it will
    then change approximatly between 0 and 10% of the header with random
    bytes." (from the author)

<!-- end list -->

  - Zzuf can act as a fuzzed file generator, <http://sam.zoy.org/zzuf/>

<!-- end list -->

  - One may use tools like [Hachoir](http://hachoir.org/) as a generic
    parser for file format fuzzer development.

## Fuzzers advantages

*The great advantage of fuzz testing is that the test design is
extremely simple, and free of preconceptions about system behavior*
(from Wikipedia <http://en.wikipedia.org/wiki/Fuzz_testing>).

The systematical/random approach allows this method to find bugs that
would have often been missed by human eyes. Plus, when the tested system
is totally closed (say, a SIP phone), fuzzing is one of the only means
of reviewing it's quality.

## Fuzzers limitations

Fuzzers usually tend to find simple bugs; plus, the more a fuzzer is
protocol-aware, the less weird errors it will find. This is why the
exhaustive / random approach is still popular among the fuzzing
community.

Another problem is that when you do some black-box-testing, you usually
attack a closed system, which increases difficulty to evaluate the
dangerosity/impact of the found vulnerability (no debugging
possibilities).

## Why Fuzz?

The purpose of fuzzing relies on the assumption that there are bugs
within every program, which are waiting to be discovered. Therefore, a
systematical approach should find them sooner or later.

Fuzzing can add another point of view to classical software testing
techniques (hand code review, debugging) because of it's non-human
approach. It doesn't replace them, but is a reasonable complement,
thanks to the limited work needed to put the procedure in place.

Recent fuzzing initiatives:

  - The [Month of Kernel Bugs](http://projects.info-pull.com/mokb/),
    which revealed an Apple Wireless flaw; see
    <http://kernelfun.blogspot.com/>; mainly used file system fuzzing
    tools

<!-- end list -->

  - The [Month of Browser Bugs](http://browserfun.blogspot.com/)
    ([review here](http://osvdb.org/blog/?p=127)); number of bugs found:
    MSIE: 25 Apple Safari: 2 Mozilla: 2 Opera: 1 Konqueror: 1; used
    DHTML, Css, DOM, ActiveX fuzzing tools

## Fuzzers from OWASP

Fuzzing with [WebScarab](WebScarab "wikilink"): a framework for
analysing applications that communicate using the HTTP and HTTPS
protocols

[JBroFuzz](JBroFuzz "wikilink"): a web application fuzzer

[WSFuzzer](WSFuzzer "wikilink"): real-world manual SOAP pen testing tool

## Technical resources on OWASP

[OWASP Testing Guide Appendix C: Fuzz
Vectors](OWASP_Testing_Guide_Appendix_C:_Fuzz_Vectors "wikilink")

## References

Wikipedia article - <http://en.wikipedia.org/wiki/Fuzz_testing>

Fuzzing-related papers -
<http://www.threatmind.net/secwiki/FuzzingPapers>

[The fuzzing mailing list
archive](https://web.archive.org/web/20090202043027/http://www.whitestar.linuxbox.org/pipermail/fuzzing/)

## Fuzzing tools

### Open Source

#### Mutational Fuzzers

[american fuzzy
lop](https://en.wikipedia.org/wiki/American_fuzzy_lop_\(fuzzer\))

[Radamsa - a flock of fuzzers](https://github.com/aoh/radamsa)

#### Fuzzing Frameworks

[Sulley Fuzzing Framework](https://github.com/OpenRCE/sulley)

[boofuzz](https://github.com/jtpereyda/boofuzz)

[BFuzz](https://github.com/RootUp/BFuzz)

#### Domain-Specific Fuzzers

[Microsoft SDL MiniFuzz File
Fuzzer](http://www.microsoft.com/download/en/details.aspx?id=21769)

[Microsoft SDL Regex
Fuzzer](http://www.microsoft.com/download/en/details.aspx?id=20095)

[ABNF Fuzzer](https://github.com/nradov/abnffuzzer)

### Commercial products

[Codenomicon's product
suite](http://www.codenomicon.com/products/all.shtml)

[Peach Fuzzing Platform](http://peachfuzzer.com)

[Spirent Avalanche NEXT](http://www.spirent.com/Products/AvalancheNEXT)

[Beyond Security's beSTORM
product](http://www.beyondsecurity.com/bestorm_overview.html)

### Deprecated Tools

[Untidy - XML
Fuzzer](http://www.bonsai-sec.com/en/research/untidy-xml-fuzzer.php)
(Now integrated into Peach)
