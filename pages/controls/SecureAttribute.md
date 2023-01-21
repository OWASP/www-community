---

title: Secure Cookie Attribute
layout: col-sidebar
author: MichaelCoates
contributors: Andrew Smith, Gladwin, Bill Sempf, Wichers, James Jardine, Zerosum0x0, Paco, Dan Wallis, Nawwar, kingthorin, Grant Ongers
permalink: /controls/SecureCookieAttribute

---

{% include writers.html %}

# Overview

The secure attribute is an option that can be set by the application server
when sending a new cookie to the user within an HTTP Response. The
purpose of the secure attribute is to prevent cookies from being observed by
unauthorized parties due to the transmission of the cookie in clear
text.
To accomplish this goal, browsers which support the secure attribute will
only send cookies with the secure attribute when the request is going to an
HTTPS page. Said in another way, the browser will not send a cookie with
the secure attribute set over an unencrypted HTTP request.
By setting the secure attribute, the browser will prevent the transmission of
a cookie over an unencrypted channel.

# Setting the Secure Attribute

Following sections describes setting the Secure Attribute in respective
technologies.

## Java

### Servlet 3.0 (Java EE 6)

Sun Java EE supports secure attribute in Cookie interface since version 6
(Servlet class version
3)[1](http://java.sun.com/javaee/6/docs/api/javax/servlet/http/Cookie.html#setSecure%28boolean%29),
also for session cookies
(JSESSIONID)[2](http://java.sun.com/javaee/6/docs/api/javax/servlet/SessionCookieConfig.html#setSecure%28boolean%29).
Methods *setSecure* and *isSecure* can be used to set and check for
secure value in cookies.

#### web.xml

Servlet 3.0 (Java EE 6) introduced a standard way to configure secure
attribute for the session cookie, this can be done by applying the
following configuration in web.xml

```xml
<session-config>
  <cookie-config>
  <secure>`true`</secure>
  </cookie-config>
</session-config>
```

### Tomcat

In **Tomcat 6** if the first request for session is using *https* then
it automatically sets secure attribute on session cookie.

### Setting it as a custom header

For **older versions** the workaround is to rewrite `JSESSIONID` value
using and setting it as a custom header. The drawback is that servers
can be configured to use a different session identifier than `JSESSIONID`.

`String sessionid = request.getSession().getId();`
`response.setHeader("SET-COOKIE", "JSESSIONID=" + sessionid + "; secure");`

### Environment consideration

With this attribute always set, sessions won't work in
environments(development/test/etc.) that may use http.
SessionCookieConfig
[3](http://java.sun.com/javaee/6/docs/api/javax/servlet/SessionCookieConfig.html#setSecure%28boolean%29)
interface or setting custom
header[4](https://www.owasp.org/index.php/SecureFlag#Setting_it_as_a_custom_header)
trick can be leveraged to configure setting of this attribute differently for
each environment and can be driven by application configuration.

## ASP.NET

Set the following in Web.config: `<httpCookies requireSSL="true" />`

For some objects that have a requireSSL property, like the forms
Authentication Cookie, set the `requireSSL="true"` attribute in the web.config
for that specific element. For example: 

```xml
<authentication mode="Forms">
  <forms loginUrl="member_login.aspx"
         cookieless="UseCookies"
         `requireSSL="true"`
         path="/MyApplication" />
</authentication>
```

Which will enable the secure attribute on the Forms Authentication cookie, as well as checking that the http request is coming to the server over SSL/TLS connection. Note that in case TLS is offloaded to a load balancer, the requireSSL solution wouldn't work.
 
Alternatively, the cookies can be set to secure programmatically using the following code by adding a EndRequest event handler to the `Global.asax.cs` file:

```
protected void Application_EndRequest(Object sender, EventArgs e) {
    // Iterate through any cookies found in the Response object.
    foreach (string cookieName in Response.Cookies.AllKeys) {
        Response.Cookies[cookieName]?.Secure = true;
    }
} 
```

## PHP

For session cookies managed by PHP, the attribute is set either permanently
in php.ini [PHP manual on
*SecureFlag*](http://php.net/manual/en/session.configuration.php#ini.session.cookie-secure)
through the parameter:

`session.cookie_secure = True`

or in and during a script via the function
[5](http://pl.php.net/manual/en/function.session-set-cookie-params.php):

```
void session_set_cookie_params ( int $lifetime  [, string $path  [, string $domain  
                                  [, bool $secure= false  [, bool $httponly= false  ]]]] )
```

For application cookies a parameter in setcookie() sets the secure attribute
[6](http://pl.php.net/setcookie):

```
bool setcookie ( string $name  [, string $value  [, int $expire= 0  [, string $path  
                 [, string $domain  [, bool $secure= false  [, bool $httponly= false  ]]]]]] )
```

## Go

### Iris

For [session cookies managed by Iris](https://docs.iris-go.com/iris/security/security-sessions-cookies), the attribute is set through the `CookieSecureTLS` option:

```go
app := iris.New()
sess := sessions.New(sessions.Config{
  CookieSecureTLS: true,
  // ...more options
})
app.Use(sess.Handler())
```

For application cookies a parameter in `SetCookie()` sets the secure attribute:

```go
app.Post("/", func(ctx iris.Context) {
  ctx.SetCookie(&http.Cookie{
    Secure: true,
    // ...more options
  })
})
```

OR by `CookieSecure` cookie option:

```go
ctx.SetCookieKV("name", "value", iris.CookieSecure)
```

OR set the attribute permanently:

```go
app := iris.New()
app.Use(withCookieOptions)

withCookieOptions := func(ctx iris.Context) {
	ctx.AddCookieOptions(iris.CookieSecure)
	ctx.Next()
}
```

For Single-Sign-On managed by Iris, the attribute is set through the `Cookie.Secure` option:

```go
authConfig := auth.Configuration{
  Cookie: auth.CookieConfiguration{
    Secure: true,
    // ...more options
  },
  // ...more options
}
```

# Testing for the Secure Attribute

Verifying that a web site sets this attribute on any particular cookie is
easy. Using an intercepting proxy, like [ZAP](https://www.zaproxy.org), you can
capture each response from the server and examine any Set-Cookie headers
it includes to see if the secure attribute is set on the cookie.

# Related Articles

- [http://www.troyhunt.com/2011/11/owasp-top-10-for-net-developers-part-9.html](http://www.troyhunt.com/2011/11/owasp-top-10-for-net-developers-part-9.html)
