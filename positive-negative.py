value = 2
if value >= 0 and value % 2 == 0:
    print("Positive")
elif value % 2 > 0 and value >= 0:
    print("Positive and odd")
elif value <=0 and value % 2 ==0:
    print ("The rest")
else:
    print("Negative")