---

layout: col-sidebar
title: Insufficient Entropy
author: 
contributors: 
permalink: /vulnerabilities/Insufficient_Entropy
tags: vulnerability, Insufficient Entropy

---

{% include writers.html %}

## Description

When an undesirably low amount of entropy is available. Psuedo Random Number Generators are susceptible to suffering from insufficient entropy when they are initialized, because entropy data may not be available to them yet.

## Related [Attacks](../attacks/)

- In many cases, a PRNG uses a combination of the system clock and entropy to create seed data. If insufficient entropy is available, an attacker can reduce the size magnitude of the seed value considerably. Furthermore, by guessing values of the system clock, they can create a manageable set of possible PRNG outputs.

## Related [Vulnerabilities](../vulnerabilities/)

## Related [Controls](../controls/)

- Many PRNG's (`/dev/random` and `/dev/urandom` for example) store their last value before shutdown. By using this value at intialization, they can sometimes avoid insufficient or predictable starting entropy.
