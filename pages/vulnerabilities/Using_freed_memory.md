---

layout: col-sidebar
title: Using freed memory
author: 
contributors: 
permalink: /vulnerabilities/Using_freed_memory
tags: vulnerability, Using freed memory
auto-migrated: 1

---

{% include writers.html %}

# Description

Referencing memory after it has been freed can cause a program to crash.

The use of heap allocated memory after it has been freed or deleted
leads to undefined system behavior and, in many cases, to a
write-what-where condition.

Use after free errors occur when a program continues to use a pointer
after it has been freed. Like [double free errors](Doubly_freeing_memory) 
and [memory leaks](Memory_leak), use after free errors have two common
and sometimes overlapping causes:

- Error conditions and other exceptional circumstances
- Confusion over which part of the program is responsible for freeing
    the memory

Use after free errors sometimes have no effect and other times cause a
program to crash. While it is technically feasible for the freed memory
to be re-allocated and for an attacker to use this reallocation to
launch a buffer overflow attack, we are unaware of any exploits based on
this type of attack.

The use of previously freed memory can have any number of adverse
consequences - ranging from the corruption of valid data to the
execution of arbitrary code, depending on the instantiation and timing
of the flaw.

The simplest way data corruption may occur involves the system's reuse
of the freed memory. In this scenario, the memory in question is
allocated to another pointer validly at some point after it has been
freed. The original pointer to the freed memory is used again and points
to somewhere within the new allocation. As the data is changed, it
corrupts the validly used memory; this induces undefined behavior in the
process.

If the newly allocated data chances to hold a class, in C++ for example,
various function pointers may be scattered within the heap data. If one
of these function pointers is overwritten with an address to valid
shellcode, execution of arbitrary code can be achieved.

# Consequences

- Integrity: The use of previously freed memory may corrupt valid
    data, if the memory area in question has been allocated and used
    properly elsewhere.
- Availability: If chunk consolidation occurs after the use of
    previously freed data, the process may crash when invalid data is
    used as chunk information.
- Access Control (instruction processing): If malicious data is
    entered before chunk consolidation can take place, it may be
    possible to take advantage of a write-what-where primitive to
    execute arbitrary code.

# Exposure period

- Implementation: Use of previously freed memory errors occur largely
    at implementation time.

# Platform

- Languages: C, C++, Assembly
- Operating Platforms: All

# Examples

## Example1

```
    #include <stdio.h>
    #include <unistd.h>

    #define BUFSIZER1   512
    #define BUFSIZER2   ((BUFSIZER1/2) - 8)

    int main(int argc, char **argv) {
        char *buf1R1;
        char *buf2R1;
        char *buf2R2;
        char *buf3R2;

        buf1R1 = (char *) malloc(BUFSIZER1);
        buf2R1 = (char *) malloc(BUFSIZER1);

        free(buf2R1);

        buf2R2 = (char *) malloc(BUFSIZER2);
        buf3R2 = (char *) malloc(BUFSIZER2);

        strncpy(buf2R1, argv[1], BUFSIZER1-1);
        free(buf1R1);
        free(buf2R2);
        free(buf3R2);
    }
```

## Example2

```
    char* ptr = (char*)malloc (SIZE);
    ...
    if (err) {
        abrt = 1;
        free(ptr);
    }
    ...
    if (abrt) {
        logError("operation aborted before commit", ptr);
    }
```

# Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

- [Buffer Overflow](Buffer_Overflow) (in particular, heap
    overflows): The method of exploitation is often the same, as both
    constitute the unauthorized writing to heap memory.
  - Write-what-where condition: The use of previously freed memory can
    result in a write-what-where in several ways.

# Related [Controls](https://owasp.org/www-community/controls/)

- Implementation: Ensuring that all pointers are set to NULL once the
    memory they point to has been freed can be effective strategy. The
    utilization of multiple or complex data structures may lower the
    usefulness of this strategy.
