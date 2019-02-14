a = float(input("Input a:"))
b = float(input("Input b:"))
c = float(input("Input c:"))

d = (b**2 - 4*a*c)**0.5
x1 = (-b + d)/2*a
x2 = (-b - d)/2*a

print("x1 = {}, x2 = {}".format(x1, x2))