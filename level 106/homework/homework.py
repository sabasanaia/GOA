def greet():
    return "hello world!"

def count_sheeps(sheep):
    return sheep.count(True)

def basic_op(operator, value1, value2):
    if operator == "-":
        return value1 - value2
    elif operator == "*":
        return value1 * value2
    elif operator == "/":
        return value1 / value2
    elif operator == "+":
        return value1 + value2

4) https://www.codewars.com/kata/5a3fe3dde1ce0e8ed6000097/train/javascript


def sum_array(a):
    if a == []:
        return 0
    return sum(a)


def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo" 