# 2) კომენტარის სახით ჩამოწერეთ თუ რა განსხვავებაა set-ებსა და list-ებს შორის.
#the difffrence beetwen sets is that sets dont allow duplicates while lists can have as much duplicates as it wants and the last diffrence is that sets elements sequence is random while lists elemnts sequence is like how you wrote it in the list
# 3) შექმენით set სადაც შეინახავთ რიცხვებს, შემდეგ კი ინდექსინგის საშუალებით სცადეთ თითოეული ელემენტის შეცვლა და დააკვირდით შედეგს.

# 4) შექმენით set, რომელშიც შენახული გექნებათ Fast food საკვები პროდუქტები. შემდეგ კი ამოშალეთ ყველა პირვანდელი ელემენტები set-იდან, და მათ ნაცვლად დაამატეთ ჯანსაღი საკვები პროდუქტები.

# 5) შექმენით ფუნქცია, რომელიც არგუმენტად იღებს სიას, და აბრუნებს იგივე სიას, მაგრამ დუპლიკატების გარეშე. hint: გააკეთეთ set-ის საშუალებით (output-ში ელემენტების თანმიმდევრობას მნიშვნელობა არ აქვს)
def no_duplicates(list1):
    return list(set(list1))

print(no_duplicates([89, 90, 56, 45, 90, 78, 90]))
# test cases:

# list1 = [7, 5, 44, 14, 5, 5, 44]

# list2 = [89, 90, 56, 45, 90, 78, 90]