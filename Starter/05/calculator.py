def add (x, y):
    return x + y


def sub (x, y):
    return x - y


def mult (x, y):
    return x * y


def div (x, y):
    if y == 0:
        print('Incorrect operation (division by zero)')
    else:
        return x / y


def calc(x, operator, y):
    result = None
    if operator == '+':
        result = add(x, y)
    elif operator == '-':
        result = sub(x, y)
    elif operator == '*':
        result = mult(x, y)
    elif operator == '/':
        result = div(x, y)
    else:
        print('Unsupported operation')

    if result is not None:
        print('Result:', result)


def input_output():
    x = input("Input first number or 'exit':")
    if x == "exit":
        return "exit"
    operator = input("Input operation or 'exit':")
    if operator == "exit":
        return "exit"
    y = input("Input second number or 'exit':")
    if y == "exit":
        return "exit"
    return calc(float(x), operator, float(y))

    
def main():
    while True:
        if input_output() == "exit":
            break
        else:
            print()


if __name__ == "__main__":
    main()
