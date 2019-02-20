def simple_list(limits):
    simple_numbers = []
    for i in range(limits[0], limits[-1]+1):
        if simple_check(i):
            simple_numbers.append(i)
    return simple_numbers

def simple_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def limits():
    limits_temp = []
    limits_out = []
    for i in range(2):
        limits_temp.append(int(input("Input number: ")))
    limits_out.append(min(limits_temp))
    limits_out.append(max(limits_temp))
    return limits_out

def mult_list(list1):
    mult_result = 1
    for i in list1:
        mult_result *= i
    return mult_result

def operation(result):
    add_mult = input("Enter '+' or '*': ")
    if add_mult == "+":
        print("Sum is:", sum(result))
    elif add_mult == "*":
        print("Mult is:", mult_list(result))
    else:
        print("Incorrect operation")


result = simple_list(limits())
print(result)
operation(result)
