x = float(input('x = '))

if 0 < x < 8:
    print("Value is in range, let's continue")
    y = 2 * x - 6
    if y > 0:
        print('y is positive')
    elif y < 0:
        print('y is negative')
    else:
        print('y = 0')