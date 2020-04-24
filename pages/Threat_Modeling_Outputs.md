---

layout: col-sidebar
title: 'Threat Modeling Outputs'
author: Adamshostack
contributors: Avid, irene221b, lojikil, mplatt, Spartucvs, swierckx, tash,
    tonyuv, zeroxten, ADubhlaoich
permalink: /Threat_Modeling_Outputs
tags: 'Threat Modeling'

---

# Summary

This page details the discussions and responses prompted by the question "Are
all outputs of threat modeling bugs?" as part of the OWASP Slack Threat
Modeling Project.

Not all outputs are bugs, and it is difficult to classify a design problem in
code (Versus an implementation problem) as a bug. An issue discovered at
different times will take different forms. A trivial example would be
"Spoofing" at the design stage of a web application.

When creating a user story, the user in question may think "I want secure
authentication so that only I can access my data". During the development
stage, "Spoofing" may appear while threat modeling - and thus considered a bug,
if it appeared upon realising that changing their account password does not
require the user to input the current password.

## Considerations

* Changed whiteboard diagrams
* Bugs
* Requirements (Technical or Procedural)
* New user stories in the backlog
* Using wikis at the intermediate stage
* Findings 
* Classifying bugs as threats
* Organizational discipline:
    * Agreement 
    * Driving discussion using threat modeling
    * Tagging

## Possible Responses

1. Take the bug out of threat modeling and consider what needs to happen next,
weighting the risk vs value for the bug and the attention it receives as part
of priorisation. 
2. Allow whoever creates priorities during threat modeling to contextualise the 
risk, then make the decision on what should be immediately prioritised, what 
should be put aside, and what research is necessary for further focus later on.

*Response 2 is preferable to response 1.*

## Follow Up

Deliver the decisions and changes to:
* Software
* Operations/IT
* Risk management
