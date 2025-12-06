const btn = document.getElementById("btn")
btn.addEventListener("mouseover",function(){
    console.log(10)
})
btn.addEventListener("mouseout",function(){
    console.log(5)
})

// btn.onmouseover = function(){console.log(10)}
// btn.onmouseout = function(){console.log(5)}