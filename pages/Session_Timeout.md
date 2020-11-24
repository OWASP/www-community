---

title: Session Timeout
layout: col-sidebar
author:
contributors:
tags: java, web session
auto-migrated: 1
permalink: /Session_Timeout

---

{% include writers.html %}

## Description of the session timeout

Session timeout represents the event occuring when a user does not perform
any action on a web site during an interval (defined by a web server). The
event, on the server side, changes the status of the user session to
'invalid' (ie. "not used anymore") and instructs the web server to
destroy it (deleting all data contained in it).

## Define the session timeout

On JEE web applications , there 2 ways to define a session timeout,

  - Declaratively in web deployment descriptor (file "web.xml") : This
    definition is applied to all sessions created for the application.
  - Programmatically on the session object : This definition applies only to the
    current session.

**Timeout defined declaratively**

    <?xml version="1.0" encoding="UTF-8"?>
    <web-app xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        ns="http://java.sun.com/xml/ns/javaee" xmlns:web="http://java.sun.com/xml/ns/javaee/web-app_2_5.xsd"
        xsi:schemaLocation="http://java.sun.com/xml/ns/javaee http://java.sun.com/xml/ns/javaee/web-app_3_0.xsd"
        id="WebApp_ID" version="3.0">

        ...

        <!-- Define a session timeout to 15 minutes -->
        <session-config>
            <session-timeout>15</session-timeout>
        </session-config>

        ...

    </web-app>

**Timeout defined Programmatically**

    package org.owasp.javaproject.sessiontimeout;

    import java.io.IOException;

    import javax.servlet.ServletException;
    import javax.servlet.annotation.WebServlet;
    import javax.servlet.http.HttpServlet;
    import javax.servlet.http.HttpServletRequest;
    import javax.servlet.http.HttpServletResponse;
    import javax.servlet.http.HttpSession;

    /**
     * Code sample showing how to access to session timeout and act on it.
     */
    @SuppressWarnings("serial")
    @WebServlet("/SessionTimeout")
    public class SessionTimeoutCodeSample extends HttpServlet {

        /**
         * {@inheritDoc}
         *
         * @see javax.servlet.http.HttpServlet#doGet(javax.servlet.http.HttpServletRequest,
         *      javax.servlet.http.HttpServletResponse)
         */
        @SuppressWarnings("boxing")
        @Override
        protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
            // Get reference on session object
            HttpSession session = req.getSession();

            // Display session timeout value defined in "web.xml"
            // Value here is specified in seconds...
            System.out.printf("Session timeout defined at application level : %s\n", session.getMaxInactiveInterval());

            // Change session timeout for this session and display new timeout value
            // Value here is defined in seconds...
            session.setMaxInactiveInterval(60);
            System.out.printf("Session timeout defined at code level : %s\n", session.getMaxInactiveInterval());
        }

    }

    Session timeout defined at application level : 900
    Session timeout defined at code level        : 60

## Impact of the session timeout on security and best practices

The Session timeout defines an action window time for a user, this window
represents the time in which an attacker can try to steal and use a existing user session...

For this, it's best practices to :

  - Set session timeout to the minimal value possible depending on the
    context of the application.
  - Avoid "infinite" session timeout.
  - Prefer declarative definition of the session timeout in order to
    apply a global timeout for all application sessions.
  - Trace session creation/destruction in order to analyse the creation trend
    and try to detect a normal number of session creations (application
    profiling phase in a attack).
