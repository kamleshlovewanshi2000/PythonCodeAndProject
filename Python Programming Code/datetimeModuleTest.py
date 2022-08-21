import datetime

# datetime.now() Returns Current Date and Time
print("Current Date & Time:",datetime.datetime.now())

# Creating a datetime object
o = datetime.datetime(2022,2,25)
print("Created Object:",o)

# strftime() Method takes one parameter, format, to specify
# the formate of the returned string
x = datetime.datetime.now()
print()

# "%Y" Return years 2022
year = x.strftime("%Y")
print("Year:",year)

# "%y" Return years 22
print("Year:",x.strftime("%y"))
print()

# "%b" return month name in short version as Dec, Jun, Apr
print("Month:",x.strftime("%b"))

# "%B" return month name in Full version as August, December
print("Month:",x.strftime("%B"))
print()

# "%m" return Month as a number 01-12  like 08, 12
print("Month as a number:",x.strftime("%m"))
print()

# "%H" return Hour as 00-23 (24 hours)
print("Hour as 00-23:",x.strftime("%H"))

# "%I" return Hour as 00-12 (12 hours)
print("Hour as 00-12:",x.strftime("%I"))

# "%p" return time in AM/PM
print("Time in AM/PM :",x.strftime("%p"))
print()

# "%M" return Minute as 00-59
print("Minute:",x.strftime("%M"))
print()

# "%S" return Seconds as 00-59
print("Second:",x.strftime("%S"))


