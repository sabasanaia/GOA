function cappingwords(str) {
  let list = str.split(" ");
  let result = [];
  for (let i = 0; i < str.length; i++) {
    if(i % 3 === 1){
        result.push(list[i[0]]+ i[0])
    }
  }
  return result
}
console.log(cappingwords("javascript and python are fun languages"))
