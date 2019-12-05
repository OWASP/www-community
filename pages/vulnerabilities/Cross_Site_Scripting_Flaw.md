---

layout: col-sidebar
title: Cross Site Scripting Flaw
author: 
contributors: 
permalink: /vulnerabilities/Cross_Site_Scripting_Flaw
tag: vulnerability, Cross Site Scripting Flaw
auto-migrated: 1

---

Last revision (mm/dd/yy): **//**

[Vulnerabilities Table of Contents](ASDR_TOC_Vulnerabilities "wikilink")

## Description

Cross site Scripting (XSS) attacks are a type of injection problem, in
which malicious scripts are injected into otherwise benign and trusted
web sites. Cross site scripting flaws are the most prevalent flaw in web
applications today. Cross site scripting attacks occur when an attacker
uses a web application to send malicious code, generally in the form of
a browser side script, to a different end user. Flaws that allow these
attacks to succeed are quite widespread and occur anywhere a web
application uses input from a user in the output it generates without
validating or encoding it.

Attackers frequently use a variety of methods to encode the malicious
portion of the tag, such as using Unicode, so the request is less
suspicious looking to the user. There are hundreds of variants of these
attacks, including versions that do not even require any \< \> symbols.
For this reason, attempting to “filter out” these scripts is not likely
to succeed. Instead we recommend validating input against a rigorous
positive specification of what is expected. XSS attacks usually come in
the form of embedded JavaScript. However, any embedded active content is
a potential source of danger, including: ActiveX (OLE), VBscript,
Shockwave, Flash and more.

XSS issues can also be present in the underlying web and application
servers as well. Most web and application servers generate simple web
pages to display in the case of various errors, such as a 404 ‘page not
found’ or a 500 ‘internal server error.’ If these pages reflect back any
information from the user’s request, such as the URL they were trying to
access, they may be vulnerable to a reflected XSS attack.

The likelihood that a site contains XSS vulnerabilities is extremely
high. There are a wide variety of ways to trick web applications into
relaying malicious scripts. Developers that attempt to filter out the
malicious parts of these requests are very likely to overlook possible
attacks or encodings. Finding these flaws is not tremendously difficult
for attackers, as all they need is a browser and some time. There are
numerous free tools available that help hackers find these flaws as well
as carefully craft and inject XSS attacks into a target site.

### Environments Affected

All web servers, application servers, and web application environments
are susceptible to cross site scripting.

### How to Determine If You Are Vulnerable

There are three known types of cross site scripting:
[reflected](Cross-site_Scripting_\(XSS\)#Reflected_XSS_Attacks "wikilink"),
[stored](Cross-site_Scripting_\(XSS\)#Stored_XSS_Attacks "wikilink"),
and [DOM injection](DOM_Based_XSS "wikilink"). Reflected XSS is the
easiest to exploit – a page will reflect user supplied data directly
back to the user:

echo $_REQUEST\['userinput'\];

Stored XSS takes hostile data, stores it in a file, a database, or other
back end system, and then at a later stage, displays the data to the
user, unfiltered. This is extremely dangerous in systems such as CMS,
blogs, or forums, where a large number of users will see input from
other individuals.

With DOM based XSS attacks, the site’s JavaScript code and variables are
manipulated rather than HTML elements. Alternatively, attacks can be a
blend or hybrid of all three types. The danger with cross site scripting
is not the type of attack, but that it is possible.

Attacks are usually implemented in JavaScript, which is a powerful
scripting language. Using JavaScript allows attackers to manipulate any
aspect of the rendered page, including adding new elements (such as
adding a login tile which forwards credentials to a hostile site),
manipulating any aspect of the internal DOM tree, and deleting or
changing the way the page looks and feels. JavaScript allows the use of
XmlHttpRequest, which is typically used by sites using AJAX
technologies, even if victim site does not use AJAX today.

Using XmlHttpRequest (AJAX), it is sometimes possible to get around a
browser’s same source origination policy - thus forwarding victim data
to hostile sites, and to create complex worms and malicious zombies that
last as long as the browser stays open. AJAX attacks do not have to be
visible or require user interaction to perform dangerous cross site
request forgery (CSRF) attacks (see [CSRF](CSRF "wikilink")).

XSS flaws can be difficult to identify and remove from a web
application. The best way to find flaws is to perform a security review
of the code and search for all places where input from an HTTP request
could possibly make its way into the HTML output. Note that a variety of
different HTML tags can be used to transmit a malicious JavaScript.
Nessus, Nikto, and some other available tools can help scan a website
for these flaws, but can only scratch the surface.

## Prevention

OWASP's recommended defenses against XSS are documented in the OWASP
[XSS (Cross Site Scripting) Prevention Cheat
Sheet](XSS_\(Cross_Site_Scripting\)_Prevention_Cheat_Sheet "wikilink").

## Examples

  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-4206>
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2005-3966>
  - <http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2006-5204>

## Related [Attacks](Attacks "wikilink")

  - [Cross-site Scripting
    (XSS)](Cross-site_Scripting_\(XSS\) "wikilink")
  - [Cross Site History Manipulation
    (XSHM)](Cross_Site_History_Manipulation_\(XSHM\) "wikilink")

## References

  - [XSS (Cross Site Scripting) Prevention Cheat
    Sheet](XSS_\(Cross_Site_Scripting\)_Prevention_Cheat_Sheet "wikilink")
  - OWASP Guide to Building Secure Web Applications and Web Services,
    [Data Validation](Data_Validation "wikilink")
  - OWASP Testing Guide, [Testing for Cross site
    scripting](Testing_for_Cross_site_scripting "wikilink")
  - The Cross Site Scripting FAQ:
    <http://www.cgisecurity.com/articles/xss-faq.shtml>
  - XSS Cheat Sheet: [XSS Filter Evasion Cheat
    Sheet](XSS_Filter_Evasion_Cheat_Sheet "wikilink") New home for the
    old: ha.ckers.org/xss.html site.
  - CERT Advisory on Malicious HTML Tags:
    <http://www.cert.org/advisories/CA-2000-02.html>
  - CERT "Understanding Malicious Content Mitigation"
    <http://www.cert.org/tech_tips/malicious_code_mitigation.html>
  - Understanding the cause and effect of CSS Vulnerabilities:
    <http://www.technicalinfo.net/papers/CSS.html>
  - [How to Build an HTTP Request Validation Engine (J2EE validation
    with
    Stinger)](How_to_Build_an_HTTP_Request_Validation_Engine_for_Your_J2EE_Application "wikilink")
  - XSSed - Cross-Site Scripting (XSS) Information and Mirror Archive of
    Vulnerable Websites <http://www.xssed.com>
  - Cross-Site Scripting Security Exposure Executive Summary:
    <http://technet.microsoft.com/en-us/library/cc750326.aspx>
  - [Have Your Cake and Eat It
    Too](Have_Your_Cake_and_Eat_It_Too "wikilink") (.NET request
    validation)

__NOTOC__

[add links \[\[Category:Input_Validation_Vulnerability|Category:Input
Validation Vulnerability\]\] ](Category:FIXME "wikilink")
[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Externally Linked
Page](Category:Externally_Linked_Page "wikilink")