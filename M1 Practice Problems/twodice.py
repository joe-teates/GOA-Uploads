#  Write a function that uses the random package and rolls two dice. The function should return "win"
#  if the sum of those two dice is 6, 7 or 8 and returns "lose" otherwise. (video)

import random


def roll():
    dice_one = (random.random()*5+1).__round__()
    dice_two = (random.random()*5+1).__round__()
    sum = dice_one + dice_two
    if sum == 6 or sum == 7 or sum == 8:
        return "win"
    else:
        return "lose"


print(roll())
