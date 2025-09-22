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