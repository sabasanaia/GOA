// 3)მომხმარებელს შემოატანინეთ თავის სახელი, გვარი და დაბადების თარიღი, შემდეგ შექმენით ერთი div სადაც ყოველ ჯერზე ჩაემატება შემოტანილი ინფორმაცია წინადადების სახით (მაგ: გამარჯობა name surname, შენ დაიბადე age!
const form = document.getElementById("myForm")
const result = document.getElementById("result")

form.addEventListener("submit", function(e){
    e.preventDefault();

    const name = form.name.value
    const surname = form.surname.value
    let date = form.date.value
    date = date.split("-")


    result.innerHTML += `
    <p>Your Fullname is: ${name} ${surname}, Your were born in ${date[0]}y, Your birth of month is ${date[1]}, Your day of birth is ${date[2]}</p>
    `
})