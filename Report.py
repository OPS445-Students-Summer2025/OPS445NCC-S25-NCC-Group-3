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

