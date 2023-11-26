---

layout: col-sidebar
title: Reverse Tabnabbing
author: 
contributors: 
permalink: /attacks/Reverse_Tabnabbing
tags: attack, Reverse Tabnabbing
auto-migrated: 1

---

{% include writers.html %}

## Update 2023 - this is fixed in modern, evergreen, browsers 

Links that use `target="_blank"`  now have implicit `rel="noopener"` in 
modern browsers, so this vulnerability isn't as widespread and critical 
as before. This implicit rule is also a part of the 
[HTML standard](https://github.com/whatwg/html/issues/4078).
According to Caniuse.com evergreen browsers support implicit `rel="noopener"` 
from about 2018, but there are still some browsers out there that doesn't support
it, so please consider your userbase when/if deciding to
drop `rel="noopener"`.

Using `rel="noreferrer"` implies also `rel="noopener"`, so if you have 
chosen to use `rel="noreferrer"`, the use of `rel="noopener"` isn't required.

## Description

Reverse tabnabbing is an attack where a page linked from the target page
is able to rewrite that page, for example to replace it with a phishing
site. As the user was originally on the correct page they are less
likely to notice that it has been changed to a phishing site, especially
if the site looks the same as the target. If the user authenticates to
this new page then their credentials (or other sensitive data) are sent
to the phishing site rather than the legitimate one.

As well as the target site being able to overwrite the target page, any
http link can be spoofed to overwrite the target page if the user is on
an unsecured network, for example a public wifi hotspot. The attack is
possible even if the target site is only available via https as the
attacker only needs to spoof the http site that is being linked to.

The attack is typically possible when the source site uses a `target`
instruction in a [html link](https://www.scaler.com/topics/html/html-links/) to specify a [target loading
location](https://www.w3schools.com/tags/att_a_target.asp) that do not
replace the current location and then let the current window/tab
available and does not include any of the preventative measures detailed
below.

The attack is also possible for link opened via the `window.open`
javascript function.

## Overview

### With back link

Link between parent and child pages when prevention attribute is not
used:

![Tabnabbing with back link](../assets/images/TABNABBING_OVERVIEW_WITH_LINK.png)

### Without back link

Link between parent and child pages when prevention attribute is used:

![Tabnabbing without back link](../assets/images/TABNABBING_OVERVIEW_WITHOUT_LINK.png)

## Examples

Vulnerable page:

``` html
<html>
 <body>
  <li><a href="bad.example.com" target="_blank">Vulnerable target using html link to open the new page</a></li>
  <button onclick="window.open('https://bad.example.com')">Vulnerable target using javascript to open the new page</button>
 </body>
</html>
```

Malicious Site that is linked to:

``` html
<html>
 <body>
  <script>
   if (window.opener) {
      window.opener.location = "https://phish.example.com";
   }
  </script>
 </body>
</html>
```

When a user clicks on the **Vulnerable Target** link/button then the
**Malicious Site** is opened in a new tab (as expected) but the target
site in the original tab is replaced by the phishing site.

## Accessible properties

The malicious site can only access to the following properties from the
**opener** javascript object reference (that is in fact a reference to a
**window** javascript class instance) in case of **cross origin** (cross
domains) access:

- `opener.closed`: Returns a boolean value indicating whether a window has been closed or not.
- `opener.frames`: Returns all iframe elements in the current window.
- `opener.length`: Returns the number of iframe elements in the current window.
- `opener.opener`: Returns a reference to the window that created the window.
- `opener.parent`: Returns the parent window of the current window.
- `opener.self`: Returns the current window.
- `opener.top`: Returns the topmost browser window.

If the domains are the same then the malicious site can access all the
properties exposed by the
**[window](https://developer.mozilla.org/en-US/docs/Web/API/Window)** javascript
object reference.

## Prevention

Please check the first heading on this page, Update 2023, as this is now automatically prevented in all modern, evergreen, browsers. 
Check prevention information documented in the [HTML5 Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/HTML5_Security_Cheat_Sheet.html#tabnabbing).

## References

- [WHATWG HTML - Windows opened via `<a target="_blank">` should not have an opener by default](https://github.com/whatwg/html/issues/4078)
- [Caniuse implicit rel="noopener" when using `target="_blank"`](https://caniuse.com/mdn-html_elements_a_implicit_noopener)
- [Chrome Platform Status - Feature: Anchor `target="_blank"` implies `rel="noopener"` by default](https://chromestatus.com/feature/6140064063029248)
- [Chromium - Issue 898942: Anchor `target="_blank"` should imply `rel="noopener"`](https://bugs.chromium.org/p/chromium/issues/detail?id=898942)
- [Mozilla - Make `target="_blank"` on `a`/`area` elements imply `rel="noopener"` by default](https://bugzilla.mozilla.org/show_bug.cgi?id=1522083)
- [WebKit Bugzilla - Bug 190481: Experiment: `target="_blank"` on anchors should imply `rel="noopener"`](https://bugs.webkit.org/show_bug.cgi?id=190481)
- [The `target="_blank"` vulnerability by example](https://dev.to/ben/the-targetblank-vulnerability-by-example)
- [About `rel="noopener"` attribute values](https://mathiasbynens.github.io/rel-noopener/)
- [`target="_blank"` —  the most underestimated vulnerability ever](https://medium.com/@jitbit/target-blank-the-most-underestimated-vulnerability-ever-96e328301f4c)
- Cure53's [Browser Security WhitePaper](https://github.com/cure53/browser-sec-whitepaper/raw/master/browser-security-whitepaper.pdf)
- [Reverse tabnabbing and blackshield demo](https://danielstjules.github.io/blankshield/)
