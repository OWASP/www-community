---

layout: col-sidebar
title: Memory leak
author: 
contributors: 
permalink: /vulnerabilities/Memory_leak
tags: vulnerability, Memory leak
auto-migrated: 1

---

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

A memory leak is an unintentional form of memory consumption whereby the
developer fails to free an allocated block of memory when no longer
needed. The consequences of such an issue depend on the application
itself. Consider the following general three cases:

| align="center" style="width:20%; background:\#4058A0; color:white" | Case                                  | align="center" style="width:60%; background:\#4058A0; color:white" | Description of Consequence  |
| ------------------------------------------------------------------ | ------------------------------------- | ------------------------------------------------------------------ | --------------------------- |
| style="background:\#F2F2F2"                                        | **Short Lived User-land Application** |                                                                    | style="background:\#F2F2F2" |
| style="background:\#F2F2F2"                                        | **Long Lived User-land Application**  |                                                                    | style="background:\#F2F2F2" |
| style="background:\#F2F2F2"                                        | **Kernel-land Process**               |                                                                    | style="background:\#F2F2F2" |
|                                                                    |                                       |                                                                    |                             |

Memory is allocated but never freed.

Memory leaks have two common and sometimes overlapping causes:

  - Error conditions and other exceptional circumstances.
  - Confusion over which part of the program is responsible for freeing
    the memory

Most memory leaks result in general software reliability problems, but
if an attacker can intentionally trigger a memory leak, the attacker
might be able to launch a denial of service attack (by crashing the
program) or take advantage of other unexpected program behavior
resulting from a low memory condition \[1\].

## Risk Factors

  - Talk about the [factors](OWASP_Risk_Rating_Methodology "wikilink")
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

## Examples

### Example 1

The following example is a basic memory leak in C:

`#include <stdlib.h>`
`#include <stdio.h>`

`#define  LOOPS    10`
`#define  MAXSIZE  256`

`int main(int argc, char **argv)`
`{`
`     int count = 0;`
`     char *pointer = NULL;`

`     for(count=0; count<LOOPS; count++) {`
`          pointer = (char *)malloc(sizeof(char) * MAXSIZE);`
`     }`

`     free(pointer);`

`     return count;`
`}`

:\* In this example, we have 10 allocations of size MAXSIZE. Every
allocation, with the exception of the last, is lost. If no pointer is
pointed to the allocated block, it is unrecoverable during program
execution. A simple fix to this trivial example is to place the free()
call inside of the 'for' loop.

:\*[Here](http://www.securiteam.com/securitynews/5ZP0M1PIUI.html) is a
real world example of a memory leak causing denial of service

### Example 2

The following C function leaks a block of allocated memory if the call
to read() fails to return the expected number of bytes:

```
    char* getBlock(int fd) {
    char* buf = (char*) malloc(BLOCK_SIZE);
    if (!buf) {
      return NULL;
    }
    if (read(fd, buf, BLOCK_SIZE) != BLOCK_SIZE) {
      return NULL;
    }
    return buf;
    }
```

## Related [Attacks](Attacks "wikilink")

  - [Attack 1](Attack_1 "wikilink")
  - [Attack 2](Attack_2 "wikilink")

## Related [Vulnerabilities](Vulnerabilities "wikilink")

  - [Denial of Service](Denial_of_Service "wikilink")

## Related [Controls](Controls "wikilink")

Avoiding memory leaks in applications is difficult for even the most
skilled developers. Luckily, there are tools with aide in tracking down
such memory leaks. One such example on the Unix/Linux environment is
[Valgrind](http://valgrind.org/). Valgrind runs the desired program in
an environment such that all memory allocation and de-allocation
routines are checked. At the end of program execution, Valgrind will
display the results in an easy to read manner. The following is the
output of Valgrind using the flawed code above:

`[root@localhost Programming]# gcc -o leak leak.c`
`[root@localhost Programming]# valgrind ./leak`
`==6518== Memcheck, a memory error detector for x86-linux.`
`==6518== Copyright (C) 2002-2005, and GNU GPL'd, by Julian Seward et al.`
`==6518== Using valgrind-2.4.0, a program supervision framework for x86-linux.`
`==6518== Copyright (C) 2000-2005, and GNU GPL'd, by Julian Seward et al.`
`==6518== For more details, rerun with: -v`
`==6518==`
`==6518==`
`==6518== ERROR SUMMARY: 0 errors from 0 contexts (suppressed: 13 from 1)`
`==6518== malloc/free: in use at exit: 2304 bytes in 9 blocks.`
`==6518== malloc/free: 10 allocs, 1 frees, 2560 bytes allocated.`
`==6518== For counts of detected errors, rerun with: -v`
`==6518== searching for pointers to 9 not-freed blocks.`
`==6518== checked 49152 bytes.`
`==6518==`
`==6518== LEAK SUMMARY:`
`==6518==    definitely lost: 2304 bytes in 9 blocks.`
`==6518==      possibly lost: 0 bytes in 0 blocks.`
`==6518==    still reachable: 0 bytes in 0 blocks.`
`==6518==         suppressed: 0 bytes in 0 blocks.`
`==6518== Use --leak-check=full to see details of leaked memory.`

:\* As we can see in this example, we leak 9 block with a total of 2304
bytes as we expected. If we were to place the free() call inside of the
loop, we would get 0 memory blocks definitely lost.

## Related [Technical Impacts](Technical_Impacts "wikilink")

  - [Technical Impact 1](Technical_Impact_1 "wikilink")
  - [Technical Impact 2](Technical_Impact_2 "wikilink")

## References

\[1\] J. Whittaker and H. Thompson. How to Break Software Security.
Addison Wesley, 2003.

\[\[Category:FIXME|add links

In addition, one should classify vulnerability based on the following
subcategories:
Ex:\[\[Category:Error_Handling_Vulnerability|Category:Error Handling
Vulnerability\]\]

Availability Vulnerability

Authorization Vulnerability

Authentication Vulnerability

Concurrency Vulnerability

Configuration Vulnerability

Cryptographic Vulnerability

Encoding Vulnerability

Error Handling Vulnerability

Input Validation Vulnerability

Logging and Auditing Vulnerability

Session Management Vulnerability\]\]

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:C/C++](Category:C/C++ "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink") [Category:
Vulnerability](Category:_Vulnerability "wikilink")