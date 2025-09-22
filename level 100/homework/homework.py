def solution(number):
    sum = 0
    for i in range(number):
        if i % 3 == 0 or i % 5 == 0:
            sum += i
        else:
            continue
    return sum

def array_diff(a, b):
    return [i for i in a if i not in b]


def spin_words(sentence):
    result = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)

def digital_root(n):
    N = str(n)
    res = []
    if len(N.split(" ")) == 1:
        return int(N)
    while len(n.split(" ")) > 1: # უმეტესობა არ მუშაობს ვერ გავიგე 
        res.append(int(N))
        " ".join(sum(res))
        
    return res

5) https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python
#-------------------------------------------------------------

1) https://www.codewars.com/kata/514b92a657cdc65150000006/train/python

2) https://www.codewars.com/kata/523f5d21c841566fde000009/train/python

3) https://www.codewars.com/kata/5264d2b162488dc400000001/train/python

4) https://www.codewars.com/kata/541c8630095125aba6000c00/train/python

5) https://www.codewars.com/kata/5839edaa6754d6fec10000a2/train/python