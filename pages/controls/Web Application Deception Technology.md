---

layout: col-sidebar
title: Web Application Deception Technology
author: Vaibhav Malik
tags: [controls, application, web]
permalink: /controls/WebAppDeception

---

 {% include writers.html %}


## Description

Deception technology, similar to honeypot, is an approach to cybersecurity that involves distributing decoy systems, credentials, and data throughout an environment to deceive, detect, and disrupt attackers. Rather than simply blocking all malicious activity, deception techniques aim to mislead attackers and waste their time while providing high-fidelity alerts of their presence.

For web application security, deception can take several forms:

1. Honeytoken Cookies - Fake session cookies containing enticing names (e.g., "admin_session"), but invalid values are seeded into the application. Any attempts to use these cookies indicate an attacker is stealing and replaying cookies.
2. Honeytoken Form Fields — In addition to hidden form fields, honeytokens can be placed in visible fields that normal users should never use. For example, an "admin_override" field that regular users have no reason to interact with. Any submissions with that field populated indicate an attacker probing the application.
3. Honeytoken API Keys - Fake API keys or access tokens can be seeded in an application's JavaScript or HTML source. Attackers who scrape the client-side code looking for sensitive tokens to steal will pick up these fake tokens. Any use of these honeytoken API keys indicates malicious recon activity.
4. Deceptive Links/URLs - Hidden links and API endpoints are placed in the application's client-side code. Regular users never see these links, so any requests to them suggest an attacker is inspecting the source code for vulnerabilities.  
5. Booby-trapped Form Fields - Invisible form fields are added to lure attackers. These fields are not rendered for real users, so any data submitted in them points to malicious form tampering.
6. Canary Files/Records - Fake sensitive files (e.g., "salaries.xlsx") or database records are planted in the application. Access to these dummy assets indicates an attacker has broken in and is snooping around.
7. Tarpit Pages - Requests for certain pages (e.g., WordPress's wp-admin for a non-WordPress site) are redirected to an infinite loop or a resource-intensive puzzle. This slows down attackers, especially scanners and crawlers.

Deception technology provides several advantages for web application defenders:
High signal-to-noise Ratio — Alerts from deception systems are highly confident since legitimate users rarely trigger them. This reduces alert fatigue for security teams.
Early detection - Deceptions can catch attackers early in the reconnaissance and lateral movement stages before they cause damage.
Attribution - Analyzing how attackers interact with deceptions can reveal their intent, tools, and techniques.
Threat intelligence - Collecting data on attacker behavior can generate indicators of compromise (IOCs) and threat intelligence to strengthen other defenses.

However, deception technology also has some challenges and considerations:
Maintenance - Deceptions must be kept fresh and believable. Attackers may grow suspicious if they repeatedly encounter stale or unconvincing decoys.  
Interference - Deceptions should not interfere with normal application functionality or confuse legitimate users.
Legal issues - Consult with legal counsel on entrapment and privacy laws before implementing deceptions, especially in public-facing systems.

## Sample Code

Below is a Python snippet using the Flask web framework to create a web application honeypot with a deceptive link:

```python
from flask import Flask, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    # Render a normal page, but include a hidden link in the HTML
    return '''
    <html>
        <head><title>Welcome</title></head>
        <body>
            <h1>Welcome to my web app!</h1>
            <a href="/admin" style="display:none">Admin Panel</a>
        </body>
    </html>
    '''

@app.route('/admin')
def admin():
    # An attacker found the hidden link! Log the event and redirect them to a fake admin page
    log_event(f"Potential attacker from IP {request.remote_addr} accessed /admin URL")
    return redirect("http://decoy.example.com/admin", code=302)

def log_event(message):
    # Log the attack details to a file or SIEM
    with open('attacks.log', 'a') as f:
        f.write(f"{message}\n")
```

This code creates a web page with a hidden `/admin` link. Normal users won't see or click this link. However, an attacker inspecting the source code may find it enticing and attempt to access it. The `/admin` route handler logs this event and redirects the attacker to a decoy site, wasting their time and providing deception-based detection.

To make the deception more sophisticated, the decoy site could mimic an admin panel and induce the attacker to enter credentials, revealing their methods and tooling.

In conclusion, deception technology is a proactive defense strategy that can complement traditional web application security controls. Laying traps and misdirecting attackers provide high-confidence detections and valuable threat intelligence. Modern web application security programs should consider incorporating deception alongside techniques like input validation, strong authentication, and regular patching.
