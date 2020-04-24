---

layout: col-sidebar
title: Multiple admin levels
author: 
contributors: 
permalink: /vulnerabilities/Multiple_admin_levels
tags: vulnerability, Multiple admin levels
auto-migrated: 1

---

{% include writers.html %}

## Description

In an application with administrators that have the ability to alter
login credentials of users, if there are multiple levels of
administrator permissions, there needs to be a control preventing
administrators with lower permission levels from altering login
credentials of higher level admins.

## Risk Factors

  - Likelihood of this happening relies on an attacker getting control
    of a lower level admin account in the first place.
  - Administrator misconduct or mistakes could be made worse if they
    could easily escalate their own permissions.
  - There is no point to create administrators with different levels of
    permissions if you don't prevent them from easily escalating their
    own permissions.