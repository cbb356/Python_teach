for attempt_left in range(3, 0, -1):
    password = input(('Enter you password (you have {} attempts left): ').format(attempt_left))
    if password == '1':
        print('Access granted')
        break
else:
    print('Access denied.')