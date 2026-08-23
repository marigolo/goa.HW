/*
3) შექმენით 5 სხვადასხვა ცვლადი. მათ შესაქმნელად გამოიყენეთ camelCase. ცვლადები გამოიტანეთ კონსოლში და დააკვირდით მათ მნიშვნელობებს. შემდეგ მიანიჭეთ ამ ცვლადებს თვქნთის სასურველი მნიშვნელობები და თავიდან გამოიტანეთ კონსოლში.

4) შექმენით 3 ცვლადი const-ის გამოყენებით. პირველ ცვლადში - ქვეყნის დასახელება, მეორე ცვლადში - დედაქალაქის დასახელება, მესამე ცვლადში კი - ქალაქის დასახელება შეინახეთ. სამივე ცვლადი ერთ ხაზზე დაბეჭდეთ კონსოლში. 

5) მოიფიქრეთ გზა რომ გამოიტანოთ კონსოლში undefined, ისე რომ თვითონ unefined არ არ დაბეჭდოთ
*/


// 1)

// let - ით შექმნილ ცვლადს შეგვიძლია მოგვიანებით ახალი მნიშვნელობა მივანიჭოთ.
// const - ით შექმნილ ცვლადს მნიშვნელობას თავიდანვე ვანიჭებთ და შემდეგ შეცვლა აღარ შეგვიძლია.

// 1.1)

let age = 15;
age = 16; 

// 1.2) 

const name = "Mariam";
name = "Nino";

// 2)

// 2.1)

let firstName = "Mariam";
let lastName = "Goloshvili";
let favoriteColor = "Purple";
let favoriteAnimal = "Cat";
let favoriteFood = "Pizza";

console.log(firstName);
console.log(lastName);
console.log(favoriteColor);
console.log(favoriteAnimal);
console.log(favoriteFood);

// 2.2)

firstName = "Nino";
lastName = "Beridze";
favoriteColor = "Blue";
favoriteAnimal = "Dog";
favoriteFood = "Burger";

console.log(firstName);
console.log(lastName);
console.log(favoriteColor);
console.log(favoriteAnimal);
console.log(favoriteFood);

// 3)

const country = "Georgia";
const capital = "Tbilisi";
const city = "Batumi";
console.log(country, capital, city);

// 4)

let myVariable;
console.log(myVariable);