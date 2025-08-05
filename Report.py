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

