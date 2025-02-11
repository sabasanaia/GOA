def same_case(a, b): 
    if a.islower() == True and b.islower() == True:
        return 1
    elif a.isupper() and b.isupper() == True:
        return 1
    elif a.islower() and b.islower() == False:
        return 0
    elif a.isupper() and b.isupper() == False:
        return 0
    else:
        return -1
    

def calculate_age(year_of_birth, current_year):
    sum = current_year - year_of_birth
    if sum == 0:
        return "You were born this very year!"
    elif sum == -1:
        return f"You will be born in {sum * 1} year."
    elif sum < 0:
        return f"You will be born in {sum * 1} years."
    elif sum == 1:
        return f"You are {sum} year old."
    return f"You are {sum} years old."