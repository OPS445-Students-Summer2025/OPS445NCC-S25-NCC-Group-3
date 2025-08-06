## Winter 2025 Assignment 2  
**OPS445 Assignment 2 – Advanced User Report Module**  
**Contributor:** Koshish Adhikari (kadhikari9)  
**Role:** Advanced User Report Module (Part 1)  
**Course:** OPS445 – Summer 2025 (Professor Eric Brauer)  

---

### About This Assignment  
This branch implements the **Advanced User Report Module**, which is **Part 1** of our group project. It performs the following tasks:

- Lists **non-system users** (UID ≥ 1000 and ≠ 65534) by reading `/etc/passwd`.
- Identifies **duplicate home directories** shared by multiple users (a potential security issue).

This functionality is useful for detecting misconfigurations or security risks related to user management on Linux systems.

---

### How to Run

```bash
# To list all non-system users:
python3 assignment2.py report --list-non-system

# To check for duplicate/shared home directories:
python3 assignment2.py report --duplicate-homes



##REFRENCES
https://docs.python.org/3/library/argparse.html

https://man7.org/linux/man-pages/man5/passwd.5.html

https://docs.python.org/3/tutorial/controlflow.html#for-statements
