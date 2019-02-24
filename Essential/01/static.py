class MyObject:
    class_attribute = 9

    def __init__(self):
        self.data_attribute = 43

    def instance_method(self):
        print(self.data_attribute)

    @staticmethod
    def static_method():
        print(MyObject.class_attribute)

MyObject.static_method()
obj = MyObject()
obj.instance_method()
obj.static_method()
