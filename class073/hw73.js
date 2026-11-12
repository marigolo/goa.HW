// 3)

let words = ['Hello', ' ', 'World', '!']
let result = words.reduce((accumulator, currentValue) => accumulator + currentValue);
console.log(result);


// 4)

let numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
let sum = numbers.reduce((acc, currentValue) => acc + currentValue, 0);
console.log('ჯამი:', sum);
let product = numbers.reduce((acc, currentValue) => acc * currentValue, 1);
console.log('ნამრავლი:', product);

// 5)

let number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10];
let evenNumbers = number.filter(num => num % 2 === 0);
let multiplied = evenNumbers.map(num => num * 3);
let sums = multiplied.reduce((acc, num) => acc + num, 0);
console.log(sums);

// 6)

let word = ['python', 'java', 'c', 'javascript', 'go'];
let filtered = word.filter(words  => words.length > 3);
let upperCase = filtered.map(words => words.toUpperCase());
let sentence = upperCase.reduce((acc, words) => acc + ' ' + words);
console.log(sentence);

// 7)

let arr = [-5, 2, -3, 4, 6, -1];
let positive = arr.filter(x => x > 0);
let square = positive.map(x => x ** 2);
let total = square.reduce((a, b) => a + b, 0);
console.log(total);