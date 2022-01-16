# 2d robo/matrix
from os import system
# LEGEND
# 1 cell - 1m2
# 0 - empty
# 1 - wall


room_map = [
    [1,1,1,1,0,0,1,1,1,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,2,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,0,1],
    [1,0,0,0,0,0,0,0,3,1],
    [1,1,1,1,1,1,1,1,1,1],
]

####### print the map: nested loop  #######
system("cls") #(HW)

for ri in range(10):
    for ci in range(10):
        if room_map[ri] [ci] == 0:
            print(".", end=" ")
        elif room_map[ri] [ci] == 1:
            print("#", end=" ")
        elif room_map[ri] [ci] == 2:
            print("R", end=" ")
        elif room_map[ri] [ci] == 3:
            print("B", end=" ")
    print("   |", ri)   # print row index (HW)  
    
####### print column index (HW)  #########
print()
print("- "*10)
for ci in range(10):
    print(ci, end=" ")
print()
print()
