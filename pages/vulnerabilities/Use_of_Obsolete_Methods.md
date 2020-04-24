---

layout: col-sidebar
title: Use of Obsolete Methods
author: 
contributors: 
permalink: /vulnerabilities/Use_of_Obsolete_Methods
tags: vulnerability, Use of Obsolete Methods
auto-migrated: 1

---

{% include writers.html %}

# Description

The use of deprecated or obsolete functions may indicate neglected code.

As programming languages evolve, functions occasionally become obsolete
due to:

  - Advances in the language
  - Improved understanding of how operations should be performed
    effectively and securely
  - Changes in the conventions that govern certain operations
  - Functions that are removed are usually replaced by newer
    counterparts that perform the same task in some different and
    hopefully improved way.

Refer to the documentation for this function in order to determine why
it is deprecated or obsolete and to learn about alternative ways to
achieve the same functionality. The remainder of this text discusses
general problems that stem from the use of deprecated or obsolete
functions.

# Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

# Examples

The following code uses the deprecated function getpw() to verify that a
plaintext password matches a user's encrypted password. If the password
is valid, the function sets result to 1; otherwise it is set to 0.

```
   ...
    getpw(uid, pwdline);
    for (i=0; i<3; i++){
        cryptpw=strtok(pwdline, ":");
        pwdline=0;
    }
    result = strcmp(crypt(plainpw,cryptpw), cryptpw) == 0;
    ...
```

Although the code often behaves correctly, using the getpw() function
can be problematic from a security standpoint, because it can overflow
the buffer passed to its second parameter. Because of this
vulnerability, getpw() has been supplanted by getpwuid(), which performs
the same lookup as getpw() but returns a pointer to a
statically-allocated structure to mitigate the risk.

Not all functions are deprecated or replaced because they pose a
security risk. However, the presence of an obsolete function often
indicates that the surrounding code has been neglected and may be in a
state of disrepair. Software security has not been a priority, or even a
consideration, for very long. If the program uses deprecated or obsolete
functions, it raises the probability that there are security problems
lurking nearby.

[Category:Code Quality
Vulnerability](Category:Code_Quality_Vulnerability "wikilink")
[Category:C/C++](Category:C/C++ "wikilink")
[Category:Implementation](Category:Implementation "wikilink")
[Category:Code Snippet](Category:Code_Snippet "wikilink") [Category:Use
of Dangerous API](Category:Use_of_Dangerous_API "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")