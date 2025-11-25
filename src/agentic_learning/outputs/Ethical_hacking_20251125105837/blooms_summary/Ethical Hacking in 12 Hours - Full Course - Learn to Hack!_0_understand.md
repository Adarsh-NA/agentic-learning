# Practical Ethical Hacking — Fundamental Concepts & Principles

Below are the core terms, precise definitions, helpful analogies, a conceptual mind‑map showing how things connect, and reflection questions to deepen understanding. These are drawn from the transcription and organized to help a student internalize what ethical hacking (penetration testing) is and how the foundational concepts interrelate.

---

## 1) Key Terms & Short Definitions
- **Ethical Hacking / Penetration Testing (Pen Test)**  
  Authorized, legal security testing where a hired tester attempts to find and exploit weaknesses in systems (networks, web apps, wireless, physical) so the owner can fix them.

- **Reconnaissance / Information Gathering**  
  Passive and active collection of intelligence about a target (OSINT, public records, subdomains, employee info). First phase of a pentest.

- **Scanning & Enumeration**  
  Actively probing the target (ports, services, versions) and extracting more detailed information (user lists, shares, software versions) to find exploitable points.

- **Exploitation (Gaining Access)**  
  Using discovered vulnerabilities, misconfigurations, or credentials to obtain access (a shell, user session) on a target.

- **Post‑Exploitation (Maintaining Access)**  
  Actions after initial access: privilege escalation, persistence, lateral movement, data collection, evidence capture — done ethically and documented for clients.

- **Covering Tracks / Cleanup**  
  For ethical hackers: remove test accounts and tools they added, fully document actions — restore systems to their original state.

- **Methodology / Five Stages of Ethical Hacking**  
  A repeatable workflow: Reconnaissance → Scanning & Enumeration → Exploitation → Maintaining Access → Covering Tracks (plus Reporting & Debrief).

- **OSI Model**  
  Seven-layer networking model: Physical, Data Link, Network, Transport, Session, Presentation, Application. Useful shorthand when discussing problems (e.g., “Layer 2 issue”).

- **IP Address (IPv4 / IPv6)**  
  Layer-3 logical addresses; IPv4 is 32-bit (dotted decimal), IPv6 is 128-bit (hex). NAT helps conserve IPv4 by mapping many private addresses to one public address.

- **NAT (Network Address Translation)**  
  Router technique that lets private internal addresses share a single public IP so many devices can use IPv4.

- **Subnet / CIDR (`/24`, `/16`, etc.)**  
  Division of an IP network; CIDR notation indicates how many bits are fixed for the network. Determines host count and ranges.

- **MAC Address**  
  Layer-2 physical address (NIC). First 3 octets identify vendor (OUI). Used by switches.

- **TCP / UDP**  
  Transport protocols — TCP (connection-oriented, reliable; e.g., HTTP, SSH) and UDP (connectionless, faster; e.g., DNS, VoIP).

- **TCP Three‑Way Handshake**  
  SYN → SYN‑ACK → ACK; how TCP connections are established.

- **Ports & Common Services**  
  Numeric endpoints used by services: HTTP(80), HTTPS(443), SSH(22), FTP(21), DNS(53), SMB(139/445), etc.

- **Virtual Machine (VM)**  
  Software emulation of a computer used to create isolated labs (Kali, Windows VMs, etc.).

- **Root / Administrator / Privilege Escalation**  
  Highest privilege on Linux (`root`) or Windows (`SYSTEM`/`Administrator`). Escalation is moving from a lower-privilege account to higher privileges.

- **`sudo`**  
  Run a command with elevated privileges in Unix‑like systems (super-user do). Users must be in `sudoers`.

- **Shell (Bind vs Reverse)**  
  - *Reverse shell*: target connects back to attacker’s listener.  
  - *Bind shell*: target binds a port and attacker connects to that port.

- **Payload (Staged vs Non-staged)**  
  Code sent during exploitation. *Staged* payloads are sent in pieces (often smaller initial footprint); *non‑staged* payloads send the full payload at once. In metasploit, the notation often shows the difference (`/` vs `_` in how payloads are listed).

- **SUID / SGID / Sticky Bit (Unix permissions)**  
  Special file permission bits: SUID allows a binary to run with the file owner’s privileges (often root) — can be abused for privilege escalation if misconfigured.

- **LFI / RFI (Local/Remote File Inclusion)**  
  Web vulnerability where an attacker can include local (LFI) or remote (RFI) files via web input — may lead to info disclosure or RCE.

