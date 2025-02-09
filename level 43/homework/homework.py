def sequence_sum(begin_number, end_number, step):
    sum = 0
    for i in range(begin_number,end_number + 1,step):
        sum += i
    return sum

def filter_list(l):
    result = []
    for i in l:
        if type(i) == int:
            result.append(i)
    return result

def to_jaden_case(string):
    list = string.split(" ")
    result = []
    for string in list:
        result.append(string.capitalize())
    return " ".join(result)

def sum_mix(arr):
    sum = 0
    for i in arr:
        if type(i) == str:
            sum += int(i)
        else:
            sum += i
    return sum

def array_plus_array(arr1,arr2):
    return sum(arr1 + arr2) 

def reverse_words(s):
    return " ".join(s.split(" ")[::-1] )

def sum_str(a, b):
    if len(a) == 0 and len(b) == 0:
        return "0"
    if len(a) == 0:
        a = 0
    if len(b) == 0:
        b = 0
    return str(int(a) + int(b))
    