my_list = [5, 17, 26, 3, 6, 1]

value = int(input("Enter a number: "))
if value in my_list:
    print("Number in list")
else:
    print("Number is out of list")

print([5, 17, 26] in my_list)