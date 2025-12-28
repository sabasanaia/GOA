// 1. დაბეჭდეთ რიცხვები 1-დან 5-მდე 2 წამიანი ინტერვალებით.

let count = 1;
let counting = setInterval(() => {
  count += 1;
  console.log(count);                   //მუშაობს
  if (count >= 5) {
    clearInterval(counting);
  }
}, 2000);

// 2. დაიწყე 10-იდან და დაიწყე ქვევით თვლა (თან კონსოლში გამოიტანე), როდესაც 0-ზე ჩამოვა, კონსოლში გამოიტანე - 'done'.

let count1 = 10;
let counting1 = setInterval(() => {
    count1 -= 1
    console.log(count1)                 //მუშაობს
    if(count1 === 0){
        console.log("done")
        clearInterval(counting1)
    }
}, 1000);

// 3. შექმენი setInterval სადაც კიდევ ერთ setInterval ჩააშენებ, გაუკეთე სასურველი ფუქნციონალი, ოღონდ აამუშავე.

setInterval(() => {
    console.log(hello)
    setInterval(() => {       //------- ვერ გავიგე / არ მუშაობსშ
        console.log("hello")
    }, 1000);
}, 2000);

// 4. საიტის ჩატვირთვიდან 5 წამში კონსოლში გამოიტანე 5-იანი

setTimeout(() => {
    console.log(5) // მუშაობს
}, 5000);

