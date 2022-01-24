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

| Name                                               | Licence                                                                               | Platforms      | Posture                                                            | Runtime                                                            | Testing                                                            |
| ----                                               | ----                                                                                  | ----           | ----                                                               | ----                                                               | ----                                                               |
| [APIsec]</br>APIsec                                | ![License](https://img.shields.io/badge/License-Commercial-9cf.svg)                   | SaaS           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Astra]</br>flipkart-incubator                     | ![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)                | Linux/Mac OS   | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Automatic API Attack Tool]</br>Imperva            | ![License](https://img.shields.io/badge/license-MIT-4EB1BA.svg)                       | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [ffuf] [1]</br>ffuf                                | ![License](https://img.shields.io/badge/license-MIT-4EB1BA.svg)                       | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [http-tanker] [2]</br>PierreKieffer                | ![License](https://img.shields.io/badge/license-BSD--2--Clause-4EB1BA.svg)            | Linux/Mac OS   | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Noname API Security Platform]</br>Noname Security | ![License](https://img.shields.io/badge/License-Commercial-9cf.svg)                   | SaaS, OnPrem   | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Nuclei] [3]</br>ProjectDiscovery                  | ![License](https://img.shields.io/badge/license-MIT-4EB1BA.svg)                       | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Wfuzz] [4]</br>xmendez                            | ![License](https://img.shields.io/badge/license-GPL--2.0-4EB1BA.svg)                  | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |
| [Zed Attack Proxy (Zap)] [5]</br>OWASP             | ![License](https://img.shields.io/badge/license-Apache%202-4EB1BA.svg)                | Cross Platform | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![No](https://img.shields.io/badge/Supported-No-red.svg)           | ![Yes](https://img.shields.io/badge/Supported-Yes-brightgreen.svg) |


[APIsec]: https://www.apisec.ai/
[Astra]: https://github.com/flipkart-incubator/Astra
[Automatic API Attack Tool]: https://github.com/imperva/automatic-api-attack-tool
[ffuf]: https://github.com/ffuf/ffuf
[http-tanker]: https://github.com/PierreKieffer/http-tanker
[Noname API Security Platform]: https://nonamesecurity.com/platform
[Nuclei]: https://github.com/projectdiscovery/nuclei
[Wfuzz]: https://github.com/xmendez/wfuzz
[Zed Attack Proxy (ZAP)]: https://www.zaproxy.org/

### Footnotes

1. General http/web fuzzer which can also fuzz http-based APIs
2. Very manual terminal program e.g. Postman in your terminal
3. General scanning of TCP, DNS, HTTP, etc so can be used to test APIs
4. General http/web fuzzer which can also fuzz http-based APIs
5. See https://www.zaproxy.org/faq/how-can-you-use-zap-to-scan-apis/

### Table Columns

* Name: The name of the API tool and owner of the tool (as appropriate)
* License: The license for the tool e.g. Commercial or a FLOSS license
* Platforms: The platform on which the tool runs
* Posture: The tool support API Security Posture
* Runtime: The tool supports API Runtime Security
* Testing: The tool supports API Security Testing

