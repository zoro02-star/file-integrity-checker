remeber to install all libraries using:
npm install

🔗 Step 1 – Add Your Discord Webhook
Open watcher.py and find the configuration section near the top

You will see something like:
DISCORD_WEBHOOK_URL = "YOUR_WEBHOOK_URL_HERE"

Replace it with your real webhook URL from Discord:
DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/xxxxx/yyyyy"
Save the file.

📂 Step 2 – Put Files to Protect
Move or create files inside the monitor/ folder.

Example:
monitor/
  config.txt
  script.sh
  secrets.json

Only files inside this folder will be monitored.

📸 Step 3 – Create Baseline (IMPORTANT)

Run once:

python3 baseline_create.py

This creates the trusted fingerprint snapshot.

Step 4 - Start Real-Time Monitoring
python3 watcher.py
you should see :
File Integrity Monitor started...

Options:
to run in background:
nohup python3 watcher.py &

Auto Start on Reboot(Cron):
crontab -e
@reboot python3 /full/path/to/watcher.py

✅ That’s it

Your system now has:

• Real-time file monitoring • Tamper detection • Discord alerts • Forensic logging • 24/7 operation

