# DRAW this PATTERN:
# HW2:  * * * # # * * * # # * * * ....

print("\n")

for x in range(1, 21):
    if x % 5 == 0:
        print("# ", end="")
    elif (x + 1) % 5 == 0:
        print("# ", end="")
    else:
        print("* ", end="") 