class MyObject:
    def __del__(self):
        print("Destructor invoked")
        raise Exception

def main():
    print("Creating object...")
    obj = MyObject()

    print("Deleting object...")      
    del obj

    print("Done")
    
if __name__ == "__main__":
    main()



