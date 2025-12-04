// 9) .clear() ფუნქციის დახმარებით გაასუფთავეთ თქვენი localStorage()
localStorage.setItem("password","vsjjawkdjakwdjkawkjdajdajdw")
localStorage.setItem("hell0","eeeee")
localStorage.setItem("e","a")
localStorage.setItem("t","c")
localStorage.setItem("m","d")
localStorage.setItem("p","b")
localStorage.setItem("o","r")
localStorage.clear()


// 10) შეინახეთ კვლავ 2 ახალი მნიშვნელობა localStorage-ში და დაბეჭდეთ მათი key-ები index-ების მეშვეობით .key() ფუნქციის დახმარებით.

localStorage.setItem("pass","abcd")
localStorage.setItem("pass2","1234")
console.log(localStorage.key(1))
console.log(localStorage.key(0))

// 1) დაბეჭდეთ for loops-ის დახმარებით კენტრი რიცხვები 1-დან 76-მდე
for(let i = 0; i < 76;i=i+2){
    console.log(i)
}
// 2) შექმენით ობიექტი, რომელშიც შეინახავთ თქვენთვის სასურველ key და value-ებს. თქვენი დავალებაა for in iterator-ის დახმარებით დაბეჭდოთ ობიექტში მყოფი ყველა key და value.
account = {
    name: "saba",
    age: 13,
}
for(let i in account){
    console.log(i)
}
// 3) შექმენით 6 ელემენტიანი სია, თქვენი დავალებაა დაბეჭდოთ ამ სიაში მყოფი ყველა ელემენტი for of iterator-ის დახმარებით.
list1 = [1,2,3,4,5,6]
for(let i of list1){
    console.log(i)
}
