def print_info(object_name="unknown object", color="unknown", price=0):
    print("Object:", object_name, sep="\t")
    print("Color:", color, sep="\t")
    print("Price", price, sep="\t")
    print()
        
def main():
    print_info("pen", "blue", 1)
    print_info(object_name="pen", color="blue", price=1)
    print_info(color="blue", object_name="pen", price=1)
    print_info("coffee", price = 2, color="black")
    print_info("coffee", color="black")
    print_info(color="black")
    print_info()
            
if __name__ == "__main__":
    main()
        
