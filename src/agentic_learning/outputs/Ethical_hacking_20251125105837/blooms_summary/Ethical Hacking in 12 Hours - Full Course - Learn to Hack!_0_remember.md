# Practical Ethical Hacking – Memory Aids (Mnemonics, Flashcards, Stories, Acronyms)

Below are custom **mnemonics, flashcards, vivid stories, and acronyms** to help you remember the *subject properties* and big concepts from Practical Ethical Hacking: methodology, networking, tools, shells/payloads, privilege escalation, soft skills, and note‑keeping.

---

## 1. Big Picture Mnemonics

### 1.1 Five Stages of Ethical Hacking

**Stages:**  
Reconnaissance → Scanning & Enumeration → Exploitation → Maintaining Access → Covering Tracks

**Mnemonic:**  
> **R**accoons **S**can **E**very **M**eal **C**arefully

- **R**accoons → **R**econ (Information Gathering)  
- **S**can → **S**canning & **E**numeration  
- **E**very → **E**xploitation  
- **M**eal → **M**aintaining Access  
- **C**arefully → **C**overing Tracks

**Key “Properties” of Each Stage**

- **Recon**: Passive, OSINT, social media, subdomains, email patterns.
- **Scan/Enum**: Active, ports/services, versions, dir busting, auth checks.
- **Exploit**: Use vuln → shell (low or high privilege).
- **Maintain**: Persistence, pivoting, further movement.
- **Cover/Clean**: Remove backdoors/accounts, logs (for real attackers), cleanup (for ethical hackers).

---

### 1.2 Day-in-the-Life Assessment Types

**Common Engagement Types:**  
External, Internal, Web App, Wireless, Physical/Social, Purple Team

**Mnemonic:**  
> **E**very **I**nquisitive **W**easel **W**alks **P**ast **P**eople

- **E**very → **E**xternal Network  
- **I**nquisitive → **I**nternal Network  
- **W**easel → **W**eb Applications  
- **W**alks → **W**ireless  
- **P**ast → **P**hysical / Social Engineering  
- **P**eople → **P**urple teaming (SOC / Red+Blue)

---

### 1.3 Core Technical Foundations (Base Skills)

**Heath’s “Base Must-Haves”:** Linux, Networking, Scripting, Methodology, Tools

**Mnemonic:**  
> **L**ittle **N**injas **S**lice **M**any **T**argets

- **L**ittle → **L**inux (Kali, Parrot)  
- **N**injas → **N**etworking (OSI, TCP/UDP, subnets)  
- **S**lice → **S**cripting (Python, Bash)  
- **M**any → **M**ethodology (5 stages)  
- **T**argets → **T**ools (nmap, Metasploit, Burp, Nessus)

---

### 1.4 Preferred Skills (Bonus, Make You Stand Out)

**Preferred Column:** AD, Wireless, OWASP, Coding

**Mnemonic:**  
> **A**dvanced **W**arriors **O**wn **C**ode

- **A**dvanced → **A**ctive Directory  
- **W**arriors → **W**ireless Attacks  
- **O**wn → **O**WASP Top 10  
- **C**ode → **C**oding (beyond scripting)

---

### 1.5 Soft Skills You Must Grow

Heath emphasized: Desire to Learn, Perseverance, Non‑complacency, Communication, Contribution.

**Mnemonic:**  
> **D**eep **P**ractice **N**ourishes **C**areer **C**lout

- **D**eep → **D**esire to learn (lifelong learning)  
- **P**ractice → **P**erseverance (don’t quit when stuck)  
- **N**ourishes → **N**on‑complacency (never “done”)  
- **C**areer → **C**ommunication (writing & speaking)  
- **C**lout → **C**ommunity contribution (blog, GitHub, Twitter)

---

## 2. Networking & OSI – Memory Aids

### 2.1 OSI Layers

**Mnemonic (Layer 1 to 7):**  
> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way

- **1 – Physical** – cables, bits on wire  
- **2 – Data Link** – switching, MAC addresses  
- **3 – Network** – IP, routing  
- **4 – Transport** – TCP/UDP  
- **5 – Session** – session management  
- **6 – Presentation** – data formats (JPEG, video)  
- **7 – Application** – HTTP, SMTP, etc.

