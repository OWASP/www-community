---

title: Injection Theory
layout: col-sidebar
author: Jeff Williams
contributors: Jmanico, kingthorin
tags:
permalink: /Injection_Theory

---

{% include writers.html %}

[Injection](Injection_Flaws) is an attacker's attempt to send
data to an application in a way that will change the meaning of commands
being sent to an interpreter. For example, the most common example is
SQL injection, where an attacker sends "101 OR 1=1" instead of just
"101". When included in a SQL query, this data changes the meaning to
return ALL records instead of just one. There are lots of interpreters
in the typical web environment, such as SQL, LDAP, Operating System,
XPath, XQuery, Expression Language, and many more. Anything with a
"command interface" that combines data into a command is susceptible.
Even XSS is really just a form of HTML injection.

Frequently these interpreters run with a lot of access, so a successful
attack can easily result in significant data breaches, or even loss of
control of a browser, application, or server. Taken together, injection
attacks are a huge percentage of the serious application security risk.
Many organizations have poorly thought through security controls in
place to prevent injection attacks. Vague recommendations for input
validation and output encoding are not going to prevent these flaws.
Instead, we recommend a strong set of controls integrated into your
application frameworks. The goal is to make injections impossible for
developers.

# Why Injection Happens to Good Developers

Injection can be complex. The subtleties of data flow, parsers,
contexts, capabilities, and escaping are overwhelming even for security
specialists. In the following sections we will outline these topics to
make it clear how injection can happen in a variety of different
technologies.

## Untrusted Data

First we need to consider the vehicle for injection attacks -- untrusted
data.

