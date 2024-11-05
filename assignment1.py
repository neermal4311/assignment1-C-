#!/usr/bin/env python3
"""
OPS445ZAA Assignment 1
Program: assignment1.py
Author: "Nirmal Gautam -ngautam11"
The python code in this file (assignment1.py) is original work written by
"Nirmal Gautam". No code in this file is copied from any other source 
except those provided by the course instructor, including any person, 
textbook, or on-line resource. I have not shared this python script 
with anyone or anything except for submission for grading.  
I am aware that infractions will be recorded and that appropriate
 action will be taken in accordance with the Academic Honesty Policy.
"""

import sys

def usage():
    """this Display usage message and exit"""
    print("Usage: assignment1.py YYYY-MM-DD NN")
    sys.exit(1)

def leap_year(year):
    """This shows whether the given year is leap year or no"""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def mon_max(month, year):
    """ This gives the max number of days in the given month and year"""
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29 if leap_year(year) else 28
    else:
        return 31
