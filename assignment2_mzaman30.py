#!/usr/bin/env python3
# Student ID: mzaman30

import subprocess
import pwd
from datetime import datetime, timedelta

def is_real_user(username):
    """Return True if user is a human (UID >= 1000)"""
    try:
        user_info = pwd.getpwnam(username)
        return user_info.pw_uid >= 1000
    except KeyError:
        return False

def login_activity_analyzer():
    """Analyze and display user login activity"""
    user_logins = {}

    # 1. Count logins per user using `last`
    output = subprocess.getoutput("last -F -w -n 1000")
    lines = output.splitlines()

    for line in lines:
        if "wtmp begins" in line or line.strip() == "":
            continue

        parts = line.split()
        username = parts[0]

        # Ignore system or non-human users
        if username in ["reboot", "shutdown", "wtmp", "runlevel"] or not is_real_user(username):
            continue

        user_logins[username] = user_logins.get(username, 0) + 1

    print("=== Login Activity Analyzer (mzaman30) ===\n")

    # 2. Users inactive for 30+ days
    print("=== Users inactive for 30+ days ===")
    threshold_date = datetime.now() - timedelta(days=30)
    output_lastlog = subprocess.getoutput("lastlog")
    inactive_users = []

    for line in output_lastlog.splitlines()[1:]:
        parts = line.split()
        username = parts[0]

        if not is_real_user(username):
            continue

        if "Never" in line:
            inactive_users.append(username)
            continue

        try:
            date_str = " ".join(parts[2:7])
            last_login = datetime.strptime(date_str, "%b %d %H:%M:%S %Y")
            if last_login < threshold_date:
                inactive_users.append(username)
        except:
            continue

    if inactive_users:
        for user in inactive_users:
            print(user)
    else:
        print("No inactive users found.")

    # 3. Show all active users with login counts
    print("\n=== Active Users and Login Counts ===")
    if user_logins:
        for user, count in user_logins.items():
            print(f"{user}: {count} logins")
    else:
        print("No active users found.")
