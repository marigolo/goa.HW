// 1) arrays

const hobbies = ["reading", "gaming", "drawing"];
console.log(hobbies) 

// 2) indexs

//                                0                                1                               2
const famousSayings = ['Fortune favors the brave.', 'A joke is a very serious thing.', 'Where there is love there is life.'];

const listItem = famousSayings[0];
console.log(listItem);
console.log(famousSayings[2]);
console.log(famousSayings[3]);


// 3) Update Elements index

// let groceryList = ['bread', 'tomatoes', 'milk'];
// groceryList[1] = 'avocados';



//.push() - ბოლოში ამატებს ელემნტს

// let fuit = ['Apple', 'Banana'];
// fuits.push('Orange');
// console.log(fuit);


// .pop() -  ბოლოში შლის ელემნტს

// let fruit = ['Apple', 'Banana', 'Orange'];
// fruit.pop();
// console.log(fruit);

// .at() -აბრუნებს კონკრეტულ ინდეხსზე რომელი ელემენტია

// let futs = ['Apple', 'Banana', 'Orange'];

// console.log(futs.at(1));

//.concat() - აერთიანებს მასივებს ან სტრინგებს

// let naw = ['Apple', 'Banana'];
// let vegetables = ['Carrot', 'Potato'];
// let food = naw.concat(vegetables);
// console.log(food);

//shift() - შლის პირველ ელემენტს

// let first = ['Banana', 'Orange'];

// first.unshift('Apple');
// console.log(first);

//unshift() - ამატებს პირველ პოზიციაზე ელემენტს

// let secound = ['Banana', 'Orange'];

// secound.unshift('Apple');
// console.log(secound);

//.slice()

let animals = ['cat', 'dog', 'lion', 'tiger', 'bear'];

console.log(animals.slice(1, 4));


// .indexOf() - გამოიყენება მასივში კონკრეტული ელემენტის მოსაძებნად და აბრუნებს მის ინდექსს.

let colors = ['red', 'blue', 'green', 'yellow'];

console.log(colors.indexOf('green'));

//  class work





// 1)


let films = ['Avatar', 'The 100', 'Spiderman', 'Spyfamily']

films[1] = 'Endgame'
console.log(films)

// 2)

let fruet = ['Apple', 'peah',  'painapple',  'lemon', 'greenapple',  'redapple', 'stwraberry', 'Grape']
console.log(fruet.length)
console.log(fruet)

// 3)

let num = [1, 3, 4, 5, 7, 8, 10, 12, 15, 20]

num[4] = 'Seven'
num[10] = 'Twenty'

console.log(num)