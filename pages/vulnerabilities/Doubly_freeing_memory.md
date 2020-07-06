---

layout: col-sidebar
title: Doubly freeing memory
author: 
contributors: 
permalink: /vulnerabilities/Doubly_freeing_memory
tags: vulnerability, Doubly freeing memory

---

{% include writers.html %}

## Description

Double free errors occur when `free()` is called more than once with the same memory address as an argument.

Calling `free()` twice on the same value can lead to memory leak. When a program calls `free()` twice with the same argument, the program's memory management data structures become corrupted and could allow a malicious user to write values in arbitrary memory spaces. This corruption can cause the program to crash or, in some circumstances, alter the execution flow. By overwriting particular registers or memory spaces, an attacker can trick the program into executing code of their own choosing, often resulting in an interactive shell with elevated permissions.

When a buffer is `free()`'d, a linked list of free buffers is read to rearrange and combine the chunks of free memory (to be able to allocate larger buffers in the future). These chunks are laid out in a double linked list which points to previous and next chunks. Unlinking an unused buffer (which is what happens when `free()` is called) could allow an attacker to write arbitrary values in memory; essentially overwriting valuable registers, calling shellcode from its own buffer.

### Consequences

- Access control: Doubly freeing memory may result in a write-what-where condition, allowing an attacker to execute arbitrary code.

### Exposure period

- Requirements specification: A language which handles memory allocation and garbage collection automatically might be chosen.
- Implementation: Double frees are caused most often by lower-level logical errors.

### Platform

- Language: C, C++, Assembly
- Operating system: All

### Required resources

Any

### Severity

High

### Likelihood of exploit

Low to Medium

Doubly freeing memory can result in roughly the same write-what-where condition that the use of previously freed memory will.

## Examples

While contrived, this code should be exploitable on Linux distributions that don't ship with heap-chunk check summing turned on.

```
#include <stdio.h>
#include <unistd.h>

#define BUFSIZE1    512
#define BUFSIZE2    ((BUFSIZE1/2) - 8)

int main(int argc, char **argv) {
  char *buf1R1;
  char *buf2R1;
  char *buf1R2;

  buf1R1 = (char *) malloc(BUFSIZE2);
  buf2R1 = (char *) malloc(BUFSIZE2);

  free(buf1R1);
  free(buf2R1);

  buf1R2 = (char *) malloc(BUFSIZE1);
  strncpy(buf1R2, argv[1], BUFSIZE1-1);

  free(buf2R1);
  free(buf1R2);
}
``` 

Double free vulnerabilities have three common (and sometimes overlapping) causes:

- Error conditions and other exceptional circumstances
- Usage of the memory space after it's freed.
- Confusion over which part of the program is responsible for freeing the memory

Although some double free vulnerabilities are not much more complicated than the previous example, most are spread out across hundreds of lines of code or even different files. Programmers seem particularly susceptible to freeing global variables more than once.

## Related [Controls](../controls/)

- Implementation: Ensure that each allocation is freed only once. After freeing a chunk, set the pointer to NULL to ensure the pointer cannot be freed again. In complicated error conditions, be sure that clean-up routines respect the state of allocation properly. If the language is object oriented, ensure that object destructors delete each chunk of memory only once.

## Related [Attacks](../attacks/)

- [Buffer overflow attack](../attacks/Buffer_overflow_attack)
