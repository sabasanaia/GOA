def arithmetic(a, b, operator):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b

def is_anagram(test, original):
    x = test.lower()
    y = original.lower()
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def count_by(x, n):
    list = []
    for i in range(x,x*n+1,x):
        list.append(i)
    return list

def other_angle(a, b):
    return 180 - a - b

def sum_even_numbers(seq): 
    result_sum = []
    for i in seq:
        if i % 2 == 0:
            result_sum.append(i)
        elif i % 2 != 0:
            continue
    return int(sum(result_sum))

def human_years_cat_years_dog_years(human_years):
    if human_years > 2:
        return [human_years, (human_years - 2) * 4 + 24, (human_years - 2) * 5 + 24]
    elif human_years == 2:
        return [human_years, 24, 24]
    else:
        return [human_years, 15, 15]

def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return "0"
    if len(a) == 0:
        a = 0
    if len(b) == 0:
        b = 0
    return str(int(a) + int(b))

8) https://www.codewars.com/kata/563cf89eb4747c5fb100001b/train/python