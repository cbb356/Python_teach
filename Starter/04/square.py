x = int(input("Enter width: "))
y = int(input("Enter height: "))

for i in range(y):
    if i == 0 or i == y - 1:
        for j in range(x):
            print("*", end='')
    else:
        for j in range(x):
            if j == 0 or j == x - 1:
                print("*", end='')
            else:
                print(' ', end='')
    print()


