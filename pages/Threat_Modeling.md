---

layout: col-sidebar
title: OWASP Threat Modeling
author:
contributors:
tags: Threat Modeling
auto-migrated: 1
permalink: /Threat_Modeling

---

## Overview

The term "Threat Modeling" has become quite popular recently. Microsoft
has published a book about their process and includes threat modeling as
a key activity in their [Secure Development
Lifecycle](http://msdn.microsoft.com/security/default.aspx?pull=/library/en-us/dnsecure/html/sdl.asp)
(SDL).

A threat model is essentially a structured representation of all the
information that affects the security of an application. In essence, it
is a view of the application and its environment through security
glasses.

Threat modeling is a process for capturing, organizing, and analyzing
all of this information. Threat modeling enables informed
decision-making about application security risk. In addition to
producing a model, typical threat modeling efforts also produce a
prioritized list of security improvements to the concept, requirements,
design, or implementation.

## **Objectives of Threat Modeling**

Threat modeling is a family of activities for improving security by
identifying objectives and vulnerabilities, and then defining
countermeasures to prevent, or mitigate the effects of, threats to the
system. A threat is a potential or actual undesirable event that may be
malicious (such as DoS attack) or incidental (failure of a Storage
Device). Threat modeling is a planned activity for identifying and
assessing application threats and vulnerabilities.

## Threat Modeling Across the Lifecycle

Threat modeling is best applied continuously throughout a software
development project. The process is essentially the same at different
levels of abstraction, although the information gets more and more
granular throughout the lifecycle. Ideally, a high-level threat model
should be defined in the concept or planning phase, and then refined
throughout the lifecycle. As more details are added to the system, new
attack vectors are created and exposed. The ongoing threat modeling
process should examine, diagnose, and address these threats.

Note that it is a natural part of refining a system for new threats to
be exposed. For example, when you select a particular technology -- such
as Java for example -- you take on the responsibility to identify the
new threats that are created by that choice. Even implementation choices
such as using regular expressions for validation introduce potential new
threats to deal with.

## Threat Modeling - Generic Steps

For a threat to an application to exist, there must be a combination of
the following where the combined likelihood and impact are important
enough to do something about. Following is a four question framework
that helps understand threat modeling:

  - What are we working on?
  - What can go wrong?
  - What are we going to do about it?
  - Did we do a good job?

There are many ways to answer each of these questions.

To understand whether an application is secure enough or not, you have
to search out combinations of these ingredients that lead to realistic
threats.

There is no "right" way to evaluate the search space of possible
threats. But there are better or worse ways. Attempting to evaluate all
the possible combinations of threat agent, attack, vulnerability, and
impact is often a waste of time and effort. Note that many of the
automated tools take this approach - gathering lots of data and
producing thousands of possible threats. Generally it is more productive
to focus on finding high likelihood and high impact threats.

The basic threat modeling process consists of the following generic
steps. The process of exploring the search space is iterative and
constantly refined based on what you have done so far. So, for example,
starting with all possible vulnerabilities is usually pointless, as most
of them are not attackable by the threat agents, protected by a
safeguard, or do not lead to a conseequence. Therefore, it's generally
best to start with the factors that make a lot of difference.

  - **Assessment Scope** - The first step is always to understand what's
    on the line. Identifying tangible assets, like databases of
    information or sensitive files is usually easy. Understanding the
    capabilities provided by the application and valuing them is more
    difficult. Less concrete things, such as reputation and goodwill are
    the most difficult to measure, but are often the most critical.

<!-- end list -->

  - **Identify [Threat Agents](http://www.owasp.org/index.php/Category:Threat_Agent) and
    possible [Attacks](/attacks)** - A key part of the threat
    model is a characterization of the different groups of people who
    might be able to attack your application. These groups should
    include insiders and outsiders, performing both inadvertent mistakes
    and malicious attacks.

<!-- end list -->

  - **Understand existing
    Countermeasures - The model must
    include the existing countermeasures

<!-- end list -->

  - **Identify exploitable
    [Vulnerabilities](/vulnerabilities)** - Once you have an
    understanding of the security in the application, you can then
    analyze for new vulnerabilities. The search is for vulnerabilities
    that connect the possible attacks you've identified to the negative
    consequences you've identified.

<!-- end list -->

  - **Prioritized identified risks** - Prioritization is everything in
    threat modeling, as there are always lots of risks that simply don't
    rate any attention. For each threat, you estimate a number of
    likelihood and impact factors to determine an overall risk or
    severity level.

<!-- end list -->

  - **Identify Countermeasures to reduce threat** - The last step is to identify countermeasures to reduce
    the risk to acceptable levels.

## Benefits

Done right, threat modeling provides a clear "line of sight" across a
project that justifies security efforts. The threat model allows
security decisions to be made rationally, with all the information on
the table. The alternative is to make knee-jerk security decisions with
no support. The threat modeling process naturally produces an assurance
argument that can be used to explain and defend the security of an
application. An assurance argument starts with a few high level claims,
and justifies them with either subclaims or evidence.

## ThreatModel SDK

The ThreatModel SDK is a minimalistic Java library that provides a basic
vendor-neutral object model along with the ability to parse reports
generated from common threat modeling tools. Supported Threat Modeling
Tools:

  - Microsoft Threat Modeling Tool 2016

Planned Threat Modeling Tools:

  - Mozilla SeaSponge

<https://github.com/stevespringett/threatmodel-sdk>

## References

  - [Microsoft's Security Development
    Process](http://msdn.microsoft.com/library/default.asp?url=/library/en-us/dnsecure/html/sdl.asp)
