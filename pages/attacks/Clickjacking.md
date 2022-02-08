---

title: Clickjacking
layout: col-sidebar
author: Gustav Rydstedt 
contributors: Wichers, Jmanico, MichaelCoates, Till Maas, Ajay, Michael Monsivais, Arun Kumar V, Abhinav, Neil Smithline, kingthorin, Shai Alon
permalink: /attacks/Clickjacking
tags: attack, clickjacking

---

{% include writers.html %}

Clickjacking, also known as a "UI redress attack", is when an attacker
uses multiple transparent or opaque layers to trick a user into clicking
on a button or link on another page when they were intending to click on
the top level page. Thus, the attacker is "hijacking" clicks meant
for their page and routing them to another page, most likely owned by
another application, domain, or both.

Using a similar technique, keystrokes can also be hijacked. With a
carefully crafted combination of stylesheets, iframes, and text boxes, a
user can be led to believe they are typing in the password to their
email or bank account, but are instead typing into an invisible frame
controlled by the attacker.

# Examples

For example, imagine an attacker who builds a web site that has a button
on it that says "click here for a free iPod". However, on top of that
web page, the attacker has loaded an iframe with your mail account, and
lined up exactly the "delete all messages" button directly on top of the
"free iPod" button. The victim tries to click on the "free iPod" button
but instead actually clicked on the invisible "delete all messages"
button. In essence, the attacker has "hijacked" the user's click, hence
the name "Clickjacking".

One of the most notorious examples of Clickjacking was an attack against
the [Adobe Flash plugin settings
page](http://www.macromedia.com/support/documentation/en/flashplayer/help/settings_manager06.html).
By loading this page into an invisible iframe, an attacker could trick a
user into altering the security settings of Flash, giving permission for
any Flash animation to utilize the computer's microphone and camera.

Clickjacking also made the news in the form of a [Twitter
worm](http://shiflett.org/blog/2009/feb/twitter-dont-click-exploit).
This clickjacking attack convinced users to click on a button which
caused them to re-tweet the location of the malicious page, and
propagated massively.

There have also been clickjacking attacks abusing Facebook's "Like"
functionality. [Attackers can trick logged-in Facebook users to
arbitrarily like fan pages, links, groups,
etc](http://threatpost.com/en_us/blogs/facebook-jacking-scams-expand-060310)

# Defending against Clickjacking

There are three main ways to prevent clickjacking:

1.  Sending the proper Content Security Policy (CSP) frame-ancestors directive response headers that instruct the browser to not allow framing from other domains. The older `X-Frame-Options` HTTP headers is used for graceful degradation and older browser compatibility.
2. Properly setting authentication cookies with `SameSite=Strict` (or `Lax`), unless they explicitly need `None` (which is rare).
3. Employing defensive code in the UI to ensure that the current frame is the most top level window.

For more information on Clickjacking defense, please see the the [Clickjacking Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html).

# References
- [Why am I anxious about Clickjacking?](https://www.linkedin.com/pulse/20141202104842-120953718-why-am-i-anxious-about-clickjacking)
- A Basic understanding of Clickjacking Attack
- <https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors>
- Mozilla developer resource on Content-Security-Policy frame-ancestors response header.
- <https://developer.mozilla.org/en-US/docs/The_X-FRAME-OPTIONS_response_header>
- Mozilla developer resource on the X-Frame-Options response header.
- [Busting Frame Busting: A study of clickjacking vulnerabilities on top sites](http://w2spconf.com/2010/papers/p27.pdf)
- A study by the Stanford Web Security Group outlining problems with deployed frame busting code.
- [Clickjacking, Sec Theory](http://www.sectheory.com/clickjacking.htm)
- A paper by Robert Hansen defining the term, its implications against Flash at the time of writing, and a disclosure timeline.
- <https://www.codemagi.com/blog/post/194>
- Framebreaking defense for legacy browsers that do not support X-Frame-Option headers.
- A simple J2EE servlet filter that sends anti-framing headers to the browser.
- [CSP frame-ancestors vs. X-Frame-Options for Clickjacking prevention](https://medium.com/@shaialon/csp-frame-ancestors-vs-x-frame-options-for-clickjacking-prevention-30383a713772)
