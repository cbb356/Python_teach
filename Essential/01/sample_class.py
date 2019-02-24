class MyClass:
    int_field = 8
    string_field = "a string"

print(MyClass.int_field)
print(MyClass.string_field)

object1 = MyClass()
object2 = MyClass()

print(object1.int_field)
print(object2.string_field)

MyClass.int_field = 10

print(MyClass.int_field)
print(object1.int_field)

object1.string_field = "another string"

print(MyClass.string_field)
print(object1.string_field)
print(object2.string_field)

object2.string_field = 5
print(object2.string_field)
