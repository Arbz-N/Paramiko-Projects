import paramiko
import schedule
import os
from dotenv import load_dotenv
from time import sleep

load_dotenv()


hostname = os.getenv("HOST_NAME")        # e.g. 192.168.1.10
username = os.getenv("SSH_USERNAME")     # e.g. ubuntu, ec2-user
keyPath = "PATH/TO/YOUR/PRIVATE_KEY.pem" # e.g. C:/keys/server-key.pem
# ============================================

csv_file = "daily_memory_logs.csv"


def get_memory_usage():
    try:
        client = paramiko.SSHClient()
        client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        key = paramiko.RSAKey.from_private_key_file(keyPath)
        client.connect(
            hostname=hostname,
            username=username,
            pkey=key,
            timeout=10
        )

        # Commands
        total_cmd = "free -m | grep Mem | awk '{print $2}'"
        used_cmd  = "free -m | grep Mem | awk '{print $3}'"
        free_cmd  = "free -m | grep Mem | awk '{print $4}'"

        # Execute commands
        _, stdout1, _ = client.exec_command(total_cmd)
        _, stdout2, _ = client.exec_command(used_cmd)
        _, stdout3, _ = client.exec_command(free_cmd)

        # Read outputs
        total = stdout1.read().decode().strip()
        used  = stdout2.read().decode().strip()
        free  = stdout3.read().decode().strip()

        # Save to log
        with open(csv_file, "a") as f:
            f.write(f"Hostname: {hostname}\n")
            f.write(f"Total Memory (MB): {total}\n")
            f.write(f"Used Memory (MB): {used}\n")
            f.write(f"Free Memory (MB): {free}\n")
            f.write("-" * 30 + "\n")

        print("Memory usage logged successfully.")
        client.close()

    except Exception as e:
        print("Error:", e)


# Run every minute (change as needed)
schedule.every().minute.do(get_memory_usage)
print("Scheduler running. Waiting for next task...")
while True:
    schedule.run_pending()
    sleep(1)
