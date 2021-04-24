---

layout: col-sidebar
title: Cross Site History Manipulation (XSHM)
author: Adar Weidman
contributors: James Bowie, kingthorin
permalink: /attacks/Cross_Site_History_Manipulation_(XSHM)
tags: attack, Cross Site History Manipulation (XSHM)

---

{% include writers.html %}

## Description

**Cross-Site History Manipulation (XSHM)** is a [SOP (Same Origin
Policy)](http://en.wikipedia.org/wiki/Same_origin_policy) security
breach. SOP is the most important security concept of modern browsers.
SOP means that web pages from different origins by design cannot
communicate with each other. **Cross-Site History Manipulation** breach
is based on the fact that client-side browser history object is not
properly partitioned on a per-site basis. Manipulating browser history
may lead to SOP compromising, allow bi-directional
[CSRF]({{ site.baseurl }}/attacks/csrf) and other
exploitations such as: user privacy violation, login status detection,
resources mapping, sensitive information inferring, users’ activity
tracking and URL parameter stealing.

## Risk Factors

By manipulating the browser history it is possible to compromise SOP and
violate user privacy. Using [CSRF]({{ site.baseurl }}/attacks/csrf) in conjunction
with history manipulation, not only integrity but also confidentiality
can be targeted. Feedbacks from a different origin can be accessed and
Cross-Site information leakage is achieved.

The following attack vectors based on techniques of **XSHM** are
possible:

- Cross-Site Condition Leakage
    - Login Detection
    - Resource Mapping
    - Error Leakage
    - State Detection
    - Information Inference
- Cross-Site User Tracking
- Cross-Site URL/Parameters Enumeration

## Examples

### What is Condition Leakage?

Condition leakage occurs when an attacker can infer a sensitive value of
a conditional statement in an attacked application. For example, if a
site contains the following logic:

```
Page A: If (CONDITION)
    Redirect(Page B)
```

an attacker can execute the [CSRF]({{ site.baseurl }}/attacks/csrf) and get an
indication about the value of the condition as a feedback. This attack
is executed from an attacker site. The site then submits a Cross-Site
request to a victim site, and by manipulating the History object gets a
feedback with required information leaked from a victim site. It is
important to mention that the redirect command can appear explicitly in
the code, or can be completed by the operational environment.

Attack Vector:

1. Create IFRAME with src=Page B
2. Remember the current value of history.length
3. Change src of IFRAME to Page A
4. If the value of history.length is the same, then the CONDITION is TRUE

### Login Detection

The following demo for IE and Facebook can show how one can identify if
users are currently using facebook: ["Am I using
Facebook?"](http://www.checkmarx.com/Demo/XSHM.aspx)

### Cross-Site Information Inference

It is possible to inference sensitive information from a page on a
different origin, if it implements a conditional redirect. Suppose that
in an HR application which is not publically accessible, a legal user
can search employees by name, salary and other criteria. If the search
has no results, a redirect command is then executed to a "Not Found"
page. By submitting the following URL:

<http://Intranet/SearchEmployee.aspx?name=Jon&SalaryFrom=3000&SalaryTo=3500>

and observing the NotFound redirection, attackers can inference
sensitive information about a worker's salary.

This can be done by using the following attack vector:

1. Create IFRAME with src="NotFound.aspx"
2. Remember the current value of history.length
3. Change src of IFRAME to "SearchEmployee.aspx?name=Jon\&SalaryFrom=3000\&SalaryTo=3500"
4. If the value of history.length remains the same, then your search has no results

By repeating the above attack and trying different values of the salary
parameters, an attacker can gather very sensitive salary information of
any employee. This is a very serious Cross-Site information leakage. If
an application has a functionality like a search page with conditional
redirect, then this application is vulnerable to **XSHM** and
essentially it is a similar to a direct exposure to [Universal
XSS](https://owasp.org/www-pdf-archive//OWASP_IL_The_Universal_XSS_PDF_Vulnerability.pdf)
– the application itself is
[XSS]({{ site.baseurl }}/attacks/xss)-safe, but running it from
a different site inside an IFRAME makes it vulnerable.

## Related [Attacks]({{ site.baseurl }}/attacks/)

- [Cross-site Scripting (XSS)]({{ site.baseurl }}/attacks/xss)
- [Cross-Site Request Forgery (CSRF)]({{ site.baseurl }}/attacks/csrf)

## References

- [Presentation in OWASP Israel Local Chapter Meeting
  (Feb-2010)](OWASP_Israel_2010_02#19:10_-_19:40.C2.A0:_XSHM_-_Cross_Site_History_Manipulation "wikilink")
- [Cross site history manipulation (XSHM)
  Guide](https://www.checkmarx.com/wp-content/uploads/2012/07/XSHM-Cross-site-history-manipulation.pdf)
- [Checkmarx identifies new web browser
  vulnerability](http://www.infosecurity-magazine.com/view/6828/checkmarx-identifies-new-web-browser-vulnerability/),
  *InfoSecurity Magazine*, January 27, 2010
- [Demo for Internet Explorer users - "Am I using
  Facebook?"](http://www.checkmarx.com/Demo/XSHM.aspx)
- [Wikipedia: Same Origin Policy
  (SOP)](http://en.wikipedia.org/wiki/Same_origin_policy)
