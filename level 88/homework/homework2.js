// 2) JS'ში შექმენით ცვლადი სადაც შეინახავთ თქვენს სახელს ასევე HTML'ში შექმენით ერთი ღილაკი ღილაკზე დაადეთ მოვლენის მსმენელი და დაკლიკების დროს კონსოლში გამოიტანეთ Hello {name}!
let name1 = prompt("enter your name")
let button = document.getElementById("btn")
button.addEventListener("click",function(){
    console.log(`Hello ${name1}`)
})