def to_jaden_case(string):
    list = string.split(" ")
    result = []
    for string in list:
        result.append(string.capitalize())
    return " ".join(result)
    
        
def sequence_sum(begin_number, end_number, step):
    sum = 0
    for i in range(begin_number,end_number + 1,step):
        sum += i
    return sum

def lowercase_count(string):
    count = 0
    lower_letters = "qwertyuiopasdfghjklzxcvbnm"
    for i in string:
        if i in lower_letters:
            count += 1
    return count

def better_than_average(class_points, your_points):
    sum = 0
    for i in range(len(class_points)):
        sum += class_points[i]
    average = sum / len(class_points)
    return average < your_points

def grow(arr):
    multiply = 1
    for i in arr:
        multiply *= i
    return multiply

def smash(words):
    return " ".join(words)

#---------------------------------------------------------------- manual join------------------------------------------------------------------------
def manual_join(lst,separator):
    result = ""
    for i in range(len(lst)):
        if i != len(lst) - 1:
            result += lst[i] + separator
        else:
            result += lst[i]
    return result
print(manual_join(["hello","i","am","12","years","old"]," "))

result = ""
lowercase_count
