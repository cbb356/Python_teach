class Temperature:
    def __init__(self):
        self._celsius = 0
        self._farenheit = 0

    def __str__(self):
        return "Temperature is {:.1f} C or {:.1f} F".format(self._celsius, self._farenheit)

    @property
    def celsius(self):
        return "Temperature is {:.1f} C".format(self._celsius)

    @celsius.setter
    def celsius(self, value):
        self._celsius = value
        self._farenheit = value * 9/5 + 32

    @property
    def farenheit(self):
        return "Temperature is {:.1f} F".format(self._farenheit)

    @farenheit.setter
    def farenheit(self, value):
        self._celsius = (value - 32) / (9/5)
        self._farenheit = value

def main():

    t = Temperature()
    print(t)
    t.celsius = 10
    print(t)
    print(t.celsius, t.farenheit)
    t.farenheit = 30
    print(t)
    print(t.celsius, t.farenheit)

if __name__ == "__main__":
    main()