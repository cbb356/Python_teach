def function():
    global var
    var = "first local variable"
    print(var)

def function1():
    global var
    var = "second local variable"
    print(var)
    
def main():
    print(var)
    function()
    function1()
    print(var)
    
var = "global variable"
    
if __name__ == "__main__":
    main()
