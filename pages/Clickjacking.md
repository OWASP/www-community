---
layout: col-sidebar
title: "Clickjacking"
author: "Aishwarya"
contributors: ["Aishwarya011k"]
permalink: /Clickjacking
tags: ["attack", "clickjacking", "web security"]
---

{% include writers.html %}

## What is Clickjacking?

Clickjacking is a sneaky kind of web attack where a user ends up clicking on something different than what they see on the screen. It’s often used to trick people into doing things they didn’t intend to — like changing settings, liking something on social media, or even authorizing transactions.

The basic idea is that an attacker hides a legitimate webpage (like your bank or email) inside a transparent frame and overlays it with fake content. You think you’re clicking a harmless button, but behind the scenes, you're actually interacting with the hidden page.

---

## How the Attack Works

Here’s a simple example:

1. An attacker creates a webpage with a flashy “Click here to win!” button.
2. Underneath that button, they load your bank’s transfer form inside an invisible iframe.
3. When you click the visible button, your browser actually registers the click on the hidden bank form — maybe transferring money without you realizing it.

It’s not just theory — real-world attacks like this have been used to get people to like pages, follow accounts, or even change device settings.

---

## How to Protect Your Website

Fortunately, there are a few solid ways to protect against clickjacking:

### 🛡️ 1. Use `X-Frame-Options` Header

This HTTP response header tells browsers not to load your site inside a frame. Use either:

