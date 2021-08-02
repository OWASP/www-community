---

layout: col-sidebar
title: Regular expression Denial of Service - ReDoS
author: Adar Weidman 
contributors: Ebing, Rsl81, Wichers, Bjoern Kimminich, kingthorin, pi3ch
permalink: /attacks/Regular_expression_Denial_of_Service_-_ReDoS
tags: attack, redos, Regular expression Denial of Service - ReDoS

---

{% include writers.html %}

## Introduction

The **Regular expression Denial of Service (ReDoS)** is a [Denial of
Service](Denial_of_Service) attack, that exploits the fact
that most Regular Expression implementations may reach extreme
situations that cause them to work very slowly (exponentially related to
input size). An attacker can then cause a program using a Regular
Expression (Regex) to enter these extreme situations and then hang for a very
long time.

## Description

### The problematic Regex naïve algorithm

The Regex naïve algorithm builds a [Nondeterministic Finite
Automaton
(NFA)](http://en.wikipedia.org/wiki/Nondeterministic_finite_state_machine),
which is a finite state machine where for each pair of state and input
symbol there may be several possible next states. Then the engine starts
to make transition until the end of the input. Since there may be
several possible next states, a deterministic algorithm is used. This
algorithm tries one by one all the possible paths (if needed) until a
match is found (or all the paths are tried and fail).

For example, the Regex pattern or quantifier `^(a+)+$` is represented by the following
NFA:

![Nondeterministic Finite Automaton](../assets/images/attacks/NFA.png)

For the input `aaaaX` there are 16 possible paths in the above
graph. But for `aaaaaaaaaaaaaaaaX` there are 65536 possible paths,
and the number is double for each additional `a`. This is an extreme
case where the naïve algorithm is problematic, because it must pass on
many paths to find a **non-matching input**.

The root-cause of the above example is in a Regex engine feature called **backtracking**.
Simply, if the input (token) fails to match, the engine goes back to
previous positions where it could take a different path.
The engine tries this many times until it explores all possible paths.
In the above example, this feature create a long running loop 
because there were many paths to explore due to inefficient Regex pattern.

Notice, that not all algorithms are naïve, and actually Regex algorithms
can be written in an efficient way. Unfortunately, most Regex engines
today try to solve not only "pure" Regexes, but also "expanded" Regexes
with "special additions", such as back-references that cannot be always
be solved efficiently (see **Patterns for non-regular languages** in
[Wiki-Regex](http://en.wikipedia.org/wiki/Regular_expression) for some
more details). So even if the Regex is not "expanded", a naïve algorithm
is used.

### Evil Regex

A Regex pattern is called **Evil Regex** if it can get stuck on crafted input.

**Evil Regex contains**:

- Grouping with repetition
- Inside the repeated group:
    - Repetition
    - Alternation with overlapping

**Examples of Evil Regex**:

- `(a+)+`
- `([a-zA-Z]+)*`
- `(a|aa)+`
- `(a|a?)+`
- `(.*a){x} for x \> 10`

All the above are susceptible to the input
`aaaaaaaaaaaaaaaaaaaaaaaa!` (The minimum input length might change
slightly, when using faster or slower machines).

### Attacks

The attacker might use the above knowledge to look for applications that
use Regular Expressions, containing an **Evil Regex**, and send a
well-crafted input, that will hang the system. Alternatively, if a Regex
itself is affected by a user input, the attacker can inject an **Evil
Regex**, and make the system vulnerable.

## Risk Factors

The Web is Regex-Based:

![](../assets/images/attacks/RegexBasedWeb.png)

In every layer of the WEB there are Regular Expressions, that might
contain an **Evil Regex**. An attacker can hang a WEB-browser (on a
computer or potentially also on a mobile device), hang a Web Application
Firewall (WAF), attack a database, and even stack a vulnerable WEB
server.

For example, if a programmer uses a Regex to validate the client side of
a system, and the Regex contains an **Evil Regex**, the attacker can
assume the same vulnerable Regex is used in the server side, and send a
well-crafted input, that stacks the WEB server.

## Examples

### Vulnerable Regex in online repositories

1. [ReGexLib,id=1757 (email validation)](http://regexlib.com/REDetails.aspx?regexp_id=1757) - see
bold part, which is an **Evil Regex**

`^([a-zA-Z0-9])`**`(([\-.]|[_]+)?([a-zA-Z0-9]+))*`**`(@){1}[a-z0-9]+[.]{1}(([a-z]{2,3})|([a-z]{2,3}[.]{1}[a-z]{2,3}))$`

Input:

`aaaaaaaaaaaaaaaaaaaaaaaa!`

2. [OWASP Validation Regex Repository](https://wiki.owasp.org/index.php/OWASP_Validation_Regex_Repository), Java
Classname - see bold part, which is an **Evil Regex**

`^`**`(([a-z])+.)+`**`[A-Z]([a-z])+$`

Input:

`aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!`

### Web application attack

- Open a JavaScript
- Find **Evil Regex**
- Craft a malicious input for the found Regex
- Submit a valid value via intercepting proxy
- Change the request to contain a malicious input
- You are done!

### ReDoS via Regex Injection

The following example checks if the username is part of the password
entered by the user.

```
String userName = textBox1.Text;
String password = textBox2.Text;
Regex testPassword = new Regex(userName);
Match match = testPassword.Match(password);
if (match.Success)
{
    MessageBox.Show("Do not include name in password.");
}
else
{
    MessageBox.Show("Good password.");
}
```

If an attacker enters `^(([a-z])+.)+[A-Z]([a-z])+$` as a username
and `aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa!` as a password, the program
will hang.

## References

- [Regular Expression Denial Of Service / Crosby&Wallach, Usenix Security 2003](http://www.cs.rice.edu/~scrosby/hash/slides/USENIX-RegexpWIP.2.ppt)
- [Regular expression Denial of Service Revisited, Sep-2009](http://www.checkmarx.com/NewsDetails.aspx?id=23&cat=3)
- [RegExLib](http://regexlib.com/)
- [ReDOS Attacks: From the Exploitation to the Prevention (in .NET)](https://dzone.com/articles/regular-expressions-denial)
- [Tool for detecting ReDoS vulnerabilities.](http://www.cs.bham.ac.uk/~hxt/research/rxxr.shtml)
- Examples of ReDoS in open source applications:
    - [ReDoS in DataVault](https://nvd.nist.gov/vuln/detail/CVE-2009-3277)
    - [ReDoS in EntLib](https://nvd.nist.gov/vuln/detail/CVE-2009-3275)
    - [ReDoS in NASD CORE.NET Terelik](https://nvd.nist.gov/vuln/detail/CVE-2009-3276)
    - [ReDoS in .NET Framework](http://blog.malerisch.net/2015/09/net-mvc-redos-denial-of-service-vulnerability-cve-2015-2526.html)
    - [ReDoS in Javascript minimatch](https://nodesecurity.io/advisories/118)

[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
