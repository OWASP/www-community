---

layout: col-sidebar
title: Brute Force Attack
author:
contributors: Gsami, Rezos, Thiagoalz, KristenS, D0ubl3 h3lix, Andrew Smith, Jenjava1762, Mtesauro, kingthorin
permalink: /attacks/Brute_force_attack
tags: attack, brute force

---

{% include writers.html %}

## Related Security Activities

### How to Test for Brute Force Vulnerabilities

See the [OWASP Testing Guide](https://owasp.org/www-project-web-security-testing-guide/) article on how to
Test for Brute Force Vulnerabilities.

## Description

A brute force attack can manifest itself in many different ways, but
primarily consists in an attacker configuring predetermined values,
making requests to a server using those values, and then analyzing the
response. For the sake of efficiency, an attacker may use a dictionary
attack (with or without mutations) or a traditional brute-force attack
(with given classes of characters e.g.: alphanumeric, special, case
(in)sensitive). Considering a given method, number of tries, efficiency
of the system which conducts the attack, and estimated efficiency of the
system which is attacked the attacker is able to calculate approximately
how long it will take to submit all chosen predetermined values.

## Risk Factors

## Examples

Brute-force attacks are often used for attacking authentication and
discovering hidden content/pages within a web application. These attacks
are usually sent via GET and POST requests to the server. In regards to
authentication, brute force attacks are often mounted when an [account
lockout policy](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html#account-lockout)
is not in place.

### Example 1

A web application can be attacked via brute force by taking a word list
of known pages, for instance from a popular content management system,
and simply requesting each known page then analyzing the HTTP response
code to determine if the page exists on the target server.

[DirBuster](https://wiki.owasp.org/index.php/Category:OWASP_DirBuster_Project)
is a tool that does exactly this.

Other tools for this type of attack are as follows:

- [dirb](http://sourceforge.net/projects/dirb/)
- [WebRoot](http://www.cirt.dk/tools/webroot/WebRoot.txt)

dirb is capable of:

- setting cookies
- adding any HTTP header
- using PROXY
- mutating objects which were found
- testing http(s) connections
- seeking catalogues or files using defined dictionaries and templates
- and much much more

The simplest test to perform is:

```console
rezos@dojo ~/d/owasp_tools/dirb $ ./dirb http://testsite.test/
-----------------
DIRB v1.9
By The Dark Raver
-----------------
START_TIME: Mon Jul  9 23:13:16 2007
URL_BASE: http://testsite.test/
WORDLIST_FILES: wordlists/common.txt
SERVER_BANNER: lighttpd/1.4.15
NOT_EXISTANT_CODE: 404 [NOT FOUND]
(Location: '' - Size: 345)

-----------------

Generating Wordlist...
Generated Words: 839

---- Scanning URL: http://testsite.test/ ----
FOUND: http://testsite.test/phpmyadmin/
       (***) DIRECTORY (*)
```

In the output the attacker is informed that `phpmyadmin/` directory was
found. The attacker has now found a potential directory of interest
within this application. In dirb's templates there are, among others, a
dictionary containing information about invalid httpd configurations.
This dictionary will detect weaknesses of this kind.

The application
[WebRoot.pl](http://www.cirt.dk/tools/webroot/WebRoot.txt), written by
CIRT.DK, has embedded mechanisms for parsing server responses, and based
on the phrase specified by the attacker, measures if the server response
is expected.

For example:

Np.

```console
./WebRoot.pl -noupdate -host testsite.test -port 80 -verbose -match "test" -url "/private/<BRUTE>" -incremental lowercase -minimum 1 -maximum 1

`oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00`
`o          Webserver Bruteforcing 1.8          o`
`0  ************* !!! WARNING !!! ************  0`
`0  ******* FOR PENETRATION USE ONLY *********  0`
`0  ******************************************  0`
`o       (c)2007 by Dennis Rand - CIRT.DK       o`
`oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00`

`[X] Checking for updates                - NO CHECK`
`[X] Checking for False Positive Scan    - OK`
`[X] Using Incremental                   - OK`
`[X] Starting Scan                       - OK`
`   GET /private/b HTTP/1.1`
`   GET /private/z HTTP/1.1`

`[X] Scan complete                       - OK`
`[X] Total attempts                      - 26`
`[X] Sucessfull attempts                 - 1`
`oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00oo00`

WebRoot.pl found one file "/private/b" on testsite.test, which contains
phrase "test".
```

Another example is to examine ranges of the variable's values:

`./WebRoot.pl -noupdate -host testsite.test -port 80 -verbose -diff "Error" -url "/index.php?id=<BRUTE>" -incremental integer -minimum 1 -maximum 1`

  - Road Blocks:

One of the main issues with tools like dirb/dirbuster consist in the
analysis of server responses. With more advanced server configuration
(e.g. with mod_rewrite) automatic tools are sometimes unable to
determine "File not found" errors due to the server response being an
HTTP response code 200 but the page itself indicates "File not found".
This can lead to false positives if the brute force tool is only relying
on HTTP response codes.

[Burp Suite](http://portswigger.net/), can be used to parse specific parts of
the page returned, looking for certain strings in an effort to reduce
false positives.

### Example 2

In regards to authentication, when no password policy is in place an
attacker can use lists of common username and passwords to brute force a
username or password field until successful authentication.

## Defensive Tools

[Php-Brute-Force-Attack Detector](http://yehg.net/lab/pr0js/files.php/php_brute_force_detect.zip)

Detect your web servers being scanned by brute force tools such as
WFuzz, OWASP DirBuster and vulnerability scanners such as Nessus, Nikto,
Acunetix, etc. This helps you quickly identify probable probing by bad
actors who want to dig possible security holes.

[Docs](http://yehg.net/lab/pr0js/tools/php-brute-force-detector-readme.pdf)


## References

[DirBuster](https://wiki.owasp.org/index.php/Category:OWASP_DirBuster_Project)
