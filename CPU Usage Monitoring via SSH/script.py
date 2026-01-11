import paramiko
import os
from dotenv import load_dotenv
import csv
from datetime import datetime
import schedule
import time

load_dotenv()

# ====== PLACEHOLDERS FOR SENSITIVE DATA ======
hostName = os.getenv("HOST_NAME")        # e.g. 192.168.1.10 or ec2-xx-xx.compute.amazonaws.com
userName = os.getenv("SSH_USERNAME")     # e.g. ubuntu, ec2-user
keyPath = "PATH/TO/YOUR/PRIVATE_KEY.pem" # e.g. C:/keys/server-key.pem
csv_file = "cpu_usage_logs.csv"
# ============================================

def fetch_cpu_usage():
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    try:
        print(f"Connecting to {hostName} at {timestamp}...")
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        key = paramiko.RSAKey.from_private_key_file(keyPath)
        client.connect(
            hostname=hostName,
            username=userName,
            pkey=key,
            timeout=10
        )

        print("SSH Connected Successfully!")

        process = (
            "ps aux --sort=-%cpu | head -n 6 | "
            "awk '{print NR \",\" $1,$2,$3,$4,$11}' | "
            "sed -E 's/ +/,/g'"
        )

        stdin, stdout, stderr = client.exec_command(process)
        output = stdout.read().decode()
        error = stderr.read().decode()

        if error:
            print("Error:\n", error)

        # CSV Logging
        with open(csv_file, "a", newline='') as file:
            writer = csv.writer(file)

            # Add timestamp row
            writer.writerow([f"Timestamp: {timestamp}"])

            # Add CPU usage rows
            for line in output.splitlines():
                if line.strip():
                    writer.writerow(line.split(','))

        print(f"Data saved to {csv_file}\n")
        client.close()

    except Exception as e:
        print("Connection Failed:", e)


# Run every 5 minutes
schedule.every(5).minutes.do(fetch_cpu_usage)

print("Scheduler started... Press Ctrl+C to stop")
while True:
    schedule.run_pending()
    time.sleep(1)
