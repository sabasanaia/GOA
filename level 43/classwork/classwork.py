def nth_even(n):
    return n * 2 - 2

def add_length(str_):
    result = []
    for i in str_.split(" "):
        result.append(i + " " + str(len(i)))
    return result

def array(string):
    if len(string.split(",")) <= 2:
        return None
    return " ".join(string.split(",")[1:-1])

def find_difference(a, b):
    volumeA = a[0] * a[1] * a[2]
    volumeB = b[0] * b[1] * b[2]
    if volumeB > volumeA:
        return volumeB - volumeA
    return volumeA - volumeB