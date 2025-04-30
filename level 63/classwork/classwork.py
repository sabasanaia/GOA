def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i,'')
    return string_

def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        
    return f"{max(numbers)} {min(numbers)}"

