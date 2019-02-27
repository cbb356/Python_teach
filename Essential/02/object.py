class Base(object):
    def method(self):
        print("Method class:", __class__.__name__)
        print("Instance class:", type(self).__name__)

class Child(Base):
    pass

def main():
    base_instance = Base()
    base_instance.method()

    child_instance = Child()
    child_instance.method()


if __name__ == "__main__":
    main()