import math

x = float(input('x = '))

if x >= - math.pi and x <= math.pi:
    y = math.cos(x)
else:
    y = x

print('y =', y)