---
layout: col-sidebar
title: Password Spraying Attack
author: Rishu Ranjan
contributors: 
permalink: /attacks/Password_Spraying_Attack
tags: attack, password spraying
---

{% include writers.html %}

## Description
**Password spraying** is a type of brute force attack. In this attack, an attacker will brute force logins based on list of usernames with default passwords on the application. 
For example, an attacker will use one password (say, Secure@123) against many different accounts on a application to avoid account lockouts that would normally occur when brute forcing a single account with many passwords.

This attack can be found commonly where the application or admin sets a default password for the new users.

![psa](https://user-images.githubusercontent.com/51092706/116527869-c24b4280-a8f8-11eb-9023-edc0601d4504.png)

## Mitigations
- Brute force preventation should be on both field, i.e., Username and Password.
- Set account lockout policies after a certain number of failed login attempts to prevent credentials from being guessed. Implement CAPTCHA, if lockout is not a viable option.
- The admin managed application should force users to change their password on first login with default password.
- Use multi-factor authentication. Where possible, also enable multi-factor authentication on externally facing services.

## Reference
- https://attack.mitre.org/techniques/T1110/003/
