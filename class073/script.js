/* 
.reduce() არის მასივის მეთოდი, რომელიც ელემენტებს ამუშავებს და ერთ საბოლოო მნიშვნელობას აბრუნებს.


const sum = numbers.reduce((accumulator, curentvalue) => accumulator + curentvalue)

accumulator = 0
        +
curentvalue = 1






*/
// ex:1

// const numbers = [1, 2, 3, 4, 5];

// const sum = numbers.reduce((accumulator, currentValue) => {
//     return accumulator + currentValue;
// });

// console.log(sum);

// ex:2

// const numbers = [10, 8, 6, 4, 2];

// const result = numbers.reduce((accumulator, currentValue) => {
//     return accumulator - currentValue;
// });

// console.log(result);


// const newSum = newNumbers.reduce((accumulator, currentValue) => {
//   console.log('The value of accumulator: ', accumulator);
//   console.log('The value of currentValue: ', currentValue);

//   return accumulator + currentValue;
// }, 10);

// console.log(newSum);



// cw




/*


/*
1)

accumulator - არის ცვლადი, რომელშიც ინახება
გამოთვლის წინა შედეგი.

მაგალითად: accumulator = 2

currentValue - არის მასივის მიმდინარე ელემენტი,
რომელზეც ამ ეტაპზე ვასრულებთ მოქმედებას.

მაგალითად: currentValue = 3

მაგალითი:
[2, 3, 4]
*/

// 2)

const numbers = [1, 2, 3, 4, 5, 6, 7];

const result = numbers.reduce((accumulator, currentValue) => {
    return accumulator ** currentValue;
},1);

console.log(result);

// 3)

const num =  [1, 2, 3, 4, 5]
const minuseValue = num.reduce((accumulator, currentValue) =>{
    return accumulator - currentValue
})

console.log(minuseValue)