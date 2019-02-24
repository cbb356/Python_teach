class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = object.__new__(cls)

        return cls._instance

    def __init__(self):
        self.value = "some value"


print(Singleton._instance)
obj1 = Singleton()
print(obj1)
print(Singleton._instance)
obj2 = Singleton()
print(obj2)
