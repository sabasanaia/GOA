const inp1 = document.getElementById("inp1")
const inp2 = document.getElementById("inp2")
const submit = document.getElementById("submit")
submit.innerHTML = "Log in"
submit.addEventListener("click",function(e){
    e.preventDefault()
    console.log(inp1)
    console.log(inp2)
})