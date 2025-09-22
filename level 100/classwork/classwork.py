def feast(beast, dish):
    dish1 = dish.split()
    for i in beast:
        if i == dish1[0] and dish[-1]:
            return True
        else:
            return False # უმეტესობა მუშაობს მაგრამ რაღაცა აკლია და არ ვიცი რა დავამატო


def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2)

3) https://www.codewars.com/kata/5865918c6b569962950002a1/train/python

def sum_digits(number):
    sum = 0
    if number < 0:
        number *= -1
    for i in str(number):
        sum += int(i)
    return sum

5) https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python


def count_repeats(txt):
    result = 0
    
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            result += 1
    
    return result