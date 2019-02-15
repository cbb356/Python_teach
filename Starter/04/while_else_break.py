attempt_left = 3

while attempt_left > 0:
    attempt_left -= 1
    password = input(('Enter you password (you have {} attempts left): ').format(attempt_left + 1))
    if password == '1':
        print('Access granted')
        break
else:
    print('Access denied.')