1) https://www.codewars.com/kata/679e0a54f8d448b508865c3b/train/python

def estimator(obstacles, stamina):
    for i in obstacles:
        if i < stamina:
            return True # most of it is working but theres a lil bits of bugs mostlyu it works i got 20 errors
        else:
            return False

3) https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

4) https://www.codewars.com/kata/58a66c208b88b2de660000c3/train/python

5) https://www.codewars.com/kata/552564a82142d701f5001228/train/python

6) https://www.codewars.com/kata/52dbae61ca039685460001ae/train/python

7) https://www.codewars.com/kata/526571aae218b8ee490006f4/train/python

def count_repeats(txt):
    result = 0
    
    for i in range(len(txt) - 1):
        if txt[i] == txt[i + 1]:
            result += 1
    
    return resultaaw