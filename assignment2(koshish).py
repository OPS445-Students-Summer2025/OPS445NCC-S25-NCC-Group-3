from user_report import get_non_system_users, find_duplicate_homes

# Import argparse to handle command-line arguments
import argparse

parser = argparse.ArgumentParser(description="User Security & Management Suite")
subparsers = parser.add_subparsers(dest="command")

# Create a new subparser for the "report" command
report_parser = subparsers.add_parser("report", help="User report options")
# Add options (flags) for listing non-system users and detecting duplicate homes
report_parser.add_argument("--list-non-system", action="store_true", help="List non-system users")
report_parser.add_argument("--duplicate-homes", action="store_true", help="List users with duplicate home directories")

args = parser.parse_args()

# If the "report" command is selected
if args.command == "report":
  
    # Run get_non_system_users() and print results
    if args.list_non_system:
        users = get_non_system_users()
        for user in users:
            print(user)
    # Run find_duplicate_homes() and print results
    if args.duplicate_homes:
        dupes = find_duplicate_homes()
        for home, users in dupes.items():
            print(f"{home}: {', '.join(users)}")
