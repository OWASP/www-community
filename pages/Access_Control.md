---

layout: col-sidebar
title: Access Control
author:
contributors:
tags: Access Control
permalink: /Access_Control

---

{% include writers.html %}

## Overview

Access Control, also known as Authorization — is mediating access to
resources on the basis of identity and is generally policy-driven
(although the policy may be implicit). It is the primary security
service that concerns most software, with most of the other security
services supporting it. For example, access control decisions are
generally enforced on the basis of a user-specific policy, and
authentication is the way to establish the user in question. Similarly,
confidentiality is really a manifestation of access control,
specifically the ability to read data. Since, in computer security,
confidentiality is often synonymous with encryption, it becomes a
technique for enforcing an access-control policy.

Policies that are to be enforced by an access-control mechanism
generally operate on sets of resources; the policy may differ for
individual actions that may be performed on those resources
(capabilities). For example, common capabilities for a file on a file
system are: read, write, execute, create, and delete. However, there are
other operations that could be considered “meta-operations” that are
often overlooked — particularly reading and writing file attributes,
setting file ownership, and establishing access control policy to any of
these operations.

Often, resources are overlooked when implementing access control
systems. For example, buffer overflows are a failure in enforcing
write-access on specific areas of memory. Often, a buffer overflow
exploit also accesses the CPU in a manner that is implicitly
unauthorized as well.

## Definition

Access control and Authorization mean the same thing. Access control
governs decisions and processes of determining, documenting and managing
the subjects (users, devices or processes) that should be granted access
and the objects to which they should be granted access; essentially,
what is allowed. Access controls also govern the methods and conditions
of enforcement by which subjects (users, devices or processes) are
allowed to or restricted from connecting with, viewing, consuming,
entering into or making use of identified information resources
(objects).

## Principle of Least Privilege

In security, the Principle of Least Privilege encourages system
designers and implementers to allow running code only the permissions
needed to complete the required tasks and no more. When designing web
applications, the capabilities attached to running code should be
limited in this manner. This spans the configuration of the web and
application servers through the business capabilities of business logic
components.

Far too often, web and application servers run at too great a permission
level. They execute using privileged accounts such as root in UNIX
environment or LOCALSYSTEM in Windows environments. When web and
application servers run as root or LOCALSYSTEM, the processes and the
code on top of these processes run with all of the rights of these
users. Malicious code will execute with the authority of the privileged
account, thus increasing the possible damage from an exploit. Web and
application servers should be executed under accounts with minimal
permissions.

The database accounts used by web applications often have privileges
beyond those actually required or advisable. Allowing web applications
to use sa or other privileged database accounts destroys the database
server’s ability to defend against access to or modification of
unauthorized resources. Accounts with db_owner equivalent privileges
such as schema modification or unlimited data access typically have far
more access to the database than is required to implement application
functionality. Web applications should use one or more lesser-privileged
accounts that are prevented from making schema changes or sweeping
changes to or requests for data.

The J2EE and .NET platforms provide developers the ability to limit the
capabilities of code running inside of their virtual machines. Often web
applications run in environments with AllPermission (Java) or FullTrust
(.NET) turned on. This limits the ability of the virtual machine to
control the actions of code running under its control. Implementing code
access security measures is not only useful for mitigating risk when
running untrusted code – it can also be used to limit the damage caused
by compromises to otherwise trusted code.

Finally, the business logic of web applications must be written with
authorization controls in mind. Once a user has authenticated to the
running system, their access to resources should be limited based on
their identity and roles. In addition, users’ attempts to perform
actions should also be authorized. Both the J2EE and ASP.NET web
application platforms provide the ability to declaratively limit a
user’s access to web resources by their identity and roles (as
configured in web.xml and web.config respectively). The J2EE platform
provides controls down to the method-level for limiting user access to
the capabilities of EJB components. By designing file resource layouts
and components APIs with authorization in mind, these powerful
capabilities of the J2EE and .NET platforms can be used to enhance
security.

## Centralized Authorization Routines

