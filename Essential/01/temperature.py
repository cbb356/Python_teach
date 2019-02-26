class Temperature:
    def __init__(self, celsius=0):
        self._celsius = celsius
        self._fahrenheit = celsius * 9/5 + 32

    def __str__(self):
        return "Temperature is {:.1f} C or {:.1f} F".format(self._celsius, self._fahrenheit)

    @property
    def celsius(self):
        return "Temperature is {:.1f} C".format(self._celsius)

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._fahrenheit = value * 9/5 + 32

    @property
    def fahrenheit(self):
        return "Temperature is {:.1f} F".format(self._fahrenheit)

    @fahrenheit.setter
    def fahrenheit(self, value):
        self._celsius = (value - 32) / (9/5)
        self._fahrenheit = value

def main():
    t = Temperature()
    print(t)
    t = Temperature(15)
    print(t)
    t.celsius = 10
    print(t)
    print(t.celsius, t.fahrenheit)
    t.fahrenheit = 30
    print(t)
    print(t.celsius, t.fahrenheit)

if __name__ == "__main__":
    main()