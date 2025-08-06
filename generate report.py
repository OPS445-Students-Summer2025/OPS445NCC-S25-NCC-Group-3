#!/usr/bin/env python3
#Citations
#https://docs.python.org/3/library/pwd.html
#https://coderivers.org/blog/python-pwd/

import argparse
import pwd  
import sys

def generate_report(username=None):
    users = []
    if username:
        all_users = pwd.getpwall()
        user = None
        for u in all_users:
            if u.pw_name == username:
                user = u
                break
        if user:
            users.append(user)
        else:
            print("User '" + username + "' not found.")
            sys.exit(1)
    else:
        users = pwd.getpwall()

    print("User Report")
    print("-----------")
    for u in users:
        print("Username:", u.pw_name)
        print("Encrypted password:", u.pw_passwd)
        print("UID:", u.pw_uid)
        print("GID:", u.pw_gid)
        print("User name/comment:", u.pw_gecos)
        print("Home Dir:", u.pw_dir)
        print("Shell:", u.pw_shell)
        print()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--user", default=None)
    parser.add_argument("-o", "--output", default=None)
    args = parser.parse_args()

    if args.output:
        with open(args.output, "w") as f:
            original_stdout = sys.stdout
            sys.stdout = f
            generate_report(args.user)
            sys.stdout = original_stdout
        print("Report saved to " + args.output)
    else:
        generate_report(args.user)

if __name__ == "__main__":
    main()

