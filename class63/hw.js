/*

for loop - გამოიყენება ერთი და იგივე კოდის რამდენჯერმე შესასრულებლად. 
მას გადაეცემა 3 არგუმენტი 
1) ცვლადი საიდანაც ათვლა იწყება 
2) სად უნდა გაჩერდეს ლუპი
3) რამდენი უნდა მოემატოს თითვეულ იტერაციაზე

*/

// 3)

for(let i = 25; i <= 30; i++){
    console.log(i)
}

// 4)

for(let x = 90; x <= 102; x +=2){
    console.log(x)
}


// 5)

for(let y = 90; y >= 50; y--){
    console.log(y)
}

// 6)

for(let z = 40; z >= 20; z-=5){
    console.log(z)
}

// 7)

let name = "Mari";

for (let i = 0; i < name.length; i++) {
    console.log(i, name[i]);
}


// 8)
// length გვიჩვენებს სტრინგში ან მასივში ელემენტების რაოდენობას. 
// for loop-ში მისი გამოყენება საჭიროა იმისთვის, რომ ციკლმა ყველა ელემენტზე 
// გადაიაროს და ბოლო ინდექსს არ გასცდეს.


// 9)

let numbers = [1, 2, 3, 4, 5];

for (let i = 0; i < numbers.length; i++) {
    console.log("Number:", numbers[i]);
}