a = int(input("Input first integer: "))
b = int(input("Input second integer: "))

print()

if a < b:
    for i in range(a, b + 1):
        print("i =",i)
else:
    for i in range(b, a + 1):
        print("i =",i)