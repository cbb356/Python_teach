class MyObject:
    def __init__(self):
        self.password = None

    def __getattribute__(self, item):
        if item == "secret_field" and self.password == "123456":
            return "Secret value"
        else:
            return object.__getattribute__(self, item)

obj = MyObject()
print(obj.password)
obj.password = "123456"
print(obj.secret_field)
