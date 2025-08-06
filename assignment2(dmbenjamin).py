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
        subprocess.check_call(["sudo", "useradd", username])  # Subprocess.check_call() runs the command and waits for it to finish
        print(f"User '{username}' added successfully.") # Print the output
    except subprocess.CalledProcessError as e: # If command fails, it will raise CalledProcessError if command returns a nonzero exit status
        print(f"Failed to add user '{username}': {e}", file=sys.stderr) # Save the error in e and print e
    except Exception as e:
        print(f"Unknown error occurred: {e}", file=sys.stderr) # If it's not then print here


def delete_user(username: str) -> None:
    """Remove an existing user from the system."""
    try:
        subprocess.check_call(["sudo", "userdel", username])   # Subprocess.check_call() runs the command and waits for it to finish
        print(f"User '{username}' deleted successfully.") # Print the output
    except subprocess.CalledProcessError as e: # If the command fails, it will raise CalledProcessError
        print(f"Failed to delete user '{username}': {e}", file=sys.stderr) # Save the error in e and print e
    except Exception as e:
        print(f"Unknown error occurred: {e}", file=sys.stderr) # If it's not then print here


def list_human_users() -> None:
    """List all human-account usernames (UID ≥ 1000)."""
    try:
        output = subprocess.check_output(["getent", "passwd"], text=True) # Use subprocess.check_output() to execute the getent command, which grab the information from system password database.
        for line in output.splitlines(): # Grab the output from subprocess, root:x:0:0:root:/root:/bin/bash
            username, _, uid, *_ = line.split(":", 3)
            if uid.isdigit() and int(uid) >= 1000:           # skip system accounts
                print(username)    # Use for loop to print username one by one
    except subprocess.CalledProcessError: # If the system does not have getent, it will raise CalledProcessError
        print("Failed to list users.", file=sys.stderr) # Print the error
    except FileNotFoundError:  # Catch multiple exceptions
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


# Citations
# Youtube video - https://www.youtube.com/watch?v=-Sgw-6a1HjU&t=307s
# Website - https://docs.python.org/3/library/argparse.html
