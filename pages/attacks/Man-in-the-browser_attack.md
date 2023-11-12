---

layout: col-sidebar
title: Man-in-the-browser attack
author: 
contributors: kingthorin, meeque
permalink: /attacks/Man-in-the-browser_attack
tags: attack, Man-in-the-browser attack
auto-migrated: 1

---

{% include writers.html %}

## Description

The Man-in-the-Browser attack is the same approach as [Manipulator-in-the-middle
attack](Manipulator-in-the-middle_attack), but in this case a [Trojan
Horse](Trojan_Horse "wikilink") is used to intercept and manipulate
calls between the main application’s executable (ex: the browser) and
its security mechanisms or libraries on-the-fly.

The most common objective of this attack is to cause financial fraud by
manipulating transactions of Internet Banking systems, even when other
authentication factors are in use.

A previously installed Trojan horse is used to act between the browser
and the browser’s security mechanism, sniffing or modifying transactions
as they are formed on the browser, but still displaying back the user's
intended transaction.

Normally, the victim must be smart in order to notice a signal of such
attack while they are accessing a web application like an internet banking
account, even in presence of SSL channels, because all expected controls
and security mechanisms are displayed and work normally.

Points of effect:

  - **Browser Helper Objects** – dynamically-loaded libraries loaded by
    Internet Explorer upon startup
  - **Extensions** – the equivalent to Browser Helper Objects for
    Firefox Browser
  - **API-Hooking** – this is the technique used by Man-in-the-Browser
    to perform its Man-in-the-Middle between the executable application
    (EXE) and its libraries (DLL).
  - **Javascript** – By using a malicious Ajax worm, as described on
    [Ajax Sniffer - Proof of
    Concept](http://myappsecurity.blogspot.com/2007/01/ajax-sniffer-prrof-of-concept.html)

## Risk Factors

TBD

## Examples

### Manipulation thru DOM interface

In order to perform this attack, an attacker may progress thru the
following steps:

1.  The Trojan infects the computer's software, either OS or
    Application.
2.  The Trojan installs an extension into the browser configuration, so
    that it will be loaded next time the browser starts.
3.  At some later time, the user restarts the browser.
4.  The browser loads the extension.
5.  The extension registers a handler for every page-load.
6.  Whenever a page is loaded, the URL of the page is searched by the
    extension against a list of known sites targeted for attack.
7.  The user logs in securely on to for example
    https://secure.original.site/.
8.  When the handler detects a page-load for a specific pattern in its
    targeted list (for example
    https://secure.original.site/account/do_transaction) it registers a
    button event handler.
9.  When the submit button is pressed, the extension extracts all data
    from all form fields through the DOM interface in the browser, and
    remembers the values.
10. The extension modifies the values through the DOM interface.
11. The extension tells the browser to continue to submit the form to
    the server.
12. The browser sends the form, including the modified values, to the
    server.
13. The server receives the modified values in the form as a normal
    request. The server cannot differentiate between the original values
    and the modified values, or detect the changes.
14. The server performs the transaction and generates a receipt.
15. The browser receives the receipt for the modified transaction.
16. The extension detects the
    https://secure.original.site/account/receipt URL, scans the HTML for
    the receipt fields, and replaces the modified data in the receipt
    with the original data that it remembered in the HTML.
17. The browser displays the modified receipt with the original details.
18. The user thinks that the original transaction was received by the
    server intact and authorized correctly.

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [Manipulator-in-the-middle attack](Manipulator-in-the-middle_attack)

## References

  - <http://events.ccc.de/congress/2006/Fahrplan/attachments/1158-Subverting_Ajax.pdf>
    - Stefano di Paola and Giorgio Fedon, Subverting Ajax, Dec, 2006.
