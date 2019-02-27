class Base:
    def method(self):
        print("Base method on", type(self).__name__ )

class Child(Base):
    def method(self):
        Base.method(self)
        super(Child, self).method()
        super().method()    # = super(Child, self).method()
        print("Child method on", type(self).__name__ )


def main():
   base = Base()
   base.method()
   child = Child()
   child.method()
   Base.method(child)


if __name__ == "__main__":
    main()
