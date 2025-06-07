def sum_digits(number):
    sum = 0
    if number < 0:
        number *= -1
    for i in str(number):
        sum += int(i)
    return sum

2) https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

def sort_gift_code(code):
    return "".join(sorted(code))

def spin_words(sentence):
    result = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)

5) დამატებით გააკეთეთ 5 ცალი 6kyu ამოცანა