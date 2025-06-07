// 1) შექმენით ცვლადი სადაც შეინახავთ თქვენთვის სასურველ ასაკს, თუ იქნება 13 წელზე ნაკლების გამოუტანეთ You are kid, თუ იქნება 18 წელზე ნაკლების მაგრამ 13'ზე მეტის გამოუტანეთ You are not adult yet და თუ იქნება 18 წელზე მეტის გამოუტანეთ You are adult
const age = 15
if(age < 13){
    console.log("youre a kid")
}
else if(age > 13 && age < 18){
    console.log("youre not a adult yet")
}
else if(age >= 18){
    console.log("youre a adult")
}

// 2) შექმენით ცვლადი სადაც შეიტანთ რაიმე რიცხვს, თუ რიცხვი იყოფა 2'ზე უნაშთოდ გამოიტანეთ ეს რიცხვი, სხვა შემთხვევაში დააბრუნეთ "ეს რიცხვი კენტია"
if(123 % 2 === 0){
    console.log("ეს რიცხვი კენტია")
}
else{
    console.log("no number detected")
}
// 3) პირველი დავალება შეასრულეთ python'შიც და დაწერეთ განსხვავებები python'ისა და js'ს შორის.

// 4) რას აკეთებს "!" ოპერატორი ახსენით თქვენი სიტყვებით 
// ! imperator means if not for example:
if(1 !== 2){
    console.log(3)
}
// 5) შექმენით ცვლადი სადაც შეინახავთ რაღაც რიცხვს შემდეგ შეამოწმეთ თუ ეს რიცხვი იყობა 3'ზეც და 9'ზეც გამოიტანეთ ეს რიცხვი, სხვა შემთხვევაში დააბრუნეთ "task was not completed."
const number = 1241342
if(number % 3 && number % 9){
    console.log(number)
}
else{
    console.log("task was not completed.")
}