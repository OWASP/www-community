---

layout: col-sidebar
title: Custom Special Character Injection
author: 
contributors: 
permalink: /attacks/Custom_Special_Character_Injection
tags: attack, Custom Special Character Injection
auto-migrated: 1

---

## Description

The software does not properly filter or quote special characters or
reserved words that are used in a custom or proprietary language or
representation that is used by the product. That allows attackers to
modify the syntax, content, or commands before they are processed by the
end system.

## Risk Factors

TBD

## Examples

**Example1**

A simple example is an application which executes almost everything
which is passed to it from the current terminal by the user without
sanitazing and blocking user input. If the application doesn't implement
appropriate signals handling, we may interrupt or suspend program
execution by sending respectively *Ctrl+C (^C)* or *Ctrl+Z (^Z)*
combinations. These combinations are sending signals to the application.
In the first case it's *SIGINT* and in the second it's *SIGSTOP* signal.

**Example2**

The classic example, often used by the IRC warriors/bandits, was
disconnecting modem users by sending to them a special sequence of
characters. Sending via any protocol (IP) "*+++ATH0*" sequence caused
some modems to interpret this sequence as a disconnect command. So all
that had to be done was to send the sequence on an IRC channel, which in
effect forced vulnerable modems to disconnect.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [Logic/time bomb](Logic/time_bomb "wikilink")

## Related [Attacks](Attacks "wikilink")

  - [Log forging](Log_forging "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

TBD

## Related [Controls](Controls "wikilink")

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")
  - [Output Validation](Output_Validation "wikilink")
  - [Canonicalization](Canonicalization "wikilink")

## References

TBD

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Injection](Category:Injection "wikilink") [Category:Resource
Manipulation](Category:Resource_Manipulation "wikilink")
[Category:Attack](Category:Attack "wikilink")