def outer_function():
    def inner_function():
        def deep_function():
            print("Deep function")
        print("Inner function")
        deep_function()
    print("Outer function")
    inner_function()
    
def main():
    outer_function()
    
if __name__ == "__main__":
    main()
