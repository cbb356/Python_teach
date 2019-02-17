def first_function(x):
    y = x ** 2
    return y

def second_function(x):
    y = x ** 3
    return y

def loop(imin, imax, step, function):
    print("x", "y", sep="\t")
    for i in range(imin, imax+step, step):
        print (i / 2, function(i / 2), sep="\t")
    print()

def main():
    loop(-10, 10, 1, first_function)
    loop(-10, 10, 1, second_function)
    
if __name__ == "__main__":
    main()
