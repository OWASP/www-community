---

layout: col-sidebar
title: Google Season of Docs 2019
tags: gsod, Google Season of Docs, 2019
permalink: /initiatives/gsod/historical/2019_ideas/

---

## Overview
OWASP is going to apply to participate in the inaugural Google Season of Docs

The organization application is in and we are awaiting notification of acceptance into the program.

If you plan to be a mentor for 2019, please [Register Here](https://docs.google.com/forms/d/e/1FAIpQLSe-JjGvaKKGWZOXxrorONhB8qN3mjPrB9ZVkcsntR73Cv_K7g/viewform)

Tips to get you started in no particular order:

* Read [Google Season of Docs Project Ideas](https://developers.google.com/season-of-docs/docs/project-ideas)
* Read [Program Rules](https://developers.google.com/season-of-docs/terms/program-rules)

---
### OWASP ZAP
OWASP Zed Attack Proxy Project (ZAP) one of the world’s most popular free security tools and is actively maintained by hundreds of international volunteers. Previous GSoC students have implemented key parts of the ZAP core functionality and have been offered (and accepted) jobs based on their work on ZAP.

#### The API
ZAP has an extremely powerful API that allows you to do nearly everything that possible via the desktop interface. It is considered on of ZAPs strengths and is heavily used for automation. Unfortunately is also not particularly well documented and we get many queries about it on the support groups.

Existing documentation includes:

[https://github.com/zaproxy/zaproxy/wiki/ApiDetails](https://github.com/zaproxy/zaproxy/wiki/ApiDetails)
[https://github.com/zaproxy/zaproxy/wiki/ApiGen_Index](https://github.com/zaproxy/zaproxy/wiki/ApiGen_Index)

This project would:

Explain the concepts behind the UI
Explain how it can be used at a high level
Detail all of the API calls
The documentation should be suitable for publishing as web pages and for printing on paper.

#### Zest
Zest is an experimental specialized scripting language developed by the ZAP team and is intended to be used in web oriented security tools. While it is tool independent it is heavily used by ZAP.

Existing documentation includes:

[https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Zest](https://developer.mozilla.org/en-US/docs/Mozilla/Projects/Zest)
[https://github.com/mozilla/zest/wiki](https://github.com/mozilla/zest/wiki)

This project would:

Explain the concepts behind the Zest
Explain how to write Zest scripts
Document the ZAP Desktop UI provided relating to Zest
The documentation should be suitable for publishing as web pages and ideally the parts relating to the ZAP Desktop UI should be able to be included within the UI as context sensitive help.

---
### OWASP Juice Shop

OWASP Juice Shop Project is probably the most modern and sophisticated insecure web application! It can be used in security trainings, awareness demos, CTFs and as a guinea pig for security tools! Juice Shop encompasses vulnerabilities from the entire OWASP Top Ten along with many other security flaws found in real-world applications!

#### "Pwning OWASP Juice Shop" Companion Guide
Pwning OWASP Juice Shop is the official companion guide for this project. It will give you a complete overview of the vulnerabilities found in the application including hints how to spot and exploit them. In the appendix you will even find complete step-by-step solutions to every challenge. The ebook is published under CC BY-NC-ND 4.0 and is available for free as work-in-progress in HTML, PDF, Kindle and ePub format on GitBook. The latest officially released edition is available for free on LeanPub in PDF, Kindle and ePub format.

![OWASP JuiceShop Cover](/www-community/assets/images/initiatives/gsod/owaspjuiceshop_cover.jpg)

The book is divided into three parts:

* Part I - Hacking preparations (helps you to get the application running and to set up optional hacking tools)
* Part II - Challenge hunting (gives an overview of the vulnerabilities found in the OWASP Juice Shop including hints how to find and exploit them in the application)
* Part III - Getting involved (shows up various ways to contribute to the OWASP Juice Shop open source project)

Primary focus points of this project could be:

Migrate the eBook from (legacy) GitBook format to either latest GitBook or another suitable format (Mandatory requirement is the ability to generate PDF/ePub/Mobi versions of the book for LeanPub and to be able to host it in HTML online-readable form)
Tackle the idea to generate a special "CTF Edition" of the book from the same source content
This project could additionally:

Add hints and solutions for currently undocumented challenges (marked with :wrench: **TODO**)
Extend the "Codebase 101" chapter with more details and examples for new contributors
Review, curate and extend the other existing content

---
### OWASP-SecureTea Tools Project
The OWASP SecureTea Project is an application designed to help secure a person's laptop or computer / server with IoT (Internet Of Things) and notify users (via various communication mechanisms), whenever someone accesses their computer / server. This application uses the touchpad/mouse/wireless mouse to determine activity and is developed in Python and tested on various machines (Linux, Mac & Windows). The software is still under development, and will eventually have it's own IDS(Intrusion Detection System) / IPS(Instrusion Prevention System), firewall, anti-virus, intelligent log monitoring capabilities with web defacement detection, and support for much more communication medium. . - [https://github.com/OWASP/SecureTea-Project/blob/master/README.md](https://github.com/OWASP/SecureTea-Project/blob/master/README.md)

This project would:
1. Review, curate and extend the other existing content of User Guide and Developer Guide
2. Help to translate into many languages as you can do (Example : Japanese Translate)
3. As Content Writer we need your best ideas for improve The SecureTea Project Documentation.
4. Help Our Programmer/Contributors to create their Documentation such as Website content,wiki,user docs and developer docs, etc which not yet publish/completed.
5. Camera, action . we actually not bollywood or hollywood but we want create video related our project [https://www.youtube.com/channel/UCGdl9tpc1qZYcM3WRRFRPPA](https://www.youtube.com/channel/UCGdl9tpc1qZYcM3WRRFRPPA)

---
### OWASP DefectDojo
OWASP DefectDojo is a popular open source vulnerability management tool and is used as the backbone for security programs. It is easy to get started with to work on! We welcome volunteers of all experience levels and are happy to provide mentoring.

The existing documentation is on Read the Docs and is created based on the DefectDojo documentation repo.

The project would:

* Review and update the current documentation based on the latest release in the master branch
* Update and expand documentation sections including
* Installation including the new Docker Compose and Kubernetes
* Liberal inclusion of screenshots or screencasts for various features of the web UI
* Integrations with various security tools
* workflows and other real-world use cases that DefectDojo solves
* Validate the documentation against the Python3 branch which will be the bases for the next major release of DefectDojo
* Translating the current documentation to languages other than English

---
### OWASP Risk Assessment Framework
OWASP Risk Asessement Framework is SAST tools,web deface detection, Risk Assessment Tool
we participated of gsoc 2019 so we need some technical writer for docs

1. research and write references for sast tool which have api
2. make some docs of wiki
3. make video also related content of risk assessment