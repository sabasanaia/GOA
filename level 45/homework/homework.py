def format_money(amount):
    return f"${amount:.2f}"

def same_case(a, b): 
    if a.islower() and b.islower():
        return 1
    elif a.isalpha() == False or b.isalpha() == False:
        return -1        
    elif a.isupper() and b.isupper():
        return 1
    elif a.islower() and b.islower() == False:
        return 0
    elif a.isupper() and b.isupper() == False:
        return 0

def sum_mul(n, m):
    sum = 0
    if n <= 0 or m <= 0:
        return "INVALID"
    for i in range(n,m,n):
        sum += i
    return sum

def multiple_of_index(arr):
    result = []
    for i in range(len(arr)):
        if arr[i] == 0 and i == 0:
            result.append(arr[i])
        elif i != 0 and arr[i] % i == 0:
            result.append(arr[i])
    return result    

def calculate_age(year_of_birth, current_year):
    sum = current_year - year_of_birth
    if sum == 0:
        return "You were born this very year!"
    elif sum == -1:
        return f"You will be born in {sum * -1} year."
    elif sum < 0:
        return f"You will be born in {sum * -1} years."
    elif sum == 1:
        return f"You are {sum} year old."
    return f"You are {sum} years old."