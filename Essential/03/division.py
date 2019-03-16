def main():
    while True:
        try:
            a = float(input("first number:"))
            b = float(input("second number:"))
            print("Result:", a/b)
            break
        except (ZeroDivisionError, ValueError) as error:
            print(error)
            print("Try again")
    
if __name__ == "__main__":
    main()



