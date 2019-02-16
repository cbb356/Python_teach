n = int(input("Enter integer number: "))

r = 1
for i in range (n):
    r = r * (i + 1)

print(("{}! = {}").format(n, r))