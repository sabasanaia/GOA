

def find_average(nums):
    return sum(nums) / len(nums)

def no_boring_zeros(n):
    if n == 0:
        return 0
    while n % 10 == 0:
        n //= 10
    return n

def final_grade(exam, projects):
    if exam > 90 or projects > 10:
        return 100
    elif exam > 75 and projects >= 5:
        return 90
    elif exam > 50 and projects >= 2:
        return 75
    else:
        return 0
    
def maps(a):
    for i in range(len(a)):
        a[i] = a[i] * 2
    return a

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

def hero(bullets, dragons):
    return bullets >= dragons * 2
