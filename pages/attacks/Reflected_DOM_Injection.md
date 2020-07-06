---

layout: col-sidebar
title: Reflected DOM Injection
author: 
contributors: 
permalink: /attacks/Reflected_DOM_Injection
tags: attack, Reflected DOM Injection
auto-migrated: 1

---

{% include writers.html %}

Reflected DOM Injection, or *RDI*, is a form of [Stored Cross-Site
Scripting](Cross-site_scripting#Stored_and_Reflected_XSS_Attacks "wikilink").

The outline of the attack is as follows:

1.  Crawler G retrieves data elements from attacker page A and commits
    the content to persisted storage as G\[A\] (e.g., a database row).
2.  End user visits application T. Application T's persisted storage is
    the set of {G}.
3.  End user's interaction with application T results in invocation of
    JavaScript code whereby G\[A\] is retrieved, and due to a failure
    neutralize the content in G\[A\] either prior to its persisted
    storage or during JavaScript execution at page runtime on the DOM,
    G\[A\] is executed as active code instead of being properly
    interpolated as a scalar-like primitive data value or
    closure-guarded object data.

Maturely programmed crawlers often attempt to strip malicious data from
crawled resources prior to persistent storage. Additionally, maturely
programmed applications often utilize output escaping or JavaScript
sandboxing to prevent crawled data from being executed (instead of being
safely rendered). Nonetheless, obfuscation of data on a crawled resource
may sidestep detection algorithms (although obfuscation may hint at an
attempted attack), and reliance strictly on crawler sanitization of
crawled resources may result in stored cross-site scripts executing if
the target JavaScript context does not actively defend against it. In
summary, when the attack is successful, the attack succeeds due to
improper [data validation](Data_Validation "wikilink").

Arshan Dabirsiaghi surmised that vulnerability to this attack would
eventually surface in popular search engines during a presentation at
[OWASP NYC AppSec 2008](OWASP_NYC_AppSec_2008_Conference "wikilink") and
[AppSec Europe 2008](OWASP_AppSec_Europe_2008_-_Belgium "wikilink"),
*Next Generation Cross Site Scripting Worms* (see also *[Building and
Stopping Next Generation XSS Worms
(May 8, 2008)](https://www.owasp.org/images/1/1b/OWASP-AppSecEU08-Dabirsiaghi.pdf)*,
last accessed August 5, 2013). Daniel Chechik and Anat Davidi confirmed
Dabirsiaghi's surmisal by demonstrating such vulnerability in the Google
Translate web application and Yahoo\! cached page results during the DEF
CON 21 security conference in their August 2013 *[Utilizing Popular
Websites for Malicious Purposes Using
RDI](https://defcon.org/html/defcon-21/dc-21-speakers.html#Chechik)*
presentation.

The [DOM-based XSS Prevention Cheat
Sheet](https://cheatsheetseries.owasp.org/cheatsheets/DOM_based_XSS_Prevention_Cheat_Sheet.html) provides
guidance on defense against this attack.

[Category:Attack](Category:Attack "wikilink")