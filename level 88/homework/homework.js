// 1) შექმენით სარეგისტრაციო ფორმა 3 ინფუთით ემაილი, პაროლი და submit ინფუთები submit ინფუთზე დაადეთ მოვლენის მსმენელი რომელიც კლიკის დროს კონსოლში გამოიტანს ემაილს და პაროლს
let name1 = document.getElementById("name")
let password = document.getElementById("password")
let email = document.getElementById("email")
let submit = document.getElementById("submit")

submit.addEventListener("submit",function(e){
    e.preventDefault()
    console.log()
})