---

layout: col-sidebar
title: Cryptanalysis
author: 
contributors: Rezos, KristenS, kingthorin
permalink: /attacks/Cryptanalysis
tags: attack, Cryptanalysis

---

{% include writers.html %}

## Description

Cryptanalysis is a process of finding weaknesses in cryptographic
algorithms and using these weaknesses to decipher the ciphertext without
knowing the secret key (instance deduction). Sometimes the weakness is
not in the cryptographic algorithm itself, but rather in how it is
applied that makes cryptanalysis successful. An attacker may have other
goals as well, such as:

- Total Break - Finding the secret key.
- Gobal Deduction - Finding a functionally equivalent algorithm for encryption and decryption that does not require knowledge of the secret key.
- Information Deduction - Gaining some information about plaintexts or ciphertexts that was not previously known.
- Distinguishing Algorithm - The attacker has the ability to distinguish the output of the encryption (ciphertext) from a random permutation of bits.

The goal of the attacker performing cryptanalysis will depend on the
specific needs of the attacker in a given attack context. In most cases,
if cryptanalysis is successful at all, an attacker will not be able to
go past being able to deduce some information about the plaintext (goal
3). However, that may be sufficient for an attacker, depending on the
context.

## Examples

A very easy to understand (but totally inapplicable to modern
cryptographic ciphers) example is a cryptanalysis technique called
frequency analysis that can be successfully applied to the very basic
classic encryption algorithms that performed monoalphabetic substitution
replacing each letter in the plaintext with its predetermined mapping
letter from the same alphabet. This was considered an improvement over a
more basic technique that would simply shift all of the letters of the
plaintext by some constant number of positions and replace the original
letters with the new letter with the resultant alphabet position. While
monoalphabetic substitution ciphers are resilient to blind brute force,
they can be broken easily with nothing more than a pen and paper.
Frequency analysis cryptanalysis uses the fact that natural language is
not random and monoalphabetic substitution does not hide the statistical
properties of the natural language. So if the letter "E" in an English
language occurs with a certain known frequency (about 12.7%), whatever
"E" was substituted with to get to the ciphertext, will occur with the
similar frequency. Having this frequency information allows the
cryptanalyst to quickly determine the substitutions and decipher the
ciphertext. Frequency analysis techniques are not applicable to modern
ciphers as they are all resilient to it (unless this is a very bad case
of a homegrown encryption algorithm). This example is just here to
illustrate a rudimentary example of cryptanalysis.

## Related [Controls](https://owasp.org/www-community/controls/)

Use proven cryptographic algorithms with recommended key sizes.

Ensure that the algorithms are used properly. That means:

- Not rolling out your own crypto; Use proven algorithms and implementations.
- Choosing initialization vectors with sufficiently random numbers
- Generating key material using good sources of randomness and avoiding known weak keys
- Using proven protocols and their implementations.
- Picking the most appropriate cryptographic algorithm for your usage context and data

## References

- [CAPEC - Cryptanalysis](http://capec.mitre.org/data/definitions/97.html)
