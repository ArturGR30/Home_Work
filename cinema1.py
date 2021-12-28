seats = [ 0 , 0 , 0 , 0 , 0]

while True:
	for n in seats:
    	#HW_1
		if n == 0:
		  	n= "|   |"
		else:
		  	n= "| x |"
		print(n, end=" ")

	print("\n--------------------\n")

	s = int (input("Pick a seate (1..5): ")) - 1
    
    #HW_2
	if s not in range(0, 5):
		while s not in range(0, 5):
			s = int(input("You pick a non-existent seat, please pick a seat (1..5)  ")) - 1	
    
	if seats[s] == 0:
		print("Yes," , s+1, " seat is free!")
		#HW_3
		p_1 = 180
		p_2 = 200
		p_3 = 250
		if s+1 in [1, 5]:
			print("price for seat", s+1, "is",  p_1)
		elif s+1 in [2, 4]:
			print("price for seat", s+1, "is",  p_2)
		elif s+1 in [3]:
			print("price for seat", s+1,  "is", p_3)
		confirm = input("buy (yes/not)?")
		if confirm == "yes":
			seats[s] = 1
	else:
		print("No, sorry,", s+1, "seat is ocupeid!")