**Troubleshooting Rule:**  
> **P**lug, **P**ing, **P**age  
Start at **Physical** (is it plugged in?) → then **Network/Transport** (IP, ping) → then **Application** (web/app error).

---

### 2.2 TCP vs UDP

**Properties:**  
- **TCP** – Connection-oriented, reliable, handshake, ordered.  
- **UDP** – Connectionless, fast, no handshake, best-effort.

**Mnemonic:**  
> **T**ake **C**areful **P**ackages, **U**nload **D**atagrams **P**rudently

- **T C P** → *Take Careful Packages* (reliable, careful)  
- **U D P** → *Unload Datagrams Prudently* (just tossing packets, faster but no guarantee)

---

### 2.3 Three-Way Handshake

**SYN → SYN/ACK → ACK**

**Mnemonic:**  
> **S**ay **H**i, **H**ear **H**i, **H**andshake

- **SYN** – Say hi  
- **SYN/ACK** – Hear hi and accept  
- **ACK** – Final handshake / start conversation

---

### 2.4 IPv4 Private Ranges (NAT Important Subnets)

**Mnemonic:**  
> **1**0 /8: “**1**0, the Big Corporate Pen”  
> **172**.16 – 172.31 /12: “**172**, the Mid‑size Pen”  
> **192**.168 /16: “**192**, the Home Pen”

**Key Private Ranges:**

- `10.0.0.0 – 10.255.255.255`  
- `172.16.0.0 – 172.31.255.255`  
- `192.168.0.0 – 192.168.255.255`

Remember: anything starting with **192.168** or **10.** is internal/private for almost all home/small office networks.

---

### 2.5 Subnet / CIDR Patterns

**Visual Shortcut:**  
Think of CIDR as how many bits are “fixed for the street” (network) vs “house numbers” (hosts):

- `/24` (255.255.255.0) → **1 street, 256 houses**  
- `/23` (255.255.254.0) → **2 streets merged, 512 houses**  
- `/16` (255.255.0.0) → **256 streets with many houses**

**Mnemonic for Common CIDR/Host Pairs:**

> **24, 254 – “Small Office Floor”**  
> **23, 510 – “Two Floors Combined”**  
> **16, 65,534 – “Giant Corporate Campus”**

Always: **Hosts = 2^(32-CIDR) – 2**

---

## 3. Tools & Methodology – Flashcards

### 3.1 Flashcards: Methodology & Skills

**Card 1**  
Q: What are the 5 stages of ethical hacking?  
A: **Recon → Scanning/Enumeration → Exploitation → Maintaining Access → Covering Tracks**.

---

**Card 2**  
Q: What’s the difference between passive and active recon?  
A: **Passive** uses public info (Google, LinkedIn, OSINT) without touching the target. **Active** interacts directly (scanning, DNS queries to target, dir busting) and can be detected.

---

**Card 3**  
Q: What base technical skills should a junior pentester have?  
A: **Linux**, **networking**, **scripting (Python/Bash)**, **hacking methodology**, and **familiarity with tools** like nmap, Metasploit, Burp, Nessus.

---

**Card 4**  
Q: Why is effective note keeping critical in pentesting?  
A: It captures **commands, outputs, IPs, timestamps, and screenshots**, enabling **accurate reports** and answering client questions months later.

---

**Card 5**  
Q: Name two note-taking tools and one screenshot tool recommended in the course.  
A: Note tools: **KeepNote**, **CherryTree**, **OneNote**, **Joplin**. Screenshot: **GreenShot** (or **FlameShot** on Linux).

---

### 3.2 Flashcards: Networking & System Basics

**Card 6**  
Q: Which OSI layer is responsible for IP addressing and routing?  
A: Layer **3 – Network**.

---

**Card 7**  
Q: Which OSI layer handles TCP/UDP?  
A: Layer **4 – Transport**.

---

**Card 8**  
Q: What is NAT and why is it used?  
A: **Network Address Translation** maps many private IPs to one public IP, allowing multiple devices to share a single public IPv4 address.

---

