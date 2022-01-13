from os import system

students_first_name = []
students_last_name = []
students_age = []
students_mark = []

while True:
	system("clear")
	student_data = input("Enter students data ")
	x =student_data.split()
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
print( "index ", "first name", "  last name", "    age", "    mark")

for i in range( len( students_first_name ) ):
	
	print("", i+1,".  " ,students_first_name[i], "         ", students_last_name[i], "           ", students_age[i], "      ", students_mark[i])