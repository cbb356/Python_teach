import math

result = None

x = float(input('Input first number:'))
operator = input('Input operation:')

if operator != 'sin' and operator != 'cos' and operator != 'tan':
    y = float(input('Input second number:'))

if operator == '+':
    result = x + y
elif operator == '-':
    result = x - y
elif operator == '*':
    result = x * y
elif operator == '/' and y == 0:
    print('Incorrect operation (division by zero)')
elif operator == '/':
    result = x / y
elif operator == '^':
    result = x ** y
elif operator == 'sin':
    result = math.sin(x)
elif operator == 'cos':
    result = math.cos(x)
elif operator == 'tan':
    result = math.tan(x)
else:
    print('Unsupported operation')

if result is not None:
    print('\nResult:', result)

