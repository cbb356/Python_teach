def main():

    def func():
        try:
            raise ValueError
        except ZeroDivisionError:
            print('Division by 0')

    try:
        func()
    except ValueError:
        print('Value error')
    

        
if __name__ == "__main__":
    main()



