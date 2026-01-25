---
title: HttpOnly
layout: col-sidebar
author:
contributors: Rknell, Wichers, Jmanico, Pawel Krawczyk , Alan Hogan, Eyal Lupu, D0ubl3 h3lix, Roberto Martelloni, Tarin Gamberini, Ali Khalfan, Markgordon, kingthorin, mkost, Grant Ongers
permalink: /HttpOnly

---

{% include writers.html %}

## Overview

The goal of this section is to introduce, discuss, and provide language specific mitigation techniques for HttpOnly.

### Who developed HttpOnly? When?

HttpOnly support was first added by Microsoft in Internet Explorer 6 SP1 around 2002. Over time the feature became part of all major browsers and is now treated as a standard cookie attribute.

### What is HttpOnly?
HttpOnly is an extra attribute that can be added to the `Set-Cookie` HTTP response header. When this flag is present, browsers that support it keep the cookie out of JavaScript APIs such as `document.cookie`.

The example below shows the syntax used within the HTTP response header:

```
Set-Cookie: <name>=<value>[; <Max-Age>=<age>]
`[; expires=<date>][; domain=<domain_name>]
[; path=<some_path>][; secure][; HttpOnly]
```

When a cookie is marked as HttpOnly, scripts running in the browser are not able to read its value. This makes it harder for many XSS attacks to steal session cookies or other sensitive data stored in cookies.

It is important to remember that HttpOnly does not block XSS or stop script execution. It only affects access to cookies, so other XSS impacts such as page defacement or CSRF token theft may still be possible.


### Mitigating the Most Common XSS attack using HttpOnly

According to [Michael Howard](https://en.wikipedia.org/wiki/Michael_Howard_(Microsoft)), Senior
Security Program Manager in the Secure Windows Initiative group at
Microsoft, the majority of XSS attacks target theft of session cookies.
A server could help mitigate this issue by setting the HttpOnly flag on
a cookie it creates, indicating the cookie should not be accessible on
the client.

If a browser that supports HttpOnly detects a cookie containing the
HttpOnly flag, and client side script code attempts to read the cookie,
the browser *returns an empty string* as the result. This causes the
attack to fail by preventing the malicious (usually XSS) code from
sending the data to an attacker's website.

##### Using Java to Set HttpOnly

Since Java Enterprise Edition 6 (JEE 6), which adopted Java Servlet 3.0
technology, it's programmatically easy to set the HttpOnly flag on a
cookie.

In fact `setHttpOnly` and `isHttpOnly` methods are available in the
`Cookie` interface
[JEE 6](http://java.sun.com/javaee/6/docs/api/javax/servlet/http/Cookie.html#setHttpOnly%28boolean%29),
[JEE 7](https://docs.oracle.com/javaee/7/api/javax/servlet/http/Cookie.html#setHttpOnly-boolean-)
and also for session cookies (JSESSIONID)
[JEE 6](http://java.sun.com/javaee/6/docs/api/javax/servlet/SessionCookieConfig.html#setHttpOnly%28boolean%29),
[JEE 7](https://docs.oracle.com/javaee/7/api/javax/servlet/SessionCookieConfig.html#setHttpOnly-boolean-)
`cookie.setHttpOnly(true);`

Moreover, since JEE 6 it's also declaratively easy setting `HttpOnly`
flag in a session cookie by applying the following configuration in the
deployment descriptor `WEB-INF/web.xml`:

```xml
<session-config>
   <cookie-config>
    <http-only>true</http-only>
   </cookie-config>
</session-config>
```

For Java Enterprise Edition versions *prior* to JEE 6 a common
**workaround** is to overwrite the `SET-COOKIE` HTTP response header
with a session cookie value that explicitly appends the `HttpOnly` flag:

```java
String sessionid = request.getSession().getId();
// be careful overwriting: JSESSIONID may have been set with other flags
response.setHeader("SET-COOKIE", "JSESSIONID=" + sessionid + "; HttpOnly");
```

In this context, overwriting, despite appropriate for the `HttpOnly`
flag, is discouraged because the JSESSIONID may have been set with other
flags. A better workaround is taking care of the previously set flags or
using the [ESAPI\#Java_EE](https://owasp.org/www-project-enterprise-security-api/) library: in fact
the `addCookie` method of the `SecurityWrapperResponse`
[3](http://code.google.com/p/owasp-esapi-java/source/browse/tags/esapi-2.0.1/src/main/java/org/owasp/esapi/filters/SecurityWrapperResponse.java)
takes care of previously set flags for us. So we could write a servlet
filter as the following one:

```java
public void doFilter(ServletRequest request, ServletResponse response, FilterChain filterChain) throws IOException, ServletException {
    HttpServletRequest httpServletRequest = (HttpServletRequest) request;
    HttpServletResponse httpServletResponse = (HttpServletResponse) response;
    // if errors exist then create a sanitized cookie header and continue
    SecurityWrapperResponse securityWrapperResponse = new SecurityWrapperResponse(httpServletResponse, "sanitize");
    Cookie[] cookies = httpServletRequest.getCookies();
    if (cookies != null) {
        for (int i = 0; i < cookies.length; i++) {
            Cookie cookie = cookies[i];
            if (cookie != null) {
                // ESAPI.securityConfiguration().getHttpSessionIdName() returns JSESSIONID by default configuration
                if (ESAPI.securityConfiguration().getHttpSessionIdName().equals(cookie.getName())) {
                    securityWrapperResponse.addCookie(cookie);
                }
            }
        }
    }
    filterChain.doFilter(request, response);
}
```

Some web application servers, that implement JEE 5, and servlet
containers that implement Java Servlet 2.5 (part of JEE 5), also allow
creating HttpOnly session cookies:

- **Tomcat 6** In `context.xml` set the `context` tag's attribute `useHttpOnly`
[4](http://tomcat.apache.org/tomcat-6.0-doc/config/context.html#Common_Attributes)
as follow:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<Context path="/myWebApplicationPath" useHttpOnly="true">
```

