class Graphic_Object:
    def __str__(self):
        return self.__class__.__name__

class Rectangle(Graphic_Object):
    def __init__(self, width, height):
        self.width = width
        self.height = height

class Clickable:
    def on_click(self):
        print(self.__class__.__name__, "clicked")

class Button(Rectangle, Clickable):
    def __init__(self, width=20, height=5):
        super().__init__(width, height)

def main():
    rect = Rectangle(10, 15)
    print(rect)
    button = Button()
    print(button)
    button.on_click()
    
  
if __name__ == '__main__':
    main()
