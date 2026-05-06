# 🚀 Internet Speed Tracker

A Python-based automation tool designed to monitor and log local network performance (Download, Upload, and Latency) directly to a CSV file.

---

## 📋 1. Prerequisites & Environment Check
Before running the project, verify that your system has the correct tools installed.

| Command | Purpose |
| :--- | :--- |
| `python3 --version` | Ensures Python 3.x is installed |
| `git --version` | Ensures Git is installed for syncing |

---

## 🛠 2. First-Time Setup (Local Machine)
If you are starting on a new computer, follow these steps to prepare the environment:

### Clone the Repo
```bash
git clone https://github.com/premkumarsnaik/Internet-speed-tracker.git
cd Internet-speed-tracker
Create Virtual Environment

(Essential on macOS to avoid "Externally Managed Environment" errors)

python3 -m venv .venv
Activate & Install Dependencies
source .venv/bin/activate
python3 setup.py


🔄 3. Synchronizing Code (GitHub ↔ Local)
A. Pulling (GitHub Web → Local Machine)

If you edited code on GitHub and want it locally:

git pull origin main
B. Pushing (Local Machine → GitHub Web)

To upload latest script or logs:

git add tracker.py speedtest_log.csv
git commit -m "Update tracker settings and upload latest logs"
git push origin main


🏃 4. Execution Workflow
Navigate & Activate
cd Internet-speed-tracker
source .venv/bin/activate
Launch Tracker
python3 tracker.py
Stop Tracker

Press:

Ctrl + C


📊 5. Data Management
View Live Updates
tail -f speedtest_log.csv
Open in Finder (macOS)
open .
Clear Log Data
rm speedtest_log.csv


⚠️ 6. Troubleshooting
HTTP 403 (Forbidden)

Occurs when testing too frequently.
Solution: Script uses server rotation and a persistent client to reduce this.

Virtual Environment Issues

If you see command not found, ensure:

source .venv/bin/activate

Your prompt should show:

(.venv)
Merge Conflicts

Force overwrite local changes with GitHub version:

git reset --hard origin/main


📁 7. File Structure
tracker.py → Core Python automation script
setup.py → Installs dependencies (e.g., speedtest-cli)
speedtest_log.csv → Generated performance logs
.venv/ → Virtual environment (ignored by Git)
.gitignore → Prevents unnecessary files from being uploaded


💡 8. Key Logic Explanation
Persistent Client

Initializes the Speedtest client once and reuses it to avoid being flagged as a bot.

Server Rotation

Every 30 seconds, selects randomly from the top 5 nearest servers to avoid rate-limiting (403 errors).

Dynamic Timing

Adjusts sleep interval by subtracting execution time, ensuring consistent logging intervals.
