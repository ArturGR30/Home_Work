big_ship = int(input("put the coordinate of big ship "))
for x in range(1,11):
    if x == big_ship:
      print( "wWw", end="" )
    else:
      print( "~", end="" )