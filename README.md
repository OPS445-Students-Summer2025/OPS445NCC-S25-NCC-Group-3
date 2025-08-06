# Advanced User Report Module

## Author
Koshish Adhikari  
Seneca ID: kadhikari9

## Description

This module is part of the **User Security & Management Suite** assignment. It focuses on generating a security report by:

- Listing **all non-system users** (UID ≥ 1000 and ≠ 65534) on the system.
- Detecting if **any home directories are shared** by multiple users (potential security concern).

The data is collected by parsing `/etc/passwd`, which stores user account information in Linux systems.


## How to Use

Run one of the following commands:

```bash
# List non-system users
python3 assignment2.py report --list-non-system

# Find shared home directories
python3 assignment2.py report --duplicate-homes


#REFRENCES
https://docs.python.org/3/library/argparse.html

https://man7.org/linux/man-pages/man5/passwd.5.html

https://docs.python.org/3/tutorial/controlflow.html#for-statements
