---
title: "SIM Swapping Prevention"
description: "Guidelines for preventing SIM swapping attacks targeting users, organizations, and developers."
tags: ["security", "authentication", "sim-swapping", "2fa"]
---

# SIM Swapping Prevention

## Overview
SIM swapping, also known as SIM hijacking, is a type of account takeover attack where an attacker convinces a mobile carrier to transfer a victim’s phone number to a SIM card controlled by the attacker. Once the attacker has control of the phone number, they can intercept SMS-based authentication codes, reset passwords, and gain unauthorized access to sensitive accounts such as email, social media, banking, and cryptocurrency platforms.

---

## Risks
SIM swapping attacks can lead to:

- Unauthorized access to personal and financial accounts
- Theft of sensitive data, including emails and private messages
- Bypassing SMS-based two-factor authentication (2FA)
- Identity theft and impersonation
- Financial loss or fraud

---

## How Attacks Work
1. **Social Engineering**: Attackers often call the victim’s mobile carrier, impersonating the victim, and request a SIM replacement.
2. **SIM Reassignment**: The mobile carrier transfers the victim’s phone number to a new SIM controlled by the attacker.
3. **Account Takeover**: The attacker receives SMS messages and one-time passwords (OTPs) intended for the victim, allowing them to reset passwords and access accounts.

---

## Prevention Guidelines

### For Developers
- **Avoid SMS-based 2FA as the primary authentication method.**  
  Prefer alternatives such as:
  - Authenticator apps (TOTP, e.g., Google Authenticator)
  - Hardware security keys (WebAuthn / FIDO2)
- **Implement risk-based authentication**:
  - Monitor for unusual logins or device changes
  - Notify users of SIM changes if possible
- **Use multi-factor authentication layers** that do not rely solely on SMS.
- **Limit sensitive operations** (password resets, fund transfers) to verified devices or hardware keys.
- **Educate users** about SIM swapping risks and best practices.

### For Organizations
- Train customer support staff to **verify identity rigorously** before processing SIM swaps.
- Implement **internal alerts** for unusual SIM change requests.
- Encourage customers to set **account PINs or passwords** with their mobile carrier for SIM swaps.
- Maintain a clear **incident response plan** for suspected SIM swap events.

### For Users
- Use **authenticator apps** or hardware keys instead of SMS for 2FA.
- Set a **PIN or password with your mobile carrier** to prevent unauthorized SIM swaps.
- Be vigilant for sudden **loss of signal** or unexpected inability to receive SMS.
- Avoid sharing personal information over the phone or online that can be used to impersonate you.

---

## Anti-Patterns
Avoid practices that increase the risk of SIM swapping attacks:

- Sending passwords or sensitive information over SMS
- Using SMS as the only method of authentication
- Ignoring unexpected SIM or network changes

---

## References
- [OWASP Two-Factor Authentication Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Two-Factor_Authentication_Cheat_Sheet.html)
- [Vice Article: PayPal and Venmo are letting SIM swappers hijack accounts](https://www.vice.com/en_us/article/pke9zk/paypal-and-venmo-are-letting-sim-swappers-hijack-accounts)
- [NIST Digital Identity Guidelines (SP 800-63B)](https://pages.nist.gov/800-63-3/sp800-63b.html)
- [OWASP Account Security Guidelines](https://owasp.org/www-project-top-ten/)

---

*This control page is intended to provide guidance to developers, organizations, and users to reduce the risk of SIM swapping attacks.*