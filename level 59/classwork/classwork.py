1)https://www.codewars.com/kata/576bb71bbbcf0951d5000044/train/python

def are_you_playing_banjo(name):
    if name[0].lower() == "r":
        return name + " plays banjo" 
    else:
        return name + " does not play banjo" 

def simple_multiplication(number) :
    if number % 2 == 0:
        return number * 8
    else:
        return number * 9

def invert(lst):
    list = []
    for i in lst:
        i *= -1
        list.append(i)
    return list

def grow(arr):
    multiply = 1
    for i in arr:
        multiply *= i
    return multiply

def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i,'')
    return string_

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]