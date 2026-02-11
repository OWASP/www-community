---

layout: col-sidebar
title: Insecure Direct Object Reference (IDOR)
author: Dmytro Knivets
contributors:
permalink: /attacks/insecure_direct_object_reference
tags: attack, IDOR

---

{% include writers.html %}

## Overview

Insecure Direct Object Reference (IDOR) is an access control vulnerability that occurs when an application exposes internal object references — such as database keys, file names, or record IDs — and fails to verify that the requesting user is authorized to access the referenced object. An attacker can exploit this by modifying the reference value to access resources belonging to other users.

IDOR is classified under **Broken Access Control** (A01:2025) in the [OWASP Top 10](https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/index.html).

## Description

Web applications frequently use user-supplied input to directly reference objects. For example, a URL like `/api/users/123/profile` uses the ID `123` to look up a specific user record. When the application does not verify that the authenticated user is authorized to access that particular record, an attacker can simply change `123` to `124` to view or modify another user's data.

IDOR vulnerabilities can appear in:

- **URL path parameters:** `/invoices/1042` changed to `/invoices/1043`
- **Query string parameters:** `?order_id=7001` changed to `?order_id=7002`
- **Request body fields:** JSON or form data containing object identifiers
- **File references:** `?file=report_user1.pdf` changed to `?file=report_user2.pdf`

The core issue is that the application trusts the client to supply a valid reference without enforcing server-side authorization checks. Even if object identifiers are not sequential, an attacker who can obtain or guess another user's identifier can exploit the flaw.

## Examples

### Example 1 — Vulnerable API endpoint

A REST API returns a user's profile based on the ID in the URL path. The server retrieves the record but never checks whether the authenticated user is allowed to access it.

**Request:**

```http
GET /api/users/124/profile HTTP/1.1
Host: example.com
Authorization: Bearer <token_for_user_123>
```

**Vulnerable server code (Python / Flask):**

```python
@app.route("/api/users/<int:user_id>/profile")
@login_required
def get_profile(user_id):
    # No authorization check — any authenticated user can access any profile
    profile = db.session.get(UserProfile, user_id)
    if profile is None:
        abort(404)
    return jsonify(profile.to_dict())
```

Because the endpoint only checks that the caller is *authenticated* (via `@login_required`), user 123 can retrieve user 124's profile simply by changing the ID in the URL.

**Fixed version:**

```python
@app.route("/api/users/<int:user_id>/profile")
@login_required
def get_profile(user_id):
    if current_user.id != user_id:
        abort(403)
    profile = db.session.get(UserProfile, user_id)
    if profile is None:
        abort(404)
    return jsonify(profile.to_dict())
```

### Example 2 — Document download

An application serves documents based on a filename parameter:

```
https://example.com/documents?file=invoice_1001.pdf
```

An attacker changes the parameter:

```
https://example.com/documents?file=invoice_1002.pdf
```

If the server does not verify that the requested file belongs to the authenticated user, the attacker downloads another user's invoice.

## How to Prevent

- **Enforce server-side authorization checks.** Every request that accesses an object must verify that the authenticated user has permission to access that specific object. Do not rely solely on authentication.
- **Use non-guessable object references.** Avoid exposing sequential database primary keys. Use UUIDs (v4) or other random identifiers to make enumeration impractical. For higher security, map references to per-session random tokens that the server resolves internally. Note that non-guessable identifiers reduce the attack surface but are not a substitute for authorization checks — a leaked UUID still exposes the resource.
- **Apply the principle of least privilege.** Ensure that database queries and data access layers are scoped to the current user's permissions (e.g., `SELECT * FROM orders WHERE user_id = :current_user AND id = :order_id`).
- **Validate access at the data layer.** Centralize authorization logic so that every data access path — not just controller endpoints — enforces ownership or role-based checks.
- **Log and monitor access patterns.** Detect sequential enumeration attempts (e.g., a single user requesting IDs 1 through 1000) as potential IDOR exploitation.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Forced browsing](https://owasp.org/www-community/attacks/Forced_browsing)
- [Web Parameter Tampering](https://owasp.org/www-community/attacks/Web_Parameter_Tampering)
- [Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)
- [CSRF](https://owasp.org/www-community/attacks/csrf)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

- Broken Access Control (OWASP Top 10 A01:2025)

## References

- CWE-639: Authorization Bypass Through User-Controlled Key — <https://cwe.mitre.org/data/definitions/639.html>
- OWASP Top 10 A01:2025 — Broken Access Control — <https://owasp.org/Top10/2025/A01_2025-Broken_Access_Control/index.html>
- OWASP Testing Guide: Testing for IDOR — <https://owasp.org/www-project-web-security-testing-guide/latest/4-Web_Application_Security_Testing/05-Authorization_Testing/04-Testing_for_Insecure_Direct_Object_References>
- OWASP Cheat Sheet: Authorization — <https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html>
