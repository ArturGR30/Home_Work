from os import system


# a - move left
# d - move right

length = 20
roboX  = 1
bombX  = 8
bomb2  = 15
health = 100
heartX = 7
charge = 100


# HW1:
# +   + add "hp" (health) defauk: 100%, when bomb -50%
# +   +- game over -> hp == 0
# +   + show hp
# +   + many bombs
# +   + hearts (+20% hp)
# +   + limits ( a) teleport / b) stop )
# +   + charge = 100, each stop -5%
# -   + money bag (+ score)


while True:
    system("clear")
    
    ##############################################################
    
    if roboX == bombX or roboX == bomb2:   # health
        health -= 50
    elif roboX == heartX:
        health += 20     # hearts


    if health <= 0 or charge <=0:
        print(" GAME OVER ")
        break
      
    #################  DRAWING THE MAP  ##########################
    x = 1
    print("\n")

    while x <= length:
        if x == roboX:
            print(" 😶 ", end= "")
        elif x == bombX:
            print(" 💣 ", end="")
        elif x == bomb2:
            print(" 💣 ", end="")
        elif x == heartX:
            print(" ❤ ", end="")
        else:
            print(" ▬ ", end= "")
        x += 1

    print("\n")
    ##############################################################
    print("Your health ", health, " %")
    print("Your charge ", charge, " %")
    print("\n")
    ################## CONTROLS ##################################
    direction = input("dir (a/d)  > ")
    if direction == "a":
        roboX -= 1
        charge -=5
        if roboX == 0:    #teleport
           roboX = 20 
    if direction == "d":
        roboX += 1
        charge -=5
        if roboX == 21:   #teleport
            roboX = 1
    if direction == "x":
        system("clear")
        print("Thank you for playing")
        break
    ##############################################################

