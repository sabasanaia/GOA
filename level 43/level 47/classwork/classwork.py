def expression_matter(a, b, c):
    first = a * (b + c)
    second = a * b * c
    third = a + b * c
    forth = (a + b) * c
    fifth = a + b + c
    return max(first,second,third,forth,fifth)



def dup(arry):
    result = []
    for word in arry:
        new_word = ""
        for i in range(len(word)):
            if i == 0 or word[i] != word[i - 1]:
                new_word += word[i]
        result.append(new_word)
    return result

def spin_words(sentence):
    result = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)

def min_value(digits):
    result = []
    for i in sorted(set(digits)):
        result.append(str(i))
    return int("".join(result))

def max_multiple(divisor, bound):
    for i in range(bound,1,-1):
        if i % divisor == 0:
            return i

def alphabetic(s):
    return s == "".join(sorted(s))

def case_sensitive(s):
    result = []
    if s.islower() == True or s == "":
        return [True, []]
    if s.islower() == False:
        big_letters = []
        for i in s:
            if i.isupper() == True:
                big_letters.append(i)
        return  [False, big_letters]