def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def xo(s):
    s = s.lower()
    return s.count("x") == s.count("o")

3)https://www.codewars.com/kata/57cebe1dc6fdc20c57000ac9/train/python

def friend(x):
    friend = []
    for i in x:
        if len(i) == 4:
            friend.append(i)
    return friend

5)https://www.codewars.com/kata/5656b6906de340bd1b0000ac/train/python