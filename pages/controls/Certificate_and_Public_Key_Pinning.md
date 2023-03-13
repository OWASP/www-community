---

title: Certificate and Public Key Pinning
layout: col-sidebar
author: Jeffery Walton, JohnSteven, Jim Manico, Kevin Wall, Ricardo Iramar
contributors: Jack Mannino, Karl Fogel, Jshowalter , Achim, Pawel Krawczyk, Peter Bachman, Bill Sempf, Izar, Echsecutor, Jmanico, Douglasheld, Anant Shrivastava, Riramar, Nabla.c0d3, Neil Smithline, Tfrdidi, kingthorin
tags: controls
permalink: /controls/Certificate_and_Public_Key_Pinning

---

{% include writers.html %}

Certificate and Public Key Pinning is a technical
guide to implementing certificate and public key pinning as discussed at
the *[Virginia chapter's](https://owasp.org/www-chapter-northern-virginia/)*
presentation [Securing Wireless Channels in the Mobile
Space](https://wiki.owasp.org/images/8/8f/Securing-Wireless-Channels-in-the-Mobile-Space.ppt).
This guide is focused on providing clear, simple, actionable guidance
for securing the channel in a hostile environment where actors could be
malicious and the conference of trust a liability.

A cheat sheet is available at [Pinning Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Pinning_Cheat_Sheet.html).

## Introduction

Secure channels are a cornerstone to users and employees working
remotely and on the go. Users and developers expect end-to-end security
when sending and receiving data - especially sensitive data on channels
protected by VPN, SSL, or TLS. While organizations which control DNS and
CA have likely reduced risk to trivial levels under most threat models,
users and developers subjugated to other's DNS and a public CA hierarchy
are exposed to non-trivial amounts of risk. In fact, history has shown
those relying on outside services have suffered chronic breaches in
their secure channels.

The pandemic abuse of trust has resulted in users, developers and
applications making security related decisions on untrusted input. The
situation is somewhat of a paradox: entities such as DNS and CAs are
trusted and supposed to supply trusted input; yet their input cannot be
trusted. Relying on untrusted input for security related decisions is
not only bad karma, it violates a number of secure coding principals
(see, for example, OWASP's [Injection Theory](../Injection_Theory) and Data
Validation.

Pinning effectively removes the "conference of trust". An application
which pins a certificate or public key no longer needs to depend on
others - such as DNS or CAs - when making security decisions relating to
a peer's identity. For those familiar with SSH, you should realize that
public key pinning is nearly identical to SSH's `StrictHostKeyChecking`
option. SSH had it right the entire time, and the rest of the world is
beginning to realize the virtues of directly identifying a host or
service by its public key.

Others who actively engage in pinning include Google and its browser
Chrome. Chrome was successful in detecting the DigiNotar compromise
which uncovered suspected interception by the Iranian government on its
citizens. The initial report of the compromise can be found at *[Is This
MITM Attack to Gmail's
SSL?](https://productforums.google.com/d/topic/gmail/3J3r2JqFNTw/discussion)*;
and Google Security's immediate response at *[An update on attempted
man-in-the-middle
attacks](https://googleonlinesecurity.blogspot.com/2011/08/update-on-attempted-man-in-middle.html)*.

## What's the problem?

Users, developers, and applications expect end-to-end security on their
secure channels, but some secure channels are not meeting the
expectation. Specifically, channels built using well known protocols
such as VPN, SSL, and TLS can be vulnerable to a number of attacks.

Examples of past failures are listed on the discussion tab for this
article. This cheat sheet does not attempt to catalogue the failures in
the industry, investigate the design flaws in the scaffolding, justify
the lack of accountability or liability with the providers, explain the
race to the bottom in services, or demystify the collusion between, for
example, Browsers and CAs. For additional reading, please visit *[PKI is Broken](http://www.cs.auckland.ac.nz/~pgut001/pubs/pkitutorial.pdf)* and
*[The Internet is Broken](http://blog.cryptographyengineering.com/2012/02/how-to-fix-internet.html)*.

### Patient 0

The original problem was the *Key Distribution Problem*. Insecure
communications can be transformed into a secure communication problem
with encryption. Encrypted communications can be transformed into an
identity problem with signatures. The identity problem terminates at the
key distribution problem. They are the same problem.

### The Cures

There are three cures for the key distribution problem. First is to have
first hand knowledge of your partner or peer (i.e., a peer, server or
service). This could be solved with SneakerNet. Unfortunately,
SneakerNet does not scale and cannot be used to solve the key
distribution problem.

The second is to rely on others, and it has two variants: (1) web of
trust, and (2) hierarchy of trust. Web of Trust and Hierarchy of Trust
solve the key distribution problem in a sterile environment. However,
Web of Trust and Hierarchy of Trust each requires us to rely on others -
or **confer trust**. In practice, trusting others is showing to be
problematic.

## What Is Pinning?

Pinning is the process of associating a host with their *expected* X509
certificate or public key. Once a certificate or public key is known or
seen for a host, the certificate or public key is associated or 'pinned'
to the host. If more than one certificate or public key is acceptable,
then the program holds a *pinset* (taking from [Jon Larimer and Kenny
Root Google I/O
talk](https://developers.google.com/events/io/sessions/gooio2012/107/)).
In this case, the advertised identity must match one of the elements in
the pinset.

A host or service's certificate or public key can be added to an
application at development time, or it can be added upon first
encountering the certificate or public key. The former - adding at
development time - is preferred since *preloading* the certificate or
public key *out of band* usually means the attacker cannot taint the
pin. If the certificate or public key is added upon first encounter, you
will be using *key continuity*. Key continuity can fail if the attacker
has a privileged position during the first encounter.

Pinning leverages knowledge of the pre-existing relationship between the
user and an organization or service to help make better security related
decisions. Because you already have information on the server or
service, you don't need to rely on generalized mechanisms meant to solve
the *key distribution* problem. That is, you don't need to turn to DNS
for name/address mappings or CAs for bindings and status. One exception
is revocation and it is discussed below in [Pinning
Gaps](#Pinning_Gaps).

It is also worth mention that Pinning is not Stapling. Stapling sends
both the certificate and OCSP responder information in the same request
to avoid the additional fetches the client should perform during path
validations.

### When Do You Pin?

You should pin anytime you want to be relatively certain of the remote
host's identity or when operating in a hostile environment. Since one or
both are almost always true, you should probably pin all the time.

A perfect case in point: during the two weeks or so of preparation for
the presentation and cheat sheet, we've observed three relevant and
related failures. First was [Nokia/Opera willfully breaking the secure
channel](http://gaurangkp.wordpress.com/2013/01/09/nokia-https-mitm/);
second was [DigiCert issuing a code signing certificate for
malware](http://blog.malwarebytes.org/intelligence/2013/02/digital-certificates-and-malware-a-dangerous-mix/);
and third was [Bit9's loss of its root signing
key](http://krebsonsecurity.com/2013/02/security-firm-bit9-hacked-used-to-spread-malware/).
The environment is not only hostile, it's toxic.

### When Do You Allow List?

If you are working for an organization which practices "egress
filtering" as part of a Data Loss Prevention (DLP) strategy, you will
likely encounter *Interception Proxies*. I like to refer to these things
as **"good" bad guys** (as opposed to **"bad" bad guys**) since both
break end-to-end security and we can't tell them apart. In this case,
**do not** offer to allow list the interception proxy since it defeats
your security goals. Add the interception proxy's public key to your
pinset after being **instructed** to do so by the folks in Risk
Acceptance.

Note: if you allow list a certificate or public key for a different host
(for example, to accommodate an interception proxy), you are no longer
pinning the expected certificates and keys for the host. Security and
integrity on the channel could suffer, and it surely breaks end-to-end
security expectations of users and organizations.

For more reading on interception proxies, the additional risk they
bestow, and how they fail, see Dr. Matthew Green's *[How do Interception
Proxies
fail?](http://blog.cryptographyengineering.com/2012/03/how-do-interception-proxies-fail.html)*
and Jeff Jarmoc's BlackHat talk *[SSL/TLS Interception Proxies and
Transitive
Trust](https://www.blackhat.com/html/bh-eu-12/bh-eu-12-archives.html#jarmoc)*.

### How Do You Pin?

The idea is to re-use the existing protocols and infrastructure, but use
them in a hardened manner. For re-use, a program would keep doing the
things it used to do when establishing a secure connection.

To harden the channel, the program would take advantage of the
`OnConnect` callback offered by a library, framework or platform. In the
callback, the program would verify the remote host's identity by
validating its certificate or public key. While pinning does not have to
occur in an `OnConnect` callback, it's often most convenient because the
underlying connection information is readily available.

### When Do You Not Pin?

Pinning requires control of upcoming certificate attributes. If the
certificate key pair cannot be predicted in advance before it is put
into service, then pinning will lead to an outage when the endpoint
presents a new certificate. For instance, if a certificate provider
generates random key pairs whenever a certificate is rotated, and you
cannot control when this certificate is put into use, then you will
not be able to update your clients until they have already experienced
an outage. You should not pin using attributes of a certificate
presented by an endpoint outside of your control.

## What Should Be Pinned?

The first thing to decide is what should be pinned. For this choice, you
have two options: you can (1) pin the certificate; or (2) pin the public
key. If you choose public keys, you have two additional choices: (a) pin
the `subjectPublicKeyInfo`; or (b) pin one of the concrete types such as
`RSAPublicKey` or `DSAPublicKey`.

The three choices are explained below in more detail. I would encourage
you to pin the `subjectPublicKeyInfo` because it has the public
parameters (such as `{e,n}` for an RSA public key) **and** contextual
information such as an algorithm and OID. The context will help you keep
your bearings at times, and Figure 1 below shows the additional
information available.

### Encodings/Formats

For the purposes of this article, the objects are in X509-compatible
presentation format (PKCS\#1 defers to X509, both of which use ASN.1).
If you have a PEM encoded object, such as:

```
-----BEGIN CERTIFICATE-----
...
-----END CERTIFICATE-----
```

Then convert the object to DER encoding. Conversion using OpenSSL is offered
below in [Format Conversions](#Format_Conversions).

A certificate is an object which binds an entity (such as a person or
organization) to a public key via a signature. The certificate is DER
encoded, and has associated data or attributes such as *Subject* (who is
identified or bound), *Issuer* (who signed it), *Validity* (*NotBefore*
and *NotAfter*), and a *Public Key*.

A certificate has a *subjectPublicKeyInfo*. The subjectPublicKeyInfo is
a key with additional information. The ASN.1 type includes an *Algorithm
ID*, a *Version*, and an extensible format to hold a concrete public
key. Figures 1 and 2 below show different views of the same RSA key,
which is the subjectPublicKeyInfo. The key is for the site
[random.org](https://www.random.org), and it is used in the sample
programs and listings below.

| Figure 1: `subjectPublicKeyInfo` dumped with `dumpasn1`                        | Figure 2: `subjectPublicKeyInfo` under a hex editor                        |
| ----------------------------------------------------------------------------- | -------------------------------------------------------------------------- |
| ![Figure 1: subjectPublicKeyInfo dumped with dumpasn1](../assets/images/random-org-der-dump.png) | ![Figure 2: subjectPublicKeyInfo under a hex editor](../assets/images/random-org-der-hex.png) |

The concrete public key is an encoded public key. The key format will
usually be specified elsewhere - for example, PKCS\#1 in the case of RSA
Public Keys. In the case of an RSA public key, the type is
*RSAPublicKey* and the parameters `{e,n}` will be ASN.1 encoded. Figures
1 and 2 above clearly show the modulus (*n* at line 28) and exponent
(*e* at line 289). For DSA, the concrete type is DSAPublicKey and the
ASN.1 encoded parameters would be `{p,q,g,y}`.

Final takeaways: (1) a certificate binds an entity to a public key; (2)
a certificate has a subjectPublicKeyInfo; and (3) a subjectPublicKeyInfo
has an concrete public key. For those who want to learn more, a more
in-depth discussion from a programmer's perspective can be found at the
Code Project's article *[Cryptographic Interoperability:
Keys](http://www.codeproject.com/Articles/25487/Cryptographic-Interoperability-Keys)*.

### Certificate

![Certificate](../assets/images/pin-cert.png)

The certificate is easiest to pin. You can fetch the certificate out of band for
the website, have the IT folks email your company certificate to you, use
`openssl s_client` to retrieve the certificate etc. When the certificate
expires, you would update your application. Assuming your application has no
bugs or security defects, the application would be updated every year or two.

At runtime, you retrieve the website or server's certificate in the
callback. Within the callback, you compare the retrieved certificate
with the certificate embedded within the program. If the comparison
fails, then fail the method or function.

There is a downside to pinning a certificate. If the site rotates its
certificate on a regular basis, then your application would need to be
updated regularly. If you do not control when this certificate is put
into service, then pinning will lead to an outage.

### Public Key

![Public Key](../assets/images/pin-pubkey.png)

Public key pinning is more flexible but a little trickier due to the extra steps
necessary to extract the public key from a certificate. As with a certificate,
the program checks the extracted public key with its embedded copy of the public
key.

There are two downsides to public key pinning. First, it's harder to
work with keys (versus certificates) since you usually must extract
the key from the certificate. Extraction is a minor inconvenience in
Java and .NET, buts it's uncomfortable in Cocoa/CocoaTouch and
OpenSSL.  Second, the key is static and may violate key rotation
policies. For this reason, a certificate management service may
generate new keys every time. If that is the case, then it may be
difficult to pin using the public key.

### Hashing

While the three choices above used DER encoding, it's also acceptable to
use a hash of the information (or other transforms). In fact, the
original sample programs were written using digested certificates and
public keys. The samples were changed to allow a programmer to inspect
the objects with tools like `dumpasn1` and other ASN.1 decoders.

Hashing also provides three additional benefits. First, hashing allows
you to anonymize a certificate or public key. This might be important if
you application is concerned about leaking information during
decompilation and re-engineering.

Second, a digested certificate fingerprint is often available as a
native API for many libraries, so it's convenient to use.

Finally, an organization might want to supply a reserve (or back-up)
identity in case the primary identity is compromised. Hashing ensures
your adversaries do not see the reserved certificate or public key in
advance of its use. In fact, Google's IETF draft *websec-key-pinning*
uses the technique.

The downside to hashing is similar to that of pinning the
certificate. You must be able to update client applications before the
certificate is used by the service endpoint.

## Examples of Pinning

This section demonstrates certificate and public key pinning in Android
Java, iOS, .NET, and OpenSSL.

### HTTP pinning

[Expect-CT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Expect-CT) header allows sites to opt in to the [Certificate Transparency](https://developer.mozilla.org/en-US/docs/Web/Security/Certificate_Transparency) framework, in report or enforcement mode, based on the readiness of the application.

> [HPKP](https://tools.ietf.org/html/rfc7469) got deprecated in [2018](https://www.chromestatus.com/feature/5903385005916160) after intents of removing it started in [2017](https://groups.google.com/a/chromium.org/forum/#!msg/blink-dev/he9tr7p3rZ8/eNMwKPmUBAAJ). Almost [all browsers no longer support it](https://developer.mozilla.org/en-US/docs/Web/HTTP/Public_Key_Pinning#Browser_compatibility) as [attacks against HPKP surfaced](https://scotthelme.co.uk/using-security-features-to-do-bad-things/#usinghpkpforevil). HPKP is being replaced by the reactive Certificate Transparency framework coupled with the `Expect-CT` header.

[Certificate Transparency](https://www.certificate-transparency.org/) project help detect and protect users from mistakenly issued certificates or certificates that have been issued by rogue certificate authoroties (CA). One example of a rogue CA happening was the [Dutch CA DigiNotar](https://en.wikipedia.org/wiki/DigiNotar).

> `Expect-CT` header is expected to be obsolete in June 2021, as all issued certificates will already be incorporating [Signed Certificate Timestamps (SCTs)](https://www.certificate-transparency.org/faq#TOC-What-is-an-SCT-).

### Android

Since Android N, the preferred way for implementing pinning is by
leveraging Android's [Network Security
Configuration](https://developer.android.com/training/articles/security-config.html)
feature, which lets apps customize their network security settings in a
safe, declarative configuration file without modifying app code.

To enable pinning, [the `<pin-set>` configuration
setting](https://developer.android.com/training/articles/security-config.html#CertificatePinning)
can be used.

If devices running a version of Android that is earlier than N need to
be supported, a backport of the Network Security Configuration pinning
functionality is available via [the TrustKit Android library](https://github.com/datatheorem/TrustKit-Android).

Lastly, the Android documentation provides an example of how SSL
validation can be customized within the app's code (in order to
implement pinning) in the [Unknown CA implementation
document](https://developer.android.com/training/articles/security-ssl.html#UnknownCa).
However, implementing pinning validation from scratch should be avoided,
as implementation mistakes are extremely likely and usually lead to
severe vulnerabilities.

### iOS

TrustKit, an open-source SSL pinning library for iOS and macOS is
available at <https://github.com/datatheorem/TrustKit>. It provides an
easy-to-use API for implementing pinning, and has been deployed in many
apps.

Otherwise, more details regarding how SSL validation can be customized
on iOS (in order to implement pinning) are available in [the "HTTPS
Server Trust Evaluation" technical note](https://developer.apple.com/library/content/technotes/tn2232/_index.html).
However, implementing pinning validation from scratch should be avoided,
as implementation mistakes are extremely likely and usually lead to
severe vulnerabilities.

### .NET

.NET pinning can be achieved by using `ServicePointManager` for `HttpWebRequest`, or
`HttpClientHandler` when using `HttpClient`, as shown below.

#### HttpWebRequest

Download: [.Net sample program](https://wiki.owasp.org/images/2/25/Pubkey-pin-dotnet.zip).

```
// Domain name for which to perform certificate pinning
private const string DomainName = "encrypted.google.com";

// Encoded RSAPublicKey for Domain name
private const string DomainPublicKey = "30818902818100C4A06B7B52F8D17DC1CCB47362" +
	"C64AB799AAE19E245A7559E9CEEC7D8AA4DF07CB0B21FDFD763C63A313A668FE9D764E" +
	"D913C51A676788DB62AF624F422C2F112C1316922AA5D37823CD9F43D1FC54513D14B2" +
	"9E36991F08A042C42EAAEEE5FE8E2CB10167174A359CEBF6FACC2C9CA933AD403137EE" +
	"2C3F4CBED9460129C72B0203010001";

public static void Main(string[] args)
{
	ServicePointManager.ServerCertificateValidationCallback = PinPublicKey;
	var wr = WebRequest.Create(string.Format("https://{0}/", DomainName));
	wr.GetResponse();
}

private static bool PinPublicKey(
	object sender,
	X509Certificate certificate,
	X509Chain chain,
	SslPolicyErrors sslPolicyErrors)
{
	if (certificate == null)
		return false;

	var request = sender as HttpWebRequest;
	if (request == null)
		return false;

	// if the request is for the target domain, perform certificate pinning
	if (string.Equals(request.Address.Authority, DomainName, StringComparison.OrdinalIgnoreCase))
	{
		var pk = certificate.GetPublicKeyString();
		return pk.Equals(DomainPublicKey);
	}

	// Check whether there were any policy errors for any other domain
	return sslPolicyErrors == SslPolicyErrors.None;
}
```

Note that using `ServicePointManager.ServerCertificateValidationCallback` affects
server certificate validation for **all** requests requiring validation from
the AppDomain. It is therefore advisable to check that the `sender` represents a request
to the authority to which to apply certificate pinning, as the example above demonstrates.

In .NET Framework 4.5 onwards, a validation callback can be set per HTTP request

```
// Domain name for which to perform certificate pinning
private const string DomainName = "encrypted.google.com";

// Encoded RSAPublicKey for Domain name
private const string DomainPublicKey = "30818902818100C4A06B7B52F8D17DC1CCB47362" +
	"C64AB799AAE19E245A7559E9CEEC7D8AA4DF07CB0B21FDFD763C63A313A668FE9D764E" +
	"D913C51A676788DB62AF624F422C2F112C1316922AA5D37823CD9F43D1FC54513D14B2" +
	"9E36991F08A042C42EAAEEE5FE8E2CB10167174A359CEBF6FACC2C9CA933AD403137EE" +
	"2C3F4CBED9460129C72B0203010001";

public static void Main(string[] args)
{
	var wr = (HttpWebRequest)WebRequest.Create(string.Format("https://{0}/", DomainName));

	// set server validation callback for this request only
	wr.ServerCertificateValidationCallback = PinPublicKey;
	wr.GetResponse();
}

private static bool PinPublicKey(
	object sender,
	X509Certificate certificate,
	X509Chain chain,
	SslPolicyErrors sslPolicyErrors)
{
	if (certificate == null)
		return false;

	var request = sender as HttpWebRequest;
	if (request == null)
		return false;

	// if the request is for the target domain, perform certificate pinning
	if (string.Equals(request.Address.Authority, DomainName, StringComparison.OrdinalIgnoreCase))
	{
		var pk = certificate.GetPublicKeyString();
		return pk.Equals(DomainPublicKey);
	}

	// Check whether there were any policy errors for any other domain
	return sslPolicyErrors == SslPolicyErrors.None;
}
```

#### HttpClient

When using `HttpClient`, a server validation callback can be set on
`HttpClientHandler` that will affect **all** requests requiring
validation made with `HttpClient` instances using the `HttpClientHandler`.

```
// Domain name for which to perform certificate pinning
private const string DomainName = "encrypted.google.com";

// Encoded RSAPublicKey for Domain name
private const string DomainPublicKey = "30818902818100C4A06B7B52F8D17DC1CCB47362" +
	"C64AB799AAE19E245A7559E9CEEC7D8AA4DF07CB0B21FDFD763C63A313A668FE9D764E" +
	"D913C51A676788DB62AF624F422C2F112C1316922AA5D37823CD9F43D1FC54513D14B2" +
	"9E36991F08A042C42EAAEEE5FE8E2CB10167174A359CEBF6FACC2C9CA933AD403137EE" +
	"2C3F4CBED9460129C72B0203010001";

public static void Main(string[] args)
{
	MainAsync().Wait();
}

private static async Task MainAsync()
{
	var handler = new HttpClientHandler
	{
		ServerCertificateCustomValidationCallback = PinPublicKey
	};

	var client = new HttpClient(handler);
	await client.GetAsync(string.Format("https://{0}/", DomainName));
}

private static bool PinPublicKey(
	HttpRequestMessage requestMessage,
	X509Certificate2 certificate,
	X509Chain chain,
	SslPolicyErrors sslPolicyErrors)
{
	if (certificate == null)
		return false;

	// if the request is for the target domain, perform certificate pinning
	if (string.Equals(requestMessage.RequestUri.Authority, DomainName, StringComparison.OrdinalIgnoreCase))
	{
		var pk = certificate.GetPublicKeyString();
		return pk.Equals(DomainPublicKey);
	}

	// Check whether there were any policy errors for any other domain
	return sslPolicyErrors == SslPolicyErrors.None;
}
```

### OpenSSL

Pinning can occur at one of two places with OpenSSL. First is the user
supplied `verify_callback`. Second is after the connection is
established via `SSL_get_peer_certificate`. Either method will allow you
to access the peer's certificate.

Though OpenSSL performs the X509 checks, you must fail the connection
and tear down the socket on error. By design, a server that does not
supply a certificate will result in `X509_V_OK` with a **NULL**
certificate. To check the result of the customary verification: (1) you
must call `SSL_get_verify_result` and verify the return code is
`X509_V_OK`; and (2) you must call `SSL_get_peer_certificate` and verify
the certificate is **non-NULL**.

Download: [OpenSSL sample program](https://wiki.owasp.org/images/f/f7/Pubkey-pin-openssl.zip).

```
int pkp_pin_peer_pubkey(SSL* ssl)
{
    if(NULL == ssl) return FALSE;

    X509* cert = NULL;
    FILE* fp = NULL;

    /* Scratch */
    int len1 = 0, len2 = 0;
    unsigned char *buff1 = NULL, *buff2 = NULL;

    /* Result is returned to caller */
    int ret = 0, result = FALSE;

    do
    {
        /* http://www.openssl.org/docs/ssl/SSL_get_peer_certificate.html */
        cert = SSL_get_peer_certificate(ssl);
        if(!(cert != NULL))
            break; /* failed */

        /* Begin Gyrations to get the subjectPublicKeyInfo       */
        /* Thanks to Viktor Dukhovni on the OpenSSL mailing list */

        /* http://groups.google.com/group/mailing.openssl.users/browse_thread/thread/d61858dae102c6c7 */
        len1 = i2d_X509_PUBKEY(X509_get_X509_PUBKEY(cert), NULL);
        if(!(len1 > 0))
            break; /* failed */

        /* scratch */
        unsigned char* temp = NULL;

        /* http://www.openssl.org/docs/crypto/buffer.html */
        buff1 = temp = OPENSSL_malloc(len1);
        if(!(buff1 != NULL))
            break; /* failed */

        /* http://www.openssl.org/docs/crypto/d2i_X509.html */
        len2 = i2d_X509_PUBKEY(X509_get_X509_PUBKEY(cert), &temp);

        /* These checks are verifying we got back the same values as when we sized the buffer.      */
        /* It's pretty weak since they should always be the same. But it gives us something to test. */
        if(!((len1 == len2) && (temp != NULL) && ((temp - buff1) == len1)))
            break; /* failed */

        /* End Gyrations */

        /* See the warning above!!!                                            */
        /* http://pubs.opengroup.org/onlinepubs/009696699/functions/fopen.html */
        fp = fopen("random-org.der", "rx");
        if(NULL ==fp) {
            fp = fopen("random-org.der", "r");

        if(!(NULL != fp))
            break; /* failed */

        /* Seek to eof to determine the file's size                            */
        /* http://pubs.opengroup.org/onlinepubs/009696699/functions/fseek.html */
        ret = fseek(fp, 0, SEEK_END);
        if(!(0 == ret))
            break; /* failed */

        /* Fetch the file's size                                               */
        /* http://pubs.opengroup.org/onlinepubs/009696699/functions/ftell.html */
        long size = ftell(fp);

        /* Arbitrary size, but should be relatively small (less than 1K or 2K) */
        if(!(size != -1 && size > 0 && size < 2048))
            break; /* failed */

        /* Rewind to beginning to perform the read                             */
        /* http://pubs.opengroup.org/onlinepubs/009696699/functions/fseek.html */
        ret = fseek(fp, 0, SEEK_SET);
        if(!(0 == ret))
            break; /* failed */

        /* Re-use buff2 and len2 */
        buff2 = NULL; len2 = (int)size;

        /* http://www.openssl.org/docs/crypto/buffer.html */
        buff2 = OPENSSL_malloc(len2);
        if(!(buff2 != NULL))
            break; /* failed */

        /* http://pubs.opengroup.org/onlinepubs/009696699/functions/fread.html */
        /* Returns number of elements read, which should be 1 */
        ret = (int)fread(buff2, (size_t)len2, 1, fp);
        if(!(ret == 1))
            break; /* failed */

        /* Re-use size. MIN and MAX macro below... */
        size = len1 < len2 ? len1 : len2;

        /*************************/
        /*****    PAYDIRT    *****/
        /*************************/
        if(len1 != (int)size || len2 != (int)size || 0 != memcmp(buff1, buff2, (size_t)size))
            break; /* failed */

        /* The one good exit point */
        result = TRUE;

    } while(0);

    if(fp != NULL)
        fclose(fp);

    /* http://www.openssl.org/docs/crypto/buffer.html */
    if(NULL != buff2)
        OPENSSL_free(buff2);

    /* http://www.openssl.org/docs/crypto/buffer.html */
    if(NULL != buff1)
        OPENSSL_free(buff1);

    /* http://www.openssl.org/docs/crypto/X509_new.html */
    if(NULL != cert)
        X509_free(cert);

    return result;
}
```

## Miscellaneous

This sections covers administrivia and miscellaneous items related to
pinning.

### Ephemeral Keys

Ephemeral keys are temporary keys used for one instance of a protocol
execution and then thrown away. An ephemeral key has the benefit of
providing forward secrecy, meaning a compromise of the site or service's
long term (static) signing key does not facilitate decrypting past
messages because the key was temporary and discarded (once the session
terminated).

Ephemeral keys do not affect pinning because the Ephemeral key is
delivered in a separate `ServerKeyExchange` message. In addition, the
ephemeral key is a key and not a certificate, so it does not change the
construction of the certificate chain. That is, the certificate of
interest will still be located at `certificates[0]`.

### Pinning Gaps

There are two gaps when pinning due to reuse of the existing
infrastructure and protocols. First, an explicit challenge is **not**
sent by the program to the peer server based on the server's public
information. So the program never knows if the peer can actually decrypt
messages. However, the shortcoming is usually academic in practice since
an adversary will receive messages it can't decrypt.

Second is revocation. Clients don't usually engage in revocation
checking, so it could be possible to use a known bad certificate or key
in a pinset. Even if revocation is active, Certificate Revocation Lists
(CRLs) and Online Certificate Status Protocol (OCSP) can be defeated in
a hostile environment. An application can take steps to remediate, with
the primary means being freshness. That is, an application should be
updated and distributed immediately when a critical security parameter
changes.

### No Relationship `^@$\!`

If you don't have a pre-existing relationship, all is not lost. First,
you can pin a host or server's certificate or public key the first time
you encounter it. If the bad person was not active when you encountered the
certificate or public key, they will not be successful with future
funny business.

Second, bad certificates are being spotted quicker in the field due to
projects like [Chromium](http://www.chromium.org) and [Certificate
Patrol](https://addons.mozilla.org/en-us/firefox/addon/certificate-patrol/),
and initiatives like the EFF's [SSL Observatory](https://www.eff.org/observatory).

Third, help is on its way, and there are a number of futures that will
assist with the endeavors:

- Public Key Pinning (http://www.ietf.org/id/draft-ietf-websec-key-pinning-09.txt) – an extension to the HTTP protocol allowing web host operators to instruct user agents (UAs) to remember ("pin") the hosts' cryptographic identities for a given period of time.
- DNS-based Authentication of Named Entities (DANE) (https://datatracker.ietf.org/doc/rfc6698/) - uses Secure DNS to associate Certificates with Domain Names For S/MIME, SMTP with TLS, DNSSEC and TLSA records.
- Sovereign Keys (http://www.eff.org/sovereign-keys) - operates by providing an optional and secure way of associating domain names with public keys via DNSSEC. PKI (hierarchical) is still used. Semi-centralized with append only logging.
- Convergence (http://convergence.io) – different \[geographical\] views of a site and its associated data (certificates and public keys). Web of Trust is used. Semi-centralized.

While Sovereign Keys and Convergence still require us to confer trust to
outside parties, the parties involved do not serve share holders or
covet revenue streams. Their interests are industry transparency and
user security.

### More Information?

Pinning is an *old new thing* that has been shaken, stirred, and
repackaged. While "pinning" and "pinsets" are relatively new terms for
old things, Jon Larimer and Kenny Root spent time on the subject at
Google I/O 2012 with their talk *[Security and Privacy in Android
Apps](https://developers.google.com/events/io/sessions/gooio2012/107/)*.

### Format Conversions

As a convenience to readers, the following with convert between PEM and
DER format using OpenSSL.

```
# Public key, X509
$ openssl genrsa -out rsa-openssl.pem 3072
$ openssl rsa -in rsa-openssl.pem -pubout -outform DER -out rsa-openssl.der

# Private key, PKCS#8
$ openssl genrsa -out rsa-openssl.pem 3072
$ openssl pkcs8 -nocrypt -in rsa-openssl.pem -inform PEM -topk8 -outform DER -out rsa-openssl.der
```

## References

- OWASP [Injection Theory](../Injection_Theory "wikilink")
- OWASP [Transport Layer Protection Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Transport_Layer_Protection_Cheat_Sheet.html)
- IETF [Public Key Pinning](http://www.ietf.org/id/draft-ietf-websec-key-pinning-09.txt)
- IETF [RFC 5054 (SRP)](http://www.ietf.org/rfc/rfc5054.txt)
- IETF [RFC 4764 (EAP-PSK)](http://www.ietf.org/rfc/rfc4764.txt)
- IETF [RFC 1421 (PEM Encoding)](http://www.ietf.org/rfc/rfc1421.txt)
- IETF [RFC 5280 (Internet X.509, PKIX)](http://www.ietf.org/rfc/rfc5280.txt)
- IETF [RFC 4648 (Base16, Base32, and Base64 Encodings)](http://www.ietf.org/rfc/rfc4648.txt)
- IETF [RFC 3279 (PKI, X509 Algorithms and CRL Profiles)](http://www.ietf.org/rfc/rfc3279.txt)
- IETF [RFC 4055 (PKI, X509 Additional Algorithms and CRL Profiles)](http://www.ietf.org/rfc/rfc4055.txt)
- IETF [RFC 2246 (TLS 1.0)](http://www.ietf.org/rfc/rfc2246.txt)
- IETF [RFC 4346 (TLS 1.1)](http://www.ietf.org/rfc/rfc4346.txt)
- IETF [RFC 5246 (TLS 1.2)](http://www.ietf.org/rfc/rfc5246.txt)
- IETF [RFC 6698, Draft (DANE)](http://www.ietf.org/rfc/rfc6698.txt)
- EFF [Sovereign Keys](http://www.eff.org/sovereign-keys)
- Thoughtcrime Labs [Convergence](http://convergence.io/)
- RSA Laboratories [PKCS\#1, RSA Encryption Standard](http://www.rsa.com/rsalabs/node.asp?id=2125)
- RSA Laboratories [PKCS\#6, Extended-Certificate Syntax Standard](http://www.rsa.com/rsalabs/node.asp?id=2128)
- ITU [Specification of Basic Encoding Rules (BER), Canonical Encoding Rules (CER) and Distinguished Encoding Rules (DER)](http://www.itu.int/rec/T-REC-X.690-200811-I/en)
- TOR Project [Detecting Certificate Authority Compromises and Web Browser Collusion](https://blog.torproject.org/blog/detecting-certificate-authority-compromises-and-web-browser-collusion)
- Code Project [Cryptographic Interoperability: Keys](http://www.codeproject.com/Articles/25487/Cryptographic-Interoperability-Keys)
- Google I/O [Security and Privacy in Android Apps](https://developers.google.com/events/io/sessions/gooio2012/107/)
- Trevor Perrin [Transparency, Trust Agility, Pinning (Recent Developments in Server Authentication)](https://crypto.stanford.edu/RealWorldCrypto/slides/perrin.pdf)
- Dr. Peter Gutmann's [PKI is Broken](http://www.cs.auckland.ac.nz/~pgut001/pubs/pkitutorial.pdf)
- Dr. Matthew Green's [The Internet is Broken](http://blog.cryptographyengineering.com/2012/02/how-to-fix-internet.html)
- Dr. Matthew Green's [How do Interception Proxies fail?](http://blog.cryptographyengineering.com/2012/03/how-do-interception-proxies-fail.html)
- Presentation: [SSL Pinning implementation and bypasses for iOS and Android](http://www.slideshare.net/anantshri/ssl-pinning-and-bypasses-android-and-ios)
