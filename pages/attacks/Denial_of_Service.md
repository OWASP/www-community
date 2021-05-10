---

layout: col-sidebar
title: Denial of Service
author: Nsrav
contributors: KristenS, Adar Weidman, psiinon, Adrew Smith, Jkurucar, kingthorin
permalink: /attacks/Denial_of_Service
tags: attack, Denial of Service

---

{% include writers.html %}

## Description

The Denial of Service (DoS) attack is focused on making a resource
(site, application, server) unavailable for the purpose it was designed.
There are many ways to make a service unavailable for legitimate users
by manipulating network packets, programming, logical, or resources
handling vulnerabilities, among others. If a service receives a very
large number of requests, it may cease to be available to legitimate
users. In the same way, a service may stop if a programming
vulnerability is exploited, or the way the service handles resources it
uses.

Sometimes the attacker can inject and execute arbitrary code while
performing a DoS attack in order to access critical information or
execute commands on the server. Denial-of-service attacks significantly
degrade the service quality experienced by legitimate users. These
attacks introduce large response delays, excessive losses, and service
interruptions, resulting in direct impact on availability.

## Risk Factors

Risk factors can break down into multiple categories. Two principle
sources of risk include inadequate resources and non-technical threat
motivators.

The first example of a risk factor, inadequate resources, requires
attention if system architecture was not designed to meet traffic demand
overflows. This risk reduces the difficulty of successfully executing a
DoS attack and can, left unchecked, result in DoS symptoms absent an
actual attack.

The second example and perhaps the largest risk factor is not technical
and is in the domain of public relations or strategic communications. An
organization should avoid taking action that can make them a target of a
DoS attack unless the benefits of doing so outweigh the potential costs
or mitigating controls are in place.

Other risk factors may also exist depending on the specific environment.

## Examples

The following DoS techniques and examples were extracted from OWASP
Testing Guide v2.

### DoS User Specified Object Allocation

If users can supply, directly or indirectly, a value that will specify
how many of an object to create on the application server, and if the
server does not enforce a hard upper limit on that value, it is possible
to cause the environment to run out of available memory. The server may
begin to allocate the required number of objects specified, but if this
is an extremely large number, it can cause serious issues on the server,
possibly filling its whole available memory and corrupting its
performance.

The following is a simple example of vulnerable code in Java:

```java
String TotalObjects = request.getParameter(“numberofobjects”);
int NumOfObjects = Integer.parseInt(TotalObjects);
ComplexObject[] anArray = new ComplexObject[NumOfObjects];  // wrong!
```

### DoS User Input as a Loop Counter

Similar to the previous problem of User Specified Object Allocation, if
the user can directly or indirectly assign a value that will be used as
a counter in a loop function, this can cause performance problems on the
server.

The following is an example of vulnerable code in Java:

```java
public class MyServlet extends ActionServlet {
   public void doPost(HttpServletRequest request, HttpServletResponse response)
          throws ServletException, IOException {
          . . .
          String [] values = request.getParameterValues("CheckboxField");
      // Process the data without length check for reasonable range – wrong!
          for ( int i=0; i<values.length; i++) {
                // lots of logic to process the request
         }
         . . .
   }
    . . .
}
```

As we can see in this simple example, the user has control over the loop
counter. If the code inside the loop is very demanding in terms of
resources, and an attacker forces it to be executed a very high number
of times, this might decrease the performance of the server in handling
other requests, causing a DoS condition.

### DoS Failure to Release Resources

If an error occurs in the application that prevents the release of an
in-use resource, it can become unavailable for further use. Possible
examples include:

  - An application locks a file for writing, and then an exception occurs but does not explicitly close and unlock the file
  - Memory leaking in languages where the developer is responsible for memory management such as C & C++. In the case where an error causes normal logic flow to be circumvented, the allocated memory may not be removed and may be left in such a state that the garbage collector does not know it should be reclaimed
  - Use of DB connection objects where the objects are not being freed if an exception is thrown. A number of such repeated requests can cause the application to consume all the DB connections, as the code will still hold the open DB object, never releasing the resource.

The following is an example of vulnerable code in Java. In the example,
both the Connection and the CallableStatement should be closed in a
finally block.

```
public class AccountDAO {
    … …
    public void createAccount(AccountInfo acct)
                 throws AcctCreationException {
       … …
           try {
            Connection conn = DAOFactory.getConnection();
            CallableStatement  calStmt = conn.prepareCall(…);
          …  … 
           calStmt.executeUpdate();
           calStmt.close();
          conn.close();
       }  catch (java.sql.SQLException e) {
            throw AcctCreationException (...);
       }
    }
}
```

### DoS Buffer Overflows

Any language where the developer has direct responsibility for managing
memory allocation, most notably C & C++, has the potential for a [Buffer
Overflow](Buffer_Overflow_attack). While the most serious risk
related to a buffer overflow is the ability to execute arbitrary code on
the server, the first risk comes from the denial of service that can
happen if the application crashes.

The following is a simplified example of vulnerable code in C:

```c
void overflow (char *str) {
   char buffer[10];
   strcpy(buffer, str); // Dangerous!
}

int main () {
  char *str = "This is a string that is larger than the buffer of 10";
  overflow(str);
}
```

If this code example were executed, it would cause a segmentation fault
and dump core. The reason is that strcpy would try to copy 53 characters
into an array of 10 elements only, overwriting adjacent memory
locations. While this example above is an extremely simple case, the
reality is that in a web based application there may be places where the
user input is not adequately checked for its length, making this kind of
attack possible.

### DoS Storing too Much Data in Session

Care must be taken not to store too much data in a user session object.
Storing too much information in the session, such as large quantities of
data retrieved from the database, can cause denial of service issues.
This problem is exacerbated if session data is also tracked prior to a
login, as a user can launch the attack without the need of an account.

### DoS Locking Customer Accounts

The first DoS case to consider involves the authentication system of the
target application. A common defense to prevent brute-force discovery of
user passwords is to lock an account from use after between three to
five failed attempts to login. This means that even if a legitimate user
were to provide their valid password, they would be unable to login to
the system until their account has been unlocked. This defense mechanism
can be turned into a DoS attack against an application if there is a way
to predict valid login accounts.

Note, there is a business vs. security balance that must be reached
based on the specific circumstances surrounding a given application.
There are pros and cons to locking accounts, to customers being able to
choose their own account names, to using systems such as CAPTCHA, and
the like. Each enterprise will need to balance these risks and benefits,
but not all of the details of those decisions are covered here.

## Related [Attacks](https://owasp.org/www-community/attacks/)

- [Resource Injection](https://owasp.org/www-community/attacks/Resource_Injection)

## References

- [Denial of Service through Resource Depletion](http://capec.mitre.org/data/index.html)
