---

layout: col-sidebar
title: String Termination Error
author: 
contributors: 
permalink: /vulnerabilities/String_Termination_Error
tags: vulnerability, String Termination Error
auto-migrated: 1

---

{% include writers.html %}

## Description

Relying on proper string termination may result in a buffer overflow.

String termination errors occur when:

  - Data enters a program via a function that does not null terminate
    its output.
  - The data is passed to a function that requires its input to be null
    terminated.

## Risk Factors

TBD

## Examples

### Example 1

The following code reads from cfgfile and copies the input into inputbuf
using strcpy(). The code mistakenly assumes that inputbuf will always
contain a NULL terminator.

```
    #define MAXLEN 1024
    ...
    char *pathbuf[MAXLEN];
    ...
    read(cfgfile,inputbuf,MAXLEN); //does not null terminate
    strcpy(pathbuf,input_buf); //requires null terminated input
    ...
```

The code in Example 1 will behave correctly if the data read from
cfgfile is null terminated on disk as expected. But if an attacker is
able to modify this input so that it does not contain the expected NULL
character, the call to strcpy() will continue copying from memory until
it encounters an arbitrary NULL character. This will likely overflow the
destination buffer and, if the attacker can control the contents of
memory immediately following inputbuf, can leave the application
susceptible to a buffer overflow attack.

### Example 2

In the following code, readlink() expands the name of a symbolic link
stored in the buffer path so that the buffer filename contains the
absolute path of the file referenced by the symbolic link. The length of
the resulting value is then calculated using strlen().

```
    ...
    char buf[MAXPATH];
    ...
    readlink(path, buf, MAXPATH);
    int length = strlen(filename);
    ...
```

The code in Example 2 will not behave correctly because the value read
into buf by readlink() will not be null terminated. In testing,
vulnerabilities like this one might not be caught because the unused
contents of buf and the memory immediately following it may be NULL,
thereby causing strlen() to appear as if it is behaving correctly.
However, in the wild, strlen() will continue traversing memory until it
encounters an arbitrary NULL character on the stack, which results in a
value of length that is much larger than the size of buf and may cause a
buffer overflow in subsequent uses of this value.

Traditionally, strings are represented as a region of memory containing
data terminated with a NULL character. Older string-handling methods
frequently rely on this NULL character to determine the length of the
string. If a buffer that does not contain a NULL terminator is passed to
one of these functions, the function will read past the end of the
buffer.

Malicious users typically exploit this type of vulnerability by
injecting data with unexpected size or content into the application.
They may provide the malicious input either directly as input to the
program or indirectly by modifying application resources, such as
configuration files. In the event that an attacker causes the
application to read beyond the bounds of a buffer, the attacker may be
able use a resulting buffer overflow to inject and execute arbitrary
code on the system.

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

TBD

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Input Validation
Vulnerability](Category:Input_Validation_Vulnerability "wikilink")
[Category:C/C++](Category:C/C++ "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")