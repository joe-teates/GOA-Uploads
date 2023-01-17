# Write a function that is given the month, day, and year of each of two dates (six arguments in all!),
# and determines which date comes earlier.  Return the string "before" if the first date comes before
# the second one, "after" if the first date comes after the second one, and "same" if they are the same

def earlier(month_one, day_one, year_one, month_two, day_two, year_two):
    if year_one < year_two:
        return "before"
    elif year_one > year_two:
        return "after"
    elif month_one < month_two:
        return "before"
    elif month_one > month_two:
        return "after"
    elif day_one < day_two:
        return "before"
    elif day_one > day_two:
        return "after"
    else:
        return "same"


print(earlier(11, 31, 2021, 10, 31, 2020))
