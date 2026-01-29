import hashlib
import json
import os

FOLDER_TO_MONITOR = "./monitor"

def hash_file(path):
    sha256 = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            sha256.update(chunk)
        return sha256.hexdigest()
    
baseline = {}

for root, dirs, files in os.walk(FOLDER_TO_MONITOR):
    for file in files:
        filepath = os.path.join(root, file)
        baseline[filepath] = hash_file(filepath)

with open("baseline.json", "w") as f:
    json.dump(baseline, f, indent=4)

print("Baseline created!")