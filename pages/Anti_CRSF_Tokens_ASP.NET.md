---

title: Anti CSRF Tokens ASP.NET
layout: col-sidebar
author:
contributors: kingthorin
tags:
permalink: /Anti_CRSF_Tokens_ASP-NET

---

{% include writers.html %}

# Description

CSRF abuses the **trust** relationship between **browser and
server**. This means that anything that a server uses in order to
establish trust with a browser (e.g., cookies, but also HTTP/Windows
Authentication) is exactly what allows CSRF to take place. This is
only the first piece for a successful CSRF attack, however.

The second piece is a web form or request containing parameters that are:
**predictable** enough an attacker could craft their own malicious
form/request which, in turn, would be successfully accepted by the
target service. Then, usually through social engineering or XSS, the
victim would trigger that malicious form/request submission **while
authenticated** to the legitimate service. This is where the
browser/server trust is exploited.

In order to prevent CSRF in ASP.NET, anti-forgery tokens (also known as
request verification tokens) must be utilized.

These tokens are randomly-generated values included in any
form/request that warrants protection. Note that this value should be
unique for every session. This guarantees that every
form/request is tied to the authenticated user and, therefore, protected
from CSRF.

**Important**: non-[idempotent](https://www.wordnik.com/words/idempotent) GET requests
represent an anti-pattern where CSRF protection is concerned. Always use
POST requests with anti-CSRF tokens for proper protection.

# Mitigation Examples

Please note that the following examples may not entail a complete
anti-CSRF solution for any given Web application. Specific requirements
may call for adjustments and/or combinations of different strategies.

## Solutions NOT considered secure

- All of the solutions provided in this article are not designed to
work with GET requests that change the server state (e.g.,
/example/delete.aspx?id=1). GET requests should be
[idempotent](https://www.wordnik.com/words/idempotent) so that CSRF
cannot take place.

- Assuming that SSL/TLS will thwart CSRF attacks just because the
cookie is marked "Secure" and/or "HTTPOnly". The problem lies in the
trust between legitimate browser and server. Therefore, the browser will
just send its current cookies when the forged request is triggered. The
attacker never has to touch any cookies.

- Referer header verification as the only protection. This can be
easily manipulated.

- Cookie double-submission when the cookie utilized is the session
cookie. This exposes the session cookie to JavaScript. Always mark the
session cookie "HTTPOnly" so that it cannot be accessed with JavaScript.

- Any CSRF protection is null and void given the presence of XSS, for
several reasons. The main and obvious reason is that, through XSS, the
attacker can hijack the session and spoof the user, not even having to
worry about performing CSRF.

## ASP.NET MVC and Web API: Anti-CSRF Token

ASP.NET has the capability to generate anti-CSRF security tokens for
consumption by your application, as such:

1) Authenticated user (has session which is managed by the framework)
requests a page which contains form(s) that changes the server state
(e.g., user options, account transfer, file upload, admin functions,
etc.)

2) Generate the security token (or grab it from the session state) and
send the token as a session cookie (again, managed in the session state,
unique per session) **as well as within a hidden value in each form**.

3) Once the user submits the form, validate the token stored in the
session state against the token included in the submitted form value. On
failure, disregard form.

Effectively, this is the cookie double-submission approach done right,
since the security token is submitted both as a cookie (managed in the
framework session state) and within a hidden form value at the same
time.

