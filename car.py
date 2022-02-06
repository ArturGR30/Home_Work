# car module



def createCar(brand, model, year):
    car = {}

    car["brand"] = brand
    car["model"] = model
    car["year"]  = year

    return car


def printCarInfo(car):
    print("#"*50)
    print(f"# {car['brand']} / {car['model']} ({car['year']}) ")
    print("#"*50)


def printCarListInfo(cars):
    for c in cars:
        printCarInfo(c)
        
