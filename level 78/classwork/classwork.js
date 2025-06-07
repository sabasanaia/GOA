// 1) მომხმარებელს შემოატანინეთ თვისი წლოვანება თუ ასაკი არ აღემატება 14 გამოიტანეთ "you are kid" თუ ასაკი აღემატება 14 მაგრამ არ აღემატება 18 დააბრუნეთ "you are not adult yet" და თუ აღემატება 18 დააბრუნეთ "you are adult"
age = prompt("age")
if(age === "14"){
    console.log("you are kid")
}
else if(age === "17"){
    console.log("you are not adult yet" )
}
else if(age === "18"){
    console.log("adult")
}
// 2) შემქენით ცვლადი რომელშიც შეინახავთ თქვენთვის სასურველ სახელს ან დატოვებთ ცარიელს თუ ცვლადი იქნება true მიესალმეთ ამ სახელს სხვაშემთხვევაში მიანიჭეთ "guest" და შემდეგ მიესალმეთ მას
let ame = "saba"
if(ame === ""){
    console.log("hello guest!")
}
else if(ame.length > 0 ){
    console.log(`hello ${ame}!`)
}
// 3) შექმენით ცვლადი სადაც მომხმარებელს შემოატანინებთ თავის სახელს შემდეგ შემქნით ცვლადი სადაც მომხმარებელს შემოატანინებთ თავის ასაკს თუ ასაკი არ აღემატება 18 გამოიტანეთ "you are not adult yet 'name'!" თუ ასაკი აღემატება 18 მაშინ გამოიტანეთ "Hello 'name'!"
let name1 = prompt("name")
let age = prompt("age")
if(age < 18){
    console.log(`your not a adult yet ${name1}`)
}
else if(age >= 18){
    console.log(`your a adult ${name1}`)
}
