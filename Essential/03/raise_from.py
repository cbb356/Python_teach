def main():
    a = 5
    b = 0
    
    try:
        result = a / b
    except ZeroDivisionError as error:
        raise ValueError('invalid b') from error


if __name__ == "__main__":
    main()



