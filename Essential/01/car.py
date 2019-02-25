class Car:
    def __init__(self, number):
        self.number = number
    def __repr__(self):
        return "Car #{}".format(self.number)
    def __str__(self):
        return "Car is {}".format(self.number)
    def __eq__(self, other):
        return self.number == other.number

class Salon:
    cars = [Car(1), Car(2), Car(2), Car(3), Car(3), Car(5), Car(3)]

    def add_car(self, number):
        self.cars.append(Car(number))

    def sell_a_car(self, number):
        for i in self.cars:
            if i == Car(number):
                self.cars.remove(i)
                break

    def sell_all_cars(self, number):
        while Car(number) in self.cars:
            self.cars.remove(Car(number))


salon = Salon()
print(salon.cars)
salon.add_car(4)
print(salon.cars)
salon.sell_a_car(3)
print(salon.cars)
salon.sell_all_cars(2)
print(salon.cars)