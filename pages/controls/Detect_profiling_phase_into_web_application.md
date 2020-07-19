---

title: Detect Profiling Phase
layout: col-sidebar
author: Dominique RIGHETTO
contributors: Imifos, kingthorin
tags: controls
permalink: /controls/Detect_profiling_phase_into_web_application

---

{% include writers.html %}

Last revision (mm/dd/yyyy): **01/06/2014**

## Remark

The ideas proposed into this page can seems to be uncommon, aggressive
or a little bit crazy in corporate environment (like a web banking) but
the initial page author is personally convinced that if we can detect a
profiling phase and send sign, to the originator, indicating clearly to
them that "*we know what is currently doing*" we must be able to stop
attack before that it can cause damage.

## Introduction

Into the context of the web application, defensive security is applied
in order to avoid attacks to be successful. This page proposes some
ideas in order to be more "proactive" by trying to detect attacks
preparation and take measures against the attacker before that any
attack be launched.

This page is provided with Java projects in which examples of
implementation described into this page are showed:

- [Profiling detection filters](https://code.google.com/p/righettod/source/browse/#git%2FJEE%2FProfilingDetectionPOC)
- [Attacker identification](https://code.google.com/p/righettod/source/browse/#git%2FJEE%2FClientIdentifyPOC)

> Links to source code management system are provided instead of static archives because initial authorcontinue to work on profiling detection and attacker identification concepts using feedback coming from implementationin real production application.

## Reminder about profiling phase of an attack

Except on TV, attacking a web application (or anything) always start by
a phase in which the target is deeply analysed in order to gather as
much information as possible about it (web server software, application
framework, application software version and type, operating system…).

This phase is commonly called "**profiling**" and this one takes a big
place into the attack time frame. The profiling can be performed in a
"**passive**" or "**active**" way:

- The "**passive**" way is performed using public information and/or navigating on the target

application without doing any suspicious behaviour (browsing like a
normal user), the objective here is to not be detected.

- The "**active**" way is performed by having behaviour on the target application than can, perhaps, generate alerts depending on the monitoring in place

(example: sending HTTP request with an invalid parameter value in order
to see how the application behave).

## How can we detect that a application is currently under profiling?

### Passive profiling

#### Concept

Using this method, it's difficult to distinguish a normal user than an
attacker. An idea is to analyse the number of application
functionalities visited by user in a representative time frame.

Normal user will only use a part of the application or will use the
entire application but on an extended period (one week, one month…) but
an attacker will visit as much functionalities as possible in a
representative time frame.

Take all the web application that you use in your personal/professional
life, afterwards count how many functionalities do you use and for how
long ? Interesting track to explore it is not ?

#### Implementation

The idea is to uniquely identify a HTTP request sender in order to trace
is set of requests. There no "silver bullet" method here because IP can
be spoofed and HTTP request can be easily forged but, using information
for these sources, we can still catch a panel of attacker. As a skilled
and motivated attacker cannot be stopped, the goal here is to raise the
skill level required to play with the application.

We will use the information below to identify sender:

- Sender IP address,
- HTTP request headers:
  - Accept,
  - Accept-Encoding,
  - Accept-Language,
  - Connection,
  - User-Agent.

We will use storage to keep information below:

- Digest of the HTTP request sender information above (used as unique ID),
- Identifier of the application functionality visited (URI for example),
- Last visit date time.

We also need to know the list of functionality exposed by the
application in order to perform comparison. This one can be stored into
the same storage than information above.

We will assume here that the representative time frame is two weeks.

For each HTTP request, we will store the hit and next check if, for the
last two weeks, the visitor has visited all the application
functionalities. If it's the case then:

1. We send all current request information (we send information here because in the store we only keep a digest) to a monitoring system in order to generate an alert and launch a review of the sender information in order to decide if aggressive defensive measure should be taken against them,
2. We clean the store with the information of this sender (in order to avoid duplicate alert). Optionally it's possible to move information to archive storage type in order to perform global statistic processing for the application but it's not the goal here.

See this class
[PassiveDetectionFilter](https://code.google.com/p/righettod/source/browse/JEE/ProfilingDetectionPOC/src/main/java/com/googlecode/righettod/pdec/PassiveDetectionFilter.java)
for implementation details.

### Active profiling

#### Concept

When an attacker use this method it's a little much easier to detect the
profiling behaviour. There several point into the application that can
be checked for abnormal behaviour.

One of them is the invalid value submitted into application form, indeed
we can analyse (during input validation step) the number of invalid
values submitted by a user into a functionality (bank transfer form for
example).

If the count of error is superior to an acceptable limit (three for
example) we can assume that the visitor is playing with the application.
This method is efficient but can lead to false positive in the case of
some lubberly user.

There another more subtle way to detect profiling by literally "phishing
the attacker". In this method, we put some "honeypot" into the
application. "Honeypot" are represented here into the form of a special
custom cookie or custom HTTP header that sounds to be very interesting
to the attacker.

Theses cookies/headers are good place because a normal user will not
modify theses (they are managed by the browser). An attacker will
probably try to modify the value in order to check if the application
behaves in different way and it’s at this point that we can detect the
profiling.

#### Implementation

We will focus here on cookies area. The idea is to find, according to
application context and functionalities provided, an interesting name
and value for a cookie.

We assume here that we want to detect profiling without requiring user
to be authenticated and we also assume that there no real application
session opened with the user. Like for "Passive" profiling, we will use
some information from incoming HTTP request to uniquely identify a HTTP
request sender in order to trace is set of requests.

Expected value will be hard coded string in order to not impact
application performance.

The table below lists the name and value of the fake cookie that will be
issued at first visitor request:

| Name           | Description                                                                    | Value          | Life Time  |
|----------------| -------------------------------------------------------------------------------|--------------- |------------|
| `verbose_mode` | Simulate a flag that can enable development mode (verbose) of the application. | false          | 1 day      |

See this class
[ActiveDetectionFilter](https://code.google.com/p/righettod/source/browse/JEE/ProfilingDetectionPOC/src/main/java/com/googlecode/righettod/pdec/ActiveDetectionFilter.java)
for implementation details.

## We have detected a profiling phase then how application can defend itself?

There several way to apply counter measures against an attacker in order
to bother them in their task and we can classify them according to their
level of invasion on the client.

> Invasive measures are not legal but it's very rare that an attacker file a claim against is target.

**Level 1: Without invasion**

*Simply block connection to application*

Close TCP/IP connection or block list IP address.

**Level 2: With invasion**

*Gather information about attacker from is computer*

Run client application through browser plugin (for example Java applet
signed by the company, crafted pdf file…) and gather information like
geographically location, browser cookies, system environment variables
or any others personal information in order to obtain location/identity
of the attacker.

See this class
[WindowsDataGrabber](https://code.google.com/p/righettod/source/browse/JEE/ClientIdentifyPOC/src/main/java/com/googlecode/righettod/cip/WindowsDataGrabber.java)
for implementation details.
