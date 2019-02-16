def function(x):
    if x < 0:
        return x * 2
    else:
        return x * 3
        
def main():
    while True:
        ki = input("Input number or 'exit': ")
        if ki == "exit":
            print("Exit...")
            break
        x = float(ki)
        print(function(x))
        
if __name__ == "__main__":
    main()
        
