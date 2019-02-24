class Car:
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return "Car #{}".format(self.number)

class Salon:
    cars = [Car(1), Car(2), Car(3)]

    def sell_car(self, number):
        for i in self.cars:
            if i == Car(number):
                del self.cars[i]

salon = Salon()
print(salon.cars)
salon.sell_car(3)
print(salon.cars)

    
