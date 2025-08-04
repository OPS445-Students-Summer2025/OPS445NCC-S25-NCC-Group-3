#!/usr/bin/env python3
# Student ID: mzaman30

import login_report

if __name__ == "__main__":
    print("=== Testing Login Activity Analyzer ===")
    login_report.generate_login_report(days=30, threshold=5)
