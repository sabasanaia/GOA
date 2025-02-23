def derive(coefficient, exponent): 
    return f"{exponent * coefficient}x^{exponent - 1}" 

def whatday(num):
    if num == 1:
        return "Sunday"
    elif num == 2:
        return "Monday"
    elif num == 3:
        return "Tuesday"
    elif num == 4:
        return "Wednesday"
    elif num == 5:
        return "Thursday"
    elif num == 6:
        return "Friday"
    elif num == 7:
        return "Saturday"
    else:
        return "Wrong, please enter a number between 1 and 7"

def create_array(n):
    res=[]
    i=1
    while i<=n: 
        res+=[i]
        i += 1
    return res

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False

def quote(fighter):
    if fighter.lower() == "conor mcgregor":
        return "I'd like to take this chance to apologize.. To absolutely NOBODY!"
    elif fighter.lower() == "george saint pierre":
        return "I am not impressed by your performance."