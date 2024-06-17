---

layout: col-sidebar
title: Subresource Integrity (SRI)  
author: Vaibhav Malik
tags: [controls, application, web]
permalink: /controls/SubresourceIntegrity

---

{% include writers.html %}


## Description

Subresource Integrity (SRI) is a security mechanism that allows web browsers to check the integrity of resources they 
fetch from external sources, such as Content Delivery Networks (CDNs). SRI ensures that the resources are delivered without
any unexpected modifications or tampering. With SRI, you can specify a cryptographic hash value that the fetched resource 
must match before the browser accepts and uses it. This helps protect against scenarios where an attacker might attempt to 
inject malicious code into a resource, or where a CDN might accidentally serve corrupted files. By using SRI, you can 
enhance the security of your web application and provide an extra layer of protection for your users.

Web sites often rely on resources hosted on third-party servers, such as 
JavaScript libraries or CSS stylesheets. However, using these resources introduces risks:

1. The third-party server could get compromised, leading to the resources being modified to include malicious content.
2. Network attacks could modify the resources en route from the third-party server to the user's browser.

SRI helps mitigate these risks by ensuring that the browser only executes resources 
that match the expected hash. If the resource doesn't match the hash, the browser won't 
load it, protecting the page and users from potential attacks.

To use SRI, you specify the hash of the resource you're expecting 
in the `integrity` attribute of the `<script>` or `<link>` tag:

```html
<script src="https://example.com/example-framework.js"
        integrity="sha384-oqVuAfXRKap7fdgcCY5uykM6+R9GqQ8K/uxy9rx7HNQlGYl1kPzQho1wx4JwY8wC"
        crossorigin="anonymous"></script>
```

SRI provides several key benefits:
- Ensures integrity of externally hosted resources
- Detects and prevents execution of tampered code
- Complements other security measures like HTTPS and CSP
- Helps maintain trust in third-party content

However, SRI also introduces some considerations:
- Requires knowledge of expected resource hashes
- Can break sites if resource updates change hashes
- Doesn't protect against compromise of the main site itself

## Sample Code

Here's how you might implement SRI in a web page:

```html
<!DOCTYPE html>
<html>
  <head>
    <title>SRI Example</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css"
          integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm"
          crossorigin="anonymous">
  </head>
  <body>
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"
            integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN"
            crossorigin="anonymous"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
            integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl"
            crossorigin="anonymous"></script>

    <div class="container">
      <h1>Hello, world!</h1>
      <p>This is an example of a site using SRI.</p>
    </div>
  </body>
</html>
```

This page loads Bootstrap CSS and JavaScript from a CDN, as well as jQuery.
Each of these external resources has an `integrity` attribute with a hash of the 
expected content. If any of these resources are altered, the hashes won't match and the browser won't load them.

To generate the `integrity` hashes, you can use a tool like [SRI Hash Generator](https://www.srihash.org/). For example, to generate the hash for the Bootstrap CSS:

1. Go to [https://www.srihash.org/](https://www.srihash.org/)
2. Enter the URL of the resource (in this case, `https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css`)
3. Click "Generate"
4. Copy the `integrity` attribute provided

It's important to note that if the resource is updated (for 
example, if you upgrade to a new version of Bootstrap), you'll 
need to update the `integrity` hash to match the new version. If you don't, the resource will fail to load.

SRI is a powerful control for ensuring the integrity of third-party resources,
 but it's not a complete security solution on its own. It should be used 
 in combination with other security best practices, like serving your site over 
 HTTPS and using Content Security Policy (CSP).

## References

- [MDN Web Docs: Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity)
- [Can I use... Subresource Integrity?](https://caniuse.com/#feat=subresource-integrity)
- [SRI Hash Generator](https://www.srihash.org/)
- [OWASP Cheat Sheet Series: Third Party JavaScript Management](https://cheatsheetseries.owasp.org/cheatsheets/Third_Party_Javascript_Management_Cheat_Sheet.html)

