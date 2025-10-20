# DATE TIME
# This module provides functions to work with date and time in Python.

import datetime

# CURRENT DATE AND TIME

a = datetime.datetime.now()
print(a) # Current date and time
print(a.year) # Year
print(a.strftime("%A"))  # Day of the week

# --------------------------------------------------------------

# SPECIFIC DATE AND TIME

bday = datetime.datetime(2025,5,24)
print(bday) # Specific date and time
print(bday.strftime("%B"))  # Month
print(bday.strftime("%A"))  # Day of the week
print(bday.strftime("%d"))  # Date