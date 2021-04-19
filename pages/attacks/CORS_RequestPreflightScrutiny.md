---

layout: col-sidebar
title: CORS RequestPreflightScrutiny
author: Dominique RIGHETTO
contributors: Imifos, kingthorin
permalink: /attacks/CORS_RequestPreflightScrutiny
tags: attack, CORS RequestPreflightScrutiny

---

{% include writers.html %}
Last revision (mm/dd/yyyy): **10/12/2012**

## Introduction

**CORS** stands for **C**ross-**O**rigin **R**esource **S**haring.

Is an feature offering the possbility to:

- A web application to expose resources to all or restricted domain,
- A web client to made AJAX request for resource on other domain than is source domain.

This article will focus on HTTP **Request Preflight** feature proposed
by CORS W3C specification and (mainly) how to setup a protection, on web
application side, against CORS HTTP request that try to bypass the
preflight process.

## Request preflight process overview

In order to not duplicate explanation, and because Mozilla wiki have a
great introduction article about CORS, you can read a description of the
process using link below:

- [Source](https://developer.mozilla.org/en-US/docs/HTTP_access_control#Preflighted_requests)
- [Google cache](http://webcache.googleusercontent.com/search?q=cache:f1R5zF__S20J:https://developer.mozilla.org/en-US/docs/HTTP_access_contro+cors%2Bmozilla&cd=1&hl=en&ct=clnk&gl=fr)

## Risk

Request preflight have to objective to ensure that HTTP request will not
have a bad impact on data, this, using a first request in which browser
describe the final HTTP request that will send later.

The main risk here (for web application), is that the request preflight
process is entirely managed on client side (by the browser) and then
anything warrant web application that the request preflight process will
be always followed...

A user can create/send (using tools like Curl,OWASP Zap Proxy,...) a
final HTTP request without previously send the first request for
preflight and then bypass request preflight process in order to act on
data in a unsafe way.

## Countermeasure

We must ensure the **Request Preflight process** compliance on server
side.

To achieve it we will use JEE Web Filter that will check every CORS
request using theses steps:

- Step 1 : Determine the type of the incoming request,
- Step 2 : Process request according to is type using temporary cache
    to keep state of preflighting step of the process.

**Sample implementation: Filter class**

```
```java
import java.io.IOException;
import java.util.Collections;
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

import net.sf.ehcache.Cache;
import net.sf.ehcache.CacheManager;
import net.sf.ehcache.Element;
import net.sf.ehcache.config.CacheConfiguration;
import net.sf.ehcache.config.PersistenceConfiguration;
import net.sf.ehcache.store.MemoryStoreEvictionPolicy;

/**
 * Sample filter implementation to scrutiny that CORS "Request Preflight" process is followed by HTTP request concerned.<br/>
 *
 * This implementation has a dependency on EHCache API because it use Caching to store preflighted requests.
 *
 * Assume here that all CORS resources are grouped in context path "/cors/".
 *
 * @see "https://developer.mozilla.org/en-US/docs/HTTP_access_control#Simple_requests"
 */
@SuppressWarnings("static-method")
@WebFilter("/cors/*")
public class CORSRequestPreflightProcessScrutiny implements Filter {

    // Filter configuration
    private FilterConfig filterConfig = null;

    // Period during which we keep a request as correctly followed the request preflight process
    private int requestPreflightCacheDelayInSeconds = 60;

    // Cache used to cache preflighted requests
    private Cache requestPreflightCache = null;

    /**
     * {@inheritDoc}
     *
     * @see Filter#init(FilterConfig)
     */
    @Override
    public void init(FilterConfig fConfig) throws ServletException {
        // Get filter configuration
        this.filterConfig = fConfig;
        // Initialize preflighted requests dedicated cache with a cache of X minutes expiration delay for each item
        PersistenceConfiguration cachePersistence = new PersistenceConfiguration();
        cachePersistence.strategy(PersistenceConfiguration.Strategy.NONE);
        CacheConfiguration cacheConfig = new CacheConfiguration().memoryStoreEvictionPolicy(MemoryStoreEvictionPolicy.FIFO).eternal(false)
                .timeToLiveSeconds(this.requestPreflightCacheDelayInSeconds)
                .statistics(false).diskExpiryThreadIntervalSeconds(this.requestPreflightCacheDelayInSeconds / 2)
                .persistence(cachePersistence).maxEntriesLocalHeap(10000).logging(false);
        cacheConfig.setName("PreflightedRequestsCacheConfig");
        this.requestPreflightCache = new Cache(cacheConfig);
        this.requestPreflightCache.setName("PreflightedRequestsCache");
        CacheManager.getInstance().addCache(this.requestPreflightCache);
    }

    /**
     * {@inheritDoc}
     *
     * @see Filter#destroy()
     */
    @Override
    public void destroy() {
        // Remove Cache
        CacheManager.getInstance().removeCache("PreflightedRequestsCache");
    }

    /**
     * {@inheritDoc}
     *
     * @see Filter#doFilter(ServletRequest, ServletResponse, FilterChain)
     */
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        HttpServletRequest htReq = ((HttpServletRequest) request);
        HttpServletResponse htResp = ((HttpServletResponse) response);
        int accessDeniedHttpResponse = HttpServletResponse.SC_FORBIDDEN;
        String accessControlAllowMethods = "GET, POST";
        String accessControlAllowOrigin = "http://foo.example";

        /* Step 01 : Determine the type of the incoming request */
        CORSRequestPreflightType corsReqType = determineRequestType(htReq);

        /* Step 02 : Process request according to is type */
        switch (corsReqType) {
        // --HTTP request send by client to preflight a further 'Complex' request
        case REQUEST_FOR_PREFLIGHT: {
            CORSRequestPreflightData corsReq = new CORSRequestPreflightData(htReq);
            // ----Step 2a: Check that request for preflight is valid, if not, send an access denied (do not give infos about bad resquest root cause)
            if (corsReq.getOrigin().trim().isEmpty() || corsReq.getExpectedMethod().trim().isEmpty()) {
                traceInvalidRequestDetected(htReq);
                htResp.reset();
                htResp.sendError(accessDeniedHttpResponse);
                // Exit Filter : Use 'return' algorithm break in order to avoid multiple IF statement and enhance readability...
                return;

            }
            // ----Step 2b: Store preflight request data in the Cache to keep (mark) the request as correctly followed the request preflight process
            Element cachedRequest = new Element(CORSUtils.buildRequestCacheIdentifier(htReq), corsReq);
            this.requestPreflightCache.put(cachedRequest);
            // ----Step 2c: Return corresponding response - This part should be customized with application specific constraints.....
            htResp.reset();
            htResp.setStatus(HttpServletResponse.SC_OK);
            htResp.setHeader("Access-Control-Allow-Origin", accessControlAllowOrigin);
            htResp.setHeader("Access-Control-Allow-Methods", accessControlAllowMethods);
            if (!corsReq.getExpectedCustomHeaders().isEmpty()) {
                htResp.setHeader("Access-Control-Allow-Headers", corsReq.getExpectedCustomHeaders().toString().replaceFirst("\\[", "").replaceFirst("\\]", "").trim());
            }
            htResp.setIntHeader("Access-Control-Max-Age", (this.requestPreflightCacheDelayInSeconds));
            break;
        }
        // --Normal HTTP request send by client that require preflight ie 'Complex' resquest in Preflight process
        case COMPLEX_REQUEST: {
            String rid = CORSUtils.buildRequestCacheIdentifier(htReq);
            // ----Step 2a: Check if the current request has an entry into the preflighted requests Cache
            if (this.requestPreflightCache.get(rid) == null) {
                traceInvalidRequestDetected(htReq);
                htResp.reset();
                htResp.sendError(accessDeniedHttpResponse);
                // Exit Filter : Use 'return' algorithm break in order to avoid multiple IF statement and enhance readability...
                return;
            }
            // ----Step 2b: Check that preflight information declared during the preflight request match the current request on key information
            CORSRequestPreflightData corsPreflightReq = (CORSRequestPreflightData) this.requestPreflightCache.get(rid).getValue();
            String origin = CORSUtils.retrieveHeader("Origin", htReq);
            List<String> customHeaders = CORSUtils.retrieveCustomHeaders(htReq);
            boolean match = false;
            // ------Start with comparison of "Origin" HTTP header (according to utility method impl. used to retrieve header reference cannot be null)...
            if (origin.equals(corsPreflightReq.getOrigin())) {
                // ------Continue with HTTP method...
                if (accessControlAllowMethods.contains(htReq.getMethod()) && htReq.getMethod().equals(corsPreflightReq.getExpectedMethod())) {
                    // ------Finish with custom HTTP headers (use an method to avoid manual iteration on collection to increase the speed)...
                    if (customHeaders.size() == corsPreflightReq.getExpectedCustomHeaders().size()) {
                        Collections.sort(customHeaders);
                        Collections.sort(corsPreflightReq.getExpectedCustomHeaders());
                        if (customHeaders.toString().equals(corsPreflightReq.getExpectedCustomHeaders().toString())) {
                            match = true;
                        }
                    }
                }
            }
            if (match) {
                // Continue chain to next filter
                chain.doFilter(request, response);
            } else {
                traceInvalidRequestDetected(htReq);
                htResp.reset();
                htResp.sendError(accessDeniedHttpResponse);
            }
            break;
        }
        // --Normal HTTP request send by client that do not require preflight ie 'Simple' resquest in Preflight process
        case SIMPLE_REQUEST: {
            // Continue chain to next filter
            chain.doFilter(request, response);
            break;
        }
        // --Unknown HTTP request type !
        default: {
            traceInvalidRequestDetected(htReq);
            htResp.reset();
            htResp.sendError(accessDeniedHttpResponse);
            break;
        }
        }
    }

    /**
     * Internal method to determine the type of the incoming request.
     *
     * @param htReq HTTP Request
     * @return the type as enumeration item
     */
    private CORSRequestPreflightType determineRequestType(HttpServletRequest htReq) {
        CORSRequestPreflightType type = CORSRequestPreflightType.UNKNOWN;

        if ("OPTIONS".equalsIgnoreCase(htReq.getMethod())) {
            type = CORSRequestPreflightType.REQUEST_FOR_PREFLIGHT;
        } else {
            if (!CORSUtils.retrieveCustomHeaders(htReq).isEmpty()) {
                type = CORSRequestPreflightType.COMPLEX_REQUEST;
            } else if ("POST".equalsIgnoreCase(htReq.getMethod()) && !"application/x-www-form-urlencoded".equalsIgnoreCase(htReq.getContentType())
                    && !"multipart/form-data".equalsIgnoreCase(htReq.getContentType()) && !"text/plain".equalsIgnoreCase(htReq.getContentType())) {
                type = CORSRequestPreflightType.COMPLEX_REQUEST;
            } else if ("HEAD".equalsIgnoreCase(htReq.getMethod()) || "DELETE".equalsIgnoreCase(htReq.getMethod()) || "PUT".equalsIgnoreCase(htReq.getMethod())
                    || "TRACE".equalsIgnoreCase(htReq.getMethod()) || "CONNECT".equalsIgnoreCase(htReq.getMethod())) {
                type = CORSRequestPreflightType.COMPLEX_REQUEST;
            } else {
                type = CORSRequestPreflightType.SIMPLE_REQUEST;
            }

        }

        return type;
    }

    /**
     * Method to add data of invalid request detected to a trace log
     *
     * @param htReq Invalid request detected
     */
    private void traceInvalidRequestDetected(HttpServletRequest htReq) {
        // Customize trace...
        this.filterConfig.getServletContext().log("---[CORS Invalid request detected]---");
        this.filterConfig.getServletContext().log(String.format("Client Address : %s", htReq.getRemoteAddr()));
        this.filterConfig.getServletContext().log(String.format("Target URL     : %s", htReq.getRequestURL()));
        this.filterConfig.getServletContext().log(String.format("Query String   : %s", htReq.getQueryString()));
        this.filterConfig.getServletContext().log(String.format("HTTP Method    : %s", htReq.getMethod()));
        // Print more request useful data.....
        this.filterConfig.getServletContext().log("-------------------------------------");
    }
}
```

**Sample implementation: Utility class used by Filter**

```java
import java.util.ArrayList;
import java.util.Enumeration;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

/**
 * Utility class for CORS data retrieving & processing.
 */
public class CORSUtils {

    /**
     * Method to retrieve HTTP request custom headers list.
     *
     * @param httpRequest Source HTTP request
     * @return List of custom headers (converted to uppercase to avoid case issue)
     */
    public static List<String> retrieveCustomHeaders(HttpServletRequest httpRequest) {
        List<String> xHeaders = new ArrayList<String>();
        String name = null;

        if (httpRequest == null) {
            throw new IllegalArgumentException("HTTP Request cannot be null !");
        }

        Enumeration<String> headers = httpRequest.getHeaderNames();
        while (headers.hasMoreElements()) {
            name = headers.nextElement().toUpperCase().trim();
            if (name.startsWith("X-")) {
                xHeaders.add(name.trim());
            }
        }

        return xHeaders;

    }

    /**
     * Method to retrieve a HTTP Header value from the source HTTP request. <br/>
     * Manage Header name case issue and take only first value.
     *
     * @param headerName HTTP name
     * @param httpRequest Source HTTP request
     * @return The HTTP Header value or "" if it cannot be found
     */
    public static String retrieveHeader(String headerName, HttpServletRequest httpRequest) {
        String value = "";
        String name = null;

        if (httpRequest == null) {
            throw new IllegalArgumentException("HTTP Request cannot be null !");
        }
        if ((headerName == null) || headerName.trim().isEmpty()) {
            throw new IllegalArgumentException("HTTP header name be null !");
        }

        Enumeration<String> headers = httpRequest.getHeaderNames();
        while (headers.hasMoreElements()) {
            name = headers.nextElement();
            if (name.trim().equalsIgnoreCase(headerName)) {
                value = httpRequest.getHeader(name);
                break;
            }
        }

        return value;
    }

    /**
     * Method to build an identifier for a request into the preflighted requests cache
     *
     * @param httpRequest Source HTTP request
     * @return The ID as String
     */
    public static String buildRequestCacheIdentifier(HttpServletRequest httpRequest) {
        return (httpRequest.getRemoteAddr() + "_" + httpRequest.getRequestURI()).trim();
    }
}
```

**Sample implementation: Pojo class used to store Preflight request key
information**

```java
import java.io.Serializable;
import java.util.ArrayList;
import java.util.List;

import javax.servlet.http.HttpServletRequest;

/**
 * Class to store information about a CORS preflighted request.
 */
@SuppressWarnings("serial")
public class CORSRequestPreflightData implements Serializable {

    /** Final HTTP request expected method */
    private String expectedMethod = null;
    /** Final HTTP request expected custom headers */
    private List<String> expectedCustomHeaders = null;

    /** Current HTTP request uri */
    private String uri = null;
    /** Current HTTP request origin header */
    private String origin = null;
    /** Current Sender IP address */
    private String sender = null;

    /**
     * Constructor
     *
     * @param httpRequest Source HTTP request
     */
    public CORSRequestPreflightData(HttpServletRequest httpRequest) {
        super();
        String tmp = null;
        if (httpRequest == null) {
            throw new IllegalArgumentException("HTTP request cannot be null !");
        }
        this.sender = httpRequest.getRemoteAddr();
        this.uri = httpRequest.getRequestURI();
        this.origin = CORSUtils.retrieveHeader("Origin", httpRequest);
        this.expectedMethod = CORSUtils.retrieveHeader("Access-Control-Request-Method", httpRequest);
        tmp = CORSUtils.retrieveHeader("Access-Control-Request-Headers", httpRequest);
        if (!tmp.trim().isEmpty()) {
            this.expectedCustomHeaders = new ArrayList<String>();
            String[] hs = tmp.split(",");
            for (String h : hs) {
                if ((h != null) && !h.trim().isEmpty()) {
                    this.expectedCustomHeaders.add(h.toUpperCase().trim());
                }
            }
        }
    }

    /**
     * Getter
     *
     * @return the expectedMethod
     */
    public String getExpectedMethod() {
        return this.expectedMethod;
    }

    /**
     * Getter
     *
     * @return the expectedCustomHeaders
     */
    public List<String> getExpectedCustomHeaders() {
        return this.expectedCustomHeaders;
    }

    /**
     * Getter
     *
     * @return the uri
     */
    public String getUri() {
        return this.uri;
    }

    /**
     * Getter
     *
     * @return the origin
     */
    public String getOrigin() {
        return this.origin;
    }

    /**
     * Getter
     *
     * @return the sender
     */
    public String getSender() {
        return this.sender;
    }
}
```

**Sample implementation: Enumeration used to represents the differents
CORS request type**

```java
/**
 * Enumeration of the differents CORS "request preflight" HTTP request type.
 */
public enum CORSRequestPreflightType {

    /** HTTP request send by client to preflight a further 'Complex' request */
    REQUEST_FOR_PREFLIGHT,

    /** Normal HTTP request send by client that require preflight ie 'Complex' resquest in Preflight process */
    COMPLEX_REQUEST,

    /** Normal HTTP request send by client that do not require preflight ie 'Simple' resquest in Preflight process */
    SIMPLE_REQUEST,

    /** Cannot determine request type */
    UNKNOWN;
}
```

**Note:** [W3AF](Automated_Audit_using_W3AF "wikilink") audit tools
(http://w3af.org) contains plugins to automatically audit web
application to check if they implements this type of countermeasure.

It's very useful to include this type of tools into a web application development process in order to perform a regular automatic first level check (do not replace an manual audit and manual audit must be also conducted regularly).

## Informations links

- [W3C Specification](http://www.w3.org/TR/cors/)
- [Mozilla Wiki](https://developer.mozilla.org/en-US/docs/HTTP_access_control)
- [Wikipedia](http://en.wikipedia.org/wiki/Cross-origin_resource_sharing)
