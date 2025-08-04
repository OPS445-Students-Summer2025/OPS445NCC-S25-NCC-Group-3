#!/usr/bin/env python3
# Student ID: mzaman30

from datetime import datetime

def format_report(title, data):
    """Return a nicely formatted string for the login report."""
    report = f"\n=== {title} ===\n"
    if isinstance(data, dict):
        for user, count in data.items():
            report += f"{user}: {count} logins\n"
    elif isinstance(data, list):
        for user in data:
            report += f"{user}\n"
    return report
