# Winter 2025 Assignment 2
# OPS445 Assignment 2 – User Report and Management

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
