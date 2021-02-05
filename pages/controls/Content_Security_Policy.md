---

layout: col-sidebar
title: Content Security Policy
author: Dominique RIGHETTO
contributors: Dimisec, Peter Mosmans, Taras Ivashchenko, Ajin Abraham, Pawel Krawczyk, Imifos, Neil Smithline, kingthorin
permalink: /controls/Content_Security_Policy
tags: controls, Content Security Policy

---

{% include writers.html %}
Last revision (mm/dd/yyyy): **08/31/2013**

## Introduction

**CSP** stands for **C**ontent **S**ecurity **P**olicy.

Is a W3C specification offering the possibility to instruct the client
browser from which location and/or which type of resources are allowed
to be loaded. To define a loading behavior, the CSP specification use
"directive" where a directive defines a loading behavior for a target
resource type.

This article is based on version
[1.1](http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html)
of the W3C specification.

Directives can be specified using HTTP response header (a server may
send more than one CSP HTTP header field with a given resource
representation and a server may send different CSP header field values
with different representations of the same resource or with different
resources) or HTML Meta tag, the HTTP headers below are defined by the
specs:

- **Content-Security-Policy** : Defined by W3C Specs as standard header, used by Chrome version 25 and later, Firefox version 23 and later, Opera version 19 and later.
- **X-Content-Security-Policy** : Used by Firefox until version 23, and Internet Explorer version 10 (which partially implements Content Security Policy).
- **X-WebKit-CSP** : Used by Chrome until version 25

The supported directives are:

- **default-src** : Define loading policy for all resources type in case of a resource type dedicated directive is not defined (fallback),
- **script-src** : Define which scripts the protected resource can execute,
- **object-src** : Define from where the protected resource can load plugins,
- **style-src** : Define which styles (CSS) the user applies to the protected resource,
- **img-src** : Define from where the protected resource can load images,
- **media-src** : Define from where the protected resource can load video and audio,
- **frame-src** : Define from where the protected resource can embed frames,
- **font-src** : Define from where the protected resource can load fonts,
- **connect-src** : Define which URIs the protected resource can load using script interfaces,
- **form-action** : Define which URIs can be used as the action of HTML form elements,
- **sandbox** : Specifies an HTML sandbox policy that the user agent applies to the protected resource,
- **script-nonce** : Define script execution by requiring the presence of the specified nonce on script elements,
- **plugin-types** : Define the set of plugins that can be invoked by the protected resource by limiting the types of resources that can be embedded,
- **report-uri** : Specifies a URI to which the user agent sends reports about policy violation

An introduction to CSP is available on
[HTML5Rocks](http://www.html5rocks.com/en/tutorials/security/content-security-policy/).
The browser support is shown on
<http://caniuse.com/#feat=contentsecuritypolicy>

## Risk

The risk with CSP can have 2 main sources:

1.  Policies misconfiguration,
2.  Too permissive policies.

## Countermeasure

This article will focus on providing an sample implementation of a JEE
Web Filter in order to apply a set of CSP policies on all HTTP response
returned by server.

The policies will instruct the browser to have the loading behavior
below using all HTTP headers defined in W3C Specs:

- Explicit loading definition of each resource type,
- Resources are loaded only from source domain,
- Inline style is not allowed,
- For JavaScript:
  - *Inline script* will be allowed because inline scripting is     commonly used (can be disabled if target site does not use this     type of scripting),
  - *eval()* function will be allowed in order to not break use of     popular JavaScript libraries (ex: JQuery, JQueryUI, Sencha, ...)     because they use eval() function (it was the case last time I     have checked the source code from CDN ;) ),
- Generation of a random not guessable script nonce to use into all script tags,
- Plugin types only allow PDF and Flash,
- No font loading (configurable),
- No Audio / Video loading (configurable),
- Enable browser XSS filtering feature.

The support for CSP directives is not the same level in major browsers (Firefox/Chrome/IE). It's recommanded to check the support provided by target browsers  (using site provided in link section of this article) in order to configure CSP policies. The sample below try to provide a set of policies from which your can add policies specific to your application context.

