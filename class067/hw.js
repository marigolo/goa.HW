/* 

3) შექმენი ცვლადი sum = 0 და რიცხვი i = 1. do...while ციკლის მეშვეობით დაითვალე 1-დან 5-მდე რიცხვების ჯამი და საბოლოო შედეგი დაბეჭდე კონსოლში.

4) შექმენი ცვლადი count = 10. do...while ციკლის გამოყენებით დაბეჭდე უკუთვლა 10-დან 1-მდე.

5) გამოიყენე prompt() მომხმარებლისგან პაროლის მისაღებად (do...while ციკლში). ციკლი უნდა გაგრძელდეს მანამ, სანამ მომხმარებელი არ შეიყვანს სწორ პაროლს (მაგალითად: "secret123"). სწორი პაროლის შეყვანისას დაბეჭდე "წვდომა დაშვებულია!".

6) დაწერე for ციკლი, რომელიც ითვლის 1-დან 10-მდე. გამოიყენე break, რათა ციკლი შეწყდეს მაშინვე, როცა ინდექსი გაუტოლდება 6-ს. მოცემულია მასივი: let numbers = [5, 12, 8, 130, 44]. გამოიყენე for ციკლი და მოძებნე პირველი რიცხვი, რომელიც 100-ზე მეტია. როგორც კი იპოვი, დაბეჭდე ის და გააჩერე ციკლი break-ის საშუალებით.

7) დაწერე while (true) (უსასრულო) ციკლი. შიგნით შექმენი ცვლადი, რომელიც ყოველ ბიჯზე 1-ით იზრდება. როდესაც ცვლადის მნიშვნელობა 15-ს მიაღწევს, გამოიყენე break ციკლის შესაჩერებლად.

8) მოცემულია სახელების მასივი: let names = ["John", "Mary", "Jane", "STOP", "Patrick"]. გაიარე მასივი ციკლით და დაბეჭდე თითოეული სახელი. თუ შეხვდები ელემენტს "STOP", შეწყვიტე ციკლი break-ით ისე, რომ "მარიამი" არ დაბეჭდოს.

9) შექმენით მასივი სადაც შეინახავთ  სხვადასხვა სახეობის ხილს, თქვენი დავალებაა, რომ forEach მეთოდის გამოყენებით ცალ - ცალკე გამოიტანოთ ხილის სახელები ისე, რომ წინ ეწეროს 'My favorite fruit is' - ხილის სახელი

10) მოცემულია რიცხვების მასივი: let numbers = [2, 4, 6, 8, 10]. forEach-ის დახმარებით გამოთვალე ამ რიცხვების ჯამი და დაბეჭდე შედეგი.

11) მოცემულია ფასების მასივი: let prices = [10, 20, 30, 40]. forEach-ით დაბეჭდე თითოეული ელემენტი თავის ინდექსთან ერთად.

12) მოცემულია რიცხვების მასივი: let scores = [45, 80, 32, 95, 60, 50]. forEach-ის გამოყენებით დაბეჭდე მხოლოდ ის რიცხვები, რომლებიც 50-ზე მეტია ან ტოლია.


*/


// 1)

let i = 1;

while (i <= 10) {
  console.log(i);
  i++;
}


// 2) 

let sum = 0;
let num = 1;

while (num <= 100) {
  sum = sum + num;
  num++;
}

console.log(sum);


// 3) 

let sum2 = 0;
let i2 = 1;

do {
  sum2 = sum2 + i2;
  i2++;
} while (i2 <= 5);

console.log(sum2);


// 4)

let count = 10;

do {
  console.log(count);
  count--;
} while (count >= 1);


// 5) 

// let password;

// do {
//   password = prompt("შეიყვანე პაროლი:");
// } while (password !== "secret123");

// console.log("წვდომა დაშვებულია!");


// 6) a

for (let i3 = 1; i3 <= 10; i3++) {
  if (i3 === 6) {
    break;
  }

  console.log(i3);
}


// 6) b

let numbers = [5, 12, 8, 130, 44];

for (let i4 = 0; i4 < numbers.length; i4++) {
  if (numbers[i4] > 100) {
    console.log(numbers[i4]);
    break;
  }
}


// 7) 

let number = 0;

while (true) {
  number++;

  if (number === 15) {
    break;
  }
}


// 8) -

let names = ["John", "Mary", "Jane", "STOP", "Patrick"];

for (let i5 = 0; i5 < names.length; i5++) {
  if (names[i5] === "STOP") {
    break;
  }

  console.log(names[i5]);
}


// 9) 

let fruits = ["Apple", "Banana", "Orange", "Mango"];

fruits.forEach(function(fruit) {
  console.log("My favorite fruit is " + fruit);
});


// 10) 

let numbers2 = [2, 4, 6, 8, 10];
let sum3 = 0;

numbers2.forEach(function(number) {
  sum3 = sum3 + number;
});

console.log(sum3);


// 11) 

let prices = [10, 20, 30, 40];

prices.forEach(function(price, index) {
  console.log(index, price);
});


// 12) 

let scores = [45, 80, 32, 95, 60, 50];

scores.forEach(function(score) {
  if (score >= 50) {
    console.log(score);
  }
});