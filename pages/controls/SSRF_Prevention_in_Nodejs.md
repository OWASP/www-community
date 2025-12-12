---
title: SSRF Prevention in Node.js
layout: col-sidebar
tags: SSRF, Node.js, URL validation, DNS, redirects, security
author: "RelunSec"
---

{% include writers.html %}

## Introduction

Server-Side Request Forgery (SSRF) is a class of vulnerabilities where an attacker tricks a server into making unintended requests.  
Node.js applications are especially exposed because many libraries accept user-provided URLs without performing proper validation, normalization, or DNS/IP safety checks.

This page provides practical guidance for preventing SSRF in Node.js applications using safe-by-construction techniques aligned with OWASP recommendations.


## Why SSRF Is Hard to Prevent in Node.js

Many SSRF defenses fail because they rely on **blacklists**, **regex checks**, or **string matching**. These approaches are ineffective against:

- URL parsing inconsistencies  
- Unicode and percent-encoding tricks  
- DNS rebinding  
- Redirect chains  
- IPv6 edge cases  
- Encoded or alternative IP representations  
- Protocol smuggling  

Node’s built-in `URL` parser and many third-party libraries do not automatically protect against these issues.



## Common Pitfalls

### 1. Using regex to validate URLs
Regex cannot safely parse URLs and fails against encoded payloads, nested schemes, and normalization tricks.

### 2. Checking only the hostname string
Attackers can bypass hostname checks using:
- DNS rebinding  
- Redirects  
- Alternate IP formats  
- IPv6-mapped IPv4  
- Octal/hexadecimal IPs  

### 3. Trusting the initial DNS resolution
A hostname may resolve to a safe IP or domain at first, then later resolve to an internal IP as known DNS rebinding attack.

### 4. Ignoring redirects
A safe-looking URL may redirect to:
- `127.0.0.1`
- `::1`
- cloud metadata endpoints
- internal services

### 5. Not normalizing URLs
Attackers can use:
- backslashes  
- mixed slashes  
- Unicode homoglyphs  
- embedded credentials  
- malformed schemes  

to bypass naive filters.

## Recommended Defense Strategy

A robust SSRF defense in Node.js should include **all** of the following steps:

### 1. Normalize the URL
- Convert Unicode to canonical form  
- Replace backslashes with forward slashes  
- Remove embedded credentials (`user@host`)  
- Normalize repeated slashes  
- Validate the scheme before parsing  

### 2. Restrict allowed protocols
Allow only:
- `http`
- `https`

Block:
- `file`
- `gopher`
- `ftp`
- `data`
- `javascript`
- `jar`
- `dict`
- `smb`
- and all non-HTTP schemes

### 3. Parse using the WHATWG URL API
This ensures consistent handling of:
- IPv6 literals  
- ports  
- credentials  
- normalization  

### 4. Resolve the hostname
Perform DNS resolution and classify the resulting IPs.

Block:
- RFC1918 private ranges  
- loopback ranges  
- link-local ranges  
- IPv6 local addresses  
- cloud metadata IPs  
- multicast/broadcast ranges  

### 5. Validate redirect chains
For each redirect:
- normalize the URL  
- validate the scheme  
- resolve the hostname  
- classify the resulting IP  

Reject the entire request if any redirect leads to an internal or unsafe IP.

### 6. Enforce timeouts and safe HTTP clients
Use:
- short timeouts  
- no automatic redirects  
- no automatic retries  

