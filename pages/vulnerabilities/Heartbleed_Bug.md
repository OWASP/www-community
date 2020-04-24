---

layout: col-sidebar
title: Heartbleed Bug
author: 
contributors: 
permalink: /vulnerabilities/Heartbleed_Bug
tags: vulnerability, Heartbleed Bug

---

{% include writers.html %}

# Introduction

Heartbleed is a catastrophic bug in OpenSSL, announced in April 2014.

![](https://upload.wikimedia.org/wikipedia/commons/archive/d/dc/20140423155152%21Heartbleed.svg)

# About the Name

Like most major vulnerabilities, this major vulnerability is well branded. It gets it's name from the heart beat function between client and server. According to [Dan Kaminsky](https://itunes.apple.com/us/podcast/apm-marketplace-tech-report/id73330855),

>When you are communicating with another computer, sometimes you have a pulse message that says 'yes I'm still here'. This is a heart beat. In this particular case there is the possibility to leak information from the heartbeat, so you don't just know that someone is on the other side, you know something about them. In this case, you know too much. There's a bleeding of information from the heartbeat.

# Timing

**What's known:** The vulnerability became public on April 7, 2014 after being independently discovered by Google Security and Codenomicon. The vulnerability was widely reported on April 9, 2014. The vulnerable versions have been widely used for two years.

> Has this been abused in the wild?

We don't know. Security community should deploy TLS/DTLS honeypots that entrap attackers and to alert about exploitation attempts. According to [Bruce Schneier](https://www.schneier.com/blog/archives/2014/04/heartbleed.html):

> The real question is whether or not someone deliberately inserted this bug into OpenSSL, and has had two years of unfettered access to everything. My guess is accident, but I have no proof." According to EFF, intelligence agencies may have been using heartbleed in November 2013[(source)](https://www.eff.org/deeplinks/2014/04/wild-heart-were-intelligence-agencies-using-heartbleed-november-2013)

# Severity

According to [Bruce Schneier](https://www.schneier.com/blog/archives/2014/04/heartbleed.html), "Catastrophic is the right word. On the scale of 1 to 10, this is an 11." Counterpoint also from Bruce Schneier:

> If nothing really bad happens -- if this turns out to be something like the Y2K bug -- then we are going to face criticisms of crying wolf."

According to [Codenomicon](http://heartbleed.com/):

>There is no total of 64 kilobytes limitation to the attack, that limit applies only to a single heartbeat. Attacker can either keep reconnecting or during an active TLS connection keep requesting arbitrary number of 64 kilobyte chunks of memory content until enough secrets are revealed.

## Session Hijacking with Heartbleed

Matt Sullivan published [an interesting article](https://www.mattslifebytes.com/?p=533) about leveraging Heartbleed for [session hijacking attacks](../attacks/Session_hijacking_attack), including a walkthrough on JIRA [here](https://www.mattslifebytes.com/?p=533).

# Explanation of the Bug

This serious flaw (CVE-2014-0160) is a missing bounds check before a `memcpy()` call that uses non-sanitized user input as the length parameter. An attacker can trick OpenSSL into allocating a 64KB buffer, copy more bytes than is necessary into the buffer, send that buffer back, and thus leak the contents of the victim's memory, 64KB at a time.

TheRegister's [explanation](http://www.theregister.co.uk/2014/04/09/heartbleed_explained/) and [OpenSSL Github Fix](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=96db902)

# The Fix

The patch in OpenSSL 1.0.1g is essentially a bounds check, using the correct record length in the SSL3 structure (`s3->rrec`) that described the incoming HeartbeatMessage.

Below is the revised code from [Github](http://git.openssl.org/gitweb/?p=openssl.git;a=commitdiff;h=731f431497f463f3a2a97236fe0187b11c44aead)

```
hbtype = *p++;
n2s(p, payload);
if (1 + 2 + payload + 16 > s->s3->rrec.length)
  return 0; /* silently discard per RFC 6520 sec. 4 */
pl = p;
```

# Impact of the Vulnerability

This vulnerability allows an attacker to extract memory contents from the webserver through the vulnerability in the heartbeat. As a result an attacker may be able to access sensitive information such as the private keys used for SSL/TLS.

## Active Attack

Equipped with the private key, an attacker can silently monitor and decrypt communications between the user and the web server. As a result, an attacker could view private data such as passwords, credit card data, medical records and any other sensitive data the user exchanges with the website. In addition, the attacker could impersonate the target website to deliver fake, inaccurate or malicious data to the user.

## Offline Attack

Some well funded attackers gather large amounts of encrypted data and store this data in the event they can later decrypt the information. Using the Heartbleed vulnerability the attackers could decrypt this information if it was obtained when passed between a user and a vulnerable website. This means that sensitive data exchanged up to two years ago could also now be at risk for exposure to attackers. Note: sites implementing Perfect Forward Secrecy are protected against this particular attack.

## Scope

1.0.1 and 1.0.2-beta releases of OpenSSL are affected including 1.0.1f and 1.0.2-beta1. Apache, which uses OpenSSL for HTTPS, is used by 66% of all websites according to netcraft.com. A study of the TLS heartbeat extension by Netcraft also identified that 17.5% of SSL sites may be vulnerable to the Heartbleed bug.

# Defending against Vulnerability

## What should website owners do?

Verify if you are using a vulnerable version of OpenSSL. Upgrade OpenSSL as soon as possible. OpenSSL 1.0.1g was released on April 7, 2014 (https://www.openssl.org/source/).

### Reissue your security certificates for SSL/TLS
The vulnerability has been present for two years and there is no way to verify if your private key has been compromised as a result of this vulnerability. In addition, a compromised key would be used to silently monitor communications from your users and the attack would be undetectable. It is prudent to assume a breach and proactively reissue security certificates.

### Implement Perfect Forward Secrecy 
This additional layer of security protects encrypted data from several potential attacks by using a per session random keys.

### Change passwords
If the compromised OpenSSL library had been used to protect login and password information (e.g. like in many cases using SSL for account login pages), this information should be considered compromised. That means that after the library has been upgraded all compromised passwords should be changed. The best way to do this is to inform the users that their password might have been compromised due to this vulnerability and that they should change their password, combined with system of one-time forced change of password after login.

## What should users do? 

Unfortunately there’s not much a user can do. If you have an account at one of the many large websites that may have been affected, you can proactively change your password just to be safe.

According to [Errata Security](http://blog.erratasec.com/2014/04/yes-you-might-have-to-change-your.html#.U0blvq1dWv0), "The only passwords you need to change would be ones that you entered in the last couple of days. Personally, I haven't entered any passwords over the last couple days, so I don't need to change any passwords."

# Exploit POCs

A list of Heartbeat exploit POCs is provided [here](https://blog.bugcrowd.com/heartbleed-exploit-yet/)

# Links for More Information

- Heartbleed page from [Codenomicon](http://heartbleed.com/)
- Test a website's vulnerability [here](http://filippo.io/Heartbleed/)
- [Firefox Plug-in](https://addons.mozilla.org/en-US/firefox/addon/heartbleed-checker/) for user to test website for vulnerability Red=Bad, Green=Good
- Blog post from [Michael Coates](http://blog.shapesecurity.com/heartbleed-bug-places-encrypted-user-data-and-webservers-at-risk)
- [XKCD cartoon](https://xkcd.com/1353)