
# HW Function "drawLine( length, direction )"

simbol_1 = "-"
simbol_2 = "|"

def drawLine( length, direction ):
    if direction == "h":
        print(length * simbol_1)
    elif direction == "v":
        for x in range(length):
            print(simbol_2)
            

