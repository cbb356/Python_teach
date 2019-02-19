my_list = []

size = int(input("Enter size: "))

for i in range(size):
    my_list.append(input("Enter element: "))

print(my_list[::-1])