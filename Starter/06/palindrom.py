def pal(string):
    a = []
    b = []
    for i in (string):
        a.append(i)
    for i in reversed(string):
        b.append(i)
    if a == b:
        return True
    else:
        return False

def reverse_rec(string):
    if len(string) == 0:
        return string
    else:    
        return reverse_rec(string[1:]) + string[0]

def reverse_cycle(string):
    str = ''
    for i in string:
        str = i + str
    return str

s = input("Enter phrase: ")
print(pal(s))
print(s == reverse_rec(s))
print(s == reverse_cycle(s))

    
