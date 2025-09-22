// 2)შექმენით ერთი ღიალაკი და ერთი პარაგრაფი, ყოველ ღილაკის დაკლიკებაზე უნდა დაემატოს განსხვავებული ფერის პარაგრაფები
const div = document.getElementById("div")
const btn = document.getElementById("btn")
let list = ["red","blue","green"]
btn.addEventListener("click",function(){
    div.innerHTML += "hello world"
})