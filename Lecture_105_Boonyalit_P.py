class Vehicle:
    licenseCode = ""
    serialCode = ""
    face = ""
    def trunOnAirConditioner(self):
        print("Trun On : Air")

class Car(Vehicle):
    def sayHello(self):
        print("Hello World !")
class Van(Vehicle):
    pass
class Pickup(Vehicle):
    pass
class Estatecar(Vehicle):
    pass

car1 = Car()
car1.trunOnAirConditioner()
car1.sayHello()

van1 = Van()
van1.trunOnAirConditioner()

pickup1 = Pickup()
pickup1.trunOnAirConditioner()

estatecar1 = Estatecar()
estatecar1.trunOnAirConditioner()