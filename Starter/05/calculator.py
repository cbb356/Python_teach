def calc(x, operator, y):
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


def input_data():
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

def exit():
    print("Exit...")
    
def main():
    while True:
        if input_data() == "exit":
            exit()
            break
        else:
            print()

if __name__ == "__main__":
    main()
