---
title: Fail Securely
layout: col-sidebar
author:
contributors: Daniel Waller
tags: principles
permalink: /Fail_securely
---

{% include writers.html %}

## Description
Handling errors securely is a key aspect of secure coding. 
There are two types of errors that deserve special attention. 

The first is exceptions that occur in the processing of a security control itself. 
It's important that these exceptions do not enable behavior that the countermeasure would normally not allow. 
As a developer, you should consider that there are generally three possible outcomes from a security mechanism:
* allow the operation
* disallow the operation
* exception

In general, you should design your security mechanism so that a failure will follow the same execution path as disallowing the operation. 
For example, security methods like isAuthorized(), isAuthenticated(), and validate() should all return false if there is an exception during processing. 
If security controls can throw exceptions, they must be very clear about exactly what that condition means.

The other type of security-relevant exception is in code that is not part of a security control. 
These exceptions are security-relevant if they affect whether the application properly invokes the control. 

An exception might cause a security method not to be invoked when it should, or it might affect the initialization of variables used in the security control.


## Examples

### isAdmin

    isAdmin = true; 
    try { 
      codeWhichMayFail(); 
      isAdmin = isUserInRole( “Administrator” ); 
    }
    catch (Exception ex)
    {
      log.write(ex.toString()); 
    } 

If codeWhichMayFail() fails, the user is an admin by default. This is
obviously a security risk. The fix is simple, in this case. It involves
a simple reversing of the logic. In the example instance, this is very
easy to do.

    isAdmin = false;
    try {
      codeWhichMayFail();
      isAdmin = isUserInrole( "Administrator" );
    }
    catch (Exception ex)
    {
      log.write(ex.toString());
    }

This example is also an example of the [Least privilege](vulnerabilities/Least_Privilege_Violation) principle, which states you should never grant more access than required. 
If `codeWhichmayFail()` requires admin access, we should be verifying that admin access before we run that code.

## References

  - [US Cert - Failing Securely](https://buildsecurityin.us-cert.gov/articles/knowledge/principles/failing-securely)