- **JBoss 5.0.1** and **JBOSS EAP 5.0.1** In
`server <myJBossServerInstance> \deploy\jbossweb.sar\context.xml`
set the `SessionCookie` tag
[5](https://community.jboss.org/message/598558#598558) as follow:

```xml
<Context cookies="true" crossContext="true">
    <SessionCookie secure="true" httpOnly="true" />
```

- **IBM Websphere** offer HTTPOnly for session cookies as a [configuration option](http://pic.dhe.ibm.com/infocenter/tivihelp/v33r1/topic/com.ibm.mam.inswas.doc/install/t_configuringthehttponlyattribute.html)

##### Using .NET to Set HttpOnly

- By *default*, **.NET 2.0** sets the HttpOnly attribute for
1. Session ID
2. Forms Authentication cookie

In .NET 2.0, HttpOnly can also be set via the HttpCookie object for all custom application cookies

- Via **web.config** in the system.web/httpCookies element

`<httpCookies httpOnlyCookies="true" …> `

- Or **programmatically**

C# Code:

```C#
HttpCookie myCookie = new HttpCookie("myCookie");
myCookie.HttpOnly = true;
Response.AppendCookie(myCookie);
```

VB.NET Code:

```vb
Dim myCookie As HttpCookie = new HttpCookie("myCookie")
myCookie.HttpOnly = True
Response.AppendCookie(myCookie)
```

- However, in **.NET 1.1**, you would have to do this *manually*,
e.g.,

`Response.Cookies[cookie].Path += ";HttpOnly";`

##### Using Python (cherryPy) to Set HttpOnly

Python Code (cherryPy):
To use HTTP-Only cookies with Cherrypy sessions just add the following
line in your configuration file:
`tools.sessions.httponly = True`
If you use SLL you can also make your cookies secure (encrypted) to
avoid "manipulator-in-the-middle" cookies reading with:
`tools.sessions.secure = True`

##### Using PHP to set HttpOnly

PHP supports setting the HttpOnly flag since version 5.2.0 (November
2006).

For session cookies managed by PHP, the flag is set either permanently
in php.ini [PHP manual on
*HttpOnly*](http://www.php.net/manual/en/session.configuration.php#ini.session.cookie-httponly)
through the parameter:

`session.cookie_httponly = True`

or in and during a script via the
function[6](http://pl.php.net/manual/en/function.session-set-cookie-params.php):

```
void session_set_cookie_params  ( int $lifetime  [, string $path  [, string $domain
                                  [, bool $secure= false  [, bool $httponly= false  ]]]] )
```

For application cookies last parameter in setcookie() sets HttpOnly
flag[7](http://pl.php.net/setcookie):

```
bool setcookie  ( string $name  [, string $value  [, int $expire= 0  [, string $path
                 [, string $domain  [, bool $secure= false  [, bool $httponly= false  ]]]]]] )
```


## Modern Browser Support

HttpOnly is available in all current mainstream browsers, including:

- Google Chrome and Microsoft Edge (Chromium-based)
- Mozilla Firefox
- Apple Safari

These browsers prevent client-side JavaScript from reading cookies that are marked with the HttpOnly attribute. Older products such as legacy Internet Explorer and Opera are no longer widely used and generally do not need to be considered when planning HttpOnly deployment.


### Web Application Firewalls

If code changes are infeasible, web application firewalls can be used to
add HttpOnly to session cookies:

- Mod_security - using SecRule and Header
directives[8](http://blog.modsecurity.org/2008/12/fixing-both-missing-httponly-and-secure-cookie-flags.html)
- ESAPI
WAF[9](http://code.google.com/p/owasp-esapi-java/downloads/list)
using *add-http-only-flag*
directive[10](http://www.slideshare.net/llamakong/owasp-esapi-waf-appsec-dc-2009)


## References

1. [CWE-1004: Sensitive Cookie Without 'HttpOnly' Flag](https://cwe.mitre.org/data/definitions/1004.html)
2. Wiens, Jordan ["No cookie for you!"](http://www.networkcomputing.com/careers/no-cookie-you/1270585242)
3. [Mitigating Cross-site Scripting with HTTP-Only Cookies](http://msdn2.microsoft.com/en-us/library/ms533046.aspx)
4. Howard, Michael. [Some Bad News and Some Good News](http://msdn2.microsoft.com/en-us/library/ms972826.aspx)
5. MSDN. [Setting the HttpOnly property in .NET](http://msdn.microsoft.com/en-us/library/system.web.httpcookie.httponly.aspx)
6. [XSS: Gaining access to HttpOnly Cookie in 2012](http://seckb.yehg.net/2012/06/xss-gaining-access-to-httponly-cookie.html)
7. [Setting HttpOnly in Java](http://stackoverflow.com/questions/13147113/setting-an-httponly-cookie-with-javax-servlet-2-5)
8. [Misunderstandings on HttpOnly Cookie](https://web.archive.org/web/20130701055119/http://blog.fortify.com:80/blog/2011/11/02/Misunderstandings-on-HttpOnly-Cookie)
