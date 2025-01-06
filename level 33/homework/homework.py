# 1)შექმენით სია, სადაც გექნებათ 5 ელემენტი. წაშალეთ სიის მე-3 ელემენტი და დაამატეთ ახალი მე-0 ინდექსზე. საბოლოოდ დააბრუნეთ ეს სია
list = [1,2,3,4,5]
list.pop(2)
list.insert(0,0)
print(list)
# 2)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა ორი რიცხვი შემდეგ ,პირველი რიცხვი აიყვანეთ მეორე რიცხვის ხარისხში და დააბრუნეთ
def numbers_2(number1,number2):
    return number1**number2
print(numbers_2(1,3))
# 3)შექმენით ფუნქცია რომელსაც არგუმენტად გადაეცემა სია შემდეგ უნდა შეამოწმოთ ამ სიის სიგრძე თუ ლუწია დააბრუნეთ --> List length is even, ხოლო სხვა შემთხვევაში დააბრუნეთ --> List length is odd
def even_or_odd(lst):
    if len(lst) % 2 == 0:
        return "List length is even"
    else:
        return "List length is odd"
print(even_or_odd([1,2,3,4,5,6,7,7,7,7]))
#--------------------------------------------------------------CODEWARS-------------------------------------------------------------------------------
def double_integer(i):
    return i * 2

def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend

def grow(arr):
    multiply = 1
    for i in arr:
        multiply *= i
    return multiply

def find_average(numbers):
    sum = 0
    if numbers == []:
        return 0
    for i in numbers:
        sum += i
    return sum / len(numbers)

def goals(laliga, copadelrey, championsleague):
    return laliga + copadelrey + championsleague

def double_char(s):
    e = ""
    for i in s:
        e += i * 2
    return e

def remove_url_anchor(url):
    result = ""
    for i in url:
        if i == "#":
            break
        else:
            result += i
    return result

def sum_cubes(n):
    sum = 0
    for i in range(1,n+1):
        sum += i**3
    return sum
