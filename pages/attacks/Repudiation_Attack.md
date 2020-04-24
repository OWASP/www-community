---

layout: col-sidebar
title: Repudiation Attack
author: 
contributors: 
permalink: /attacks/Repudiation_Attack
tags: attack, Repudiation Attack
auto-migrated: 1

---

{% include writers.html %}

## Description

A repudiation attack happens when an application or system does not
adopt controls to properly track and log users' actions, thus permitting
malicious manipulation or forging the identification of new actions.
This attack can be used to change the authoring information of actions
executed by a malicious user in order to log wrong data to log files.
Its usage can be extended to general data manipulation in the name of
others, in a similar manner as spoofing mail messages. If this attack
takes place, the data stored on log files can be considered invalid or
misleading.

## Risk Factors

TBD

## Examples

Consider a web application that makes access control and authorization
based on *JSESSIONID*, but registers user actions based on a *user*
parameter defined on the Cookie header, as follows:

` POST http://someserver/Upload_file.jsp HTTP/1.1`
` Host: tequila:8443`
` User-Agent: Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.8.1.4) Gecko/20070515 Firefox/2.0.0.4`
` Accept: text/xml,application/xml,application/xhtml+xml,text/html;q=0.9,text/plain;q=0.8,image/png,*/*;q=0.5`
` Accept-Language: en-us,en;q=0.5`
` Accept-Charset: ISO-8859-1,utf-8;q=0.7,*;q=0.7`
` Keep-Alive: 300`
` Connection: keep-alive`
` Referer: http://someserver/uploads.jsp`
` `**`Cookie:``   ``JSESSIONID=EE3BD1E764CD6EED280426128201131C;``
 ``user=leonardo`**
` Content-Type: multipart/form-data; boundary=---------------------------263152394310685`
` Content-Length: 321`

And the log file is composed by:

`Date, Time, Source IP, Source port, Request, User`

Once user information is acquired from user parameter on HTTP header, a
malicious user could make use of a local proxy (eg:paros) and change it
by a known or unknown username.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [:Category: Authorization](:Category:_Authorization "wikilink")
  - [:Category: Logical Attacks](:Category:_Logical_Attacks "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Web Parameter Tampering](Web_Parameter_Tampering "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category: Input
    Validation](:Category:_Input_Validation "wikilink")
  - [:Category: Access Control
    Vulnerability](:Category:_Access_Control_Vulnerability "wikilink")
  - [:Category: Logging and Auditing
    Vulnerability](:Category:_Logging_and_Auditing_Vulnerability "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category: Logging](:Category:_Logging "wikilink")
  - [:Category: Access Control](:Category:_Access_Control "wikilink")

## References

  - <http://capec.mitre.org/data/definitions/93.html> - Log
    Injection-Tampering-Forging

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Resource
Manipulation](Category:Resource_Manipulation "wikilink")
[Category:Attack](Category:Attack "wikilink")