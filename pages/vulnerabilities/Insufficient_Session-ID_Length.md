---

layout: col-sidebar
title: Insufficient Session ID Length
author: Jake Karnes
contributors: Greg Heartsfield
permalink: /vulnerabilities/Insufficient_Session-ID_Length
tags: vulnerability, Insufficient Session-ID Length

---

{% include writers.html %}

## Description

Session identifiers must have **at least 64 bits of entropy** to prevent brute-force session guessing attacks. Entropy refers to the amount of randomness or unpredictability in a value. Each "bit" of entropy doubles the number of possible outcomes, meaning a session ID with 64 bits of entropy can have 2<sup>64</sup> possible values. This randomness provides security, as it makes it harder for attackers to guess valid session IDs.

It's important to understand that session ID length alone is not a sufficient indicator of security. Instead, the critical factor is the entropy (or randomness) contained within the session identifier. While the length of the session ID can affect how much entropy is encoded, the actual entropy depends on how the session ID is generated. Encoding methods (e.g., hexadecimal, Base64, etc) influence how the session ID is represented, but the security ultimately comes from the randomness of the identifier, not the encoding itself.

### Key Takeaways

- **Entropy is the most important factor**: No matter the session ID length, the goal is to achieve at least 64 bits of entropy.
- **Randomness over length**: The randomness and unpredictability of session IDs are what ultimately prevent attacks, not just the length of the session identifier.
- **Encoding can impact required length**: If using hexadecimal encoding, the randomly chosen session ID must be at least 16 hexadecimal characters long to achieve the required 64 bits of entropy. If using another encoding, a different character length may be required.
- **Estimating attack difficulty**: The expected number of guesses required by an attacker to guess a valid session ID can be calculated based on the bits of entropy (B), the number of valid sessions (S), and the attacker’s guessing rate (A). For example, the expected time for an attacker to succeed is approximately:

![](../assets/images/Session_id_guessing_1.png)

### Session ID Length and Entropy Relationship

The most important factor in securing session identifiers is the amount of entropy they contain. While longer session IDs are often recommended, the actual security comes from the randomness within the identifier, not just its length.

#### Focus on Hexadecimal Encoding

Hexadecimal encoding is commonly used in session identifiers. Each hexadecimal character (0-9, A-F) represents 4 bits of entropy. This means that to achieve 64 bits of entropy, a session ID must contain at least 16 random hexadecimal characters, which provides 2<sup>64</sup> possible combinations. When each character is chosen randomly, the session ID offers the desired 64 bits of entropy, making it secure against brute-force guessing attacks. Let’s explore good and bad examples of hexadecimal session IDs to better understand this:

1. **Good Example - 64 bits of entropy (16 characters)**
   - Example Session ID: `A1B2C3D4E5F67890`
   - This is a 16-character hexadecimal value. Assuming 16 random hexadecimal characters are chosen, there are 2<sup>64</sup> possible combinations. This represents exactly 64 bits of entropy. With 2<sup>64</sup> possible combinations, it is secure against brute-force guessing attacks as demonstrated below.

2. **Bad Example - 32 bits of entropy (8 characters)**
   - Example Session ID: `A1B2C3D4`
   - This is an 8-character hexadecimal value. While it’s half the length of the good example, it provides significantly less security because there are only 2<sup>32</sup> possible values. This provides 32 bits of entropy and is vulnerable to brute-force attacks as discussed later.

**Note:** When session IDs are stored or transmitted as text (e.g., in a cookie), they may be represented using ASCII or UTF-8 encoding. This does not affect the entropy but does influence the size of the session identifier. For example, a 16-character hexadecimal session ID occupies 16 bytes (128 bits) when encoded as ASCII, but it still only represents 64 bits of entropy.

#### Examples Where Length Alone Isn’t Sufficient

While hexadecimal encoding provides a clear relationship between length and entropy, length alone can be misleading depending on the encoding or generation method used. Let’s explore some illustrative but hypothetical examples:

1. **Session ID using Binary encoding**
    - Example Session ID: `1010101010101010`
    - This session ID is 16 characters long, but because each character can only represent 0 or 1, there are only 2<sup>16</sup> possible values. The total entropy is just 16 bits. This shows that despite its length of 16 characters, the security of this session ID is very low.
    - This is not used in practice but illustrative of the concept.
  
