
def count_by(x, n):
    list = []
    for i in range(x,x*n+1,x):
        list.append(i)
    return list

def abbrev_name(name):
    name = name.split(" ")
    return name[0][0].upper() + "." + name[1][0].upper()

def greet(name):
    if name == "Johnny":
        return "Hello, my love!"
    else:
        return "Hello, {name}!".format(name=name)
    
def update_light(current):
    if current == "green":
        return "yellow"
    elif current == "yellow":
        return "red"
    elif current == "red":
        return "green"