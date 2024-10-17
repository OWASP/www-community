---

layout: col-sidebar
title: "Prologue - Preparation"
author: "Raphael Moreira"
contributors: 
permalink: /initiatives/isc_handler_roadmap/acts
tags: ["cybersecurity", "kali", "linux", "environment", "virtualization"]

---

{% include writers.html %}

🇺🇸 | [🇧🇷](prologue.pt-BR.md)

# Prologue - Preparation
Aiming for objectivity and security in the learning process, the following steps will guide you in creating a [🔍virtualized Linux environment](https://www.redhat.com/en/topics/virtualization/what-is-virtualization). 
For reference, we will be using **Microsoft Windows 10 Pro**, version **22H2**, build **19045.4123**. The suggested 
distribution is [🔍Kali Linux](https://www.kali.org/).

>**Disclaimer:** the OWASP does not endorse any vendor or tool by mentioning it. If it is cited, it is because we believe 
> it is available for free use in open-source projects. Feel free to use the tool that best suits your needs.

## Kali Linux
The [🔍Kali distribution](https://www.kali.org/features/) is dedicated to cybersecurity, providing a set of tools ideal 
for the task. If you're more comfortable with another distribution, there's no need to switch to Kali, as throughout the acts, 
there will be guidance on each tool and how to obtain it. On the official Kali site, you'll find various [platforms](https://www.kali.org/get-kali/#kali-platforms) 
available for use. However, for our initiative, we will be using [VMware](https://cdimage.kali.org/kali-2024.1/kali-linux-2024.1-vmware-amd64.7z). 
If you’re not comfortable with this virtualization tool, the site also offers [other options](https://www.kali.org/get-kali/#kali-virtual-machines).

>**WARNING:** make sure your operating system has [🔍Hyper-V](https://learn.microsoft.com/en-us/virtualization/hyper-v-on-windows/about/) 
> enabled; otherwise, you will encounter issues with virtualization.

## Recommendations
Once your environment is functional, meaning it is virtualized and running, remember that everything we will demonstrate 
throughout this initiative requires elevated privileges (administrative access). However, it is highly recommended that 
you do not use the **root** user. Try to create another user and mark it as **Administrator**. Although it may seem the same, 
it is not. The **root** user has privileges that can put you at risk if used improperly.

In the case of virtualization, ensure that encryption for this image is enabled. Even if you are at the initial stage of 
learning, try to internalize the culture of protecting the environment you work in, thus ensuring the privacy of your work.

---

| [⬆️Return to index](../index.md) | [Go to Act 1](act_1.md)➡️ |
|----------------------------------|---------------------------|

