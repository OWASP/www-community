---

layout: col-sidebar
title: "Changing A User's Registered Email Address"
author: "Philip H. Schlesinger"
tags: ["control", "email", "address", "registered", "change", "account", "takeover"]

---

{% include writers.html %}

People's email addresses regularly change.  The process below is the recommended method to implement in a system to handle that situation.  The process is less-stringent when using [Multifactor Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) because the identity-proof is stronger than just using a password.

## Process (Depending on a System's Level of Authentication)

### Recommended Process If The User HAS [Multifactor Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) Enabled

1. The System shall confirm the User's authentication cookie / token is still valid; if not, the System should display a login screen.
1. To reduce User friction, the System shall describe to the User the process that the User will be expected to follow to change their registered email address within the System.
1. The System shall ask the User to submit a proposed-new email address.  The System **shall not** continue this process unless the proposed-new email address meets the System's rules for registered email addresses.
1. The System shall ask the User to use [Multifactor Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) to prove their identity. The System **shall not** continue this process until the [Multifactor Authentication](https://cheatsheetseries.owasp.org/cheatsheets/Multifactor_Authentication_Cheat_Sheet.html) submission is successful.
1. The System shall now store in the data-store the proposed-new email address in a way that represents this is a "proposed-new" email address for that User's account in the System AND NOT the actual registered email address.
1. The System shall now create and stored in the System data-store two separate time-limited nonces associated with the User's account -- making sure to not duplicate any existing nonces in the data-store:
   1. A nonce to be used to notify the System to, in turn, directly notify the System Administrators that the request to change the registered email address was unexpected and should be investigated immediately.
   1. A separate nonce to be used to notify the System that the User has confirmed the proposed-new email address is both (a) valid, and (b) within the User's control.
1. The System shall now send out two email messages to confirm that the change is valid:
    1. A **notification-only** email message to the still-currently-registered email address stating that the registered email address for the User on the System is about to change -- and if this is unexpected to either:
       - Click the specified link within the email message within the specified time-limit; this link shall include the nonce for notifying System Administrators that the request was unexpected
       - AND / OR
       - Contact Customer Service / Help Desk via a specified phone number or email address
    1. A separate **confirmation-required** email message to the proposed-new email address stating that the registered email address for the User on the System has been requested to change and:
       - IF this IS expected
          - THEN the User should click the link with the nonce confirming the change is expected within the specified time limit.
       - IF this IS NOT expected,
          - THEN to click another specified link within the email message within the specified time limit; this link shall include the nonce for notifying System Administrators that the request was unexpected
          - AND / OR
          - Contact Customer Service / Help Desk via a specified phone number or email address
1. WHEN the System receives a request from the link with a nonce to notify System Administrators that the request to change the registered email address was unexpected:
   - IF the nonce in that link has not expired by that time
     - THEN the System shall notify System Administrators that a change to a registered email address was identified as unexpected -- and to figure out what happened immediately via human means.
   - On the other hand:
      - IF the nonce in that link has expired,
        - THEN the System shall:
          - FIRST remove that now-detected-as-expired nonce from the System data-store.
          - AND THEN state to the User that the request is invalid.
   - In the case that the nonce in the link cannot be found:
      - The System shall state to the User that the request is invalid.
1. WHEN the System receives a request from the link with a nonce to confirm to the System that the request to change the registered email address is valid:
   - IF the nonce in that link has not expired by that time
     - THEN the System shall:
       - FIRST update the data-store to change the registered email address to the proposed-new email address for the User.  
       - SECOND log out the User / invalidate the User's token / authentication cookie from the System
       - THIRD inform the User that (a) the change of registered email address was successful (b) the User has been logged out and should now log in with their usual login credentials
   - On the other hand:
      - IF the nonce in that link has expired
      - THEN the System shall:
        - FIRST remove that now-detected-as-expired nonce from the System data-store.
        - AND THEN state to the User that the request is invalid.
   - In the case that the nonce in the link cannot be found:
      - The System shall state to the User that the request is invalid.

### Recommended Process If The User DOES NOT HAVE Multifactor Authentication Enabled

1. The System shall confirm the User's authentication cookie / token is still valid; if not, the System should display a login screen.
1. To reduce User friction, the System shall describe to the User the process that the User will be expected to follow to change their registered email address within the System.
1. The System shall ask the User to submit a proposed-new email address.  The System **shall not** continue this process unless the proposed-new email address meets the System's rules for registered email addresses.
1. The System shall ask the User to provide their current password to prove their identity. The System **shall not** continue this process until the password submitted matches the User's current password.
1. The System shall now store in the data-store the proposed-new email address in a way that represents this is a "proposed-new" email address for that User's account in the System AND NOT the actual registered email address.
1. The System shall now create and stored in the System data-store three separate time-limited nonces associated with the User's account -- making sure to not duplicate any existing nonces in the data-store:
   1. A nonce to be used to notify the System to, in turn, directly notify the System Administrators that the request to change the registered email address was unexpected and should be investigated immediately.
   1. A separate nonce to be used to notify the System that the User has confirmed from their still-currently-registered email address that the change of registered email address is ok.
      - NOTE: this extra step may cause User friction; however, it is recommended in the event that the User's password was easily guessed or used as part of a repeated-password attack.
   1. Another separate nonce to be used to notify the System that the User has confirmed the proposed-new email address is both (a) valid, and (b) within the User's control.
1. The System shall now send out two email messages to confirm that the change is valid:
    1. A **confirmation-required** email message to the still-currently-registered email address stating that the registered email address for the User on the System has been requested to change and:
       - IF this IS expected,
          - THEN the User should click the link with the nonce confirming the change is expected within the specified time limit.
       - IF this IS NOT expected,
          - THEN to click another specified link within the email message within the specified time limit; this link shall include the nonce for notifying System Administrators that the request was unexpected
          - AND / OR
          - Contact Customer Service / Help Desk via a specified phone number or email address
    1. A separate **confirmation-required** email message to the proposed-new email address stating that the registered email address for the User on the System has been requested to change and:
       - IF this IS expected,
          - THEN the User should click the link with the nonce confirming the change is expected within the specified time limit.
       - IF this IS NOT expected,
          - THEN to click another specified link within the email message within the specified time limit; this link shall include the nonce for notifying System Administrators that the request was unexpected
          - AND / OR
          - Contact Customer Service / Help Desk via a specified phone number or email address
1. WHEN the System receives a request from the link with a nonce to notify System Administrators that the request to change the registered email address was unexpected:
   - IF the nonce in that link has not expired by that time
     - THEN the System shall notify System Administrators that a change to a registered email address was identified as unexpected -- and to figure out what happened immediately via human means.
   - On the other hand:
     - IF the nonce in that link has expired
     - THEN the System shall:
        - FIRST remove that now-detected-as-expired nonce from the System data-store.
        - AND THEN state to the User that the request is invalid.
   - In the case that the nonce in the link cannot be found:
      - The System shall state to the User that the request is invalid.
1. WHEN the System receives a request from the link with the nonce to confirm to the System that the User has confirmed the request to change the registered email address from the still-currently-registered email address:
   - IF the nonce in that link has not expired by that time AND IF the User HAS already confirmed the change of the registered email address from the message to the proposed-new email address
     - THEN the System shall:
       - FIRST update the data-store to change the registered email address to the proposed-new email address for the User.  
       - SECOND log out the User / invalidate the User's token / authentication cookie from the System
       - THIRD inform the User that (a) the change of registered email address was successful (b) the User has been logged out and should now log in with their usual login credentials
   - On the other hand:
      - IF the nonce in that link has not expired by that time AND IF the User HAS NOT already confirmed the change of the registered email address from the message to the proposed-new email address
        - THEN the System shall inform the User that they now just need to click the confirmation link in the email message to the proposed-new email address
   - On the other hand:
      - IF the nonce in that link has expired
      - THEN the System shall:
        - FIRST remove that now-detected-as-expired nonce from the System data-store.
        - AND THEN state to the User that the request is invalid.
   - In the case that the nonce in the link cannot be found:
      - The System shall state to the User that the request is invalid.
1. WHEN the System receives a request from the link with the nonce to confirm to the System that the User has confirmed the request to change the registered email address from the proposed-new email address:
   - IF the nonce in that link has not expired by that time AND IF the User HAS already confirmed the change of the registered email address from the message to the still-currently-registered email address
     - THEN the System shall:
       - FIRST update the data-store to change the registered email address to the proposed-new email address for the User.  
       - SECOND log out the User / invalidate the User's token / authentication cookie from the System
       - THIRD inform the User that (a) the change of registered email address was successful (b) the User has been logged out and should now log in with their usual login credentials
   - On the other hand:
      - IF the nonce in that link has not expired by that time AND IF the User HAS NOT already confirmed the change of the registered email address from the message to the proposed-new email address
        - THEN the System shall inform the User that they now just need to click the confirmation link in the email message to the proposed-new email address
   - On the other hand:
      - IF the nonce in that link has expired
      - THEN the System shall:
        - FIRST remove that now-detected-as-expired nonce from the System data-store.
        - AND THEN state to the User that the request is invalid.
   - In the case that the nonce in the link cannot be found:
      - The System shall state to the User that the request is invalid.

## Notes on the Above Processes

- Google thinks differently

IF a User of Google only has their account protected with a password, when someone submits a change of registered email address, if the submitter knows the User's password, [Google just sends a **notification-only** email message to the currently-registered email address](https://support.google.com/accounts/answer/55393?hl=en) for that Google User with a link for "I didn't request this email address change".

This is risky:

The User's password might be easily-guessable -- or might be a repeated-password stolen from someplace else.

Nevertheless, Google apparently is still ok with the risk that the request might be unauthorized.  Hopefully the real User will see the email message to the soon-to-be originally-registered email address and click the "this is unexpected" link before the "this is unexpected" nonce expires.

- Regular Social Engineering Training Is Essential

In the event someone contacts a System's System Administrator or Help Desk to request the change of a registered email address stating they are unable to go through the above process, the System Administrator / Help Desk has to either:

(a) be instructed to refuse to make any changes that do not follow the above process

-- or --

(b) be instructed on best-practice dalternative methods of verifying the person's identity before making changes that do not follow the above process

OWASP recommends regularly training staff on how to identify and respond to social engineering attacks.  However, as of this writing (2023-12-01), OWASP does not offer social engineering training.

For a brief guide, see the United States Cybersecurity & Infrastructure Agency's (CISA) ["Avoiding Social Engineering and Phishing Attacks"](https://www.cisa.gov/news-events/news/avoiding-social-engineering-and-phishing-attacks).
