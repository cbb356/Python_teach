def main():

    def func():
        try:
            raise ValueError('value is incorrect')
        except ValueError as error:
            print('Exceprtion', error)
            raise

    try:
        func()
    except ValueError:
        print('Value error detected')
    

        
if __name__ == "__main__":
    main()



