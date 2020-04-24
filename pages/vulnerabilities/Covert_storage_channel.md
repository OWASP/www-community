---

layout: col-sidebar
title: Covert storage channel
author: 
contributors: 
permalink: /vulnerabilities/Covert_storage_channel
tags: vulnerability, Covert storage channel

---

{% include writers.html %}

## Overview

The existence of a covert storage channel in a communications channel may release information which can be of significant use to attackers.

## Consequences

- Confidentiality: Covert storage channels may provide attackers with important information about the system in question.

## Exposure period

- Implementation: The existence of data in a covert storage channel is largely a flaw caused by implementers.

## Platform

- Languages: All
- Operating platforms: All

## Required resources

Network proximity: Some ability to sniff network traffic would be required to capitalize on this flaw.

## Severity

Medium

## Likelihood of exploit

High

## Avoidance and mitigation

- Implementation: Ensure that all reserved fields are set to zero before messages are sent and that no unnecessary information is included.

## Discussion

Covert storage channels occur when out-of-band data is stored in messages for the purpose of memory reuse. If these messages or packets are sent with the unnecessary data still contained within, it may tip off malicious listeners as to the process that created the message.

With this information, attackers may learn any number of things, including the hardware platform, operating system, or algorithms used by the sender. This information can be of significant value to the user in launching further attacks.

## Examples

An excellent example of covert storage channels in a well known application is the ICMP error message echoing functionality. Due to ambiguities in the ICMP RFC, many IP implementations use the memory within the packet for storage or calculation.

For this reason, certain fields of certain packets - such as ICMP error packets which echo back parts of received messages - may contain flaws or extra information which betrays information about the identity of the target operating system.

This information is then used to build up evidence to decide the environment of the target. This is the first crucial step in determining if a given system is vulnerable to a particular flaw and what changes must be made to malicious code to mount a successful attack.

## Related problems

Not available.