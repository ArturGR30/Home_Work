from os import system
from prettytable import PrettyTable

students_first_name = []
students_last_name = []
students_age = []
students_mark = []

while True:
	system("clear")
	student_data = input("Enter students data ")
	x = student_data.split()
	for i in range(len(x)):
		if i == 0:
			students_first_name.append(x[i])
		elif i == 1:
			students_last_name.append(x[i])
		elif i == 2:
			students_age.append(x[i])
		elif i == 3:
			students_mark.append(x[i])
	if student_data == "":
		break
		

print("\n")

################# print data in table ################
columns = ["First Name", "Last Name", "Age", "Mark"]
table = PrettyTable()
table.add_column(columns[0], students_first_name)
table.add_column(columns[1], students_last_name)
table.add_column(columns[2], students_age)
table.add_column(columns[3], students_mark)
print("STUDENTS LIST" "\n")
print(table)
print()
################# print data in table ################



