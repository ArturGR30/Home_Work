################    input data     ################################
clients = ["John","Marry","Kate"]
clientsHighPriority = ["Tob","Pete"]
clientsLowPriority = ["Vicky","Lessly"]
################    input data     ################################

################ adds new elements in lists by priority (condition 2 of the BOBUS HW)  ######################		
while True:
	name_client = input("Hello, Enter your name please ")   
	choose_the_list = input("Pease enter your priority rang ( high / normal / low ) ")
	if choose_the_list == "high":
		clientsHighPriority.append(name_client)
	elif choose_the_list == "normal":
		clients.append(name_client)
	elif choose_the_list == "low":
		clientsLowPriority.append(name_client)
	elif name_client and choose_the_list == "x":
		break
	
#################  merging lists use insert() and append() (HW condition) ##########
for i in range(len(clientsHighPriority)):
	clients.insert(i,clientsHighPriority[i])
for i in range(len(clientsLowPriority)):
	clients.append(clientsLowPriority[i])
#################  merging lists use insert() and append() ##########

################# another method of merging lists ###################
#clients_total = clientsHighPriority + clients + clientsLowPriority
#clients_list = []

#for i in range(len(clients_total)):
#	clients_list.append(clients_total[i])
################# another method of merging lists ###################

#################  print list (condition 1 of the BONUS HW )  ######################################
def showClients():
	for i in range(len(clients)):
		print(i+1,".", clients[i])
showClients()


