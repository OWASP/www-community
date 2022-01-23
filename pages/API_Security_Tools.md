---

title: API Security Tools
layout: col-sidebar
author: Matt Tesauro
contributors:
tags: api, tools, oss
permalink: /API_Security_Tools

---

APIs are becoming an increasingly large portion of the software that powers the Internet including mobile applications, single-page applications (SPAs) and cloud infrastructure. While APIs share much of the same security controls and software security issues with traditional web applications, they are different enough to make a distinction between 'normal' AppSec tools and ones that were built with APIs in mind.  This page was created to list tools known to support APIs natively and by design.

### Types of API tools

* API Security Posture: Creates an inventory of APIs, the methods exposed and classifies the data used by each method.
  * Goal: Provide visibility into the security state of a collection of APIs.
* API Runtime Security: provides protection to APIs during their normal running and handling of API requests.
  * Goal: Detect and prevent malicious requests to an API.
* API Security Testing
  * Goal: Evaluate the security of a running API by interacting with the API dynamically (DAST-like behavior)

The goal is to provide as comprehensive a list of API tools as possible using the input of the diverse perspectives of the OWASP community.

## Tools Listing

| Name                                             | Licence                                                                | Platforms      | Posture                                                            | Runtime                                                            | Testing                                                                |
| ----                                             | ----                                                                   | ----           | ----                                                               | ----                                                               | ----                                                                   |
| [Noname API Security Platform] (Noname Security) | ![License](https://img.shields.io/badge/License-commercial-9cf.svg)    | SaaS, OnPrem   | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg)     |
| [OWASP Zap]                                      | ![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg) | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) [1] |

[Noname API Security Platform]: https://nonamesecurity.com/platform
[OWASP Zap]: https://www.zaproxy.org/
### Footnotes

[1] See https://www.zaproxy.org/faq/how-can-you-use-zap-to-scan-apis/

### Table Columns

* Name: The name of the API tool and owner of the tool (as appropriate)
* License: The license for the tool e.g. Commercial or a FLOSS license
* Platforms: The platform on which the tool runs
* Posture: The tool support API Security Posture
* Runtime: The tool supports API Runtime Security
* Testing: The tool supports API Security Testing