- **Credential Stuffing / Password Spraying / Brute Force**  
  - *Credential stuffing*: replay leaked username+password pairs against services.  
  - *Password spraying*: try a small set of likely passwords against many usernames (avoids account lockout).  
  - *Brute force*: test many passwords for a single account (can cause lockouts and be noisy).

- **OSINT (Open Source Intelligence)**  
  Collection of publicly available information (social media, search engines, public breaches) for reconnaissance.

- **Tools Mentioned (categories)**  
  - Note taking: KeepNote, CherryTree, OneNote, Joplin  
  - Screenshots: Greenshot, Flameshot  
  - VM: VMware Workstation, VirtualBox  
  - Linux / Hacking OS: Kali Linux  
  - Scanning/Enumeration: nmap, netdiscover, arp-scan, nikto, dirb/dirbuster, ffuf, sublist3r, Amass, crt.sh  
  - Proxy / Web testing: Burp Suite (Community / Pro), Wappalyzer, BuiltWith, WhatWeb  
  - Vulnerability scanners: Nessus  
  - Exploitation & post: Metasploit (msfconsole), msfvenom; netcat (nc)  
  - Enum/Automation: linPEAS / winPEAS, pspy, sx tools, hashcat for cracking  
  - GitHub code, exploit-database, Dehashed, breach parsing scripts

- **Note Keeping Best Practices**  
  - Capture screenshots with evidence (IP, timestamp, output).  
  - Keep a consistent structure (target → findings → screenshots → evidence).  
  - Use check marks to indicate report items completed.

- **Soft Skills**  
  - Clear writing (reports), presentation (debriefs), desire to learn, perseverance, non‑complacency, community contribution (blogs, GitHub, Twitter).

---

## 2) Core Analogies (to internalize the ideas)
- **Three‑way handshake = greeting at the door**  
  - SYN = “Hello, can we talk?”  
  - SYN‑ACK = “Yes, I hear you and can talk.”  
  - ACK = “Great — let’s talk.”

- **NAT = Home router / family mailbox**  
  - Your home has many devices (phones, TV, cameras) but one mailbox address facing the world (public IP). NAT maps many private addresses to one public.

- **Subnetting = Apartment building**  
  - The building is a network. Floors are subnets. Each floor has a limited number of apartments (hosts). CIDR `/24` is like a floor with 256 apartment numbers.

- **MAC address = House’s physical mail slot (hardware ID)**  
  - The MAC is the unique physical identifier attached to the NIC — like the unique plaque on a mailbox.

- **VM = Dollhouse inside a house**  
  - Virtual machine = a computer that lives inside another computer, like a dollhouse inside your home — isolated, but using the host’s resources.

- **Reverse shell = Victim calling attacker**  
  - Attacker listens on a phone line; the victim calls the attacker and the connection is established (reverse).  
  - Bind shell = Attacker calls the victim’s open phone line (bind).

- **SUID binary = A staffer’s key that opens the boss’s office**  
  - If a program runs with SUID root, running that program is like being allowed to temporarily use the boss’s key — misuse can give you access to the boss room (root).

- **Reconnaissance = Detective work before the break-in**  
  - Gather public clues (social media, Google dorks, cert logs) before attempting to probe the walls.

---

## 3) Conceptual Mind Map (simplified)
Use this as the navigation map for study and action. The arrows mean “leads to / informs”:

```
Ethical Hacking (Goal: find & fix weaknesses)
|
+-- Reconnaissance / OSINT
|    - Google / Google dorks
|    - Social media (LinkedIn, Twitter)
|    - Email discovery (Hunter, Phonebook, Clearbit)
|    - Breach data (Dehashed, local breach databases)
|    -> produces: user lists, domain & subdomain names, leaked credentials
|
+-- Scanning & Enumeration (active)
|    - Discover live hosts (netdiscover, arp-scan)
|    - Port & service discovery (nmap)
|    - Web app fingerprinting (WhatWeb, BuiltWith, Wappalyzer)
|    - Subdomain discovery (crt.sh, sublist3r, amass)
|    - Directory busting (ffuf, dirb, dirbuster)
|    - Vulnerability scanning (nikto, nessus)
|    -> produces: open ports, versions, endpoints, potential vuln IDs
|
+-- Analysis / Research
|    - Map findings to public exploits (Exploit-DB, GitHub)
|    - Check CVEs, metasploit modules
|    -> decide: exploitation strategy (manual vs metasploit)
|
+-- Exploitation (Gaining Access)
|    - Choose payload: reverse vs bind shell
|    - Choose payload staging: staged vs non-staged
|    - Use metasploit / manual exploit scripts
|    -> result: shell (low privilege or root/admin)
|
+-- Post-Exploitation
|    - Privilege escalation (linPEAS, winPEAS, SUID, unquoted path)
|    - Password harvesting ( /etc/shadow, LSA secrets )
|    - Lateral movement (pivoting)
|    - Persistence & cleanup (only in authorized tests)
|    -> final: report & debrief
|
+-- Reporting & Debrief
     - Include screenshots, evidence, remediation steps
     - Walk client through vulnerabilities and fixes
```