*This implementation provide an option to add CSP directives used by Firefox (Mozilla CSP directives).*

```java
import java.io.IOException;
import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;
import java.security.SecureRandom;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.Filter;
import javax.servlet.FilterChain;
import javax.servlet.FilterConfig;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

import org.apache.commons.codec.binary.Hex;

/**
 * Sample filter implementation to define a set of Content Security Policies.<br/>
 * This implementation has a dependency on Commons Codec API.<br/>
 * This filter set CSP policies using all HTTP headers defined into W3C specification.<br/>
 * <br/>
 * This implementation is oriented to be easily understandable and easily adapted.<br/>
 */
@WebFilter("/*")
public class CSPPoliciesApplier implements Filter {

    /** Configuration member to specify if web app use web fonts */
    public static final boolean APP_USE_WEBFONTS = false;

    /** Configuration member to specify if web app use videos or audios */
    public static final boolean APP_USE_AUDIOS_OR_VIDEOS = false;

    /**
     * Configuration member to specify if filter must add CSP directive used by Mozilla (Firefox)
     */
    public static final boolean INCLUDE_MOZILLA_CSP_DIRECTIVES = true;

    /** Filter configuration */
    @SuppressWarnings("unused")
    private FilterConfig filterConfig = null;

    /** List CSP HTTP Headers */
    private List<String> cspHeaders = new ArrayList<String>();

    /** Collection of CSP polcies that will be applied */
    private String policies = null;

    /** Used for Script Nonce */
    private SecureRandom prng = null;

    /**
     * Used to prepare (one time for all) set of CSP policies that will be applied on each HTTP
     * response.
     *
     * @see javax.servlet.Filter#init(javax.servlet.FilterConfig)
     */
    @Override
    public void init(FilterConfig fConfig) throws ServletException {
// Get filter configuration
        this.filterConfig = fConfig;

// Init secure random
        try {
            this.prng = SecureRandom.getInstance("SHA1PRNG");
        } catch (NoSuchAlgorithmException e) {
            throw new ServletException(e);
        }

// Define list of CSP HTTP Headers
        this.cspHeaders.add("Content-Security-Policy");
        this.cspHeaders.add("X-Content-Security-Policy");
        this.cspHeaders.add("X-WebKit-CSP");

// Define CSP policies
// Loading policies for Frame and Sandboxing will be dynamically defined : We need to know if context use Frame
        List<String> cspPolicies = new ArrayList<String>();
        String originLocationRef = "'self'";
        // --Disable default source in order to avoid browser fallback loading using 'default-src'
        // locations
        cspPolicies.add("default-src 'none'");
        // --Define loading policies for Scripts
        cspPolicies.add("script-src " + originLocationRef + " 'unsafe-inline' 'unsafe-eval'");
        if (INCLUDE_MOZILLA_CSP_DIRECTIVES) {
            cspPolicies.add("options inline-script eval-script");
            cspPolicies.add("xhr-src 'self'");
        }
        // --Define loading policies for Plugins
        cspPolicies.add("object-src " + originLocationRef);
        // --Define loading policies for Styles (CSS)
        cspPolicies.add("style-src " + originLocationRef);
        // --Define loading policies for Images
        cspPolicies.add("img-src " + originLocationRef);
        // --Define loading policies for Form
        cspPolicies.add("form-action " + originLocationRef);
        // --Define loading policies for Audios/Videos
        if (APP_USE_AUDIOS_OR_VIDEOS) {
            cspPolicies.add("media-src " + originLocationRef);
        }
        // --Define loading policies for Fonts
        if (APP_USE_WEBFONTS) {
            cspPolicies.add("font-src " + originLocationRef);
        }
        // --Define loading policies for Connection
        cspPolicies.add("connect-src " + originLocationRef);
        // --Define loading policies for Plugins Types
        cspPolicies.add("plugin-types application/pdf application/x-shockwave-flash");
        // --Define browser XSS filtering feature running mode
        cspPolicies.add("reflected-xss block");

        // Target formating
        this.policies = cspPolicies.toString().replaceAll("(\\[|\\])", "").replaceAll(",", ";")
                .trim();
    }

    /**
     * Add CSP policies on each HTTP response.
     *
     * @see javax.servlet.Filter#doFilter(javax.servlet.ServletRequest,
     *      javax.servlet.ServletResponse, javax.servlet.FilterChain)
     */
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain fchain)
            throws IOException, ServletException {
        HttpServletRequest httpRequest = ((HttpServletRequest) request);
        HttpServletResponse httpResponse = ((HttpServletResponse) response);

        /* Step 1 : Detect if target resource is a Frame */
        // Customize here according to your context...
        boolean isFrame = true;

        /* Step 2 : Add CSP policies to HTTP response */
        StringBuilder policiesBuffer = new StringBuilder(this.policies);

        // If resource is a frame add Frame/Sandbox CSP policy
        if (isFrame) {
            // Frame + Sandbox : Here sandbox allow nothing, customize sandbox options depending on
            // your app....
            policiesBuffer.append(";").append("frame-src 'self';sandbox");
            if (INCLUDE_MOZILLA_CSP_DIRECTIVES) {
                policiesBuffer.append(";").append("frame-ancestors 'self'");
            }
        }

        // Add Script Nonce CSP Policy
        // --Generate a random number
        String randomNum = new Integer(this.prng.nextInt()).toString();
        // --Get its digest
        MessageDigest sha;
        try {
            sha = MessageDigest.getInstance("SHA-1");
        } catch (NoSuchAlgorithmException e) {
            throw new ServletException(e);
        }
        byte[] digest = sha.digest(randomNum.getBytes());
        // --Encode it into HEXA
        String scriptNonce = Hex.encodeHexString(digest);
        policiesBuffer.append(";").append("script-nonce ").append(scriptNonce);
        // --Made available script nonce in view app layer
        httpRequest.setAttribute("CSP_SCRIPT_NONCE", scriptNonce);

        // Add policies to all HTTP headers
        for (String header : this.cspHeaders) {
            httpResponse.setHeader(header, policiesBuffer.toString());
        }

        /* Step 3 : Let request continue chain filter */
        fchain.doFilter(request, response);
    }

    /**
     * {@inheritDoc}
     *
     * @see javax.servlet.Filter#destroy()
     */
    @Override
    public void destroy() {
        // Not used
    }
}
```

