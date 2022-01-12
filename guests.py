##################     input data       ########################
guests_1 = [ "Bethaney Bain", "Kacey Johns", "Manpreet Saunders" ]
guests_2 = [ "Elwood Curtis", "Diya Griffin", "Kacey Johns" ]
guests_3 = [ "Tobey Weiss", "Kadie Barnes", "Diya Griffin" ]
##################     input data      #########################


guests_total = guests_1 + guests_2 + guests_3

guests_list = []

for i in range(len(guests_total)):
	if guests_total[i] not in guests_list:
		guests_list.append(guests_total[i])
		
guests_list.sort()

#########  print the guests_list  #########
for i in range(len(guests_list)):
	print("\t>", guests_list[i])