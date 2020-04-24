---

layout: col-sidebar
title: Insecure Compiler Optimization
author: 
contributors: 
permalink: /vulnerabilities/Insecure_Compiler_Optimization
tags: vulnerability, Insecure Compiler Optimization

---

{% include writers.html %}

## Description

Improperly scrubbing sensitive data from memory can compromise security.

Compiler optimization errors occur when:

- Secret data is stored in memory.
- The secret data is scrubbed from memory by overwriting its contents.
- The source code is compiled using an optimizing compiler, which identifies and removes the function that overwrites the contents as a dead store because the memory is not used subsequently.

## Risk Factors

TBD

## Examples

### Example: "Dead store removal"

Memory overwriting code is removed by optimizing compiler, which causes sensitive information left in the memory after its usage.

The following code reads a password from the user, uses the password to connect to a back-end mainframe, and then attempts to scrub the password from memory using `memset()`.

```
     void GetData(char *MFAddr) {
     char pwd[64];
     if (GetPasswordFromUser(pwd, sizeof(pwd))) {
      if (ConnectToMainframe(MFAddr, pwd)) {
              // Interaction with mainframe
         }
       }
       memset(pwd, 0, sizeof(pwd));
    }
```

The code in the example will behave correctly if it is executed verbatim, but if the code is compiled using an optimizing compiler, such as Microsoft Visual C++® .NET or GCC 3.x, then the call to `memset()` will be removed as a dead store because the buffer pwd is not used after its value is overwritten [1]. Because the buffer `pwd` contains a sensitive value, the application may be vulnerable to attack if the data is left memory resident. If attackers are able to access the correct region of memory, they may use the recovered password to gain control of the system.

It is common practice to overwrite sensitive data manipulated in memory, such as passwords or cryptographic keys, in order to prevent attackers from learning system secrets. However, with the advent of optimizing compilers, programs do not always behave as their source code alone would suggest. In the example, the compiler interprets the call to memset() as dead code because the memory being written to is not subsequently used, despite the fact that there is clearly a security motivation for the operation to occur. The problem here is that many compilers, and in fact many programming languages, do not take this and other security concerns into consideration in their efforts to improve efficiency.

Attackers typically exploit this type of vulnerability by using a core dump or runtime mechanism to access the memory used by a particular application and recover the secret information. Once an attacker has access to the secret information, it is relatively straightforward to further exploit the system and possibly compromise other resources with which the application interacts.

## Related [Attacks](../attacks/)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

[1] M. Howard and D. LeBlanc. Writing Secure Code, Second Edition. Microsoft Press, 2003.