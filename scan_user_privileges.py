#!/usr/bin/env python3

"""
Assignment 2 - Group Project: User Reports and Management
Main file: assignment2.py
"""

import argparse
import os
import pwd
import grp
import subprocess
import csv
import sys

# ---------------------------
# 🔹 1. Advanced User Report Module
# Assigned to: Person 1
# ---------------------------
# Tasks:
# - List only non-system users (UID ≥ 1000)
# - Count login shells used (e.g., /bin/bash, /bin/false)
# - Detect duplicate home directories (multiple users sharing same home)
# - Detect users who have never logged in (via lastlog or /var/log/wtmp)
# - Generate full audit report (option to export as .txt or .json)
# Function: def generate_user_report(output_format='txt'): ...

# ---------------------------
# 🔹 2. Login Activity Analyzer
# Assigned to: Person 2
# ---------------------------
# Tasks:
# - Use lastlog or /var/log/auth.log to check login history
# - Count users who have:
#     • Not logged in for 30+ days
#     • Logged in more than X times (X = CLI argument)
# - Optional: Display login frequency as text-based bar chart (e.g., user1: ||||| )
# Function: def analyze_login_activity(min_logins=5): ...

# ---------------------------
# 3. User Privilege Scanner
# Assigned to: Vrund Padariya
# ---------------------------
# Tasks:
# - List users in 'sudo' and 'admin' groups (using grp module)
# - Find users with UID 0 (should only be root)
# - Check ownership of /etc/shadow and /etc/sudoers
# - List users who share the same UID or GID 

def scan_user_privileges():
    print(" Any privileged  users in 'sudo' and 'admin' groups ")
    for group_name in ['sudo', 'admin']:
        try:
            usernames = grp.getgrnam(group_name).gr_mem
            if usernames:
                print(f"Group '{group_name}' includes: {', '.join(usernames)}")
            else:
                print(f"Group '{group_name}' exists but has no users.")
        except KeyError:
            print("Sorry! No group found ", group_name)

    print(" Looking for users with root privileges (UID 0) ")
    root_found = False
    for user in pwd.getpwall():
        if user.pw_uid == 0:
            print(f"User '{user.pw_name}' has UID 0 (full system access).")
            root_found = True
    if not root_found:
        print("Sorry! No users with the root privileges.")

    print("  Owner of the important system files")
    files = ["/etc/shadow", "/etc/sudoers"]
    for filepath in files:
        try:
            information = os.stat(filepath)
            owner = pwd.getpwuid(information.st_uid).pw_name
            group = grp.getgrgid(information.st_gid).gr_name
            print(f"File '{filepath}' is owned by user '{owner}' and group '{group}'.")
        except Exception as v:
            print(f"Could not access '{filepath}'. Reason: {v}")

    print(" Users with the same UID ")
    users = pwd.getpwall()
    duplicate_uid = False
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i].pw_uid == users[j].pw_uid:
                print(f"Users '{users[i].pw_name}' and '{users[j].pw_name}' share UID {users[i].pw_uid}.")
                duplicate_uid = True
    if not duplicate_uid:
        print("Congrats! No duplicate UIDs found.")

    print(" Users with the same GID ")
    duplicate_gid = False
    for i in range(len(users)):
        for j in range(i + 1, len(users)):
            if users[i].pw_gid == users[j].pw_gid:
                print(f"Users '{users[i].pw_name}' and '{users[j].pw_name}' share GID {users[i].pw_gid}.")
                duplicate_gid = True
    if not duplicate_gid:
        print("Congrats! No duplicate GIDs found.")

# ---------------------------
# 🔹 4. User Management Tool (Safe Ops)
# Assigned to: Person 4
# ---------------------------
# Tasks:
# - Add new user (simulate using command string or log it instead)
# - Disable user with: subprocess.run(["sudo", "passwd", "-l", username])
# - Optional: Prompt confirmation before deleting a user (simulated or real)
# - If `sudo` not available, log command instead of executing
# Function: def manage_user(action, username): ...

# ---------------------------
# 🔹 5. CLI + Report Coordinator
# Assigned to: Person 5
# ---------------------------
# Tasks:
# - Use argparse to handle the following options:
#     --report             → Full system report (calls Person 1)
#     --login-stats        → Analyze login activity (calls Person 2)
#     --sudo-users         → Scan user privileges (calls Person 3)
#     --add-user <user>    → Add new user (calls Person 4)
#     --disable-user <user>→ Disable/lock user (calls Person 4)
# - Connect all functions inside main()
# - Format CLI help output and final report output
# Function: def parse_arguments(): ...

