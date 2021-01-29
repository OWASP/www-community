---

layout: col-sidebar
title: Cash Overflow
author: psiinon
contributors: Andrew Smith, kingthorin
permalink: /attacks/Cash_Overflow
tags: attack, Cash Overflow

---

{% include writers.html %}

## Description

A Cash Overflow attack is a [Denial of
Service](Denial_of_Service) attack specifically aimed at
exceeding the hosting costs for a cloud application, either essentially
bankrupting the service owner or exceeding the application cost limits,
leading the cloud service provider to disable the application.

## Risk Factors

Given enough resources, fairly easy to launch attack.
Quickly detected due to immediate downtime/resources consumption/logging.
Impact usually limited to loss of availability.

## Related [Controls](https://owasp.org/www-community/controls/)

DoS Prevention Techniques

## References

[Denial of Service through Resource Depletion](http://capec.mitre.org/data/index.html)
