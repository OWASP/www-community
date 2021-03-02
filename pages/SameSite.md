---
title: SameSite
layout: col-sidebar
author: Riramar, Pawel Krawczyk
contributors: Neil Smithline, Dirk Wetter, Ayesh
permalink: /SameSite
---

{% include writers.html %}

## Overview
SameSite prevents the browser from sending this cookie along with cross-site requests. 
The main goal is to mitigate the risk of cross-origin information leakage. It also provides some protection against cross-site request forgery attacks. 
Possible values for the flag are `none`, `lax`, or `strict`.

The `strict` value will prevent the cookie from being sent by the browser to the target site in all cross-site browsing contexts, even when following a regular link. 
For example, for a GitHub-like website this would mean that if a logged-in user follows a link to a private GitHub project posted on a corporate discussion forum or email, 
GitHub will not receive the session cookie and the user will not be able to access the project.

A bank website however most likely doesn't want to allow any transactional pages to be linked from external sites so the strict flag would be most appropriate here.

The `lax` value provides a reasonable balance between security and usability for websites that want to maintain user's logged-in session 
after the user arrives from an external link. In the above GitHub scenario, the session cookie would be allowed when following a regular link 
from an external website while blocking it in CSRF-prone request methods (e.g. POST).

The `none` value won't give any kind of protection. The browser attaches the cookies in all cross-site browsing contexts.

The default value of the SameSite attribute differs with each browser, therefore it is advised to explicitly set the value of the attribute.

As of November 2017 the SameSite attribute is implemented in Chrome, Firefox, and Opera. Since version 12.1 Safari also supports this. Windows 7 
with IE 11 lacks support as of December 2018, see caniuse.com below.

## References
- https://tools.ietf.org/html/draft-west-first-party-cookies-07
- https://caniuse.com/#search=samesite
- http://www.sjoerdlangkemper.nl/2016/04/14/preventing-csrf-with-samesite-cookie-attribute/
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie/SameSite
