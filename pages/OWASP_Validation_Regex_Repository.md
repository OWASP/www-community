---

title: OWASP Validation Regex Repository
layout: col-sidebar
author:
contributors:
tags: regex, validation
permalink: /OWASP_Validation_Regex_Repository

---

{% include writers.html %}

    Note: These Regexs are examples and not built for a particular Regex
    engine. However, the PCRE syntax is mainly used. In particular, this
    means that character classes do not contain meta characters which
    need to be escaped, except the `-` and `]` character, where it is
    assumed that a `-` needs not to be escaped only when it is the last
    character in a character class. The character class supports
    shortcut notations for other character classes like `\s` or `\w`
    which should not be used as they depend on the LOCALE environment
    setting in most systems.

Please carefully test the regex in your regex engine.

    <?xml version="1.0"?>

      <regex>
        <name>url</name>
        <pattern><![CDATA[^((((https?|ftps?|gopher|telnet|nntp)://)|(mailto:|news:))(%[0-9A-Fa-f]{2}|[-()_.!~*';/?:@&=+$,A-Za-z0-9])+)([).!';/?:,][[:blank:|:blank:]])?$]]></pattern>
        <description>A valid URL per the URL spec.</description>
      </regex>

      <regex>
        <name>IP</name>
        <pattern><![CDATA[^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$]]></pattern>
        <description>A valid IP Address</description>
      </regex>

      <regex>
        <name>e-mail</name>
        <pattern><![CDATA[^[a-zA-Z0-9_+&*-]+(?:\.[a-zA-Z0-9_+&*-]+)*@(?:[a-zA-Z0-9-]+\.)+[a-zA-Z]{2,7}$]]></pattern>
        <description>A valid e-mail address</description>
      </regex>

      <regex>
        <name>safetext</name>
        <pattern><![CDATA[^[a-zA-Z0-9 .-]+$]]></pattern>
        <description>Lower and upper case letters and all digits</description>
      </regex>

      <regex>
        <name>date</name>
        <pattern><![CDATA[^(?:(?:(?:0?[13578]|1[02])(\/|-|\.)31)\1|(?:(?:0?[1,3-9]|1[0-2])(\/|-|\.)(?:29|30)\2))(?:(?:1[6-9]|[2-9]\d)?\d{2})$|^(?:0?2(\/|-|\.)29\3(?:(?:(?:1[6-9]|[2-9]\d)?(?:0[48]|[2468][048]|[13579][26])|(?:(?:16|[2468][048]|[3579][26])00))))$|^(?:(?:0?[1-9])|(?:1[0-2]))(\/|-|\.)(?:0?[1-9]|1\d|2[0-8])\4(?:(?:1[6-9]|[2-9]\d)?\d{2})$]]></pattern>
        <description>Date in US format with support for leap years</description>
      </regex>

      <regex>
        <name>creditcard</name>
        <pattern><![CDATA[^((4\d{3})|(5[1-5]\d{2})|(6011)|(7\d{3}))-?\d{4}-?\d{4}-?\d{4}|3[4,7]\d{13}$]]></pattern>
        <description>A valid credit card number</description>
      </regex>

      <regex>
        <name>password</name>
        <pattern><![CDATA[^(?=.*\d)(?=.*[a-z])(?=.*[A-Z]).{4,8}$]]></pattern>
        <description>4 to 8 character password requiring numbers and both lowercase and uppercase letters</description>
      </regex>

      <regex>
        <name>complexpassword</name>
        <pattern><![CDATA[^(?:(?=.*\d)(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[^A-Za-z0-9])(?=.*[a-z])|(?=.*[^A-Za-z0-9])(?=.*[A-Z])(?=.*[a-z])|(?=.*\d)(?=.*[A-Z])(?=.*[^A-Za-z0-9]))(?!.*(.)\1{2,})[A-Za-z0-9!~<>,;:_=?*+#."&§%°()\|\[\]\-\$\^\@\/]{12,128}$]]></pattern>
        <description>12 to 128 character password requiring at least 3 out 4 (uppercase and lowercase letters, numbers and special characters) and no more than 2 equal characters in a row</description>
      </regex>

      <regex>
        <name>English_digitwords</name>
        <pattern><![CDATA[^(zero|one|two|three|four|five|six|seven|eight|nine)$]]></pattern>
        <description>The English words representing the digits 0 to 9</description>
      </regex>

      <regex>
        <name>English_daywords</name>
        <pattern><![CDATA[^(Mo|Tu|We|Th|Fr|Sa|Su)$]]></pattern>
        <description>English 2 character abbreviations for the days of the week</description>
      </regex>

      <regex>
        <name>English_monthwords</name>
        <pattern><![CDATA[^(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)$]]></pattern>
        <description>English 3 character abbreviations for the months</description>
      </regex>

      <regex>
        <name>French_digitwords</name>
        <pattern><![CDATA[^(z[eé]ro|un|deux|trois|quatre|cinq|six|sept|huit|neuf)$]]></pattern>
        <description>The French words representing the digits 0 to 9</description>
      </regex>

      <regex>
        <name>German_digitwords</name>
        <pattern><![CDATA[^(null|eins|zwei|drei|vier|f(ue|ü)nf|sechs|sieben|acht|neun)$]]></pattern>
        <description>The German words representing the digits 0 to 9</description>
      </regex>

      <regex>
        <name>Spanish_digitwords</name>
        <pattern><![CDATA[^(cero|uno|dos|tres|cuatro|cinco|seis|siete|ocho|nueve)$]]></pattern>
        <description>The Spanish words representing the digits 0 to 9</description>
      </regex>

      <regex>
        <name>US_zip</name>
        <pattern><![CDATA[^\d{5}(-\d{4})?$]]></pattern>
        <description>US zip code with optional dash-four</description>
      </regex>

      <regex>
        <name>US_phone</name>
        <pattern><![CDATA[^\D?(\d{3})\D?\D?(\d{3})\D?(\d{4})$]]></pattern>
        <description>US phone number with or without dashes</description>
      </regex>

      <regex>
        <name>US_state</name>
        <pattern><![CDATA[^(AE|AL|AK|AP|AS|AZ|AR|CA|CO|CT|DE|DC|FM|FL|GA|GU|HI|ID|IL|IN|IA|KS|KY|LA|ME|MH|MD|MA|MI|MN|MS|MO|MP|MT|NE|NV|NH|NJ|NM|NY|NC|ND|OH|OK|OR|PW|PA|PR|RI|SC|SD|TN|TX|UT|VT|VI|VA|WA|WV|WI|WY)$]]></pattern>
        <description>2 letter U.S. state abbreviations</description>
      </regex>

      <regex>
        <name>US_ssn</name>
        <pattern><![CDATA[^\d{3}-\d{2}-\d{4}$]]></pattern>
        <description>9 digit U.S. social security number with dashes</description>
      </regex>

      <!-- Some additional examples that have not been vetted

           // HTML HEX CODE   ^#?([a-f]|[A-F]|[0-9]){3}(([a-f]|[A-F]|[0-9]){3})?$
           // FLOATING POINT   ^[-+]?[0-9]+[.]?[0-9]*([eE][-+]?[0-9]+)?$
           // PERSON NAME   ^[a-zA-Z]+(([',. -][a-zA-Z ])?[a-zA-Z]*)*$
           // MAC ADDRESS  ^([0-9a-fA-F][0-9a-fA-F]:){5}([0-9a-fA-F][0-9a-fA-F])$
           // GUID    ^[A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}$
           // IP ADDRESS  ^\b((25[0-5]|2[0-4]\d|[01]\d\d|\d?\d)\.){3}(25[0-5]|2[0-4]\d|[01]\d\d|\d?\d)\b$
           // IP ADDRESS (^\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b$
           // REASONABLE DOMAIN NAME   ^([a-zA-Z0-9]([a-zA-Z0-9\-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,6}$
           // RFC 1918 NON ROUTABLE IP   ^(((25[0-5]|2[0-4][0-9]|19[0-1]|19[3-9]|18[0-9]|17[0-1]|17[3-9]|1[0-6][0-9]|1[1-9]|[2-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9]))|(192\.(25[0-5]|2[0-4][0-9]|16[0-7]|169|1[0-5][0-9]|1[7-9][0-9]|[1-9][0-9]|[0-9]))|(172\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|1[0-5]|3[2-9]|[4-9][0-9]|[0-9])))\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(25[0-5]|2[0-4][0-9]|1[0-9][0-9]|[1-9][0-9]|[0-9])$
           // VALID WINDOWS FILENAME  ^(?!^(PRN|AUX|CLOCK\$|NUL|CON|COM\d|LPT\d|\..*)(\..+)?$)[^\x00-\x1f\\?*:\";|/]+$
           //
           //
           // Warning, per https://en.wikipedia.org/wiki/ReDoS the Java Classname RegEx below is vulnerable to RegExDos
           // Java Classname  ^(([a-z])+.)+[A-Z]([a-z])+$
           // The correct RegEx for java classnames is the following one, and not vulnerable:
           // Java Classname  ^(([a-z])+\.)+[A-Z]([a-zA-Z])+$
           //
           //  ANY PLATFORM FILENAME   ^(([a-zA-Z]:|\\)\\)?(((\.)|(\.\.)|([^\\/:*?"|<>. ](([^\\/:*?"|<>. ])|([^\\/:*?"|<>]*[^\\/:*?"|<>. ]))?))\\)*[^\\/:*?"|<>. ](([^\\/:*?"|<>. ])|([^\\/:*?"|<>]*[^\\/:*?"|<>. ]))?$
      -->

# Other Regex References

**Regex Library Site**

<http://regexlib.com>: A site that has a HUGE library of regular
expressions and other regex resources

**Regex Tutorial Site**

<http://www.regular-expressions.info>: A site with lots of tutorials on
writing Regexs and numerous examples

**Regex Construction Tool**

<http://www.ultrapico.com/Expresso.htm>: A free regex construction tool

**Regex Explanation Tool**

<http://rick.measham.id.au/paste/explain.pl?regex=.*>: Explains in
English what the supplied regex means
