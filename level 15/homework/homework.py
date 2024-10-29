#1
name = input("please enter your name")
name1 = "saba"
if name == name1:
    print("hello")
else:
    print("bye")
#----------------------------------------------------------------------------------------------------------------------------------------------------
#2
num = 12
num1 = int(input("please enter your favourite number"))
while num != num1:
    print("not it")
    num1 = int(input("please enter your favourite number"))
print("perfect")
#-----------------------------------------------------------------------------------------------------------------------------------------------
#3
for i in range (150,2):
    print("luwia",i)

for i in range (150,3):
    print("kentia",i)
#-----------------------------------------------------------------------------------------------------------------------------------------------
#4
age = 12
name = "saba"
age1 = int(input("please enter your age"))
name1 = input("please enter your name")
if name == name1 and age == age1:
    print("twins")
else:
    print("not twins")
#------------------------------------------------------------------------------------------------------------------------------------------------
#5
account_password = 12343
account_password_guess = int(input("please enter your password "))
while account_password != account_password_guess:
    print("incorrect")
    print("please try again")
    account_password_guess = int(input("please enter your password "))
print("welcome")