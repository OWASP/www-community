---

layout: col-sidebar
title: Unsafe function call from a signal handler
author: 
contributors: 
permalink: /vulnerabilities/Unsafe_function_call_from_a_signal_handler
tags: vulnerability, Unsafe function call from a signal handler
auto-migrated: 1

---

{% include writers.html %}

## Description

There are several functions which - under certain circumstances, if used
in a signal handler - may result in the corruption of memory, allowing
for exploitation of the process.

**Consequences**

  - Access control: It may be possible to execute arbitrary code through
    the use of a write-what-where condition.
  - Integrity: Signal race conditions often result in data corruption.

**Exposure period**

  - Requirements specification: A language might be chosen which is not
    subject to this flaw.
  - Design: Signal handlers with complicated functionality may result in
    this issue.
  - Implementation: The use of any number of non-reentrant functions
    will result in this issue.

**Platform**

  - Languages: C, C++, Assembly
  - Platforms: All

**Required resources**

Any

**Severity**

High

**Likelihood of exploit**

Low

This flaw is a subset of race conditions occurring in signal handler
calls which is concerned primarily with memory corruption caused by
calls to non-reentrant functions in signal handlers.

Non-reentrant functions are functions that cannot safely be called,
interrupted, and then recalled before the first call has finished
without resulting in memory corruption. The function call syslog() is an
example of this. In order to perform its functionality, it allocates a
small amount of memory as "scratch space." If syslog() is suspended by a
signal call and the signal handler calls syslog(), the memory used by
both of these functions enters an undefined, and possibly, exploitable
state.

## Risk Factors

  - Talk about the [factors](https://owasp.org/www-community/OWASP_Risk_Rating_Methodology)
    that make this vulnerability likely or unlikely to actually happen
  - Discuss the technical impact of a successful exploit of this
    vulnerability
  - Consider the likely \[business impacts\] of a successful attack

## Examples

See *Race condition in signal handler*, for an example usage of free()
in a signal handler which is exploitable.

## Related [Controls](https://owasp.org/www-community/controls/)

  - Requirements specification: A language might be chosen which is not
    subject to this flaw, through a guarantee of reentrant code.
  - Design: Design signal handlers to only set flags rather than perform
    complex functionality.
  - Implementation: Ensure that non-reentrant functions are not found in
    signal handlers. Also, use sanity checks to ensure that state is
    consistently performing asynchronous actions which effect the state
    of execution.

__NOTOC__

[Category:Vulnerability](Category:Vulnerability "wikilink")