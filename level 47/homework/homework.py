# 8 kyu
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
    
def rain_amount(mm):
    if mm >= 40:
         return "Your plant has had more than enough water for today!"
    elif mm < 40:
         return f"You need to give your plant {40 - mm}mm of water"

def lovefunc( flower1, flower2 ):
    if flower1 % 2 != 0 and flower2 % 2 == 0:
        return True
    elif flower2 % 2 != 0 and flower1 % 2 == 0:
        return True
    else:
        return False
    
# 7kyu
def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        
    return f"{max(numbers)} {min(numbers)}"

def get_count(sentence):
    result = []
    for i in sentence:
        if i == "a":
            result.append(i)
        elif i == "e":
            result.append(i)
        elif i == "i":
            result.append(i)
        elif i == "o":
            result.append(i)
        elif i == "u":
            result.append(i)
    return len(result)

#6kyu

def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        else:
            continue
    return sum