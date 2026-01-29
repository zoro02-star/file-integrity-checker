# Real-Time File Integrity Checker (Python)

## Introduction

This project demonstrates a **real-time File Integrity Monitoring (FIM)** system built using Python. Instead of scanning files occasionally, it continuously watches the filesystem and alerts instantly when suspicious changes occur.

This blog explains:

* What the tool does (features)
* How to use it step by step
* How to monitor multiple folders
* How to run it 24/7 using cron or system startup

(No code deep-dive — focus is on usage and security concepts.)

---

## Key Features of This Project

### 🔍 Real-Time Monitoring

* Watches files continuously using OS-level filesystem events
* No waiting for periodic scans

### 🔐 Cryptographic Verification

* Uses secure hashing (SHA-256)
* Even a one-character change is detected

### 📦 Baseline-Based Trust Model

* Establishes a known-good state of files
* All future changes are compared against this baseline

### 🚨 Instant Alerts (Discord)

* Sends alerts immediately to a Discord channel
* Ideal for SOC-style monitoring or personal servers

### 🧾 Professional Logging

* Maintains a permanent log file
* Useful for audits, investigations, and incident timelines

---



## Project Workflow (High-Level)

1. Select folders to protect
2. Create a baseline (trusted snapshot)
3. Start the real-time watcher
4. Receive alerts when changes occur
5. Review logs for forensic analysis

---

## Step-by-Step Usage Guide

### 1️⃣ Choose Folders to Monitor

Decide which folders are **security-sensitive**, for example:

* Application config directories
* Script folders
* Deployment directories

Avoid volatile paths like:

* Log directories
* Cache or temp folders

---

### 2️⃣ Create the Baseline (One-Time Step)

The baseline represents a **clean and trusted state**.

Important security rule:

> Only create the baseline when you are 100% sure the system is clean.

This snapshot is later used to detect tampering.

---

### 3️⃣ Start Real-Time Monitoring

Once the baseline exists, start the watcher process.

From this moment:

* File modifications are detected instantly
* New or deleted files raise alerts
* All events are logged

This simulates how professional host-based security tools operate.

---

## Monitoring Multiple Folders

You can monitor **multiple folders** in two common ways:

### Option 1: Multiple Watch Paths

* Add several directories to the monitoring list
* Each directory is watched recursively

### Option 2: Parent Directory Strategy

* Place all critical folders under one parent directory
* Monitor the parent directory recursively

Security tip:

> Fewer, well-chosen directories = fewer false alerts

---

## Running the Tool 24/7 on a Server

For real security value, the monitor must run continuously.

### Why 24/7 Execution Matters

* Attacks do not follow schedules
* Detection delays reduce response time
* Continuous monitoring reduces blind spots

---

## Running with Cron (Linux)

Cron is useful if you want:

* Automatic startup after reboot
* Periodic execution (fallback scan)

Common approaches:

* Use cron to start the watcher at boot
* Use cron as a watchdog to ensure it’s running

Example use cases:

* Personal VPS
* Lightweight servers

---

## Alternative: Run as a System Service (Recommended)

For production-like setups:

* Configure the tool as a system service
* Starts automatically on boot
* Restarts if it crashes
* Runs silently in background

This is how real security agents operate.

---

## Logs and Alerts

### Log File

The log file acts as:

* An audit trail
* Incident timeline
* Forensic evidence

It records:

* Timestamp
* Event severity
* File path

### Discord Alerts

Discord alerts provide:

* Instant notification
* Remote visibility
* Lightweight SOC-style monitoring

---

## Security Best Practices

* Protect the baseline file from modification
* Store logs in restricted directories
* Use alert rate-limiting to avoid spam
* Combine with periodic scans for defense-in-depth

---

## Limitations (Honest Engineering)

* Cannot detect in-memory attacks
* Requires secure baseline creation
* Alerts may increase for frequently changing files

These are expected trade-offs for host-based monitoring.

---

## Learning Outcomes

By building and using this project, you learn:

* File integrity concepts
* Host-based intrusion detection
* Real-time security monitoring
* Alerting and logging fundamentals

These are **core security engineering skills**.

---

## Conclusion

This File Integrity Checker demonstrates how professional security tools think:

> Establish trust → Monitor continuously → Alert immediately → Preserve evidence

It’s a strong foundation for building advanced security systems such as:

* HIDS
* Endpoint Detection tools
* Compliance monitoring agents

---

*Next improvements could include log rotation, alert throttling, secure baseline protection, or a dashboard.*
