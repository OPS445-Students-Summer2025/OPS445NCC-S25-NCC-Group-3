# Winter 2025 Assignment 2
# OPS445 Assignment 2 – User Report and Management

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


**Contributor:** Md. Shahriar Zaman (mzaman30)  
**Role:** Login Activity Analyzer (Part 2)  
**Course:** OPS445 – Summer 2025 (Professor Eric Brauer)  

---

## About This Assignment

This branch implements the **Login Activity Analyzer**, which is **Part 2** of our group project:  

- Analyzes login activity for **non-system users** (UID ≥ 1000)  
- Detects users **inactive for 30+ days**  
- Shows active users
---

## Research and References

The following official resources were used to implement the login activity analyzer:  

1. [Linux `last` Command Manual](https://man7.org/linux/man-pages/man1/last.1.html)  
2. [Linux `lastlog` Command Manual](https://man7.org/linux/man-pages/man8/lastlog.8.html)  
3. Python Standard Library Documentation:  
   - [`pwd` module](https://docs.python.org/3/library/pwd.html)  
   - [`subprocess` module](https://docs.python.org/3/library/subprocess.html)  
   - [`datetime` module](https://docs.python.org/3/library/datetime.html)  
---
**Contributor:** Darian Benjamin (dmbenjamin)  
**Role:** User Management Tool (Part 4)  
**Course:** OPS445 – Summer 2025 (Professor Eric Brauer)  

---
## About This Assignment

This branch implements the **User Management Tool**, which is **Part 4** of our group project:  

1. Create a user:
    `python3 assignment2.py user-mgmt create --username ben`

2. Delete a user:
    `python3 assignment2.py user-mgmt delete --username ben`

3. List all human users:
    `python3 assignment2.py user-mgmt list`

---

## Research and References

The following official resources were used to implement the user management tool:  

1. Youtube video - (https://www.youtube.com/watch?v=-Sgw-6a1HjU&t=307s)
2. Python Standard Library Documentation:  
   - [`argparse` module](https://docs.python.org/3/library/argparse.html)
**Contributor:** Samarth Waghela (swaghela)  
**Role:** CLI and generate report (Part 5)  
**Course:** OPS445 – Summer 2025 (Professor Eric Brauer)  

---

## About This Assignment

The code in the last part of the assignment is supposed to generate a final report which will cover all the details that can be obtained from the user database.

- A specific user details 
- All the users in the database
- Gives output to file options
---

## Research and References

The following official resources were used to implement the report generator:  

1. [pwd module and further options]
   (https://docs.python.org/3/library/pwd.html)
   (https://coderivers.org/blog/python-pwd/)
                                    
                                   
3. help with stderr
   - (https://www.geeksforgeeks.org/python/how-to-print-to-stderr-and-stdout-in-python/)
