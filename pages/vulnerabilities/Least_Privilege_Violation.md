---

layout: col-sidebar
title: Least Privilege Violation
author: 
contributors: 
permalink: /vulnerabilities/Least_Privilege_Violation
tags: vulnerability, Least Privilege Violation

---

{% include writers.html %}

## Description

The elevated privilege level required to perform operations such as `chroot()` should be dropped immediately after the operation is performed.

When a program calls a privileged function, such as `chroot()`, it must first acquire root privilege. As soon as the privileged operation has completed, the program should drop root privilege and return to the privilege level of the invoking user.

## Risk Factors

TBD

## Examples

The following code calls `chroot()` to restrict the application to a subset of the filesystem below APP_HOME in order to prevent an attacker from using the program to gain unauthorized access to files located elsewhere. The code then opens a file specified by the user and processes the contents of the file.

```
...
chroot(APP_HOME);
chdir("/");

FILE* data = fopen(argv[1], "r+");
...
```

Constraining the process inside the application's home directory before opening any files is a valuable security measure. However, the absence of a call to `setuid()` with some non-zero value means the application is continuing to operate with unnecessary root privileges. Any successful exploit carried out by an attacker against the application can now result in a privilege escalation attack because any malicious operations will be performed with the privileges of the superuser. If the application drops to the privilege level of a non-root user, the potential for damage is substantially reduced.

### J2EE Misconfiguration: Weak Access Permissions

Permission to invoke EJB methods should not be granted to the ANYONE role.

If the EJB deployment descriptor contains one or more method permissions that grant access to the special ANYONE role, it indicates that access control for the application has not been fully thought through or that the application is structured in such a way that reasonable access control restrictions are impossible.

The following deployment descriptor grants ANYONE permission to invoke the Employee EJB's method named `getSalary()`.

```
<ejb-jar>
    ...
    <assembly-descriptor>
        <method-permission>
            <role-name>ANYONE</role-name>
            <method>
                <ejb-name>Employee</ejb-name>
                <method-name>getSalary</method-name>
        </method-permission>
    </assembly-descriptor>
    ...
</ejb-jar>
```

## Related [Attacks](../attacks/)


## Related [Vulnerabilities](../vulnerabilities/)

- [Broken Access Control](../Broken_Access_Control)

## Related [Controls](https://owasp.org/www-community/controls/)

- [Access Control](../Access_Control)

## References
