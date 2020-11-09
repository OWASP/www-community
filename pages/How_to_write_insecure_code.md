---

title: How to Write Insecure Code
layout: col-sidebar
author:
contributors: Jeff Williams, KristenS, Jarrod Stenberg, Jesse Ruderman, Shady, Myilmaz, kingthorin
tags:
permalink: /How_to_write_insecure_code

---

{% include writers.html %}

## Introduction

In the interest of ensuring that there will be a future for hackers,
criminals, and others who want to destroy the digital future, this paper
captures tips from the masters on how to create insecure code. With a
little creative use of these tips, you can also ensure your own
financial future. Be careful, you don't want to make your code look
hopelessly insecure, or your insecurity may be uncovered and fixed.

The idea for this article comes from Roedy Green's [How to write
unmaintainable code](http://mindprod.com/jgloss/unmain.html). You may
find the [one page version more
readable](http://thc.org/root/phun/unmaintain.html). Actually, making
your code unmaintainable is a great first step towards making it
insecure and there are some great ideas in this article, particularly
the section on camouflage. Also many thanks to Steven Christey from
MITRE who contributed a bunch of particularly insecure items.

*Special note for the slow to pick up on irony set. This essay is a
**joke**! Developers and architects are often bored with lectures about
how to write **secure** code. Perhaps this is another way to get the
point across.*

## General Principles

- **Avoid the tools**
To ensure an application is forever insecure, you have to think
about how security vulnerabilities are identified and remediated.
Many software teams believe that automated tools can solve their
security problems. So if you want to ensure vulnerabilities, simply
make them difficult for automated tools to find. This is a lot
easier than it sounds. All you have to do is make sure your
vulnerabilities don't match anything in the tool's database of
signatures. Your code can be as complex as you want, so it's pretty
easy to avoid getting found. In fact, most inadvertent
vulnerabilities can't be found by tools anyway.
- **Always use default deny**
Apply the principle of "Default Deny" when building your
application. Deny that your code can ever be broken, deny
vulnerabilities until there's a proven exploit, deny to your
customers that there was ever anything wrong, and above all - deny
responsibility for flaws. Blame the dirty cache buffers.
- **Be a shark**
Always be on the move. Leave security problems to operations staff.

## Complexity

- **Distribute security mechanisms**
Security checks should be designed so that they are as distributed
as possible throughout the codebase. Try not to follow a consistent
pattern and don't make it easy to find all the places where the
mechanism is used. This will virtually ensure that security is
implemented inconsistently.
- **Spread the wealth**
Another great way to avoid being found is to make sure your security
holes aren't located in one place in your code. It's very difficult
for analysts to keep all of your code in their head, so by spreading
out the holes you prevent anyone from finding or understanding them.
- **Use dynamic code**
The single best way to make it difficult for a security analyst (or
security tool for that matter) to follow through an application and
uncover a flaw is to use dynamic code. It can be almost impossible
to trace the flow through code that is loaded at runtime. Features
like reflection and classloading are beautiful features for hiding
vulnerabilities. Enable as many "plugin" points as possible.

## Secure Languages

- **Type safety**
Means anything you enter at the keyboard is secure.
- **Secure languages**
Pick only programming languages that are completely safe and don't
require any security knowledge or special programming to secure.
- **Mix languages**
Different languages have different security rules, so the more
languages you include the more difficult it will be to learn them
all. It's hard enough for development teams to even understand the
security ramifications of one language, much less three or four. You
can use the transitions between languages to hide vulnerabilities
too.

## Trust Relationships

- **Rely on security checks done elsewhere**
It's redundant to do security checks twice, so if someone else says
that they've done a check, there's no point in doing it again. When
possible, it's probably best to just assume that others are doing
security right, and not waste time doing it yourself. Web services
and other service interfaces are generally pretty secure, so don't
bother checking what you send or what they return.
- **Trust insiders**
Malicious input only comes from the Internet, and you can trust that
all the data in your databases is perfectly validated, encoded, and
sanitized for your purposes.
- **Code wants to be free!**
Drop your source code into repositories that are accessible by all
within the company. This also prevents having to email those
hard-coded shared secrets around.

## Logging

- **Use your logs for debugging**
Nobody will be able to trace attacks on your code if you fill up the
logs with debugging nonsense. Extra points for making your log
messages undecipherable by anyone except you. Even more points if
the log messages look as though they might be security relevant.
- **Don't use a logging framework**
The best approach to logging is just to write to stdout, or maybe to
a file. Logging frameworks make the logs too easy to search and
manage to be sure that nobody will ever review them.

## Encryption

- **Build your own encryption scheme**
The standard encryption mechanisms are way too complicated to use.
It's much easier to make up an encryption algorithm that scrambles
up secret stuff. You don't need to bother with a key or anything,
just mix it all up and nobody will figure it out.
- **Hard-code your keys**
Hard-coding is the best way to retain control. This way those pesky
operations folks won't be able to monkey with (they say "rotate")
the keys, and they'll be locked into the source code where only
smart people can understand them. This will also make it easier to
move from environment to environment as the hard-coded key will be
the same everywhere. This in turn means your code is secure
everywhere.
- **Smart coders don't read manuals**
Just keep adding bytes until the algorithm stops throwing
exceptions. Or just save yourself time and cut-and-paste from a
popular coding site. This looks like a good start: `byte[] keyBytes
= new byte[] { 0x00, 0x01, 0x02, 0x03, 0x04, 0x05, 0x06, 0x07,
0x08, 0x09, 0x0a, 0x0b, 0x0c, 0x0d, 0x0e, 0x0f, 0x10, 0x11, 0x12,
0x13, 0x14, 0x15, 0x16, 0x17 };`
- **Pack up your sensitive payload**
If you need to pass things that are sensitive, like passwords or
PII, just pack it up in an encrypted blob. Then just email the key
to the developer who is coding the other side of the transaction,
and punch out early. This will also get you past Data Loss
Prevention (DLP) tools which is a huge bonus.
- **Encryption is hard**
A great way to improve the security posture of your site is to use
client-side JavaScript to encrypt passwords and other sensitive data
that are submitted. This can be used with or without HTTPS
(TLS/SSL). If you use it without HTTPS, you can save some money by
skipping the annual purchase of a signed third party certificate.
- **HTTPS makes your application bullet proof**
If you use HTTPS encryption between your web application endpoint
and the client, there is absolutely no way for anyone to steal any
of the data that is transmitted.

## Authentication

- **Build your own authentication scheme**
Authentication is simple, so just use your common sense and
implement. Don't worry about esoteric stuff you hear about like
session prediction, hashing credentials, brute force attacks, and so
on. Only NSA eggheads could possibly ever figure that stuff out. And
if users want to choose weak passwords, that's their own fault.

**Just use a hash**

Salt is for pigs. Its way too much work to salt and hash passwords.
Besides, only the application can get to the database and hashes are one
way trap doors, so why would you need it?

- **Sessions are inherently secure**
Sessions timeout after 20 minutes, so don't worry about them. You
can put the SESSIONID in the URL, log files, or wherever else you
feel like. What could an attacker do with a SESSIONID anyway? It's
just a bunch of random letters and numbers.
- **Single Sign-On is easy**
If you need to submit a username and password (or other secret
knocks) from one site to another, pack it up in an encrypted blob as
above. This way if anyone finds the blob, they'll have a heck of a
time decrypting it, which is what they'll need to do to be able to
encrypt it again and create the blob themselves.
A one-way hash cannot be decrypted. Therefore, this is a way to take
the latter approach and make it unbreakable.

## Authorization

- **Forget about it**
See
[Authentication](#authentication).
Only ivory tower knuckleheads think there's a difference between
authentication and authorization.
- **Just let your authorization scheme evolve**
It's really hard to figure out all the access control rules for your
application, so use a **just in time** development methodology. This
way you can just code up new rules when you figure them out. If you
end up with hundreds or thousands of lines of authorization code
scattered throughout your application, you're on the right track.
- **Privilege makes code just work**
Using the highest privilege levels makes your product easier to
install and run.
- **Optimize the developer... always**
Each developer, independent of one another, must decide where
authorization decision and enforcement is made.
- **Trust the client**
RIA clients and fat clients that use remote services can make
decisions about what the end-user can or can't see.
- **Volunteer to authorize access to other systems**
When a service you are calling, for example, has inappropriate
access controls just be nice and live with it. After all it will be
your fault when a direct object reference permits any user of your
system to see any data on their service. Should that happen, it will
be a chance for you to show your dedication when you're up at 3 AM
on a Saturday morning sorting out a breach.

## Policy

- **Forget about it**
Policy can't be known until the user requests arrive. Put
authorization logic where you see fit. Sometimes you need to roll it
into the UI. Sometimes it's in the data layer. Sometimes it's both.
See
[Authentication](#authentication).
Only ivory tower knuckleheads think that security requirements can
be known at design time and expressed in a
runtime-readable/declarative format.
- **The tool knows how to do it**
Let your automated tools dictate your security requirements.
Tailoring is for suckers.

## Input Validation

- **Validation is for suckers**
Your application is already protected by a firewall, so you don't
have to worry about attacks in user input. The security *experts*
who keep nagging you are just looking to keep themselves in a job
and know nothing about programming.
- **Let developers validate their way**
Don't bother with a standard way of doing validation, you're just
cramping developer style. To create truly insecure code, you should
try to validate as many different ways as possible, and in as many
different places as possible.
- **Trust the client**
If the client doesn't, by design, produce wacky encoding, for
example, then wacky encoding isn't a threat.

## Documentation

- **If you can build it and it appears to work then why describe
it?**
The most successful applications do not waste time with
requirements, security or otherwise. Optimize the development by
keeping the developers from having to read.
- **Security is just another option**
Assume that your sysadmins will RTFM and change the default settings
you specified in a footnote on page 124.
- **Don't document how security works**
There is no point in writing down all the details of a security
design. If someone wants to figure out if it works, they should
check the code. After all, the code may change and then the
documentation would be useless.
- **Freedom to innovate**
Standards are really just guidelines for you to add your own custom
extensions.
- **Print is dead**
You already know everything about security, what else is there to
learn? Books are for lamers, mailing lists and blogs are for media
whores and FUD-tossing blowhards.

## Coding

- **Most APIs are safe**
Don't waste time poring through documentation for API functions.
It's generally pretty safe to assume that APIs do proper validation,
exception handling, logging, and thread safety.
- **Don't use security patterns**
Make sure there's no standard way of implementing validation,
logging, error handling, etc... on your project. It's best when
developers are left free to express themselves and channel their
inner muse in their code. Avoid establishing any security coding
guidelines, that'll just inhibit creativity.
- **Make sure the build process has lots of steps**
You want to maximize the number of steps in the build process that
have to occur in the right order to make a successful build. It's
best if only one person knows how to actually set up all the config
files and build the distribution. If you do have steps written down,
you should have lots of notes distributed across a bunch of files
and howto's in lots of locations.

## Testing

- **Testing is overrated**
Testing is expensive and time-consuming. Just code and ship
immediately. The market wants your newest release yesterday. If
anything is broken, your loyal users will let you know.
- **Test with a browser**
All you need to test a web application is a browser. That way, you
ensure that your code will work perfectly for all of your legitimate
users. And what do you care if it doesn't work for hackers,
attackers, and criminals? Using a fancy security testing tool like
[Zed Attack Proxy](https://www.zaproxy.org) is a waste of your valuable time.

**Test with only one browser**

After all, they all work the same way and follow standards and never
differ in terms of security.

- **Build test code into every module**
You should build test code throughout the application. That way
you'll have it there in production in case anything goes wrong and
you need to run it.
- **Security warnings are all false alarms**
Everyone knows that security warnings are all false alarms, so you
can safely just ignore them. Why should you waste your valuable time
chasing down possible problems when it's not your money on the line.
If a tool doesn't produce perfect results, then just forget it.

## Libraries

- **Use lots of precompiled libraries**
Libraries are great because you don't have to worry about whether
the code has any security issues. You can trust your business to
just about any old library that you download off the Internet and
include in your application. Don't worry about checking the source
code, it's probably not available and it's too much trouble to
recompile. And it would take way too long to check all that source
code anyway.
- **Don't worry about using the latest version of components**
Just because a library has known vulnerabilities doesn't mean it's
not safe to use. If there's no proof that *my* application is
vulnerable then you're just wasting my time.

## Culture

- "I got a security approval"
So what if it was several years ago, it's basically the same code anyway.
- "Security has to *prove* it before I do anything"
So what if you exploited my application, you cheated by using hacking
- "Hello, this is an internal application, so security doesn't matter"
We have firewalls and stuff

## DevOps

**Automation is enough security**

Forget about integrity, if we have a problem with a node, all we need to
do is kill it and stand another up

**Automated Scanning**

It just creates more garbage nobody is going to read anyways

**Access Control on DevOps systems**

IAM roles and how keys are managed don't matter much, we can just check
them right into GitHub and it'll be lost in a world of anonymity. Hell,
we can even put all our code there so we can just pull it from anywhere.

**Static Analysis**

See automated scanning

**Dynamic Analysis**

See automated scanning

**Dependency checking**

No one would ever think to put a payload in a library, and hey, the
signature on libraries are probably always there.

**Auditing is a waste of money**

There is no reason to check actual configurations written when we are
using playbooks and configuration automation the tell us a node started
out with a good configuration. Why would it ever change? Also see
Automation is enough security

**We'll never lose control of our nodes**

Let's just write that root key down on paper and share it with the team.
Nobody would ever leak it and create a botnet on our dollar.

**CORS**

The cloud is all about sharing! Let's CORS * everything!

**Logging Services**

We're using other peoples infrastructure anyways, why bother with logs
or alerts? It's just a waste of time
