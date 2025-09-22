function boolToWord( bool ){
  if(bool === true){
    return "Yes"
  }
  else{
    return "No"
  }
}

function greet(){
  return "hello world!"
}


// 3) https://www.codewars.com/kata/523b4ff7adca849afe000035/train/javascript

function basicOp(operation, value1, value2){
  if(operation === "-"){
    return value1 - value2
  }
  else if(operation === "*"){
    return value1 * value2
  }
  else if(operation === "/"){
    return value1 / value2
  }
  else if(operation === "+"){
    return value1 + value2
  }
}

// 5) https://www.codewars.com/kata/57356c55867b9b7a60000bd7/train/javascript

// 6) https://www.codewars.com/kata/53dc54212259ed3d4f00071c/train/javascript

function lovefunc(flower1, flower2){
  if(flower1 % 2 != 0 && flower2 % 2 === 0){
    return true
  }
  else if(flower2 % 2 != 0 && flower1 % 2 === 0){
    return true
  }
  else{
    return false
  }
}
