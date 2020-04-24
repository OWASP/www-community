---

layout: col-sidebar
title: Allowing Domains or Accounts to Expire
author: 
contributors: 
permalink: /vulnerabilities/Allowing_Domains_or_Accounts_to_Expire
tags: vulnerability, Allowing Domains or Accounts to Expire

---

{% include writers.html %}

## Description

Through neglect an administrator may allow a domain name or e-mail account to expire. Domains have a significant grace period for expiration, and e-mail addresses using free services such as Yahoo may expire after several months of not logging in.

## Risk Factors

- The biggest risk involved is if you have an e-mail server on a domain that is allowed to expire. The more users there are, the more personal information you are putting at risk when they use those e-mails as backup e-mails for accounts on websites. An attacker can simply purchase the domain and setup a mailserver. By analyzing the spam coming in, they can determine the actual usernames people used on the domain and possibly what services they used with those e-mails.
- Considering that, you should be careful only to use e-mails hosted on domains owned by companies that don't show any sign of going under in the future.
- There is very little recourse if a malicious entity has purchased your domain. They can sell it back to you for however much money they want to charge. Even if you have grounds for a lawsuit, it can take months at least.
- If you have applications(especially no-longer supported) sending data to a domain, if an attacker buys the domain they can gather personal information from your users.
- Domains most likely to expire are those belonging to projects or companies that no longer exist.