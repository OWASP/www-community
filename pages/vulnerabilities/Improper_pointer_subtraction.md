---

layout: col-sidebar
title: Improper pointer subtraction
author: 
contributors: 
permalink: /vulnerabilities/Improper_pointer_subtraction
tags: vulnerability, Improper pointer subtraction

---

{% include writers.html %}

## Overview

The subtraction of one pointer from another in order to determine size is dependant on the assumption that both pointers exist in the same memory chunk.

## Consequences

- Authorization: There is the potential for arbitrary code execution with privileges of the vulnerable program.

## Exposure period

- Pre-design through Build: The use of tools to prevent these errors should be used.
- Implementation: Many logic errors can lead to this condition. It can be exacerbated by lack of or misuse of mitigating technologies.

## Platform

- Languages: C/C++/C#
- Operating Platforms: Any

## Required resources

Any

## Severity

High

## Likelihood of exploit

Medium

## Avoidance and mitigation

- Pre-design through Build: Most static analysis programs should be able to catch these errors.
- Implementation: Save an index variable. This is the recommended solution. Rather than subtract pointers from one another, use an index variable of the same size as the pointers in question. Use this variable "walk" from one pointer to the other and calculate the difference. Always sanity check this number.

## Related problems

Any
