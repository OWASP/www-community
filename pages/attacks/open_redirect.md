---

layout: col-sidebar
title: Open Redirect
author: Dmytro Knivets
contributors:
permalink: /attacks/open_redirect
tags: attack, Open Redirect

---

{% include writers.html %}

## Overview

Open Redirect (also known as Unvalidated Redirects and Forwards) is an attack that occurs when a web application redirects users to a URL supplied via an unvalidated parameter. While open redirects can be used for phishing on their own, their primary value to attackers is as a component in exploit chains — they allow an attacker to bypass domain-based validation checks and redirect security-sensitive flows (such as OAuth authorization) through the legitimate domain to an attacker-controlled destination.

Open Redirect is classified under **Broken Access Control** (A01:2025) in the [OWASP Top 10](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/index.html).

## Description

Many web applications redirect users as part of normal workflows — for example, redirecting back to a requested page after login, forwarding to a partner site after completing an action, or handling OAuth callback URLs. When the redirect target comes from user-controlled input and is not validated, an attacker can substitute a malicious URL.

The most common use of open redirects is **phishing**. Because the link starts with a legitimate domain (e.g., `https://example.com/login?next=...`), victims trust it and click through. The application then silently redirects them to an attacker-controlled site that mimics the real login page, harvesting their credentials.

However, the main danger of open redirects is that they serve as **building blocks in exploit chains**. Security-critical systems like OAuth authorization servers validate that `redirect_uri` belongs to a trusted domain. If that trusted domain contains an open redirect, the attacker can supply a `redirect_uri` that passes validation (because it points to the legitimate domain) but ultimately forwards the user — along with authorization codes or tokens in the URL — to an attacker-controlled server. Similarly, open redirects can bypass SSRF protections when a server-side request to a trusted domain gets redirected to an internal resource.

Open redirects commonly appear in login flows (`/login?next=`), post-action redirects (`/logout?return_to=`), and generic redirect endpoints (`/go?url=`) often left over from marketing or link-tracking features.

## Examples

### Example 1 — Vulnerable login redirect

A web application redirects users to a URL provided in the `next` query parameter after successful login. The server performs no validation on the redirect target.

#### Malicious link

```
https://example.com/login?next=https://evil.com/fake-login
```

The victim sees a link starting with `example.com` and trusts it. After logging in, the application redirects them to the attacker's site.

#### Vulnerable server code (Python / Flask)

```python
@app.route("/login", methods=["GET", "POST"])
def login():
    next_url = request.args.get("next", "/")

    if request.method == "POST" and authenticate(request.form):
        session["user"] = request.form["username"]
        # No validation — redirects to any URL the client supplies
        return redirect(next_url)

    return render_template("login.html")
```

#### Fixed version

```python
from urllib.parse import urlparse

ALLOWED_HOSTS = {"example.com", "www.example.com"}

@app.route("/login", methods=["GET", "POST"])
def login():
    next_url = request.args.get("next", "/")

    if request.method == "POST" and authenticate(request.form):
        session["user"] = request.form["username"]

        # Validate: only allow relative paths or URLs on allowed hosts
        parsed = urlparse(next_url)
        if parsed.netloc and parsed.netloc not in ALLOWED_HOSTS:
            next_url = "/"

        return redirect(next_url)

    return render_template("login.html")
```

### Example 2 — Encoded and obfuscated URL bypasses

Attackers use URL encoding, userinfo abuse, and protocol-relative URLs to bypass naive redirect validation. Even if a developer checks whether the URL "starts with" the trusted domain, these techniques can defeat simple string matching.

