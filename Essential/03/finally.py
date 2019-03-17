import warnings

def main():
    name = input('Enter your first name and last name: ')

    if name.count(' ') != 1:
        warnings.warn('Name format may be incorrect')

    print('Hello, ', name, '!', sep='')

if __name__ == '__main__':
    main()
