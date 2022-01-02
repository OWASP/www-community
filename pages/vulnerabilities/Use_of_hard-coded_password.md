---

layout: col-sidebar
title: Use of hard-coded password
author: 
contributors: 
permalink: /vulnerabilities/Use_of_hard-coded_password
tags: vulnerability, Use of hard-coded password
auto-migrated: 1

---

{% include writers.html %}

## Description

The use of a hard-coded password increases the possibility of password
guessing tremendously.

**Consequences**

  - Authentication: If hard-coded passwords are used, it is almost
    certain that malicious users will gain access through the account in
    question.

**Exposure period**

  - Design: For both front-end to back-end connections and default
    account settings, alternate decisions must be made at design time.

**Platform**

  - Languages: All
  - Operating platforms: All

**Required resources**

Knowledge of the product or access to code.

**Severity**

High

**Likelihood of exploit**

Very high

The use of a hard-coded password has many negative implications - the
most significant of these being a failure of authentication measures
under certain circumstances.

On many systems, a default administration account exists which is set to
a simple default password which is hard-coded into the program or
device. This hard-coded password is the same for each device or system
of this type and often is not changed or disabled by end users. If a
malicious user comes across a device of this kind, it is a simple matter
of looking up the default password (which is freely available and public
on the internet) and logging in with complete access.

In systems which authenticate with a back-end service, hard-coded
passwords within closed source or drop-in solution systems require that
the back-end service use a password which can be easily discovered.
Client-side systems with hard-coded passwords propose even more of a
threat, since the extraction of a password from a binary is exceedingly
simple.

## Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

## Examples

In C\\C++:

```
int VerifyAdmin(char *password) {

  if (strcmp(password, "Mew!")) {
    printf("Incorrect Password!\n");
    return 0;
  }

  printf("Entering Diagnostic Mode\n");
  return 1;
}
```

In Java:

```java
int verifyAdmin(String password) {

  if (!password.equals("Mew!")) {
    return 0;
  }
  //Diagnostic Mode
  return 1;
}
```

Every instance of this program can be placed into diagnostic mode with
the same password. Even worse is the fact that if this program is
distributed as a binary-only distribution, it is very difficult to
change that password or disable this "functionality."

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - Use of hard-coded cryptographic key
  - Storing passwords in a recoverable format

## Related [Controls](https://owasp.org/www-community/controls/)

  - Design (for default accounts): Rather than hard code a default
    username and password for first time logins, utilize a "first login"
    mode which requires the user to enter a unique strong password.
  - Design (for front-end to back-end connections): Three solutions are
    possible, although none are complete. The first suggestion involves
    the use of generated passwords which are changed automatically and
    must be entered at given time intervals by a system administrator.
    These passwords will be held in memory and only be valid for the
    time intervals. Next, the passwords used should be limited at the
    back end to only performing actions valid to for the front end, as
    opposed to having full access. Finally, the messages sent should be
    tagged and checksummed with time sensitive values so as to prevent
    replay style attacks.

[Category:Vulnerability](Category:Vulnerability "wikilink")
