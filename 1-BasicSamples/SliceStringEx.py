class AutoMobile:
    fuel = "gas"

    def __init__(self, brand, cost):
        self.brand = brand
        self.cost = cost

class SportsCar(AutoMobile):

    doors = 2
    seats = 2


class Truck(AutoMobile):

    fuel = "diesel"


Aventador = SportsCar("Lamborghini", 399500)
print("Brand: ", Aventador.brand)
print(Aventador.cost)
print("Doors: ", Aventador.doors)
print("Seats: ", Aventador.seats)
print("--------------")
Ram_1500 = Truck("Dodge", 27095)
print("Brand: ", Ram_1500.brand)
print(Ram_1500.cost)
print(Ram_1500.fuel)

