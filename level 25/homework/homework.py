# 1)შექმენით ცარიელი სია და for ციკლის მეშვეობით ჩაამატეთ ყველა ლუწი რიცხვი 0დან 200მდე, ბოლოს დაბეჭდეთ სია.
list = []
for i in range(1,201,2):
    print(i,list.append(i))
print(list)
# 2)შექმენით ცარიელი სია და for ციკლის მეშვოებით მომხმარებელს შეეკითხეთ მისი top 5 საყვარელი სახელი (ანუ ხუთჯერ input).
list = []
for i in range(5):
    input("enter your top favourite name: ")
    print(i,list.append(i))
print(list)
# 3)შექმენით სია 10 ელემენტით და გამოიტანეთ მხოლოდ კენტ ინდექსზე მდგომი ელემენტები.
list = [23,16,38,18,39,25,374,16,176,13]
# 4)შექმენით ცვლადი რომელშიც შენახული იქნება სტრინგი შემდეგ კი გაიგეთ ამ სტრინგის სიმბოლოების რაოდენობა.
name = "saba"
print(len(name))
# 5)შექმენით სია შემდგარი 5 ელემენტისგან, მომხმარებელს შემოატანინეთ რიცხვი და სიიდან ამოაგდეთ შემოტანილ რიცხვის ინდექსზე მდგომი ელემენტი.
list = [1,2,3,4,5]
int(input("enter your favourite number: "))
if int(input) == list:
    list.pop(int(input))
print(list)
# 6)შექმენით სია და დაბეჭდეთ ამ სიის სიგრძე.
list = ["ohio","texas","california"]
print(len(list))
# 7)ვისაც არ დაგისრულებიათ საკლასო სამუშაო დაასრულეთ აუცილებლად.