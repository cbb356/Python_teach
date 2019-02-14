string = input('Enter text:')
print('You have entered "{}"'.format(string))
print('You have entered "', string, '"', sep='')

print('Press "Enter" to continue...')
input()

x = int(input('Input first integer number:'))
y = int(input('Input second integer number:'))
print('The sum is: {} + {} = {}'.format(x, y, x+y))
