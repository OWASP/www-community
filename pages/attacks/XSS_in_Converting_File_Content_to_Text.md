---

layout: col-sidebar
title: XSS in Converting File Content to Text
author: Mohammad Reza Omrani
contributors: 
permalink: /attacks/XSS_in_Converting_File_Content_to_Text
tags: [attack, XSS]

---

 {% include writers.html %}

## Description

Attackers may be able to execute JavaScript during the conversion of the content
of a file to text, which is commonly known as Cross-Site Scripting (XSS).
If an image containing XSS payload is imported into an image-to-text program,
its output may result in execution of JavaScript code. This vulnerability has been
verified by testing some services that translate text from photos and convert
photos to text. This same process may apply to other vulnerabilities as well!

## Examples

Attackers can use programs like Paint to write payloads on blank white photos and send them to targets.
![first example](../assets/images/XSS_in_Converting_File_Content_to_Text.png)
