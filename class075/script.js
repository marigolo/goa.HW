/* 

function - key word
getReminder() -function name 
{} - function use instad of :

თუ ვიყენებთ - return - გამოვიყენოთ console.log()



------------ფუნქციები პარამეტრებით------------

ფუნქციას შეგვიძლია გადავცეთ პარამეტრი, რათა მან მიიღოს ინფორმაცია და გამოიყენოს ფუნქციის შიგნით.

- Parameter — ცვლადი, რომელიც ფუნქციის შექმნისას ფრჩხილებში იწერება.

- Argument — კონკრეტული მნიშვნელობა, რომელსაც ფუნქციის გამოძახებისას გადავცემთ.

- name — პარამეტრია (parameter).

- 'Cole' — არგუმენტია (argument).

ფუნქციას სხვადასხვა არგუმენტით რამდენჯერმე გამოვიძახებთ და სხვადასხვა შედეგს მივიღებთ.

--------------Default Parameter---------------

Default Parameter - არის პარამეტრი, რომელსაც წინასწარ ვანიჭებთ მნიშვნელობას. თუ ფუნქციის გამოძახებისას არგუმენტს არ გადავცემთ, გამოიყენება წინასწარ მინიჭებული მნიშვნელობა.


--------------Helper Functions--------------

Helper Function არის ფუნქცია, რომელიც სხვა ფუნქციას ეხმარება კონკრეტული დავალების შესრულებაში.

ის გამოიყენება იმისთვის, რომ კოდი იყოს უფრო მოწესრიგებული, მარტივი და თავიდან ავიცილოთ ერთი და იმავე კოდის გამეორება.

- multiplyByTwo() — დამხმარე ფუნქციაა.
- addFive() — იყენებს დამხმარე ფუნქციას თავისი დავალების შესასრულებლად.
- ჯერ რიცხვი მრავლდება 2-ზე, შემდეგ ემატება 5.
*/

// function getReminder() {
//     console.log("Don't forget to complete your tasks!");
// }

// getReminder()


// function greet() {
//     return 'hello'
// }

// console.log(greet())

// // Parameter

// function sayThanks(name) {
//     console.log(`Thank you, ${name}!`);
// }

// sayThanks('Cole');


// // Default Parameter

// function greet(name = 'Guest') {
//     console.log(`Hello, ${name}!`);
// }

// greet('Cole'); 
// greet();    

// // Helper Functions

// function multiplyByTwo(number) {
//     return number * 2;
// }

// function addFive(number) {
//     return multiplyByTwo(number) + 5;
// }

// console.log(addFive(3)); 


// ------------- cw ---------

/*
1) ახსენით ფუნქციის სინტაქსი ჯავასკრიპტში (function keyword-ით შექმნილი ფუნქციის).

2) შექმენით ფუნქცია, რომელიც არგუმენტად მიიღებს ფარენგეიტში და დააბრუნებს მას გრადუსებში გადაყვანილს.

3) შექმენით ფუნქცია, რომელიც მიიღებს მომხმარებლის სახელს, მისამართს და მეილს. (პარამეტრებს გაუწერეთ default მნიშვნელობები). თქვენი დავალებაა წინადადების სახით დააბრუნოთ იგი ფუნქციაში. შექმენით ცვლადი userData1 და userData2, ორივეში შეინახეთ ორი სხვადასხვა მომხმარებლის მონაცემები ფუნქციის სახით, ბოლოს კი ეს ცვლადები კონსოლში გამოიტანეთ. 
*/

// 1) ფუნქციის შესაქმნელად ვიყენებთ keyword function-ს  იგი საკვანძო სიტყვაა როგორც python - ში def - ი. შემდეგ ვწერთ  getReminder() - function name (ფუნქციის სახელი)

// 2)

function toFahrenheit(c) {
    return (c * 1.8) + 32;
}

console.log(toFahrenheit(23));


// 3) 

function userInfo(name = 'User', email = 'mail', address = 'your address') {
    return `სახელი: ${name}, მისამართი: ${address}, ემაილი: ${email}`;
}
const userData1 = userInfo('Giorgi', 'giorgi@gmail.com', 'Tbilisi');
const userData2 = userInfo('Nino', 'nino@gmail.com', 'Batumi');

console.log(userData1);
console.log(userData2);     