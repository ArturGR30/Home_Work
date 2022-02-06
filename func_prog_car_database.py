# main module
from car import *
from ui import *


is_admin = False

cars = [
    createCar("BMW", "series 3", 2000),
    createCar("BMW", "series 5", 2010),
    createCar("BMW", "series 7", 2020)
]



while True:
    clear()
    if not is_admin:
        option = printClientCarMenu()

        if option == 1:
            printCarListInfo(cars)
            wait()
        elif option == 2:
            createCar()
        elif option == 3:
            pass
        elif option == 4:
            pass
        elif option == 5:
            pass
        elif option == 6:
            pass
        elif option == 7:
            pass
        elif option == 8:
            pass

        if option == 9:
            is_admin = loginAdministrator()
    else:
        option = printAdminCarMenu()
        if option == 9:
            is_admin =False




################!!!!!!!!##############
    