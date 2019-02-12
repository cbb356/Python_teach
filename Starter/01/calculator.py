x = float(input('Input first number:'))
operator = input('Input operation:')
y = float(input('Input second number:'))

result = None

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
else:
    print('Unsupported operation')

if result is not None:
    print('Result:', result)