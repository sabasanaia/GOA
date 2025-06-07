def small_enough(array, limit):
    for i in array:
        if i >= limit:
            return False
        else:
            return True # რაღაცის გასწორება სწირდება და ვერ ვხვდები რა ისე არასწროი მხოლოდ 3

def largest_pair_sum(numbers): 
    return sorted(numbers)[-1] + sorted(numbers)[-2]

def spin_words(sentence):
    result = []
    for i in sentence.split(" "):
        if len(i) >= 5:
            result.append(i[::-1])
        else:
            result.append(i)
    return " ".join(result)
            

def delete_nth(order,max_e):
    result = []
    
    for i in order:
        if result.count(i) < max_e:
            result.append(i)
    
    return result

