---

layout: col-sidebar
title: Buffer Overflow Attack
author: 
contributors: OWASP, Rezos, Thaigoalz, KristenS, Andrew Smith, Jmanico, hblankenship , nbaars, cmvar8, CRImier, pranavek, hblankenship , tghosth, nbaars, k-37, kingthorin
permalink: /attacks/Buffer_overflow_attack
tags: attack, buffer overflow

---

{% include writers.html %}

## Description

Buffer overflow errors are characterized by the overwriting of memory
fragments of the process, which should have never been modified
intentionally or unintentionally. Overwriting values of the IP
(Instruction Pointer), BP (Base Pointer) and other registers causes
exceptions, segmentation faults, and other errors to occur. Usually
these errors end execution of the application in an unexpected way.
Buffer overflow errors occur when we operate on buffers of char type.

Buffer overflows can consist of overflowing the stack [Stack
overflow] or overflowing the heap [Heap
overflow]. We don't distinguish between these
two in this article to avoid confusion.

Below examples are written in C language under GNU/Linux system on x86
architecture.

## Examples

### Example 1

```C
#include <stdio.h>
int main(int argc, char **argv)
{
char buf[8]; // buffer for eight characters
gets(buf); // read from stdio (sensitive function!)
printf("%s\n", buf); // print out data stored in buf
return 0; // 0 as return value
}
```

This very simple application reads from the standard input an array of
the characters, and copies it into the buffer of the char type. The size
of this buffer is eight characters. After that, the contents of the
buffer is displayed and the application exits.

Program compilation:

```console
user@spin ~/inzynieria $ gcc bo-simple.c -o bo-simple
/tmp/ccECXQAX.o: In function `main':
bo-simple.c:(.text+0x17): warning: the `gets' function is dangerous and
should not be used.
```

At this stage, even the compiler suggests that the function gets() isn't
safe.

Usage example:

```console
user@spin ~/inzynieria $ ./bo-simple // program start
1234 // we eneter "1234" string from the keyboard
1234 // program prints out the conent of the buffer
user@spin ~/inzynieria $ ./bo-simple // start
123456789012 // we eneter "123456789012"
123456789012 // content of the buffer "buf" ?!?!
Segmentation fault // information about memory segmenatation fault
```

We manage (un)luckily to execute the faulty operation by the program,
and provoke it to exit abnormally.

Problem analysis:

The program calls a function, which operates on the char type buffer and
does no checks against overflowing the size assigned to this buffer. As
a result, it is possible to intentionally or unintentionally store more
data in the buffer, which will cause an error. The following question
arises: The buffer stores only eight characters, so why did function
printf() display twelve?. The answer comes from the process memory
organisation. Four characters which overflowed the buffer also overwrite
the value stored in one of the registers, which was necessary for the
correct function return. Memory continuity resulted in printing out the
data stored in this memory area.

### Example 2

```C
#include <stdio.h>
#include <string.h>

void doit(void)
{
        char buf[8];

        gets(buf);
          printf("%s\n", buf);
}

int main(void)
{
        printf("So... The End...\n");
        doit();
        printf("or... maybe not?\n");

        return 0;
}
```

This example is analogous to the first one. In addition, before and
after the doit() function, we have two calls to function printf().

```console
Compilation:

user@dojo-labs ~/owasp/buffer_overflow $ gcc example02.c -o example02
-ggdb
/tmp/cccbMjcN.o: In function `doit':
/home/user/owasp/buffer_overflow/example02.c:8: warning: the `gets'
function is dangerous and should not be used.

Usage example:
user@dojo-labs ~/owasp/buffer_overflow $ ./example02
So... The End...
TEST                   // user data on input
TEST                  // print out stored user data
or... maybe not?
```

The program between the two defined printf() calls displays the content
of the buffer, which is filled with data entered by the user.

```console
user@dojo-labs ~/owasp/buffer_overflow $ ./example02
So... The End...
TEST123456789
TEST123456789
Segmentation fault
```

Because the size of the buffer was defined (char buf\[8\]) and it was
filled it with thirteen characters of char type, the buffer was
overflowed.

If our binary application is in ELF format, then we are able to use an
objdump program to analyse it and find necessary information to exploit
the buffer overflow error.