2. **Session ID using Base64 encoding**
    - Example Session ID #1: `abcdefghijkl`
    - Example Session ID #2: `mnopqrstuvwx`
    - This 12-character Base64 value can represent 72 bits of entropy. Base64 is more efficient than hexadecimal because each character represents more than 4 bits of entropy. The result is that even though this session ID is shorter than the previous hexadecimal example, it offers significantly more security.
    - We can use the popular encoding/decoding tool CyberChef to confirm this value can represent a 72-bit number. We can see [example #1](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)To_Binary('None',8)&input=YWJjZGVmZ2hpamts) and [example #2](https://gchq.github.io/CyberChef/#recipe=From_Base64('A-Za-z0-9%2B/%3D',true,false)To_Binary('None',8)&input=bW5vcHFyc3R1dnd4) decode to a 72-bit binary value. 

3. **16-byte hexadecimal session ID with fixed characters**
    - Example Session ID #1: `DECAFBAD12345678`
    - Example Session ID #2: `DECAFBAD87654321`
    - Example Session ID #3: `DECAFBAD12341234`
    - In this case, the first half of the session ID (`DECAFBAD`) is fixed and predictable, while only the second half is random. Because there are only 8 random hexadecimal characters, this means that there are only 2<sup>32</sup> possible values. This means that the session ID provides only 32 bits of entropy, despite being 16 characters long. Predictable patterns in the session ID can severely undermine security.

These examples show that **session ID length alone is not a reliable indicator of security** — what matters is the amount of randomness (entropy) the ID can represent. 

### Estimating Attack Time

The time required to guess a valid session identifier depends on several factors:

- **Entropy (B)**: The number of bits of randomness in the session identifier.
- **Valid sessions (S)**: The number of valid session identifiers available at any time.
- **Guesses per second (A)**: The speed at which an attacker can try potential session identifiers.

The attack time can be estimated using two different formulas depending on whether session IDs are dynamic (changing during the attack) or static (remaining constant). These scenarios reflect different real-world situations, such as expiring user sessions or long-lived tokens like API keys.

Here's a simple webpage that implements these 2 formulas where you can test these different conditions: [https://jakekarnes42.github.io/session-id-guesser/](https://jakekarnes42.github.io/session-id-guesser/)

#### Formula 1: Dynamic Session IDs (e.g., users logging in/out)
In this scenario, session IDs are constantly changing due to users logging in, logging out, or session expiration. Each guess is independent, meaning previously guessed values might later become valid. Because the guesses are independent, the expected number of guesses to find a valid session ID can be estimated using a geometric distribution. The formula to estimate the expected time for an attacker to guess a valid session ID is:

![](../assets/images/Session_id_guessing_1.png)

#### Formula 2: Static Session IDs (e.g., API keys or tokens)
In this scenario, we'll assume that the set of valid session identifiers is **not** changing throughout the attack. In the real world, this could occur when the attacker is able to exhaust all possibilities quickly (e.g., low entropy or many requests per second) or when targeting long-lived identifiers (e.g., API keys or tokens). When the set of valid session identifiers remains static, the attack becomes more efficient because the attacker can eliminate previously guessed invalid session IDs. This scenario follows the hypergeometric distribution, where the expected number of guesses is the average position of the first valid session ID among all possible values. In this case, the expected time for an attacker to guess a valid session ID is:

![](../assets/images/Session_id_guessing_2.png)

This formula accounts for the increasing probability of success with each guess as the pool of possible valid session IDs shrinks.

### Example Calculations
The following provides some example calcuations based on different attack scenarios. 

#### Example 1
Let's consider that the target website is using 32 bits of entropy for its session identifiers. This is a fairly active website with 10,000 valid sessions at any given moment. The attacker is able to leverage one or more computers to send 1,000 guesses per second. Let's calculate how long it's expected to take for the attacker to guess a valid session ID. 

We have the following as our key variables:
- \( B = 32 \) bits of entropy
- \( S = 10,000 \) valid session IDs
- \( A = 1,000 \) guesses per second

Using Formula 1 (dynamic session IDs):

![](../assets/images/Session_id_guessing_3.png)

Using Formula 2 (static session IDs):

![](../assets/images/Session_id_guessing_4.png)

We can see that for large values of \( B \), the difference is negligible. 

#### Example 2: 64 bits of entropy, 100,000 valid sessions, 10,000 guesses per second
Let's consider now that the target website is using stronger session identifiers with 64 bits of entropy. This is a very large, active website with 100,000 valid sessions at any given moment. The attacker is able to leverage many computers to send a total of 10,000 guesses per second. Let's calculate how long it's expected to take for the attacker to guess a valid session ID. 

- \( B = 64 \) bits of entropy
- \( S = 100,000 \) valid session IDs
- \( A = 10,000 \) guesses per second

Using Formula 1 (dynamic session IDs):

![](../assets/images/Session_id_guessing_5.png)

Using Formula 2 (static session IDs):

![](../assets/images/Session_id_guessing_6.png)

We can see that even though the attacker has more potential session ids to compromise, and is making many more requests per second, the 64 bits of entropy in the session ID make it effectively unguessable.

## Risk Factors

- Attackers that are trying to obtain a valid session ID for [Session hijacking](../attacks/Session_hijacking_attack).
- The attack becomes more feasible if session identifiers are not random enough or lack sufficient entropy.


## Related [Attacks](../attacks/)

- [Brute force attack](../attacks/Brute_force_attack)
