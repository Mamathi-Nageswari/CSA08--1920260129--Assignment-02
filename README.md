# CSA08 Python Programming - Assignment 2

- Name: ____________________
- Register number: ____________________
- Python version: Python 3.10.12
- Libraries: standard library only (functools, timeit, time, io, tracemalloc, re, inspect, sys). See requirements.txt.

## How to run
Open a terminal in the question folder and run each program with `python3 <file>.py`.

| Folder | Command | Result |
|---|---|---|
| Q1 | `python3 subsidy.py`, `python3 nested_vs_combined.py`, `python3 match_vs_lookup.py` | if-elif-else gives one decision per household; separate ifs give two at 100 and 200 units; all designs agree |
| Q2 | `python3 otp.py`, `python3 otp_changed.py`, `python3 otp_recursive.py` | while and for versions lock after 3 wrong attempts, blanks not counted; security question adds 2 attempts |
| Q3 | `python3 plate.py`, `python3 immutability.py`, `python3 regex_vs_slicing.py` | Expected output reproduced; 6/6 predictions correct; regex and slicing agree |
| Q4 | `python3 sms_bill.py`, `python3 three_ways.py`, `python3 stringio_file.py` | Same text, length 3048890; += becomes quadratic once the string has a second reference |
| Q5 | `python3 canteen.py`, `python3 order_design.py`, `python3 closure_vs_explicit.py` | Expected output reproduced; three customers have independent orders |
| Q6 | `python3 temple_steps.py`, `python3 growth.py`, `python3 limit.py` | naive 242785 calls vs memo 26; RecursionError at n = 1000; loop version works |
| Q7 | `python3 redesign.py` | Bottom-up loop: 29 operations instead of 2,692,537 calls at n = 30 |

Screenshots of every run are in each folder's `screenshots/` directory.
