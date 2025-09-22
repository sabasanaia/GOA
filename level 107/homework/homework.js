// 4) კომენტარების სახით თქვენი სიტყვებით ახსენით რა არის localStorage და მისი მეთოდები.

// localstorage - ამას ჩვენ ვიყენებთ რომ შევინახოთ მნიშვნელოვანი ინფორმაცია და ტუ საიტს დავხურავტ ან დავარესტარტებთ ის ინფორმაცია სულლ იქ იქნება შენახულ

// clear - ასუფთავებს ყველაფერს რაც შენახულია local storage-ში

// set item - ინახავს ინფორმაციას რაც ჩავწერთ local storage-ში

// 5) localStorage-სა და .setItem() ფუნქციის დახმარებით შეინახეთ 7 მნიშვნელობა storage-ში თქვენთვის სასურველი key და value-ები.
localStorage.setItem("password","vsjjawkdjakwdjkawkjdajdajdw")
localStorage.setItem("hell0","eeeee")
localStorage.setItem("e","a")
localStorage.setItem("t","c")
localStorage.setItem("m","d")
localStorage.setItem("p","b")
localStorage.setItem("o","r")

// 6) წინა დავალებაში გაკეთებულ localStorage-ში შენახული მნიშვნელობებიდან ამოშალეთ .removeItem() ფუნქციის დახმარებით ნებისმიერი 2 მნიშვნელობა.

localStorage.removeItem("password")
localStorage.removeItem("hell0")

// 7) დაბეჭდეთ და console-ში გამოიტანეთ თქვენი localStorage-ი სიგრძე .length მეთოდის დახმარებით.

console.log(localStorage.length)

// 8) localStorage-დან წამოიღეთ .getItem()-ის დახმარებით მნიშვნელობები და შეინახეთ შესაბამისს ცვლადებში. ბოლოს დაბეჭდეთ ყველა ცვლადის შიგთავსი ;>

const lllllsssss = localStorage.getItem("m")
console.log(lllllsssss)
