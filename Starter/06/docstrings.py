def function():
    """Example function

    This function do nothing
    """
    print("Function called")
        
def main():
    function()
    help(function)
    print(function.__doc__)

if __name__ == "__main__":
    main()