For implementation details, see:
- [MVC CSRF Prevention (official ASP.NET blog)](http://www.asp.net/mvc/overview/security/xsrfcsrf-prevention-in-aspnet-mvc-and-web-pages)
- [Web API CSRF Prevention (official ASP.NET blog)](http://www.asp.net/web-api/overview/security/preventing-cross-site-request-forgery-%28csrf%29-attacks)

The standard frequency of token generation is **per-session**, so make
sure your sessions have a reasonable/configurable **time-out**. It is
possible to issue new tokens on a per-request basis. However, the added
protection may be insignificant, if this approach even fits your
application. See the link below for a discussion on the matter:
[Why refresh CSRF token per form request?](http://security.stackexchange.com/questions/22903/why-refresh-csrf-token-per-form-request)

## WebForms: ViewState

**Requirement:**
[EnableViewStateMac](https://msdn.microsoft.com/en-us/library/ms972969.aspx#securitybarriers_topic5)
must be set.
In fact, the ViewState MAC can no longer be disabled for versions since
September 2014.

The ASP.NET ViewState contains a property,
[ViewStateUserKey](https://msdn.microsoft.com/en-us/library/ms972969.aspx#securitybarriers_topic2),
which offers protection against CSRF by adding uniqueness to the
ViewState MAC as long as you set it to a new value for every session.

Note that ViewStateUserKey will not actually add a new value to the
ViewState, but rather simply influence the MAC process so as to make
every MAC unique per user session. Therefore, setting ViewStateUserKey
to the current Session ID is acceptable.

Since Visual Studio 2012, the anti-CSRF mechanism has been improved.

The new strategy still uses the ViewState as the main entity for CSRF
protection but also makes use of tokens (which you can generate as
GUIDs) so that you can set the ViewStateUserKey to the token rather than
the Session ID, and then validate it against the cookie.

Here's a [blog post by Eric Johnson and James Jardine](http://software-security.sans.org/developer-how-to/developer-guide-csrf)
with an example of this implementation.

For more implementation details, see:
- [MSDN - Securing ViewState](http://msdn.microsoft.com/en-us/library/ms178199%28v=vs.85%29.aspx)
- [MSDN - ViewStateUserKey](http://msdn.microsoft.com/en-us/library/ms972969.aspx#securitybarriers_topic2)

## Considerations for AJAX

Depending on your application, you'll likely have to choose between
using HTTP Headers or POST data to carry your anti-CSRF tokens.

Whatever you choose, the optimal validation method is indeed through
tokens. This means you can follow the token strategy while creating
either a **custom** header to hold the token value or just sending the
token with the rest of the POST data.

For more guidance, see the **answers** given to the following
questions:
- [Anti-CSRF Cookie](http://stackoverflow.com/questions/8253396/anti-csrf-cookie)
- [CSRF Protection With Custom Headers](http://security.stackexchange.com/questions/23371/csrf-protection-with-custom-headers-and-without-validating-token)

# Related [Attacks](https://owasp.org/www-community/attacks/)

- [CSRF (Attack)](https://owasp.org/www-community/attacks/csrf)
- [CSRF (Full Wikipedia Article)](https://en.wikipedia.org/wiki/Cross-site_request_forgery)
- [XSS (Attack)](https://owasp.org/www-community/attacks/xss/)

# Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

- [XSS](https://wiki.owasp.org/index.php/Cross_Site_Scripting_Flaw)
- [Insecure Randomness](https://owasp.org/www-community/vulnerabilities/Insecure_Randomness)
- [Insecure Third-Party Domain Access](https://owasp.org/www-community/vulnerabilities/Insecure_Third_Party_Domain_Access)

# References

- [Why refresh CSRF token per form request?](http://security.stackexchange.com/questions/22903/why-refresh-csrf-token-per-form-request)
- [CSRF Prevention (official ASP.NET blog)](http://www.asp.net/mvc/overview/security/xsrfcsrf-prevention-in-aspnet-mvc-and-web-pages)
- [Preventing CSRF Attacks (official ASP.NET blog)](http://www.asp.net/web-api/overview/security/preventing-cross-site-request-forgery-%28csrf%29-attacks)
- [Anti-CSRF and Cookies](http://stackoverflow.com/questions/8253396/anti-csrf-cookie)
- [How to protect against CSRF by default in ASP.NET MVC 4?](http://stackoverflow.com/questions/9965342/how-to-protect-against-csrf-by-default-in-asp-net-mvc-4)
- [How does ViewState protect against CSRF?](http://security.stackexchange.com/questions/19152/how-does-viewstate-protect-against-csrf)
- [How To Fix CSRF using Microsoft .Net ViewStateUserKey and Double Submit Cookie, by Eric Johnson and James Jardine](http://software-security.sans.org/developer-how-to/developer-guide-csrf)
- [CSRF Protection With Custom Headers (focus on the answer, not the question)](http://security.stackexchange.com/questions/23371/csrf-protection-with-custom-headers-and-without-validating-token)
- [MSDN - Securing ViewState](http://msdn.microsoft.com/en-us/library/ms178199%28v=vs.85%29.aspx)
- [MSDN - ViewStateUserKey](http://msdn.microsoft.com/en-us/library/ms972969.aspx#securitybarriers_topic2)
- [MSDN - HtmlHelper.AntiForgeryToken](http://msdn.microsoft.com/en-us/library/dd470175%28v=vs.100%29.aspx)
- [MSDN - ValidateAntiForgeryTokenAttribute](http://msdn.microsoft.com/en-us/library/system.web.mvc.validateantiforgerytokenattribute%28v=vs.100%29.aspx)