## Tools

There's a number of free tools that can assist with the generating, evaluation and monitoring of content security policy.

It's very useful to include these types of tools into a web application development process in order to perform a regular automatic first level check (do not replace an manual audit and manual audit must be also conducted regularly).

* [w3af](http://w3af.org) audit tools contains a [plugin](https://github.com/andresriancho/w3af/blob/master/plugins/grep/csp.py)
to automatically audit web application to check if they correctly implement CSP policies.
* [CSP Tester (browser extension)](https://oxdef.info/csp-tester) to build and test the policy for your web application.
* [CSP Generator](https://csper.io/generator) for automatically generating policies ([chrome](https://chrome.google.com/webstore/detail/content-security-policy-c/ahlnecfloencbkpfnpljbojmjkfgnmdc)/[firefox](https://addons.mozilla.org/en-US/firefox/addon/csp-generator/) extension).
* [CSP Evaluator](https://csper.io/evaluator) for evaluating existing content security policies for security misconfigurations.
* [Csper report collector](https://csper.io/report-uri) for monitoring a content security policy using report-uri.

## Information Links

- [W3C Specifications: CSP 1.0](http://www.w3.org/TR/CSP), [CSP 1.1](http://w3c.github.io/webappsec/specs/content-security-policy/csp-specification.dev.html)
- [Introduction to CSP](http://www.html5rocks.com/en/tutorials/security/content-security-policy)
- [CSP browser support](http://caniuse.com/#feat=contentsecuritypolicy)
- [CSP readiness browser testing](http://erlend.oftedal.no/blog/csp/readiness/)
- [CSP Quick Reference](https://content-security-policy.com/)
