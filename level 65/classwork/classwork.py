1) https://www.codewars.com/kata/57faece99610ced690000165/train/python

2) https://www.codewars.com/kata/55ca43fb05c5f2f97f0000fd/train/python

def integrate(coefficient, exponent):
    exponent = exponent + 1
    return f"{coefficient // exponent}x^{exponent}"

def is_anagram(test, original):
    x = test.lower()
    y = original.lower()
    if sorted(x) == sorted(y):
        return True
    else:
        return False

def break_chocolate(n, m):
    if n <= 0 or m <= 0:
        return 0
    return (n * m) - 1

def in_asc_order(arr):
    if arr == sorted(arr):
        return True
    elif arr != sorted(arr):
        return False

def flatten_and_sort(array):
    res = []
    for i in array:
        res += i
    return sorted(res)