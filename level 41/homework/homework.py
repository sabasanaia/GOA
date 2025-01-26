def paperwork(n, m):
    if n < 0 or m < 0:
        return 0
    else:
        return n * m
    
def past(h, m, s):
    return h * 3600000 + m * 60000 + s * 1000

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9
    
def abbrev_name(name):
    name = name.split(" ")
    return name[0][0].upper() + "." + name[1][0].upper()

def minimum(arr):
    return min(arr)
def maximum(arr):
    return max(arr)

def reverse_seq(n):
    result = []
    for i in range(n,0,-1):
        result.append(i)
    return result

def is_even(n): 
    return n % 2 == 0

def is_divisible(n,x,y):
    return n % x == 0 and n % y == 0

def greet(name, owner):
    if name == owner:
        return "Hello boss"
    else:
        return "Hello guest"

def remove_exclamation_marks(s):
    return s.replace("!","")