---

## 4) Reflection Questions (for deeper thinking and interview prep)

1. **Ethics & Scope**
   - Why is it essential to have explicit permission before testing a target? What are legal and professional consequences of failing to secure written permission?

2. **Recon & Prioritization**
   - Given a new external client with dozens of public subdomains and thousands of IPs, how would you prioritize which systems to scan and attack first? Which data from reconnaissance informs that prioritization?

3. **Technical Foundations**
   - Explain the TCP three‑way handshake in your own words and why a SYN scan can identify open ports without completing the handshake.

4. **Network Design**
   - How does NAT allow many devices to share a single IPv4 address? What security advantages and disadvantages does NAT introduce?

5. **Scripting & Automation**
   - When would you prefer a custom Python script or bash script over off‑the‑shelf tools? Describe a small automation that would speed up a repetitive pentesting task you’ve had to do.

6. **Credential Use**
   - Compare credential stuffing and password spraying. What defensive controls can prevent each technique from succeeding at an organization?

7. **Privilege Escalation Mindset**
   - Suppose you have a low-privilege shell on a Linux host. Outline three distinct categories of escalation techniques you would check immediately (e.g., sudo misconfigs, SUID binaries, cron jobs). Why those first?

8. **Reporting & Communication**
   - How would you explain a high-severity vulnerability (e.g., RCE found in a public web page) to a non-technical executive in a debrief? What are the key points to include?

9. **Tool Selection**
   - When should you use an automated scanner (Nessus / Nikto) and when should you perform manual probing with nmap + grep + custom scripts?

10. **Learning & Career**
    - Which one non-technical skill (from Heath’s list) do you think is most important to develop first — and what practical daily habit would help build it?

---

## 5) Quick Practical Study Plan (to apply fundamentals)

- Week 1: Tools & notes  
  - Set up Kali VM + a Windows VM.  
  - Install KeepNote / CherryTree & Greenshot.  
  - Practice taking notes and screenshots for a small lab.

- Week 2: Networking & scanning  
  - Rewatch subnetting and OSI; practice `ip a`, `arp-scan`, `netdiscover`.  
  - Run `nmap -T4 -p- -A <vm>`; review results and practice identifying services.

- Week 3: Web enumeration & Burp  
  - Learn `ffuf`/`dirb`; use Burp Repeater & Intruder on a local web app.  
  - Practice LFI/dir traversal discoveries on a test app.

- Week 4: Exploitation basics & scripting  
  - Create a simple bash ping sweeper and a small Python port scanner.  
  - Try an exploit in a lab (metasploit + manual).

- Ongoing: OSINT & credentials  
  - Practice email discovery tools and check breach data for a personal test domain.  
  - Learn `hashcat` basics and practice cracking hashes on GPU or in cloud if available.

---

## 6) Final Practical Tips (from the transcription)
- Always take structured notes with screenshots and IPs included.
- Use VMs for labs and keep snapshots before tests.
- Start recon and scanning as early tasks — run scans and use the time while they run to do OSINT, credential checks, and research.
- When an automated exploit fails, examine the payload type (staged vs non‑staged) and try the other.
- Be persistent — many real-world compromises come after long, persistent research and pivots.
- Give back to community (blog, GitHub, Twitter) — it helps your career.
- Practice ethical behavior — only attack permitted targets.

---

If you want, I can:
- Produce a compact one-page cheat sheet in Markdown with commands for the core tools (nmap, netdiscover, nikto, hydra, ffuf, linpeas, winpeas, msfconsole).
- Convert the Concept Mind Map into a printable visual (SVG/PNG).
- Generate a short checklist template for an initial external pentest reconnaissance/scanning phase.

Which would you prefer next?