string1 = "String"
string2 = 'String'
string3 = 'Str' + "ing"

print(string1, string2, string3)
print(string1 == string2)
print(string1 is string2)
print(string1 == string3)
print(string1 is string3)

string4 = 'First line'\
    'Second line'
string5 = 'First line\
    Second line'
string6 = 'First line\nSecond line'
string7 = 'First line\"Second line'
string8 = """multiline text
second line
        indent
4th line"""
print(string4)
print(string5)
print(string6)
print(string7)
print(string8)