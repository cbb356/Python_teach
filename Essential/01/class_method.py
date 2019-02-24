class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return "Rectangle({:.1f}, {:.1f})".format(self.side_a, self.side_b)

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return "Circle({:.1f})".format(self.radius)

    @classmethod
    def from_rectangle(cls, rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0.5 / 2
        return cls(radius)

class Disc(Circle):
    def __repr__(self):
        return "Disc({:.1f})".format(self.radius)

def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    circle1 = Circle(1)
    print(circle1)

    circle2 = Circle.from_rectangle(rectangle)
    print(circle2)

    disc = Disc.from_rectangle(rectangle)
    print(disc)


if __name__ == "__main__":
    main()
