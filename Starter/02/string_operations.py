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

x = 5.17
print('Number is %d' % (x))
print('Number is {:f}'.format(x))
print('Number is {}'.format(x))