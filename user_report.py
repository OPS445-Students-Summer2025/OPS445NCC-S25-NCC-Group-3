# user_report.py
# Author: Koshish Adhikari
# Username: kadhikari9

# This module provides user reports for the assignment.
# It lists non-system users and detects shared home directories.

# Function 1: Get all non-system users (UID >= 1000 and != 65534)
def get_non_system_users():
    users = []
    with open("/etc/passwd") as file:
        for line in file:
            parts = line.strip().split(":")  # Split each line by colon
            if len(parts) >= 7:
                uid = int(parts[2])  # UID is the third field
                if uid >= 1000 and uid != 65534:  # Non-system user
                    users.append({
                        "username": parts[0],      # Username
                        "uid": uid,                # User ID
                        "gid": int(parts[3]),      # Group ID
                        "home": parts[5],          # Home directory
                        "shell": parts[6]          # Default shell
                    })
    return users

# Function 2: Find users that share the same home directory
def find_duplicate_homes():
    home_map = {}      # Maps home directories to usernames
    duplicates = {}    # Stores homes used by multiple users
    with open("/etc/passwd") as file:
        for line in file:
            parts = line.strip().split(":")
            if len(parts) >= 6:
                username = parts[0]
                home = parts[5]
                if home in home_map:
                    if home not in duplicates:
                        duplicates[home] = [home_map[home]]  # Add first user
                    duplicates[home].append(username)  # Add duplicate user
                else:
                    home_map[home] = username  # Store the first user for this home
    return duplicates