**Card 9**  
Q: What does `chmod 777 file` do?  
A: Grants **read, write, execute** privileges to **owner, group, and others** (full world access).

---

**Card 10**  
Q: What is an SUID binary and why is it dangerous?  
A: A binary with **set-user-ID** that runs with the file owner’s privileges (often root). If misused, it can give a low-privileged user **root-level execution**.

---

### 3.3 Flashcards: Shells & Payloads

**Card 11**  
Q: What’s the difference between a reverse shell and a bind shell?  
A: **Reverse shell**: target connects back to attacker’s listener.  
**Bind shell**: target opens a port and listens; attacker connects to that port.

---

**Card 12**  
Q: In metasploit, what does a staged payload mean vs non-staged?  
A: **Staged**: payload comes in parts (smaller initial footprint).  
**Non-staged**: full payload sent in one go. Often named with `_` vs `/` in metasploit.

---

**Card 13**  
Q: If a metasploit exploit seems to work but the shell dies immediately, what should you try?  
A: Try changing **payload** – e.g., from **staged to non‑staged** (`reverse_tcp` vs `meterpreter/reverse_tcp`), or switch shell type.

---

### 3.4 Flashcards: Recon & Web Enumeration

**Card 14**  
Q: What tools can you use to discover subdomains?  
A: **sublist3r**, **Amass**, **crt.sh**, Google dorks (`site:*.example.com`).

---

**Card 15**  
Q: What tools identify web tech stack (server, CMS, frameworks)?  
A: **BuiltWith**, **Wappalyzer**, **WhatWeb**.

---

**Card 16**  
Q: What’s directory busting and which tools can perform it?  
A: Brute-forcing hidden web paths using wordlists. Tools: **ffuf**, **dirb**, **dirbuster**.

---

**Card 17**  
Q: What is Burp Suite primarily used for?  
A: It’s a **web proxy** for **intercepting, modifying, and replaying** HTTP/S requests, plus web fuzzing and manual testing.

---

### 3.5 Flashcards: Credentials & OSINT

**Card 18**  
Q: Define credential stuffing vs password spraying in one sentence each.  
A: **Credential stuffing**: using **known username+password pairs** from breaches against a site.  
**Password spraying**: using **one or few passwords** across **many usernames** to avoid lockout.

---

**Card 19**  
Q: Name three email/OSINT tools and their main use.  
A: **Hunter.io** (discover pattern & emails), **Phonebook.cz** (bulk email discovery), **Clearbit** (people search & enrichment inside email client).

---

**Card 20**  
Q: What is Dehashed used for?  
A: Searching **breach data** (emails, usernames, hashes, etc.) to find leaked credentials and tie accounts together.

---

## 4. Vivid Stories (to cement concepts)

### 4.1 Story: The Ethical Burglar’s Day

Imagine you’re **Alex**, an ethical burglar hired to test a skyscraper’s security.

1. **Reconnaissance – “From the Park with Binoculars”**  
   You spend a day in the park **watching the building**. You note:
   - Where employees enter.
   - Badges hanging off belts.
   - People posting selfies with their badges on LinkedIn.
   - A map on the corporate website showing three offices you didn’t know existed.  
   This is **OSINT** — everything you can see **without touching** the building.

2. **Scanning & Enumeration – “Walking the Perimeter”**  
   At night, you walk around the block:
   - You tap on doors and windows (nmap), looking for **unlocked ones** (open ports).  
   - You find:
     - A side door (port 80) with a keycard reader (Apache server).
     - A back door that looks old and poorly maintained (ancient mod_ssl version).  
   You write down each door, its type, and its condition — that’s **enumeration**.

3. **Exploitation – “Picking the Rusty Lock”**  
   You research rusty locks online and find a specific lockpick pattern for that exact model (`openfuck` or `trans2open`).  
   You apply the pattern on the back door; with a *click*, the door swings open — you’re inside. That’s your **exploit** landing a **shell**.

4. **Post-Exploitation – “Climbing to the Executives’ Floor”**  
   Inside, you’re only at the **reception level** (low-privilege shell). You:
   - Find a cleaning staff elevator key (SUID PHP).  
   - Use it to access **every floor**, including the CEO’s office (root/SYSTEM privilege).  
   You also notice a locked server room door frequently opening at midnight: that’s a **cron job** you might abuse.

