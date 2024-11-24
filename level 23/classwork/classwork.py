# 1)კომენტარის მეშვეობით ახსენით .lower() / .upper() / .capitalize() / .find() ფუნქციების დანიშნულება
# lower ით შეიძლება სტრინგის ასოები გადავაქციოთ პატარათ
# upper ით შეიძლება სტრინგის ყველა ასო გადავაქციოთ დიდად
# find ით შეიჩლება ვიპოვოტ სტრინგის ასო და დავწეროთ რომელ ინდექსზე დგას
# capitalize ით შეიძლება სტრინგი გადავაქციოთ ისეთ სტრინგად რომ 1 ასო ქონდეს დიდი და დანარჩენი პატარა
# 2)მომხმარებელს შემოატანინეთ მისი გვარი და შეამოწმეთ, თუ გვარის პირველი ასო არის დიდი ასო, მაშინ დაუბეჭდეთ "Hello", თუ არ არის მაშინ დაუბეჭდეთ "Bye"
name = input("please enter your name: ")
if name[0] == name[0].upper():
    print("hello")
else:
    print("bye")
# 3)მომხმარებელს შემოატანინეთ სახელი, შემდეგ შემოატანინეთ ასო და თუ ამ სახელში ეს ასო არიქნება, მაშინ გამოუტანეთ "Can't find character", თუ იქნება მაშინ გამოუტანეთ "found it" და გვერდზე მიუწერეთ ამ ასოს ინდექსი
name = input("please enter your name: ")
shsh = input("enter an letter: ")
if name.find(shsh) == -1:
    print("cant find character")
else:
    print("found it")
# 4)მომხმარებელს შემოატანინეთ მისი გვარი, შემდეგ შეეკითხეთ როგორ უნდა რო შეიცვალოს მისი გვარის ასოები, თუ გიპასუხებთ "upper" გადაიყვანეთ მთლიანი გვარი დიდ ასოებად, თუ გიპასუხებთ "lower" გადაიყვანეთ მთლიანი გვარი პატარა ასოებად და თუ გიპასუხებთ "capitalize" გადაიყვანეთ გვარის მხოლოდ პირველი ასო დიდ ასოდ.
name = input("please enter your name: ")
option = input("would you like your name in all caps,all not in caps or first letter cap and the rest not?: upper , lower or capitalize: ")
if option == "upper":
    print(name.upper())
elif option == "lower":
    print(name.lower())
elif option == "capitalize":
    print(name.capitalize())