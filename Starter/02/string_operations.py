string1 = 'Sample string'
string2 = 'Second string'

print(string1, string2)
print(string1+string2)
print(string1+' '+string2)

print(string1[0])
print(string1[1])
print(string1[2])

print('See on strings: %s and %s' % (string1, string2))
print('See on strings: {} and {}'.format(string1, string2))

string3 = 'Number is:'
x = 5.19
y = 4
print('%s %d' % (string3, x))
print('{} {:f}'.format(string3, x))
print('{} {:5.1f}'.format(string3, x))
print('{1} {1:5.1f}'.format(string3, x))
print('{} {}'.format(x, y))
print('{1} {0}'.format(x, y))