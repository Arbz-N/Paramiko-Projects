# Remote Memory Usage Monitoring via SSH

## Overview
This project is a Python-based automation tool that connects to a remote Linux server using SSH and monitors system memory usage.
It collects total, used, and free memory statistics and logs them into a file at regular intervals. 
The solution is designed for system administrators, DevOps engineers, and learners who want a simple yet effective way to track server performance over time.

---

## Features
- Secure SSH connection using key-based authentication  
- Fetches real-time memory usage from a remote server  
- Logs data with timestamps for historical analysis  
- Fully automated using a scheduler  
- Easy configuration using environment variables  

---

## Prerequisites
Make sure you have the following installed:

- Python **3.8+**
- SSH access to a remote Linux server
- Required Python libraries:
  - `paramiko`
  - `python-dotenv`
  - `schedule`

Install dependencies using:

```bash
pip install paramiko python-dotenv schedule


Installation

    Clone the repository
    git clone https://github.com/your-username/remote-memory-monitor.git
    cd remote-memory-monitor


Create a .env file

    HOST_NAME=your_server_ip_or_hostname
    SSH_USERNAME=your_ssh_username


    Set private key path
    Update this line in the script:

    keyPath = "PATH/TO/YOUR/PRIVATE_KEY.pem"


    Secure your files
    Add this to .gitignore:
    
    .env
    *.pem

    Usage
    
    Run the script using:
    script.py


The program will:

    Connect to the remote server every minute
    Fetch memory statistics
    Save them in daily_memory_logs.csv
    
You can change the schedule timing here:
    schedule.every().minute.do(get_memory_usage)
    
    Examples:
    schedule.every().hour.do(get_memory_usage)
    schedule.every(10).minutes.do(get_memory_usage)

Project Explanation
    How it works
    Load Configuration
    Reads hostname and username from .env file.
    Establish SSH Connection
    Uses Paramiko with RSA private key authentication.
    Execute Remote Commands
    Runs Linux commands:
    free -m → fetch memory stats
    awk → extract required values
    Process Data
    Parses total, used, and free memory values.
    Log Results
    Writes data into a log file with timestamps.
    Automation
    Uses schedule library to repeat the task automatically.
    
Sample Log Output
    Timestamp: 2026-01-12 22:10:01
    Hostname: my-server
    Total Memory (MB): 7980
    Used Memory (MB): 3120
    Free Memory (MB): 4860
    ------------------------------