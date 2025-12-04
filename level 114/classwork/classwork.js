// გააგზავნეთ მოთხოვნა ამ საიტზე და კონსოლში გამოიტანეთ json-ად ქცეული შედეგი

// 'https://fakestoreapi.com/products/1'

fetch('https://fakestoreapi.com/products/1')
    .then(result => console.log(result.json()))

