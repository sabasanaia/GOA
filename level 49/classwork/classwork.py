def replace_exclamation(st):
    return st.replace("a","!").replace("e","!").replace("i","!").replace("o","!").replace("u","!").replace("A","!").replace("E","!").replace("I","!").replace("O","!").replace("U","!")

def get_size(w,h,d):
    return [2 * w * h + 2 * w * d + 2 * h * d,w * d * h]

def get_min_max(seq): 
    return min(seq),max(seq)

def sp_eng(sentence): 
    return "english" in sentence.lower()

def cookie(x):
    if type(x) == str:
        return "Who ate the last cookie? It was Zach!"
    elif type(x) == bool:
        return "Who ate the last cookie? It was the dog!"
    else:
        return "Who ate the last cookie? It was Monica!"
    