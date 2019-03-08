class Graphic_Object:
    pass

class Rectangle(Graphic_Object):
    pass

class Clickable:
    pass

class Button(Rectangle, Clickable):
    pass

def main():
    print(Graphic_Object.mro())
    print(Rectangle.mro())
    print(Clickable.mro())
    print(Button.mro())

if __name__ == '__main__':
    main()
