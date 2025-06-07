// 1) მომხმარებელს შემოატანინეთ რიცხვი და უთხარით ლუწია თუ კენტი. 
number = prompt("number")
if(number % 2 === 0){
    console.log(luwia)
}
else{
    console.log(kenti)
}
// 2) მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. მომხმარებელს შემოატანინე მისი წლოვანება და დაწერეთ პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება.
age = prompt("age")
MCprice = 20 
if(age >= 18){
    console.log(MCprice)
}
else if(age < 18){
    console.log(MCprice % 2)
}
// 3) მაღაზიაში არის ფასდაკლება მხოლოდ არასრულწოვნებზე და 18 წლის ხალხზე. არასრუწლოვანი ადამიანი მიიღებს 50%იან ფასდაკლებას,18 წლის ადამიანი მიიღებს 25% ფასდაკლებას, ხოლო სრულწლოვანი გადაიხდის ჩვეულებრივ ფასს. მომხმარებელს შემოატანინეთ მისი ასაკი და დაწერეთ პროგრამა რომელიც ადამიანს ეტყვის მან მიიღო თუ არა ფასდაკლება და თუ მიიღო რამდენი.
age = prompt("age")
bevaragePrice = 2 
if(age > 18){
    console.log(bevaragePrice)
}
else if(age === 18){
    console.log("bevaragePrice 25% off")
}
else if(age < 18){
    console.log(bevaragePrice % 2)
}
// 4) კომენტარის სახით ახსენით რა შემთხვევაში აქვს ცვლადს false/true მნიშვნელობა პასუხ დაწერეთ ვრცლად

//ცვლადი False არის როდესაც ცვლადი არის : undefined,null,nan
//ცვლადი არის True როდესაც ცვლადი არის : number,string

// 5) მომხმარებელს შემოატანინეთ სახელი თუ მისი სახელის სიგრძე აღემატება 6 მაშინ დაბეჭდეთ "hello my friend 'name!' სხვა შემთხვევაში "hello 'name'!"
nameLenght = prompt("name:")
name5 = nameLenght.lenght
if(name5 >= 6){
    console.log(`hello my friend ${name5}!`)
}
else if(name5 < 6){
    console.log(`hello ${name5}!`)
}