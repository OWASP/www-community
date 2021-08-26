---

layout: col-sidebar
title: CSV Injection
author: Timo Goosen, Albinowax
contributors: kingthorin
permalink: /attacks/CSV_Injection
tags: attack, vulnerability, CSV Injection

---

{% include writers.html %}

CSV Injection, also known as Formula Injection, occurs when websites
embed untrusted input inside CSV files.

When a spreadsheet program such as Microsoft Excel or LibreOffice Calc
is used to open a CSV, any cells starting with `=` will be interpreted
by the software as a formula. Maliciously crafted formulas can be used
for three key attacks:

- Hijacking the user's computer by exploiting vulnerabilities in the spreadsheet software, such as CVE-2014-3524.
- Hijacking the user's computer by exploiting the user's tendency to ignore security warnings in spreadsheets that they downloaded from their own website.
- Exfiltrating contents from the spreadsheet, or other open spreadsheets.

This attack is difficult to mitigate, and explicitly disallowed from
quite a few bug bounty programs. To remediate it, ensure that no cells
begin with any of the following characters:

- Equals to (`=`)
- Plus (`+`)
- Minus (`-`)
- At (`@`)
- Tab (`0x09`)
- Carriage return (`0x0D`)

Keep in mind that it is not sufficient to make sure that the untrusted user input does not start with these characters. You also need to take care of the field separator (e.g., '`,`', or '`;`') and quotes (e.g., `'`, or `"`), as attackers could use this to start a new cell and then have the dangerous character in the middle of the user input, but at the beginning of a cell.

Alternatively, apply the following sanitization to each field of the CSV, so that their content will be read as text by the spreadsheet editor:
* Wrap each cell field in double quotes
* Prepend each cell field with a single quote
* Escape every double quote using an additional double quote

 Two examples:

| Input                    | Escaped Output      |
|--------------------------|---------------------|
| `=1+2";=1+2`             | `"'=1+2"";=1+2"`   |
| `=1+2'" ;,=1+2`          | `"'=1+2'"" ;,=1+2"` |

For further information, please refer to the following articles:

- [Comma Separated Vulnerabilities](https://www.contextis.com/resources/blog/comma-separated-vulnerabilities/)
- [Video showing CSV Injection against Piwik](https://www.youtube.com/watch?v=SC7AkclnG2g)
- [Stealing Google Docs via CSV Injection](http://georgemauer.net/2017/10/07/csv-injection.html)
