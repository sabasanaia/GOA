def capitals(word):
    list = [] #ცვლადი სადაც შევინაავთ ინდექსებს
    for i in range(len(word)):#გადავუარეთ ინდექსებს
        if word[i].isupper():#ვამოწმებთ თუ ინდექსის ელემენტი დიდი ასოთია დაწერილი
            list.append(i)#ყველა ელემენტი რომელიც დიდ ასოთი არის დწერილი ემატება ლისტს
    return list#ვაბრუნებთ ლისტს

def max_multiple(divisor, bound):
    for i in range(bound,1,-1):
        if i % divisor == 0:
            return i
            
def sum_digits(number):
    sum = 0
    if number < 0:
        number *= -1
    for i in str(number):
        sum += int(i)
    return sum

def dont_give_me_five(start,end):
    result = []
    for i in range(start,end + 1):
        if "5" not in str(i):
            result.append(i)
    return len(result)

def fizzbuzz(n):
    list = []
    for i in range(1,n+1):
        if i % 3 == 0 and i % 5 == 0:
            list.append("FizzBuzz")
        elif i % 3 == 0:
            list.append("Fizz")
        elif i % 5 == 0:
            list.append("Buzz")
        else:
            list.append(i)
    return list

def invert(lst):
    list = []
    for i in lst:
        i *= -1
        list.append(i)
    return list

def sum_array(arr):
    sum = 0
    if arr == None:
        return 0 
    if len(arr) <= 2:
        return 0
    for i in arr:
        sum += i
    return sum - max(arr) - min(arr)