a = float(input("Input a: "))
b = float(input("Input b: "))
c = float(input("Input c: "))

d2 = (b**2 - 4*a*c)
d = d2**0.5
x1 = (-b + d)/(2*a)
x2 = (-b - d)/(2*a)

if d2 < 0:
    print('There are no regular roots')
elif d2 == 0:
    print('x = ', x1)
else:
    print("x1 = {}, x2 = {}".format(x1, x2))