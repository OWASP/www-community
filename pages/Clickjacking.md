---

layout: col-sidebar  
title: Clickjacking  
author: Purushottam sarsekar 
contributors:  
tags: Web Security, Clickjacking, UI Redress  
permalink: /Clickjacking  

---

{% include writers.html %}

## Overview

**Clickjacking**, also known as **User Interface (UI) Redress Attack**, is a malicious technique where an attacker tricks a user into clicking on something different from what the user perceives. This is usually done by hiding a legitimate UI component (e.g., a "Like" button, file download, or form submission) underneath a seemingly harmless interface. When users interact with the visible interface, they unknowingly perform actions on the hidden elements.

This attack is a serious concern for websites with sensitive actions like financial transactions, social media sharing, or privileged operations, as it can lead to unauthorized actions or data exposure without the user's knowledge.

## Description

Clickjacking leverages HTML and CSS to create a layered interface where the visible content does not align with the actual action being performed. The attacker often uses techniques such as:

- Transparent iframes
- Z-index manipulation
- CSS opacity tricks
- Full-screen modes to hide browser UI

By exploiting these techniques, the attacker can frame the victim site and overlay misleading content, deceiving users into performing unintended actions like:

- Enabling webcam/microphone
- Making purchases
- Sharing content
- Changing settings

## Risks

Clickjacking can result in:

- Compromise of user accounts or credentials  
- Unintentional sharing or posting of sensitive content  
- Misuse of device permissions (camera, mic, geolocation)  
- Financial loss through fraudulent transactions  
- UI/UX manipulation undermining trust in the application

## Real-World Examples

- **Facebook Likejacking**: Attackers trick users into "liking" a Facebook page via a hidden iframe embedded under a fake video play button.
- **Twitter Clickjacking**: Tricking users into following accounts or retweeting links without their consent.
- **Adobe Flash Exploits**: Old versions of Flash allowed transparent overlays to access camera/mic permissions via clickjacking.

## Mitigations

### 1. Use Framebusting Techniques

Prevent your site from being embedded inside iframes:

```html
<script>
  if (top !== self) {
    top.location = self.location;
  }
</script>
```

⚠️ Not foolproof: Framebusting can be bypassed in some browsers or environments.

### 2. HTTP Headers

#### X-Frame-Options (Deprecated but still useful)

- `DENY`: Prevents all framing
- `SAMEORIGIN`: Allows framing from the same origin only

```http
X-Frame-Options: DENY
```

#### Content-Security-Policy (CSP) `frame-ancestors` Directive

Modern and preferred method:

```http
Content-Security-Policy: frame-ancestors 'none';
```

Or limit to specific origins:

```http
Content-Security-Policy: frame-ancestors 'self' https://trustedpartner.com;
```

### 3. UI Defenses

- Add visual cues or CAPTCHA before sensitive actions  
- Require re-authentication for high-privilege operations  
- Disable click-through on sensitive controls using JavaScript or CSS  

### 4. Use Sandbox Iframes

When embedding third-party content, use the `sandbox` attribute to limit its capabilities:

```html
<iframe src="https://example.com" sandbox="allow-scripts"></iframe>
```

## Detection

- Use security scanners or penetration testing tools to detect clickjacking vulnerabilities.
- Implement client-side monitoring for suspicious iframe usage or behavior anomalies.

## Testing for Clickjacking

Manual test:

1. Create a test page with an iframe embedding your target site.
2. Set the iframe to `opacity: 0.1` or fully transparent.
3. Place fake UI controls over real buttons.
4. Test if user interactions on the top layer trigger actions in the embedded site.

If successful, the target site is vulnerable.

Tools:

- [OWASP Clickjacking Test Page](https://owasp.org/www-community/attacks/Clickjacking)
- Browser developer tools
- Custom test harnesses

## Best Practices

- Always set appropriate security headers
- Educate developers about UI security
- Regularly audit front-end and embedded resources
- Avoid mixing trusted and untrusted content in the same interface
- Use iframe sandboxing for embedded third-party resources

## Related Attacks

- **UI Redressing**: A broader category of which clickjacking is a subset
- **Tapjacking**: Variant on mobile platforms
- **Cross-Site Request Forgery (CSRF)**: Often used in combination with clickjacking

## References

- [OWASP Clickjacking](https://owasp.org/www-community/attacks/Clickjacking)
- [Clickjacking Defense Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Clickjacking_Defense_Cheat_Sheet.html)
- [Mozilla Developer Docs – X-Frame-Options](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/X-Frame-Options)
- [CSP: frame-ancestors Directive](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy/frame-ancestors)