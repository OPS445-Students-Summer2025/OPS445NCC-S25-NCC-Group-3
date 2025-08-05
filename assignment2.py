#!/usr/bin/env python3
"""
Student ID: dmbenjamin
"""

import subprocess
import argparse
import sys


def create_user(username: str) -> None:
    """Add a new user to the system."""
    try:
        subprocess.check_call(["sudo", "useradd", username])  # create user
        print(f"User '{username}' added successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to add user '{username}': {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unknown error occurred: {e}", file=sys.stderr)


def delete_user(username: str) -> None:
    """Remove an existing user from the system."""
    try:
        subprocess.check_call(["sudo", "userdel", username])   # delete user
        print(f"User '{username}' deleted successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to delete user '{username}': {e}", file=sys.stderr)
    except Exception as e:
        print(f"Unknown error occurred: {e}", file=sys.stderr)


def list_human_users() -> None:
    """List all human-account usernames (UID ≥ 1000)."""
    try:
        output = subprocess.check_output(["getent", "passwd"], text=True) # pull passwd
        for line in output.splitlines():
            username, _, uid, *_ = line.split(":", 3)
            if uid.isdigit() and int(uid) >= 1000:           # skip system accounts
                print(username)
    except subprocess.CalledProcessError:
        print("Failed to list users.", file=sys.stderr)
    except FileNotFoundError:
        print("getent not found on this system.", file=sys.stderr)
    except Exception as e:
        print(f"Unknown error occurred: {e}", file=sys.stderr)



def main() -> None:
    parser = argparse.ArgumentParser(description="Darian user-management toolkit")
    parser.add_argument(
        "action",
        choices=["create", "delete", "list"],
        help="Action to perform",
    )
    parser.add_argument(
        "--username",
        help="Username for 'create' or 'delete' actions",
    )

    args = parser.parse_args()

    if args.action in {"create", "delete"} and not args.username:
        parser.error("--username is required for the chosen action")

    if args.action == "create":
        create_user(args.username)
    elif args.action == "delete":
        delete_user(args.username)
    else:  # list
        list_human_users()


if __name__ == "__main__":
    main()
