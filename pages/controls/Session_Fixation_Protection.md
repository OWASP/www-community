---

title: Session Fixation Protection
layout: col-sidebar
author: RoganDawes
contributors: Wichers, KirstenS, Jmanico, Mike Santillana, kingthorin
tags: controls, ASP
permalink: /controls/Session_Fixation_Protection

---

{% include writers.html %}

## Overview

Some platforms make it easy to protect against [Session
Fixation](../attacks/Session_fixation), while others make it a lot more
difficult. In most cases, simply discarding any existing session is
sufficient to force the framework to issue a new sessionid cookie, with
a new value. Unfortunately, some platforms, notably Microsoft ASP, do
not generate new values for sessionid cookies, but rather just associate
the existing value with a new session. This guarantees that almost all
ASP apps will be vulnerable to session fixation, unless they have taken
specific measures to protect against it.

## Anti-Fixation in ASP

Here is some sample code to illustrate an approach to preventing session
fixation attacks in ASP. The idea is that, since ASP prohibits write
access to the `ASPSESSIONIDxxxxx` cookie, and will not allow us to change
it in any way, we have to use an additional cookie that we do have
control over to detect any tampering. So, we set a cookie in the user's
browser to a random value, and set a session variable to the same value.
If the session variable and the cookie value ever don't match, then we
have a potential fixation attack, and should invalidate the session, and
force the user to log on again.

### Example implementation

Here is a sample implementation:

`AntiFixation.asp`:

```
<%
   ' This routine is intended to provide a degree of protection
   ' against Session Fixation attacks in classic ASP
   
   ' Session fixation attacks are a problem in ASP, since ASP does not
   ' allow you any access to the ASPSESSIONIDxxx cookie. Even invalidating
   ' the session does not alter the value of this cookie, preventing
   ' implementation of best practice recommendations, such as
   ' issuing new session cookies when the session is authenticated, or 
   ' invalidated.
   
   ' The basic premise of this routine is that we create a cookie that 
   ' we CAN control, e.g. ASPFIXATION, and assign a random value to this
   ' cookie when the session is authenticated. On subsequent pages, we 
   ' check the value of this cookie against the same variable stored in
   ' the user's session. If they do not match, access is denied.
   ' When the user logs out, the session should be invalidated, and so 
   ' by default, the cookie no longer matches the value in the session.
   
   Private Function RandomString(l)
       Dim value, i, r
       Randomize
       For i = 0 To l
           r = Int(Rnd * 62)
           If r<10 Then
               r = r + 48
           ElseIf r<36 Then
               r = (r - 10) + 65
           Else
               r = (r - 10 - 26) + 97
           End If
           value = value & Chr(r)
       Next
       RandomString = value
   End Function
   
   ' This routine should be called after the user has been authenticated.
   ' It is expected that the session has been invalidated prior to this call.
   Public Sub AntiFixationInit() 
       Dim value
       value = RandomString(10)
       Response.Cookies("ASPFIXATION") = value
       Session("ASPFIXATION") = value
   End Sub
   
   Public Sub AntiFixationVerify(LoginPage)
       Dim cookie_value, session_value
       cookie_value = Request.Cookies("ASPFIXATION")
       session_value = Session("ASPFIXATION")
       If cookie_value <> session_value Then
           Response.redirect(LoginPage)
       End If
   End Sub
   
%>
```

> NOTE: In an enterprise deployment, consider the use of a COM wrapper
object that invokes a cryptographically secure random number generator
in favor of the VBScript Rnd function.

Include the following lines in your login page:

and, when your user is successfully authenticated:

`AntiFixationInit()`

All other private pages (i.e. only accessible by an authenticated user)
should include the following lines (preferably as the first couple of
lines in the file):

`<% AntiFixationVerify("login.asp") %>`

In this case, any requests that do not contain a valid ASPFIXATION
cookie will be redirected to the page indicated, in this case
"login.asp". Note that we do not automatically invalidate the session,
since that would allow a denial of service attack against the legitimate
user. If one were concerned about brute force attacks against the
fixation cookie, one could either make the random value longer, and/or
use a counter in the session to detect repeated attacks, and invalidate
the session if a threshold is exceeded.
