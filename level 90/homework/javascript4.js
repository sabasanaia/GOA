// 4) შექმენით ერთ დივი რომელსაც გაუწერთ თქვენთვის სასურველ სიმაღლეს და სიგანეს ასევე მისცემთ ფერსაც და border-radius'საც შემდეგ კი ამ div'ზე მოახდინეთ მოვლენის მსმენელი და როდესაც მასზე დაკლიკება მოხდება მისი ზომა გაიზარდოს ორჯერ და ასევე შეეცვალოს ფერი 
const e = document.getElementById("e")
e.addEventListener("click",function(){
    e.style.backgroundColor = "blue"
    e.style.height = "200px"
    e.style.width = "200px"
})