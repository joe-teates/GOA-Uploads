def casino_game():
    i1, i2 = map(int, input().split())
    d1, d2, d3, d4, d5, d6 = map(int, input().split())
    
    dice_faces = [d1,d2,d3,d4,d5,d6]
    
    i1_prob = 0
    i2_prob = 0
    for face in dice_faces:
        if face == i1:
            i1_prob+=1
        if face == i2:
            i2_prob+=1
            
    i1_prob /= 6
    i2_prob /= 6
    return i1_prob * i2_prob
print(casino_game())
