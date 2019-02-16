x = int(input("Enter side length: "))

for i in range(x):
    if i == 0 or i == x - 1:
        for j in range(i + 1):
            print("*", end="")
    else:
        print("*", end="")
        for j in range(i - 1):
            print(" ", end="")
        print("*", end="")
    print()
