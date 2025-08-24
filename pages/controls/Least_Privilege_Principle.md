---

title: Least Access Principle
layout: col-sidebar
author: Shezan Rohinton Mirzan
tags: controls, access control
permalink: /controls/Least_Access_Principle

---

{% include writers.html %}

## Description
The principle of **Least Privilege** is a fundamental concept in information security. It dictates that a user, process, or program should be given only the minimum level of access or permissions necessary to perform its intended function, and nothing more. This principle helps to reduce the potential for damage from system compromises, whether due to human error, malicious activity, or software vulnerabilities.

## Why is Least Privilege Necessary
The primary goal of PoLP is to reduce the "attack surface" and limit the "blast radius" of a security breach.

- **Minimizing the Attack Surface**: The attack surface is the sum of all possible entry points an unauthorized user could use to gain access to a system. By granting minimal permissions, you reduce the number of avenues an attacker can exploit.
  
> Example: A web server running with root (administrator) privileges can modify, delete, or access any file on the entire system if compromised. However, if the server is configured to run with a low-privilege user account that can only read from the web directory, a successful attack would be contained, preventing the attacker from causing widespread damage to the operating system or other applications.

- **Limiting the Blast Radius**: The blast radius is the extent of damage an attacker can inflict if they successfully compromise a part of the system. PoLP ensures that even if a part of your system is breached, the attacker can't move laterally or escalate privileges to access critical data or systems.
  
> Example: Imagine an employee whose laptop is compromised by a phishing attack. If they have standard user access to the company network, the attacker can only access the files and systems that employee is authorized to use. However, if the employee has administrative privileges across the network, the attacker could potentially access sensitive information, deploy malware to other computers, and shut down critical services, causing catastrophic damage.
    
## Applicable Systems
- **Operating Systems**: Operating systems use a user-based permission model. In other words, when the user installs any application, it should not require administrator access unless it genuinely needs to modify system files. Granting an application like a web browser or a text editor unnecessary admin rights is a security risk.
- **Databases**: Database administrators often have full control over the data. However, an application connecting to the database should have a separate user account with limited privileges.
  
    > Example: A product catalog application for an e-commerce site only needs to read product descriptions and prices. It should be given read-only access to the product table. It should not have permission to delete customer records or modify sensitive financial data
- **Cloud Computing**: Strict Identity and Access Management (IAM) roles should be applied to all systems and users. They should only be granted privileges that are required for them to get the work done.
  
> Example: You can create a service account for a function that resizes images uploaded to a cloud storage bucket. This service account should have a policy that grants it only permission to read from the 'uploads' bucket and write to the 'resized_images' bucket. It should not have permissions to delete the entire bucket or access other critical cloud resources.

- **Software Engineering**: : When designing applications, developers should build with this principle in mind. Services should be broken down into smaller, microservices, each with its own set of minimal permissions.

    > Example: An online payment system can be separated into three microservices: one for handling credit card transactions, one for sending confirmation emails, and one for updating the order status in a database. Each of these services should run with unique credentials and only the permissions needed for its specific task. The email service, for instance, doesn't need to access the database or credit card information.

## Relationship with Other Security Models

Least Privilege Principle is often considered a building block for more comprehensive security frameworks, particularly **Zero Trust**. In a Zero Trust model, you "_never trust, always verify_." Every user, device, and service is treated as potentially malicious, regardless of its location (inside or outside the corporate network). Least privilege is the mechanism through which you enforce this verification. After a user is authenticated and authorized, their access is still limited to the minimum required, adhering to the principle of least privilege.

## Additional Reads
- [OWASP Attack Surface Analysis](https://cheatsheetseries.owasp.org/cheatsheets/Attack_Surface_Analysis_Cheat_Sheet.html)
- [OWASP Zero Trust Cheat Sheet](https://cheatsheetseries.owasp.org/cheatsheets/Zero_Trust_Architecture_Cheat_Sheet.html)

