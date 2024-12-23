def count_sheeps(sheep):
    return sheep.count(True)

def no_space(x):
    return x.replace(" ","")

def summation(num):
    sum = 0
    for i in range(num + 1):
        sum += i
    return sum
    

def find_smallest_int(arr):
    return min(arr)


def square_sum(numbers):
    sum = 0
    for i in numbers:
        sum += i**2
    return sum

def repeat_str(repeat, string):
    return repeat * string

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

def positive_sum(arr):
    sum = 0
    for i in arr:
        if i > 0:
            sum += i
    return sum

def make_negative( number ):
    if number > 0:
        return -number
    else:
        return number

def opposite(number):
    return number * -1


def greet():
    return "hello world!"