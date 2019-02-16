def hello_name(name="Andrew"):
    print("Hello, ", name, "!\n", sep="")

def input_name():
    name = input("Enter name or 'exit': ")
    return name

def exit():
    print("Exit...")
    
def main():
    while True:
        text = input_name()
        if text == "exit":
            exit()
            break
        elif text == "":
            hello_name()
        else:
            hello_name(text)
                    
if __name__ == "__main__":
    main()
        