Below is output produced by the objdump. From that output we are able to
find addresses, where printf() is called (0x80483d6 and 0x80483e7).

```console
user@dojo-labs ~/owasp/buffer_overflow $ objdump -d ./example02

 080483be <main>:
 80483be:       8d 4c 24 04             lea    0x4(%esp),%ecx
 80483c2:       83 e4 f0                and    $0xfffffff0,%esp
 80483c5:       ff 71 fc                pushl  0xfffffffc(%ecx)
 80483c8:       55                      push   %ebp
 80483c9:       89 e5                   mov    %esp,%ebp
 80483cb:       51                      push   %ecx
 80483cc:       83 ec 04                sub    $0x4,%esp
 80483cf:       c7 04 24 bc 84 04 08    movl   $0x80484bc,(%esp)
 80483d6:       e8 f5 fe ff ff          call   80482d0 <puts@plt>
 80483db:       e8 c0 ff ff ff          call   80483a0 <doit>
 80483e0:       c7 04 24 cd 84 04 08    movl   $0x80484cd,(%esp)
 80483e7:       e8 e4 fe ff ff          call   80482d0 <puts@plt>
 80483ec:       b8 00 00 00 00          mov    $0x0,%eax
 80483f1:       83 c4 04                add    $0x4,%esp
 80483f4:       59                      pop    %ecx
 80483f5:       5d                      pop    %ebp
 80483f6:       8d 61 fc                lea    0xfffffffc(%ecx),%esp
 80483f9:       c3                      ret
 80483fa:       90                      nop
 80483fb:       90                      nop
```

If the second call to printf() would inform the administrator about user
logout (e.g. closed session), then we can try to omit this step and
finish without the call to printf().

```console
user@dojo-labs ~/owasp/buffer_overflow $ perl -e 'print "A"x12
  ."\xf9\x83\x04\x08"' | ./example02
  So... The End...
  AAAAAAAAAAAAu*.
  Segmentation fault
```

The application finished its execution with segmentation fault, but the
second call to printf() had no place.

A few words of explanation:

perl -e 'print "A"x12 ."\\xf9\\x83\\x04\\x08"' - will print out twelve
"A" characters and then four characters, which are in fact an address of
the instruction we want to execute. Why twelve?

```console
   8 // size of buf (char buf[8])
+  4 // four additional bytes for overwriting stack frame pointer
----
  12
```

Problem analysis:

The issue is the same as in the first example. There is no control over
the size of the copied buffer into the previously declared one. In this
example we overwrite the EIP register with address 0x080483f9, which is
in fact a call to ret in the last phase of the program execution.

How to use buffer overflow errors in a different way?

Generally, exploitation of these errors may lead to:

- application DoS
- reordering execution of functions
- code execution (if we are able to inject the shellcode, described in
  the separate document)

How are buffer overflow errors are made?

These kinds of errors are very easy to make. For years they were a
programmer's nightmare. The problem lies in native C functions, which
don't care about doing appropriate buffer length checks. Below is the
list of such functions and, if they exist, their safe equivalents:

- `gets() -\> fgets()` - read characters
- `strcpy() -\> strncpy()` - copy content of the buffer
- `strcat() -\> strncat()` - buffer concatenation
- `sprintf() -\> snprintf()` - fill buffer with data of different types
- `(f)scanf()` - read from STDIN
- `getwd()` - return working directory
- `realpath()` - return absolute (full) path

Use safe equivalent functions, which check the buffers length, whenever
it's possible. Namely:

1.  `gets() -\> fgets()`
2.  `strcpy() -\> strncpy()`
3.  `strcat() -\> strncat()`
4.  `sprintf() -\> snprintf()`

Those functions which don't have safe equivalents should be rewritten
with safe checks implemented. Time spent on that will benefit in the
future. Remember that you have to do it only once.

Use compilers, which are able to identify unsafe functions, logic errors
and check if the memory is overwritten when and where it shouldn't be.

## Related Security Activities

### How to Review Code for Buffer Overflow Vulnerabilities

See the [OWASP Code Review Guide](https://owasp.org/www-project-code-review-guide/)

## References

- [SmashStack](http://insecure.org/stf/smashstack.html)
