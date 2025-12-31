import hashlib
import os
import time

def calculate_sha256(filepath):
    hasher = hashlib.sha256()
    with open(filepath, 'rb') as f:
        while chunk := f.read(8192):
            hasher.update(chunk)
    return hasher.hexdigest()

def monitor_file(target_file):
    print(f"--- Monitoring: {target_file} ---")
    last_hash = calculate_sha256(target_file)
    try:
        while True:
            time.sleep(5)
            current_hash = calculate_sha256(target_file)
            if current_hash != last_hash:
                print(f"[!] ALERT: File modified at {time.ctime()}")
                last_hash = current_hash
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
  
