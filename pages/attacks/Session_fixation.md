---

layout: col-sidebar
title: Session fixation
author: 
contributors: 
permalink: /attacks/Session_fixation
tags: attack, Session fixation
auto-migrated: 1

---

{% include writers.html %}

## Description

Session Fixation is an attack that permits an attacker to hijack a valid
user session. The attack explores a limitation in the way the web
application manages the session ID, more specifically the vulnerable web
application. When authenticating a user, it doesn’t assign a new session
ID, making it possible to use an existent session ID. The attack
consists of obtaining a valid session ID (e.g. by connecting to the
application), inducing a user to authenticate himself with that session
ID, and then hijacking the user-validated session by the knowledge of
the used session ID. The attacker has to provide a legitimate Web
application session ID and try to make the victim's browser use it.

The session fixation attack is not a class of [Session
Hijacking](Session_hijacking_attack), which steals the
established session between the client and the Web Server after the user
logs in. Instead, the Session Fixation attack fixes an established
session on the victim's browser, so the attack starts before the user
logs in.

There are several techniques to execute the attack; it depends on how
the Web application deals with session tokens. Below are some of the
most common techniques:

**• Session token in the URL argument:** The Session ID is sent to the
victim in a hyperlink and the victim accesses the site through the
malicious URL.

**• Session token in a hidden form field:** In this method, the victim
must be tricked to authenticate in the target Web Server, using a login
form developed for the attacker. The form could be hosted in the evil
web server or directly in html formatted e-mail.

**• Session ID in a cookie:**

o Client-side script

Most browsers support the execution of client-side scripting. In this
case, the aggressor could use attacks of code injection as the
[XSS](Cross-site_Scripting_\(XSS\) "wikilink") (Cross-site scripting)
attack to insert a malicious code in the hyperlink sent to the victim
and fix a Session ID in its cookie. Using the function document.cookie,
the browser which executes the command becomes capable of fixing values
inside of the cookie that it will use to keep a session between the
client and the Web Application.

o
```
<META>

tag

<META>
```
tag also is considered a code injection attack, however, different from
the XSS attack where undesirable scripts can be disabled, or the
execution can be denied. The attack using this method becomes much more
efficient because it's impossible to disable the processing of these
tags in the browsers.

o HTTP header response

This method explores the server response to fix the Session ID in the
victim's browser. Including the parameter Set-Cookie in the HTTP header
response, the attacker is able to insert the value of Session ID in the
cookie and sends it to the victim's browser.

## Examples

### Example 1

The example below explains a simple form, the process of the attack, and
the expected results.

(1)The attacker has to establish a legitimate connection with the web
server which (2) issues a session ID or, the attacker can create a new
session with the proposed session ID, then, (3) the attacker has to send
a link with the established session ID to the victim, they have to click
on the link sent from the attacker accessing the site, (4) the Web
Server saw that session was already established and a new one need not
to be created, (5) the victim provides their credentials to the Web
Server, (6) knowing the session ID, the attacker can access the user's
account.

<center>

<https://www.owasp.org/images/9/9c/Fixation.jpg>

Figure 1. Simple example of Session Fixation attack.

</center>

### Example 2

Client-side scripting

The processes for the attack using the execution of scripts in the
victim's browser are very similar to example 1, however, in this case,
the Session ID does not appear as an argument of the URL, but inside of
the cookie. To fix the value of the Session ID in the victim's cookie,
the attacker could insert a JavaScript code in the URL that will be
executed in the victim's browser.

` http://website.kom/<script>document.cookie=”sessionid=abcd”;</script>`

### Example 3
```
<META>

tag
```
As well as client-side scripting, the code injection must be made in the
URL that will be sent to the victim.

`http://website.kon/<meta http-equiv=Set-Cookie content=”sessionid=abcd”>`

### Example 4

HTTP header response

The insertion of the value of the SessionID into the cookie manipulating
the server response can be made, intercepting the packages exchanged
between the client and the Web Application inserting the Set-Cookie
parameter.

<center>

<https://www.owasp.org/images/e/ed/Fixation2.jpg>

Figure 2. Set-Cookie in the HTTP header response

</center>

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Authorization](:Category:Authorization "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [XSS Attacks](XSS_Attacks "wikilink")
  - [Session hijacking attack](Session_hijacking_attack "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:Session Management
    Vulnerability](:Category:Session_Management_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Session Fixation
    Protection](Session_Fixation_Protection "wikilink")

## References

  - <http://www.acros.si/papers/session_fixation.pdf>
  - <http://en.wikipedia.org/wiki/Session_fixation>
  - <http://www.derkeiler.com/pdf/Mailing-Lists/Securiteam/2002-12/0099.pdf>

## Categories

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Exploitation of
Authentication](Category:Exploitation_of_Authentication "wikilink")
[Category:Attack](Category:Attack "wikilink")
