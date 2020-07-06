---

layout: col-sidebar
title: XPATH Injection
author: 
contributors: 
permalink: /attacks/XPATH_Injection
tags: attack, XPATH Injection
auto-migrated: 1

---

{% include writers.html %}

## Description

Similar to [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection), XPath Injection
attacks occur when a web site uses user-supplied information to
construct an XPath query for XML data. By sending intentionally
malformed information into the web site, an attacker can find out how
the XML data is structured, or access data that they may not normally have
access to. They may even be able to elevate their privileges on the web site
if the XML data is being used for authentication (such as an XML based
user file).

Querying XML is done with XPath, a type of simple descriptive statement
that allows the XML query to locate a piece of information. Like SQL,
you can specify certain attributes to find, and patterns to match. When
using XML for a web site it is common to accept some form of input on
the query string to identify the content to locate and display on the
page. This input **must** be sanitized to verify that it doesn't mess up
the XPath query and return the wrong data.

XPath is a standard language; its notation/syntax is always
implementation independent, which means the attack may be automated.
There are no different dialects as it takes place in requests to the SQL
databases.

Because there is no level access control it's possible to get the entire
document. We won't encounter any limitations as we may know from SQL
injection attacks.

## Example Vulnerability

We'll use this XML snippet for the examples.

    <?xml version="1.0" encoding="utf-8"?>
    <Employees>
       <Employee ID="1">
          <FirstName>Arnold</FirstName>
          <LastName>Baker</LastName>
          <UserName>ABaker</UserName>
          <Password>SoSecret</Password>
          <Type>Admin</Type>
       </Employee>
       <Employee ID="2">
          <FirstName>Peter</FirstName>
          <LastName>Pan</LastName>
          <UserName>PPan</UserName>
          <Password>NotTelling</Password>
          <Type>User</Type>
       </Employee>
    </Employees>

Suppose we have a user authentication system on a web page that used a
data file of this sort to login users. Once a username and password have
been supplied the software might use XPath to look up the user:

    VB:
    Dim FindUserXPath as String
    FindUserXPath = "//Employee[UserName/text()='" & Request("Username") & "' And
            Password/text()='" & Request("Password") & "']"

    C#:
    String FindUserXPath;
    FindUserXPath = "//Employee[UserName/text()='" + Request("Username") + "' And
            Password/text()='" + Request("Password") + "']";

With a normal username and password this XPath would work, but an
attacker may send a bad username and password and get an XML node
selected without knowing the username or password, like this:

    Username: blah' or 1=1 or 'a'='a
    Password: blah

    FindUserXPath becomes //Employee[UserName/text()='blah' or 1=1 or
            'a'='a' And Password/text()='blah']

    Logically this is equivalent to:
            //Employee[(UserName/text()='blah' or 1=1) or
            ('a'='a' And Password/text()='blah')]

In this case, only the first part of the XPath needs to be true. The
password part becomes irrelevant, and the UserName part will match ALL
employees because of the "1=1" part.

## XPath Injection Defenses

Just like the techniques to avoid SQL injection, you need to use a
parameterized XPath interface if one is available, or escape the user
input to make it safe to include in a dynamically constructed query. If
you are using quotes to terminate untrusted input in a dynamically
constructed XPath query, then you need to escape that quote in the
untrusted input to ensure the untrusted data can't try to break out of
that quoted context. In the following example, single quotes (') are
used to terminate the Username and Password parameters. So, we need to
replace any ' characters in this input with the XML encoded version of
that character, which is "'".

    VB:
    Dim FindUserXPath as String
    FindUserXPath = "//Employee[UserName/text()='" & Request("Username").Replace("'", "&apos;") & "' And
            Password/text()='" & Request("Password").Replace("'", "&apos;") & "']"

    C#:
    String FindUserXPath;
    FindUserXPath = "//Employee[UserName/text()='" + Request("Username").Replace("'", "&apos;") + "' And
            Password/text()='" + Request("Password").Replace("'", "&apos;") + "']";

Another <strong>better</strong> mitigation option is to use a
precompiled XPath[1](http://www.tkachenko.com/blog/archives/000385.html)
query. Precompiled XPath queries are already preset before the program
executes, rather than created on the fly <strong>after</strong> the
user's input has been added to the string. This is a better route
because you don't have to worry about missing a character that should
have been escaped.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [Command Injection](Command_Injection "wikilink")
  - [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
  - [LDAP injection](LDAP_injection "wikilink")
  - [Server-Side_Includes_%28SSI%29_Injection](https://owasp.org/www-community/attacks/Server-Side_Includes_(SSI)_Injection)

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Blind_SQL_Injection](Blind_SQL_Injection "wikilink")
  - [Blind_XPath_Injection](https://owasp.org/www-community/attacks/Blind_XPath_Injection)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input Validation
    Vulnerability](:Category:_Input_Validation_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")
  - [Input Validation](Input_Validation "wikilink")

Just like SQL injection, in order to protect yourself you must escape
single quotes (or double quotes) if your application uses them.

VB:

    Dim FindUserXPath as String
    FindUserXPath = "//Employee[UserName/text()='" &
    Request("Username").Replace("'", "&apos;") & "' And
           Password/text()='" & Request("Password").Replace("'", "&apos;") & "']"

C\#:

    String FindUserXPath;
    FindUserXPath = "//Employee[UserName/text()='" +
    Request("Username").Replace("'", "&apos;") + "' And
           Password/text()='" + Request("Password").Replace("'", "&apos;") + "']";

Another better mitigation option is to use a precompiled XPath\[1\].
Precompiled XPaths are already preset before the program executes,
rather than created on the fly after the user's input has been added to
the string. This is a better route because you don't have to worry about
missing a character that should have been escaped.

Use of parameterized XPath queries - Parameterization causes the input
to be restricted to certain domains, such as strings or integers, and
any input outside such domains is considered invalid and the query
fails.

Use of custom error pages - Attackers can glean information about the
nature of queries from descriptive error messages. Input validation must
be coupled with customized error pages that inform about an error
without disclosing information about the database or application.

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category: Injection](Category:_Injection "wikilink")
[Category:Attack](Category:Attack "wikilink") [Category:Injection
Attack](Category:Injection_Attack "wikilink")