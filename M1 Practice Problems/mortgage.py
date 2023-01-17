"""
Write a Python function that computes the monthly payments needed for a 30 year 
mortgage, given the annual interest rate and the amount of money borrowed
"""


def compute_interest(r, p):
    r = r / 12  # the interest rate which is divided by 12 to get the monthly percentage
    n = 30 * 12  # 30 times 12 gets how many months are in 30 years
    p = 293200  # money borrowed - price of a 911 GT2 RS

    numerator = r*p*((1+r)**n)
    denomonator = ((1+r)**n) - 1
    return (numerator / denomonator)


print(compute_interest(0.05, 293200))
