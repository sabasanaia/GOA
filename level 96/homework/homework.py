def estimator(obstacles, stamina):
    for i in obstacles:
        if i < stamina: #its a little  buggy but mostly it works
            return True
            stamina -= 1
        else:
            return False
    
2) https://www.codewars.com/kata/5fc7caa854783c002196f2cb/train/python

3) https://www.codewars.com/kata/56f253dd75e340ff670002ac/train/python

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def delete_nth(order,max_e):
    result = []
    
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    
    return result