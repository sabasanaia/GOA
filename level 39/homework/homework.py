def even_or_odd(number):
    if number % 2== 0:
        return 'Even'
    else:
        return 'Odd'
    
def number_to_string(num):
    return str(num)

def basic_op(operator, value1, value2):
    if operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    elif operator == "+":
        return value1 + value2
    
def digitize(n):
    list = []
    for i in str(n)[::-1]:
        list.append(int(i))
    return list

def greet(name):
    return f"Hello, {name} how are you doing today?" 