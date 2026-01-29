import time
import json
import hashlib
import os
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import requests

# =====================================================
# CONFIGURATION SECTION
# =====================================================

# File that stores original trusted file hashes (baseline)
BASELINE_FILE = "baseline.json"

# Log file where all security events will be stored
LOG_FILE = "integrity.log"

# Folder we want to protect and monitor
MONITOR_FOLDER = "./monitor"

DISCORD_WEBHOOK_URL = "https://discord.com/api/webhooks/1463261712416378943/EXD0CrtFVeNJolEMUBDSLhZthxmjbxO2L5vAMNamCnp9E0XdMAQ55XYQFFh0SYt0qlD9"
# =====================================================
# LOGGING SETUP (professional security style)
# =====================================================

# Logs will be saved to integrity.log with timestamp + severity
logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
)

# Also show logs in terminal (useful while testing)
console = logging.StreamHandler()
console.setLevel(logging.INFO)
logging.getLogger("").addHandler(console)


# =====================================================
# LOAD BASELINE HASHES
# =====================================================

# Baseline contains trusted hash of each file
# Example:
# { "./monitor/file.txt": "abc123hash..." }

with open(BASELINE_FILE) as f:
    baseline = json.load(f)


# =====================================================
# HASH FUNCTION (file fingerprint)
# =====================================================

def hash_file(path):
    """
    Reads a file and returns its SHA256 hash.

    Why chunk reading?
    → prevents memory issues for large files
    """

    sha256 = hashlib.sha256()

    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)

    return sha256.hexdigest()


# =====================================================
# FILE EVENT HANDLER (brain of the system)
# =====================================================

class IntegrityHandler(FileSystemEventHandler):
    """
    This class reacts whenever:
    - file is modified
    - file is created
    - file is deleted
    """

    def on_modified(self, event):
        """
        Triggered when a file changes
        """

        # Ignore folder changes (we only care about files)
        if event.is_directory:
            return

        path = event.src_path

        # If file didn't exist in baseline → suspicious new file
        if path not in baseline:
            logging.warning(f"📂 NEW FILE detected: {path}")
            return

        # Recalculate file hash
        new_hash = hash_file(path)

        # Compare with trusted baseline hash
        if new_hash != baseline[path]:
            logging.critical(f"📂 FILE MODIFIED: {path}")
        else:
            logging.info(f"📂 File accessed but unchanged: {path}")

    def on_deleted(self, event):
        """
        Triggered when a file is removed
        """
        if event.is_directory:
            return

        logging.critical(f"📂 FILE DELETED: {event.src_path}")
        send_discord_alert(f"📂 FILE DELETED: `{event.src_path}`")

    def on_created(self, event):
        """
        Triggered when a new file appears
        """
        if event.is_directory:
            return

        logging.warning(f"📂 NEW FILE created: {event.src_path}")
        send_discord_alert(f"📂 NEW FILE created : `{event.src_path}`")

# =====================================================
# Alert function
# =====================================================
def send_discord_alert(message):
    """
    Sends alert message to Discord channel using webhook
    """

    data = {
        "content": f"🚨 **File Integrity Alert** 🚨\n{message}"
    }

    try:
        requests.post(DISCORD_WEBHOOK_URL, json=data, timeout=5)
    except Exception as e:
        logging.error(f"Discord alert failed: {e}")

# =====================================================
# START REAL-TIME MONITORING
# =====================================================

observer = Observer()

# Attach our handler to the folder
observer.schedule(
    IntegrityHandler(),
    path=MONITOR_FOLDER,
    recursive=True
)

observer.start()

logging.info("File Integrity Monitor started...")


# =====================================================
# KEEP PROGRAM RUNNING
# =====================================================

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    logging.info("Stopping monitor...")
    observer.stop()

observer.join()