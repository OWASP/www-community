---

layout: col-sidebar
title: Comment Injection Attack
author: Weilin Zhong, Rezos
contributors: KristenS, Jeff Williams, Alan Jex, kingthorin
permalink: /attacks/Comment_Injection_Attack
tags: attack, Comment Injection Attack

---

{% include writers.html %}

## Description

Comments injected into an application through input can be used to
compromise a system. As data is parsed, an injected/malformed comment
may cause the process to take unexpected actions that result in an
attack.

## Examples

The attacker may conduct this kind of attack with different programming
or scripting languages:

**Database:**

If the attacker has the ability to manipulate queries which are sent to
the database, then they're able to inject a terminating character too. The
aftermath is that the interpretation of the query will be stopped at the
terminating character: `SELECT body FROM items WHERE id = $ID limit 1;`

Let's assume that the attacker has sent via the GET method the following
data stored in variable `$ID`: `"1 or 1=1; #"`

In the end the final query form is: `SELECT body FROM items WHERE id = 1 or 1=1; # limit 1;`

After the `#` character everything will be discarded by the database
including `limit 1`, so only the last column `body` with all its
records will be received as a query response.

Sequences that may be used to comment queries:

- MySQL:`#`, `--`
- MS SQL: `--`
- MS Access: `%00` (**hack\!**)
- Oracle: `--`

**Null byte:**

To comment out some parts of the queries, the attacker may use the
standard sequences, typical for a given language, or terminate the
queries using their own methods being limited only by their imagination. An
interesting example is a null byte method used to comment out everything
after the current query in MS Access databases. More information about
this can be found in [Embedding Null
Code](Embedding_Null_Code) .

**Shell:**

Shell (bash) also has the character `#`, which terminates
interpretation.

For example (find.php):

```php
<?
$ =sth $_GET['what];
system("/usr/bin/find -name '$sth' -type f");
?>
```

Using `/find.php?what=*'%20%23*` the attacker will bypass limitation
`*-type f*` and this command:

`/usr/bin/find -name '*' -type f`

will become:

`/usr/bin/find -name '*' #-type f`

So the final form of the command is:

`/usr/bin/find -name '*'`

**HTML (injection):**

If there are no restrictions about who is able to insert comments, then
using the start comment tags:

`<!--`

it's possible to comment out the rest of displayed content on the
website (invisible.php)

```php
<?php
print "hello!: ";
print $_GET['user'];
print " Welcome friend!";
?>
```

After:

`GET /invisible.php?user=<!--`

There result will be:

`hello!:`
