def simple(min_limit, max_limit):
    simple_numbers = []
    for i in range(min_limit, max_limit+1):
        if simple_check(i):
            simple_numbers.append(i)
    return simple_numbers

def simple_check(number):
    for i in range(2, number):
        if number % i == 0:
            return False
    return True

def min_limit():
    limit_min = int(input("From: "))
    return limit_min

def max_limit():
    limit_max = int(input("To: "))
    return limit_max

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


result = simple(min_limit(), max_limit())
print(result)
operation(result)
