# 🔍 NetPulse Listener: Turn the Tables on Network Probes  

The internet is full of **bots, scanners, and malicious actors** constantly probing for open ports, weak services, and exploitable systems. If you've ever checked your server logs, you've probably seen random connection attempts from unfamiliar IPs trying to access endpoints that don’t even exist.  

But what if, instead of ignoring them, you could **turn the tables**—capturing their browser details, logging their IPs, and gathering intelligence on who's probing your network?  

That’s exactly what **NetPulse Listener** does. It’s a **lightweight, no-fuss TCP listener** designed to trap attackers, log their details, and give you full visibility into who’s poking around.  

---

## 🚨 The Problem: Blind Spots in Network Security  

Most people assume that unless they’re running a public-facing website, their network isn’t being scanned. **The truth?** Bots and attackers are constantly scanning open IPs, looking for services to exploit.  

Even a simple **home server, Raspberry Pi, or IoT device** can be an entry point for attackers. But traditional firewalls and IDS (Intrusion Detection Systems) only tell you **something happened**—they don’t show you **who’s behind it**.  

That’s where **NetPulse Listener** comes in.  

---

## 🛠 The Solution: NetPulse Listener  

**NetPulse Listener** is a **stealthy honeypot** that listens for incoming connections on a chosen port. Instead of just rejecting requests, it records the attacker's details, including:  

- **IP Address**  
- **User-Agent** (reveals their browser & OS)  
- **Full request headers** (sometimes containing extra metadata)  
- **Timestamp of the attempt**  

If they’re using a browser, the script can even **fingerprint their system**.  

And here’s the best part: **Instead of revealing any useful information, NetPulse Listener sends a fake response, tricking the attacker** into thinking they’ve found a real service—while in reality, they’re just giving away their details.  

---

## 🔎 How It Works  

1. **Run NetPulse Listener** on any machine—it opens a port and waits for incoming connections.  
2. **An attacker (or bot) scans your network**, detecting the open port and attempting to connect.  
3. **NetPulse Listener captures everything**, logging the attacker’s request details.  
4. **The attacker gets tricked**—instead of real data, they receive a misleading response.  

---

## 📌 A Real-World Example  

Say an attacker is scanning your network, looking for a misconfigured web server. They connect to **port 8080**.  

Without NetPulse Listener, you’d never know they were there. **But with it, here’s what happens instead:**  

✅ **Their IP gets logged** – Now you know where the scan is coming from.  
✅ **Their user-agent gets captured** – See if they’re using a bot, a Linux command-line scanner, or a regular browser.  
✅ **Their request headers reveal more info** – Attackers often leave identifiable fingerprints.  
✅ **They receive a deceptive response** – The script tricks them into thinking they’ve found something real.  

This isn’t just a passive tool—it’s an **active intelligence-gathering honeypot**.  

---

# 🚀 The New Update – Making It Even More Powerful  

Now that NetPulse Listener has been tested in real-world use, I wanted to improve it even further. This update adds **major enhancements** that make it a more effective honeypot while keeping it **lightweight and easy to use**.  

### 🎨 **What’s New?**  

### 1️⃣ Custom ASCII Art Banner for Instant Recognition  
When you launch the script, it now greets you with a **clear, professional-looking ASCII banner**. This **looks awesome** and ensures you immediately know the script is running.  

### 2️⃣ Color-Coded Output for Easy Monitoring  
Reading logs in plain text is **boring and inefficient**. Now, the output is **color-coded**:  

- 🔴 **Red** for errors  
- 🟢 **Green** for successful logs  
- 🔵 **Blue** for informational messages  

This makes it easier to **spot important events** at a glance.  

### 3️⃣ Automatic Logging of All Attacks  
Before, you had to manually check the console for connections. Now, **every incoming request is logged to a file** with timestamps for later analysis.  

📌 **Example log entry:**  
```
[2025-04-04 13:45:20] Connection from 192.168.1.50  
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64)  
Headers: GET / HTTP/1.1  
Host: 192.168.1.100  
Connection: keep-alive  
```

Now you can analyze trends—**where are most attackers coming from? What tools are they using?**  

### 4️⃣ Improved Fake Response System  
To keep attackers **engaged**, the script now **dynamically generates misleading responses** to make it look like they’ve found a real service. This **increases the chance they’ll stay connected long enough** for you to gather more intelligence.  

---

## 🏗 How to Use It  

### ▶️ **Run the Script**  
To start listening on a port (e.g., 8080), simply run:  

```bash
python netpulse.py -p 8080
```

By default, the script **exits with a red message once a user falls for the trap**. If you want to keep it running continuously, use the **-c flag**:  

```bash
python netpulse.py -p 8080 -c
```

### 🎭 **Customize the Response**  
By default, NetPulse Listener sends a simple text response:  
*"NetPulse Listener works!"*  

But you can provide **your own response file**:  

```bash
python netpulse.py -r fake_response.txt
```

---

## 📊 Summary  

NetPulse Listener helps you:  

✔ **Detect malicious activity** before it becomes a real threat.  
✔ **Gather intelligence** on attackers and their tools.  
✔ **Create a deceptive honeypot** to waste attackers' time.  
✔ **Log suspicious requests** for later analysis.  

Unlike traditional security tools, **NetPulse Listener is lightweight and easy to deploy**. It requires:  

- **No configuration**  
- **No dependencies**  
- **Runs on any system with Python**  

---

## 🔥 Final Thoughts  

Most security tools focus on **blocking threats**. **NetPulse Listener takes a different approach**: it **studies them**.  

Instead of blindly shutting out attackers, it **collects valuable data**, helping you understand **who’s targeting your network**.  

This update makes it **smarter, more effective, and easier to use**. If you’ve ever wanted a **simple honeypot that provides real insights, this is it**.  

### 💬 I’d love to hear your thoughts!  
Let me know if you try it out and share any logs or findings—this tool is only going to get better with community feedback.  

🔒 **Stay safe, and happy hacking.** 🚀  
