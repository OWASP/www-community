---

layout: col-sidebar
title: Blind XPath Injection
author: 
contributors:
permalink: /attacks/Blind_XPath_Injection
tags: attack, blind xpath injection, xpath injection

---

{% include writers.html %}

## Description

XPath is a type of query language that describes how to locate specific
elements (including attributes, processing instructions, etc.) in an XML
document. Since it is a query language, XPath is somewhat similar to
Structured Query Language (SQL), however, XPath is different in that it
can be used to reference almost any part of an XML document without
access control restrictions. In SQL, a "user" (which is a term undefined
in the XPath/XML context) may be restricted to certain databases,
tables, columns, or queries. Using an XPATH Injection attack, an
attacker is able to modify the XPATH query to perform an action of their
choosing.

Blind XPath Injection attacks can be used to extract data from an
application that embeds user supplied data in an unsafe way. When input
is not properly sanitized, an attacker can supply valid XPath code that
is executed. This type of attack is used in situations where the
attacker has no knowledge about the structure of the XML document, or
perhaps error message are suppressed, and is only able to pull once
piece of information at a time by asking true/false
questions(booleanized queries), much like [Blind SQL Injection](Blind_SQL_Injection).

For more information, please see the article on regular [XPATH Injection](XPATH_Injection).

## Risk Factors

TBD

## Examples

The attacker may mount a successful attack using two methods:
Boolenization and XML Crawling. By adding to the XPath syntax, the
attacker uses additional expressions (replacing what the attacker
entered in the place of the injection).

### Boolenization

Using the "Boolenization" method the attacker may find out if the given
XPath expression is True or False. Let's assume that the aim of the
attacker is to log in to an account in a web application. A Successful
log in would return "True" and failed log in attempt would return
"False". Only a small portion of the information is targeted via the
analyzed character or number. When the attacker focuses on a string they
may reveal it in its entirety by checking every single character within
the class/range of characters this string belongs to.

Using a `string-length(S)` function, where S is a string, the attacker
may find out the length of this string. With the appropriate number of
`substring(S,N,1)` function iterations, where S is a previously
mentioned string, N is a start character, and "1" is a next character
counting from N character, the attacker is able to enumerate the whole
string.

Code:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<data>
   <user>
   <login>admin</login>
   <password>test</password>
   <realname>SuperUser</realname>
   </user>
   <user>
   <login>rezos</login>
   <password>rezos123</password>
   <realname>Simple User</realname>
   </user>
</data>
```

Function:

- `string.stringlength(//user\[position()=1\]/child::node()\[position()=2\])`
    returns the length of the second string of the first user (8),
- `substring((//user\[position()=1\]/child::node()\[position()=2),1,1)`
    returns the first character of this user ('r').

### XML Crawling

To get to know the XML document structure the attacker may use:

- count(expression)

``` 
count(//user/child::node()
```

This will return the number of nodes (in this case 2).

-  stringlength(string)

``` 
string-length(//user[position()=1]/child::node()[position()=2])=6 
```

Using this query the attacker will find out if the second string
(password) of the first node (user 'admin') consists of 6 characters.

- substring(string, number, number)

```
substring((//user[position()=1]/child::node()[position()=2]),1,1)="a"
```

This query will confirm (True) or deny (False) that the first character
of the user ('admin') password is an "a" character.

If the log in form would look like this:

C\#:

```
String FindUser;
FindUser = "//user[login/text()='" + Request("Username") + "' And
            password/text()='" + Request("Password") + "']";
```

then the attacker should inject the following code:

```
Username: ' or substring((//user[position()=1]/child::node()[position()=2]),1,1)="a" or ''='
```

The XPath syntax may remind you of common [SQL Injection](SQL_Injection) attacks but the attacker must
consider that this language disallows commenting out the rest of
expresssion. To omit this limitation the attacker should use OR
expressions to void all expressions, which may disrupt the attack.

Because of *Boolenization* the number of queries, even within a small
XML document, may be very high (thousands, hundreds of thousands and
more). That is why this attack is not conducted manually. Knowing a few
basic XPath functions, the attacker is able to write an application in a
short time which will rebuild the structure of the document and will
fill it with data by itself.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Blind_SQL_Injection](Blind_SQL_Injection)
- [XPATH_Injection](XPATH_Injection)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

- http://dl.packetstormsecurity.net/papers/bypass/Blind_XPath_Injection_20040518.pdf
  - by Amit Klein (much more detailes, in my opinion the best source about Blind XPath Injection).
- http://projects.webappsec.org/w/page/13247005/XPath%20Injection

