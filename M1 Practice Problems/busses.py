import math


def num_busses(total_students):
    return math.ceil(total_students / 52)


print(num_busses(105))
