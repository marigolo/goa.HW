/* 
.map() - იღებს არგუმენტს  ცვლის და აბრუნებს ახალ სიას ამიტომ ცვლადს ვუტოლებთმას

.filter() -აბრუნებს ახალ სიას შეცვლილი ელემენთებით return - ში ვწერთ პირობას

.findIndex() -abrutmebs porvelive elemnts romelic simarTlea abrunebs index

*/

// using .map()

let numbers = [1, 2, 3, 4];

let spuear_num = numbers.map(number => {
    return number * 2;
});

console.log(spuear_num);


// using .filter()

const words = ['chair', 'music', 'pillow', 'brick', 'pen', 'door']; 

const shortWords = words.filter(word => {
  return word.length < 6;
});


// гыштп findIndex
const jumbledNums = [123, 25, 78, 5, 9]; 

const lessThanTen = jumbledNums.findIndex(num => {
  return num < 10;
});


// cw
/* 

1) დაწერეთ map, რომელიც სიტყვების მასივიდან ახალ მასივში დაამატებს თითოეული სიტყვის ბოლო ასოს.

2) დაწერეთ filter, რომელიც [1, 3.14, 'javaScript', true, 'Hello World', 82] მასივს გაფილტრავს და ახალ სიაში დატოვებს მხოლოდ სტრინგ მონაცემებს.

3) forEach მეთოდით სიტყვების მასივიდან დააბრუნეთ იმ ელემენტის ინდექსი, რომელიც ასო 'L' ზე იწყება.

*/

// 1)

let words1 = ['yellow', 'purple', 'bar', 'boll', 'blue', 'js', 'py']
let endsWith = words1.map(words1 => {return [words1.length -1]})
console.log(endsWith)

// 2)

const arrs = [1, 3.14, 'javaScript', true, 'Hello World', 82]
const strings = arrs.filter(arr =>(typeof arr === 'string'))
console.log(strings)


// 3)

const wprd3 = ['hi', 'whats up', 'city', 'london', 'lost']
words.forEach((wprd3 , index) => {
    if (wprd3 [index] === 'l') {
        console.log(index)
    }
})

// const words = ['Hello', 'Apple', 'London', 'World'];
// const index = words.findIndex(word => word[0] === 'L');
// console.log(index);