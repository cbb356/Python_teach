def check_instance(obj, cls):
    return cls in type(obj).mro()

def check_subclass(child, base):
    return base in child.mro()

def check_subclass_bases(child, base):
    if child == base:
        return True

    for direct_base in child.__bases__:
        if base == direct_base:
            return True
        return check_subclass(direct_base, base)

    return False


def main():
    print(check_instance(8, int))
    print(check_instance(8, str))
    print(check_instance("8", str))
    print(check_instance(True, int))
    print(check_instance("True", object))
    print(isinstance(8, int))
    print()

    print(check_subclass(bool, int))
    print(check_subclass(int, object))
    print(check_subclass(bool, str))
    print(issubclass(bool, str))
    print(check_subclass(bool, bool))
    print(issubclass(bool, bool))
    print()

    print(check_subclass_bases(bool, int))
    print(issubclass(bool, int))
    print(check_subclass_bases(bool, str))
    print(issubclass(bool, str))
    print(check_subclass_bases(bool, bool))
    print(issubclass(bool, bool))

if __name__ == "__main__":
    main()
