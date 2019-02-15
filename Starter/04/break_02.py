name = None

while True:
    print('Menu:')
    print('1. Enter name')
    print('2. Print greeting')
    print('3. Quit')

    responce = input('Please choose an action: ')

    print()

    if responce == '1':
        name = input('Enter you name: ')
    elif responce == '2':
        if name:
            print('Hello, ', name, '!', sep='')
        else:
            print("I don't know your name.")
    elif responce == '3':
        break
    else:
        print('Incorrect input')

    print()