Untrusted data is most often data that comes from the HTTP request, in
the form of URL parameters, form fields, headers, or cookies. But data
that comes from databases, web services, and other sources is frequently
untrusted from a security perspective. That is, untrusted data is input
that can be manipulated to contain a web attack payload. The [OWASP Code
Review Guide](https://wiki.owasp.org/index.php/Category:OWASP_Code_Review_Project) has a decent
list of methods that return untrusted data in various languages, but you
should be careful about your own methods as well.

Untrusted data should always be treated as though it contains an attack.
That means you should not send it **anywhere** without taking steps to
make sure that any attacks are detected and neutralized. As applications
get more and more interconnected, the likelihood of a buried attack
being decoded or executed by a downstream interpreter increases rapidly.

As untrusted data flows through an application, it is frequently split
into parts, combined with safe data, transformed, validated, and encoded
in a variety of ways. A single piece of data could go through dozens of
these steps before it gets to an interpreter. This makes identifying
injection problems very difficult. Tools have a difficult time tracing
the entire data flow and understanding exactly what data can run the
gauntlet and what cannot.

## Injection Context

When untrusted data is used by an application, it is often inserted into
a command, document, or other structure. We will call this the
**injection context**. For example, consider a SQL statement constructed
with `SELECT * FROM users WHERE name='" + request.getParameter( "name"
) + "'";` In this example, the name is data from a potentially hostile
user, and so could contain an attack. But the attack is constrained by
the injection context. In this case, inside single quotes `'`. That's
why single quotes are so important for SQL injection.

Consider a few of the types of commands and documents that might allow
for injection...

- SQL queries
- LDAP queries
- Operating system command interpreters
- Any program invocation
- XML documents
- HTML documents
- JSON structures
- HTTP headers
- File paths
- URLs
- A variety of expression languages
- etc...

In all of these cases, if the attacker can "break out" of the intended
injection context and modify the meaning of the command or document,
they might be able to cause significant harm.

## Parsers

Every interpreter has a parser. Injection attacks target those parsers
-- attempting to trick them into interpreting data as commands.
Understanding how a particular interpreter's parser works is the key to
successful injection attacks -- and, ultimately, the path to creating
defenses against injection.

If you are a student of application security, you should learn as much
as you can about how real parsers work. Learn about grammars, and how to
read BNF. Beware, though, that the grammar may not match the
implementation. Real world parsers have many corner cases and flaws that
may not match the spec. A scientific approach to testing the *real*
behavior of a parser is the best course forward.

TBD. Describe different types of parsers, tokens (particularly control
characters), BNF.

## Injection into References

A "reference" could be a database key, a URL, a filename, or some other
kind of lookup index. While injecting into these references doesn't
typically allow for command execution, it's interesting because the
parsers for these references aren't typically too complicated. However,
URLs and filenames can become quite complex. See the "jar:" scheme for
examples of non-intuitive syntax begging for injection.

TBD. This is for URLs, paths, and other simple forms. Focus on the
parser. Could be as simple as Double.parseDouble (mark of the beast)

## Injection into Commands

TBD. Recursive descent or LALR parsers.

## Injecting in Hierarchical Documents

To really understand what's going on with XSS, you have to consider
injection into the hierarchical structure of the [HTML
DOM](https://www.w3schools.com/whatis/whatis_htmldom.asp). Given a place to
insert data into an HTML document (that is, a place where a developer
has allowed untrusted data to be included in the DOM), there are two
ways to inject code:

- Injecting UP:The most common way is to close the current context and
start a new code context. For example, this is what you do when you
close an HTML attribute with a `"\>` and start a new
`<script>`
tag. This attack closes the original context (going up in the hierarchy)
and then starts a new tag that will allow script code to execute.
Remember that you may be able to skip many layers up in the hierarchy
when trying to break out of your current context. For example, a
`</script>`
tag may be able to terminate a script block even if it is injected
inside a quoted string inside a method call inside the script. This
happens because the HTML parser runs before the JavaScript parser.

- Injecting DOWN:The less common way to perform XSS injection is to
introduce a code subcontext without closing the current context. For
example, if the attacker is able to change
`<img src="...UNTRUSTED DATA HERE..." />` into 
`<img src="<javascript:alert(document.cookie>)" />` they do not have to
break out of the HTML attribute context. Instead, they introduce a
subcontext that allows scripting within the `src` attribute (in this
case a javascript url). Another example is the `expression()`
functionality in CSS properties. Even though you may not be able to
escape a quoted CSS property to inject up, you may be able to
introduce something like
`xss:expression(document.write(document.cookie))` without ever leaving
the current context.

There's also the possibility of injecting directly in the current
context. For example, if you take untrusted input and put it directly
into a JavaScript context. While insane, accepting code from an attacker
is more common than you might think in modern applications. Generally it
is impossible to secure untrusted code with escaping (or anything else).
If you do this, your application is just a conduit for attacker code to
get running in your users' browsers.

The rules in this document have been designed to prevent both UP and
DOWN varieties of XSS injection. To prevent injecting up, you must
escape the characters that would allow you to close the current context
and start a new one. To prevent attacks that jump up several levels in
the DOM hierarchy, you must also escape all the characters that are
significant in all enclosing contexts. To prevent injecting down, you
must escape any characters that can be used to introduce a new
sub-context within the current context.

## Injection with Multiple Nested Parsers

XSS is a form of injection where the interpreter is the browser and
attacks are buried in an HTML document. HTML is easily the worst mashup
of code and data of all time, as there are so many possible places to
put code and so many different valid encodings. HTML is particularly
difficult because it is not only hierarchical, but also contains many
different parsers (XML, HTML, JavaScript, VBScript, CSS, URL, etc...).

TBD

# Defenses

## Validation

Traditionally, input validation has been
the preferred approach for handling untrusted data. However, input
validation is not a great solution for injection attacks. First, input
validation is typically done when the data is received, before the
destination is known. That means that we don't know which characters
might be significant in the target interpreter. Second, and possibly
even more importantly, applications must allow potentially harmful
characters in. For example, should poor Mr. O'Malley be prevented from
registering in the database simply because SQL considers ' a special
character?

While input validation is important and should always be performed, it
is not a complete solution for injection attacks. It's better to think
of input validation as defense in depth
and use of **escaping** as described below as the primary defense.

## Using Safe Interfaces

TBD - parameterized interfaces with strong typing

## Escaping (aka Output Encoding)

"[Escaping](http://www.w3.org/TR/charmod/#sec-Escaping)" is a technique
used to ensure that characters are treated as data, not as characters
that are relevant to the interpreter's parser. There are lots of
different types of escaping, sometimes confusingly called output
"encoding." Some of these techniques define a special "escape"
character, and other techniques have a more sophisticated syntax that
involves several characters.

Do not confuse output escaping with the notion of Unicode character
[encoding](http://www.w3.org/TR/charmod/#sec-Digital), which involves
mapping a Unicode character to a sequence of bits. This level of
encoding is automatically decoded, and does **not** defuse attacks.
However, if there are misunderstandings about the intended charset
between the server and browser, it may cause unintended characters to be
communicated, possibly enabling XSS attacks. This is why it is still
important to [specify](http://www.w3.org/TR/charmod/#sec-Encodings) the
Unicode character encoding (charset), such as UTF-8, for all
communications.

Escaping is the primary means to make sure that untrusted data can't be
used to convey an injection attack. There is **no harm** in escaping
data properly - it will still render in the browser properly. Escaping
simply lets the interpreter know that the data is not intended to be
executed, and therefore prevents attacks from working.
