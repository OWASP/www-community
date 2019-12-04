---

layout: col-sidebar
title: Improper pointer subtraction.md
author: 
contributors: 
permalink: /vulnerabilities/Improper_pointer_subtraction
tag: vulnerability, Improper pointer subtraction.md
auto-migrated: 1

---

## Overview

The subtraction of one pointer from another in order to determine size
is dependant on the assumption that both pointers exist in the same
memory chunk.

## Consequences

  - Authorization: There is the potential for arbitrary code execution
    with privileges of the vulnerable program.

## Exposure period

  - Pre-design through Build: The use of tools to prevent these errors
    should be used.

<!-- end list -->

  - Implementation: Many logic errors can lead to this condition. It can
    be exacerbated by lack of or misuse of mitigating technologies.

## Platform

  - Languages: C/C++/C\#

<!-- end list -->

  - Operating Platforms: Any

## Required resources

Any

## Severity

High

## Likelihood of exploit

Medium

## Avoidance and mitigation

  - Pre-design through Build: Most static analysis programs should be
    able to catch these errors.

<!-- end list -->

  - Implementation: Save an index variable. This is the recommended
    solution. Rather than subtract pointers from one another, use an
    index variable of the same size as the pointers in question. Use
    this variable "walk" from one pointer to the other and calculate the
    difference. Always sanity check this number.

## Related problems

Any

## Categories

[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:General Logic
Errors](Category:General_Logic_Errors "wikilink")