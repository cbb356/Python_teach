class MyObject:
    def __init__(self):
        self.__private_attribute = 42
    def get_private(self):
        return self.__private_attribute
    def set_attribute(self, value):
        if value < 100:
            self.__private_attribute = value
    

obj = MyObject()
print(obj.get_private())
print(obj._MyObject__private_attribute)
obj.set_attribute(int(input("Enter value: ")))
print(obj.get_private())

