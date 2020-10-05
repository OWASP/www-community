---

layout: col-sidebar
title: Full Path Disclosure
author: 
contributors: 
permalink: /attacks/Full_Path_Disclosure
tags: attack, Full Path Disclosure
auto-migrated: 1

---

{% include writers.html %}

## Description

Full Path Disclosure (FPD) vulnerabilities enable the attacker to see
the path to the webroot/file. e.g.: /home/omg/htdocs/file/. Certain
vulnerabilities, such as using the load_file() (within a [SQL
Injection](https://owasp.org/www-community/attacks/SQL_Injection)) query to view the page source,
require the attacker to have the full path to the file they wish to
view.

## Risk Factors

The risks regarding FPD may produce various outcomes. For example, if
the webroot is getting leaked, attackers may abuse the knowledge and use
it in combination with file inclusion vulnerabilites (see [PHP File
Inclusion](https://owasp.org/www-community/vulnerabilities/PHP_File_Inclusion)) to steal
configuration files regarding the web application or the rest of the
operating system.

    Warning: session_start() [function.session-start]: The session id contains illegal characters,
    valid characters are a-z, A-Z, 0-9 and '-,' in /home/example/public_html/includes/functions.php on line 2

In combination with, say, unproteced use of the PHP function
file_get_contents, the attacker gets an opportunity to steal
configuration files.

**The sourcecode of index.php:**

    <?php
       echo file_get_contents(getcwd().$_GET['page']);
    ?>

An attacker crafts a URL like so:
`http://example.org/index.php?page=../../../../../../../home/example/public_html/includes/config.php`
with the knowledge of the FPD in combination with [Relative Path
Traversal](https://owasp.org/www-community/attacks/Path_Traversal).

**The leaked sourcecode of config.php:**

    <?php
       //Hidden configuration file containing database credentials.
       $hostname = 'localhost';
       $username = 'root';
       $password = 'owasp_fpd';
       $database = 'example_site';
       $connector = mysql_connect($hostname, $username, $password);
       mysql_select_db($database, $connector);
    ?>

Disregarding the above sample, FPD can also be used to reveal the
underlaying operation system by observing the file paths. Windows for
instance always start with a drive-letter, e.g; C:\\, while Unix based
operating system tend to start with a single front slash.

**\*NIX:**

    Warning: session_start() [function.session-start]: The session id contains illegal characters,
    valid characters are a-z, A-Z, 0-9 and '-,' in /home/alice/public_html/includes/functions.php on line 2

**Microsoft Windows:**

    Warning: session_start() [function.session-start]: The session id contains illegal characters,
    valid characters are a-z, A-Z, 0-9 and '-,' in C:\Users\bob\public_html\includes\functions.php on line 2

The FPD may reveal a lot more than people normally might suspect. The
two examples above reveal usernames on the operating systems as well;
"**alice**" and "**bob**". Usernames are of course important pieces of
credentials. Attackers can use those in many different ways, ranging all
from bruteforcing over various protocols (SSH, Telnet, RDP, FTP...) to
launching exploits requiring working usernames.

## Examples

**Empty Array**

If we have a site that uses a method of requesting a page like this:

    http://example.org/index.php?page=about

We can use a method of opening and closing braces that causes the page
to output an error. This method would look like this:

    http://example.org/index.php?page[]=about

This renders the page defunct thus spitting out an error:

    Warning: opendir(Array): failed to open dir: No such file or directory in /home/omg/htdocs/index.php on line 84
    Warning: pg_num_rows(): supplied argument ... in /usr/home/example/html/pie/index.php on line 131

**Null Session Cookie**

Another popular and very reliable method of producing errors containing
a FPD is to give the page a nulled session using JavaScript Injections.
A simple injection using this method would look something like so:

    javascript:void(document.cookie="PHPSESSID=");

By simply setting the PHPSESSID cookie to nothing (null) we get an
error.

    Warning: session_start() [function.session-start]: The session id contains illegal characters,
    valid characters are a-z, A-Z, 0-9 and '-,' in /home/example/public_html/includes/functions.php on line 2

This vulnerability is prevented simply by turning error reporting off so
your code does not spit out errors.

    error_reporting(0);

Errors can contain useful information for site owner so instead of
disabling the error reporting at all, it is possible to only hide errors
from output by
[display_errors](http://www.php.net/errorfunc.configuration#ini.display-errors).

**Invalid Session Cookie**

As a complement to the Null Session Cookie, a very long session could
also produce an error containing FPD. This could also be accomplished
using a JavaScript injection like so:

    javascript:void(document.cookie='PHPSESSID=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA');

By simply setting the PHPSESSID cookie to 129 bytes or more, PHP may
spit out a warning.

Another approach would be to to set the PHPSESSID cookie data to one of
the reserved bytes.

    javascript:void(document.cookie='PHPSESSID=.');

Both variants result in the following.

    Warning: session_start(): The session id is too long or contains illegal characters,
    valid characters are a-z, A-Z, 0-9 and '-,' in /home/example/public_html/includes/functions.php on line 2

The same remedy as for Null Session Cookie may be applied here. Errors
may be hidden from the output by
[display_errors](http://www.php.net/errorfunc.configuration#ini.display-errors).

**Direct Access to files that requires preloaded library files**

Web application developers sometimes fail to add safe checks in files
that requires preloaded library/function files. This is prone to reveal
possible sensitive information when those applications' URLs are
directly requested. Sometimes, it's a clue to Local File Inclusion
vulnerability.

Concerning with Mambo CMS, if we access to a direct url,
<http://example.org/mambo/mambots/editors/mostlyce/jscripts/tiny_mce/plugins/spellchecker/classes/PSpellShell.php>,
then we gets

    <br />
    <b>Fatal error</b>:  Class 'SpellChecker' not found in <b>/home/victim/public_html/mambo/mambots/editors/mostlyce/jscripts/tiny_mce/plugins/spellchecker/classes/PSpellShell.php</b> on line <b>9</b><br />

## Tool

The above three checks can be done with the aid of
[inspathx](https://code.google.com/p/inspathx/) tool.

## Related [Threat Agents](Threat_Agents "wikilink")

  - [internal software
    developer](internal_software_developer "wikilink")

## Related [Attacks](https://owasp.org/www-community/attacks/)

  - [SQL Injection](https://owasp.org/www-community/attacks/SQL_Injection)
  - [Relative Path Traversal](https://owasp.org/www-community/attacks/Path_Traversal)

## Related [Vulnerabilities](https://owasp.org/www-community/vulnerabilities/)

  - None

## Related [Controls](https://owasp.org/www-community/controls/)

  - [Error Handling](Error_Handling "wikilink")
  - [Bounds Checking](Bounds_Checking "wikilink")
  - [Safe Libraries](Safe_Libraries "wikilink")
  - [Static Code Analysis](Static_Code_Analysis "wikilink")
  - [Executable space
    protection](Executable_space_protection "wikilink")
  - [Address space layout randomization
    (ASLR)](Address_space_layout_randomization_\(ASLR\) "wikilink")
  - [Stack-smashing Protection
    (SSP)](Stack-smashing_Protection_\(SSP\) "wikilink")

## References

  - <http://www.acunetix.com/vulnerabilities/Full-path-disclosure.htm>
  - [Articled summarised from Full Path Disclosure article by haZed on
    EnigmaGroup.org.](http://www.enigmagroup.org/)
  - [Path Disclosure Vulnerability - Is it
    serious?](http://yehg.net/lab/pr0js/view.php/path_disclosure_vulnerability.txt)
  - [inspathx - Internal Path Disclosure
    Finder](http://yehg.net/lab/pr0js/files.php/inspath.zip)

__NOTOC__

[Category:OWASP ASDR Project](Category:OWASP_ASDR_Project "wikilink")
[Category:Injection](https://owasp.org/www-community/Injection_Flaws)
[Category:Attack](Category:Attack "wikilink")
