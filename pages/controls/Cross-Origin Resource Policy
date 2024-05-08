---

layout: col-sidebar
title: Cross-Origin Resource Policy (CORP)
author: Vaibhav Malik
tags: [controls, application, web]
permalink: /controls/CrossOriginResourcePolicy

---

{% include writers.html %}

## Description

Cross-Origin Resource Policy (CORP) is a web platform security feature that 
allows websites to control which origins can load their resources. It 
mitigates the risk of cross-origin information leaks by ensuring that 
resources like images, scripts, and sub-documents are loaded only by authorized origins.

CORP is implemented via an HTTP response header that specifies one of three 
resource-sharing policies:

1. **Cross-Origin-Resource-Policy : same-site** - The resource can only be 
loaded from the same site, i.e., the same origin or a subdomain of the 
serving origin. This is the default behavior if no CORP header is present.
2. **Cross-Origin-Resource-Policy : same-origin** - This is the most 
restrictive policy. The resource can only be loaded from the exact 
same origin, excluding subdomains.
3. **Cross-Origin-Resource-Policy : cross-origin** - The resource can 
be loaded from any origin. This opt-out of protections should be used 
sparingly and only for public resources.

CORP complements cross-origin protections like Cross-Origin Resource 
Sharing (CORS) and Same-Origin Policy (SOP). While CORS and SOP restrict 
access from a requesting website's perspective, CORP enforces restrictions from the serving website's side.

CORP provides several security benefits:

- **Prevents cross-origin information leaks** - Sensitive resources 
accidentally exposed without CORS cannot be loaded by unauthorized external websites.
- **Mitigates speculative execution side-channel attacks** - Untrusted origins 
cannot load resources that might be impacted by CPU speculative execution vulnerabilities like Spectre.
- **Protects against timing attacks** - Measuring the time taken to load a 
cross-origin resource cannot be used to infer sensitive information.
- **Reduces attack surface** - Unauthorized origins cannot include a 
website's resources in their pages, minimizing avenues for clickjacking, UI redressing, etc.

However, CORP also introduces some considerations:

- **Browser support** : CORP is a relatively new standard that may not 
be supported by older browsers. Fallback protection may be needed.
- **Resource isolation** - Resources served with a restrictive CORP 
policy must not depend on external origins for proper rendering or functioning.
- **Subdomain configuration** - The `same-site` policy allows resource 
loading from subdomains. Each subdomain should carefully set its own 
CORP headers to avoid unintended exposure.

## Sample Code

Below is an example of setting CORP headers in a Node.js/Express application:

```javascript
const express = require('express');
const app = express();

// Serve public resources with cross-origin access
app.use('/public', express.static('public', {
  setHeaders: (res, path, stat) => {
    res.set('Cross-Origin-Resource-Policy', 'cross-origin');
  }
}));

// Serve sensitive resources only to same-origin 
app.use('/private', express.static('private', {
  setHeaders: (res, path, stat) => {
    res.set('Cross-Origin-Resource-Policy', 'same-origin');
  }
}));

// Set default CORP policy to same-site for the rest of the app
app.use((req, res, next) => {
  res.set('Cross-Origin-Resource-Policy', 'same-site');
  next();
});

app.get('/', (req, res) => {
  res.send('Hello World!');
});

app.listen(3000, () => {
  console.log('Server started on port 3000');
});
```

This code sets up an Express server with three CORP policies:
- The `/public` route serves resources that can be loaded by any origin.  
- The `/private` route serves resources that can only be loaded by the same origin.
- The rest of the app defaults to the `same-site` policy, allowing loading from the same site and its subdomains.

To test the policies, you can host an HTML file on a different origin that tries to load resources from this server:

```html
<!DOCTYPE html>
<html>
<head>
  <title>CORP Test</title>
</head>
<body>
  <h1>Attempting cross-origin loads...</h1>
  
  <!-- This will load successfully due to the cross-origin policy -->
  <img src="http://example.com:3000/public/image.jpg">
  
  <!-- This will be blocked by the same-origin policy -->
  <img src="http://example.com:3000/private/sensitive.jpg">

  <!-- This will be blocked by the default same-site policy -->  
  <img src="http://example.com:3000/cat.jpg">
</body>
</html>
```

When loaded from a different origin, only the `/public/image.jpg` resource will successfully load. The other two images will be blocked by CORP.

In conclusion, the Cross-Origin Resource Policy is a robust security control for protecting sensitive web resources from unauthorized cross-origin access. When properly configured, it provides defense-in-depth alongside CORS and SOP. Web developers should leverage CORP headers to enhance the isolation and integrity of their applications.

## References

- [MDN Web Docs: Cross-Origin Resource Policy (CORP)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Cross-Origin_Resource_Policy_(CORP))
- [web.dev: Protect your resources from web attacks with Fetch Metadata](https://web.dev/fetch-metadata/)
- [Fetch Metadata Request Headers playground](https://secmetadata.appspot.com/)
- [OWASP Cheat Sheet Series: Cross-Origin Resource Sharing](https://cheatsheetseries.owasp.org/cheatsheets/Cross-Origin_Resource_Sharing_Cheat_Sheet.html)

