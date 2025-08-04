#!/usr/bin/env python3
# Student ID: mzaman30

import subprocess
from datetime import datetime, timedelta

def get_inactive_users(days=30):
    """Return a list of users who have not logged in for X days."""
    inactive_users = []
    cutoff_date = datetime.now() - timedelta(days=days)
    try:
        output = subprocess.run(["lastlog"], capture_output=True, text=True, check=True)
        lines = output.stdout.splitlines()[1:]
    except subprocess.CalledProcessError:
        return inactive_users

    for line in lines:
        parts = line.split()
        if len(parts) < 8:
            continue
        username = parts[0]
        if "Never" in line:
            inactive_users.append(username)
        else:
            date_str = " ".join(parts[3:7])
            try:
                login_date = datetime.strptime(date_str, "%b %d %H:%M:%S %Y")
                if login_date < cutoff_date:
                    inactive_users.append(username)
            except ValueError:
                continue
    return inactive_users

def get_frequent_users(threshold=5):
    """Return dict of users who logged in >= threshold times."""
    user_login_counts = {}
    try:
        output = subprocess.run(["last"], capture_output=True, text=True, check=True)
        lines = output.stdout.splitlines()
    except subprocess.CalledProcessError:
        return user_login_counts

    for line in lines:
        if not line.strip() or "reboot" in line or "wtmp" in line:
            continue
        username = line.split()[0]
        user_login_counts[username] = user_login_counts.get(username, 0) + 1

    return {user: count for user, count in user_login_counts.items() if count >= threshold}

def format_report(title, data):
    """Format a human-readable report for login activity."""
    report = f"\n=== {title} ===\n"
    if isinstance(data, dict):
        for user, count in data.items():
            report += f"{user}: {count} logins\n"
    elif isinstance(data, list):
        for user in data:
            report += f"{user}\n"
    return report

def generate_login_report(days=30, threshold=5):
    """Generates and prints the login activity report."""
    inactive_users = get_inactive_users(days)
    frequent_users = get_frequent_users(threshold)
    print(format_report(f"Users inactive for {days}+ days", inactive_users))
    print(format_report(f"Users logged in >= {threshold} times", frequent_users))
