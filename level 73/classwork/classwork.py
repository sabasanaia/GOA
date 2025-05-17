def printer_error(s):
    count = 0
    alf = 'abcdefghijklm'
    
    for i in s:
        if i not in alf:
            count += 1
    return f"{count}/{len(s)}"

2) https://www.codewars.com/kata/5648b12ce68d9daa6b000099/train/python

def dont_give_me_five(start,end):
    result = []
    for i in range(start,end + 1):
        if "5" not in str(i):
            result.append(i)
    return len(result)

def array_diff(a, b):
    return [i for i in a if i not in b]

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    if walk.count('n') != walk.count('s'):
        return False
    if walk.count('w') != walk.count('e'):
        return False
    return True

6) https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

def unique_in_order(sequence):
    res = []
    res1 = ""
    for i in sequence:
        if i != res1:
            res.append(i)
            res1 = i
    return res 