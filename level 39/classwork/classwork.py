def generate_range(start, stop, step):
    result = []
    for i in range(start,stop + 1,step):
        result.append(i)
    return result
        
def reverse_it(data):
    if type(data) == str:
        return data[::-1]
    elif type(data) == int:
        return int(str(data)[::-1])
    elif type(data) == float:
        return float(str(data)[::-1])
    else:
        return data
    
def sum_array(arr):
    sum = 0
    if arr == None:
        return 0 
    if len(arr) <= 2:
        return 0
    for i in arr:
        sum += i
    return sum - max(arr) - min(arr)

def count_by(x, n):
    list = []
    for i in range(x,x*n+1,x):
        list.append(i)
    return list