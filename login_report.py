#!/usr/bin/env python3
# Student ID: mzaman30

from login_activity import get_inactive_users, get_frequent_users
from login_utils import format_report

def generate_login_report(days=30, threshold=5):
    """Generates and prints a login activity report."""
    inactive_users = get_inactive_users(days)
    frequent_users = get_frequent_users(threshold)

    print(format_report(f"Users inactive for {days}+ days", inactive_users))
    print(format_report(f"Users logged in >= {threshold} times", frequent_users))
