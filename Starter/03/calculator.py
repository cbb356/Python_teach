import math

x = float(input('Input first number:'))
operator = input('Input operation:')
y = float(input('Input second number:'))

result = None
result1 = None

if operator == '+':
    result = x + y
elif operator == '-':
    result = x - y
elif operator == '*':
    result = x * y
elif operator == '/' and y == 0:
    print('Incorrect operation(division by zero)')
elif operator == '/':
    result = x / y
elif operator == '^':
    result = x ** y
elif operator == 'sin':
    result = math.sin(x)
    result1 = math.sin(y)
elif operator == 'cos':
    result = math.cos(x)
    result1 = math.cos(y)
elif operator == 'tan':
    result = math.tan(x)
    result1 = math.tan(y)
else:
    print('Unsupported operation')

if result is not None:
    print('\nResult:', result, "\n")

if result1 is not None:
    print('Result 1:', result1)