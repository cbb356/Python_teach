class Shape:
    def __init__(self, side):
        self.side = side

    def render(self):
        print(self)
        self.draw()
        print()

    def __str__(self):
        return "Abstract figure object"

    def draw(self):
        pass


class Square(Shape):
    def draw(self):
        for i in range(self.side):
            print("* " * self.side)

    def __str__(self):
        return "Square with a side of {!r}".format(self.side)


class Triangle(Shape):
    def draw(self):
        for i in range(1, self.side + 1):
            print("* " * i)

    def __str__(self):
        return "Triangle with a side of {!r}".format(self.side)


def main():
    shapes = [Square(5), Triangle(4), Square(7), Triangle(8)]
    for shape in shapes:
        shape.render()

if __name__ == '__main__':
    main()
