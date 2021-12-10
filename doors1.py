PIN_1_DOOR = "1234"
PIN_2_DOOR = "5678"

pin_1_door = input("Enter PINCOD 1: ")
lock_1_open  = pin_1_door == PIN_1_DOOR

if lock_1_open:
    pin_2_door = input("Enter PINCOD 2: ")
    if pin_2_door == PIN_2_DOOR:
        print("Door is open")
    else:
        while pin_2_door !=  PIN_2_DOOR:
            print("PINCOD_2 EROR, Please try again")
            pin_2_door = input("Enter PINCOD 2: ")
            if pin_2_door == PIN_2_DOOR:
                print("Door is open")   
else :
    while pin_1_door !=  PIN_1_DOOR:
        print("PINCOD_1 EROR, Please try again")
        pin_1_door = input("Enter PINCOD 1: ")
        if pin_1_door == PIN_1_DOOR:
            pin_2_door = input("Enter PINCOD 2: ")
            if pin_2_door == PIN_2_DOOR:
                print("Door is open")
            else:
                while pin_2_door !=  PIN_2_DOOR:
                    print("PINCOD_2 EROR, Please try again")
                    pin_2_door = input("Enter PINCOD 2: ")
                    if pin_2_door == PIN_2_DOOR:
                        print("Door is open")