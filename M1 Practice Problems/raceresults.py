"""You are an olympic athlete who has just finished a race against three opponents.  
Write a function that takes all four race times as arguments (your time as the first argument), 
and returns a string describing the medal you just won ("gold", "silver", "bronze", or "no medal").  
No ties!! """


def podium_place(personal_time, opponent_one, opponent_two, opponent_three):
    result_list = [personal_time, opponent_one, opponent_two, opponent_three]
    result_list.sort()
    place = result_list.index(personal_time)
    if place == 0:
        return "gold"
    elif place == 1:
        return "silver"
    elif place == 2:
        return "bronze"
    else:
        return "no medal"


print(podium_place(2, 11, 8, 9))
