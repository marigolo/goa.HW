/* 
************* foor loops *************
for loops -ციკლი ვეუბნებით რომ გაიმეორეს იქამდე სანამ არ მიაღწევს იმ გამაჩერებელ რიცხვამდე


let i = 0; - Starting Condition ვქმნით ათვლის წერტილისთვის ცვლადს

counter < 4; - Stoping Condition სადამდე უნდა გააგრძელოს ცვლადმა მატება

counter++ - Stap Condition რამდენი უნდა მიემატოს თითვეულ იტერაციაზე


********** Ravers foor loops *********

let i = 3; - Starting Condition რაიმე 0 >-ია

i >= 0; - Stoping Condition სადაც i >= რამე რიცხვზე

i-- - Stap Condition აკლდება 1

*********** using with  str ***********

let word = "Hello";

for (let i = 0; i < word.length; i++) {
  console.log(word[i]);
}
*/

// 1)

for (let i = 5; i <= 10; i++) {
  console.log(i);
}

// 2)
for (let i = 3; i >= 0; i--) {
  console.log(i);
}

// 3)

for (let i = 0; i < vacationSpots.length; i++) {
  console.log('I would love to visit ' + vacationSpots[i]);
}












// **************** CW ****************

// 1) დაწერეთ for loop-ი, რომელიც 10-დან 1-ის ჩათვლით დაითვლის რიცხვებს.
// 2) დაწერეთ for loop-ი, რომელიც გადაუვლის თქვენი საყვარელი ფილმების მასივს 
// და გამოიტანს მის თითოეულ ელემენტს. (მასივში მინიმუმ 5 ელემენტი უნდა ინახებოდეს.)


// 1)
for (let i = 10; i >= 1; i--) {
    console.log(i);
}

// 2) 
let films = ["The 100", "Avatar", "Spider-Man: No Way Home", "Avengers", "Scream"];

for (let i = 0; i < films.length; i++) {
    console.log(films[i]);
}