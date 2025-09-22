const a = document.getElementById("a")
const b = document.getElementById("b")
const c = document.getElementById("c")
const d = document.getElementById("d")
const e = document.getElementById("e")
a.addEventListener("click",function(){
    a.innerHTML = ">:("
    a.style.color = "red"
})
b.addEventListener("click",function(){
    alert("B: a gets angry when someone tries to talk whit him ;-; meanwhile e gets happy when someone interacts whit him")
})
c.addEventListener("click",function(){
    let you = prompt("hello whats your name")
    alert(`hi ${you} :D`)
})
d.addEventListener("click",function(){
    alert("my name is d")
})
e.addEventListener("click",function(){
    e.style.height = "23px"
    e.style.backgroundColor = "black"
    e.innerHTML = ":)"
    e.style.color = "white"
})