5. **Maintaining Access – “Leaving a Spare Badge”**  
   You quietly hide **a second badge** behind a fire extinguisher that allows you back in later — a backdoor/persistence. For the ethical version, you only *document* how you would do this.

6. **Covering Tracks & Debrief – “The Report to the Owner”**  
   You leave everything as you found it:
   - You close the door behind you.
   - Remove any tools you placed.  
   Then you meet with the building owner:
   - Show where each lock failed.
   - Explain how to **fix each lock**.  
   This is **reporting & debrief**.

By mapping every pentest phase to a physical heist metaphor, you can visualize the **properties** of each stage and remember the flow.

---

### 4.2 Story: The “SUID Elevator” Trick

You’re working night shift as a new junior in a company’s office tower. Most floors are locked, accessible only to **root (the CEO)** using a special elevator key.

One night you discover a strange “maintenance elevator button” labeled `php7.3`. You press it and see a note scribbled:  
> “Runs **as CEO** if you know the secret code.”

You enter the secret code: `posix_setuid(0); system("/bin/sh");` and suddenly, the elevator whooshes past all staff levels and **drops you into the CEO’s private office** — no questions asked.  

That **maintenance button** is a **SUID PHP binary** — if someone misconfigures it, any intern (www-data) who finds it can ride it straight to CEO privileges (root shell).

So now, when you see an executable with **SUID root**, picture that **CEO elevator** that can secretly elevate whoever presses the button.

---

### 4.3 Story: The Brute-Force Bouncer vs Credential Stuffing Skimmer

- **Brute-Force Bouncer:**  
  Imagine a nightclub with one bouncer (SSH service). One guy keeps trying different names and birthdays for **one person**:  
  - “John with 1234, 12345, 123456…”  
  That’s brute force; the bouncer gets suspicious and locks John out quickly.

- **Password Spraying:**  
  Now someone tries **the same easy password** for many people:  
  - “John-123456, Mary-123456, Paul-123456…”  
  Only **one guess per person**. Harder to catch — that’s **password spraying**.

- **Credential Stuffing:**  
  Finally, someone finds a wallet full of **valid ID+pin combos** stolen from another nightclub (breach):  
  - “John: 42Blue!”, “Mary: Pa$$w0rd!”, “Tom: Tesla1!”  
  They go to tonight’s club and try each **ID+pin pair** hoping people reused PINs — that’s **credential stuffing**.

Visualizing these patterns helps you recall the **behavioral properties** and the defensive reactions needed (lockouts, MFA, anomaly detection).

---

## 5. Acronyms That Capture Processes & Properties

### 5.1 RECON – What Good Recon Collects

> **R E C O N**

- **R**ecords – DNS records, certificate transparency, WHOIS.  
- **E**mails – patterns & lists from Hunter, Phonebook, Clearbit.  
- **C**redentials – leaked combos from Dehashed, breach-parse, etc.  
- **O**pen hosts – early host discovery hints, hostnames.  
- **N**etwork map – subdomains, IP ranges.

---

### 5.2 SCAN – Enumeration Steps

> **S C A N**

- **S**ervices – enumerate TCP/UDP ports (nmap).  
- **C**onfiguration – versions & banners (WhatWeb, headers).  
- **A**dministrative panels – `/admin`, `/phpmyadmin`, `/jenkins`.  
- **N**ew endpoints – directory busting, API routes.

---

### 5.3 SHELL – Remember Shell Types & Payloads

> **S H E L L**

- **S**taged vs non‑staged (payload behavior)  
- **H**andshake (TCP handshake properties for reverse/bind shells)  
- **E**gress – does reverse shell traffic escape network filters?  
- **L**istener – proper netcat/metasploit listeners correctly configured  
- **L**ocation – which machine will be connecting where (reverse vs bind)?

---

### 5.4 ADAPT – Privilege Escalation Mindset

> **A D A P T**

