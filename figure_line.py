figure = input("what figure to draw? ")

if figure == "line":
    print("-----")
elif figure =="square":
    print("------\n|    |\n|    |\n------")
elif figure =="parallel horizontal lines":
    print("-----\n-----")
elif figure == "parallel vertical lines":
    print("|    |\n|    |")
else:
    print("CAN'T DRAW SUCH FIGURE!")