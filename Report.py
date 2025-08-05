#!/usr/bin/env python3

import argparse
import pwd
import sys

def generate_report(username=None):
    users = []
    if username:
        try:
            user = pwd.getpwnam(username)
            users.append(user)
        except KeyError:
            print(f"User '{username}' not found.", file=sys.stderr)
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
            sys.stdout = sys._stdout_
            print(f"Report saved to {args.output}")
        except Exception as e:
            print("Failed to write to file:", e, file=sys.stderr)
            sys.exit(1)
    else:
        generate_report(args.user)

if _name_ == "_main_":
    main()