| Technique | Malicious URL | Why it works |
|---|---|---|
| Userinfo abuse | `https://example.com@evil.com/path` | The browser treats `example.com` as the [userinfo](https://datatracker.ietf.org/doc/html/rfc3986#section-3.2.1) component and navigates to `evil.com` |
| Protocol-relative URL | `//evil.com` | The browser uses the current page's scheme and navigates to `evil.com` |
| URL encoding | `/login?next=https%3A%2F%2Fevil.com` | The server decodes the parameter and redirects to `https://evil.com` |
| Backslash trick | `https://evil.com\@example.com` | Some URL parsers treat `\` as a path separator, causing inconsistent parsing |
| Subdomain confusion | `https://example.com.evil.com` | A check for "contains example.com" passes, but the actual host is `evil.com` |

These bypasses demonstrate why blocklist and simple string-matching approaches are insufficient. Proper URL parsing and strict allowlist validation are required.

### Example 3 — OAuth token theft via open redirect

An open redirect can be chained with OAuth to steal authorization codes. This attack exploits OAuth implementations that do not enforce exact `redirect_uri` matching or do not require [PKCE](https://oauth.net/2/pkce/).

Suppose `example.com` has an open redirect at `/go?url=`. The attacker crafts an OAuth authorization URL, setting `redirect_uri` to the open redirect endpoint:

```
https://auth.example.com/authorize?
  response_type=code&
  client_id=example-app&
  redirect_uri=https://example.com/go?url=https://evil.com/collect&
  scope=read
```

1. The victim clicks the crafted link. The authorization server sees that `redirect_uri` starts with `https://example.com` and passes validation.
2. The victim authenticates (or is already logged in) and consents.
3. The authorization server redirects to: `https://example.com/go?url=https://evil.com/collect&code=AUTHORIZATION_CODE`
4. The open redirect at `example.com` forwards the victim to: `https://evil.com/collect&code=AUTHORIZATION_CODE`
5. The attacker's server receives the authorization code and exchanges it for an access token.

To mitigate this, OAuth implementations should enforce exact `redirect_uri` matching against pre-registered values, so that an open redirect on the same domain cannot be substituted for the legitimate callback URL.

### Example 4 — SSRF filter bypass via open redirect

An open redirect on a trusted domain can bypass server-side URL validation. In this example, an application fetches URL previews (e.g., link unfurling in a chat app) and validates the URL before making the request.

#### Vulnerable server code (Python / Flask)

```python
import requests

@app.route("/api/link-preview", methods=["POST"])
def link_preview():
    url = request.json["url"]

    # validate URL against allowlist of trusted hosts
    if not is_allowed_url(url):
        abort(403)

    # server follows redirects by default
    resp = requests.get(url)
    return jsonify({"title": extract_title(resp.text)})
```

The attacker knows that `trusted-site.com` has an open redirect at `/go?url=`. They submit:

```
https://trusted-site.com/go?url=http://169.254.169.254/latest/meta-data/iam/security-credentials/
```

1. The server validates the URL — `trusted-site.com` passes `is_allowed_url()`, so the request proceeds.
2. The server makes a GET request to `trusted-site.com`, which responds with a 302 redirect to `http://169.254.169.254/...`.
3. The HTTP client follows the redirect and fetches AWS instance metadata, including IAM credentials.
4. The server returns the content to the attacker.

#### Fixed version

```python
import requests

@app.route("/api/link-preview", methods=["POST"])
def link_preview():
    url = request.json["url"]

    # validate URL against allowlist of trusted hosts
    if not is_allowed_url(url):
        abort(403)

    # do not follow redirects — reject if the response is not final
    resp = requests.get(url, allow_redirects=False)

    if resp.is_redirect:
        abort(502, "Unexpected redirect")

    return jsonify({"title": extract_title(resp.text)})
```

For comprehensive SSRF prevention including URL validation, see the [Server-Side Request Forgery Prevention Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Server_Side_Request_Forgery_Prevention_Cheat_Sheet.html).

## How to Prevent

- **Use your language's built-in URL parsing functions.** Never parse or validate URLs with string operations (startsWith, contains, regex). Use standard library functions like Python's `urllib.parse.urlparse`, JavaScript's `new URL()`, or Java's `java.net.URI`. These handle encoding, authority components, and edge cases that manual parsing will miss.
- **Prefix the destination with your base domain.** If the redirect target should be a path within your application, prepend your domain before redirecting: `redirect("https://example.com" + path)`. This ensures the result is always on your domain regardless of what the user supplies.
- **Use an allowlist of permitted domains.** When redirecting to external domains is required, parse the URL with a standard library and compare the hostname against a strict allowlist of trusted domains.
- **Do not rely on blocklists or string matching.** Encoding tricks, userinfo abuse, and parser inconsistencies make blocklist approaches easy to bypass (see Example 2).
- **Display an interstitial warning for external redirects.** If the application must redirect to user-supplied external URLs, show a warning page: "You are about to leave example.com" with the full destination URL visible, so the user can make an informed decision.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Server Side Request Forgery](https://owasp.org/www-community/attacks/Server_Side_Request_Forgery)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

- Broken Access Control (OWASP Top 10 A01:2025)

## References

- CWE-601: URL Redirection to Untrusted Site ('Open Redirect') — <https://cwe.mitre.org/data/definitions/601.html>
- OWASP Testing Guide: Testing for Client-side URL Redirect — <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/11-Client-side_Testing/04-Testing_for_Client-side_URL_Redirect>
- OWASP Cheat Sheet: Unvalidated Redirects and Forwards — <https://cheatsheetseries.owasp.org/cheatsheets/Unvalidated_Redirects_and_Forwards_Cheat_Sheet.html>
