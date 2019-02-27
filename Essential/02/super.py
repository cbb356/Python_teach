class MethodContainer:
    def __init__(self, data):
        self.data = data
    def method(self):
        print("Method involved")
        print("data = ", self.data)

def main():
    instance = MethodContainer(3)
    print(type(MethodContainer.method))
    print(type(instance.method))
    instance.method()

if __name__ == "__main__":
    main()
