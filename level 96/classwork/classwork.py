1) https://www.codewars.com/kata/529b418d533b76924600085d/train/python

def generate_hashtag(s):
    result = []
    for i in s:
        if i == " ":
            continue # i tried what i could but mostly this code doesnt work i coldnt come up whit a diffrent code
        if i.isalpha() == True:
            result.append(i)
    result1 = "".join(result)
    return f"#{result1.capitalize()}"

def count_repeats(txt):
    result = 0
    
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            result += 1
    
    return result

def string_transformer(s):
    result = []
    for i in s:
        if i == i.lower():
            result.append(i.upper())
        elif i == i.upper(): # i tried what i could but mostly this code doesnt work i coldnt come up whit a diffrent code
            result.append(i.lower())
    return " ".join(result)