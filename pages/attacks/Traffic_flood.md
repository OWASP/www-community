---

layout: col-sidebar
title: Traffic flood
author: 
contributors: 
permalink: /attacks/Traffic_flood
tags: attack, Traffic flood
auto-migrated: 1

---

{% include writers.html %}

## Description

Traffic Flood is a type of [DoS](Denial_of_Service "wikilink") attack
targeting web servers. The attack explores the way that the TCP
connection is managed. The attack consists of the generation of a lot of
well-crafted TCP requisitions, with the objective to stop the Web Server
or cause a performance decrease.

The attack explores a characteristic of the HTTP protocol, opening many
connections at the same time to attend a single requisition. This
special feature of the http protocol, which consists of opening a TCP
connection for every html object and closing it, could be used to make
two different kinds of exploitations. The Connect attack is done during
the establishment of the connection, and the Closing attack is done
during the connection closing.

## Examples

### Connect attack

This type of attack consists of establishing a big number of fake TCP
connections with an incomplete HTTP request until the web server is
overwhelmed with connections and stops responding.

The aim of the incomplete HTTP request is to keep the web server, with
the TCP connection in Established state, waiting for the completion of
the request, as shown in figure 1. Depending on the implementation of
the web server, the connection stays in this state until there is a
timeout of the TCP connection or of the web server. In this way it’s
possible to establish a great number of new connections before the first
ones begin to timeout. Moreover, the generation rate of new connections
grows faster than the expiring ones.

<center>

<https://www.owasp.org/images/b/b4/Trafficatual.jpg>

</center>

The attack could also affect a firewall that implements a proxy like
access control as Checkpoint FW1.

### Closing Attack

The Closing Attack is done during the ending steps of a TCP connection,
exploring how some web servers deal with the finalization of the TCP
connection especially with the FIN_WAIT_1 state. The attack, as
explained by Stanislav Shalunov, "comes in two flavors: mbufs exhaustion
and process saturation."

When doing mbufs exhaustion, one wants the user-level process on the
other end to write the data without blocking and closing the descriptor.
The kernel will have to deal with all the data, and the user-level
process will be free, so that more requests can be sent this way and
eventually consume all the mbufs or all physical memory, if mbufs are
allocated dynamically.

When doing process saturation, one wants user-level process to block
while trying to write data. The architecture of many HTTP servers will
allow serving only a certain number of connections at a time. When this
number of connections is reached, the server will stop responding to
legitimate users. If the server doesn't put a bound on the number of
connections, resources will still be tied up and eventually the machine
comes to a crawling halt.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category:Logical Attacks](:Category:Logical_Attacks "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Denial of Service](Denial_of_Service "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:General Logic Error
    Vulnerability](:Category:General_Logic_Error_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - TBD

## References

  - <http://shlang.com/netkill/netkill.html>

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Protocol
Manipulation](Category:Protocol_Manipulation "wikilink")
[Category:Attack](Category:Attack "wikilink")