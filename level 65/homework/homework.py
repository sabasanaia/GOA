def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def to_jaden_case(string):
    sr = []
    se = string.split(" ")
    for i in se:
        sr.append(i.capitalize())
    return " ".join(sr)

def sum_two_smallest_numbers(numbers):
    numbers.sort()
    return numbers[0] + numbers[1]

4) https://www.codewars.com/kata/56606694ec01347ce800001b/train/python

#ვაკეთებდი ვერ გავიგე მხოლოდ 14 არასწორი იყო
def is_triangle(a, b, c):
    if a or b or c < 0:
        return False
    if a and b and c > 0:
        return True