- **A**udit – run linPEAS/winPEAS, manual checks.  
- **D**iscover – misconfigs: sudo no-password, SUID, cron jobs, unquoted paths.  
- **A**ssess – which escalation path is safest/reliable?  
- **P**roof – verify shell as root/SYSTEM with screenshots.  
- **T**idy up – remove test files, document clearly for the report.

---

## 6. Mini “Scenario” Flashcards (Exploit Chains)

These are chained scenarios that highlight **properties** of multi-step attacks.

---

**Scenario Card A – Linux Web Exploit (Academy Machine)**

- **1. Recon:**  
  `ftp` allows anonymous login → `note.txt` reveals MD5 hashed password & SQL insert syntax.
- **2. Analysis:**  
  Identify hash as MD5 → `hashcat -m 0` + `rockyou.txt` → crack to `student`.
- **3. Web Login:**  
  Use `reg_no` from note + `student` on `/academy` login form.
- **4. File Upload RCE:**  
  “Upload photo” → upload `php-reverse-shell.php`.  
  Trigger via URL → reverse shell as `www-data`.
- **5. PrivEsc:**  
  `linpeas.sh` → finds cron/backup script running as root.  
  Modify `backup.sh` to include bash reverse shell.  
  Wait for cron → root shell.

*Main properties to remember: FTP leak → hash cracking → web auth → upload → cron job abuse.*

---

**Scenario Card B – Windows Jenkins & Unquoted Path (Butler)**

- **1. Recon:**  
  Jenkins on `:8080`. No default creds, login required.
- **2. Credential Guessing:**  
  Burp Intruder tries username/password combos.  
  `jenkins:jenkins` stands out by different response length → valid login.
- **3. RCE:**  
  Use Jenkins script console → Groovy reverse shell → shell as `butler`.
- **4. PrivEsc Audit:**  
  Run `winPEAS.exe` → find WiseBootAssistant unquoted service path under `C:\Program Files (x86)\Wise\Wise Care 365\BootTime.exe`.
- **5. Exploit Unquoted Path:**  
  Create `Wise.exe` via `msfvenom` (reverse shell payload).  
  Place in `C:\Program Files (x86)\Wise\`.  
  Stop & start service → service runs `Wise.exe` as SYSTEM → SYSTEM shell.

*Properties: Auth regen via subtle length diff → script console as RCE → unquoted path as classic Windows priv‑esc vector.*

---

## 7. Ultra-Condensed “Memory Grid” (for quick recall)

| Area                | 1-line Property Summary                                                | Memory Hook                           |
|---------------------|-------------------------------------------------------------------------|----------------------------------------|
| Methodology         | 5 repeatable phases, from info-gathering to cleanup                    | Raccoons Scan Every Meal Carefully    |
| Recon               | Passive info without touching target directly                          | RECON: Records, Emails, Creds, Open hosts, Network map |
| Scanning/Enum       | Active probing: ports, services, dirs, vulns                           | SCAN: Services, Config, Admin, New endpoints |
| Exploitation        | Turn a vuln into a shell (reverse/bind), pick correct payload type     | SHELL mnemonic                         |
| Post-Exploitation   | Escalate privileges, gather more info, maintain/persist, then clean    | ADAPT mnemonic                         |
| OSI Model           | L1–L7 stack to categorize issues & protocols                           | Please Do Not Throw Sausage Pizza Away |
| Subnetting          | CIDR defines network vs hosts; /24 = 254 hosts, /16 huge networks      | Floors & apartments analogy            |
| NAT                 | Maps many private IPs to one public; common on home routers            | Family sharing one mailbox             |
| Shells              | Reverse vs bind indicates who connects to whom                         | Victim calls vs attacker calls         |
| SUID/Unquoted Path  | Run code as owner/service account; dangerous if misconfigured          | CEO elevator & WiseCare boot path     |
| OSINT & Credentials | Public info & breach data combine to reveal emails, passwords & links  | Forget-Password link, Dehashed, Hunter |

---

Use these mnemonics, flashcards, stories, and acronyms as **anchors**: when you see a tool or situation (e.g., unquoted service, SUID, Jenkins, FTP leak), recall its story or acronym and let that guide your reasoning and next steps.