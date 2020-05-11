---

layout: col-sidebar
title: OWASP Bug Bounty
tags: bugbounty
permalink: /initiatives/bugbounty/

---

OWASP Bug Bounty programs are run different from most traditional Bug Bounties. First of all, the applications to be tested are not available as deployed web applications online. For this part you will need to download the applications and deploy or install them on your computer. The following is a guideline for each bug bounty program we are running:

# OWASP ZAP Bug Bounty
The OWASP ZAP Bug Bounty program can be found [here](https://bugcrowd.com/owaspzap).

OWASP ZAP is a client application written in JAVA. Therefore is important that you keep in mind the scope of the bounty.
[Download](https://www.zaproxy.org/download/) the latest version and install it on your computer.

## Bug Bounty Tips

### Check the Code
OWASP ZAP is an open source application, meaning that you have access to the source code and you can debug it while testing it. This offers you a much better view of what is happening, but also, you have the ability to white-test the application and find out vulnerable Java Methods faster than the Blackbox approach.

You will need to run ZAP within a Java IDE like Eclipse. The easiest way to get ZAP running this way is to follow these instructions [here](https://github.com/zaproxy/zaproxy/wiki/Building) or follow these videos:

- [OWASP ZAP for Developers - Building ZAP -Part 1](https://www.youtube.com/watch?v=1UsH1jSnE3c)
- [OWASP ZAP for Developers - Building ZAP -Part 2](https://www.youtube.com/watch?v=qhm1g1klyas)
- [OWASP ZAP for Developers - Building ZAP -Part 3](https://www.youtube.com/watch?v=xevZ7n7ETMI)
- [OWASP ZAP for Developers - Build ZAP from Eclipse - Part 4](https://www.youtube.com/watch?v=n9mQASWRcps)

You can also use STATS analysis tools that might unmask vulnerable methods.

OWASP Source code can be found [here](https://github.com/zaproxy/zaproxy/).

### Scope

Any design or implementation issue that is reproducible and substantially affects the security of ZAP users is likely to be in scope for the program, but in particular:

- Remote code execution
- Unauthorized API actions

# OWASP CRSFGuard Bug Bounty
OWASP CRSFGuard Bug Bounty program can be found [here](https://bugcrowd.com/owaspcrsfguard).

Please read careful the scope of the bounty and make sure you understand the target.

For the purpose of this bounty , the library has been deployed within a Dummy Java application of just consisting a web form. You can download the entire app source code file [here](https://github.com/OWASP/OWASPBugBounty/blob/master/CRSFGuard/bountyguard.zip).

You can open the Maven project in [Eclipse IDE for Java Developers](https://www.eclipse.org/downloads/packages/eclipse-ide-java-developers/lunasr2). If you are not familiar opening Maven projects in Eclipse IDE , check the following video:

- [Import OWASP CRSFGuard Bounty File into Eclipse](https://www.youtube.com/watch?v=xWXPJexUPHg)

# OWASP JAVA HTML Sanitizer Bug Bounty
This bounty program is to be found [here](https://bugcrowd.com/owaspjavasanitizer)

Please make sure your read carefully the scope of the bounty clear.

## How to Deploy

OWASP Java HTML Sanitize is actually a Java library. For the purpose of this bounty, the library has been deployed within a dummy Java application of just consisting a web form. You can download the [WAR file here](https://github.com/OWASP/OWASPBugBounty/tree/master/JavaHTMLSanitizer/war-files).

If you have no experience deploying a war file as an application, you can decide to run it within a IDE like Eclipse or deployed it into an Apache Server. Follow the following videos if you need more information regarding this:

- [01 - Importing a WAR file and running java project using eclipse IDE](https://www.youtube.com/watch?v=GBKzjMwQMoQ)
- [Install and Configure Apache Tomcat Web Server in Eclipse IDE](https://www.youtube.com/watch?v=kLgquZ2FiuQ)
- [Tomcat - war file deployment [Manager Application]](https://www.youtube.com/watch?v=9X9DA8oVodk)

# Questions

If you have more questions regarding the program or how to join it please contact: [support@bugcrowd.com](mailto:support@bugcrowd.com).
