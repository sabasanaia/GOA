1)https://www.codewars.com/kata/559590633066759614000063/train/python

def is_leap_year(year):
    if year % 4 == 0 and year % 100 != 0:
        return True
    elif year % 400 == 0:
        return True
    else:
        return False


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

5)https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python