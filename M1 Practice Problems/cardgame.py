
def card_game():
    top = input()
    bottom = input()
    d_count = 0
    a_count = 0
    
    for i in range(3):
        if top[i:i+1] == "d" or bottom[i:i+1] == "d":
            d_count+=1
        elif top[i:i+1] == "a" or bottom[i:i+1] == "a":
            a_count+=1
    # catching exception
    if d_count == 3:
        for i in range(3):
            if top[i:i+1] == "a" or bottom[i:i+1] == "a":
                return "yes"
            
    if d_count >= 2 and a_count >=1:
        return "yes"
    else:
        return "no"
print(card_game())
