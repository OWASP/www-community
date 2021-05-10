---

layout: col-sidebar
title: Custom Special Character Injection
author: Rezos
contributors: Weilin Zhong, KristenS, Alan Jex, kingthorin 
permalink: /attacks/Custom_Special_Character_Injection
tags: attack, Custom Special Character Injection
auto-migrated: 1

---

{% include writers.html %}

## Description

The software does not properly filter or quote special characters or
reserved words that are used in a custom or proprietary language or
representation that is used by the product. That allows attackers to
modify the syntax, content, or commands before they are processed by the
end system.

## Examples

### Example 1

A simple example is an application which executes almost everything
which is passed to it from the current terminal by the user without
sanitizing and blocking user input. If the application doesn't implement
appropriate signals handling, we may interrupt or suspend program
execution by sending respectively `Ctrl+C (^C)` or `Ctrl+Z (^Z)`
combinations. These combinations are sending signals to the application.
In the first case it's `SIGINT` and in the second it's `SIGSTOP` signal.

### Example 2

The classic example, often used by the IRC warriors/bandits, was
disconnecting modem users by sending to them a special sequence of
characters. Sending via any protocol (IP) `*+++ATH0*` sequence caused
some modems to interpret this sequence as a disconnect command. So all
that had to be done was to send the sequence on an IRC channel, which in
effect forced vulnerable modems to disconnect.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Log forging](https://owasp.org/www-community/attacks/Log_Injection)
