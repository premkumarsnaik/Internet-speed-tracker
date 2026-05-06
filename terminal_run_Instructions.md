# 🚀 Internet Speed Tracker

A Python-based automation tool designed to monitor and log local network performance (Download, Upload, and Latency) directly to a CSV file.

---

## 📋 1. Prerequisites & Environment Check

Before running the project, verify that your system has the correct tools installed.

| Command | Purpose |
|--------|--------|
| `python3 --version` | Ensures Python 3.x is installed |
| `git --version` | Ensures Git is installed |

---

## 🛠 2. First-Time Setup (Local Machine)

If you are starting on a new computer, follow these steps:

### Clone the Repository

    git clone https://github.com/premkumarsnaik/Internet-speed-tracker.git
    cd Internet-speed-tracker

### Create Virtual Environment

    python3 -m venv .venv

### Activate Environment & Install Dependencies

    source .venv/bin/activate
    python3 setup.py

---

## 🔄 3. Synchronizing Code (GitHub ↔ Local)

### Pull (GitHub → Local)

    git pull origin main

### Push (Local → GitHub)

    git add tracker.py speedtest_log.csv
    git commit -m "Update tracker settings and upload latest logs"
    git push origin main

---

## 🏃 4. Execution Workflow

### Navigate & Activate

    cd Internet-speed-tracker
    source .venv/bin/activate

### Run Tracker

    python3 tracker.py

### Stop Tracker

Press:

    Ctrl + C

---

## 📊 5. Data Management

### View Live Logs

    tail -f speedtest_log.csv

### Open Folder (macOS)

    open .

### Clear Logs

    rm speedtest_log.csv

---

## ⚠️ 6. Troubleshooting

### HTTP 403 (Forbidden)
- Happens when tests are too frequent  
- Script handles this using server rotation + persistent client  

### Virtual Environment Issue
Make sure environment is active:

    source .venv/bin/activate

You should see:

    (.venv)

### Merge Conflict Fix

    git reset --hard origin/main

---

## 📁 7. File Structure

- `tracker.py` → Core script  
- `setup.py` → Installs dependencies  
- `speedtest_log.csv` → Output log file  
- `.venv/` → Virtual environment (ignored in Git)  
- `.gitignore` → Prevents unnecessary uploads  

---

## 💡 8. Key Logic Explanation

### Persistent Client
Reuses a single Speedtest instance to avoid being flagged as a bot.

### Server Rotation
Switches between top 5 nearest servers every 30 seconds to prevent rate limiting.

### Dynamic Timing
Adjusts sleep time based on execution duration to maintain consistent intervals.

---
