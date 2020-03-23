---

layout: col-sidebar
title: Credential stuffing
author: 
contributors: 
permalink: /attacks/Credential_stuffing
tags: attack, Credential stuffing
auto-migrated: 1

---

## Description

Credential stuffing is the automated injection of breached
username/password pairs in order to fraudulently gain access to user
accounts. This is a subset of the brute force attack category: large
numbers of spilled credentials are automatically entered into websites
until they are potentially matched to an existing account, which the
attacker can then hijack for their own purposes.

### Uniqueness

Credential stuffing is a new form of attack to accomplish account
takeover through automated web injection. Credential stuffing is related
to the breaching of databases; both accomplish account takeover.
Credential stuffing is an emerging threat.

Credential stuffing is dangerous to both consumers and enterprises
because of the ripple effects of these breaches. For more information on
this please reference the Examples section showing the connected chain
of events from one breach to another through credential stuffing.

### Severity

Credential stuffing is one of the most common techniques used to
take-over user accounts.

### Anatomy of Attack

1.  The attacker acquires spilled usernames and passwords from a website
    breach or password dump site.
2.  The attacker uses an account checker to test the stolen credentials
    against many websites (for instance, social media sites or online
    marketplaces).
3.  Successful logins (usually 0.1-0.2% of the total login attempts)
    allow the attacker to take over the account matching the stolen
    credentials.
4.  The attacker drains stolen accounts of stored value, credit card
    numbers, and other personally identifiable information
5.  The attacker may also use account information going forward for
    other nefarious purposes (for example, to send spam or create
    further transactions)

### Diagram

[<file:Credentialstuffing.png>](file:Credentialstuffing.png "wikilink")

### References

\[1\]
<http://michael-coates.blogspot.be/2013/11/how-third-party-password-breaches-put.html>

## Examples

Below are excerpts taken from publications analyzing large-scale
breaches. Evidence supports that these breaches were the result of
credential stuffing.

  - Sony, 2011 breach: “I wish to highlight that two-thirds of users
    whose data were in both the Sony data set and the Gawker breach
    earlier this year used the same password for each system.”
      - Source: Agile Bits
        [1](https://blog.agilebits.com/2011/06/07/two-thirds-of-web-users-re-use-the-same-passwords/)
      - Source: Wired
        [2](http://www.wired.com/2011/10/93000-sony-accounts-breached/)

<!-- end list -->

  - Yahoo, 2012 breach: “What do Sony and Yahoo\! have in common?
    Passwords\!”.
      - Source: Troy Hunt.
        [3](http://www.troyhunt.com/2012/07/what-do-sony-and-yahoo-have-in-common.html)

<!-- end list -->

  - Dropbox, 2012 breach: “The usernames and passwords referenced in
    these articles were stolen from unrelated services, not Dropbox.
    Attackers then used these stolen credentials to try to log in to
    sites across the internet, including Dropbox”.
      - Source: Dropbox.
        [4](https://blog.dropbox.com/2014/10/dropbox-wasnt-hacked/)

<!-- end list -->

  - JPMC, 2014 breach: “\[The breached data\] contained some of the
    combinations of passwords and email addresses used by race
    participants who had registered on the Corporate Challenge website,
    an online platform for a series of annual charitable races that
    JPMorgan sponsors in major cities and that is run by an outside
    vendor. The races are open to bank employees and employees of other
    corporations”.
      - Source: NY Times.
        [5](http://dealbook.nytimes.com/2014/10/31/discovery-of-jpmorgan-cyberattack-aided-by-company-that-runs-race-website-for-bank/)

This connected chain of events from Sony to Yahoo to Dropbox excludes
JPMC. The JPMC breach came from a separate and unrelated source. We know
that the JPMC breach was caused by attackers targeting an unrelated
third-party athletic race/run site for credentials to use against JPMC.

## Related Threat Agents

  - [:Category:Authentication](:Category:Authentication "wikilink")

## Related Attacks

  - [Brute force attack](Brute_force_attack "wikilink")

## Related Vulnerabilities

  - [API Abuse](API_Abuse "wikilink")

## Related Controls

  - [Authentication](Authentication "wikilink")

## Defense

  - [Credential Stuffing Prevention Cheat
    Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Credential_Stuffing_Prevention_Cheat_Sheet.html)

## References

  - Ramification of Credential Stuffing
    [6](https://prezi.com/kdilcmkhhrfl/ramification-of-credential-stuffing/)
  - What Happens to Stolen Data After a Breach?
    [7](http://www.securityweek.com/what-happens-stolen-data-after-breach)
  - How Third Party Password Breaches Put Your Website at Risk
    [8](http://michael-coates.blogspot.com/2013/11/how-third-party-password-breaches-put.html)

[Category:Attack](Category:Attack "wikilink")