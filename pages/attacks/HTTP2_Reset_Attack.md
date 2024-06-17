
---

layout: col-sidebar
title: HTTP/2 Reset Attack
author: Vaibhav Malik
tags: [attacks, application, web]
permalink: /attacks/HTTP2_Reset_Attack

---

{% include writers.html %}

## Description

HTTP/2 is an iteration of the HTTP protocol, designed to improve 
performance and security compared to HTTP/1.1. However, a vulnerability 
in the HTTP/2 protocol, known as the "Rapid Reset Vulnerability", was discovered that 
could allow an attacker to terminate connections and prevent assets from loading.

In an HTTP/2 Reset Attack, the attacker sends a crafted RST_STREAM frame 
to abruptly terminate an established stream. If this RST_STREAM frame is 
sent before the client receives the complete response from the server, the 
browser will discard the partial response and will not render or execute any 
further data on that stream. This can lead to pages failing to load completely, 
or specific resources like images, stylesheets, or scripts being blocked.

The attack is possible because HTTP/2 allows a client or a server to 
terminate a stream at any time by sending an RST_STREAM frame with an 
error code. The protocol does not require any verification of whether 
the sender is authorized to close the stream. An attacker can exploit 
this by sending a forged RST_STREAM frame, pretending to be the server.

## Example Scenario

Suppose a web page includes a critical JavaScript file:

```html
<script src="/core.js"></script>
```

An attacker who can monitor the network traffic (e.g., on an public
 Wi-Fi network) can observe when the browser requests `/core.js`. 
 Before the server can complete sending the response, the attacker 
 sends a forged RST_STREAM frame with an error code (e.g., REFUSED_STREAM). 

```
RST_STREAM
  Stream ID: 5
  Error Code: REFUSED_STREAM (0x7)
```

Upon receiving this frame, the browser will abort the stream and 
will not process any further data received on that stream. As a 
result, the `core.js` file will not be loaded, potentially breaking the functionality of the page.

## Impact

The HTTP/2 Reset Attack can lead to:

1. Broken functionality: If essential resources like scripts or stylesheets are blocked, the page may not function or display as intended.
2. Degraded performance: Blocked resources will need to be re-requested, adding latency to page loads.
3. Vulnerabilities introduced: If security-critical resources like a Content Security Policy (CSP) are blocked, the page may become vulnerable to cross-site scripting (XSS) and other attacks.

## Mitigation

There are several ways to mitigate HTTP/2 Reset Attacks:

1. Ignore RST_STREAM with idle streams: Clients should ignore RST_STREAM frames received on idle streams. If no request has been sent on a stream, a RST_STREAM is not valid.
2. Authenticate RST_STREAM: Optionally, clients could authenticate RST_STREAM frames to ensure they originate from the server and not from an attacker. This would require extending the HTTP/2 protocol.
3. Use HTTPS: Encrypting the traffic with HTTPS (TLS) prevents attackers from seeing which resources are being requested and from injecting forged frames.
4. Load critical resources early: Load the most critical resources as early as possible in the page lifecycle to reduce the window of vulnerability.

Ultimately, the HTTP/2 specification needs to be updated to address this vulnerability. Work is underway to amend the spec and provide clear guidance to implementers.

## References
- [HTTP/2 Reset Attack paper](https://www.usenix.org/system/files/sec22summer_hossain-sazzad.pdf)
- [RFC 9113 - HTTP/2](https://www.rfc-editor.org/rfc/rfc9113.html)
- [Cloudflare Blog - HTTP/2 Reset Attack](https://blog.cloudflare.com/technical-breakdown-http2-rapid-reset-ddos-attack)
- [CVE-2023-44487](https://nvd.nist.gov/vuln/detail/CVE-2023-44487)

[[:Category:Attack]](https://owasp.org/www-community/attacks/)
