// Helper Function არის ფუნქცია, რომელიც სხვა ფუნქციას ეხმარება კონკრეტული დავალების შესრულებაში.


// მაგ: Helper Function 

function monitorCount(rows, columns) {
    return rows * columns;
}

function costOfMonitors(rows, columns) {
    return monitorCount(rows, columns) * 200;
}

// Function Expressions - ი არის ფუნქციის შექმნის მეთოდი, როდესაც ფუნქციას ვინახავთ ცვლადში.

// მაგ: Function Expressions
const greet = function() {
    console.log("Hello!");
};

greet();

// ---------------------- CW ---------------------- //

/* 
1) დაწერე function expression, რომელიც მიიღებს პროდუქტის რაოდენობასა და მის ფასს და დააბრუნებს საბოლოო ღირებულებას.

2) დაწერე function expression, რომელიც მიიღებს პროდუქტის ამჟამინდელ ფასს და პროცენტს. შენი დავალებაა დააბრუნო ფასდაკლების შემდეგ რა ფასი ექნება პროდუქტს..

3) შექმენი მთავარი ფუნქცია greeting, რომელიც მიიღებს firstName და lastName არგუმენტებს და დააბრუნებს მისალმებას.შენი დავალებაა დაწერო upperCase(word) ფუნქცია, რომელიც დაბრუნებულ პასუხს აიყვანს upeercase-ში.

*/

// 1)

const totlePrice = function(q , p){
    return q * p
}

console.log(totlePrice(2, 20))

// 2)  

const discountPrice = function(p , pd){
    return p - (p * pd / 100)
}

console.log(discountPrice(100, 20))
console.log(discountPrice(10, 20))

// 3)

function greeting(firstName, lastName) {
    return 'Hi ' + firstName + ' ' + lastName;
}

function toupper(firstName, lastName) {
    return greeting(firstName, lastName).toUpperCase();
}

console.log(toupper('anna', 'gg'));