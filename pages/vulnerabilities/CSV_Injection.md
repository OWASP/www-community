---

layout: col-sidebar
title: CSV Injection.md
author: 
contributors: 
permalink: /vulnerabilities/CSV_Injection
tag: vulnerability, CSV Injection.md
auto-migrated: 1

---

CSV Injection, also known as Formula Injection, occurs when websites
embed untrusted input inside CSV files.

When a spreadsheet program such as Microsoft Excel or LibreOffice Calc
is used to open a CSV, any cells starting with '=' will be interpreted
by the software as a formula. Maliciously crafted formulas can be used
for three key attacks:

  - Hijacking the user's computer by exploiting vulnerabilities in the
    spreadsheet software, such as CVE-2014-3524
  - Hijacking the user's computer by exploiting the user's tendency to
    ignore security warnings in spreadsheets that they downloaded from
    their own website
  - Exfiltrating contents from the spreadsheet, or other open
    spreadsheets.

This attack is difficult to mitigate, and explicitly disallowed from
quite a few bug bounty programs. To remediate it, ensure that no cells
begin with any of the following characters:

  - Equals to ("=")
  - Plus ("+")
  - Minus ("-")
  - At ("@")

For further information, please refer to the following articles:

  - [Comma Separated
    Vulnerabilities](https://www.contextis.com/resources/blog/comma-separated-vulnerabilities/)
  - [Video showing CSV Injection against
    Piwik](https://www.youtube.com/watch?v=SC7AkclnG2g)
  - [Stealing Google Docs via CSV
    Injection](http://georgemauer.net/2017/10/07/csv-injection.html)

[Category:Vulnerability](Category:Vulnerability "wikilink")
[Category:Attack](Category:Attack "wikilink")