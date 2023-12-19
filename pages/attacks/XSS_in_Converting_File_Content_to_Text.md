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

## Attack Scenario

An attacker can use an image that contains an XSS payload to execute JavaScript
code on the website. The following descriptions will explain the different stages
of this scenario and how the XSS attack unfolds within this process.

![Attack Scenario](../assets/images/attacks/XSS_in_Converting_File_Content_to_Text_Attack_Scenario.png)
    
Image Upload:
- An attacker uploads an image containing an XSS payload to the website.

OCR Execution:
- The OCR system identifies and analyzes the content of the image.

Text Extraction:
- The system extracts the text containing the XSS payload from the image.

Display Output:
- The XSS payload is executed on the website.

## Examples

An attacker can use a program like Paint to write the payload on a blank image
and send it to the website.

![payload example](../assets/images/attacks/XSS_in_Converting_File_Content_to_Text_2.png)

## Related Controls

- [Data Validation](https://wiki.owasp.org/index.php/Data_Validation)

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [XSS Attacks](https://owasp.org/www-community/attacks/xss/)
