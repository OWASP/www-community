---

layout: col-sidebar
title: Credential stuffing
author: Neal Mueller
contributors: Jmanico, Dirk Wetter, kingthorin, Nick Malcolm
permalink: /attacks/Credential_stuffing
tags: attack, Credential stuffing

---

{% include writers.html %}

## Description

Credential stuffing is the automated injection of stolen username and password pairs ("credentials") in to website login forms, in order to fraudulently gain access to user accounts. 

Since many users will re-use the same password and username/email, when those credentials are exposed (by a database breach or phishing attack, for example) submitting those sets of stolen credentials into dozens or hundreds of other sites can allow an attacker to compromise those accounts too.

Credential Stuffing is a subset of the brute force attack category. Brute forcing will attempt to try multiple passwords against one or multiple accounts; guessing a password, in other words. Credential Stuffing typically refers to specifically using known (breached) username / password pairs against other websites.


### Likelihood & Severity

Credential stuffing is one of the most common techniques used to
take-over user accounts. 

Credential stuffing is dangerous to both consumers and enterprises because of the ripple effects of these breaches. For more information on this please reference the Examples section showing the connected chain of events from one breach to another through credential stuffing.

### Anatomy of Attack

1.  The attacker acquires usernames and passwords from a website breach, phishing attack, password dump site.
2.  The attacker uses automated tools to test the stolen credentials against many websites (for instance, social media sites, online marketplaces, or web apps).
3.  If the login is successful, the attacker knows they have a set of valid credentials.

Now the attacker knows they have access to an account. Potential next steps include:

1.  Draining stolen accounts of stored value or making purchases.
2.  Accessing sensitive information such as credit card numbers, private messages, pictures, or documents.
3.  Using the account to send phishing messages or spam.
4.  Selling known-valid credentials to one or more of the compromised sites for other attackers to use.

### Diagram

![A diagram showing an attacker submitting the same set of credentials to three distinct websites, identifying which credentials are valid on which sites](../assets/images/attacks/credential-stuffing.png)

In the diagram above, acme.com's database is compromised. An attacker takes the breached database and tries the credentials on three other websites, looking for successful logins. The attacker identifies two websites where the user "spongebob" is reusing their password, and one website where the user "sally" is reusing their password. The attacker can now get access to those three accounts.

## Defense

Defenses against Credential Stuffing are described in the [Credential Stuffing Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html), Multi-Factor Authentication being a primary counter-measure.


## Examples

Below are excerpts taken from publications analyzing large-scale
breaches. Evidence supports that these breaches were the result of
credential stuffing.

- Sony, 2011 breach: “I wish to highlight that two-thirds of users whose data were in both the Sony data set and the Gawker breach earlier this year used the same password for each system.”
  - Source: Agile Bits     [1](https://blog.agilebits.com/2011/06/07/two-thirds-of-web-users-re-use-the-same-passwords/) - Source: Wired [2](http://www.wired.com/2011/10/93000-sony-accounts-breached/)
- Yahoo, 2012 breach: “What do Sony and Yahoo\! have in common? Passwords\!”.
  - Source: Troy Hunt. [3](http://www.troyhunt.com/2012/07/what-do-sony-and-yahoo-have-in-common.html)
- Dropbox, 2012 breach: “The usernames and passwords referenced in these articles were stolen from unrelated services, not Dropbox. Attackers then used these stolen credentials to try to log in to sites across the internet, including Dropbox”.
  - Source: Dropbox. [4](https://blog.dropbox.com/topics/company/dropbox-wasnt-hacked/)
- JPMC, 2014 breach: “[The breached data] contained some of the combinations of passwords and email addresses used by race participants who had registered on the Corporate Challenge website, an online platform for a series of annual charitable races that JPMorgan sponsors in major cities and that is run by an outside vendor. The races are open to bank employees and employees of other corporations”.
  - Source: NY Times. [5](http://dealbook.nytimes.com/2014/10/31/discovery-of-jpmorgan-cyberattack-aided-by-company-that-runs-race-website-for-bank/)

This connected chain of events from Sony to Yahoo to Dropbox excludes
JPMC. The JPMC breach came from a separate and unrelated source. We know
that the JPMC breach was caused by attackers targeting an unrelated
third-party athletic race/run site for credentials to use against JPMC.


## References


  - [F5's 2021 Credential Stuffing Report](https://www.f5.com/labs/articles/threat-intelligence/2021-credential-stuffing-report)
  - [You Can’t Secure 100% of Your Data 100% of the Time (2017)](https://hbr.org/2017/12/you-cant-secure-100-of-your-data-100-of-the-time)
  - [How Third Party Password Breaches Put Your Website at Risk (2013)](http://michael-coates.blogspot.be/2013/11/how-third-party-password-breaches-put.html)
  - [What Happens to Stolen Data After a Breach?](http://www.securityweek.com/what-happens-stolen-data-after-breach)

## See Also

  - OWASP [Credential Stuffing Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)
  - OWASP [Brute Force Attack](https://owasp.org/www-community/attacks/Brute_force_attack) 
  - OWASP [Password Spraying](https://owasp.org/www-community/attacks/Password_Spraying_Attack) 

[Category:Attack](https://owasp.org/www-community/attacks/)
