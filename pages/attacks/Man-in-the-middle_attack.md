---

layout: col-sidebar
title: Man-in-the-middle attack
author: 
contributors: 
permalink: /attacks/Man-in-the-middle_attack
tags: attack, Man-in-the-middle attack
auto-migrated: 1

---



Last revision (mm/dd/yy): **//**

## Description

The man-in-the middle attack intercepts a communication between two
systems. For example, in an http transaction the target is the TCP
connection between client and server. Using different techniques, the
attacker splits the original TCP connection into 2 new connections, one
between the client and the attacker and the other between the attacker
and the server, as shown in figure 1. Once the TCP connection is
intercepted, the attacker acts as a proxy, being able to read, insert
and modify the data in the intercepted communication.

The MITM attack is very effective because of the nature of the http
protocol and data transfer which are all ASCII based. In this way, it’s
possible to view and interview within the http protocol and also in the
data transferred. So, for example, it’s possible to capture a session
cookie reading the http header, but it’s also possible to change an
amount of money transaction inside the application context, as shown in
figure 2.

<center>

![Image:request.JPG](request.JPG "Image:request.JPG")

Figure 2. Illustration of a HTTP Packet intercepted with Paros Proxy.

</center>

The MITM attack could also be done over an https connection by using the
same technique; the only difference consists in the establishment of two
independent SSL sessions, one over each TCP connection. The browser sets
a SSL connection with the attacker, and the attacker establishes another
SSL connection with the web server. In general the browser warns the
user that the digital certificate used is not valid, but the user may
ignore the warning because he doesn’t understand the threat. In some
specific contexts it’s possible that the warning doesn’t appear, as for
example, when the Server certificate is compromised by the attacker or
when the attacker certificate is signed by a trusted CA and the CN is
the same of the original web site.

MITM is not only an attack technique, but is also usually used during
the development step of a web application or is still used for Web
Vulnerability assessments.

### MITM Attack tools

There are several tools to realize a MITM attack. These tools are
particularly efficient in LAN network environments, because they
implement extra functionalities, like the arp spoof capabilities that
permit the interception of communication between hosts.

  - PacketCreator
  - Ettercap
  - Dsniff
  - Cain e Abel

### MITM Proxy only tools

Proxy tools only permit interactiion with the parts of the HTTP
protocol, like the header and the body of a transaction, but do not have
the capability to intercept the TCP connection between client and
server. To intercept the communication, it’s necessary to use other
network attack tools or configure the browser.

  - [OWASP WebScarab](OWASP_WebScarab "wikilink")
  - Paros Proxy
  - Burp Proxy
  - ProxyFuzz
  - Odysseus Proxy
  - Fiddler (by Microsoft)

## Examples

TBD

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Authentication](:Category:Authentication "wikilink")
  - [:Category:Client-side
    Attacks](:Category:Client-side_Attacks "wikilink")

## Related [Attacks](Attacks "wikilink")

  - [Man-in-the-browser_attack](Man-in-the-browser_attack "wikilink")

## Related [Vulnerabilities](Vulnerabilities "wikilink")

  - [:Category:Session Management
    Vulnerability](:Category:Session_Management_Vulnerability "wikilink")

## Related [Controls](Controls "wikilink")

  - [Session Management](Session_Management "wikilink")

## References

  - <http://www.sans.org/reading_room/whitepapers/threats/480.php>
  - <http://cwe.mitre.org/data/definitions/300.html>
  - <http://resources.infosecinstitute.com/video-man-in-the-middle-howto/>
  - <http://en.wikipedia.org/wiki/Man-in-the-middle_attack>

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[could these all be links?](Category:FIXME "wikilink") [could these all
be links?](Category:FIXME "wikilink") [these aren't threat
agents](Category:FIXME "wikilink")
[Category:Spoofing](Category:Spoofing "wikilink")
[Category:Attack](Category:Attack "wikilink")