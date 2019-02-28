class Vehicle:
    def __init__(self, speed=None, weight=None, color=None):
        self.speed = speed
        self.weight = weight
        self.color = color

    def __str__(self):
        return "Some vehicle with speed: {}, weight: {}, color: {}".format(self.speed, self.weight, self.color)


class Wheeled_Vehicle(Vehicle):
    def __init__(self, speed=None, weight=None, color=None, wheels=None):
        super().__init__(speed, weight, color)
        self.wheels = wheels

    def __str__(self):
        return "Some wheeled vehicle with speed: {}, weight: {}, color: {}, wheels: {}".format(self.speed, self.weight, \
                                                                                               self.color, self.wheels)


class Flying_Vehicle(Vehicle):
    def __init__(self, speed=None, weight=None, color=None, max_height=None):
        super().__init__(speed, weight, color)
        self.max_height = max_height

    def __str__(self):
        return "Some flying vehicle with speed: {}, weight: {}, color: {}, max_height: {}".format(self.speed, self.weight, \
                                                                                                  self.color, self.max_height)


class Auto(Wheeled_Vehicle):
    def __init__(self, speed=None, weight=None, color=None, wheels=4, transmission=None):
        super().__init__(speed, weight, color, wheels)
        self.transmission = transmission

    def __str__(self):
        return "Some auto with speed: {}, weight: {}, color: {}, wheels: {}, transmission: {}".format(self.speed, self.weight, \
                                                                                                      self.color, self.wheels, self.transmission)

class Bike(Wheeled_Vehicle):
    def __init__(self, speed=None, weight=None, color=None, wheels=2, breaks=None):
        super().__init__(speed, weight, color, wheels)
        self.breaks = breaks

    def __str__(self):
        return "Some bike with speed: {}, weight: {}, color: {}, wheels: {}, breaks: {}".format(self.speed, self.weight, \
                                                                                                self.color, self.wheels, self.breaks)


class Plane(Flying_Vehicle):
    def __init__(self, speed=None, weight=None, color=None, max_height=None, supersonic=None):
        super().__init__(speed, weight, color, max_height)
        self.supersonic = supersonic

    def __str__(self):
        return "Some plane with speed: {}, weight: {}, color: {}, max_height: {}, supersonic: {}".format(self.speed, self.weight, \
                                                                                                         self.color, self.max_height, self.supersonic)


class Helicopter(Flying_Vehicle):
    def __init__(self, speed=None, weight=None, color=None, max_height=None, turbine=None):
        super().__init__(speed, weight, color, max_height)
        self.turbine = turbine

    def __str__(self):
        return "Some helicopter with speed: {}, weight: {}, color: {}, max_height: {}, turbine: {}".format(self.speed, self.weight, \
                                                                                                           self.color, self.max_height, self.turbine)


def main():
    vehicles = [Vehicle(), Wheeled_Vehicle(), Flying_Vehicle(), Auto(300, 2000, "red", transmission="Auto"), Bike(20, 30, "blue", breaks="disc"),\
                Plane(2000, 15000, "white", 10000, True), Helicopter(1000, 7000, "green", 2000, True)]
    for vehicle in vehicles:
        print(vehicle)


if __name__ == '__main__':
    main()
