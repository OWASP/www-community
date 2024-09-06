---

title: Certificate and Public Key Pinning
layout: col-sidebar
author: Mark Gamache, Kevin Wall
contributors: 
tags: controls
permalink: /controls/Certificate_and_Public_Key_Pinning

---

{% include writers.html %}

## Background
Certificate and Public Key Pinning is a guide to understanding the current state of PKI security and significant changes in the threat model for TLS connections. Pinning was discussed at the [Virginia chapter’s](https://owasp.org/www-chapter-northern-virginia/) presentation [Securing Wireless Channels in the Mobile Space](https://wiki.owasp.org/images/8/8f/Securing-Wireless-Channels-in-the-Mobile-Space.ppt). The [previous version of this guide](https://web.archive.org/web/20230831033917/https:/owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning) was focused on providing clear, simple, actionable guidance for securing the channel in a hostile environment as well as a look at the threat model that made pinning necessary. If one finds the need, that implantation information is still valid. However, this guide is focused on understanding the current state of publicly trusted PKI and shows why, in nearly all cases, pinning creates much more risk than reward.

The document is also meant to clarify a point that was not made clear in the old OWASP article. If pinning is warranted, it should only be done when the client and server sides are both controlled by the same party. Trying to coordinate certificate rotations is a recipe for outages. Further, the original scope is intended for mobile applications only, which may not have been clear on older guidance.

A cheat sheet with more information on the threat model and tooling is available at [Pinning Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html).

## Introduction
Secure channels are a cornerstone of nearly all networked communications today. When channels carry vital data that needs its confidentiality or integrity maintained, most solutions involve X509 digital certificates. The other main components of the system are; the Certificate Authorities that issue the certificates, client side trust stores that determine which CAs can be trusted, and the communications channel itself. The client side OS is a consideration, but if it is compromised, pinning is the least of your problems.

In the past, various parts of the overall environment were considered so hostile that additional steps needed to be taken to truly secure a communications channel. This (older versions of this document and the cheat sheet are linked in Reference) was an excellent analysis and reading the older documents on this topic should be essential reading for those working in the applied cryptography space. You should not elect to pin certificates or keys unless you have read both the old and new documents.

Since the last guidance was published, the PKI ecosystem has significantly matured. Pinning is discouraged, unless your threat model meets very specific criteria and your pinning solution meets a very specific set of criteria as well.

### What was wrong with PKI?
The world of PKI had many issues when the [first OWASP Pinning Cheat Sheet](https://web.archive.org/web/20130423162921/https:/www.owasp.org/index.php/Pinning_Cheat_Sheet) was posted in April 2013. There was little explanation of the threat model, but the guidance was clear, "You should pin anytime you want to be relatively certain of the remote host's identity or when operating in a hostile environment. Since one or both are almost always true, you should probably pin all the time."

In May of 2013, the [first version](https://web.archive.org/web/20130508212238/https:/www.owasp.org/index.php/Certificate_and_Public_Key_Pinning) of **Certificate and Public Key Pinning** was posted. It relied heavily on two sources, [PKI is Broken](http://www.cs.auckland.ac.nz/~pgut001/pubs/pkitutorial.pdf) and [The Internet is Broken](http://blog.cryptographyengineering.com/2012/02/how-to-fix-internet.html). Interestingly, while the page title of Dr. Green’s piece may be **The Internet is Broken**, the page name is **how-to-fix-internet** and two of the key recommendations were completed and adopted.

The root cause of each criticism of PKI at the time was that the hierarchical nature of PKI conferred too much trust to too many CA operators who were not up to the task of maintaining security. Whether due to failure of security operations, application level bugs, being run by oppressive governments, or greed, some were allowing rogue certificates to be created. As a website operator had no control over which CAs a client might trust, pinning was introduced to limit this conference of trust.

It’s worth noting that for pinning to work we must assume that the client is not compromised. While it might be tempting to think it can help with a compromised client, this thinking is dangerous, as it suggests the attacker is sophisticated enough to compromise the client a little bit, but that they stop at not also disabling pinning. There are numerous, [well known](https://medium.com/@click4abhishekagarwal/pin-there-done-that-93033a351354), ways to easily defeat pinning if the client is compromised.

### What went wrong with pinning?
While the idea of pinning is simple, the execution proved difficult, if not impossible at scale. Getting pinning wrong could create an outage and might even block updating the pinning configuration to recover from the outage.

[HTTP Public Key Pinning](https://datatracker.ietf.org/doc/html/rfc7469) (HPKP) was the largest and most well thought out attempt to formalize pinning. Due to outages and the complexity of using HPKP, it was dropped by the few browsers that supported it. Deprecation was [completed by 2019](https://en.wikipedia.org/wiki/HTTP_Public_Key_Pinning#Browser_support_and_deprecation). Pinsets were key to making pinning workable. Rather than pinning one key, you pin a set of keys. HPKP allowed for pinsets of public keys. There are times when there is more than one legitimate public key. The most obvious is during certificate rotation. Trying to time pin rotation with certificate rotation with a single cert pinned would be impossible, as most clients would be offline and have an old pin. Also, in terms of private key protection, it is a best practice to create keys locally and not copy them around. For a geo load balanced system, this means there can be several live and valid certificates for a single name, which is likely a best practice if you are properly protecting private keys. Finally, the pinset allows for better planning by pre-creating keys and having proper time to update the pinset and make sure it is distributed before the new certificate is ever used. These sets were delivered in band via HTTP headers inside of the TLS channel. On the first visit to a URL, the browser would have no pinset and the browser would complete TLS. Then the web server would offer up the pinset. For all subsequent connections, the client would check to see that the current certificate’s public key was part of the pinset. If it wasn’t, the browser would drop the connection and generally show some error page. On every successful HTTP response, the server would send the pinset, allowing for updates to the set. 

This model had three meaningful issues:
1. The use of Trust on First Use (TOFU) creates risk if the attacker has their MITM running on first use.
2. The pinset could only be updated inside of the TLS session. If the site operator failed, or worse an attacker was performing MITM during Trust On First Use (TOFU), access to the site could be completely locked out. In order to make sure HPKP could not be hacked by way of client side tampering or social engineering, there was no mechanism to locally reset the pinsets. 
3. Many corporate environments use MITM based TLS inspection, which issues cloned certificates from a corporate trusted CA. While the naming information would match, the certificate’s public key would not. This could create an unintended denial of service on the application.

Part of the reason HPKP was so difficult to run successfully was because, in the case of a full stack developer, pinning with forward looking planning was just too much to handle. Exacerbating the problem was the fact that many companies had policies that required a new key pair be generated for every Certificate Signing Request [(CSR)](https://www.securew2.com/blog/certificate-signing-requests-explained) instead of allowing an existing key pair to be used for a CSR. Obviously the same key pair should not be used for significantly longer than the [NIST SP 800-57](https://csrc.nist.gov/pubs/sp/800/57/pt1/r5/final) (§ 5.3 Cryptoperiods) guidelines, but in the case of a mistake in pinning, renewing the certificate with the same key was often vital in order to keep the site alive and send an updated pinset. Pinning the current certificate’s key is easy enough, but planning and executing rotations proved too much. For larger organizations, where developers hand off code to be run by operations teams, pinning happened at the application layer, but the certificates were part of networking. The gaps in clear ownership caused problems and outages.

HPKP’s lifespan and eventual failure show elements of how every other attempt at pinning has failed or at least created availability risk. Ultimately, those pushing HPKP realized that the state of PKI was secure enough to stop forcing pinning. 

### What has changed in PKI security? 
The largest driver of changes to PKI security was understanding the incentives and leverage of the various parties involved. When [Taher Elgamal](https://en.wikipedia.org/wiki/Taher_Elgamal) created SSL for Netscape in 1995, the idea was to make the web secure. In those early days, there were not a lot of CAs to choose from. Netscape wanted the secure web to grow and could not afford to be too picky as to which CAs were trusted. CAs quickly became big business. Like many businesses, cutting costs and trying to sell more products sometimes got in the way of doing their core job well. CAs made horrible mistakes or choices, with no repercussions. They were treated as too big to fail. 

#### General Changes 
Fast forward from 1995, through the pain described in the original Certificate and Public Key Pinning in 2015, until now, the landscape has changed considerably. A small set of web browsers dominate the market and there are a large number of CAs, some that even offer certificates for free. As the browsers control the trust store, which in turn controls which CAs are trusted, the balance of power significantly favors the browser vendors. At this point, being the most secure browser trumps nearly every other consideration and those vendors are not afraid to wield their power.

The [Common CA Database](https://www.ccadb.org/resources) is a joint venture by Mozilla, Microsoft, Apple, and Google. It provides current lists of the CAs that each trusts and information on how a CA can get added to their trust stores. The trust store programs also make it clear that CAs will be removed if they are found to fall out of compliance. In the past, OS and browser vendors were often reluctant to exercise their power, be it for financial reasons or fear of being sued by a CA vendor. The most important component of the requirement to add CAs to these trust stores is that the CA pass a [Webtrust audit](https://www.cpacanada.ca/en/business-and-accounting-resources/audit-and-assurance/overview-of-webtrust-services/principles-and-criteria) or equivalent. This is a rigorous audit that covers PKI design, implementation, and operations. All three companies require the CA to pass the audit every year. Each program also retains the right to remove a CA at any time if meaningful violations are found in the CA design or operations. This process worked as designed during the [2022 Trustcor incident](https://www.washingtonpost.com/technology/2022/11/08/trustcor-internet-addresses-government-connections/). While there is still always a risk of a browser vendor doing the wrong thing, security and trust are now key features that users or enterprises demand from browsers.

For the purposes of this document OS and browser trust store can be used interchangeably. Some browsers, like Safari and Edge use the OS’s trust store. Chrome browser and OS have their own store, but when the browser runs on non-ChormeOS, it also trusts the OS store, and Firefox has its own TLS stack and store. In the mobile space, this is similar, as Android uses the Google store and Apple uses their own, both which apply to applications on the platform, not just browsers. 

The [CA Browser Forum](https://cabforum.org/) (CA/BF) is another organization working to make sure that the PKI industry is in sync. The Forum is an unincorporated association of separate organizations. It is made up of CA vendors, browser vendors, and other key parties with an interest in securing the internet. This collaboration between industries is useful in finding common ground when incentives do not align. The Forum has voting members and working groups that come together to evaluate and address risks in the space. They set [baseline requirements](https://cabforum.org/baseline-requirements-documents/) for how CAs are designed and operated. These rules must also be followed for a CA to be accepted into and remain in a Mozilla, Microsoft, Apple, or Google trust store.

#### Specific Changes
Cryptographer [Dr. Matthew Green](https://engineering.jhu.edu/faculty/matthew-green/) had two main recommendations on how to fix the internet. 
1. Rely on the browser vendors. 
As shown above, the browser vendors have taken great steps to deal with these issues and they have shown a strong commitment to continued vigilance in this space.
2. Sunlight is the best disinfectant.

##### Certificate Transparency Logs
This recommendation suggests publishing issued certificates into a [Merkle tree](https://en.wikipedia.org/wiki/Merkle_tree) so that the records are public and immutable. Thanks to Google’s market leverage, [Certificate Transparency Logging](https://certificate.transparency.dev/) has become a de facto standard. Google introduced CT Logging as optional in Chrome, for a time and then as CA’s came on board, they eventually began requiring every certificate that Chrome trusts to have been logged in CT. Given the success of this feature, CT logging is now reunited by Safari and Edge as well, covering [approximately 91%](https://www.browserstack.com/guide/understanding-browser-market-share) of the browser market as of 2023. Before a certificate is valid in any of these browsers, it must first be sent to 2 or 3 CT logs. The log servers themselves are readable to verify the certificate was logged, but they also provide signatures to be added to the final certificates, so that they can be verified in-band.

While CT Logs are a Merkle tree that is not simply searchable, there are many sites, like [crt.sh](https://crt.sh/) and [merklemap](https://www.merklemap.com/), that gather CT log data, as well as test other aspects of the certificates, and make data more searchable.
 
##### CAA Records
Another criticism of having larger trust stores with many CAs is that in most cases, a website will only use one or two CA vendors, despite most stores having more than 200 CAs present. This opens the possibility for an attacker to get a certificate for that site from any of the other numerous CAs (by trickery, bribery, etc.) and then use DNS cache poisoning or similar techniques to enable man-in-the-middle attacks against some specific web server. To combat this, the CA/BF requires CAs to respect [RFC 8659](https://datatracker.ietf.org/doc/html/rfc8659) DNS Certification Authority Authorization (CAA) Resource Record. A CAA record is a DNS record that is used to tell a CA, at the moment of certificate issuance, that only a certain CA or set of CAs is allowed to issue certificates for that domain or DNS name. CAA Resource Records are commonly used to support / bootstrap DNSSEC.

CAA records and the CA’s processing algorithm use the hierarchical nature of DNS, to allow different CAs to be authorized at different levels in DNS. One vendor can be used, for example.com and another for this.example.com. A key point in processing is that the name on the certificate is evaluated from the bottom up and if any CAA record set is found, it is used to pass or fail the request and processing stops going further. This allows for large organizations with varying procurement practices as well as delegating to 3rd parties who might provide hosting.

CAA record processing also respects the concept of DNS aliases using the CNAME. If site.example.com is CNAMEd to example-site.foo.com, the CA will first check for a CAA record at site.example.com and then, if not found, seeing the CNAME will check for a CAA record set at example-site.foo.com.

While CAA records can narrow which CAs can issue the certificate, what if the attacker reads the CAA record and simply gets an account with that CA? Some CAs also support the account or accounturi parameters in the CAA record, in order to limit which of the vendor’s accounts can issue the certificates.

If internet traffic can be MITMd, then DNS traffic can too. This is why most CA vendors don’t simply check the DNS record once, they use the concept of perspectives and check the record from many points on the globe. While not an absolute guarantee, it is a much harder task to MITM the entire web than just a small segment. Further, DNS and the target site are likely to not share the same network segments, requiring the attacker to perform MITM twice without detection. On top of that, if DNSSEC is used the CA vendors verify signatures making the MITM of DNS pointless.

A final note on CAA records. They are meant to be checked only at the time of certificate issuance and will change when the owner switches vendors. Do not attempt to use them as part of your connection validation code.

## What it takes to pin successfully
If the client’s pinset and the server’s keys are not kept in sync in real-time, do not pin, unless your use case allows for forced upgrades of the application where the pinset is part of a signed package, which may include an updated application version itself. This will only create operational burden and outages.

HPKP’s design took into account that pins needed to be updated frequently and the client and server needed to be in sync. HPKP showed us that, in order to pin safely and successfully, pins and pinsets need to be delivered out-of-band from the pinned channel. If the channel that delivers the pins is not protected against MITM, that is pinned itself, then what is the point of pinning your main API or site? This does raise the bar if the pinset comes from a site with a different DNS name as the attacker has to get two certificates and MITM two IPs. Your threat model may work with this. One, stronger, answer is to deliver the pins as signed data. Even if the attacker is able to achieve MITM, they cannot tamper with the set, however tampering could create a denial of service risk if the set can’t be updated. Additionally, signing means that the client needs to trust the public key of the signer, which, like in the PKI scenario, must also be delivered safely and occasionally rotated. There are no standards for this and creating them would be mirroring the threat model of the CA and browser space.

[JWK](https://openid.net/specs/draft-jones-json-web-key-03.html) and [JWS](https://openid.net/specs/draft-jones-json-web-signature-04.html) are good options as they have built in agility support making this far more future-proof. 

An option would be to deliver the set as JWS signed JSON. The JWS would look like this:
`eyJhbGciOiJFUzI1NiIsInR5cCI6IkpTT04ifQ.IltcclxuICB7XHJcbiAgICBcImRvbWFpblwiOiBcImNydC5zaFwiLFxyXG4gICAgXCJsYXN0X3VwZGF0ZWRcIjogXCIxNzE4MTMwNjA5XCIsXHJcbiAgICBcImtleV9waW5zXCI6IFtcclxuICAgICAgXCJwaW4tc2hhMjU2PTlSZUthY2xkVHlvUlNxUXgvOWR3a0Z1SGRWOE1UeU1XZGNLRWYyb2g2OW89XCIsXHJcbiAgICAgIFwicGluLXNoYTI1Nj03a0JoYVpDSmN5eTJ5dEY3cldFeGg0c1dYSGlnZGd3dkdhbVpza1Fhb0RNPVwiXHJcbiAgICBdXHJcbiAgfSxcclxuICB7XHJcbiAgICBcImRvbWFpblwiOiBcInd3dy5jcnQuc2hcIixcclxuICAgIFwibGFzdF91cGRhdGVkXCI6IFwiMTcxODEzMDYwOVwiLFxyXG4gICAgXCJrZXlfcGluc1wiOiBbXHJcbiAgICAgIFwicGluLXNoYTI1Nj03a0JoYVpDSmN5eTJ5dEY3cldFeGg0c1dYSGlnZGd3dkdhbVpza1Fhb0RNPVwiXHJcbiAgICBdXHJcbiAgfVxyXG5dIg.hkBX00q0YOSHzUk6cOI1vLuiIsMUZREP1c7EPf0laCzEKHgLai_HDG9_lLjA2NfsuTSL6Gzvr5Clme-jDHTItA`

Holding a signed payload like this:
```json
[
  {
	"domain": "crt.sh",
	"last_updated": "1718130609",
	"key_pins": [
  	"pin-sha256=9ReKacldTyoRSqQx/9dwkFuHdV8MTyMWdcKEf2oh69o=",
  	"pin-sha256=7kBhaZCJcyy2ytF7rWExh4sWXHigdgwvGamZskQaoDM="
	]
  },
  {
	"domain": "www.crt.sh",
	"last_updated": "1718130609",
	"key_pins": [
  	"pin-sha256=7kBhaZCJcyy2ytF7rWExh4sWXHigdgwvGamZskQaoDM="
	]
  }
]
```

This could be delivered via an unpinned URL or as part of the application package. Protecting the private signing key is vital as is making sure that an attacker can’t substitute their own signing key pair. As pinning should only be done for mobile applications, the public key could be part of the signed package data.

## Conclusion
While the idea of pinning is simple to talk about, it is very difficult to safely execute on. Considering the current risks in the CA and browser space and comparing them to the risk of down time, pinning is not recommended. Google, Microsoft, Apple, and Firefox control almost every trust store on every device on the planet and they wield this power with an eye on security as a competitive advantage. If your use case is so hostile that you wish to pin, make sure to read this document in full, the cheat sheet in full, and both original documents, so that you can weigh the risks and rewards based on your threat model.
 
## Reference 
- [Digicert CAA domain locking](https://docs.digicert.com/en/certcentral/manage-certificates/organization-and-domain-management/domain-locking.html)
- [Let’s Encrypt CAA account locking](https://letsencrypt.org/docs/caa/#the-accounturi-parameter)
- [Current OWASP Pinning Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html)
- [OWASP Previous Guidance on Pinning](https://web.archive.org/web/20230831033917/https:/owasp.org/www-community/controls/Certificate_and_Public_Key_Pinning)
- [Original OWASP Pinning Cheat Sheet](https://web.archive.org/web/20130423162921/https:/www.owasp.org/index.php/Pinning_Cheat_Sheet)
