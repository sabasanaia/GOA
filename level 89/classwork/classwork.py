def factorial(n):
    list = []
    while i > n:
        list.append(i) # არ მუშაობს
        i += 1
    return list

2) https://www.codewars.com/kata/526233aefd4764272800036f/train/python # ვერ გავიგე

def kebabize(st):
    st1 = st.lower()
    list = st.split() # მივხვდი რა უნდა გამეკეთა მაგრამ რომ ვცადე არ გამომივიდა
    return "-".join(list)

def is_isogram(string):
    result = []
    for i in string:
        if i[i] == i[i+1]: # რაღაცა აკლია და დასამატებელია მაგრამ მაინც არ მუშაობს
            continue
        elif i[i] != i[i+1]:
            result.append(i[0])

5) https://www.codewars.com/kata/55f2b110f61eb01779000053/train/python