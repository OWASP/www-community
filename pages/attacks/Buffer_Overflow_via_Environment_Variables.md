---

title: Buffer Overflow via Environment Variables
layout: col-sidebar
author:
contributors: Rezos, KristenS, hblankenship, cmvar8, kingthorin
tags: attacks
permalink: /attacks/Buffer_Overflow_via_Environment_Variables

---

{% include writers.html %}

## Description

This attack pattern involves causing a buffer overflow through
manipulation of environment variables. Once the attacker finds that they
can modify an environment variable, they may try to overflow associated
buffers. This attack leverages implicit trust often placed in
environment variables.

The following conditions must be met to conduct successful attack:

- The application uses environment variables.
- The environment variable exposed to the user is vulnerable to a
  buffer overflow.
- The vulnerable environment variable uses untrusted data.
- Tainted data used in the environment variables is not properly
  validated. For instance boundary checking is not done before copying

the input data to a buffer.

The attacker performs the following steps:

- The attacker tries to find an environment variable which can be
  overwritten, by gathering information about the target

host (error pages, software's version number, hostname, etc.).

- The attacker manipulates the environment variable to contain
  excessive-length content to cause a buffer overflow.
- The attacker leverages the buffer overflow to inject maliciously
  crafted code in an attempt to execute privileged command on the
  target environment.

## Examples

**Example1**

The application below gets information about its run environment from
environment variables.

```C
user@dojo-labs ~/owasp/buffer_overflow $ cat bo_env.c
#include <stdio.h>
#include <stdlib.h>

int main(void)
{
       char *ptr_h;
       char h[64];

       ptr_h = getenv("HOME");
       if(ptr_h != NULL) {
               sprintf(h, "Your home directory is: %s !", ptr_h);
               printf("%s\n", h);
       }

       return 0;
}
```

The application checks the value of the environment variable *HOME*
(path to the home directory) and stores it. It is done by calling the
getenv(3) library function in GNU/Linux. If the return value of this
function is different than NULL (NULL value means that variable is not
set), then a message is created by calling sprintf(3). This function
doesn't validate the length of the string, which is going to be written
in the target 64 char size buffer - h\[\].

Common program execution:

```console
user@dojo-labs ~/owasp/buffer_overflow $ ./bo_env
Your home directory is: /home/user !
```

Now let's change the value of HOME to 128 'A' characters.

`user@dojo-labs ~/owasp/buffer_overflow $ export HOME=`perl -e 'print "A"x128'``

When we run program again, a message is copied to the buffer h\[64\],
which has a length of (assuming sizeof(char) = 1):

```console
strlen("Your home directory is:  !") + strlen(ptr_h) = 28 + 128 = 156

user@dojo-labs /home/user/owasp/buffer_overflow $ ./bo_env
Your home directory is:
AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
!
Segmentation fault
user@dojo-labs /home/user/owasp/buffer_overflow $
```

The program ended with memory segmentation fault, and buffer h\[\] was
overwritten. Using environment variables themselves is not a problem.
The real problem is when application lacks their proper validation -
size and content. More information about errors related to buffer
overflows may be found in the
[Buffer_overflow_attack](/attacks/Buffer_overflow_attack) article.

Code injection is performed in the same way as in buffer overflow
attacks with only one difference; the shellcode is placed in environment
variable(s).
