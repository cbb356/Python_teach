class My_Exception(Exception):
    pass

def func():
    while True:
        x = input('Input value: ')
        if x == 'exit':
            raise My_Exception('Exiting')

def main():
    try:
        func()
    except My_Exception as error:
        print(error)

if __name__ == '__main__':
    main()
