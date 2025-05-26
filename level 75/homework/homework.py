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
            
def disemvowel(string_):
    for i in "aeiouAEIOU":
        string_ = string_.replace(i,'')
    return string_

def high_and_low(numbers):
    numbers = numbers.split(" ")
    for i in range(len(numbers)):
        numbers[i] = int(numbers[i])
        
    return f"{max(numbers)} {min(numbers)}"