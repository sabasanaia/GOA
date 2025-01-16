def lowercase_count(string):
    count = 0
    lower_letters = "qwertyuiopasdfghjklzxcvbnm"
    for i in string:
        if i in lower_letters:
            count += 1
    return count

def capitals(word):
    list = []
    for i in range(len(word)):
        if word[i].isupper():
            list.append(i)
    return list

