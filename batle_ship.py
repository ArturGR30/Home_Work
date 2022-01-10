from os import system
from random import randint
# LEGEND
water = 0
ship = 1
miss = 2
hit = 3
# ✕ ○ ■ □

colA = [
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
    0,
]
colA[randint(0,9)] = ship
#HW, add 2 more ships
colA[randint(0,9)] = ship

#score = 2

# Game Loop

#HW3, add max 5 shoots
n=0
while n <= 5:
    n+=1
  
    
    ## Draw the map
    system("clear")
    for y in range(1, 11):
        
        if colA[y-1] == water or colA[y-1] == ship:
            sign = "□"
        if colA[y-1] == miss:
            sign = "○"
        if colA[y-1] == hit:
            sign = "✕"
        
        print(sign, y)
          
    
    
    shootY = int(input("shoot: "))
    
	
    if colA[shootY-1] == water:
        colA[shootY-1] = miss
    
    if colA[shootY-1] == ship:
        colA[shootY-1] = hit
 
#HW, add score here   
    if colA[shootY-1] == hit:
        score=1
    else:
        score=0
    print("Your score is", + score)