---

layout: col-sidebar
title: Missing Error Handling
author: 
contributors: 
permalink: /vulnerabilities/Missing_Error_Handling
tags: vulnerability, Missing Error Handling

---

{% include writers.html %}

## Description

A web application must define a default error page for 404 errors, 500 errors, and to catch java.lang. Throwable exceptions prevent attackers from mining information from the application container's built-in error response.

When an attacker explores a web site looking for vulnerabilities, the amount of information that the site provides is crucial to the eventual success or failure of any attempted attacks. If the application shows the attacker a stack trace, it relinquishes information that makes the attacker's job significantly easier. For example, a stack trace might show the attacker a malformed SQL query string, the type of database being used, and the version of the application container. This information enables the attacker to target known vulnerabilities in these components.

The application configuration should specify a default error page in order to guarantee that the application will never leak error messages to an attacker. Handling standard HTTP error codes is useful and user-friendly in addition to being a good security practice, and a good configuration will also define a last-chance error handler that catches any exception that could possibly be thrown by the application.

## Risk Factors

TBD

## Examples

An "HTTP 404 - File not found" error tells an attacker that the requested file doesn't exist rather than that they don't have access to the file. This can help the attacker to decide their next step.

## Related [Attacks](../attacks/)

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

## References

TBD