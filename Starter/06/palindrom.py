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

def reverse_cycle_rev(string):
    str = ''
    for i in reversed(string):
        str = str + i
    return str

def no_spaces(string):
    str = ''
    for i in (string):
        if i != " ":
            str += i
    return str


s = no_spaces(input("Enter phrase: "))
print(pal(s))
print(s == reverse_rec(s))
print(s == reverse_cycle(s))
print(s == reverse_cycle_rev(s))
    
