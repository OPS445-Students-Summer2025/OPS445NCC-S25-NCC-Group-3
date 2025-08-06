#!/usr/bin/env python3

from scan_user_privileges import scan_user_privileges
from user_report import get_non_system_users, find_duplicate_homes
from generate_report import generate_report
from assignment2_mzaman30 import login_activity_analyzer
from assignment2_dmbenjamin import create_user, delete_user, list_human_users

import sys
import pwd
import subprocess
import argparse

def main():
    parser = argparse.ArgumentParser(description="Integrated User Management Toolkit")

    subparsers = parser.add_subparsers(dest="command")

    # scan user privileges
    subparsers.add_parser("scan-privileges", help="Scan user privileges")

    # user reports
    report_parser = subparsers.add_parser("user-report", help="Generate user reports")
    report_parser.add_argument("--list-non-system", action="store_true", help="List non-system users")
    report_parser.add_argument("--duplicate-homes", action="store_true", help="List duplicate home directories")

    # generate report
    gen_report_parser = subparsers.add_parser("generate-report", help="Generate detailed user report")
    gen_report_parser.add_argument("-u", "--user", default=None, help="Specify a user to generate report")
    gen_report_parser.add_argument("-o", "--output", default=None, help="Output file")

    # login activity analyzer
    subparsers.add_parser("login-analyzer", help="Analyze user login activity")

    # user management
    user_mgmt_parser = subparsers.add_parser("user-mgmt", help="User management actions")
    user_mgmt_parser.add_argument("action", choices=["create", "delete", "list"], help="Action to perform")
    user_mgmt_parser.add_argument("--username", help="Username for create/delete")

    args = parser.parse_args()

    if args.command == "scan-privileges":
        scan_user_privileges()

    elif args.command == "user-report":
        if args.list_non_system:
            users = get_non_system_users()
            for user in users:
                print(user)
        if args.duplicate_homes:
            duplicates = find_duplicate_homes()
            for home, users in duplicates.items():
                print(f"{home}: {', '.join(users)}")

    elif args.command == "generate-report":
        if args.output:
            original_stdout = sys.stdout
            with open(args.output, "w") as f:
                sys.stdout = f
                generate_report(args.user)
                sys.stdout = original_stdout
            print("Report saved to " + args.output)
        else:
            generate_report(args.user)

    elif args.command == "login-analyzer":
        login_activity_analyzer()

    elif args.command == "user-mgmt":
        if args.action == "create" and args.username:
            create_user(args.username)
        elif args.action == "delete" and args.username:
            delete_user(args.username)
        elif args.action == "list":
            list_human_users()
        else:
            print("--username is required for create/delete actions")

if __name__ == "__main__":
    main()

