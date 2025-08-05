#!/usr/bin/env python3

import argparse
import pwd
import sys

def generate_report(username=None):
    users = []
    if username:
        all_users = pwd.getpwall()
        user = next((u for u in all_users if u.pw_name == username), None)
        if user:
            users.append(user)
        else:
            print(f"User '{username}' not found.")
            sys.exit(1)
    else:
        users = pwd.getpwall()

    print("User Report")
    print("-----------")
    for u in users:
        print("Username:", u.pw_name)
        print("UID:", u.pw_uid)
        print("GID:", u.pw_gid)
        print("Home Dir:", u.pw_dir)
        print("Shell:", u.pw_shell)
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", default=None)
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args()

    if args.output:
        try:
            with open(args.output, "w") as f:
                sys.stdout = f
                generate_report(args.user)
            sys.stdout = sys.__stdout__
            print(f"Report saved to {args.output}")
        except Exception as e:
            print("Failed to write to file:", e, file=sys.stderr)
            sys.exit(1)
    else:
        generate_report(args.user)

if __name__ == "__main__":
    main()

