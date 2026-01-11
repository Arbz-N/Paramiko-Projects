# CPU Usage Monitoring via SSH

## Overview
This project allows you to monitor CPU usage on a remote server over SSH and log the data into a CSV file. Using Python and Paramiko, it connects securely to the server, fetches the top CPU-consuming processes, and maintains historical logs for analysis. The scheduler ensures that monitoring happens automatically at regular intervals, making it ideal for system administrators and DevOps engineers to track server performance efficiently.

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Project Explanation](#project-explanation)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Features
- Fetch CPU usage of top processes from a remote server.
- Log data into a CSV file with timestamps.
- Automated monitoring using a scheduler.
- Error handling for SSH connections and command execution.
- Easy configuration using environment variables.

## Prerequisites
Before running the project, ensure the following:
- Python 3.8 or higher installed
- `paramiko` library for SSH connections
- `python-dotenv` library for environment variable management
- `schedule` library for automated task scheduling
- SSH access to the remote server with a private key

Install required libraries:
```bash
pip install paramiko python-dotenv schedule

Installation
    Clone the repository:
    
    git clone https://github.com/your-username/cpu-usage-monitor.git
    cd cpu-usage-monitor


Create a .env file with the following variables:

    host_name=<REMOTE_SERVER_IP>
    user_name=<SSH_USERNAME>


Ensure your private key (.pem file) path is correctly set in the script.

    Usage
    Run the Python script:
    python cpu_monitor.py


The script will connect to the remote server every 5 minutes and append CPU usage data to cpu_usage_logs.csv.
You can open the CSV file in Excel or any spreadsheet software to analyze historical CPU usage.

Project Explanation

    The workflow of this project is as follows:
    Environment Setup: Load server credentials (host_name, user_name) securely from a .env file.
    SSH Connection: Establish a secure connection using Paramiko with RSA key authentication.
    Fetch CPU Usage:
    Executes a command to list top 5 CPU-consuming processes.
    Formats output into CSV-friendly structure.
    Data Logging: Writes the timestamp and CPU usage data into cpu_usage_logs.csv.
    Automation: Uses schedule library to fetch CPU data every 5 minutes.
    Error Handling: Handles connection failures and command errors gracefully.
    Scalability: Easy to extend for memory, disk, or network monitoring.