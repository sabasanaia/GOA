# 1) კომენტარის სახით ახსენით, თუ რა განასხვავებს tuple-ებს List-ებისგან.
# the diffrence beetwen tuple and lists are that tuples are unchangable unlike lists wich are changable
# 2) შექმენით tuple, რომელიც შეიცავს თქვენს 5 საყვარელ ფილმს, შემდეგ კი დაბეჭდეთ პირველი და ბოლო ელემენტი ამ tuple-დან.
films = ("harry potter","jaws","i just cant remember more","i just cant remember more","i just cant remember more")
print(films[(0)])
print(films[(-1)])
# 3) შემენით Tuple, რომელშიც შეინახავთ კვირის დღეებს და მოახდინეთ მათი unpacking (destruction),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

# 4) შექმენით tuple, რომელიც შეიცავს რამდენიმე ელემენტს. შემდეგ შეამოწმეთ, შეიცავს თუ არა ეს tuple კონკრეტულ ელემენტს
num = [2,3,2,43,54,2,34,3,32,4,342,42434,432432,39384,299292929299]
if 1 in num:
    print(True)
elif 1 not in num:
    print(False)