A common mistake is to perform an authorization check by cutting and
pasting an authorization code snippet into every page containing
sensitive information. Worse yet would be re-writing this code for every
page. Well written applications centralize access control routines, so
if any bugs are found, they can be fixed once and the results apply
throughout the application immediately.

## Controlling Access to Protected Resources

Some applications check to see if a user is able to undertake a
particular action, but then do not check if access to all resources
required to complete the requested action is allowed. For example, forum
software may check to see if a user is allowed to reply to a previous
message, but then fails to check that the requested message is not
within a protected or hidden forum or thread. Another example would be
an Internet Banking application that checks to see if a user is allowed
to transfer money, but does not validate that the “from account” is one
of the user’s accounts.

## Some Generic Types of Access Controls:

When thinking of access control, you might first think of the ability to
login to a system or access files or a database. Access can be
controlled, however, at various levels and with respect to a wide range
of subjects and objects. Some examples include:

- Network access - the ability to connect to a system or service;
- At the host - access to operating system functionality;
- Physical access - at locations housing information assets or
    physical access to the assets themselves;
- Restricted functions - operations evaluated as having an elevated
    risk, such as financial transactions, changes to system
    configuration, or security administration.

Resource access may refer not only to files and database functionality,
but to:

- applications or APIs;
- specific application screens or functions;
- specific data fields;
- memory;
- private or protected variables;
- storage media;
- transmission media;
- In short, any object used in processing, storage or transmission of
    information.

## Access Control Models:

**Discretionary access controls** are based on the identity and
need-to-know of subjects and/or the groups to which they belong. They
are discretionary in the sense that a subject with certain access
permissions is capable of passing on that access, directly or
indirectly, to other subjects.

**Mandatory access controls** are based on the sensitivity of the
information contained in the objects / resources and a formal
authorization. They are mandatory in the sense that they restrain
subjects from setting security attributes on an object and from passing
on their access.

From the perspective of end-users of a system, access control should be
mandatory whenever possible, as opposed to discretionary. Mandatory
access control means that the system establishes and enforces a policy
for user data, and the user does not get to make their own decisions of
who else in the system can access data. In discretionary access control,
the user can make such decisions. Enforcing a conservative mandatory
access control policy can help prevent operational security errors,
where the end user does not understand the implications of granting
particular privileges. It usually keeps the system simpler as well.

Mandatory access control is also worth considering at the OS level,
where the OS labels data going into an application and enforces an
externally defined access control policy whenever the application
attempts to access system resources. While such technologies are only
applicable in a few environments, they are particularly useful as a
compartmentalization mechanism, since — if a particular application gets
compromised — a good MAC system will prevent it from doing much damage
to other applications running on the same machine.

**Role-based access controls (RBAC)** are based on the roles played by
users and groups in organizational functions. Roles, alternatively
referred to as security groups, include collections of subjects that all
share common needs for access. Authorization for access is then provided
to the role or group and inherited by members.

**Attribute-based access control (ABAC)** is a newer paradigm based on
properties of an information exchange that may include identified
attributes of the requesting entity, the resource requested, or the
context of the exchange or the requested action. Some examples of
contextual attributes are things such as:

- time of day;
- location;
- currently evaluated threat level;
- required hygiene measures implemented on the respective hosts.

In general, in ABAC, a rules engine evaluates the identified attributes
to issue an authorization decision.

## Examples of Access Controls in Software:

- Account management;
- Mapping of user rights to business and process requirements;
- Mechanisms that enforce policies over information flow;
- Limits on the number of concurrent sessions;
- Session lock after a period of inactivity;
- Session termination after a period of inactivity, total time of use
    or time of day;
- Limitations on the number of records returned from a query (data
    mining);
- Features enforcing policies over segregation of duties;
- Segregation and management of privileged user accounts;
- Implementation of the principle of least privilege for granting
    access;
- Requiring VPN (virtual private network) for access;
- Dynamic reconfiguration of user interfaces based on authorization;
- Restriction of access after a certain time of day.

## Related resources:

1.  OWASP [Access Control Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Access_Control_Cheat_Sheet.html)
