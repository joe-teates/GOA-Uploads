"""Write a function that takes a year and returns the boolean True if it is a leap year, and false if it is not.  
You may need to do some research to determine the rules for leap days."""


def is_leap_year(year):
    if year % 4 != 0 or (year % 100 == 0 and year % 400 != 0):
        return False
    elif year % 4 == 0:
        return True


print(is_leap_year(2028))
