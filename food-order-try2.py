# menu
food_1_name      = 'Pizza'
food_2_name      = 'Shaurma'
drink_name       = 'Juice'
food_1_price     = 100   
food_2_price     = 40
drink_price      = 15
# quantity available 
food_1_available = 5
food_2_available = 30
drink_available  = 40

# the dialog window

print("Hello and Welcome in our Bistro! \nHere you can enjoy a " + food_1_name + " or a " + food_2_name + " and drink a " + drink_name)
print("key words in this app is "+" 'Pizza' " + " 'Shaurma' " + " 'Juice' " + " 'yes' " + " 'not' ")
   
# place first order

order_place_1 = input('What would you like  ')

if order_place_1 == food_1_name:
    quantity_1 = input ("How many " + food_1_name + " you want ")
    if int(quantity_1) < 0 or int(quantity_1) > food_1_available:
        print("Sorry but our quantity avialable is " + str(food_1_available) )
        quantity_1 = input ("How many " + food_1_name + " you want ")
elif order_place_1 == food_2_name:
    quantity_2 = input ("How many " + food_2_name + " you want ")
    if int(quantity_2) < 0 or int(quantity_2) > food_2_available:
        print("Sorry but our quantity avialable is " + str(food_2_available) )
        quantity_2 = input ("How many " + food_2_name + " you want ")
else:
    quantity_3 = input ("How many " + drink_name + " you want ")
    if int(quantity_3) < 0 or int(quantity_3) > drink_available:
        print("Sorry but our quantity avialable is " + str(drink_available) )
        quantity_3 = input ("How many " + drink_name + " you want ")

# place second order

order_place_2 = input('Anything else (please enter any our product or "not") ')

if order_place_2 == food_1_name:
    quantity_1 = input ("How many " + food_1_name + " you want ")
    if int(quantity_1) < 0 or int(quantity_1) > food_1_available:
        print("Sorry but our quantity avialable is " + str(food_1_available) )
        quantity_1 = input ("How many " + food_1_name + " you want ")
elif order_place_2 == food_2_name:
    quantity_2 = input ("How many " + food_2_name + " you want ")
    if int(quantity_2) < 0 or int(quantity_2) > food_2_available:
        print("Sorry but our quantity avialable is " + str(food_2_available) )
        quantity_2 = input ("How many " + food_2_name + " you want ")
elif order_place_2 == drink_name:
    quantity_3 = input ("How many " + drink_name + " you want ")
    if int(quantity_3) < 0 or int(quantity_3) > drink_available:
        print("Sorry but our quantity avialable is " + str(drink_available) )
        quantity_3 = input ("How many " + drink_name + " you want ")      
elif order_place_2 == "not":
    print("Thanks for your order")
  
# third order place

if order_place_1 == food_1_name and order_place_2 == food_2_name:
    order_place_3 = input("Would you like a " + drink_name + "(please enter yes or not) " )
    if order_place_3 == "yes":
        quantity_3 = input ("How many " + drink_name + " you want ")
        print("Thanks for your order")
        if int(quantity_3) < 0 or int(quantity_3) > drink_available:
            print("Sorry but our quantity avialable is " + str(drink_available) )
            quantity_3 = input ("How many " + drink_name + " you want ")
            print("Thanks for your order")
        food_cost = int(quantity_1) * food_1_price + int(quantity_2) * food_2_price + int(quantity_3) * drink_price
        command = str(quantity_1) + 'x ' + food_1_name + ', ' + str(quantity_2) + 'x ' + food_2_name + ', ' + str(quantity_3) + 'x ' + drink_name
    else:
        print("Thanks for your order")
        food_cost = int(quantity_1) * food_1_price + int(quantity_2) * food_2_price
        command = str(quantity_1) + 'x ' + food_1_name + ', ' + str(quantity_2) + 'x ' + food_2_name

elif order_place_1 == food_1_name and order_place_2 == drink_name:
    print("Thanks for your order")
    food_cost = int(quantity_1) * food_1_price + int(quantity_3) * drink_price
    command = str(quantity_1) + 'x ' + food_1_name + ', ' + str(quantity_3) + 'x ' + drink_name     

elif order_place_1 == food_1_name and order_place_2 == "not":
    food_cost = int(quantity_1) * food_1_price
    command = str(quantity_1) + 'x ' + food_1_name
    
elif order_place_1 == food_2_name and order_place_2 == food_1_name:
    order_place_3 = input ("Would you like a " + drink_name + "(please enter yes or not) " )
    if order_place_3 == "yes":
        quantity_3 = input ("How many " + drink_name + " you want ")
        if int(quantity_3) < 0 or int(quantity_3) > drink_available:
            print("Sorry but our quantity avialable is " + str(drink_available) )
            quantity_3 = input ("How many " + drink_name + " you want ")
            print("Thanks for your order")
        food_cost = int(quantity_1) * food_1_price + int(quantity_2) * food_2_price + int(quantity_3) * drink_price
        command = str(quantity_2) + 'x ' + food_2_name + ', ' + str(quantity_1) + 'x ' + food_1_name + ', ' + str(quantity_3) + 'x ' + drink_name
    else:
        print("Thanks for your order")
        food_cost = int(quantity_1) * food_1_price + int(quantity_2) * food_2_price
        command = str(quantity_2) + 'x ' + food_2_name + ', ' + str(quantity_1) + 'x ' + food_1_name
    
elif order_place_1 == food_2_name and order_place_2 == drink_name:
    print("Thanks for your order")
    food_cost = int(quantity_2) * food_2_price + int(quantity_3) * drink_price
    command = str(quantity_2) + 'x ' + food_2_name + ', ' + str(quantity_3) + 'x ' + drink_name
    
elif order_place_1 == food_2_name and order_place_2 == "not":
    food_cost = int(quantity_2) * food_2_price
    command = str(quantity_2) + 'x ' + food_2_name 

elif order_place_1 == drink_name and order_place_2 == food_1_name:
    print("Thanks for your order")
    food_cost = int(quantity_1) * food_1_price + int(quantity_3) * drink_price
    command = str(quantity_1) + 'x ' + food_1_name + ', ' + str(quantity_3) + 'x ' + drink_name

elif order_place_1 == drink_name and order_place_2 == food_2_name:
    print("Thanks for your order")
    food_cost = int(quantity_2) * food_2_price + int(quantity_3) * drink_price
    command = str(quantity_3) + 'x ' + drink_name + ', ' + str(quantity_2) + 'x ' + food_2_name

elif order_place_1 == drink_name and order_place_2 == "not":
    food_cost = int(quantity_3) * drink_price
    command = str(quantity_3) + 'x ' + drink_name


# print payment order

payment_order = 'You have ordered ' + command +  ' in the total amount of ' + str(food_cost) + ' mdl'
print(payment_order)

# delivery or not

delivery = input("You need delivery? (yes/not) ")
if delivery == "yes":
    if food_cost >= 1000:
        print("Beacouse your order > 1000 mdl delivery is free!")
        input("Put your adress ")
        print("Thank you for choosing our Bistro, Good Luck!")
    else:
        total_payment_order = food_cost + 150
        print("Beacouse your order < 1000 mdl delivery cost is 150 mdl and total payment order is " + str(total_payment_order) )
        input("Put your adress ")
        print("Thank you for choosing our Bistro, Good Luck!")
else:
    print("Thank you for choosing our Bistro, Good Luck!")