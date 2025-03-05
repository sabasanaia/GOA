# 1)გადახედეთ ამ რესურსებს:
# https://www.w3schools.com/python/python_tuples.asp
# https://www.w3schools.com/python/python_tuples_access.asp
# https://www.w3schools.com/python/python_tuples_update.asp
# https://www.w3schools.com/python/python_tuples_unpack.asp
# https://www.w3schools.com/python/python_tuples_loop.asp

# 2) შემენით tuple, რომელშიც შეინახავთ საყიდლების სიას და მოახდინეთ მათი unpacking (დაშლა),რათა მიანიჭოთ თითოეული ელემენტი ცალკეულ ცვლადებს და დაბეჭდეთ ეს ცვლადები.

# 3) შექმენით tuple და შეინახეთ Fast food პროდუქტები. შემდეგ შეცვალეთ ეს tuple და მათში ჩაამატეთ ჯანსაღი საკვები პროდუქტები.
fast_food=("hamburger","fries")
healthy_food=list(fast_food).pop(0)
print(healthy_food)
# 4) კომენტარის სახით ახსენით, თუ რა ფუნქციას ასრულებს Asterisk და როგორ აღინიშნება ის.
#asterisk ფუნქცია უბრალოდ tuple-ის ყველა ელემენტს იღებს და ერთში სვამს მაგ.
# months = ("january", "february", "march", "april", "may")
# (first, second, third, fourth*)= months
#first - january
#second - february
#third - march
#fourth - aprill,may
#asterisk აღინიშნება ფიფქით(*)
# 5) მოცემულია შემდეგნაირი tuple:

# months = ("January", "February", "March", "April", "May")
# (first, second, third, fourth*)= months

# რას გამოიტანს მოცემული კოდი?
# print(first) - January
# print(second) - February
# print(third) - March
# print(fourth) - Aprill,May