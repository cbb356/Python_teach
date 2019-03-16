def main():
    print ("Calculator")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        print (a/b)
    except (ZeroDivisionError, ValueError) as error:
        print(error)
        
    print ("End of program")
    
if __name__ == "__main__":
    main()



