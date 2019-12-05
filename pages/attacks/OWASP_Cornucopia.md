---

layout: col-sidebar
title: OWASP Cornucopia
author: 
contributors: 
permalink: /attacks/OWASP_Cornucopia
tag: attack, OWASP Cornucopia
auto-migrated: 1

---

# Main

<div style="width:100%;height:160px;border:0,margin:0;overflow: hidden;">

![Cornucopia-header.jpg](Cornucopia-header.jpg "Cornucopia-header.jpg")

</div>

<div style="width:100%;height:90px;border:0,margin:0;overflow: hidden;">

![_lab_big.jpg](_lab_big.jpg "_lab_big.jpg")

</div>

<table>
<tbody>
<tr class="odd">
<td><p>valign="top" style="border-right: 1px dotted gray;padding-right:25px;"</p></td>
<td><h2 id="owasp_cornucopia">OWASP Cornucopia</h2>
<p>OWASP Cornucopia is a mechanism in the form of a card game to assist software development teams identify security requirements in Agile, conventional and formal development processes. It is language, platform and technology agnostic.</p>
<h2 id="introduction">Introduction</h2>
<p>The idea behind Cornucopia is to help development teams, especially those using Agile methodologies, to identify application security requirements and develop security-based user stories. Although the idea had been waiting for enough time to progress it, the final motivation came when <a href="http://www.safecode.org/">SAFECode</a> published its <a href="http://www.safecode.org/publications/SAFECode_Agile_Dev_Security0712.pdf">Practical Security Stories and Security Tasks for Agile Development Environments</a> in July 2012.</p>
<p>The Microsoft SDL team had already published its super <a href="http://www.microsoft.com/security/sdl/adopt/eop.aspx">Elevation of Privilege: The Threat Modeling Game</a> (EoP) but that did not seem to address the most appropriate kind of issues that web application development teams mostly have to address. EoP is a great concept and game strategy, and was <a href="http://blogs.msdn.com/b/sdl/archive/2010/03/02/announcing-elevation-of-privilege-the-threat-modeling-game.aspx">published under</a> a <a href="http://creativecommons.org/licenses/by/3.0/">Creative Commons Attribution License</a>. Cornucopia {{#switchtablink:Ecommerce Website Edition</p></td>
<td><p>Ecommerce Website Edition}} is based the concepts and game ideas in EoP, but those have been modified to be more relevant to the types of issues ecommerce website developers encounter. It attempts to introduce threat-modelling ideas into development teams that use Agile methodologies, or are more focused on web application weaknesses than other types of software vulnerabilities or are not familiar with STRIDE and DREAD.</p>
<h2 id="the_card_decks">The Card Decks</h2>
<p><em>Ecommerce Website Edition</em></p>
<p>Instead of EoP’s STRIDE suits, Cornucopia suits were selected based on the structure of the <a href="https://www.owasp.org/index.php/OWASP_Secure_Coding_Practices_-_Quick_Reference_Guide">OWASP Secure Coding Practices - Quick Reference Guide</a> (SCP), but with additional consideration of sections in the <a href="https://www.owasp.org/index.php/Category:OWASP_Application_Security_Verification_Standard_Project">OWASP Application Security Verification Standard</a>, the <a href="https://www.owasp.org/index.php/OWASP_Testing_Project">OWASP Testing Guide</a> and David Rook’s <a href="http://www.securityninja.co.uk/secure-development/the-principles-place/">Principles of Secure Development</a>. These provided five suits, and a sixth called “Cornucopia” was created for everything else:</p>
<ul>
<li>Data validation and encoding</li>
<li>Authentication</li>
<li>Session management</li>
<li>Authorization</li>
<li>Cryptography</li>
<li>Cornucopia</li>
</ul>
<p>Each suit contains 13 cards (Ace, 2-10, Jack, Queen and King) but, unlike EoP, there are also two Joker cards. The content was mainly drawn from the SCP. Full <a href="Cornucopia_-_Ecommerce_Website_Edition_-_Wiki_Deck" title="wikilink">Wiki Deck</a>.</p>
<p><em>Other Decks</em></p>
<p>Future editions such as for mobile app development will use different sources of information and suits.</p>
<h2 id="mappings">Mappings</h2>
<p>The other driver for Cornucopia is to link the attacks with requirements and verification techniques. An initial aim had been to reference <a href="http://cwe.mitre.org/">CWE</a> weakness IDs, but these proved too numerous, and instead it was decided to map each card to <a href="http://capec.mitre.org/">CAPEC</a> software attack pattern IDs which themselves are mapped to CWEs, so the desired result is achieved.</p>
<p>Each card is also mapped to the 36 primary security stories in the <a href="http://www.safecode.org/publications/SAFECode_Agile_Dev_Security0712.pdf">SAFECode document</a>, as well as to the OWASP <a href="https://www.owasp.org/index.php/OWASP_Secure_Coding_Practices_-_Quick_Reference_Guide">SCP v2</a>, <a href="https://www.owasp.org/images/3/33/OWASP_Application_Security_Verification_Standard_3.0.1.pdf">ASVS v3.0.1</a> and <a href="https://www.owasp.org/index.php/OWASP_AppSensor_Project">AppSensor</a> (application attack detection and response) to help teams create their own security-related stories for use in Agile processes.</p>
<h2 id="licensing">Licensing</h2>
<p>OWASP Cornucopia is free to use. It is licensed under the <a href="http://creativecommons.org/licenses/by-sa/3.0/">Creative Commons Attribution-ShareAlike 3.0 license</a>, so you can copy, distribute and transmit the work, and you can adapt it, and use it commercially, but all provided that you attribute the work and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.</p>
<p>© OWASP Foundation</p>
<h2 id="other_security_gamification">Other Security Gamification</h2>
<p>If you are interested in using gaming for security, also see <a href="http://www.microsoft.com/security/sdl/adopt/eop.aspx">Elevation of Privilege: The Threat Modeling Game</a> mentioned above, <a href="http://securitycards.cs.washington.edu/">Security Cards</a> from the University of Washington, the commercial card game <a href="http://www.controlalthack.com/">Control-Alt-Hack</a> (<a href="http://media.blackhat.com/bh-us-12/Briefings/Kohno/BH_US_12_Kohno_Control_Alt_Hack_Slides.pdf">presentation</a> for latter), <a href="https://www.owasp.org/index.php/OWASP_Snakes_and_Ladders">OWASP Snakes and Ladders</a>, and web application security training tools incorporating gamification such as <a href="https://www.owasp.org/index.php/OWASP_Hackademic_Challenges_Project">OWASP Hackademic Challenges Project</a>, <a href="https://www.owasp.org/index.php/OWASP_Security_Shepherd">OWASP Security Shepherd</a> and <a href="http://itsecgames.blogspot.co.uk/">ITSEC Games</a>.</p>
<p>Additionally, Adam Shostack maintains a list of tabletop security games and related resources at <a href="http://adam.shostack.org/games.html">security games</a>.</p></td>
<td><p>valign="top" style="padding-left:25px;width:200px;border-right: 1px dotted gray;padding-right:25px;"</p></td>
<td><h2 id="what_is_cornucopia">What is Cornucopia?</h2>
<p>OWASP Cornucopia is a card game used to help derive application security requirements during the software development life cycle. To start using Cornucopia:</p>
<ul>
<li>Download the document</li>
<li>Print the cards onto plain paper or pre-scored card</li>
<li>Cut/separate the individual cards</li>
<li>Identify an application, module or component to assess</li>
<li>Invite business owners, architects, developers, testers along for a card game</li>
<li>Get those infosec folk to provide chocolate, pizza, beer, flowers or all four as prizes</li>
<li>Select a portion of the deck to start with</li>
<li>{{#switchtablink:How to Play</li>
</ul></td>
<td><p>Play the game}} to discuss &amp; document security requirements (and to win rounds)</p>
<ul>
<li>Remember, points make prizes!</li>
</ul>
<p>Listen to the <a href="http://trustedsoftwarealliance.com/2014/03/21/the-owasp-cornucopia-project-with-colin-watson/">OWASP 24/7 Podcast</a> about Cornucopia.</p>
<h2 id="presentation">Presentation</h2>
<figure>
<img src="Cornucopia-presentation-small.jpg" title="Cornucopia-presentation-small.jpg" alt="Cornucopia-presentation-small.jpg" /><figcaption>Cornucopia-presentation-small.jpg</figcaption>
</figure>
<p>The game rules are in the document download. But the OpenOffice <a href="media:Owasplondon-colinwatson-cornucopia.odp" title="wikilink">project presentation</a> includes an animated version of four demonstration rounds. The presentation is recorded <a href="http://youtu.be/Q_LE-8xNXVk">on video</a>.</p>
<h2 id="project_leaders">Project Leaders</h2>
<ul>
<li><a href="https://www.owasp.org/index.php/User:Clerkendweller">Colin Watson</a> <a href="mailto:colin.watson@owasp.org">@</a></li>
<li><a href="https://www.owasp.org/index.php/User:Dariodf">Darío De Filippis</a> <a href="mailto:dariodefilippis@gmail.com">@</a></li>
</ul>
<h2 id="related_projects">Related Projects</h2>
<ul>
<li><a href="OWASP_Secure_Coding_Practices_-_Quick_Reference_Guide" title="wikilink">OWASP Secure Coding Practices - Quick Reference Guide</a></li>
<li><a href=":Category:OWASP_Application_Security_Verification_Standard_Project" title="wikilink">OWASP Application Security Verification Standard</a></li>
</ul></td>
<td><p>valign="top" style="padding-left:25px;width:200px;"</p></td>
<td><h2 id="quick_links">Quick Links</h2>
<ul>
<li><a href="https://youtu.be/i5Y0akWj31k">How to Play</a> video</li>
<li><a href="https://www.owasp.org/index.php/File:Cornucopia-scoresheet.pdf">Scoresheet</a></li>
<li>{{#switchtablink:Get the Cards</li>
</ul></td>
<td><p>All sources and downloads...}}</p>
<h2 id="reference_files">Reference Files</h2>
<ul>
<li><a href="https://www.owasp.org/index.php/File:OWASP_SCP_Quick_Reference_Guide_v2.pdf">OWASP SCP requirements</a></li>
<li><a href="https://www.owasp.org/images/5/58/OWASP_ASVS_Version_2.pdf">OWASP ASVS verification IDs</a></li>
<li><a href="https://www.owasp.org/index.php/AppSensor_DetectionPoints">OWASP AppSensor attack detection point IDs</a></li>
<li><a href="http://capec.mitre.org/data/archive/capec_v1.7.1.zip">CAPEC IDs</a></li>
<li><a href="http://www.safecode.org/publications/SAFECode_Agile_Dev_Security0712.pdf">SAFECode security-focused story IDs</a></li>
</ul>
<p>The OWASP SCP does not include identity values for the requirements, so please use <a href="https://www.owasp.org/index.php/File:Owasp-requirements-numbering.zip">this list</a>.</p>
<h2 id="news_and_events">News and Events</h2>
<ul>
<li>[26 Jun 2018] v1.20 FR released</li>
<li>[14 May 2018] Printed deck purchase details updated</li>
<li>[13 Jan 2018 v1.20 PT-BR released</li>
<li>[23 Aug 2016] Presentation at <a href="https://www.owasp.org/index.php/Newcastle">OWASP Newcastle</a></li>
<li>[29 Jun 2016] v1.20 released</li>
<li>[21 Jan 2016] <a href="Cornucopia_-_Ecommerce_Website_Edition_-_Wiki_Deck" title="wikilink">Wiki Deck</a> published</li>
<li>[30 Dec 2015] Darío De Filippis becomes project co-leader</li>
<li>[24 Sep 2015] <a href="http://appsecusa2015.sched.org/event/7f3dba889c0ec9e37900e289c9660503#.VZ6aoXhflNY">Lightning training</a> at AppSec USA 2015</li>
<li>[01 Jun 2015] <a href="https://youtu.be/i5Y0akWj31k">How to Play video</a> published</li>
<li>[20 May 2015] Working session at <a href="http://2015.appsec.eu/project-summit/">OWASP Project Summit</a> - How to play video</li>
<li>[31 Mar 2015] v1.10 released</li>
<li>[02 Mar 2015] Decks available from <a href="https://www.owasp.org/index.php/OWASP_Merchandise#Cornucopia_Cards">OWASP merchandise store</a></li>
<li>[18 Feb 2015] Project awarded Labs status</li>
</ul>
<h2 id="pcidss">PCIDSS</h2>
<figure>
<img src="Cornucopia-pcidss-ecommerce-guidelines-small.jpg" title="Cornucopia-pcidss-ecommerce-guidelines-small.jpg" alt="Cornucopia-pcidss-ecommerce-guidelines-small.jpg" /><figcaption>Cornucopia-pcidss-ecommerce-guidelines-small.jpg</figcaption>
</figure>
<p>OWASP Cornucopia Ecommerce Website Edition is referenced in the current <a href="https://www.pcisecuritystandards.org">Payment Card Industry Security Standards Council</a> information supplement <a href="https://www.pcisecuritystandards.org/pdfs/PCI_DSS_v2_eCommerce_Guidelines.pdf">PCI DSS E-commerce Guidelines</a> v2, January 2013</p>
<h2 id="classifications">Classifications</h2>
<table>
<tbody>
<tr class="odd">
<td><p>rowspan="2" align="center" valign="top" width="50%"</p></td>
<td><figure>
<img src="Owasp-labs-trans-85.png" title="Owasp-labs-trans-85.png" alt="Owasp-labs-trans-85.png" /><figcaption>Owasp-labs-trans-85.png</figcaption>
</figure></td>
<td><p>align="center" valign="top" width="50%"</p></td>
<td><figure>
<img src="Owasp-builders-small.png" title="Owasp-builders-small.png" alt="Owasp-builders-small.png" /><figcaption>Owasp-builders-small.png</figcaption>
</figure></td>
</tr>
<tr class="even">
<td><p>align="center" valign="top" width="50%"</p></td>
<td><figure>
<img src="Owasp-defenders-small.png" title="Owasp-defenders-small.png" alt="Owasp-defenders-small.png" /><figcaption>Owasp-defenders-small.png</figcaption>
</figure></td>
<td></td>
<td></td>
</tr>
<tr class="odd">
<td><p>colspan="2" align="center"</p></td>
<td><figure>
<img src="Cc-button-y-sa-small.png" title="Cc-button-y-sa-small.png" alt="Cc-button-y-sa-small.png" /><figcaption>Cc-button-y-sa-small.png</figcaption>
</figure></td>
<td></td>
<td></td>
</tr>
<tr class="even">
<td><p>colspan="2" align="center"</p></td>
<td><figure>
<img src="Project_Type_Files_DOC.jpg" title="Project_Type_Files_DOC.jpg" alt="Project_Type_Files_DOC.jpg" /><figcaption>Project_Type_Files_DOC.jpg</figcaption>
</figure></td>
<td></td>
<td></td>
</tr>
</tbody>
</table></td>
</tr>
</tbody>
</table>

# Get the Cards

## Printed

![Cornucopia-square-logo-350.jpg](Cornucopia-square-logo-350.jpg
"Cornucopia-square-logo-350.jpg")

Professionally printed decks are available by two methods:

  - Single decks or in bulk from OWASP (v1.20)
      - As promotion items **by OWASP Leaders** from their own chapter
        budgets [Chapter and Project Merchandise Request
        form](https://docs.google.com/a/owasp.org/forms/d/e/1FAIpQLSez9mV97HuqvYhCldE2hYhX3UjQM1oO5bLy44HkOZSpni0OzQ/viewform?formkey=dF85bGtvdWdrd2JjYldNZ1gxSkJxaEE6MQ)
      - For other individuals, organisations and companies, please email
        <dawn.aitken@owasp.org> with purchase enquiries
  - Request a free deck of cards gifted by [Blackfoot UK
    Limited](http://blackfootuk.com/) or download their donated
    print-ready artwork:
      - Request a free [pack of cards
        (v1.10)](http://blackfootuk.com/cornucopia/receive-a-set-of-cards/)
        (gifted by Blackfoot UK)

## Source files

Cornucopia - Ecommerce Website Edition:

  - v1.2 (current version)
      - [EN
        DOC](https://www.owasp.org/index.php/File:OWASP-Cornucopia-Ecommerce_Website.docx)

| [FR
DOC](https://github.com/grandtom/OWASP-Cornucopia-Translate-Cards---FR)
| [PT-BR
DOC](https://github.com/wagnerfusca/OWASP-Cornucopia-Translate-Cards---PT)

  -   - [EN
        PDF](https://www.owasp.org/index.php/File:Owasp-cornucopia-ecommerce_website.pdf)
      - [Print-Ready design
        files](https://drive.google.com/open?id=0ByNJ8mfWALwjNXpQMUNBYnJsT2QyQ0lkb3VNX1BCM3JLNlBZ)
        24Mb zip

  - v1.1 EN

      - DOC - see current version link above for previous versions of
        DOC including with track changes
      - PDF - see current version link above for previous versions of
        PDF
      - [Wiki](Cornucopia_-_Ecommerce_Website_Edition_-_Wiki_Deck "wikilink")
      - [Print-Ready design
        files](https://drive.google.com/open?id=0ByNJ8mfWALwjb283ZE5GNmFMM2FGWGl2WC14aDJDQ0ZsNk00)
        24Mb zip

  - v1.04 EN

      - DOC - see current version link above for previous versions of
        DOC including with track changes
      - PDF - see current version link above for previous versions of
        PDF
      - [Print-Ready design
        files](https://4ed64fe7f7e3f627b8d0-bc104063a9fe564c2d8a75b1e218477a.ssl.cf2.rackcdn.com/cornucopia-ecom-1v04-blackfoot.zip)
        (gifted by Blackfoot UK) 47Mb Zip

The current version of Cornucopia Ecommerce Website Edition cards (v1.20
with updated mapping to ASVS v3.0.1 and CAPEC v2.8, and has some minor
text changes on the cards) can be printed using the following methods:

1.  Download the free Adobe Illustrator files
    ([EN](https://drive.google.com/open?id=0ByNJ8mfWALwjNXpQMUNBYnJsT2QyQ0lkb3VNX1BCM3JLNlBZ))
    and get them professionally printed
2.  Download and self-print the free document word-processing
    ([EN](https://www.owasp.org/index.php/File:OWASP-Cornucopia-Ecommerce_Website.docx),
    [FR](https://github.com/grandtom/OWASP-Cornucopia-Translate-Cards---FR))
    or PDF
    ([EN](https://www.owasp.org/index.php/File:Owasp-cornucopia-ecommerce_website.pdf))
    1.  Print the document onto business card blank cards; or
    2.  Print the document onto normal card and cut the cards out
        individually using the guide; or
3.  Generate your own cards from the free [source XML data
    file](https://www.owasp.org/index.php/File:Cornucopia-deck-ecommercewebsite-XML.zip)

There are also other ways to obtain particular versions:

  - Download the free [PDF
    (v1.03)](https://www.owasp.org/index.php/File:Owasp_cornucopia_printreadyimages.zip)
    (gifted by Travelex)
      - Have the cards commercially printed; or
      - Import into your own files (such as [this
        way](http://lists.owasp.org/pipermail/owasp_cornucopia/2014-January/000018.html)
        suggested by Cam Morris via the mailing list)

OWASP does not endorse or recommend commercial products or services.

## Twitter

Collect/share/use the pseudo-random cards tweeted twice daily
[@OWASPCornucopia](https://twitter.com/OWASPCornucopia)

# How to Play

![Cornucopia-card-cornucopia-K.png](Cornucopia-card-cornucopia-K.png
"Cornucopia-card-cornucopia-K.png")
![Cornucopia-card-session-9.png](Cornucopia-card-session-9.png
"Cornucopia-card-session-9.png")

It is possible to play Cornucopia in many different ways. Here is one
way, and explained in a [YouTube video](https://youtu.be/i5Y0akWj31k).

## Primary method

  - A - Preparations
    A1. Obtain a deck, or print your own Cornucopia deck and
    separate/cut out the cards
    A2. Identify an application or application process to review; this
    might be a concept, design or an actual implementation
    A3. Create a data flow diagram
    A4. Identify and invite a group of 3-6 architects, developers,
    testers and other business stakeholders together and sit around a
    table (try to include someone fairly familiar with application
    security)
    A5. Have some prizes to hand (gold stars, chocolate, pizza, beer or
    flowers depending upon your office culture)
  - B - Play
    One suit - Cornucopia - acts as trumps. Aces are high (i.e. they
    beat Kings). It helps if there is someone dedicated to documenting
    the results who is not playing.
    B1. Remove the Jokers and a few low-score (2, 3, 4) cards from
    Cornucopia suit to ensure each player will have the same number of
    cards
    B2. Shuffle the pack and deal all the cards
    B3. To begin, choose a player randomly who will play the first card
    - they can play any card from their hand except from the trump suit
    - Cornucopia
    B4. To play a card, each player must read it out aloud, and explain
    how (or not) the threat could apply (the player gets a point for
    attacks that work, and the group thinks it is an actionable bug) -
    don’t try to think of mitigations at this stage, and don’t exclude a
    threat just because it is believed it is already mitigated - someone
    record the card on the score sheet
    B5. Play clockwise, each person must play a card in the same way; if
    you have any card of the matching lead suit you must play one of
    those, otherwise they can play a card from any other suit. Only a
    higher card of the same suit, or the highest card in the trump suit
    Cornucopia, wins the hand.
    B6. The person who wins the round, leads the next round (i.e. they
    play first), and thus defines the next lead suit
    B7. Repeat until all the cards are played
  - C - Scoring
    The objective is to identify applicable threats, and win hands
    (rounds):
    C1. Score +1 for each card you can identify as a valid threat to the
    application under consideration
    C2. Score +1 if you win a round
    C3. Once all cards have been played, whoever has the most points
    wins
  - D - Closure
    D1. Review all the applicable threats and the matching security
    requirements
    D2. Create user stories, specifications and test cases as required
    for your development methodology

See Márk Vinkovits leading a threat modelling [talk and group
session](https://www.youtube.com/watch?v=9dVDqeO6y3A) playing Cornucopia
in the OWASP track @hacktivityconf 1510.

## Alternative game rules

  - If you are new to the game, remove the two Joker cards to begin
    with. Add the Joker cards back in once people become more familiar
    with the process. Apart from the “trumps card game” rules described
    above which are very similar to the EoP, the deck can also be played
    as the “twenty-one card game” (also known as “pontoon” or
    “blackjack”) which normally reduces the number of cards played
    in each round.
  - Practice on an imaginary application, or even a future planned
    application, rather than trying to find fault with existing
    applications until the participants are happy with the usefulness of
    the game.
  - Consider just playing with one suit to make a shorter session – but
    try to cover all the suits for every project. Or even better just
    play one hand with some pre-selected cards, and score only on the
    ability to identify security requirements. Perhaps have one game of
    each suit each day for a week or so, if the participants cannot
    spare long enough for a full deck.
  - Some teams have preferred to play a full hand of cards, and then
    discuss what is on the cards after each round (instead of after each
    person plays a card).
  - Another suggestion is that if a player fails to identify the card is
    relevant, allow other players to suggest ideas, and potentially let
    them gain the point for the card. Consider allowing extra points for
    especially good contributions.
  - You can even play by yourself. Just use the cards to act as
    thought-provokers. Involving more people will be beneficial though.
  - In Microsoft's EoP guidance, they recommend cheating as a good game
    strategy

# FAQs

![Cornucopia-card-authorization-8.png](Cornucopia-card-authorization-8.png
"Cornucopia-card-authorization-8.png")
![Cornucopia-card-cryptography-j.png](Cornucopia-card-cryptography-j.png
"Cornucopia-card-cryptography-j.png")

  - Can I copy or edit the game?
    Yes of course. All OWASP materials are free to do with as you like
    provided you comply with the Creative Commons Attribution-ShareAlike
    3.0 license. Perhaps if you create a new version, you might donate
    it to the OWASP Cornucopia Project?

<!-- end list -->

  - How can I get involved?
    Please send ideas or offers of help to the project’s mailing list.

<!-- end list -->

  - How were the attackers’ names chosen?
    EoP begins every description with words like "An attacker can...".
    These have to be phrased as an attack but I was not keen on the
    anonymous terminology, wanting something more engaging, and
    therefore used personal names. These can be thought of as external
    or internal people or aliases for computer systems. But instead of
    just random names, I thought how they might reflect the OWASP
    community aspect. Therefore, apart from "Alice and Bob", I use the
    given (first) names of current and recent OWASP employees and Board
    members (assigned in no order), and then randomly selected the
    remaining 50 or so names from the current list of paying individual
    OWASP members. No name was used more than once, and where people had
    provided two personal names, I dropped one part to try to ensure
    no-one can be easily identified. Names were not deliberately
    allocated to any particular attack, defence or requirement. The
    cultural and gender mix simply reflects theses sources of names, and
    is not meant to be world-representative.

<!-- end list -->

  - Why aren’t there any images on the card faces?
    There is quite a lot of text on the cards, and the cross-referencing
    takes up space too. But it would be great to have additional design
    elements included. Any volunteers?

<!-- end list -->

  - Are the attacks ranked by the number on the card?
    Only approximately. The risk will be application and organisation
    dependent, due to varying security and compliance requirements, so
    your own severity rating may place the cards in some other order
    than the numbers on the cards.

<!-- end list -->

  - How long does it take to play a round of cards using the full
    deck?
    This depends upon the amount of discussion and how familiar the
    players are with application security concepts. But perhaps allow
    1.5 to 2.0 hours for 4-6 people.

<!-- end list -->

  - What sort of people should play the game?
    Always try to have a mix of roles who can contribute alternative
    perspectives. But include someone who has a reasonable knowledge of
    application vulnerability terminology. Otherwise try to include a
    mix of architects, developers, testers and a relevant project
    manager or business owner.

<!-- end list -->

  - Who should take notes and record scores?
    It is better if that someone else, not playing the game, takes notes
    about the requirements identified and issues discussed. This could
    be used as training for a more junior developer, or performed by the
    project manager. Some organisations have made a recording to review
    afterwards when the requirements are written up more formally.

<!-- end list -->

  - Should we always use the full deck of cards?
    No. A smaller deck is quicker to play. Start your first game with
    only enough cards for two or three rounds. Always consider removing
    cards that are not appropriate at all of the target application or
    function being reviewed. For the first few times people play the
    game it is also usually better to remove the Aces and the two
    Jokers. It is also usual to play the game without any trumps suit
    until people are more familiar with the idea.

<!-- end list -->

  - What should players do when they have an Ace card that says
    “invented a new X attack”?
    The player can make up any attack they think is valid, but must
    match the suit of the card e.g. data validation and encoding). With
    players new to the game, it can be better to remove these to begin
    with.

<!-- end list -->

  - I don’t understand what the attack means on each card - is there
    more detailed information?
    Yes, the Wiki Deck at was created to help players understand the
    attacks. See [Wiki
    Deck](https://www.owasp.org/index.php/Cornucopia_-_Ecommerce_Website_Edition_-_Wiki_Deck).

<!-- end list -->

  - My company wants to print its own version of OWASP Cornucopia - what
    license do we need to refer to?
    What is required/reasonable might depend upon how you propose to use
    the source Cornucopia material. See fuller answer immediately below.

Some examples of re-using or reproducing Cornucopia are:

1.  Print some decks and give them away to customers
2.  Reproduce the game exactly but with a corporate-branded package
3.  Use the idea and/or source files to produce a similar game but with
    different attacks/mappings
4.  Distribute modified design files

If option 1 above, you can order these in bulk from OWASP and attach
your own details below the "compliments of" section on the boxes. There
are three aspects to consider for options 2, 3 or 4, or combinations of
those - see below. The existing printed decks (and their boxes and
leaflets include such text).

*A - Cornucopia License*

The precise wording will depend how the material is being used or
reproduced. Under Creative Commons Attribution-ShareAlike 3.0 license it
is necessary to attribute all previous contributions (in this case,
Microsoft, Boeing, Mitre, etc). The easiest place to put the wording is
on the leaflet (folded inside, or separate booklet). The current
required long-form wording is:

` OWASP Cornucopia is licensed under the Creative Commons Attribution-ShareAlike 3.0 license `<http://creativecommons.org/licenses/by-sa/3.0/>

` The files used to create these materials were created from the OWASP project and are also open source, and are licensed under the same conditions. `

` OWASP Cornucopia can be downloaded for free from the OWASP website and printed yourself. The OWASP Cornucopia project source in vendor neutral and unbranded.`

` OWASP does not endorse or recommend commercial products or services.`

` © 2012-2018 OWASP Foundation`

` This document is licensed under the Creative Commons Attribution-ShareAlike 3.0 license.`

` Acknowledgments:`

` Microsoft SDL Team for the Elevation of Privilege Threat Modelling Game, published under a Creative Commons Attribution license, as the inspiration for Cornucopia and from which many ideas, especially the game theory, were copied.`

` Keith Turpin and contributors to the “OWASP Secure Coding Practices - Quick Reference Guide”, originally donated to OWASP by Boeing, which is used as the primary source of security requirements information to formulate the content of the cards.`

` Contributors, supporters, sponsors and volunteers to the OWASP ASVS, AppSensor and Web Framework Security Matrix projects, Mitre’s Common Attack Pattern Enumeration and Classification (CAPEC), and SAFECode’s “Practical Security Stories and Security Tasks for Agile Development Environments” which are all used in the cross-references provided.`

` Playgen for providing an illuminating afternoon seminar on task gamification, and tartanmaker.com for the online tool to help create the card back pattern.`

` Blackfoot UK Limited for creating and donating print-ready design files, Tom Brennan and the OWASP Foundation for instigating the creation of an OWASP-branded box and leaflet, and OWASP employees, especially Kate Hartmann, for managing the ordering, stocking and despatch of printed card decks.`

` Oana Cornea and other participants at the AppSec EU 2015 project summit for their help in creating the demonstration video.`

` Colin Watson as author and co-project leader with Darío De Filippis, along with other OWASP volunteers who have helped in many ways.`

The box/container for the cards must have the wording:

` Created by Colin Watson.`

` Contains: One pack of Cornucopia Ecommerce Website playing cards. OWASP Cornucopia is open source and can be downloaded free of charge from the OWASP website.`

` OWASP Cornucopia is free to use. It is licensed under the Creative Commons Attribution-ShareAlike 3.0 license, so you can copy, distribute and transmit the work, and you can adapt it, and use it commercially, but all provided that you attribute the work and if you alter, transform, or build upon this work, you may distribute the resulting work only under the same or similar license to this one.`

The following short-form wording must also appear on any materials
referencing the outputs (e.g. press releases, leaflets, reports, blog
posts):

` OWASP does not endorse or recommend commercial products or services.`

` OWASP Cornucopia is licensed under the Creative Commons Attribution-ShareAlike 3.0 license and is © 2012-2016 OWASP Foundation.`

If any files are distributed electronically, the long-form wording
should also be aded in a license.txt file within the distribution.

If the intention is to use the idea only (option 3 above), the
long-form, box and short-form wording might be different, and probably
simpler. And it might make more sense to start with the
Microsoft-provided Elevation of Privilege files (and open source
license).

*B - Upcoming update to Cornucopia*

Note that the current print design files are v1.04, and the current Word
document is v1.10, but we are in the process of updating all of these to
v1.20.

Whatever is used as a starting point, please state the source version,
for example:

` Based on OWASP Cornucopia Ecommerce Website Edition v1.04`

*C - OWASP brand usage*

Additionally individuals, companies and other organisations must not
breach OWASP's brand usage guidelines.

` `<https://www.owasp.org/index.php/Marketing/Resources#tab=BRAND_GUIDELINES>

In the case of Cornucopia, in 2014 Blackfoot Limited produced some
printed decks of cards. Blackfoot's name and logo did not appear
anywhere on the OWASP-branded cards, and the OWASP logo did not appear
on the Blackfoot-branded box and leaflet. In fact there is no OWASP logo
on any part of the Blackfoot branded decks.

# Acknowledgements

![Cornucopia-card-data-A.png](Cornucopia-card-data-A.png
"Cornucopia-card-data-A.png")

## Volunteers

Cornucopia is developed, maintained, updated and promoted by a worldwide
team of volunteers. The contributors to date have been:

  - Simon Bennetts
  - Thomas Berson
  - Tom Brennan
  - Fabio Cerullo
  - Oana Cornea
  - Johanna Curiel
  - Todd Dahl
  - Luis Enriquez
  - Ken Ferris
  - Darío De Filippis
  - Sebastien Gioria
  - Tobias Gondrom
  - Timo Goosen
  - Anthony Harrison
  - Martin Haslinger
  - John Herrlin
  - Jerry Hoff
  - Marios Kourtesis
  - Franck Lacosta
  - Mathias Lemaire
  - Antonis Manaras
  - Jim Manico
  - Mark Miller
  - Cam Morris
  - Susana Romaniz
  - Ravishankar Sahadevan
  - Tao Sauvage
  - Wagner Voltz
  - Stephen de Vries
  - Colin Watson

Also:

  - Attendees at OWASP London, OWASP Manchester and OWASP Netherlands
    chapter meetings, the London Gamification meetup, and the training
    at AppSec USA 2015 in san Francisco who made helpful suggestions and
    asked challenging questions

## Others

  - Microsoft SDL Team for the Elevation of Privilege Threat Modelling
    Game, published under a Creative Commons Attribution license, as the
    inspiration for Cornucopia and from which many ideas, especially the
    game theory, were copied.
  - Keith Turpin and contributors to the “OWASP Secure Coding Practices
    - Quick Reference Guide”, originally donated to OWASP by Boeing,
    which is used as the primary source of security requirements
    information to formulate the content of the cards.
  - Contributors, supporters, sponsors and volunteers to the OWASP ASVS,
    AppSensor and Web Framework Security Matrix projects, Mitre’s Common
    Attack Pattern Enumeration and Classification (CAPEC), and
    SAFECode’s “Practical Security Stories and Security Tasks for
    Agile Development Environments” which are all used in the
    cross-references provided.
  - Playgen for providing an illuminating afternoon seminar on task
    gamification, and tartanmaker.com for the online tool to help create
    the card back pattern.
  - Blackfoot UK Limited for creating and donating print-ready design
    files, Tom Brennan and the OWASP Foundation for instigating the
    creation of an OWASP-branded box and leaflet, and OWASP employees,
    especially Kate Hartmann, for managing the ordering, stocking and
    despatch of printed card decks.
  - Oana Cornea and other participants at the AppSec EU 2015 project
    summit for their help in creating the demonstration video.
  - Colin Watson as author and co-project leader with Darío De Filippis,
    along with other OWASP volunteers who have helped in many ways.

# Road Map and Getting Involved

![Cornucopia-card-authentication-7.png](Cornucopia-card-authentication-7.png
"Cornucopia-card-authentication-7.png")
![Cornucopia-card-joker-a.png](Cornucopia-card-joker-a.png
"Cornucopia-card-joker-a.png")

Version history (see
[uploads](https://www.owasp.org/index.php/File:OWASP-Cornucopia-Ecommerce_Website.docx)):

  - Alpha version (0.40) was issued in August 2012
  - Beta version (1.00) was released in February 2013
  - Stable release (1.02) was released in August 2013, following
    feedback from mailing list and use with groups of developers
  - Release v1.03 included minor changes
  - Release v1.04 included a text correction on one card
  - Release v1.05 included additional narrative and FAQs
  - Current release v1.10 included cross-references updated for 2014
    version of ASVS, contributors updated and minor text changes to
    cards to improve readability
  - Current release v1.20 included cross-references updated for version
    3.0.1 of ASVS and CAPEC v2.8, and many minor text changes including
    further contributors.

As of July 2018, the priorities are:

  - ~~Develop Cornucopia Wiki Deck~~ done
  - ~~Update the document/deck to shorten some card text \[completed
    ready for v1.10\]~~ done
  - ~~Map to ASVS 2014~~ done
  - ~~Map to ASVSv3 2016~~ done
  - ~~Check/update CAPEC mappings~~ done
  - ~~Translate into French~~ done
  - Translate into French (completed), German (in progress), Japanese,
    Portuguese (in progress), Spanish (in progress) and other languages
    (help needed please)
  - ~~Make card decks available via OWASP Merchandise Store~~ done
  - ~~Create a video "how to play"~~ done
  - Update printed decks in non-EN languages

Involvement in the development and promotion of Cornucopia is actively
encouraged\! You do not have to be a security expert in order to
contribute. Some of the ways you can help:

## Localization

Are you fluent in another language? Can you help translate Cornucopia
into that language?

## Use and Promote the Cornucopia Card Decks

Please help raise awareness of Cornucopia by printing cards:

  - Use Cornucopia with specifiers, architects, designers, developers,
    testers and others, in part to train them, but also to solicit
    feedback on their usability, practicality and appropriateness for
    their work
  - Create video about how to play the game
  - Develop a mobile app to play the game

## Feedback

Please use the [friendly project mailing
list](https://groups.google.com/a/owasp.org/forum/#!forum/cornucopia-project)
for feedback:

  - What do like?
  - What don't you like?
  - What cards don't make sense?
  - How could the guidance be improved?
  - What other decks would you like to see?

## Keep the Cards Updated

As the source referenced documents change, we have to update the decks.
You may also find errors and omissions. In the first instance, please
send a message to the [friendly project mailing
list](https://lists.owasp.org/mailman/listinfo/owasp_cornucopia) if you
have identified errors & omissions, have some time to maintain the
source documents, or can help in other ways.

## Create a New Deck

The only version currently available is the Cornucopia Ecommerce Website
Edition in English. We would like to create a new mobile app specific
deck, probably using the wonderful [OWASP Mobile Security
Project](https://www.owasp.org/index.php/OWASP_Mobile_Security_Project)
as inspiration for the card source materials. Do you have an idea for
your own application security requirements card deck? Perhaps for
{{\#switchtablink:Mobile App Edition |mobile apps}} or something else?

# About Ecommerce Website Edition

__NOTOC__ <headertabs></headertabs>

[Category: Attack](Category:_Attack "wikilink") [Category:
Threat_Modeling](Category:_Threat_Modeling "wikilink") [Category:OWASP
Project](Category:OWASP_Project "wikilink")
[Category:OWASP_Builders](Category:OWASP_Builders "wikilink")
[Category:OWASP_Defenders](Category:OWASP_Defenders "wikilink")
[Category:OWASP_Document](Category:OWASP_Document "wikilink")
[Category:OWASP_Download](Category:OWASP_Download "wikilink")
[Category:SAMM-SR-1](Category:SAMM-SR-1 "wikilink")
[Category:SAMM-SR-2](Category:SAMM-SR-2 "wikilink")
[Category:SAMM-TA-1](Category:SAMM-TA-1 "wikilink")
[Category:SAMM-EG-2](Category:SAMM-EG-2 "wikilink")